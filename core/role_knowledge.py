ROLE_HOLDERS = {
    "education minister of tamil nadu": "Anbil Mahesh Poyyamozhi",
    "school education minister of tamil nadu": "Anbil Mahesh Poyyamozhi",
    "chief minister of tamil nadu": "M. K. Stalin",
    "prime minister of india": "Narendra Modi",
}

def get_role_holder(role: str):
    return ROLE_HOLDERS.get(role.lower())
