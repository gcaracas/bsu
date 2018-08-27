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

final = []
for list in sections:
    # List = per block
    ai = list.split('\n')
    z = dict()
    # ai = line per bloxk "a:b"
    for list2 in ai:
        ab = list2.split(":")
        print(ab(1))
        #z[ab[0]] = ab[1]
        