"""Write a program to print sum, average of all numbers, 
smallest and largest element of a list."""

n = int(input("How many numbers you want to enter ? "))
l = []
sum = 0
for i in range(0,n):
    i = int(input("enter numbers = "))
    l.append(i)
    lenght = len(l)
for j in range(0,lenght):
    sum = sum + l[j]
average = sum/n
l.sort()
largest = l[-1]
smallest = l[0]
print("SUM = ", sum)
print("AVERAGE = ", average)
print("LARGEST NUMBER = ", largest)
print("SMALLEST NUMBER = ", smallest)
