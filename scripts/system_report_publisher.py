import sys
import logging
from pathlib import Path
import asyncio
import zenoh

# Add protos to path
root_dir = Path(__file__).parent.parent
proto_compiled_dir = root_dir / 'proto' / 'compiled'
sys.path.insert(0, str(proto_compiled_dir))

# Import generated protobuf classes
from sbai_system_alert_protos import system_report_pb2, system_alert_pb2
from sbai_geo_path_publisher_protos import geo_path_with_robot_id_pb2
from sbai_geographic_protos import geo_pose_stamped_pb2, geo_pose_pb2, geo_point_pb2
from sbai_std_protos import header_pb2
from sbai_geometry_protos import quaternion_pb2

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Predefined system reports
SYSTEM_REPORTS = {
    1: {
        "robot_id": "robot_300",
        "alerts": [
            {
                "severity": "I",
                "subsystem_name": "Navigation",
                "node_name": "path_planner",
                "alert_message": "nav:active:1234"
            }
        ]
    },
    2: {
        "robot_id": "robot_300", 
        "alerts": [
            {
                "severity": "I",
                "subsystem_name": "Navigation",
                "node_name": "path_planner",
                "alert_message": "nav:completed:1234"
            }
        ]
    },
    3: {
        "robot_id": "robot_300", 
        "alerts": [
            {
                "severity": "I",
                "subsystem_name": "Navigation",
                "node_name": "path_planner",
                "alert_message": "nav:canceled:1234"
            }
        ]
    },
    # 4: {
    #     "robot_id": "robot_300",
    #     "alerts": [
    #         {
    #             "severity": "E",
    #             "subsystem_name": "Navigation",
    #             "node_name": "path_planner",
    #             "alert_message": "nav:1234:problem"
    #         }
    #     ]
    # }
}

def create_system_report(config):
    report = system_report_pb2.SystemReport()
    report.robot_id = config["robot_id"]
    
    for alert_config in config["alerts"]:
        alert = report.alerts.add()
        alert.severity = alert_config["severity"]
        alert.subsystem_name = alert_config["subsystem_name"]
        alert.node_name = alert_config["node_name"]
        alert.alert_message = alert_config["alert_message"]
    
    return report

async def publish_report(session, report_num):
    if report_num not in SYSTEM_REPORTS:
        logging.error(f"Invalid report number: {report_num}")
        return

    topic = "tak/system_report"
    try:
        publisher = session.declare_publisher(topic)
        report = create_system_report(SYSTEM_REPORTS[report_num])
        serialized_data = report.SerializeToString()
        publisher.put(serialized_data)
        
        logging.info(f"Published system report {report_num} for {report.robot_id}")
        for alert in report.alerts:
            logging.info(f"- [{alert.severity}] {alert.subsystem_name}/{alert.node_name}: {alert.alert_message}")
            
    except Exception as e:
        logging.error(f"Failed to publish report: {e}")

GEO_PATH = {
    "robot_id": "robot_300",
    "geo_path": {
        "poses": [
            {
                "pose": {
                    "position": {
                        "latitude": "33.5933764",
                        "longitude": "-111.8541477",
                    }
                }
            },
            {
                "pose": {
                    "position": {
                        "latitude": "34.5933764",
                        "longitude": "-112.8541477",
                    }
                }
            }
        ]
    }
}

def create_geo_path(config):
    report = geo_path_with_robot_id_pb2.GeoPathWithRobotId()
    report.robot_id = config["robot_id"]
    
    for pose_config in config["geo_path"]["poses"]:
        poseStamped = report.geo_path.poses.add()
        pose = poseStamped.pose
        pose.position.latitude = float(pose_config["pose"]["position"]["latitude"])
        pose.position.longitude = float(pose_config["pose"]["position"]["longitude"])
    
    return report

async def publish_geopath(session):
    topic = "tak/geo_path"
    try:
        publisher = session.declare_publisher(topic)
        report = create_geo_path(GEO_PATH)
        serialized_data = report.SerializeToString()
        publisher.put(serialized_data)
        
        logging.info(f"Published geopath for {report.robot_id}")
        for pose in report.geo_path.poses:
            logging.info(f"- [{pose}]")
            
    except Exception as e:
        logging.error(f"Failed to publish report: {e}")

async def main():
    try:
        session = zenoh.open(zenoh.Config())
        logging.info("Zenoh session created successfully")
        
        while True:
            robot = "robot_300"

            print("\nAvailable System Reports:")
            print(f"1: {robot} - nav active")
            print(f"2: {robot} - nav completed")
            print(f"3: {robot} - nav canceled")
            # print(f"4: {robot} - nav error")
            print(f"9: {robot} - send single geopath")
            
            try:
                selection = int(input("\nEnter report number (0 to exit): "))
                if selection == 0:
                    break
                elif selection == 9:
                    await publish_geopath(session)
                else:
                    await publish_report(session, selection)
            except ValueError:
                print("Please enter a valid number")
                
        session.close()
        logging.info("Zenoh session closed")
        
    except Exception as e:
        logging.error(f"Session error: {e}")

if __name__ == "__main__":
    asyncio.run(main())