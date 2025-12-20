# core/advanced_brain.py
# Studentbae++ / GamkersGPT intelligence layer
# EXPLANATION ONLY — NO EXECUTION

def explain_tool(tool: str) -> str:
    tool = tool.lower()

    if tool == "nmap":
        return (
            "Nmap is a network scanning tool used in ethical hacking.\n"
            "It helps identify live hosts, open ports, and running services.\n\n"
            "Example (educational):\n"
            "nmap -sn 192.168.1.0/24\n\n"
            "⚠ Use only on networks you own or have permission to test."
        )

    if tool == "sqlmap":
        return (
            "SQLMap is an automated tool used to test SQL injection vulnerabilities.\n"
            "It detects and exploits insecure database queries.\n\n"
            "Example (educational):\n"
            "sqlmap -u \"http://example.com/page?id=1\" --batch\n\n"
            "⚠ Only use on legal labs or permitted targets."
        )

    if tool == "hydra":
        return (
            "Hydra is a login brute-force tool for protocols like SSH, FTP, HTTP.\n"
            "It is used to test password strength.\n\n"
            "Example (educational):\n"
            "hydra -l admin -P passwords.txt ssh://127.0.0.1\n\n"
            "⚠ Brute-force attacks without permission are illegal."
        )

    return "I don't have information about that tool yet."
