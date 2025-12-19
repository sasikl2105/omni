from core.executor import write_file, read_file, delete_file

path = "sandbox/test.txt"

ok, msg = write_file(path, "Hello Omni v0.9")
print(ok, msg)

ok, content = read_file(path)
print(ok, content)

ok, msg = delete_file(path)
print(ok, msg)
