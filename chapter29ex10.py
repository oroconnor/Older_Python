for x in range(-10,10):
    for y in range(-10,10):
        for z in range(-10,10):
            if ((x + y) / 2) + (3 * (z ** 2))/(x + 3*y + 45) == (x/3):
                print(x,"\t",y,"\t",z)
