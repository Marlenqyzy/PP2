import re

x = input()
y = input()
key = re.compile(y)
p = key.search(x)

if not p:
    print("(-1, -1)")
else:
    while p:
        print(f"({p.start()}, {p.end() - 1})")
        p = key.search(x, p.start() + 1)