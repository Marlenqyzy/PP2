import re
string = input()
s = re.search(r"(?P<year>.+)\s(?P<month>.+)\s(?P<day>.+)", string)
x = int(s.group("year"))
y = int(s.group("month"))
z = int(s.group("day"))

if x >= 1299 and x <= 1922:
    if y >= 1 and y <= 12:
        if z >= 1 and z <= 31:
            print("Yes")
            exit()
print("No")