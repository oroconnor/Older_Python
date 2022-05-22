#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:04:18 2020

@author: owenoconnor
"""


### Allows you to simulate dominion games and see how different paths led to victory or defeat ###

import random

num_players = 3 #Adjust to model different numbers of players
game_num = 1 #Adjust to model different numbers of games
supply = []

#%%

def choose_action(): #selects what action(s), if any, to play from hand
    pass




            
#%%
    

        
class Cards:
    #Creating a class so that will hold the info about different cards and what they can do in the game
    def __init__(self, name, cost, coin_value = 0, victory_value = 0, supply_count = 10):
        self.name = name
        self.cost = cost
        self.coin_value = coin_value
        self.victory_value = victory_value
        self.supply_count = supply_count
        global supply
        supply.append(self)
        
    def print_card(self):
        print("name = ", self.name)
        print("cost = ",self.cost)
        print("coin_value = ",self.coin_value)
        print("victory_value = ",self.victory_value)
        print("supply_count = ", self.supply_count)
            
#%%
### In this section, we're going to initialize all the cards we need to get started.
curse_count = (num_players - 1) * 10
if num_players == 2:
    victory_starter = 8
else:
    victory_starter = 12

silver = Cards("silver",3,2,0,40)
copper = Cards("copper",0,1,0,60)
gold = Cards("gold",6,3,0,30)
curse = Cards("curse",0,0,-1,curse_count)
estate = Cards("estate",2,0,1,victory_starter)
duchy = Cards("duchy",5,0,3,victory_starter)
province = Cards("province",8,0,6,victory_starter)

#%%

class Player:
#Creates a class of players to keep track of invidual players and their cards
    deck = [estate, estate, estate, copper, copper, copper, copper, copper, copper, copper]
    hand = []
    cards_played = []
    discard = []
    winner = False

    def __init__(self, name):
        self.name = name
        
    
    def print_player(self):
        deck_names = []
        for i in self.deck:
            deck_names.append(i.name)
        print("deck = ", deck_names)
        print("hand = ",self.hand)
        print("cards_played = ",self.cards_played)
        print("discard = ",self.discard)

#%%
def deal_five(player): 
    """Takes five cards from 'top' of deck and deals them to player's hand"""
    for i in range(5):
        if len(player.deck) == 0:
            shuffle_deck(player)
        a = player.deck.pop()
        player.hand.append(a)
        
def shuffle_deck(player):
    """Shuffles the player's discard pile to replenish deck"""
    player.deck = random.shuffle(player.discard)


def clean_up(player):
    """Takes cards in hand and in cards_played and adds them to discard pile"""
    for i in player.hand:
        b = player.hand.pop()
        player.discard.append(b)
        
    for j in player.cards_played:
        c = player.cards_played.pop()
        player.discard.append(c)

#%%

def make_purchase(player): #selects what card(s), if any, to purchase 
    hand = player.hand
    coin_count = 0
    for i in hand:
        coin_count += i.coin_value
    print(coin_count)
    options = []
    for x in supply:
        if x.supply_count > 0 and x.cost <= coin_count and x.name != "curse": #Excludes curse cards as an option to buy, while considering any other cards that can be afforded.
            i = x
            options.append(i)

    purchase = random.choice(options)
    player.cards_played.append(purchase)
    coin_count -= purchase.cost
    purchase.supply_count -= 1 
    
        
#%%
def action_play(player):
    """ The Action card playing phase of player's turn"""
    options = []
    for x in player.hand:
        if x.action == True:
            i = x
            options.append(i)
    action_choice = random.choice(options)
#   play_action(action_choice) #Executes the special rules of the action card
    #return extra_coin    


#%%
def turn(player):
    deal_five(player)
#    action_play(player)
#    make_purchase(player)
    clean_up(player)

#%%
    
    
def check_end():
    if province.supply_count == 0:
        return True
    count_zero = 0
    for x in supply:
        if x.supply_count == 0:
            count_zero += 1
    if count_zero >= 3:
        return True
    


#%%
    
def play_game(game_num,num_players):
    """Main code of an individual game"""
    #initiate the players
    players = []
    for i in range(num_players):
        name = str("player" + str(game_num) + ":" + str(i))
        a = Player(name)
        players.append(a)
        
    while True:
        for j in players:
            turn(j)
            if check_end() == True: break
            print("testing)")
    return players    
    

    
#OK. Here's really the main code:

# for x in range(game_num):
#     play_game(game_num,num_players)
    
#%%
play_game(game_num,num_players)
#%%



