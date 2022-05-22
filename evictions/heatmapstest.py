#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:48:13 2020

@author: owenoconnor
"""

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

import re
import numpy as np
from geopy.geocoders import Nominatim

import gmaps 
import gmaps.datasets 


#%%

gmaps.configure(api_key="AIzaSyAWLcKuHIca-IG0-dnuuQOj3stfnjYO3Ks")

earthquake_data = gmaps.datasets.load_dataset("earthquakes")


m = gmaps.Map()
m