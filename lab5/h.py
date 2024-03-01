import re

pattern = r'[A-Z]'
s = input()
new = re.split(pattern, s)
print(new)