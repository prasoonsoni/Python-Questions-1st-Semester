def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
n = int(input())
name = []
price = []
for i in range(n):
    x = input().split()
    na = [x[-1],x[0]]
    pa = [x[-1],int(x[1])]
    name.append(na)
    price.append(pa)
extract = input()
n = []
p = []
for i in range(len(name)):
    if name[i][0] == extract:
        n.append(name[i][1])
for i in range(len(price)):
    if price[i][0] == extract:
        p.append(price[i][1])
new_dict = {}
for i in range(len(n)):
    new_dict[p[i]] = n[i]
bubbleSort(p)
final = []
for i in p:
    final.append(new_dict.get(i))
print(p)
print(final)

