import os
import json

from dotenv import load_dotenv
from ollama import chat

load_dotenv()
MODEL_NAME = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:3b")
print(f"\nUsing Ollama model: {MODEL_NAME}\n")

def analyze_repository(prompt: str):
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format="json",
        options={
            "temperature": 0,
        },
    )

    content = response["message"]["content"]

    print("\n========== RAW AI RESPONSE ==========\n")
    print(content)
    print("\n=====================================\n")

    data = json.loads(content)

    required_keys = {
        "summary",
        "strengths",
        "improvements",
        "score",
    }

    missing = required_keys - set(data.keys())

    if missing:
        raise ValueError(f"Missing keys: {missing}")

    return data