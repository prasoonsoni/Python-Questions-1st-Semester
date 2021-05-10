""" how to use elif
if condition:
    statements
elif condition:
    statements   """
    
    # largest of three numbers #

a = int(input())
b = int(input())
c = int(input())

if a>b and a>c:
    print (a, "is greatest")
elif b>c:
    print (b, "is greatest")
else:
    print (c, "is greatest")