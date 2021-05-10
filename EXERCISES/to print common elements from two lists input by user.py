#to print common elements from two lists inputs by user

n1 = int(input("Number of elements in list 1st : "))
l1 = []
for i in range(0,n1):
    x = int(input("Enter Numbers : "))
    l1.append(x)
n2 = int(input("Number of elements in list 2nd : "))
l2 = []
for j in range(0,n2):
    y = int(input("Enter Numbers : "))
    l2.append(y)
a1 = set(list(l1))
a2 = set(list(l2))
intersection = a1|a2
common_elements = list(set(intersection))
print("List 1st elements :- ",l1)
print("List 2nd Elements :- ",l2)
print("Common elements in your lists are :- ",common_elements)
