#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:59:08 2020

@author: owenoconnor

Creates an series of random trials that are evenly distributed.
"""


from collections import Counter
import random
from matplotlib import pyplot as plt


nums = []

for i in range(100000):
    a = random.randint(1,6)
    nums.append(a)
    
histogram = Counter(nums)

plt.bar([x for x in histogram.keys()],histogram.values(),1, edgecolor = (0,0,0))

plt.show
#%%
