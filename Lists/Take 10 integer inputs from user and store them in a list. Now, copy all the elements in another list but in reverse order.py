"""Take 10 integer inputs from user and store them in a list. 
Now, copy all the elements in another list but in reverse order."""


l1 = []
for i in range(0,10):
    i = int(input("enter number : "))
    l1.append(i)
    l2 = l1.copy()
    l2.reverse()
print(l1)
print(l2)