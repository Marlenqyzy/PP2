thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

print('2:')

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

print("3:")

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)