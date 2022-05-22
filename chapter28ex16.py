a = int(input("a:"))
while a != -1:
    while True:
        b = int(input("b:"))
        if b > a: break
    i = a
    while i <= b:
        print(i)
        i += 1
    a = int(input("a:"))
   
