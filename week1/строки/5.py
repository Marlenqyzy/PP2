x = input()
cnt = 0
index = 0
for i in range(len(x)):
    if x[i] == "f":
        if cnt == 0:
            cnt += 1
            print(i, end = " ")
        else:
            index = i
            cnt += 1
if cnt < 2:
    print()
else:
    print(index)