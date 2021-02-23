'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''
print("1:")
a = 33
b = 200
if b > a:
  print("b is greater than a")

print("2:")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("3:")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("4:")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print("5:")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print("6:")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")