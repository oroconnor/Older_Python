#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:44:41 2020

@author: owenoconnor
"""


def Ftemp(ctemp):
    fartemp = 9/5 * ctemp + 32
    print(ctemp, "celsius is", fartemp, "degrees farenheit.")
    
    #%%
def namecity():
    fname = input("Enter first name:")
    lname = input("Enter last name:")
    city = input("Enter city:")
    state = input("Enter state:")
    print("Your name is",fname + " " + lname, "and you live in", city + ", " + state, ".")

#%%

def absnum(num):
    if num < 0:
        newnum = num * -1
    else:
        newnum = num
    print("The absolute value of", num, " equals", newnum)
    
#%%

def inch_to_feet(tot_inches):
    feet,inches = divmod(tot_inches,12)
    print(tot_inches,"inches is",feet,"feet,",inches,"inches.")