import os
import shutil
import subprocess
import tarfile
import time

DEPLOY_DIR = "deploy"
ARCHIVE = "jarvis_bundle.tar.gz"


def prepare_bundle():
    if os.path.exists(DEPLOY_DIR):
        shutil.rmtree(DEPLOY_DIR)

    os.mkdir(DEPLOY_DIR)

    # Copy essential files
    shutil.copy("main.py", DEPLOY_DIR)
    shutil.copy("README.md", DEPLOY_DIR)
    shutil.copytree("core", f"{DEPLOY_DIR}/core")

    # Create archive
    with tarfile.open(ARCHIVE, "w:gz") as tar:
        tar.add(DEPLOY_DIR)

    return ARCHIVE


def deploy_to_host(user, host, path="~/jarvis"):
    bundle = prepare_bundle()

    # Create remote directory
    subprocess.run(
        f"ssh {user}@{host} 'mkdir -p {path}'",
        shell=True
    )

    # Copy bundle
    subprocess.run(
        f"scp {bundle} {user}@{host}:{path}/",
        shell=True
    )

    # Extract & run
    cmd = (
        f"ssh {user}@{host} "
        f"'cd {path} && "
        f"tar -xzf {ARCHIVE} && "
        f"cd deploy && "
        f"python3 main.py'"
    )

    subprocess.Popen(cmd, shell=True)

    return f"🕷️ Jarvis deployed to {host}"
