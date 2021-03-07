import re

# match function will find the string at the beginning of the string
givenString = "Learning Python is very Easy"

matcher = re.match("L", givenString)

if matcher is not None:
    print("Match Found at the beginning of the string")
else:
    print("match not found")