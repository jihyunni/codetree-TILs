a = input()
b = input()
c = input()

a = a.split()
b = b.split()
c = c.split()

A = 0
B = 0
C = 0
D = 0

# print(a, b, c)


if(a[0] == 'Y' and int(a[1]) >= 37):
    A += 1
elif(a[0] == 'N' and int(a[1]) >= 37):
    B += 1
elif(a[0] == 'Y' and int(a[1]) < 37):
    C += 1
else:
    D += 1

if(b[0] == 'Y' and int(b[1]) >= 37):
    A += 1
elif(b[0] == 'N' and int(b[1]) >= 37):
    B += 1
elif(b[0] == 'Y' and int(b[1]) < 37):
    C += 1
else:
    D += 1

if(c[0] == 'Y' and int(c[1]) >= 37):
    A += 1
elif(c[0] == 'N' and int(c[1]) >= 37):
    B += 1
elif(c[0] == 'Y' and int(c[1]) < 37):
    C += 1
else:
    D += 1

if(A >= 2):
    print("E")
else:
    print("N")