a = int(input("Enter NUM1 : "))
b = int(input("Enter NUM2 : "))
c = int(input("Enter NUM3 : "))

if a>b and a>c:
    print(a, "is greatest")
else:
    if b>c :
        print(b, "is greatest")
    else:
        print(c, "is greatest")