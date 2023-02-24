n = int(input("Enter the number you want the factorial of : "))
c=n
fact = 1
while(n>1):
    fact=fact*n
    n=n-1

print("Factorial of",c,"is",fact)