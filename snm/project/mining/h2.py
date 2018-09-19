#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 08:41:14 2018

@author: gcu
"""

import networkx as nx
import  pickle
import pandas as pd
import numpy as np
import glob
import os
import re
from collections import Counter
#import pylab as plt
import matplotlib.pyplot as plt
data=pd.read_csv("./low_mem_data.csv")
# Remove rows with invalid dates
data.dropna(subset=['DAT'], inplace=True)

def getUsersTgT(Tbl=''):
    cntr = Counter(Tbl['TGT'])
    return cntr.most_common(n=None)
    
usr=getUsersTgT(Tbl=data)
# The first element is a space, which means there was no user, thus let's remove
# The first user.
del usr[0]

# We have list of users. Now let's get build a function that given 
# a user, we get a table with that data.

def getTableForUser(U='', T=''):
    tmp = T.set_index('TGT')
    return tmp.ix[U]

def validateHour(T=''):
    err=[]
    count=0
    for t in T.DAT:
        if int(t[:2]) > 23:
            print("Error",t)
            err.append(count)
        count=count+1
    if len(err) > 0:
        for i in err:
            print("Dropping",i)
            T.drop(T.index[i], inplace=True)
    return T

def acceptanceRatio(T=''):
    allElem=[]
    acc=[]
    neu=[]
    rej=[]
    accR=[]
    neuR=[]
    rejR=[]
    succR=[]
    cumSum=[]
    cumAcc=[]
    cumNeu=[]
    cumRej=[]
    
    fRes=0
    fResR=[]
    for i in T.index:
        elemV = T['VOT'][i]
        elemR = T['RES'][i]
        if int(elemV) == 1:
            acc.append(elemV)
        if int(elemV) == 0:
            print("Neutral")
            neu.append(elemV)
        if int(elemV) == -1:
            rej.append(elemV)
        #fRes=fRes+int(elemR)
        #fResR.append(fRes/len(allElem+1))
        allElem.append(elemV)
        accR.append(len(acc)/len(allElem))
        neuR.append(len(neu)/len(allElem))
        rejR.append(len(rej)/len(allElem))
        cumSum.append(len(allElem))
        cumAcc.append(len(acc))
        cumNeu.append(len(neu))
        cumRej.append(len(rej))
    T["accRatio"]=accR
    T["neuRatio"]=neuR
    T["rejRatio"]=rejR
    T["cumSumVot"]=cumSum
    T["cumAcc"]=cumAcc
    T["cumNeu"]=cumNeu
    T["cumRej"]=cumRej
    #T["resRatio"]=fResR
    return T
   
    
#usrTable=getTableForUser(U='Werdna',T=data)
usrTable=getTableForUser(U='Epbr123',T=data)    
usrTable.reset_index(inplace=True)
usrTable = validateHour(T=usrTable)
usrTable['date']=pd.to_datetime(usrTable.DAT)
usrTable.sort_index(inplace=True)
acceptanceRatio(T=usrTable)

usrTable.set_index('date',inplace=True)

r=usrTable[['accRatio','neuRatio','rejRatio']]
plt.figure();
r.plot();



