"""Take 10 integers from keyboard using loop and print their average value 
on the screen."""


sum = 0
i = 10
while i>0:
    num = int(input("Enter a number = "))
    sum = sum + num
    i = i-1
print(sum/10)