"""break 
continue 
pass (control statements)"""
# using continue
a = 10
while a>0:
    a=a-1
    if a==5:
        continue
    print(a)
print("good bye")


#using break
a = 10
while a>0:
    print(a)
    a=a-1
    if a==5:
        break
    print(a)
print("good bye")