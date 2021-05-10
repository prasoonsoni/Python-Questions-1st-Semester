"""python programme to form a new string where the first character and the last
character have been exchanged"""

a = input()
b = len(a)
f = a[0]
l = a[b-1]
m = a[1:b-1]
c = l + m + f
print(c)
