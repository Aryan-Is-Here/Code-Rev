IMPORTANT_FILES = {
    "package.json",
    "requirements.txt",
    "pyproject.toml",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "vite.config.ts",
    "vite.config.js",
    "next.config.js",
    "tsconfig.json",
    "tailwind.config.js",
    "tailwind.config.ts",
    "Dockerfile",
    "docker-compose.yml",
}


def build_repository_context(file_tree: list[str]):
    important_files = set()

    directories = set()

    for path in file_tree:

        filename = path.split("/")[-1]

        if filename in IMPORTANT_FILES:
            important_files.add(filename)

        IGNORED_DIRECTORIES = {
            ".github",
            ".vscode",
            ".devcontainer",
            ".config",
            ".agents",
        }

        if "/" in path:
            directory = path.split("/")[0]

            if directory not in IGNORED_DIRECTORIES:
                directories.add(directory)

    return {
        "important_files": sorted(important_files),
        "directories": sorted(directories),
    }