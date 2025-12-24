TITLES = {
    "super star": "rajinikanth",
    "superstar": "rajinikanth",
    "thala": "ajith kumar",
    "thalapathy": "vijay",
    "megastar": "chiranjeevi",
    "ulaganayagan": "kamal haasan"
}

def resolve_title(text: str):
    text = text.lower()
    for title, person in TITLES.items():
        if title in text:
            return person
    return None
