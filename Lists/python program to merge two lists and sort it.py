"""python program to merge two lists and sort it"""
n1 = int(input("Number of elements in list 1 = "))
n2 = int(input("Number of elements in list 2 = "))
l1 = []
l2 = []
for i in range(0,n1):
    i = int(input("Enter Elements for list 1 = "))
    l1.append(i)
for j in range(0,n2):
    j = int(input("Enter Elements for list 2 = "))
    l2.append(j)
l = l1+l2
l.sort()
print("List 1 -->", l1)
print("List 2 -->", l2)
print("Final List-->>")
print(l)