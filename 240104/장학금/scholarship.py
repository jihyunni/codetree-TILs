score = list(map(int,input().split()))

mid = score[0]
final = score[1]

if mid >=90 and final >=95:
    print(100000)
elif mid >= 90 and final >=90:
    print(50000)
elif mid >=90 and final <90:
    print(0)
else: 
    print(0)