"""The government of India has decided to give scholarships for students 
who are first graduates in family and have scored an average > 98 in math, 
physics, and chemistry. Design an algorithm and write a Python program to 
check if a student is eligible for a scholarship

Boundary Conditions: All marks should be >0"""

firstgraduate = int(input("if first graduate enter 1 if not enter 0 : "))
if firstgraduate != 1:
    print ("OOPS!! you do not qualify")
else:
    physics = int(input("enter physics marks : "))
    chemistry = int(input("enter chemistry marks : "))
    maths = int(input("enter maths marks : "))

    if physics<0 or chemistry<0 or maths<0:
        print ("invalid input")
    else:
            sum = physics + chemistry + maths 
            average = sum/3
            if average > 98:
                print("qualified")
            else:
                    print("not qualified")