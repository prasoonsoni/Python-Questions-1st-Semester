"""Write a program to check if elements of a list are same or 
not it read from front or back. E.g.-
2	3	15	15	3	2 """
n = int(input("Number of elements ? "))
l = []
for i in range(0,n):
    i = int(input("enter numbers : "))
    l.append(i)
l2 = l.copy()
l2.reverse()
if l==l2:
    print("same")
else:
    print("not same")