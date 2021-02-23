n = input().split()
min = 1001
for i in range(len(n)):
    m = int(n[i])
    if m > 0:
        if min > m:
            min = m
print(min)