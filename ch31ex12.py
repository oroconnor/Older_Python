N = 6
a = [[None] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        a[i][j] = int(input("Enter a number:"))

total = 0
antitotal = 0
for i in range(N):
    for j in range(N):
        if i == j:
            total += a[i][j]
avgdiag = total / N
print(avgdiag)

for i in range(N):
    j = N - i - 1
    antitotal += a[i][j]
avgantidiag = antitotal / N
print(avgantidiag)
        

