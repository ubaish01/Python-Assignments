
choice = int(input("1. Celcius to farenhiet \n2. Farenhiet to celcius\nEnter here : "))

if(choice==1):
    c = int(input("Enter the temprature in celcius : "))
    f = (1.8*c)+32;
    print(c,"celcius = ",f,"farenhiet")
else:
    f = int(input("Enter the temprature in farenhiet : "))
    c = ((f-32)*5)/9;   
    print(f,"farenhiet = ",c,"celcius")





