import sys
import os
from pathlib import Path
import logging
import traceback
import asyncio
import random
import time
import zenoh

# Add the compiled protos directory to the Python path
root_dir = Path(__file__).parent.parent
proto_compiled_dir = root_dir / 'proto' / 'compiled'
sys.path.insert(0, str(proto_compiled_dir))

# Import the generated protobuf classes
from sbai_tak_heartbeat_publisher_protos import to_tak_heartbeat_pb2
from sbai_cortex_protos import cortex_state_update_pb2
from sbai_geometry_protos import pose_stamped_pb2, pose_pb2, vector3_pb2, quaternion_pb2
from sbai_std_protos import header_pb2
from sbai_builtin_protos import time_pb2
from sbai_geographic_protos import geo_point_pb2

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

async def publish_heartbeat(session, robot_id, allow_lost_connections):
    key = "tak/to_tak_heartbeat"
    try:
        publisher = session.declare_publisher(key)
    except Exception as e:
        logging.error(f"Failed to declare publisher for robot_{robot_id}: {e}")
        return

    # Initialize random state and position
    current_state = random.choice(list(cortex_state_update_pb2.CortexState.values()))
    current_latitude = 33.5933764 + random.uniform(-0.0002307, 0.0002307)
    current_longitude = -111.8541477 + random.uniform(-0.0002307, 0.0002307)
    last_state_change = time.time()

    while True:
        try:
            # Check if 10 seconds have passed to potentially change state
            current_time = time.time()
            if current_time - last_state_change > 10 and random.random() < 0.2:  # 20% chance every 10 seconds
                current_state = random.choice(list(cortex_state_update_pb2.CortexState.values()))
                last_state_change = current_time

            # Slightly adjust lat/long to simulate movement
            current_latitude += random.uniform(-0.000005, 0.000005)
            current_longitude += random.uniform(-0.000005, 0.000005)

            heartbeat = to_tak_heartbeat_pb2.ToTakHeartbeat()
            heartbeat.robot_id = f"robot_{robot_id}"
            heartbeat.ip_address = f"192.168.0.143"
            heartbeat.state.new_state = current_state

            heartbeat.gps_coordinate.latitude = current_latitude
            heartbeat.gps_coordinate.longitude = current_longitude
            heartbeat.gps_coordinate.altitude = random.uniform(0, 100)

            heartbeat.magnetic_heading_deg = 45
            heartbeat.battery_percentage = 66.0
            heartbeat.body_speed_m_per_s = 1.0

            heartbeat.platform_type = "haul_ant"
            heartbeat.is_parking_brake_engaged.value = True

            serialized_data = heartbeat.SerializeToString()
            publisher.put(serialized_data)
            
            logging.info(f"Robot_{robot_id}: state={cortex_state_update_pb2.CortexState.Name(current_state)}:{current_state}, lat={current_latitude:.7f}, lon={current_longitude:.7f}")

        except Exception as e:
            logging.error(f"Error publishing heartbeat for robot_{robot_id}: {e}")
            traceback.print_exc()

        if allow_lost_connections and random.random() < 0.1:  # 10% chance of "missing" a publish
            delay = random.uniform(5, 15)
            await asyncio.sleep(delay)
        else:
            await asyncio.sleep(0.25)  # Normal 250ms interval

async def main():
    num_robots = input("Enter the number of robots (default is 1): ")
    num_robots = int(num_robots) if num_robots.isdigit() else 1

    allow_lost_connections = input("Allow lost connections? y/N: ")
    allow_lost_connections = allow_lost_connections.lower() == "y"
    logging.info(f"should lose connection = {allow_lost_connections}")
    logging.info(f"Starting heartbeat publisher for {num_robots} robots")

    try:
        session = zenoh.open(zenoh.Config())
        logging.info("Zenoh session created successfully")
    except Exception as e:
        logging.error(f"Failed to create Zenoh session: {e}")
        return

    tasks = []
    for robot_id in range(300, num_robots + 300):
        start_delay = random.uniform(0, 3)
        logging.info(f"robot_{robot_id} will start in {start_delay:.2f} seconds")
        await asyncio.sleep(start_delay)
        task = asyncio.create_task(publish_heartbeat(session, robot_id, allow_lost_connections))
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