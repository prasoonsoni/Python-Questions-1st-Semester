"""Write a program to find the sum of all elements of a list."""
n = int(input("no of inputs : "))
l =[]
i = 0
sum1 = 0
while i<n:
    num = int(input("Enter a number : "))
    l.append(num)
    sum1 = sum1 + l[i]
    i=i+1
print(sum1)