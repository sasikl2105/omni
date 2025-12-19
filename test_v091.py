from core.executor import write_file, read_file, delete_file

path = "sandbox/secure.txt"

print(write_file(path, "Omni permission test"))
print(read_file(path))
print(delete_file(path))
