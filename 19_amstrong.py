n=int(input("Enter a no to check armstrong : "))
copy=n
sum=0
while (n!=0):
	rem = n%10
	print(rem)
	sum = sum + (rem*rem*rem)
	print (sum)
	n=int(n/10)
if (sum==copy) :
	print("The no is armstrong")
else : 
	print("The no is not armstrong")
