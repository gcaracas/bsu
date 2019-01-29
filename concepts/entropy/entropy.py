#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:13:01 2019

@author: gcu
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats

# This is just how xlog(x) looks like.
fig, ax = plt.subplots()
x = np.arange(0.01, 2.0, 0.01)
ax.plot(x, x*np.log10(x))
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# Lets define a gaussian probl dist.
# Att. mean, std
x = np.arange(-4.0, 4.0, 0.01)
fig, ax = plt.subplots()
ft=scipy.stats.norm(0, 1)
ax.plot(x, ft.pdf(x))
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# Now that we have the normal prob. distribution
# Let's plot its entropy as 
# h(p) = -sum(pi*log(pi))

y_tbl = [ -1*y for y in ft.pdf(x)* np.log10(ft.pdf(x))]

fig, ax = plt.subplots()
x = np.arange(-4.0, 4.0, 0.01)
ax.plot(x,y_tbl, c='red')
ax.plot(x, ft.pdf(x), c='blue')
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')


y_tbl = [ y for y in np.log10(ft.pdf(x))]

fig, ax = plt.subplots()
x = np.arange(-4.0, 4.0, 0.01)
ax.plot(x,y_tbl, c='red')
ax.plot(x, ft.pdf(x), c='blue')
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
