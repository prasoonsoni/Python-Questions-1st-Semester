"""given an english word design algorithm and write the python code to check 
is it can be typed using just a single row of keyboard. for eg- potter, equity
pribt yes if letters of the word are from single row and print no otherwise"""

a = str(input("Enter a Word ? "))
f = "qwertyuiop"
s = "asdfghjkl"
t = "zxcvbnm"
a = a.lower()
flag = 0
for i in a:
    if a not in f:
        break
else:
    flag = 1
    print("yes")
for j in a:
    if a not in s:
        break
else:
    flag = 2
    print("yes")
for k in a:
    if a not in t:
        break
else:
    flag = 3
    print("yes")
if flag==0:
    print("no")
    
    
    
    
    