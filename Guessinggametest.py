import random
correct_number = random.randint(0,9)
one_more = correct_number + 1
one_less = correct_number -1
print(correct_number)
print(one_more)
print(one_less)
if one_more == 5 or one_more == 6:
    print("Getting Close")
else:
    print("all done")
