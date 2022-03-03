def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
num=int(input("Enter the number to find the factorial : "))
print(factorial(num))
    