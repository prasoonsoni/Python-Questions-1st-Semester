"""11. python program  to count the number of lowercase character in the string"""

a = str(input())
count=0
for i in a:
    if i.islower():
        count+=1
print(count)

