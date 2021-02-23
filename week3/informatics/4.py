n = input().split()
c = n.count("0")
for i in n:
    if i != "0":
        print(i, end = " ")

for i in range(c):
    print("0", end = " ")
