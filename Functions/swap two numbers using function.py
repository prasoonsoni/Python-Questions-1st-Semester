def swap(a,b):
    (a,b) = (b,a)
    print(a,b)
a=int(input())
b=int(input())
swap(a,b)

def swap():
    a = int(input())
    b = int(input())
    a,b = b,a
    print(a,b)
swap()

def swap():
    a = int(input())
    b = int(input())
    a,b = b,a
    return(a,b)
print(swap())

