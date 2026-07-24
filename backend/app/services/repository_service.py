import time
from concurrent.futures import ThreadPoolExecutor

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
from app.utils.code_fetcher import fetch_important_code


def analyze_github_repository(owner: str, repo: str):

    total_start = time.perf_counter()

    # ---------------- GitHub Fetch ----------------
    github_start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=4) as executor:

        repository_future = executor.submit(
            fetch_repository,
            owner,
            repo,
        )

        languages_future = executor.submit(
            fetch_languages,
            owner,
            repo,
        )

        readme_future = executor.submit(
            fetch_readme,
            owner,
            repo,
        )

        file_tree_future = executor.submit(
            fetch_file_tree,
            owner,
            repo,
        )

        repository = repository_future.result()

        if repository is None:
            return None

        repository["languages"] = languages_future.result()

        readme = readme_future.result() or ""

        file_tree = file_tree_future.result()

    print(f"GitHub Fetch: {time.perf_counter() - github_start:.2f}s")

    # ---------------- Important Code ----------------
    code_start = time.perf_counter()

    important_code = fetch_important_code(
        owner,
        repo,
        file_tree,
    )

    print(f"Important Code Fetch: {time.perf_counter() - code_start:.2f}s")

    # ---------------- Repository Processing ----------------
    processing_start = time.perf_counter()

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

    print("\n===== IMPORTANT SOURCE FILES =====")

    for file in important_code:
        print(file)

    print("===============================\n")

    prompt = build_prompt(
        repository,
        readme,
        context,
        technology_info,
        important_code,
    )

    print(f"Repository Processing: {time.perf_counter() - processing_start:.2f}s")

    # ---------------- AI Analysis ----------------
    ai_start = time.perf_counter()

    # Comment these out after debugging
    print("\n===== PROMPT PREVIEW =====")
    print(prompt[:6000])
    print("==========================\n")

    analysis = analyze_repository(prompt)

    print(f"AI Analysis: {time.perf_counter() - ai_start:.2f}s")

    repository["analysis"] = analysis

    print(f"\nTOTAL TIME: {time.perf_counter() - total_start:.2f}s\n")

    return repository