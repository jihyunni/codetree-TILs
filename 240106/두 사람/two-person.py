fir = list(map(str,input().split()))
sec = list(map(str,input().split()))

aa = int(fir[0])
ase = fir[1]

ba = int(sec[0])
bse = sec[1]

if aa >= 19 or ba >= 19:
    if ase == 'M' or bse == 'M':
        print(1)
    else:
        print(0)
else: print(0)