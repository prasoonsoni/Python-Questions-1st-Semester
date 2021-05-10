t = int(input())
def sign(l):
    if l[0] > l[1]:
        return ">"
    elif l[0] < l[1]:
        return "<"
    elif l[0]==l[1]:
        return "="
n = []
for i in range(t):
    l = list(map(int, input().split()))
    result = sign(l)
    n.append(result)

for i in n:
    print(i)

