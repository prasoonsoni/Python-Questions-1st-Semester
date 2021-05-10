"""Take input of age of 3 people by user and 
determine oldest and youngest among them."""

age1 = int(input("AGE 1 = "))
age2 = int(input("AGE 2 = "))
age3 = int(input("AGE 3 = "))

if age1 > age2 and age1 > age3 :
    print(age1, "is oldest")
else:
    if age2 > age3:
        print(age2, "is oldest")
    else:
        print(age3, "is oldest")
        
        
if age1 < age2 and age1 < age3:
    print(age1, "is youngest")
else:
    if age2 < age3:
        print(age2, "is youngest")
    else:
        print(age3, "is youngest")
    

