x = int(input())

i = -1
while 2**i <= x:
    i += 1
    if 2**i >= x:
        print(i)
        exit()