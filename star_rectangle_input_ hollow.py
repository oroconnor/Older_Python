x = int(input("How many stars do you want on each side of your square?"))
for i in range(x):
    print("*  ", end = " ")
print("\n")
for j in range(x-2):
    print("*  ",end = " ")
    for i in range(x-2):
        print("   ", end = " ")
    print("*\n")
for y in range(x):
    print("*  ", end = " ")          
    
