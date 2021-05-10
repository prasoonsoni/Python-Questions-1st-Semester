"""Sum of First Few Consecutive Prime Numbers
Given a number 'n', write an algorithm and a code to check if it can be written as sum of first few prime numbers. Print Yes if 'n' can be written as first few prime numbers and No otherwise. For example, if n is 5 then print Yes as it can be written as 2+3, if n is 41 then print Yes as it can be written as 2 + 3 + 5 + 7 + 11 + 13 and if n is 11 then print 'No' as it cannot be written as sum of first few prime numbers.

Note: C++ compilers can compile C code also

Input Format

First line contains the number, n

Output Format

First line contains Yes if the number n can be written as sum of first few prime numbers and No otherwise"""

n = int(input())
prime = []
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime.append(i)
count = 0
for i in prime:
    count+=i
    if count == n:
        print("Yes")
        break
else:
    print("No")