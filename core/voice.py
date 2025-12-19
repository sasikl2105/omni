def listen():
    """
    Simple placeholder voice input.
    Will be improved later on better device.
    """
    try:
        return input("[Voice input] Say something (or press Enter to skip): ").strip()
    except KeyboardInterrupt:
        return None
