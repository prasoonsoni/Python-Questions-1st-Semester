# TOTAL NO OF CHOCOLATE THE PERSON CAN BUY



n = float(input("ENTER AMOUNT MONEY YOU HAVE : "))
c = float(input("AMOUNT OF CHOCOLATE : "))
m = int(input())
# CALCULATE NO OF CHOCOLATES BOUGHT
p = n//c
# CALCULATE NO OF FREE CHOCOLATES
f = p//m
CHOCOLATE = p+f
print ("TOTAL NO OF CHOCOLATE : ",(CHOCOLATE))
