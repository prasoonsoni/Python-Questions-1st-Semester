"""python programme to to calculate the number of words and number of characters
in a string"""
a = str(input())
c1 = 0
c2 = 0
for i in a:
    if i.isalpha():
        c1+=1
    elif i.isdigit():
        c2+=1
print("number of characters = ", c1)
print("number of digits = ", c2)