"""Write a program to find the sum of all elements of a list."""
l = []
sum1 = 0
for i in range(0,5):
    i = int(input("enter numbers : "))
    l.append(i)
    lenght = len(l)
for j in range(0,lenght):
    sum1 = sum1 + l[j]
print ("sum = ", sum1)
        