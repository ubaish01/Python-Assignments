n = int(input("Enter the number you want to check : "))
isPrime = True 
for i in range(2,((n//2)+1)):
    if(n%i==0):
        isPrime = False
        break

if(isPrime):
    print("The number is prime")
else:
    print("The number is not prime")

