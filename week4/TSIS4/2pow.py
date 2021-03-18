def kru(str):
    cnt = 0
    for i in range(len(str)):
        p = str[i]
        if p.isalpha():
            cnt += 1
    i = 0
    y = 0
    while cnt >= y:
        y = 2**i
        if cnt == y:
            return "H"
            exit()
        i += 1
    return "C"


x = int(input())

for i in range(x):
    y = input().split()
    for j in y:
        print(kru(j), end = " ")
    print()