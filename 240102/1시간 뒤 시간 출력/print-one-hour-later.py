a = str(input())
aa = a.split(":")

later_h = int(aa[0])+1
aa[0] = later_h
m = aa[1]

aa.insert(1,":")

print(aa[0], aa[1], aa[2], sep="")