import json
from ollama import chat

def analyze_repository(prompt: str):
    response = chat(
        model="qwen2.5-coder:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    content = response["message"]["content"]

    print("\n========== RAW AI RESPONSE ==========\n")
    print(content)
    print("\n=====================================\n")

    content = content.replace("```json", "")
    content = content.replace("```", "").strip()

    return json.loads(content)