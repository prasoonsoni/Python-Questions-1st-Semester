"""Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but if the year is
 century year like 2000, 1900, 2100 then it must be divisible by 400."""
 
year = int(input("enter year = "))

if year%4==0 :
    print("leap year")
else:
    print("not a leap year")
