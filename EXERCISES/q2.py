r = int(input())
c = int(input())
matrix = []
for i in range(r):
    a = []
    for j in range(c):
        x = int(input())
        a.append(x)
    matrix.append(a)
sum_even = 0
sum_odd = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j%2==0:
            sum_even+= matrix[i][j]
        else:
            sum_odd+=matrix[i][j]


final = abs(sum_even-sum_odd)
print(final)