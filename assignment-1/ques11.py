n = int(input("Enter the number : "))
nc = n
rev = 0


count=0
while(nc>0):
    rev=rev*10
    rev = rev + (nc%10)
    nc = nc//10

print(rev)
if(rev==n):
    print("Pallindrome")
else:
    print("not pallindrome")