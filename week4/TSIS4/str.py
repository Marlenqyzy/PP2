x = input().split()
x.sort()
p = {}

for i in range(len(x)):
    if x[i] not in p.keys():
        p[x[i]] = 1
    else:
        p[x[i]] += 1
for i, j in p.items():
    print(i, "-", j) 