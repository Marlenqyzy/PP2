fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("1:")
for x in "banana":
  print(x)

print("2:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("3:")

for x in range(6):
  print(x)
print('\n')

for x in range(2, 6):
  print(x)

print('\n')

for x in range(2, 30, 3):
  print(x)

print("4:")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)