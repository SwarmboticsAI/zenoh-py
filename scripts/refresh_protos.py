import os
import requests
import subprocess
from pathlib import Path

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
    except FileNotFoundError:
        pass

    raise ValueError("GitHub token not found. Please set up your Git credentials for GitHub.")

def download_file(url, target_path, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(target_path, 'wb') as f:
        f.write(response.content)

def refresh_protos():
    # Configuration
    repo_owner = "SwarmboticsAI"
    repo_name = "swarm"
    directory_path = "robot/ros2_interfaces"
    branch = "main"

    # Get GitHub token
    github_token = get_github_token()

    # Define paths
    root_dir = Path(__file__).parent.parent
    proto_def_dir = root_dir / 'proto' / 'def'

    # Ensure the proto definition directory exists
    proto_def_dir.mkdir(parents=True, exist_ok=True)

    # GitHub API URL
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{directory_path}?ref={branch}"

    # Set up headers for authentication
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        # Get the directory contents
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        contents = response.json()

        # Download each .proto file
        for item in contents:
            if item['type'] == 'file' and item['name'].endswith('.proto'):
                file_url = item['download_url']
                file_path = proto_def_dir / item['name']
                download_file(file_url, file_path, headers)
                print(f"Downloaded: {item['name']}")

        print("Proto files refreshed successfully.")

    except requests.RequestException as e:
        print(f"Error refreshing proto files: {e}")

if __name__ == "__main__":
    refresh_protos()