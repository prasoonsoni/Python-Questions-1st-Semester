# write a program to print prime numbers using def

def prime (a,b):
    for i in range(a, b+1):
        if i > 1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
                    
a = int(input())
b = int(input())
prime(a,b)

    