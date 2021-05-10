""" Print multiplication table of 24, 50 and 29 using loop. """

a = int(input("Enter number whose table you want to get = "))
b = 1

while b>=1:
    print (a*b)
    b=b+1
    if b == 11:
        break
    