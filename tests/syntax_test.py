import re

pattern = re.compile("-?[1-9]\d?")

print re.match(pattern, '-1')