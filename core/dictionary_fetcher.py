# core/dictionary_fetcher.py
# Dictionary lookup engine for OMNI

import requests


def lookup_word(word: str) -> str | None:
    word = word.lower().strip()

    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        r = requests.get(url, timeout=5)

        if r.status_code != 200:
            return None

        data = r.json()
        meanings = data[0].get("meanings", [])

        if not meanings:
            return None

        definitions = meanings[0].get("definitions", [])
        if not definitions:
            return None

        return definitions[0].get("definition")

    except Exception:
        return None
