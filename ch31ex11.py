#calculates the total of the values at indices with even rows  and odd columns

ROWS = 4
COLUMNS = 3
total= 0
a = [[None] * COLUMNS for i in range(ROWS)]
for i in range(ROWS):
    for j in range(COLUMNS):
        print("Enter a number for indices", i, ",",j,":")
        a[i][j] = float(input())

for i in range(ROWS):
    for j in range(COLUMNS):
        if i % 2 != 0 and j % 2 == 0:
            total += a[i][j]
            print(a[i][j])
            print(i,j)

print(total)
            
