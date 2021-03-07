import re

givenString = "Learning  is Very Easy Python"
matcher = re.search("Python", givenString)
if matcher is not None:
    print("Yes we have a match")
else:
    print("No")