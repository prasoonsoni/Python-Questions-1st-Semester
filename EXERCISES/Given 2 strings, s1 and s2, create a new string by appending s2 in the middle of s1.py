"""Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1"""

s1 = str(input())
s2 = str(input())
l1 = int(len(s1))
l2 = int(len(s2))
x1 = int(l1/2)
x2 = int((l1/2) + 2)
a1 = s1[0:x1]
a2 = s1[x1:x2]
S = a1+s2+a2
print(S)