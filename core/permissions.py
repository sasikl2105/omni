SAFE = "safe"
SENSITIVE = "sensitive"
CRITICAL = "critical"

def classify_action(action_name: str) -> str:
    """
    Classify how dangerous an action is.
    v0.9 = classification only
    """
    safe_actions = [
        "write_file",
        "read_file"
    ]

    sensitive_actions = [
        "delete_file"
    ]

    critical_actions = [
        "system_command",
        "network_access"
    ]

    if action_name in safe_actions:
        return SAFE
    if action_name in sensitive_actions:
        return SENSITIVE
    return CRITICAL
