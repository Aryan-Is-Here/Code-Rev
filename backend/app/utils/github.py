import re


def parse_github_url(url: str):
    pattern = r"^https?://github\.com/([^/]+)/([^/]+)/?$"

    match = re.match(pattern, url)

    if not match:
        return None

    owner = match.group(1)
    repo = match.group(2)

    return owner, repo