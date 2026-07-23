import requests
import base64

from app.utils.github_api import HEADERS


def fetch_file(owner: str, repo: str, path: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return None

    data = response.json()

    return base64.b64decode(
        data["content"]
    ).decode("utf-8")