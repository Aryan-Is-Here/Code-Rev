from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.utils.github import parse_github_url
from app.utils.github_api import (
    fetch_repository,
    fetch_languages,
    fetch_readme,
)
from app.ai.prompt import build_prompt
from app.ai.analyzer import analyze_repository

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    repo: str


@app.get("/")
def root():
    return {
        "message": "Welcome to Code-Rev API!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze_repo(request: RepoRequest):

    parsed = parse_github_url(request.repo)

    if parsed is None:
        return {
            "status": "error",
            "message": "Invalid GitHub repository URL."
        }

    owner, repo = parsed

    repository = fetch_repository(owner, repo)
    languages = fetch_languages(owner, repo)
    
    repository["languages"] = languages

    readme = fetch_readme(owner, repo)
    prompt = build_prompt(repository, readme)
    analysis = analyze_repository(prompt)

    print("\n========== AI PROMPT ==========\n")
    print(prompt[:1200])
    print("\n===============================\n")

    print("\n===== README Preview =====")
    print(readme[:500] if readme else "README not found")
    print("==========================\n")

    print("Repository returned:", repository)

    repository["analysis"] = analysis

    return repository