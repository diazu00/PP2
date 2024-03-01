import re

pattern = r'a.+b$'
s = input()
match = re.match(pattern, s)

if match:
    print("Match found!")
else:
    print("Match not found.")