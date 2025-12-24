import difflib
import re

# Canonical scientist names
KNOWN_NAMES = {
    "max planck": "Max Planck",
    "james clerk maxwell": "James Clerk Maxwell",
    "mahatma gandhi": "Mahatma Gandhi",
    "albert einstein": "Albert Einstein",
    "isaac newton": "Isaac Newton",
    "nikola tesla": "Nikola Tesla",
    "c. v. raman": "C. V. Raman",
}

# Common phonetic / spelling mistakes
ALIASES = {
    "plank": "planck",
    "maxwell": "maxwell",
    "planck maxwell": None,   # ambiguous on purpose
}

def normalize_name(name: str):
    name = name.lower().strip()

    # Fix phonetic words
    words = name.split()
    fixed_words = [ALIASES.get(w, w) for w in words]
    fixed = " ".join(fixed_words)

    # Detect merged scientists
    if "planck" in fixed and "maxwell" in fixed:
        return {
            "ambiguous": True,
            "options": ["Max Planck", "James Clerk Maxwell"]
        }

    # Handle initials like "c v raman"
    if re.match(r"^([a-z]\s)+[a-z]+$", fixed):
        parts = fixed.split()
        initials = ". ".join(p.upper() for p in parts[:-1]) + "."
        surname = parts[-1].capitalize()
        return f"{initials} {surname}"

    match = difflib.get_close_matches(
        fixed,
        KNOWN_NAMES.keys(),
        n=1,
        cutoff=0.7
    )

    if match:
        return KNOWN_NAMES[match[0]]

    return fixed
