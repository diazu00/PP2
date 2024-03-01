import re

pattern = r'_(\w)'
s = input()
new = re.sub(pattern, lambda x: x.group(1).upper(), s)
print(new)