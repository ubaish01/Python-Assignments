point1 = int(input("Enter the position of first point : "))
point2 = int(input("Enter the position of second point : "))

diff = point1-point2;

if(diff<0):
    diff = -diff;

print("The difference is",diff)