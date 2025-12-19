import os

def write_file(path, content):
    try:
        with open(path, "w") as f:
            f.write(content)
        return True, "File written."
    except Exception as e:
        return False, str(e)

def read_file(path):
    try:
        if not os.path.exists(path):
            return False, "File not found."
        return True, open(path).read()
    except Exception as e:
        return False, str(e)
