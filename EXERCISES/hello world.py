def bubblesort(l):
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

n = int(input())
l = list(map(int, input().split()))
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

bubblesort(l1)
runnerup = l1[-2]
print(runnerup)