"""python program to find the second largest number in a list"""

n = int(input("Number of Inputs --> "))
l = []
for i in range(0,n):
    i = int(input("Enter Numbers :>> "))
    l.append(i)
    b = list(set(l))
    b.sort()
second = b[-2]
print("Second Largest Number is :->> ", second)