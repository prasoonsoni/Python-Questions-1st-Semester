n = int(input("How many elements you want to add in dictionery ? "))
d = {}
for i in range(1,n+1):
    print("Name",i," : ")
    x = input()
    print("Number",i," : ")
    y = int(input())
    d[x] = y 
print(d)

