import requests

def search_web(query: str) -> str | None:
    """
    Fetch short explanation from DuckDuckGo Instant Answer API
    """
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            "q": query,
            "format": "json",
            "no_html": 1,
            "skip_disambig": 1
        }

        res = requests.get(url, params=params, timeout=5)
        data = res.json()

        if data.get("AbstractText"):
            return data["AbstractText"]

        # fallback: related topics
        related = data.get("RelatedTopics", [])
        if related and isinstance(related, list):
            first = related[0]
            if isinstance(first, dict) and first.get("Text"):
                return first["Text"]

    except Exception:
        pass

    return None
