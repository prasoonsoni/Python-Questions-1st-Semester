def foo(b):
    c = 0
    z = 1
    for i in range(z,b):
        y = ((b%i)==0)
        y = int(y)
        c = c*y*i
        d = ((b-c)==0)
        if (d is True):
            return d
        else:
            return False

a = int(input())
f = foo(int(a))
print(f)