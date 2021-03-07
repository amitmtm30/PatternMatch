# Requirement to search group of thing
# a or b or c
# any alphabet symbol
# any digit
import re

givenString = 'abcdefghijklmnopqrstuvwxyz0123456789'
matcher = re.finditer('[0123]', givenString)

for match in matcher:
    print(match.group())