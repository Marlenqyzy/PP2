import math

x = input()
y = math.ceil(len(x)/2)

#for i in range(len(x)):
i = 0
while i + y < len(x):
    print(x[i + y], end = "")
    i += 1

i = 0
while i < y:
    print(x[i], end = "")
    i += 1
    