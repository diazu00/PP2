import re

pattern = r'[A-Z][a-z]+'
s = input()
match = re.match(pattern, s)

if match:
    print("Match found!")
else:
    print("Match not found.")