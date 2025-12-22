from core.system_access import get_cpu_usage, get_memory_usage


class SentinelAI:
    name = "sentinel"

    def respond(self, text: str):
        t = text.lower()

        if "cpu" in t:
            return "🛡️ Sentinel — CPU STATUS:\n" + get_cpu_usage()

        if "memory" in t or "ram" in t:
            return "🛡️ Sentinel — MEMORY STATUS:\n" + get_memory_usage()

        if "monitor" in t:
            return "🛡️ Sentinel: System monitoring active."

        return "🛡️ Sentinel: Standing by."


ai = SentinelAI()
