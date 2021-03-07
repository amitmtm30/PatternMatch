import re

with open("D:\\PythonPattern\\amit.txt") as file:
    content = file.read()
    print(content)
    pattern = "[1-9][1-9][1-9].[1-9][1-9][1-9].[0-9].[0-9]{1,3}"
    matcher = re.finditer(pattern, content)
    print("valid IPs are : ")
    for match in matcher:
        print(match.group())
