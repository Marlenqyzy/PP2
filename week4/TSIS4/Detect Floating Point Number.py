import re
p = int(input())

for i in range(p):
    txt = input()
    x = re.fullmatch(r"(\+|\-)?(\d){0,}(\.)(\d+)", txt)
    print(True) if x else print(False)