#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:39:27 2019

@author: ncp532
"""

# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
from windrose import WindroseAxes

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import signal, stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# SIPEXII 2012
SIPEXII_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_VMR.csv', index_col=0)     # BrO data for SIPEXII (2012)
SIPEXII_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/BrO_error/SIPEXII_BrO_error.csv', index_col=0) # BrO error data for SIPEXII (2012)
SIPEXII_Met   = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_underway_60.csv') 

#------------------------------------------------------------------------------
# Calculate the Relative Error (>=0.6)

# Define the filter
Filter_SIPEXII = SIPEXII_Error / SIPEXII_VMR

# Apply the filter
SIPEXIIF    = Filter_SIPEXII < 0.6
SIPEXII_VMR = SIPEXII_VMR[SIPEXIIF]

#------------------------------------------------------------------------------
# Set the date

# SIPEXII 2012
SIPEXII_VMR.columns     = (pd.to_datetime(SIPEXII_VMR.columns,    dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8
SIPEXII_Met['DateTime'] = pd.to_datetime(SIPEXII_Met['DateTime'], dayfirst=True)

#------------------------------------------------------------------------------
# Transpose the VMR dataframes

SIPEXIITT = SIPEXII_VMR.T

#------------------------------------------------------------------------------
# Add columns for DateTime, Date and Time

# DateTime
SIPEXIITT['DateTime'] = SIPEXIITT.index

# Date
SIPEXIITT['Date'] = SIPEXIITT['DateTime'].dt.date

# Time
SIPEXIITT['Time'] = SIPEXIITT['DateTime'].dt.time

#------------------------------------------------------------------------------
# set datetime as the index

SIPEXII_Met = SIPEXII_Met.set_index('DateTime')

#------------------------------------------------------------------------------
# Resample all data to 20 min averages

SIPEXII_Met = SIPEXII_Met.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

SIPEXII_Met.index = SIPEXII_Met.index - pd.Timedelta(minutes=10)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

#-----------------------
# SIPEXII (07:00 to 18:00)
#-----------------------
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (SIPEXIITT['Time'] >= start_time) & (SIPEXIITT['Time'] < end_time)
SIPEXIIM   = SIPEXIITT[Midday_VMR]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# SIPEXII (23 Sep to 11 Nov 2012)
start_date   = '2012-09-23'
end_date     = '2012-11-11'
SIPEX_VMR    = (SIPEXIIM.index >= start_date) & (SIPEXIIM.index < end_date)
SIPEXIIM     = SIPEXIIM[SIPEX_VMR]

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

# SIPEXII (2012)
D1_SIPEXII = pd.merge(left=SIPEXIIM, right=SIPEXII_Met, how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Calculate the Wind Speed average

WS_s_SIPEXII         = np.array(D1_SIPEXII['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXII         = np.array(D1_SIPEXII['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D1_SIPEXII['WS_Avg'] = (WS_s_SIPEXII + WS_p_SIPEXII)/2                               # Average the wind speed for port and starboard

#------------------------------------------------------------------------------
# Seperate the data into low (<=7 m/s) and high (>7 m/s) wind speeds

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

SIPEXII_LWS = (D1_SIPEXII['WS_Avg'] <= 7)
D1_SIPEXIIL = D1_SIPEXII[SIPEXII_LWS]

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

SIPEXII_HWS = (D1_SIPEXII['WS_Avg'] > 7)
D1_SIPEXIIH = D1_SIPEXII[SIPEXII_HWS]

#------------------------------------------------------------------------------
# Define the variables

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# Surface Layer
BrO_SIPEXIILS = np.array(D1_SIPEXIIL[0.1]) * 1e6 # convert from ppmv to ppbv

# Boundary Layer
BrO_SIPEXIILB = np.array(D1_SIPEXIIL[0.3]) * 1e6 # convert from ppmv to ppbv

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# Surface Layer
BrO_SIPEXIIHS = np.array(D1_SIPEXIIH[0.1]) * 1e6 # convert from ppmv to ppbv

# Boundary Layer
BrO_SIPEXIIHB = np.array(D1_SIPEXIIH[0.3]) * 1e6 # convert from ppmv to ppbv

#------------------------------------------------------------------------------
# Concate the variables from each voyage

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOLS    = BrO_SIPEXIILS

# BrO boundary volume mixing ratio (VMR)
BrOLB    = BrO_SIPEXIILB

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOHS    = BrO_SIPEXIIHS

# BrO boundary volume mixing ratio (VMR)
BrOHB    = BrO_SIPEXIIHB

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# Low Wind Speed (<=7 m/s)
#------------------------------------
#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (BrO Surface) 
SIPEXII_Y1maskLS = np.isfinite(BrO_SIPEXIILS) # Scan for NaN values
BrO_SIPEXIILS    = BrO_SIPEXIILS[SIPEXII_Y1maskLS] # BrO HWS Surface
BrO_SIPEXIILB    = BrO_SIPEXIILB[SIPEXII_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
SIPEXII_Y1maskLB = np.isfinite(BrO_SIPEXIILB) # Scan for NaN values
BrO_SIPEXIILS    = BrO_SIPEXIILS[SIPEXII_Y1maskLB] # BrO HWS Surface
BrO_SIPEXIILB    = BrO_SIPEXIILB[SIPEXII_Y1maskLB] # BrO HWS Boundary

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO Surface) 
ALL_Y1maskLS   = np.isfinite(BrOLS) # Scan for NaN values
BrOLS          = BrOLS[ALL_Y1maskLS] # BrO HWS Surface
BrOLB          = BrOLB[ALL_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
ALL_Y1maskLB   = np.isfinite(BrOLB) # Scan for NaN values
BrOLS          = BrOLS[ALL_Y1maskLB] # BrO HWS Surface
BrOLB          = BrOLB[ALL_Y1maskLB] # BrO HWS Boundary

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# High Wind Speed (>7 m/s)
#------------------------------------
#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (BrO Surface) 
SIPEXII_Y1maskHS = np.isfinite(BrO_SIPEXIIHS) # Scan for NaN values
BrO_SIPEXIIHS    = BrO_SIPEXIIHS[SIPEXII_Y1maskHS] # BrO HWS Surface
BrO_SIPEXIIHB    = BrO_SIPEXIIHB[SIPEXII_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
SIPEXII_Y1maskHB = np.isfinite(BrO_SIPEXIIHB) # Scan for NaN values
BrO_SIPEXIIHS    = BrO_SIPEXIIHS[SIPEXII_Y1maskHB] # BrO HWS Surface
BrO_SIPEXIIHB    = BrO_SIPEXIIHB[SIPEXII_Y1maskHB] # BrO HWS Boundary

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO Surface) 
ALL_Y1maskHS   = np.isfinite(BrOHS) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHS] # BrO HWS Surface
BrOHB          = BrOHB[ALL_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
ALL_Y1maskHB   = np.isfinite(BrOHB) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHB] # BrO HWS Surface
BrOHB          = BrOHB[ALL_Y1maskHB] # BrO HWS Boundary

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)
#-----------------------------------
# Between BrO Surface (0-100m) and BrO Boundary (100-300m)
#-----------------------------------

#-----------------------------------
# Low Wind Speed (<=7 m/s) 
#-----------------------------------
#--------------------------------
# COMBINED
#--------------------------------
r_rowDL, p_valueDL = stats.pearsonr(BrOLS,BrOLB)
slopeDL, interceptDL, rDL, pDL, std_errDL = stats.linregress(BrOLS,BrOLB)

#------------------------------------------------------------------------------
#-----------------------------------
# High Wind Speed (>7 m/s) 
#-----------------------------------
#--------------------------------
# COMBINED
#--------------------------------
r_rowDH, p_valueDH = stats.pearsonr(BrOHS,BrOHB)
slopeDH, interceptDH, rDH, pDH, std_errDH = stats.linregress(BrOHS,BrOHB)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs O3)

fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) 
#-----------------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO Surface (0-100m) vs BrO Boundary (100-300m)
ax.scatter(BrO_SIPEXIILS,   BrO_SIPEXIILB,   edgecolors='none', marker='x', c='cyan',  label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(BrOLS, interceptDL + slopeDL * BrOLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 25.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0, 25.0)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)\n[100-300m ASL]', fontsize=20)
ax.set_xlabel('BrO (pptv)\n[0-100m ASL]', fontsize=20)

# Plot the title
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(0.865, 0.95), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("BrO (0-100m) and BrO (100-300m):\n (slope: "+str("%7.4f"%(slopeDL))+" $\pm$"+str("%7.4f"%(std_errDL))+" pptv, r: "+str("%7.4f"%(rDL))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s)
#-----------------------------------
# Graph 1
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO Surface (0-100m) vs BrO Boundary (100-300m)
ax.scatter(BrO_SIPEXIIHS,   BrO_SIPEXIIHB,   edgecolors='none', marker='x', c='cyan',  label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(BrOHS, interceptDH + slopeDH * BrOHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 25.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0, 25.0)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)\n[100-300m ASL]', fontsize=20)
ax.set_xlabel('BrO (pptv)\n[0-100m ASL ]', fontsize=20)

# Plot the title
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("BrO (0-100m) and BrO (100-300m):\n (slope: "+str("%7.4f"%(slopeDH))+" $\pm$"+str("%7.4f"%(std_errDH))+" pptv, r: "+str("%7.4f"%(rDH))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)
