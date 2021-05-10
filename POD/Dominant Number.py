"""Dominanat Number
Given two numbers print the dominant number. A number is said to be dominant over the other if the sum of proper factors of the number is greater than the sum of proper factors of the other. Factors of a number excluding 1 and itself are called proper factors. Print 'No dominance' when the sum of the proper factors are same.

For example, fourteen is dominant over fifteen as sum of factors of 14 is 2+7 = 9 whereas sum of factors of 15 is 3+5 = 8. Whereas when the numbers 6 and 25 are considered there is 'No dominance' as they have the same sum of proper factors for the number 6 it is 2+3 = 5 and for the number 25 also it is 5.

Input Format

First line contains the first number, m

Second line contains the second number, n

Output Format

When sum of factors of numbers m and n are no equal, print the number with larger sum of proper factors and print No dominance when the sum of proper factors of m and n are equal"""





m = int(input("Number 1 : "))
n = int(input("Number 2 : "))
m_list = []
n_list = []
for i in range(2,m):
    if m%i==0:
        m_list.append(i)
for i in range(2,n):
    if n%i==0:
        n_list.append(i)
if sum(n_list) > sum(m_list):
    print(n)
elif sum(m_list) > sum(n_list):
    print(m)
else:
    print("No dominance")