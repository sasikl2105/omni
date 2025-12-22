import os
import subprocess


def get_cpu_usage():
    try:
        output = subprocess.check_output(
            ["top", "-bn1"],
            stderr=subprocess.DEVNULL
        ).decode()
        return output
    except Exception as e:
        return f"CPU read failed: {e}"


def get_memory_usage():
    try:
        output = subprocess.check_output(
            ["free", "-h"],
            stderr=subprocess.DEVNULL
        ).decode()
        return output
    except Exception as e:
        return f"Memory read failed: {e}"
