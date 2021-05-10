"""Write a program to find out the largest and smallest word in the string "This is an umbrella"."""

a = "This is an umbrella"
b = a.split()
c = b[0]
d = b[1]
e = b[2]
f = b[3]
l1 = len(c)
l2 = len(d)
l3 = len(e)
l4 = len(f)
if l1>l2 and l1>l3 and l1>l4:
    print(c)
elif l2>l3 and l2>l4 and l2>l1:
    print(d)
elif l3>l1 and l3>l2 and l3>l4:
    print(e)
else:
    print(f)
