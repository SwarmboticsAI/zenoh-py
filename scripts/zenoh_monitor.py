import zenoh
import time
import logging
import sys
from pathlib import Path
from google.protobuf import message

# Add the compiled protos directory to the Python path
root_dir = Path(__file__).parent.parent
proto_compiled_dir = root_dir / 'proto' / 'compiled'
sys.path.insert(0, str(proto_compiled_dir))

from sbai_tak_bridge_protos import state_update_request_pb2
from sbai_cortex_protos import cortex_state_update_pb2
from sbai_system_alert_protos import system_report_pb2, system_alert_pb2
from sbai_geo_path_publisher_protos import geo_path_with_robot_id_pb2
from sbai_geographic_protos import geo_pose_stamped_pb2, geo_pose_pb2, geo_point_pb2
from sbai_std_protos import header_pb2
from sbai_geometry_protos import quaternion_pb2
from sbai_behavior_protos import behavior_request_pb2
from sbai_tak_heartbeat_publisher_protos import to_tak_heartbeat_pb2

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def parse_protobuf(key: str, payload: bytes):
    """Attempt to parse different protobuf message types based on key"""
    try:
        if 'tak/to_tak_heartbeat' in key:
            msg = to_tak_heartbeat_pb2.ToTakHeartbeat()
            msg.ParseFromString(payload)
            return str(msg)
            
        elif 'tak/geo_path' in key:
            msg = geo_path_with_robot_id_pb2.GeoPath()
            msg.ParseFromString(payload)
            return str(msg)
            
        elif 'tak/system_report' in key:
            msg = system_report_pb2.SystemReport() 
            msg.ParseFromString(payload)
            return str(msg)
            
        elif '/behavior_requests' in key:
            msg = behavior_request_pb2.BehaviorRequest()
            msg.ParseFromString(payload)
            return str(msg)
        
        elif '/joy' in key:
            # msg = behavior_request_pb2.BehaviorRequest()
            # msg.ParseFromString(payload)
            return str("joy")

        return None
        
    except message.DecodeError:
        return None

def listener(sample):
    payload_bytes = bytes(sample.payload)
    
    # Try to parse as protobuf first
    parsed = parse_protobuf(str(sample.key_expr), payload_bytes)
    if parsed:
        logging.info(f"Key: {sample.key_expr}\nParsed Message:\n{parsed}")
        return

    # Fallback to raw display
    try:
        payload = payload_bytes.decode('utf-8')
    except:
        payload = payload_bytes.hex()
    
    logging.info(f"Key: {sample.key_expr}, Raw Payload: {payload}")

def main():
    session = zenoh.open(zenoh.Config())
    subscriber = session.declare_subscriber("**", listener)
    
    logging.info("Monitoring all Zenoh traffic. Press Ctrl+C to exit.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        subscriber.undeclare()
        session.close()

if __name__ == "__main__":
    main()