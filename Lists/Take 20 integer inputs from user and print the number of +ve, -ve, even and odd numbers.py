"""Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0s."""

pve = 0
nve = 0
odd = 0
even = 0
l = []
for i in range(0,20):
    i = int(input("Enter Numbers : "))
    l.append(i)
for j in l:
    if j>0:
        pve+=1 # pve =pve+1
print("POSITIVE NUMBERS = ", pve)
for k in l:
    if k<0:
        nve+=1
print("NEGATIVE NUMBERS = ", nve)
for m in l:
    if m%2!=0:
        odd+=1
print("ODD NUMBERS = ", odd)
for p in l:
    if p%2==0:
        even+=1
print("EVEN NUMBERS = ", even)
