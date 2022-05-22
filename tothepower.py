#Calculates x to the power of y without using **
x = float(input("Please enter a real number:"))
y = int(input("Please enter an integer:"))
z = x
for j in range(1,y):
    z = z * x
print("Your result is:",z)
