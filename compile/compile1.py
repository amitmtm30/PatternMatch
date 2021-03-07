# for pattern matching we have to import re module
# compile function change the string in to regex object

import re
givenString = "abababaaabaaababababbabbbbbab"
# pattern = re.compile('ab')
# matcher = pattern.finditer(givenString)
# for match in matcher:
#     print(match.group())

pattern = re.finditer('ab', givenString)
for match in pattern:
    print(match.group())