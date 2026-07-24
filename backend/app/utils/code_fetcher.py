from app.utils.file_fetcher import fetch_file

IMPORTANT_FILES = {
    "package.json",
    "requirements.txt",
    "Cargo.toml",
    "pom.xml",
    "Dockerfile",
    "docker-compose.yml",
    "vite.config.ts",
    "next.config.js",
}

IMPORTANT_SOURCE = {
    "src/main.py",
    "src/app.py",
    "src/main.ts",
    "src/main.tsx",
    "src/App.tsx",
    "src/App.jsx",
    "src/index.ts",
    "src/index.js",
    "main.py",
    "main.cpp",
    "main.java",
}


def fetch_important_code(owner, repo, file_tree):

    files = {}

    for path in file_tree:

        if path in IMPORTANT_SOURCE:
            content = fetch_file(owner, repo, path)
            if content:
                files[path] = content[:3000]

        elif "/" not in path and path in IMPORTANT_FILES:
            content = fetch_file(owner, repo, path)
            if content:
                files[path] = content[:3000]

    return files