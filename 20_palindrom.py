str = input("Enter a string to check whether it is palindrome : ")
copy=str[ ::-1]
print(copy)
if copy==str : 
	print("It is palindrome")
else :
        print("It is not palindrome")
