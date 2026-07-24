from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.utils.github import parse_github_url
from app.services.repository_service import analyze_github_repository

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

    repository = analyze_github_repository(owner, repo)

    if repository is None:
        return {
            "status": "error",
            "message": "Repository not found."
        }

    return repository