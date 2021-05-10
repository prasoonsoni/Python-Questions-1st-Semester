"""Write a program to check if a given string is a Palindrome.
A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc."""



a = str(input("Enter a word to check if palindrome or not :-- "))

b = a[::-1]

if a==b:
    print("it is a palindrome")
else:
    print("not a palindrome")