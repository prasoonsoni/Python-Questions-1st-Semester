"""A company decided to give bonus of 5% to employee if his/her year of 
service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount."""


year = float(input("enter your year of service : "))
if year < 5:
    print("you are not eligible for bonus")
else:
    salary = float(input("enter your salary : "))
    bonus = salary * (0.05)
    new_salary = salary + bonus
    print("your bonus amount is : ", bonus)
    print("your salary with bonus is : ", new_salary)