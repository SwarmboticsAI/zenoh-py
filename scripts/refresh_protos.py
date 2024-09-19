import os
import requests
import subprocess
import logging
import shutil
from pathlib import Path

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

def get_github_token():
    try:
        result = subprocess.run(
            ['git', 'credential', 'fill'],
            input='url=https://github.com\n\n',
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if line.startswith('password='):
                    return line.split('=', 1)[1]
    except Exception as e:
        logging.error(f"Error getting GitHub token: {e}")
    raise ValueError("GitHub token not found. Please set up your Git credentials for GitHub.")

def download_file(url, target_path, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with open(target_path, 'wb') as f:
        f.write(response.content)

def get_contents(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def process_directory(api_url, local_dir, headers, base_path):
    contents = get_contents(api_url, headers)
    proto_files_count = 0

    for item in contents:
        if item['type'] == 'file' and item['name'].endswith('.proto'):
            file_url = item['download_url']
            file_path = local_dir / item['name']
            download_file(file_url, file_path, headers)
            proto_files_count += 1
        elif item['type'] == 'dir':
            subdir_api_url = item['url']
            subdir_name = item['name']
            if base_path:
                subdir_local_path = local_dir / subdir_name.replace(base_path, '', 1).lstrip('/')
            else:
                subdir_local_path = local_dir / subdir_name
            subdir_proto_count = process_directory(subdir_api_url, subdir_local_path, headers, base_path or subdir_name)
            if subdir_proto_count > 0:
                proto_files_count += subdir_proto_count

    return proto_files_count

def refresh_protos():
    repo_owner = "SwarmboticsAI"
    repo_name = "swarm"
    directory_path = "robot/ros2_interfaces"
    branch = "main"

    try:
        github_token = get_github_token()
    except ValueError as e:
        logging.error(f"Failed to get GitHub token: {e}")
        return

    root_dir = Path(__file__).parent.parent
    proto_def_dir = root_dir / 'proto' / 'def'

    # Delete the current contents of /def recursively
    if proto_def_dir.exists():
        shutil.rmtree(proto_def_dir)
        print(f"Deleted existing contents of {proto_def_dir}")

    # Recreate the empty /def directory
    proto_def_dir.mkdir(parents=True, exist_ok=True)

    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{directory_path}?ref={branch}"
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        total_proto_files = process_directory(api_url, proto_def_dir, headers, '')
        if total_proto_files == 0:
            logging.warning("No .proto files found in the specified directory and its subdirectories")
        else:
            print(f"Successfully downloaded {total_proto_files} .proto files")
    except requests.RequestException as e:
        logging.error(f"Error refreshing proto files: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    refresh_protos()