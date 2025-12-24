import requests

DICT_API = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

def fetch_definition(word: str) -> str | None:
    try:
        r = requests.get(DICT_API.format(word), timeout=8)
        if r.status_code != 200:
            return None

        data = r.json()
        meaning = data[0]["meanings"][0]
        definition = meaning["definitions"][0]["definition"]
        return definition
    except Exception:
        return None
