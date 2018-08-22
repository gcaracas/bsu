#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:01:42 2018

@author: gcu
"""

import numpy as np

a =  np.array([1, 2, 3])
b=np.array((3, 4, 5))

z=np.ones((3,4), dtype=np.int16)
np.full((3,4),5.4)

np.linspace(1, 6, 6)

a.shape
a.itemsize
z.dtype
z.itemsize
a
a[::2]
a[1:]


a = np.array([1,2,5,7,8])
a[1:3] = -1
type(a)

b = [1,2,5,7,8]
type(b)
b[1:3] = -1

a = np.array([1,2,5,7,8])
a_slice = a[1:5]
a_slice[1]=1000

b=[1,2,5,7,8]
c=b[1:5]
c[1]=1

aa=np.array([1,2,5,7,8])
aa_slice=aa[1:5].copy()
aa_slice[1]=1000

a=np.arange(12).reshape(3,4)

rown_on = np.array([True, False, True])
a[rown_on,:]

coefs=np.array([[2,6],[5,3]])
depvars = np.array([6,-9])

import numpy.linalg as linalg 
solution = linalg.solve(coefs, depvars)


import pandas as pd

people_dict = { "weight": pd.Series([68, 83, 112],index=["alice", "bob", "charles"]),   "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
"children": pd.Series([0, 3], index=["charles", "bob"]),
"hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),}

people=pd.DataFrame(people_dict)
people[people["birthyear"] < 1990]

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
plt.hist(x, num_bins, facecolor='blue')