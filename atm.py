def calcnotes():
    money = int(input("How much money do you need?"))
    tens,x = divmod(money,10)
    fives,y = divmod(x,5)
    ones,z = divmod(y,1)
    print("Dispensing ", tens, " tens, ", fives, " fives, and ", ones, " ones.")
          
pin_correct = "1234"
pin_entered = input("Please enter your PIN:")
if pin_entered != pin_correct:
    print("Sorry that's not the right PIN.")
    pin_entered = input("Please enter your PIN:")
    if pin_entered != pin_correct:
        print("Sorry that's not the right PIN. One more try.")
        pin_entered = input("Please enter your PIN:")
        if pin_entered != pin_correct:
            print("Sorry, this PIN is still not correct.Your account is locked now.")
        else:
            calcnotes()
    else:
        calcnotes()
else:
    calcnotes()
