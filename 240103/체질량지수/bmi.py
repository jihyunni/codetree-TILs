hei, wei = map(int,input().split())

bmi = (wei*10000)//(hei*hei)

if bmi >=25:
    print(bmi)
    print("Obesity")
else:
    print(bmi)