# regersive function
def fact(x):
    if(x==1):
        return 1
    else:
        a = (x*fact(x-1))
        return a
n = int(input())
z = fact(n)
print(z)
