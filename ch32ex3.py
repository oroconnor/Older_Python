PLAYERS = 6
MATCHES = 3
a = [[None] * MATCHES for i in range(PLAYERS)]
for i in range(PLAYERS):
    for j in range(MATCHES):
        a[i][j] = int(input("Number of scores that Player " + str(i+1) + " had in match " + str(j+1) +":"))
for i in range(PLAYERS):
    p = 0
    for j in range(MATCHES):
        p += a[i][j]
    print("Total points for Player", i + 1,"is:",p)

for j in range(MATCHES):
    m = 0
    for i in range(PLAYERS):
        m += a[i][j]
    print("Total points for Match", j + 1,"is:",m)
