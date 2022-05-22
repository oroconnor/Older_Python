ROWS = 4
COLUMNS = 3
a = [[None] * COLUMNS for i in range(ROWS)]
for i in range(ROWS):
    for j in range(COLUMNS):
        print("Enter a number for indices", i, ",",j,":")
        a[i][j] = float(input())

for i in range(ROWS):
    for j in range(COLUMNS):
        if a[i][j] % 2 == 0:
            print(i,j)
