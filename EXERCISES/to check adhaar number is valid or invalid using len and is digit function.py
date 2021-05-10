"""check addhar number from user and check whether addhar number is valid or 
not valid"""
"""PAC
input-- adhar number
output-- valid or not"""

"""alogrithm
READ adhaar
IF lenght!=12
THEN PRINT "invalid"
ELSE
FOR X = 0 TO 11
    IF adhaar[i]is not a digit THEN
        PRINT"invalid"
        break
    END IF
END FOR
PRINT"valid"   """

number = str(input(" ENTER YOUR ADHAAR NUMBER :- "))
lenght = len(number)##len is used to check lenght of function
if lenght==12 and number.isdigit :
    print("Valid !!")
else:
    print("Invalid !!")
    