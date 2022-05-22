import random
correct_number = random.randint(0,9)
one_more = correct_number + 1
one_less = correct_number -1
guess1 = int(input("I'm thinking of a number 0-9. Try to guess it. I'll give you three tries:"))

if guess1 == correct_number:
    print("Amazing! You guessed it on the first try!")
elif guess1 == one_more or guess1 == one_more:
    guess2 = int(input("That's not it, but you're really close. Try again:"))
    if guess2 == correct_number:
        print ("Hey, you got it!")
    elif guess2 == one_more or guess2 == one_less:
        guess3 = int(input("That's not it, but you're really close. Try one last time:"))
        if guess3 == correct_number:
            print("Alright, you guessed it!")
        else:
            print("That's not it. The number was", correct_number, ". Well, thanks for playing!")
    else:
        guess3 = int(input("Sorry. Guess one last time:"))
        if guess3 == correct_number:
            print("Alright, you guessed it!")
        else:
            print("That's not it. The number was", correct_number, ". Well, thanks for playing!")    
else:
    guess2 = int(input("Sorry. That's not right. Guess again:"))
    if guess2 == correct_number:
        print ("Hey, you got it!")
    elif guess2 == one_more or guess2 == one_less:
        guess3 = int(input("That's not it, but you're really close. Try again:"))
        if guess3 == correct_number:
            print("Alright, you guessed it!")
        else:
            print("That's not it. The number was", correct_number, ". Well, thanks for playing!")
    else:
        guess3 = int(input("Sorry. Guess one last time:"))
        if guess3 == correct_number:
            print("Alright, you guessed it!")
        else:
            print("That's not it. The number was", correct_number, ". Well, thanks for playing!")



    
    
