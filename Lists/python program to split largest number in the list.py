n = int(input("Number of elements : "))
l = []
l1 = []
l2 = []
for i in range(0,n):
    i = int(input("Enter unique Elements : "))
    l.append(i)
    l1 = l.copy()
    l1.sort()
    lenght = len(l1)
    b = l.index(max(l))
for j in range(0,lenght):
    if l1[-2] + l1[j] == l1[-1]:
        l2 = l.copy()
        l2.insert(b, l1[-2])
        l2.insert(b+1, l1[j])
        l2.remove(max(l2))
print(l2)
        
