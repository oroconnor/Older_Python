
for i in range (999,10000):
    a,b = divmod(i,1000)
    b,c = divmod(b,100)
    c,d = divmod(c,10)
    if a > b and b ==c and c < d:
          print(i)
