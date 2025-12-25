# core/role_knowledge.py
# Canonical role → person mapping (LOWERCASE KEYS ONLY)

ROLE_HOLDERS = {
    "president of india": "Droupadi Murmu",
    "prime minister of india": "Narendra Modi",
    "chief minister of tamil nadu": "M. K. Stalin",
    "education minister of tamil nadu": "Anbil Mahesh Poyyamozhi",
    "school education minister of tamil nadu": "Anbil Mahesh Poyyamozhi",

    # Optional (if you want)
    "president of america": "Joe Biden",
    "president of united states": "Joe Biden",
}

def get_role_holder(role: str):
    return ROLE_HOLDERS.get(role.lower())
