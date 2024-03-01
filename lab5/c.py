import re

pattern = r'[a-z]+_[a-z]+'
s = input()
match = re.match(pattern, s)

if match:
    print("Match found!")
else:
    print("Match not found.")