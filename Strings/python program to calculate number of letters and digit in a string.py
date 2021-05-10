"""16. python program to calculate number of letters and digit in a string"""

a = str(input())
digit = 0
letter = 0
for i in a:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
print("number of digit = ", digit)
print("number of letter = ", letter)