#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 14:36:41 2018

@author: gcu
"""

import pandas as pd 
from collections import Counter # the Counter library

data = pd.read_csv('pnp-train.txt',delimiter='\t',encoding='latin-1', # utf8 encoding didn't work for this
                  names=['type','name']) # supply the column names for the dataframe

# this next line creates a new column with the lower-cased first word
data['first_word'] = data['name'].map(lambda x: x.lower().split()[0])
data.describe()

Counter(data)

counts = Counter(data) # just pass in the list and see what happens
counts.most_common()

counts
#P(T='MV')=0.29817627732012764