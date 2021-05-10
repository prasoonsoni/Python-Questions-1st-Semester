"""Given a range of first 10 numbers, Iterate from start 
number to the end number and print the sum of the current 
number and previous number"""

n = 10
l = []
for i in range(0,10):
    l.append(i)
    count = l[i] + l[i-1]
    print("Current Number : ",l[i],"Previous Number : ",l[i-1],"sum : ",count)
    