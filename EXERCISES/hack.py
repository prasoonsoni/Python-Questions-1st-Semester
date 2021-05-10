from pprint import pprint
n = int(input())
dic = {}
for i in range(1,n+1):
    l = []
    s = (i*(i+1))//2
    for j in range(1,s+1):
        if s%j==0:
            l.append(j)
    dic[s] = l
pprint(dic)

    