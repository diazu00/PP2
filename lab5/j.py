import re

pattern = r'(?<!^)(?=[A-Z])'
s = input()
new_text = re.sub(pattern, '_', s).lower()
print(new_text)