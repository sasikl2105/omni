from core.remote_exec import run_remote_command


def deploy_to_host(user, host):
    try:
        print("🖤 Venom Mode: requesting access to", f"{user}@{host}")

        linux_cmd = (
            "mkdir -p omni_node && "
            "echo 'print(\"🖤 Venom Node Online\")' > omni_node/node.py"
        )

        windows_cmd = (
            "if not exist omni_node mkdir omni_node && "
            "echo print('🖤 Venom Node Online') > omni_node\\node.py"
        )

        run_remote_command(user, host, linux_cmd, windows_cmd)

        return f"🖤 Venom connected to {user}@{host}"

    except Exception as e:
        return f"❌ Venom deploy failed: {e}"
