import re
x = input()
p = re.split(r"[,.]", x)
for i in p:
    print(i)