"""13. python program to calculate the number of uppercase letters and lowercase
letters in a string"""

a = str(input("Enter a Word ? "))
upper = 0
lower = 0
for i in a:
    if i.isupper():
        upper += 1
    elif i.islower():
            lower +=1
print("number of uppercase letters = ",upper)
print("number of lowercase letters = ",lower)
