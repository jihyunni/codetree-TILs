A = list(map(int,input().split()))

a = A[0]
b = A[1]
c = A[2]

if a>b and a>c:
    if a == A[0]:
        a = 1
    else:
        a = 0

if a<b and b>c:
    if b == A[0]:
        a = 1
    else:
        a = 0


if a<c and c>b:
    if b == A[0]:
        a = 1
    else:
        a = 0

if a==b==c:
    aa = 1
else:
    aa = 0

print(a,aa)