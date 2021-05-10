def selectionsort(l):
    n = len(l)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if l[minpos]>l[j]:
                minpos = j
                l[i],l[minpos]=l[minpos],l[i]


l = [1,3,2,5,4]
selectionsort(l)
print(l)