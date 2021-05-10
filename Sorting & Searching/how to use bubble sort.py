# bubble sort
def bubbleSort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(0,n-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                
l = [5,2,1,3,4]
bubbleSort(l)
for i in range(len(l)):
    print(l[i])
    