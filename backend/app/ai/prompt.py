def build_prompt(
    repository: dict,
    readme: str,
):
    prompt = f"""
You are a senior software engineer.

Analyze the following GitHub repository.

Repository Name:
{repository["owner"]}/{repository["name"]}

Description:
{repository["description"]}

Primary Language:
{repository["language"]}

Languages:
{", ".join(repository["languages"])}

README:
{readme[:4000]}

Provide:

1. A short summary
2. Three strengths
3. Three potential improvements
4. A code quality score out of 100

Return the answer in clear markdown.
"""

    return prompt