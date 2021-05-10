n = int(input("Enter number of elements in list : "))
l = []
for i in range(n):
    x = input("Enter elements of list : ")
    if not x.isdigit():
        print("Invalid input")
        break
    else:
        l.append(int(x))
a = str(sum(l))
l1=[]
for i in a:
    l1.append(int(i))
b = sum(l1)
for i in range(n):
    l[i] = l[i] + b
l.append(int(a))
print(l)
   
    
    