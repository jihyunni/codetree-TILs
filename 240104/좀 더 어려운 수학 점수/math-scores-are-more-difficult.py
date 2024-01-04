score = list(map(int,input().split()))
sco = list(map(int,input().split()))

am = score[0]
ae = score[1]

bm = sco[0]
be = sco[1]

if am > bm:
    print("A")
elif am < bm:
    print("B")

if am == bm and ae > be:
    print("A")
elif am == bm and ae<be:
    print("B")