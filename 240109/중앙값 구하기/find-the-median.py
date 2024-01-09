a,b,c = input().split()

if a > b and b > c:
    print(b)
elif a>b and c>b:
    if a>c:
        print(c)
    else:
        print(a)
else:
    print(b)