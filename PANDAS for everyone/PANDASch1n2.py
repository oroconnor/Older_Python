#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:06:35 2020

@author: owenoconnor
"""


import pandas as pd

df = pd.read_csv("/Users/owenoconnor/Documents/scripts/PANDAS for everyone/gapminder.tsv", sep = "\t")
print(df.head())
print(df.tail())

print(df.shape)

#%%

print(df.columns)

subset = df[["country", "continent", "year"]]
print(subset.head())

#%%
print(df.loc[0])

print(subset.tail(n=8))

#%%
subset = df.iloc[:,[2,4,-1]]
print(subset.head())

#%%
subset = df.iloc[:, :3]
print(subset.head())

#%%
subset = df.iloc[400:405,[0,2,5]]
print(subset)

#%%

print(df.loc[42,"country"])

print(df.groupby("year")["lifeExp"].mean())

multi = df.groupby(["year","continent"])[["lifeExp","gdpPercap"]].mean()
print(multi)

#%%
print(df.groupby("continent")["country"].nunique())

#%%
global_yle = df.groupby("year")["lifeExp"].mean()
print(global_yle)
global_yle.plot()


#%%
s = pd.Series(["banana",42], index = ["Fruit", "Number"])
print(s)


#%%

print(global_yle.mean())

