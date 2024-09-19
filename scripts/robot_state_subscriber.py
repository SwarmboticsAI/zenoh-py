import zenoh
from state_update_request_pb2 import StateUpdateRequest, State
import time

def listener(sample):
    state_update = StateUpdateRequest()
    state_update.ParseFromString(sample.payload)
    print(f"Received StateUpdateRequest: {State.Name(state_update.requested_state)}")

def main():
    # Initialize Zenoh session
    session = zenoh.open()

    # Create a subscriber
    subscriber = session.declare_subscriber("state/updates", listener)

    print("Subscribed to state/updates. Press Ctrl+C to exit.")

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