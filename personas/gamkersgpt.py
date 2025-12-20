def explain(command: str) -> str:
    c = command.lower()

    if "wifi" in c and "password" in c:
        return (
            "⚠️ WiFi password cracking is illegal without permission.\n\n"
            "Ethical explanation:\n"
            "Security professionals test their OWN networks by capturing "
            "WPA/WPA2 handshakes and checking password strength using tools "
            "like aircrack-ng.\n\n"
            "This is done only on lab networks or devices you own.\n"
            "Omni will NEVER attack real networks."
        )

    if "scan network" in c or "nmap" in c:
        return (
            "Network scanning is used to discover live hosts and open ports.\n"
            "Administrators use it to secure systems.\n\n"
            "Scanning without permission is illegal."
        )

    if "hydra" in c or "bruteforce" in c:
        return (
            "Bruteforce tools test password strength during audits.\n"
            "They are used ONLY on systems you own or have written permission for."
        )

    return (
        "I can explain ethical hacking concepts, tools, and defenses.\n"
        "Ask responsibly."
    )
