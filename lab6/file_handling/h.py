import os

path = "/Users/Hp/Documents/pp2_dias/PP2/lab6/file_handling/Z.txt"

# Check existence and access
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("File not found or not writable.")