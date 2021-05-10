"""IPS 8
Government of India has appointed two separate teams with three members each for investigating a case. After forming the two teams with three members each, as a cost-cutting measure, the government decides to merge the two teams in to a single team with five members, by eliminating the member with the least experience among all the six members from the two teams.  Use dictionaries to store the two teams and form a new team by concatenating the two teams. The chairperson of the new team is the person with the maximum experience. Design an algorithm and write the subsequent Python code to store the members  of the two teams as dictionaries, print the new (concatenated) dictionary with the names in an increasing order of experience, to check whether a given name is present in the new dictionary or not and to print the name of the chairperson of the new team.
Note: Assume that there is only one person with least experience in the two dictionaries.
Input format:
Enter the details of the first team
Name of the first member
Experience (in years) of the first member
...
....
Name of  the third member
Experience (in years) of the third member
Enter the details of the second team:
Name of the first member
Experience of the first member
....
....
Name of the third member
Experience of the third member
Enter the name to be checked in the new team
Output format:
Exists or Does not  Exist
New team with experience as key value
Name of the person who is having maximum experience
[Hint: use pprint function for printing dictionary in sorted order.
Syntax for pprint is
pprint(dictionary name)
Include the line “from pprint import pprint” in the top of your program"""
from pprint import pprint
t1 = {}
t2 = {}
for i in range(3):
    name1 = input()
    exp1 = int(input())
    t1[name1] = exp1
for i in range(3):
    name2 = input()
    exp2 = int(input())
    t2[name2] = exp2
t1.update(t2)
new_dict = dict([(value, key) for key, value in t1.items()])
m = min(new_dict.keys())
new_dict.pop(m)
new_dict1 = dict([(value, key) for key, value in new_dict.items()])
pprint(new_dict1)























