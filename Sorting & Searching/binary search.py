def binarysearch(l,n):
    start = 0
    end = len(l)
    while start < end:
        mid = (start+end)//2
        if l[mid]>n:
            end = mid
        elif l[mid]<n:
            start = mid+1
        else:
            return mid 
    return -1

    n = int(input())
    l = [1,2,3,4,5]
    binarysearch(l,n)
    if binarysearch == -1:
        print("Not Found")
    else:
        print("Found")

