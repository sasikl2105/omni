import requests

def fetch_role_holder(role: str):
    """
    Fetch role holder from Wikipedia summary
    Example role: 'president of pakistan'
    """
    try:
        query = role.replace(" ", "_")
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        r = requests.get(url, timeout=5)

        if r.status_code != 200:
            return None

        data = r.json()
        extract = data.get("extract")

        if not extract:
            return None

        # Return first sentence (usually name)
        return extract.split(".")[0]

    except:
        return None
