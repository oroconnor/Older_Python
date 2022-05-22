#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:13:01 2020

@author: owenoconnor
"""
#Converted pdf to .txt document with www.pdf2go.com
#document source: Kingston Landlord Support


import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

import re
import numpy as np
from geopy.geocoders import Nominatim


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns


# import gmaps 
# import gmaps.datasets 


#%%


df = pd.read_csv("tenantsAtoK.txt", sep = "\n", parse_dates=True, skiprows=(34), header = None)

NaN = np.nan
df["Address"],df["Date"] = NaN, NaN
df["Counts"] = 1

 #use regex to qualify address and then dates and assign them to differnt columns
counter = 0

for i in range(0,486,1):
    a = str(df.iloc[i])
    n = re.search("\d{1,2}\s\w+\s\d{4}", a)
    m = re.search(", NY", a)
   
    if m :  
        df.loc[[counter], 'Address'] =  df.iloc[i,0]
    if n:
        df.loc[[counter], 'Date'] =  df.iloc[i,0]
        counter += 1

df = df.drop([0],axis = 1)


#%%

geolocator = Nominatim(user_agent="tdevictions")

df["latitude"],df["longitude"] = NaN, NaN

for i in range(0,486,1):
    if df.iloc[i,0] == NaN:
        continue
    address_string = str(df.iloc[i,0])
    
    location = geolocator.geocode(address_string)
    if location != None:
        df.loc[[i], 'latitude'] = location.latitude
        df.loc[[i], 'longitude'] = location.longitude

#%%




df = df.dropna()

fig, ax = plt.subplots()
hb = ax.hexbin(x=df["longitude"], y=df["latitude"], gridsize=7, cmap = "YlOrRd", alpha = .5)
ax.set_title("Evictions")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')



#%%
kde, ax = plt.subplots()
img= plt.imread("/Users/owenoconnor/Documents/scripts/evictions/ulster.png")

sns.kdeplot(data=df["longitude"], data2=df["latitude"], shade=True,cmap = "YlOrRd", alpha = .5, thresh=0, levels=90, zorder=1)
ax.imshow(img, extent=[-74.7, -73.7,41.2, 42.4], zorder=0)


# gmaps.configure(api_key="AIzaSyAWLcKuHIca-IG0-dnuuQOj3stfnjYO3Ks")

# locations = df[["latitude", "longitude"]] 
# weights = df["Counts"] 
# fig = gmaps.figure() 
# heatmap_layer = gmaps.heatmap_layer(locations, weights=weights) 
# fig.add_layer(gmaps.heatmap_layer(locations, weights=weights)) 
# fig 

