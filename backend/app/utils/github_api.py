import requests
import base64

def fetch_repository(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code != 200:
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

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    languages = list(data.keys())

    return languages[:5]

def fetch_readme(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    content = base64.b64decode(
        data["content"]
    ).decode("utf-8")

    return content