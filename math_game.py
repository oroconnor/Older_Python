import random
import operator

counter = 0
score = 0
operation_options = {"+":operator.add,
                     "-":operator.sub,
                     "*":operator.mul,
                     "/":operator.truediv}
                        
while counter < 10:
    choosen_operation = random.choice(list(operation_options.keys())) 
    number_1 = random.randint(0,9)
    if choosen_operation == "/":
        number_2 = random.randint(1,9)
    else:
        number_2 = random.randint(0,9)
    user_answer = int(input("{} {} {} =\n".format(number_1, choosen_operation, number_2)))
    correct_answer = eval(str(number_1) + choosen_operation + str(number_2))
    if correct_answer == user_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(correct_answer)

    counter += 1
    
print("Your score was " + str(score) + " out of 10.")
