num = int(input("Please enter a number:"))
x = 1
y = 0
z = 0
for i in range(num):
        z = y
        y = x
        x = y + z
        print(x)
        
        
        
