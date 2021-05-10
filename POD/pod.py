"""Rahul is facing a unique problem, which he doesn't know how to solve. The problem asks him to build the smallest possible number by applying inversion on any digit of the number any number of times.
Inversion of a digit is defined as that digit being replaced by 9 minus that digit. Meaning that inversion of 9 will be 9 - 9 = 0 and inversion of 1 will be 9 - 1 = 8 and so on.
The final output should not have any leading zeroes.
Input Format:
The only line of the input contains an integer N
Output Format:
Print only one single integer on a line as described above.
Constraints:
1 <= N <= 10^18
Examples:
Input:
87
Output:
12
Explanation:
9-8 = 1
and 9 -7 = 2
if we see carefully, 12 is the smallest possible number we can get.
Example:
Input:
99
Output:
90
Explanation:
In this case, we do not replace the first 9 since it will lead to a leading zero."""

n =input()
n_list = []
f_list = []
for i in range(len(n)):
    n_list.append(int(n[i]))
if n_list[0]==9:
    for i in n_list:
        if i > 9-i:
            f_list.append(9-i)
        elif 9-i > i:
            f_list.append(i)
    f_list.pop(0)
    f_list.insert(0,9)
    for i in f_list:
        print(i,end="")
elif n_list[0]!=9:
    for i in n_list:
        if i > 9-i:
            f_list.append(9-i)
        elif 9-i > i:
            f_list.append(i)
    for i in f_list:
        print(i,end="")
    




















