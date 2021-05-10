"""Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n
E.g.-
4! = 1*2*3*4 = 24
3! = 3*2*1 = 6
2! = 2*1 = 2
Also,
1! = 1
0! = 1
Write a program to calculate factorial of a number. """

n = int(input("enter a number = "))

fact = 1
for n in range(1,n+1,1):
    fact = fact*n
print(fact)
