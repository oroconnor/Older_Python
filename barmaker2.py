#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:59:08 2020

@author: owenoconnor

Creates a series of bernoulli trials to display a normal distribution. 

"""


from collections import Counter
import random
from matplotlib import pyplot as plt

nums = []

for i in range(100000):
    count = 0
    for a in range(100):
        a = random.randint(0,1)
        count += a
    nums.append(count)
    
histogram = Counter(nums)

plt.bar([x + 5 for x in histogram.keys()],histogram.values(),1, edgecolor = (0,0,0))

plt.show

