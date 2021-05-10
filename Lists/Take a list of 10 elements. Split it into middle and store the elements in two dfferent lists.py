"""Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
INITIAL list :
58	24	13	15	63	9	8	81	1	78

After spliting :
58	24	13	15	63
9	8	81	1	78"""

l = []
for i in range(0,10):
    i = int(input("Enter Numbers : "))
    l.append(i)
print("INITIAL LIST :")
print(l)
l1 = l[0:5]
l2 = l[5:10]
print("AFTER SPLITTING")
print(l1)
print(l2)