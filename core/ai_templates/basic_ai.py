class BaseAI:
    def __init__(self, config):
        self.name = config.get("name", "unknown")
        self.abilities = config.get("abilities", [])
        self.permissions = config.get("permissions", [])
        self.locked = config.get("locked", True)

    def respond(self, text: str) -> str:
        raise NotImplementedError("AI must implement respond()")
