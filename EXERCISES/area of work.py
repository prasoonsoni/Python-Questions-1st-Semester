"""Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and 
then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR"."""

age = int(input("enter your age = "))
if 20<age<60:
    gender = str(input("enter your gender (m or f) = "))
    marital = str(input("enter your marital status (y or n) = "))

    if gender == "F" or gender == "f" :
        print("you can only work in urban areas")
    else:
        if gender == "m" and age>20 and age<40:
            print("you can work anywhere")
        else:
            if gender == "m" and age>40 and age<60:
                print("you can work only in urban areas")
else:
    print("ERROR")
    


