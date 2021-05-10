"""Write a program to find the product of all elements of a list."""
l = []
mul = 1
for i in range(0,5):
    i = int(input("enter numbers : "))
    l.append(i)
    lenght = len(l)
for j in range(0,lenght):
    mul = mul * l[j]
print ("product = ", mul)