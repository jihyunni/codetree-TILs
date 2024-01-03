A = list(map(int,input().split()))

a = A[0]
b = A[1]
c = A[2]

if a<=b and a<=c:
    print(1, end = " ")
else:
    print(0, end = " ")

if a==b==c:
    print(1)
else:
    print(0)