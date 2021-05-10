w = input()
w1 = w[::-1]
n = int(input())
straight = (w*(n//len(w))) + w[0:n%len(w)]
reverse = (w1*(n//len(w1))) + w1[0:n%len(w1)]
reverse = reverse[::-1]
print(reverse)
straight_d = {}
reverse_d = {}
for i in range(n):
    straight_d[i+1] = straight[i]
for i in range(n,0,-1):
    reverse_d[i] = reverse[abs(i-n)]
for i in reverse_d.keys():
    a = reverse_d.get(i)
    b = straight_d.get(i)
    if a == b:
        print(i)
        break
else:
    print(-1)
print(straight_d)
print(reverse_d)