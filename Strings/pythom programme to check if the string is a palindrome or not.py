"""12. python program to check if a string is a palindrome or not"""

a = str(input())
b = a[::-1]
if a==b:
    print("palindrome")
else:
    print("not a palindrome")