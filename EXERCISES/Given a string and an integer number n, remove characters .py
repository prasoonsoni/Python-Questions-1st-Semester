"""Given a string and an integer number n, remove characters 
from a string starting from zero up to n and return a new string"""

a = input("Enter String: ")
n = int(input("Enter 'n': "))
b = a[n:-1] + a[-1]
print(b)