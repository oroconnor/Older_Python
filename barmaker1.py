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

for i in range(1000):
    a = random.randint(0,99)
    nums.append(a)
    
histogram = Counter(min(number//10 * 10, 90) for number in nums)

plt.bar([x + 5 for x in histogram.keys()],histogram.values(),10, edgecolor = (0,0,0))

plt.show