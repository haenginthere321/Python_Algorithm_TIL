# Solution 1

a = int(input())
b = a // 4
print("long "*b + "int")

# Solution 2

a = int(input())
b = a // 4
for i in range(b):
  print("long",end=" ")
print("int")
