"""python program to put even and odd elements in a list into two
different lists"""
n = int(input("Number of inputs you want to give :  "))
l = []
l1 = []
l2 = []
for i in range(0,n):
    i = int(input("Enter Number -> "))
    l.append(i)
print("Original List")
print(l)
for j in l:
    if j%2==0:
        l1.append(j)
    else:
        if j%2!=0:
            l2.append(j)
print("Even Numbers List-> ")
print(l1)
print("Odd Number List-> ")
print(l2)
        
