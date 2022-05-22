#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:37:49 2020

@author: owenoconnor
"""

tttarray = [None] * 3
tttarray[0] = [1,2,3]
tttarray[1] = [4,5,6]
tttarray[2] = [7,8,9]

def display_array():
    for i in range(3):
        for j in range(3):
            print(tttarray[i][j], end = "    ")
        print("\n")

def user_choice():
    while True:
        try:
            choice = int(input("Enter your move:"))       
        except ValueError:
            print("Not an integer! Try again.")
            continue

        else:
            return choice 
            break 
     
def check_value(choice, array):
    counter = 0
    while True:
        for i in range(3):
            for j in range(3):
                if array[i][j] == choice:
                    counter += 1
        if counter == 0:
            print("Choice not available. Try again.")
            choice = user_choice()
            return choice
        else:
            return choice
            break
        
def turn(player):
    print("Player", player,"'s turn.")
    choice = user_choice()
    choice = check_value(choice, tttarray)
    for i in range(3):
        for j in range(3):
            if tttarray[i][j] == int(choice):
                tttarray[i][j] = player
    print("\n")
    display_array()           


#Checks for "the cat" winning the game
def check_cat():
    winner = None
    count = 0
    for i in range(3):
        for j in range(3):
            s = str(tttarray[i][j])
            if s.isdigit():
                count += 1
    if count == 0:
        winner = "'The Cat'"        
    return winner 
        
playerX = "X"
playerO = "O"
winner = None

def tttcheck(player):
    winner = None
    for i in range(3):
        if tttarray[i][0] == player and tttarray[i][1] == player and tttarray[i][2] == player:
            winner = player
    for j in range(3):
        if tttarray[0][j] == player and tttarray[1][j] == player and tttarray[2][j] == player:
            winner = player 
    if tttarray[0][0] == player and tttarray[1][1] == player and tttarray[2][2] == player:
            winner = player
    if tttarray[0][2] == player and tttarray[1][1] == player and tttarray[2][0] == player:
            winner = player
    
    return winner
    
    
print("TIC TAC TOE!!!")
print("\n")    
display_array()

while winner == None:    
    turn(playerX)
    winner = tttcheck(playerX)
    if winner != None: break
    winner = check_cat()
    if winner != None: break
    turn(playerO)
    winner = tttcheck(playerO)
    winner = check_cat()
    
print("Winner is player", winner,"!!!")

#%%
    