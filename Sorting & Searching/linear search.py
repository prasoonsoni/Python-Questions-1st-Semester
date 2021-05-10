# linear searching
n = int(input())
l = []
for i in range(n):
    i = int(input())
    l.append(i)
    
x = int(input())
for i in range(n):
    if l[i]==x:
        print("Found")
        break
else:
    print("Not Found")
    