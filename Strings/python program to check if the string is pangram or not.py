"""python program to check if the string is pangram 
or not"""


alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sentence = input("Enter your sentence :--> ")
l = []
for i in sentence:
    if i.isalpha():
        l.append(i)
        b = set(list(l))
        c = list(set(b))
        c.sort()

if c == alphabets:
    print("Pangram !")
else:
    print("Not a Pangram.")