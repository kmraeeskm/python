a=input("enter some integer values:")
b=a.split(" ")
c=list(map(int,b))
d=[i for i in c if i%2!=0]
print(d)

