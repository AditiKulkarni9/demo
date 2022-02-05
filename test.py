a = int(input("enter rows for m1:"))
#coloumns for m1 / rows for m1 
b = int(input("enter coloums for m1/ rows or m1:"))
#coloumns for m2
c = int(input("enter coloumns for m2:"))
#m1 = a*b
print("elements of m1 are:")
m1 = [[int(input()) for i in range(b)] for j in range(a)]
print("m1:")
for i in range(1):
  for j in range(1):
    print(m1)
#m2 = b*c
print("\nelements of m2 are:")
m2 = [[int(input()) for i in range(c)] for j in range(b)]
print("m2:")
for i in range(c):
  for j in range(b):
    print(m2)
