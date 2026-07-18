import requests


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
    }