import re

givenString = "Learning Python is Very Easy and easy for Implementation"
match = re.fullmatch("Learning Python is Very Easy and easy for Implementation", givenString)
#print(match)
if match is not None:
    print("Match Found")
else:
    print("Match Not Found")