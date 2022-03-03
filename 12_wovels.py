a=input("Enter the sentence to select vowels : ")
print(a)
print(a.strip())
a=list(a.strip())
print(a)
b=[i for i in a if i in "AEIOUaeiou"]
print(b)