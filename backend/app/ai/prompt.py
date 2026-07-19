def build_prompt(
    repository: dict,
    readme: str,
    context: dict,
):
    prompt = f"""
You are a senior software engineer performing a professional code review.

Analyze the following GitHub repository using ONLY the information provided.

Repository Name:
{repository["owner"]}/{repository["name"]}

Description:
{repository["description"]}

Primary Language:
{repository["language"]}

Languages:
{", ".join(repository["languages"])}

Important Files:
{chr(10).join(context["important_files"])}

Project Directories:
{chr(10).join(context["directories"])}

README:
{readme[:4000]}

Instructions:

- Identify what kind of software this repository is.
- Base your observations on the repository metadata, README, languages, important files, and directory structure.
- Avoid generic advice that could apply to every project.
- Mention repository-specific strengths whenever possible.
- Suggest realistic improvements based on the available context.
- Give a score between 0 and 100.

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