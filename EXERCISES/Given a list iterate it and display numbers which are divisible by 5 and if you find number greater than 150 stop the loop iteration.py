"""Given a list iterate it and display numbers which 
are divisible by 5 and if you find number greater than 
150 stop the loop iteration"""

n = int(input("Number of inputs : "))
l = []
for i in range(0,n):
    x = int(input("Enter elements : "))
    l.append(x)
for j in l:
    if j>=150:
        break
    else:
        if j%5==0:
            print(j)