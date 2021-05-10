salary =  int(input("salary - "))
experience = int(input("experience - "))
if salary<0 or experience<0:
    print("invalid input")
else:
    salary_10yrs = 0.1*salary + salary
    salary_5yrs = 0.05*salary + salary
    otherwise = 0.03*salary + salary
    if experience>10:
        print (int(salary_10yrs))
    else :
        if experience>5 and experience <10 :
            print(salary_5yrs)
        else:
            print(otherwise)
    