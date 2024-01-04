import requests
import os

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'token {TOKEN}'}

def get_pull_requests(state):
    url = f"https://api.github.com/repos/boto/boto3/pulls?state={state}&per_page=100"
    response = requests.get(url, headers=HEADERS)
    pull_requests = []

    if response.status_code == 200:
        for pr in response.json():
            pull_requests.append({
                "title": pr["title"],
                "num": pr["number"],
                "link": pr["html_url"]
            })
    else:
        print(f"Failed to fetch data from GitHub API: Status {response.status_code}")

    return pull_requests
