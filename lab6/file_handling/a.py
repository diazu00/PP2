import os

path = "/Users/Hp/Documents/pp2_dias/PP2/lab4"

# List only directories
print("Directories:")
for directory in os.listdir(path):
    if os.path.isdir(os.path.join(path, directory)):
        print(directory)

# List only files
print("Files:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

# List all directories and files
print("All directories and files:")
for item in os.listdir(path):
    print(item)