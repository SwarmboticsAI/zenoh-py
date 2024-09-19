import sys
import os
import logging
import traceback

# Add the directory containing the generated proto files to the Python path
proto_dir = os.path.join(os.path.dirname(__file__), 'proto')
sys.path.append(proto_dir)

import asyncio
import random
import time
from google.protobuf import timestamp_pb2
from zenoh import Session, Config

# Import the generated protobuf classes
from proto.discovery_heartbeat_pb2 import DiscoveryHeartbeat
from proto.cortex_state_update_pb2 import CortexStateUpdate, State
from proto.transform_stamped_pb2 import TransformStamped
from proto.header_pb2 import Header
from proto.transform_pb2 import Transform
from proto.vector3_pb2 import Vector3
from proto.quaternion_pb2 import Quaternion
from proto.time_pb2 import Time

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

async def publish_heartbeat(session, robot_id):
    key = f"ants/discovery_heartbeat"
    try:
        publisher = session.declare_publisher(key)
        logging.info(f"Publisher declared for robot_{robot_id}")
    except Exception as e:
        logging.error(f"Failed to declare publisher for robot_{robot_id}: {e}")
        return

    while True:
        try:
            heartbeat = DiscoveryHeartbeat()
            heartbeat.robot_id = f"robot_{robot_id}"
            heartbeat.ip_address = f"10.0.{robot_id}.1"
            
            heartbeat.state.new_state = State.TELEOP
            
            heartbeat.pose.header.frame_id = "map"
            current_time = time.time()
            heartbeat.pose.header.stamp.sec = int(current_time)
            heartbeat.pose.header.stamp.nanosec = int((current_time - int(current_time)) * 1e9)
            heartbeat.pose.child_frame_id = f"robot_{robot_id}"
            heartbeat.pose.transform.translation.x = random.uniform(-10, 10)
            heartbeat.pose.transform.translation.y = random.uniform(-10, 10)
            heartbeat.pose.transform.translation.z = 0
            heartbeat.pose.transform.rotation.w = 1

            serialized_data = heartbeat.SerializeToString()
            publisher.put(serialized_data)
            
            logging.info(f"Published heartbeat for robot_{robot_id}: x={heartbeat.pose.transform.translation.x:.2f}, y={heartbeat.pose.transform.translation.y:.2f}")
        except Exception as e:
            logging.error(f"Error publishing heartbeat for robot_{robot_id}: {e}")
            traceback.print_exc()

        if random.random() < 0.1:  # 10% chance of "missing" a publish
            delay = random.uniform(0.5, 5)
            logging.warning(f"robot_{robot_id} simulating network issue. Delaying for {delay:.2f} seconds")
            await asyncio.sleep(delay)
        else:
            await asyncio.sleep(0.25)  # Normal 250ms interval

async def main():
    num_robots = input("Enter the number of robots (default is 5): ")
    num_robots = int(num_robots) if num_robots.isdigit() else 5

    logging.info(f"Starting heartbeat publisher for {num_robots} robots")

    try:
        session = Session(Config())
        logging.info("Zenoh session created successfully")
    except Exception as e:
        logging.error(f"Failed to create Zenoh session: {e}")
        return

    tasks = []
    for robot_id in range(300, num_robots + 300):
        start_delay = random.uniform(0, 3)
        logging.info(f"robot_{robot_id} will start in {start_delay:.2f} seconds")
        await asyncio.sleep(start_delay)
        task = asyncio.create_task(publish_heartbeat(session, robot_id))
        tasks.append(task)
    
    print(f"Publishing heartbeats for {num_robots} robots. Press Enter to stop...")
    await asyncio.get_event_loop().run_in_executor(None, input)
    
    logging.info("Stopping heartbeat publishers")
    for task in tasks:
        task.cancel()
    
    await asyncio.gather(*tasks, return_exceptions=True)
    
    session.close()
    logging.info("Zenoh session closed. Exiting.")

if __name__ == "__main__":
    asyncio.run(main())