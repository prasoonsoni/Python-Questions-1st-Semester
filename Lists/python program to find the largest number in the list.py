"""python program to find the largest number in the list"""

n = int(input("Number of elements in list :-->> "))
l = []
for i in range(0,n):
    i = int(input("Enter numbers :-->> "))
    l.append(i)
    l.sort()
    a = l[-1]
print(l)
print("Largest number:--> ", a)
    