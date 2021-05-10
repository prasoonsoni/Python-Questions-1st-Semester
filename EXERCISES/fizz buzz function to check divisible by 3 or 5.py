"""Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number."""

num = int(input("Enter a number : "))
if num%3==0 and num%5==0:
    print("FizzBuzz")
else:
    if num%5==0:
        print("Buzz")
    else:
        if num%3==0:
            print("Fizz")
        else:
            print(num)