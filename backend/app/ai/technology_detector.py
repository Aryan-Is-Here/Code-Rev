def detect_technologies(file_tree: list[str]):
    technologies = set()
    features = set()

    files = set(file_tree)

    # Languages / Frameworks
    if any(path.endswith("package.json") for path in files):
        technologies.add("Node.js")

    if any(path.endswith("requirements.txt") for path in files):
        technologies.add("Python")

    if any(path.endswith("pyproject.toml") for path in files):
        technologies.add("Python")

    if any(path.endswith("Cargo.toml") for path in files):
        technologies.add("Rust")

    if any(path.endswith("go.mod") for path in files):
        technologies.add("Go")

    if any(path.endswith("pom.xml") for path in files):
        technologies.add("Java (Maven)")

    if any(path.endswith("build.gradle") for path in files):
        technologies.add("Java (Gradle)")

    # Infrastructure
    if any(path.endswith("Dockerfile") for path in files):
        features.add("Docker")

    if any(path.endswith("docker-compose.yml") for path in files):
        features.add("Docker Compose")

    if any(path.startswith(".github/workflows") for path in files):
        features.add("GitHub Actions")

    if any(
        path.startswith("test")
        or "/test/" in path
        or path.startswith("tests")
        or "/tests/" in path
        for path in files
    ):
        features.add("Automated Tests")

    if any(
        path.startswith("docs/")
        or "/docs/" in path
        for path in files
    ):
        features.add("Documentation")

    return {
        "technologies": sorted(technologies),
        "features": sorted(features),
    }