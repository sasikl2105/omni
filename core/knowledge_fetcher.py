import requests

WIKI_API = "https://en.wikipedia.org/api/rest_v1/page/summary/{}"

HEADERS = {
    "User-Agent": "JarvisAI/1.0 (learning-bot; contact: local)"
}

def fetch_knowledge(topic: str) -> str | None:
    try:
        topic = topic.strip().replace(" ", "_")
        url = WIKI_API.format(topic)

        r = requests.get(url, headers=HEADERS, timeout=8)
        if r.status_code != 200:
            return None

        data = r.json()

        extract = data.get("extract")
        if not extract:
            return None

        # Keep first paragraph only
        return extract.split("\n")[0]

    except Exception:
        return None
