n = int(input("Enter no of steps = " ))

for i in range(n-1, -1, -1):
    for j in range(0 , i+1):
        print("*", end=" ")
    print()