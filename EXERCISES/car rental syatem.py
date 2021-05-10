days = int(input("Enter number of days = "))
kilometers = int(input("Enter number of kilometers = "))
a = days * 4000
b = (1500*days) + (9*kilometers)
if days<0 or kilometers<0:
    print("invalid input")
else:
    if a > b:
        print("plan 2")
    else:
        print("plan 1")

        
    