#This program calculates the hypotenuse of a triangle.
import math
print("Now we will calculate the hypotenuse of a right angle triangle from its two right angle side.")
a = float(input("What is the length of the first right angle side of the triangle?:"))
b = float(input("What is the length of the second right angle side of the triangle?:"))
c = math.sqrt(a**2 + b**2)
print("OK. Then the lenght of the hypotenuse is ", c, "!")
