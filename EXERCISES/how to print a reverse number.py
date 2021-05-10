n = int(input(" enter a number = "))
i=10
rev=0
while(n%i!=0):
    d=n%i
    rev = (rev*10) + d
    n= n//i
print(rev)