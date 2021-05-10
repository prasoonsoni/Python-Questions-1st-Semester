r = int(input("enter number of rows = "))
c = int(input("enter number of columns = "))
print("Enter Element of first matrix : ")
matrix_a = [[int(input()) for i in range (c)] for i in range (r)]
print("Enter Elements of second matrix : ")
matrix_b = [[int(input()) for i in range (c)] for i in range (r)]
result = [[0 for i in range(r)] for i in range(c)]
for i in range(r):
    for j in range(c):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]
print("The sum of two matrices is : ")
for r in result:
    print(r)