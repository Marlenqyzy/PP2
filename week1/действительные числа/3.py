import math

x = float(input())
y = int(x*10%10)
if y >= 5:
    print(math.ceil(x))
else:
    print(math.floor(x))