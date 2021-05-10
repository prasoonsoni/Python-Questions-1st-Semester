"""Given a string of odd length greater 7, return a string made of the middle three chars of a given String"""

a = str(input("Enter a Name::-- "))
n = len(a)
n1 = int((n-3)/2)
n2 = int((n+3)/2)
if n%2!=0 and n>7:
    m = a[n1:n2:1]
    print(m)
else:
    print("error")