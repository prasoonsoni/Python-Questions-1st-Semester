"""python programme to remove the nth index character from a non empty string"""

a = input("Enter a Word? ")
l = len(a)
c = a[0:l-1:1]
print(c)