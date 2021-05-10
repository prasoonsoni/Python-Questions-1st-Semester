"""Given a two list of numbers create a new list such that 
new list should contain only odd numbers from the first list 
and even numbers from the second list"""

l = []
# for 1st list
n1 = int(input("Number of elements in first list: "))
l1 = []
for i in range(0,n1):
    x = int(input("Enter Elements of list 1: "))
    l1.append(x)
for j in l1:
    if j%2!=0:
        l.append(j)
#for 2nd list
n2 = int(input("Number of elements in second list: "))
l2 = []
for i in range(0,n2):
    y = int(input("Enter Elements of list 2: "))
    l2.append(y)
for j in l2:
    if j%2==0:
        l.append(j)
print("FIRST LIST : ",l1)
print("SECOND LIST : ",l2)
print("FINAL LIST : ",l)

