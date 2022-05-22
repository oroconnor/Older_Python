#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:48:51 2020

@author: owenoconnor
"""


import csv
from matplotlib import pyplot as plt
import statistics as st

filename = "watershed-water-quality-data.csv"
titles = []
rows = []

date = []
avgturb = []
turb12am = []

with open(filename) as f:
    csv_reader = csv.reader(f)
    fields = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
        
    
print("Total num of rows: %d"%(csv_reader.line_num),"\n" )

print("Field names are:", fields, "\n")
print("First 10 rows:")
    
for row in rows[:10]:
    for col in row:
        print(col, end = "\t"),
    print("\n")
        

for row in rows[:500]:
    date.append(row[1])
    avgturb.append(float(row[8]))
    turb12am.append(row[2])



plt.plot(date,avgturb)
plt.title("Turbity - 24 hr avgs")
plt.xlabel("Dates")
plt.ylabel("Turbity avg")
plt.show

#%%

def sumstats(x):
    count = len(x)
    mean = st.mean(x)
    mode = st.mode(x)
    median = st.median(x)
    variance = st.variance(x)
    sd = st.stdev(x)
    print("Number of values:", count)
    print("mean:",mean,"\nmode:",mode,"\nmedian:",median)
    print("Variance:", variance)
    print("Standard Deviation:", sd)
    
sumstats(avgturb)

histogram = Counter(avgturb)
plt.bar(histogram.keys(),histogram.values(), .01, edgecolor = (0,0,0))
plt.title("Turbity - 24 hr avg - Histogram")
plt.show

#%%

plt.scatter(turb12am,avgturb)
plt.show