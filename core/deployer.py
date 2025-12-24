import subprocess
from core.remote_exec import get_remote_os


def deploy_to_host(user, host):
    os_type = get_remote_os(user, host)

    if os_type == "windows":
        cmd = [
            "ssh",
            f"{user}@{host}",
            'mkdir C:\\omni_node 2>nul & echo print("🖤 Venom Node Online") > C:\\omni_node\\node.py'
        ]
    else:
        cmd = [
            "ssh",
            f"{user}@{host}",
            'mkdir -p omni_node && echo "print(\'🖤 Venom Node Online\')" > omni_node/node.py'
        ]

    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return f"🖤 Venom connected to {user}@{host} ({os_type})"
    except subprocess.CalledProcessError as e:
        return f"❌ Venom deploy failed:\n{e.output.decode()}"
