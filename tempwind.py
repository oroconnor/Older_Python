

temp = int(input("What is the temperature today?:"))
wind = int(input("What is the wind speed today?:"))
a = "It is hot and "
b = "It is cold and "
c = "windy today!"
d = "not windy today!"
if temp > 75:
    x = a
else:
    x = b
if wind > 12:
    y = c
else:
    y = d
print(x+y)

