# selection sort
def selectionSort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min = j
                
        a[i],a[min]=a[min],a[i]
        
a = [64,34,12,25,5]
selectionSort(a)
for i in a:
    print(i)