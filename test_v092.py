from core.executor import write_file, delete_file

path = "sandbox/pin_test.txt"

print(write_file(path, "PIN protected delete test"))
print(delete_file(path))
