x = int(input())

i = 0
while 2**i <= x:
    if 2**i == x:
        print("YES")
        exit() 
    i+=1
print("NO")