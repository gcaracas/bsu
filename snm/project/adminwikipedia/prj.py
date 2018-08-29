#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:17:15 2018

@author: gcu
"""

# Needed packages
import glob
import os
import re
import pandas as pd
import numpy as np
from collections import Counter

path_to_files="data/"
files = glob.glob(path_to_files+"*.txt")
files

finalDataframe = pd.DataFrame()
sections = []
for file in files:
    with open(file, mode="r") as f:
        lines = f.read()
sections = re.split("gerardocaracas\n",lines)

def extract(string):
    keys=[]
    vals=[]
    res=dict()
    data = string.split('\n')
    for eachrow in data:
        if eachrow != '':
            print(eachrow)
            key, pairs =  eachrow.split(':::')
            keys.append(key)
            vals.append(pairs)
    res=dict(zip(keys,vals))
    return res


final = []
counter = 0
for liststr in sections:
    # Remove empty strings
    
    finaldict = extract(liststr)
    counter = counter + 1
    if counter == 1:
        finalDG = pd.DataFrame.from_records([finaldict])
    else:
        tmp = pd.DataFrame.from_records([finaldict])
        finalDG = finalDG.append(tmp, ignore_index=True)

import  pickle
with  open("myData.pickle","wb") as oFile:
    pickle.dump(finalDG, oFile)
    
    