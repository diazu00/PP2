import re

pattern = r'a(b{2,3})'
s = str(input())
match = re.match(pattern, s)

if match:
    print("Match found!")
else:
    print("Match not found.")