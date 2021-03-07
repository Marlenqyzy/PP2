x = input()
print(x[2])
print(x[-2])
print(x[:5])
print(x[:len(x) - 2])

for i in range(len(x)):
    if i%2 == 0:
        print(x[i], end = "")
print()       

for i in range(len(x)):
    if i%2 == 1:
        print(x[i], end = "")
print()
print(x[::-1])

for i in range(len(x) - 1, -1, -2):
    print(x[i], end = "")
print()
print(len(x))