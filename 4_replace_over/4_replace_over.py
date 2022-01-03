str=input("enter some integer values:")
b=str.split(" ")
b=list(map(int,b))
print(b)
l=len(b)
for i in range(l):
    if b[i]>100:
        b[i]='over'
print(b)
