import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("Token loaded:", GITHUB_TOKEN is not None)
print("Token prefix:", GITHUB_TOKEN[:12] if GITHUB_TOKEN else None)

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN not found in .env")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}
 
def fetch_repository(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("GitHub Status Code:", response.status_code)
        print("GitHub Response:", response.text)
        return None

    data = response.json()

    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data["language"],
        "avatar": data["owner"]["avatar_url"],
        "html_url": data["html_url"],
        "updated_at": data["updated_at"],
    }
    
def fetch_languages(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return []

    data = response.json()

    languages = list(data.keys())

    return languages[:5]

def fetch_readme(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("GitHub Status Code:", response.status_code)
        print("GitHub Response:", response.text)
        return None

    data = response.json()

    content = base64.b64decode(
        data["content"]
    ).decode("utf-8")

    return content

def fetch_file_tree(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return []

    data = response.json()

    files = []

    for item in data["tree"]:
        if item["type"] == "blob":
            files.append(item["path"])

    return files