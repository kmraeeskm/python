a=input("enter some integer values:")
b=input("enter some integer values:")
c=a.split(" ")
d=b.split(" ")
c=list(map(int,c))
d=list(map(int,d))
clen=len(c)
dlen=len(d)
if clen==dlen:
    print("list are of same length,length =",clen)
else:
    print("list are not same length")

if sum(c)==sum(d):
    print("sum is same,sum =",sum(c))
else:
     print("sum is not same")
print("common terms:")
for i in range(clen):
    for j in range(dlen):
        if(c[i]==d[j]):
            print(c[i])




