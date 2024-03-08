import os

path = "/path/to/file.txt"

# Check existence
if not os.path.exists(path):
    print("Path does not exist.")
else:
    print("Path exists.")

# Find filename and directory portion of the path
filename = os.path.basename(path)
directory = os.path.dirname(path)

print("Filename:", filename)
print("Directory:", directory)