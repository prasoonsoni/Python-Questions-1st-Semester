"""Take 10 integer inputs from user and store them in a list. 
Again ask user to give a number. Now, tell user whether that number 
is present in list or not."""

l = []
for i in range(0,10):
    i = int(input("Enter a Number : "))
    l.append(i)
print(l)
a = int(input("enter a number you want to check : "))
if a in l:
    print("true")
else:
    print("false")