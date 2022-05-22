#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:19:15 2020

@author: owenoconnor

Basic exploration and visualization of water quality data.

"""

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

from datetime import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/owenoconnor/Documents/scripts/water/Bard Water Lab/Sawkill_water_quality.csv", na_values = ["-999.00"])

df.index  = pd.to_datetime(df["Date"], errors = "coerce", dayfirst = True)
df = df.drop(["Date"], axis = 1)

#%%

print(df.columns, "\n")
print(df.head(15),"\n")
print(df.info())

#%%

sitedf = df.groupby("Date")['Temperature_C',
       'UncompensatedConductivity_C', 'Turbidity_NTU',
       'Enterococci_conc_CFU100ml', 'Tot_coliform_conc_CFU100ml',
       'EcoliConc_CFU100ml', 'Phyococyanin', 'CDOM', 'OB', 'Chlorophyll_a'].mean()

print(sitedf.head())
#%%
#Creating basic plots of each variable over the whole time series

def basicplot(dataf,column, waterbody):
    fig, ax = plt.subplots()
    ax.scatter(dataf.index,dataf[column])
    ax.set_title(column + " - " + waterbody)
    fig.set_size_inches([12,4])
    fig, ax = plt.subplots()
    ax.plot(dataf.index,dataf[column])
    ax.set_title(column + " - " + waterbody)
    fig.set_size_inches([12,4])

for x in sitedf.columns:
    basicplot(sitedf, x, "Sawkill Creek")
    
#%%
fig = sns.pairplot(sitedf)
fig.savefig("pairplot.jpg", bbox_inches = "tight")
#%%

fig = sns.pairplot(sitedf, kind="reg")
fig.savefig("pairplotreg.jpg", bbox_inches = "tight")

#%%
correlation = sitedf['Temperature_C'].corr(sitedf['UncompensatedConductivity_C'])
print(correlation)

#%%
def basiccorr(dataf,column1,column2):
    correlation = sitedf[column1].corr(sitedf[column2])
    print("Correlation between", column1, "and", column2," is:", correlation)

for x in sitedf.columns:
    for y in sitedf.columns:
        basiccorr(sitedf,x,y)
        
#%%
#Starting to think about how to remove seasonal effects from the data

# from statsmodels.graphics.tsaplots import acf,plot_acf
# df1= sitedf['Temperature_C']
# df1 = df1.resample('M').mean()
# print(df1)
# acf_array = acf(df1)
# plot_acf(acf_array, lags=10, alpha = .05)

