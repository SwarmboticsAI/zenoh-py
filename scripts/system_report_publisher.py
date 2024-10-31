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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Predefined system reports
SYSTEM_REPORTS = {
    1: {
        "robot_id": "robot_300",
        "alerts": [
            {
                "severity": "ERROR",
                "subsystem_name": "Navigation",
                "node_name": "path_planner",
                "alert_message": "Failed to generate valid path"
            }
        ]
    },
    2: {
        "robot_id": "robot_300", 
        "alerts": [
            {
                "severity": "WARNING",
                "subsystem_name": "Power",
                "node_name": "battery_monitor",
                "alert_message": "Battery below 20%"
            },
            {
                "severity": "INFO",
                "subsystem_name": "Power",
                "node_name": "battery_monitor", 
                "alert_message": "Charging station detected nearby"
            }
        ]
    },
    3: {
        "robot_id": "robot_300",
        "alerts": [
            {
                "severity": "CRITICAL",
                "subsystem_name": "Motors",
                "node_name": "motor_controller",
                "alert_message": "Motor controller overheating"
            },
            {
                "severity": "ERROR",
                "subsystem_name": "Motors", 
                "node_name": "motor_controller",
                "alert_message": "Emergency stop activated"
            }
        ]
    }
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

async def main():
    try:
        session = zenoh.open(zenoh.Config())
        logging.info("Zenoh session created successfully")
        
        while True:
            print("\nAvailable System Reports:")
            for num in SYSTEM_REPORTS:
                robot = SYSTEM_REPORTS[num]["robot_id"]
                alerts = len(SYSTEM_REPORTS[num]["alerts"])
                print(f"{num}: {robot} ({alerts} alerts)")
            
            try:
                selection = int(input("\nEnter report number (0 to exit): "))
                if selection == 0:
                    break
                await publish_report(session, selection)
            except ValueError:
                print("Please enter a valid number")
                
        session.close()
        logging.info("Zenoh session closed")
        
    except Exception as e:
        logging.error(f"Session error: {e}")

if __name__ == "__main__":
    asyncio.run(main())