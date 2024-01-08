y = int(input())

if y%4==0:
    a = "true"
    if  y%100 == 0:
        a = "false"
        if y%400 ==0:
            a = "true"
        else: 
            a = "false"
    else: a = "true"
else: a = "false"
print(a)