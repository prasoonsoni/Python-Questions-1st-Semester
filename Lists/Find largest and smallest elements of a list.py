"""Find largest and smallest elements of a list."""
n = int(input("How many numbers you want to enter in a list ? "))
l = []
for i in range(0,n):
    i = int(input("Enter Numbers : "))
    l.append(i)
print("Your List  Of Numbers-->")
print(l)
l.sort()
largest = l[n-1]
smallest = l[0]
print("Largest number is : ", largest)
print("Smallest number is : ", smallest)
