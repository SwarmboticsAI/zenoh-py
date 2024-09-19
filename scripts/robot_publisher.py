import sys
import os
import zenoh
import time
import random

# Add the directory containing the compiled proto files to the Python path
proto_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'proto', 'compiled')
sys.path.append(proto_dir)

# Import the generated protobuf classes
from sbai_swarm_discovery_protos.discovery_heartbeat_pb2 import DiscoveryHeartbeat
from sbai_cortex_protos.cortex_state_update_pb2 import State
from sbai_geometry_protos.transform_stamped_pb2 import TransformStamped
from sbai_geometry_protos.transform_pb2 import Transform
from sbai_geometry_protos.vector3_pb2 import Vector3
from sbai_geometry_protos.quaternion_pb2 import Quaternion
from sbai_geographic_protos.geo_point_pb2 import GeoPoint

def generate_random_heartbeat(robot_id):
    heartbeat = DiscoveryHeartbeat()
    
    heartbeat.robot_id = f"robot_{robot_id}"
    heartbeat.ip_address = f"10.0.{robot_id}.1"
    
    heartbeat.state.new_state = random.choice(list(State.values()))
    
    heartbeat.pose.header.frame_id = "map"
    current_time = time.time()
    heartbeat.pose.header.stamp.sec = int(current_time)
    heartbeat.pose.header.stamp.nanosec = int((current_time - int(current_time)) * 1e9)
    heartbeat.pose.child_frame_id = f"robot_{robot_id}"
    heartbeat.pose.transform.translation.x = random.uniform(-10, 10)
    heartbeat.pose.transform.translation.y = random.uniform(-10, 10)
    heartbeat.pose.transform.translation.z = 0
    heartbeat.pose.transform.rotation.w = 1
    
    heartbeat.gps_coordinate.latitude = random.uniform(-90, 90)
    heartbeat.gps_coordinate.longitude = random.uniform(-180, 180)
    heartbeat.gps_coordinate.altitude = random.uniform(0, 1000)
    
    return heartbeat

def main():
    # Initialize zenoh session
    session = zenoh.open()

    # Declare the publisher
    publisher = session.declare_publisher("ants/discovery_heartbeat")

    robot_id = random.randint(1, 999)

    try:
        while True:
            # Generate random heartbeat
            heartbeat = generate_random_heartbeat(robot_id)
            
            # Serialize the message to Protocol Buffers
            serialized_message = heartbeat.SerializeToString()
            
            # Publish the serialized message
            publisher.put(serialized_message)
            print(f"Published heartbeat for robot_{robot_id} (size: {len(serialized_message)} bytes)")
            
            # Wait for 2 seconds
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    main()