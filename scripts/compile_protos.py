import os
import subprocess
from pathlib import Path

def compile_protos():
    root_dir = Path(__file__).parent.parent
    proto_def_dir = root_dir / 'proto' / 'def'
    proto_compiled_dir = root_dir / 'proto' / 'compiled'

    # Create the compiled directory if it doesn't exist
    proto_compiled_dir.mkdir(parents=True, exist_ok=True)

    # Find all .proto files recursively
    proto_files = list(proto_def_dir.rglob('*.proto'))

    if not proto_files:
        print("No .proto files found in the def/ directory.")
        return

    # Compile each .proto file
    for proto_file in proto_files:
        relative_path = proto_file.relative_to(proto_def_dir)
        output_dir = proto_compiled_dir / relative_path.parent

        # Create the output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        # Construct the protoc command
        cmd = [
            'protoc',
            f'--proto_path={proto_def_dir}',
            f'--python_out={proto_compiled_dir}',
            str(proto_file)
        ]

        # Run the protoc command
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"Compiled: {relative_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error compiling {relative_path}:")
            print(f"Command: {' '.join(cmd)}")
            print(f"Error output: {e.stderr}")

    print("Proto compilation completed.")

if __name__ == "__main__":
    compile_protos()