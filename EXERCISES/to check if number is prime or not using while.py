# to check whether given no is prime or not#

num = int(input())
i = 2
while(i<num):
    if num%i==0:
        print("not a prime")
        break
    i+=1
else:
    print("prime")