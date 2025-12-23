import subprocess
from core.os_detect import get_remote_os


def run_remote_command(user, host, linux_cmd, windows_cmd):
    """
    Run correct command depending on remote OS
    """
    os_type = get_remote_os(user, host)
    target = f"{user}@{host}"

    if os_type == "windows":
        cmd = windows_cmd
    else:
        cmd = linux_cmd

    return subprocess.check_output(
        ["ssh", target, cmd],
        stderr=subprocess.STDOUT
    ).decode()
