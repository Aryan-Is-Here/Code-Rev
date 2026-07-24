from app.utils.github_api import (
    fetch_repository,
    fetch_languages,
    fetch_readme,
    fetch_file_tree,
)

from app.utils.file_fetcher import fetch_file
from app.utils.dependency_parser import parse_package_json

from app.ai.context_builder import build_repository_context
from app.ai.technology_detector import detect_technologies
from app.ai.prompt import build_prompt
from app.ai.analyzer import analyze_repository


def analyze_github_repository(owner: str, repo: str):

    repository = fetch_repository(owner, repo)

    if repository is None:
        return None

    repository["languages"] = fetch_languages(owner, repo)

    readme = fetch_readme(owner, repo) or ""

    file_tree = fetch_file_tree(owner, repo)

    context = build_repository_context(file_tree)

    technology_info = detect_technologies(file_tree)

    package_json = fetch_file(owner, repo, "package.json")

    package_info = parse_package_json(package_json)

    print("\n===== TECHNOLOGY DETECTOR =====")
    print(technology_info)
    print("===============================\n")

    print("\n===== PACKAGE INFO =====")
    print(package_info)
    print("========================\n")

    prompt = build_prompt(
        repository,
        readme,
        context,
        technology_info,
    )

    analysis = analyze_repository(prompt)

    repository["analysis"] = analysis

    return repository