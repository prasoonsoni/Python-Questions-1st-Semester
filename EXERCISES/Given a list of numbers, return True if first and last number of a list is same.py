"""Given a list of numbers, return True if first and 
last number of a list is same"""

n = int(input("number of elements in a list= "))
l = []
for i in range(0,n):
    x = int(input("Enter elements : "))
    l.append(x)
if l[0]==l[-1]:
    print("True")
else:
    print("False")