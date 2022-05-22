full_name = input("Enter your full name: ")

space_pos = full_name.find(" ")

name1 = full_name[:space_pos]

name2 = full_name[space_pos + 1:]

print("First name:", name1)
print("Last name:", name2)

