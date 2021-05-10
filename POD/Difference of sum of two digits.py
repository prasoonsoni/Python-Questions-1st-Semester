"""Difference of the sum of alternate digits
Given a positive integer 'x' (with even number of digits in it), write an algorithm and the subsequent code to compute the difference between  the sum of the digits occuring in the alternate positions (starting from the first position) and the sum of the digits occuring in the alternate positions,starting from the last rightmost position of 'x'
For example, consider the number  8975.  The sum of the digits that occur in the alternate positions from the first position is 8+7=15.  The sum of the digits that occur in the alternate positions, starting from the rightmost position is 5+9 = 14. Difference between the two sums is 1 (=15-14).  Similarly, for the number 5798, the difference between  two sums, is 1.  
Note: Read the input as a number and do entire processing as  a number
C++ compilers can compile C code also
Input format 
First line contains the positive integer
Output format :
First line should contain the difference between  the sum of the digits occuring in the alternate positions (starting from the first position) and the sum of the digits occuring in the alternate positions (startting from the last rightmost position)."""


n = input()
n_list = []
f_n = []
l_n = []
for i in range(0,len(n)):
    if i%2==0:
        f_n.append(int(n[i]))
    else:
        l_n.append(int(n[i]))

difference = abs(sum(f_n)-sum(l_n))
print(difference)