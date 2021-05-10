s = input()
alpha = []
digit = []
lower = []
upper = []
#to check alnum
d=[]
c=[]
for i in s:
    if i.isdigit():
        d.append(i)
for i in s:
    if i.isalpha():
        c.append(i)
if d!=[] or c!=[]:
    print("True")
else:
    print("False")
#to check alpha
for i in s:
    if i.isalpha():
        alpha.append(i)
if alpha!=[]:
    print("True")
else:
    print("False")
#to check digit
for i in s:
    if i.isdigit():
        digit.append(i)
if digit!=[]:
    print("True")
else:
    print("False")
#to check lower
for i in s:
    if i.islower():
        lower.append(i)
if lower!=[]:
    print("True")
else:
    print("False")
#to check upper
for i in s:
    if i.isupper():
        upper.append(i)
if upper!=[]:
    print("True")
else:
    print("False")

