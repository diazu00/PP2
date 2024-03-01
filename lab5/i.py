import re

pattern = r'(?<!^)(?=[A-Z])'
s = input()
new = re.sub(pattern, ' ', s)
print(new)