import re

givenString = "abababbbbababbabababababbbbaabababa"
print(len(givenString))
matcher = re.finditer('ab', givenString)
count = 0
for match in matcher:
    print('The start index of the pattern {} and the end index of the pattern {} and the pattern is {} and count is'
          .format(match.start(), match.end(), match.group()))
    print("Number of occurance is : ", count)
    count = count + 1