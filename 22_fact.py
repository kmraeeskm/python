def factorial(n): 
    if (n==1 or n==0):
        return 1
    else:
        # n! = n x (n - 1)!4
        return n * factorial(n - 1)
num=int(input("Enter the number to find the factorial : "))
print(factorial(num))