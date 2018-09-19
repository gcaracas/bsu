#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:13:41 2018

@author: gcu
"""

import glob
import os
import re
import pandas as pd
import numpy as np
from collections import Counter
path = "files/"
files = glob.glob(path+"*.txt")

# first we need a list of all words in all files.
finalDataframe = pd.DataFrame()
for file in files:
    with open(file, mode="r") as f:
        data = f.read()
        # Split data into array of words, non case sensitive
        word = re.split(r"\W+", data,  flags=re.IGNORECASE)
        # Remove withe spaces and empty strings
        cleanWords = [line for line in [l.strip() for l in word] if line]
        # Remove duplicates, we don't want them
        words = list(set(cleanWords))
        # Add data into dictionary
        dictionary = {"filename":file, "values":pd.Series(words)}
        finalDataframe = finalDataframe.append(pd.DataFrame(dictionary))

# Create a cross tab where I get a list of each word and 
# the fiels that contain it.
test3 = pd.crosstab(finalDataframe['values'], finalDataframe['filename'])
# To post process it, let's remove the last crosstab's column
#test3 = test3.drop(columns=['All'])
# Replace the [1,0] values in the existence columns
# and replace it with the file name
for file in list(test3.columns.values):
    test3[file].replace([0,1],['',file],inplace=True)
# Convert the values of each row from series to list
chale1=test3.apply(lambda x: x.tolist(), axis=1)

a = chale1.to_dict()
