def build_prompt(
    repository: dict,
    readme: str,
    context: dict,
    technology_info: dict,
):
    prompt = f"""
You are a senior software engineer reviewing a GitHub repository.

Analyze the repository using ONLY the information provided below.

Repository:
{repository["owner"]}/{repository["name"]}

Description:
{repository["description"]}

Primary Language:
{repository["language"]}

Languages:
{", ".join(repository["languages"])}

Detected Technologies:
{", ".join(technology_info["technologies"])}

Detected Features:
{", ".join(technology_info["features"])}

Important Files:
{chr(10).join(context["important_files"])}

Project Directories:
{chr(10).join(context["directories"])}

README:
{readme[:4000]}

Instructions:

- Explain what this repository appears to be.
- Base every conclusion only on the information above.
- Mention repository-specific strengths whenever possible.
- Suggest realistic improvements.
- Avoid generic advice unless supported by the repository context.
- Give an overall quality score between 0 and 100.

Return ONLY valid JSON.

Do NOT write markdown.
Do NOT use triple backticks.

Return exactly this format:

{{
    "summary": "string",
    "strengths": [
        "string",
        "string",
        "string"
    ],
    "improvements": [
        "string",
        "string",
        "string"
    ],
    "score": 90
}}
"""
    return prompt