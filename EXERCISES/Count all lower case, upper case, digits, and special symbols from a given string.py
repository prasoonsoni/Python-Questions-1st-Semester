"""Count all lower case, upper case, digits, and special symbols from a given string"""

a = str(input())
charcount = 0
numcount = 0
specount = 0
for i in a:
    if i.isalpha():
        charcount+=1
    elif i.isdigit():
        numcount+=1
    else:
        specount+=1
print("Total Characters = ",charcount, "Total Numbers = ",numcount, "Total Special Characters = ",specount)
        