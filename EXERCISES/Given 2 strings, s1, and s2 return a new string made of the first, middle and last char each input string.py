"""Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string"""

s1 = str(input())
s2 = str(input())
l1 = int(len(s1))
l2 = int(len(s2))
f = s1[0] + s2[0]
x1 = int(l1-1)
x2 = int(l2-1)
x11 = int(x1/2)
x22 = int(x2/2)
l = s1[x1] + s2[x2]
m = s1[x11] + s2[x22]
S = f + m + l
print(S)