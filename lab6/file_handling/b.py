import os

path = "/path/to/directory"

# Check existence
if not os.path.exists(path):
    print("Path does not exist.")
else:
    print("Path exists.")

# Check readability
if not os.access(path, os.R_OK):
    print("Path is not readable.")
else:
    print("Path is readable.")

# Check writability
if not os.access(path, os.W_OK):
    print("Path is not writable.")
else:
    print("Path is writable.")

# Check executability
if not os.access(path, os.X_OK):
    print("Path is not executable.")
else:
    print("Path is executable.")