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

import time

# import gmaps 
# import gmaps.datasets 


#%%


df1 = pd.read_csv("tenantsAtoK.txt", sep = "\n", parse_dates=True, skiprows=(34), header = None)
df2 = pd.read_csv("tenantsLtoZ.txt", sep = "\n", parse_dates=True, skiprows=(34), header = None)
df3 = pd.read_csv("Archivedtenants.txt", sep = "\n", parse_dates=True, skiprows=(34), header = None)

df = pd.concat([df1,df2,df3], ignore_index = True)



#%%

NaN = np.nan
df["Address"],df["Date"] = NaN, NaN
df["Counts"] = 1



#%%

 #use regex to qualify address and then dates and assign them to differnt columns
counter = 0


#%%
for i in range(0,18258,1):
    a = str(df.iloc[i,0])
    n = re.search("\d{1,2}\s\w+\s\d{4}", a)
    m = re.search("Kingston, NY", a)
   
    if m :  
        df.loc[[counter], 'Address'] =  df.iloc[i,0]
    if n:
        df.loc[[counter], 'Date'] =  df.iloc[i,0]
        counter += 1

df = df.drop([0],axis = 1)

#%%

df = df.dropna()


#%%
total_kingston_rows = df.shape[0]




#%%

geolocator = Nominatim(user_agent="tdevictions")

df["latitude"],df["longitude"] = NaN, NaN

for i in range(0,total_kingston_rows,1):
    if df.iloc[i,0] == NaN:
        continue
    address_string = str(df.iloc[i,0])
    
    location = geolocator.geocode(address_string)
    time.sleep(1.2)
    if location != None:
        df.loc[i, 'latitude'] = location.latitude
        df.loc[i, 'longitude'] = location.longitude

#%%

print(df.head(100))


#%%

df = df.dropna()
kingston_geocoded_rows = df.shape[0]
perc_converted = float(kingston_geocoded_rows) / float(total_kingston_rows)
#%%



#%%

#make hexbin plot
fig, ax = plt.subplots()
img= plt.imread("/Users/owenoconnor/Documents/scripts/evictions/map1.png")
hb = ax.hexbin(x=df["longitude"], y=df["latitude"], gridsize=30, cmap = "YlOrRd", alpha = .5)
ax.set_title("Evictions")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')
ax.imshow(img, extent=[-74.0258, -73.9637,41.9122, 41.9504], zorder=0)


#%%
#make bivariate kde plot
kde, ax = plt.subplots()
img= plt.imread("/Users/owenoconnor/Documents/scripts/evictions/map1.png")

ax = sns.kdeplot(data=df["longitude"], data2=df["latitude"],shade=True, levels=100, cmap = "YlOrRd", alpha = .5, zorder=1)
# sns.plt.ylim(41.9122, 41.9504)
# sns.plt.xlim(-74.0258, -73.9637)
ax.imshow(img, extent=[-74.0258, -73.9637,41.9122, 41.9504], zorder=0)


# gmaps.configure(api_key="AIzaSyAWLcKuHIca-IG0-dnuuQOj3stfnjYO3Ks")

# locations = df[["latitude", "longitude"]] 
# weights = df["Counts"] 
# fig = gmaps.figure() 
# heatmap_layer = gmaps.heatmap_layer(locations, weights=weights) 
# fig.add_layer(gmaps.heatmap_layer(locations, weights=weights)) 
# fig 

#%%
#make scatter plot
#map and bounds info from openstreetdata.org
scatter, ax = plt.subplots()
img= plt.imread("/Users/owenoconnor/Documents/scripts/evictions/map1.png")

ax = sns.scatterplot(x=df["longitude"], y=df["latitude"], s=100, alpha=.3 )
# ax = sns.plt.ylim(41.9122, 41.9504)
# ax = sns.plt.xlim(-74.0258, -73.9637)
ax.imshow(img, extent=[-74.0258, -73.9637,41.9122, 41.9504], zorder=0)