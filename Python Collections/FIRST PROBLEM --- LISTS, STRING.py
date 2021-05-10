#for first polynomial:
n1 = int(input("Enter your degree for 1st : "))
l1 = []
for i in range(0,n1+1):
    p1 = int(input("Enter Your Coeff in decreasing power from x^n to x^0 : "))
    l1.append(p1)
    l1f = l1.copy()
#for second polynomial  
n2 = int(input("Enter Your Degree for 2nd: "))
l2 = []
for j in range(0,n2+1):
    p2 = int(input("enter your coeff in decreasing power from x^n to x^0 : "))
    l2.append(p2)
    l2f = l2.copy()
    
len1 = len(l1f)
len2 = len(l2f)