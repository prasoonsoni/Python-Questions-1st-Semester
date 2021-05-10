"""Given a list of numbers, Iterate it and print only those 
numbers which are divisible of 5"""

n = int(input("number of elements = "))
l = []
for i in range(0,n):
    x = int(input("Enter Elements : "))
    l.append(x)
for j in l:
    if j%5==0:
        print(j)