ROWS = 3
COLUMNS = 3
a = [16,12,3,5,6,9,18,19,20]
b = [[None] * COLUMNS for i in range(ROWS)]
k = 0
for i in range(ROWS):
    for j in range(COLUMNS):
        b[i][j] = a[k]
        k += 1

for i in range(ROWS,0,-1):
    print(i)
