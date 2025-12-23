import subprocess


_os_cache = {}


def get_remote_os(user, host):
    """
    Detect remote OS once and cache it
    """
    key = f"{user}@{host}"
    if key in _os_cache:
        return _os_cache[key]

    try:
        subprocess.check_output(
            ["ssh", key, "uname"],
            stderr=subprocess.DEVNULL
        )
        os_type = "linux"
    except Exception:
        os_type = "windows"

    _os_cache[key] = os_type
    return os_type
