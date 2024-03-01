import re

pattern = r'[ ,\.]+'
s = input()
new = re.sub(pattern, ':', s)
print(new)