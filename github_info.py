import requests
import json

def get_repo_contents(title):
    with open("config.json", "r") as f:
        config = json.load(f)
    owner = config['github']['owner']
    repo = config['github']['repo']
    headers = {
        "Authorization": f"token {config['github']['token']}"
    }

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    contents = response.json()
    problem = [item for item in contents if item['name'].endswith(title)]
    if not problem:
        print(f"{title} not exist")
        return None

    dir_url = problem[0]['url']
    dir_response = requests.get(dir_url, headers=headers)
    dir_response.raise_for_status()

    contents = dir_response.json()
    code_files = [item for item in contents if item['name'].endswith(('.cpp', '.py'))]
    if not code_files:
        print("not found files")
        return None
    file_url = code_files[0]['download_url']
    file_response = requests.get(file_url)
    file_response.raise_for_status()

    return file_response.text

if __name__ == '__main__':
    code = get_repo_contents( "making-a-large-island")
    print(code)
