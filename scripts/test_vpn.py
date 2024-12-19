import zenoh
import time
from datetime import datetime

def listener(sample):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"{sample.key_expr} => Received at {current_time}")

# zenoh.init_log_from_env_or("debug")
config = zenoh.Config.from_file('config.json')

with zenoh.open(config=config) as session:
    with session.declare_subscriber('demo/example/**', listener) as subscriber:
        time.sleep(100000)
