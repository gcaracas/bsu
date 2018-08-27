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
    # First split into sections, each section is a vote.
    #sections = sections.append(re.split('\n',lines))
#sections = re.split('^\n',lines)
#sections = re.split('\n\W+:\W+\n\W+:\W+\n\W+:\W+\n', lines)
sections = re.split(".\S", lines, re.IGNORECASE)