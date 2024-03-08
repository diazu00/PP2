import os

path = "/path/to/file.txt"

# Check existence and access
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("File not found or not writable.")