import difflib

COMMON_WORDS = [
    "seclude", "secluded", "seclusion",
    "stare", "marine", "photosynthesis",
    "gravity", "black hole"
]

def correct_word(word: str) -> str:
    matches = difflib.get_close_matches(
        word.lower(),
        COMMON_WORDS,
        n=1,
        cutoff=0.8
    )
    return matches[0] if matches else word
