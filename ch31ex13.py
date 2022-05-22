N = 5
a = [[None] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        if i + j < N -1:
            a[i][j] = 11
        elif i + j > N - 1:
            a[i][j] = 88
        else:
            a[i][j] = 5

for i in range(N):
    for j in range(N):
        print(a[i][j])
