import zenoh
import time
import logging
import sys
from pathlib import Path

# Add the compiled protos directory to the Python path
root_dir = Path(__file__).parent.parent
proto_compiled_dir = root_dir / 'proto' / 'compiled'
sys.path.insert(0, str(proto_compiled_dir))

from sbai_tak_bridge_protos import state_update_request_pb2
from sbai_cortex_protos import cortex_state_update_pb2

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def listener(sample):
    state_update = state_update_request_pb2.StateUpdateRequest()
    state_update.ParseFromString(sample.payload)
    logging.info(f"Received StateUpdateRequest: {cortex_state_update_pb2.CortexState.Name(state_update.requested_state)} :: {sample.key_expr}")

def main():
    # Initialize Zenoh session
    session = zenoh.open(zenoh.Config())

    # Create a subscriber
    subscriber = session.declare_subscriber("ants/*/state_update_request", listener)

    logging.info("Subscribed to ants/*/state_update_request. Press Ctrl+C to exit.")

    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up
        subscriber.undeclare()
        session.close()

if __name__ == "__main__":
    main()