##to validate our reg number ex- 20bcb0070##

a = str(input("enter your register number :--"))
b = len(a)
c = a[0:2]
d = a[2:5]
e = a[5:9]
if c.isdigit() and d.isalpha() and e.isdigit() and b==9:
    print("valid")
else:
    print("invalid")