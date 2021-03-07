import re


givenString = "abbbbbaaaaaaabbbb"

matcher = re.finditer('^a' and 'b$' ,givenString)
for match in  matcher:
    print(match.group())