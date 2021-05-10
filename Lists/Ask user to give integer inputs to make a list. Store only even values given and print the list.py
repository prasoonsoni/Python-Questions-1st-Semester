"""Ask user to give integer inputs to make a list. 
Store only even values given and print the list."""

n = int(input("How many elements you want to take ? "))
l =[]
for i in range(0,n):
    i = int(input("Enter Numbers = "))
    if i%2==0:
        l.append(i)
print(l)