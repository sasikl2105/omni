import subprocess

def get_cpu_usage():
    try:
        output = subprocess.check_output(
            "top -bn1 | grep 'Cpu(s)'",
            shell=True
        ).decode()
        return output.strip()
    except Exception as e:
        return f"CPU read error: {e}"

def get_memory_usage():
    try:
        output = subprocess.check_output(
            "free -h",
            shell=True
        ).decode()
        return output.strip()
    except Exception as e:
        return f"Memory read error: {e}"
