#solves an equation in two ways
import math
x = float(input("enter a value for x:"))
w = float(input("enter a value for w:"))

temp1 = 3+w
temp2 = 6*x - 7 * (x+4)
temp3 = x**5 * math.sqrt(3*w+1)
temp4 = 5*x + 4
temp5 = (x**3 + 3) * (x-1)**7
y = (temp1/temp2) + temp3 + (temp4/temp5)
print("the value of y is ",y)
z = ((3+w)/(6*x - 7 * (x+4))) + (x**5 * math.sqrt(3*w+1)) + ((5*x + 4)/((x**3 + 3) * (x-1)**7))
print("the value of z is ",z)
