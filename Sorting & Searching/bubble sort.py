def bubblesort(l):
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

l = [1,3,4,2,6,15,11]
bubblesort(l)
print(l)