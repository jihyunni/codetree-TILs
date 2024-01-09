a,b,c = map(int,input().split())

if a>b:
    if b>c:
        print(b)
    elif c>b:
        if c>a:
            print(a)
        else:
            print(c)
elif b>a:
    if a>c:
        print(a)
    elif c>a:
        if c>b:
            print(b)
        else:
            print(c)
elif c>b:
    if b>a:
        print(b)
    elif a>b:
        if c>a:
            print(a)
        else:
            print(c)