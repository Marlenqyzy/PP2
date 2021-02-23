a = set(input().split())
n = set(input().split())
c = a & n
for i in c:
    print(i, end = " ")