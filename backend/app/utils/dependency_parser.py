import json


def parse_package_json(content: str):
    if content is None:
        return None

    try:
        data = json.loads(content)

        dependencies = list(
            data.get("dependencies", {}).keys()
        )

        dev_dependencies = list(
            data.get("devDependencies", {}).keys()
        )

        peer_dependencies = list(
            data.get("peerDependencies", {}).keys()
        )

        return {
            "name": data.get("name"),
            "dependencies": dependencies[:15],
            "dev_dependencies": dev_dependencies[:15],
            "peer_dependencies": peer_dependencies[:15],
        }

    except Exception:
        return None