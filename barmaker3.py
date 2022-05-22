#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:59:08 2020

@author: owenoconnor

Creates a series of dice rolls mimicking D and D charachter sheet rolls, and displays distribution.

"""


from collections import Counter
import random
from matplotlib import pyplot as plt

nums = []

for i in range(1000000):
    rolls = []
    for a in range(4):
        a = random.randint(1,6)
        rolls.append(a)
    dice = sorted(rolls)
    dice.pop(0)
    total = sum(dice)
    nums.append(total)
    

histogram = Counter(nums)

plt.bar(histogram.keys(),histogram.values(),1, edgecolor = (0,0,0))

plt.show

