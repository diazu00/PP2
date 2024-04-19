import os
file = input()

if not os.path.exists(file):
    print("File does not exist.")
else:
    print("File exists.")