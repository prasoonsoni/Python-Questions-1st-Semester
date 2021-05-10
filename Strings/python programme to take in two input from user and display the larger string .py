"""python programme to take in two input from user and display the larger string 
without using the built in functions"""
a1 = str(input("word 1 = "))
a2 = str(input("word 2 = "))
c1 = 0
c2 = 0
for i in a1:
    c1 = c1+1
for j in a2:
    c2 = c2+1
if c1>c2:
    print("bigger word is =", a1)
else:
    print("bigger word is = ", a2)