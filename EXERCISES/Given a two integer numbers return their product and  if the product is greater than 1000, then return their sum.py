""" Question 1: Given a two integer numbers return their product and  
if the product is greater than 1000, then return their sum """

a = int(input("enter no 1 : "))
b = int(input("enter no 2 : "))

c = a*b
d = a+b
if a*b > 1000:
    print ("THE PRODUCT OF TWO NUMBER IS : ", c , "and", "THE SUM OF TWO NUMBER IS : " ,d)
else:
    print (c)