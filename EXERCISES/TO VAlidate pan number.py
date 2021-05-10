"""to validate pan number""" # lenght = 10digits

# PAN NUMBER - first 5 characters are letters, next 4 are digits and last character alphabet
#USING REGULAR EXPRESSION
import re
num = input()
a = len(num)
if a ==10 and re.match("[A-Z]{5}[0-9]{4}[A-Z]", num):
    print("valid")
else:
    print("invalid")
    
    
#USING SLICING

num = input()
a = len(num)
b = num[0:5]
c = num[5:9]
d = num[-1]
if a ==10 and b.isupper() and c.isdigit() and d.isupper():
    print("valid")
else:
    print("invalid")