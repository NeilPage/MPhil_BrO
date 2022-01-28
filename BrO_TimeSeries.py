#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:26:31 2019

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
from scipy import stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.lines import Line2D

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# BrO (Retrieval)
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv', index_col=0)       # BrO V1 (2017/18)
BrO_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv', index_col=0)       # BrO V2 (2017/18)
BrO_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv', index_col=0)       # BrO V3 (2017/18)

BrO_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv', index_col=0)       # BrO V1 (2018/19)
BrO_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv', index_col=0)       # BrO V2 (2018/19)
BrO_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv', index_col=0)       # BrO V3 (2018/19)

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv', index_col=0) # BrO SIPEXII (2012)

# Met
Met_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V1_17_underway_60.csv', index_col=0)
Met_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V2_17_underway_60.csv', index_col=0)
Met_V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V3_17_underway_60.csv', index_col=0)

Met_V1_18  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V1_18_underway_60.csv', index_col=0) 
Met_V2_18  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V2_18_underway_60.csv', index_col=0)
Met_V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V3_18_underway_60.csv',  index_col=0) 

Met_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/ShipTrack/SIPEXII_underway_60.csv', index_col=0) 

# O3
O3_V1_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv', index_col=0)
O3_V2_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv', index_col=0)
O3_V3_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv', index_col=0)

O3_V1_18  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V1_O3_1min.csv', index_col=0)
O3_V1_18.rename(columns={'O3':'O3_(ppb)'},inplace=True) # rename the column from 'O3' to 'O3_(ppb)'
O3_V2_18  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V2_O3_1min.csv', index_col=0)
O3_V2_18.rename(columns={'O3':'O3_(ppb)'},inplace=True) # rename the column from 'O3' to 'O3_(ppb)'
O3_V2_18  = O3_V2_18.loc[~O3_V2_18.index.duplicated(keep='first')] # remove duplicate values from the .csv file
O3_V3_18  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V3_O3_1min.csv', index_col=0)
O3_V3_18.rename(columns={'O3':'O3_(ppb)'},inplace=True) # rename the column from 'O3' to 'O3_(ppb)'
O3_V3_18  = O3_V3_18.loc[~O3_V3_18.index.duplicated(keep='first')] # remove duplicate values from the .csv file

O3_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv', index_col=0)
O3_SIPEXII = O3_SIPEXII.loc[~O3_SIPEXII.index.duplicated(keep='first')] # remove duplicate values from the .csv file

#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR RELATIVE ERROR 

# Calculate the Relative Error (>=0.6)
Filter1_BrO = BrO_V1_17['err_surf_vmr'] / BrO_V1_17['surf_vmr(ppmv)']
Filter2_BrO = BrO_V2_17['err_surf_vmr'] / BrO_V2_17['surf_vmr(ppmv)']
Filter3_BrO = BrO_V3_17['err_surf_vmr'] / BrO_V3_17['surf_vmr(ppmv)']

Filter4_BrO = BrO_V1_18['err_surf_vmr'] / BrO_V1_18['surf_vmr(ppmv)']
Filter5_BrO = BrO_V2_18['err_surf_vmr'] / BrO_V2_18['surf_vmr(ppmv)']
Filter6_BrO = BrO_V3_18['err_surf_vmr'] / BrO_V3_18['surf_vmr(ppmv)']

Filter7_BrO = BrO_SIPEXII['err_surf_vmr'] / BrO_SIPEXII['surf_vmr(ppmv)']

# Apply the filter
V1_17F       = Filter1_BrO < 0.6
BrO_V1_17T   = BrO_V1_17[V1_17F]

V2_17F       = Filter2_BrO < 0.6
BrO_V2_17T   = BrO_V2_17[V2_17F]

V3_17F       = Filter3_BrO < 0.6
BrO_V3_17T   = BrO_V3_17[V3_17F]

V1_18F       = Filter4_BrO < 0.6
BrO_V1_18T   = BrO_V1_18[V1_18F]

V2_18F       = Filter5_BrO < 0.6
BrO_V2_18T   = BrO_V2_18[V2_18F]

V3_18F       = Filter6_BrO < 0.6
BrO_V3_18T   = BrO_V3_18[V3_18F]

SIPEXIIF     = Filter7_BrO < 0.6
BrO_SIPEXIIT = BrO_SIPEXII[SIPEXIIF]

#------------------------------------------------------------------------------
# Set the date

# BrO (Retrieval)
BrO_V1_17T.index   = (pd.to_datetime(BrO_V1_17T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_17T.index   = (pd.to_datetime(BrO_V2_17T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_17T.index  = (pd.to_datetime(BrO_V3_17T.index,    dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

BrO_V1_18T.index   = (pd.to_datetime(BrO_V1_18T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_18T.index   = (pd.to_datetime(BrO_V2_18T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_18T.index  = (pd.to_datetime(BrO_V3_18T.index,    dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

BrO_SIPEXIIT.index = (pd.to_datetime(BrO_SIPEXIIT.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

# Met
Met_V1_17.index   = (pd.to_datetime(Met_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
Met_V2_17.index   = (pd.to_datetime(Met_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
Met_V3_17.index   = (pd.to_datetime(Met_V3_17.index,   dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

Met_V1_18.index   = (pd.to_datetime(Met_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
Met_V2_18.index   = (pd.to_datetime(Met_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
Met_V3_18.index   = (pd.to_datetime(Met_V3_18.index,   dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

Met_SIPEXII.index = (pd.to_datetime(Met_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

# O3
O3_V1_17.index   = (pd.to_datetime(O3_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
O3_V2_17.index   = (pd.to_datetime(O3_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
O3_V3_17.index   = (pd.to_datetime(O3_V3_17.index,   dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

O3_V1_18.index   = (pd.to_datetime(O3_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
O3_V2_18.index   = (pd.to_datetime(O3_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
O3_V3_18.index   = (pd.to_datetime(O3_V3_18.index,   dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

O3_SIPEXII.index = (pd.to_datetime(O3_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# CONVERT THE O3 DATASETS TO 20-MINUTE TIME RESOLUTION

O3_V1_17   = O3_V1_17.resample('20T', offset='10T').mean()
O3_V2_17   = O3_V2_17.resample('20T', offset='10T').mean()
O3_V3_17   = O3_V3_17.resample('20T', offset='10T').mean()

O3_V1_18   = O3_V1_18.resample('20T', offset='10T').mean()
O3_V2_18   = O3_V2_18.resample('20T', offset='10T').mean()
O3_V3_18   = O3_V3_18.resample('20T', offset='10T').mean()

O3_SIPEXII = O3_SIPEXII.resample('20T', offset='10T').mean()

#------------------------------------------------------------------------------
# REPLACE ERRONEOUS VALUES WITH NAN

# BrO (Retrieval)
BrO_V1_17T   = BrO_V1_17T.replace(-9999.000000, np.nan)
BrO_V2_17T   = BrO_V2_17T.replace(-9999.000000, np.nan)
BrO_V3_17T   = BrO_V3_17T.replace(-9999.000000, np.nan)

BrO_V1_18T   = BrO_V1_18T.replace(-9999.000000, np.nan)
BrO_V2_18T   = BrO_V2_18T.replace(-9999.000000, np.nan)
BrO_V3_18T   = BrO_V3_18T.replace(-9999.000000, np.nan)

BrO_SIPEXIIT = BrO_SIPEXIIT.replace(9.67e-05,np.nan)
BrO_SIPEXIIT = BrO_SIPEXIIT.replace(7.67e-06,np.nan)
BrO_SIPEXIIT = BrO_SIPEXIIT.replace(7.67e-07,np.nan)
BrO_SIPEXIIT.loc[BrO_SIPEXIIT.isnull().any(axis=1), :] = np.nan # if any element in the row is nan, set the whole row to nan
BrO_SIPEXIIT = BrO_SIPEXIIT.replace(-9999.000000, np.nan)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

#-----------------------------
# MIDDAY HOURS
#-----------------------------

# #-----------------------------
# # CAMMPCAN 2017-18
# #-----------------------------
# # V1_17 Davis (07:00 to 18:00)
# start_time   = '07:00:00'
# end_time     = '18:00:00'
# Midday       = (BrO_V1_17T['Time'] >= start_time) & (BrO_V1_17T['Time'] < end_time)
# BrO_V1_17_MM = BrO_V1_17T[Midday]

# # V2_17 Casey (08:00 to 16:00)
# start_time   = '08:00:00'
# end_time     = '16:00:00'
# Midday       = (BrO_V2_17T['Time'] >= start_time) & (BrO_V2_17T['Time'] < end_time)
# BrO_V2_17_MM = BrO_V2_17T[Midday]

# # V3_17 Mawson (08:00 to 18:00)
# start_time   = '08:00:00'
# end_time     = '18:00:00'
# Midday       = (BrO_V3_17T['Time'] >= start_time) & (BrO_V3_17['Time'] < end_time)
# BrO_V3_17_MM = BrO_V3_17T[Midday]

# #-----------------------------
# # CAMMPCAN 2018-19
# #-----------------------------
# # V1_18 Davis (07:00 to 18:00)
# start_time   = '07:00:00'
# end_time     = '18:00:00'
# Midday       = (BrO_V1_18T['Time'] >= start_time) & (BrO_V1_18T['Time'] < end_time)
# BrO_V1_18_MM = BrO_V1_18T[Midday]

# # V2_18 Casey (08:00 to 16:00)
# start_time   = '08:00:00'
# end_time     = '16:00:00'
# Midday       = (BrO_V2_18T['Time'] >= start_time) & (BrO_V2_18T['Time'] < end_time)
# BrO_V2_18_MM = BrO_V2_18T[Midday]

# # V3_18 Mawson (08:00 to 18:00)
# start_time   = '08:00:00'
# end_time     = '18:00:00'
# Midday       = (BrO_V3_18T['Time'] >= start_time) & (BrO_V3_18T['Time'] < end_time)
# BrO_V3_18_MM = BrO_V3_18T[Midday]

# #-----------------------------
# # SIPEXII 2012
# #-----------------------------
# # SIPEXII (07:00 to 18:00)
# start_time     = '07:00:00'
# end_time       = '18:00:00'
# Midday         = (BrO_SIPEXIIT['Time'] >= start_time) & (BrO_SIPEXIIT['Time'] < end_time)
# BrO_SIPEXII_MM = BrO_SIPEXIIT[Midday]

#-----------------------------
# ALL HOURS
#-----------------------------
BrO_V1_17_MM = BrO_V1_17T
BrO_V2_17_MM = BrO_V2_17T
BrO_V3_17_MM = BrO_V3_17T

BrO_V1_18_MM = BrO_V1_18T
BrO_V2_18_MM = BrO_V2_18T
BrO_V3_18_MM = BrO_V3_18T

BrO_SIPEXII_MM = BrO_SIPEXIIT

#------------------------------------------------------------------------------
# Define the variables

# CAMMPCAN (2017-18)
BrO_V1_17    = BrO_V1_17_MM['surf_vmr(ppmv)'] * 1e6 # convert from ppmv to pptv
Lat_V1_17    = Met_V1_17['latitude']
O3_V1_17     = O3_V1_17['O3_(ppb)']

BrO_V2_17    = BrO_V2_17_MM['surf_vmr(ppmv)'] * 1e6 # convert from ppmv to pptv
Lat_V2_17    = Met_V2_17['latitude']
O3_V2_17     = O3_V2_17['O3_(ppb)']

BrO_V3_17    = BrO_V3_17_MM['surf_vmr(ppmv)'] * 1e6 # convert from ppmv to pptv
Lat_V3_17    = Met_V3_17['latitude']
O3_V3_17     = O3_V3_17['O3_(ppb)']

# CAMMPCAN (2018-19)
BrO_V1_18    = BrO_V1_18_MM['surf_vmr(ppmv)'] * 1e6 # convert from ppmv to pptv
Lat_V1_18    = Met_V1_18['latitude']
O3_V1_18     = O3_V1_18['O3_(ppb)']

BrO_V2_18    = BrO_V2_18_MM['surf_vmr(ppmv)'] * 1e6 # convert from ppmv to pptv
Lat_V2_18    = Met_V2_18['latitude']
O3_V2_18     = O3_V2_18['O3_(ppb)']

BrO_V3_18    = BrO_V3_18_MM['surf_vmr(ppmv)'] * 1e6 # convert from ppmv to pptv
Lat_V3_18    = Met_V3_18['latitude']
O3_V3_18     = O3_V3_18['O3_(ppb)']

# SIPEXII (2012)
BrO_SIPEXII  = BrO_SIPEXII_MM['surf_vmr(ppmv)'] * 1e6 # convert from ppmv to pptv
Lat_SIPEXII  = Met_SIPEXII['latitude']
O3_SIPEXII   = O3_SIPEXII['O3_(ppb)']

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))
#ax3.spines["left"].set_color('blue')

# Plot the variables
#ax3.scatter(O3_V1_17.index, O3_V1_17,  marker='o', c='orange', s=3, label ='O3')
ax.scatter(BrO_V1_17.index, BrO_V1_17, marker='o', c='blue',  s=3,  label ='V1 (2017-18)')
ax2.plot(Lat_V1_17.index,   Lat_V1_17, ls='--',    c='black', label ='Latitude')


#UL1 = BrO_V1_17_DM + BrO_V1_17_STD # find the upper limit
#LL1 = BrO_V1_17_DM - BrO_V1_17_STD # find the lower limit
#ax.plot(date1_DM, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date1_DM, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date1_DM, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2017,11,12),datetime(2017,12,4)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,25)
#ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# # Format y-axis 3
# ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
# ax3.yaxis.label.set_color('orange')
# ax3.tick_params(axis='y', which='both', colors='orange')
# ax3.set_ylim(0,35)
# ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))

# Plot the variables
#ax3.scatter(O3_V2_17.index, O3_V2_17,  marker='o', c='orange', s=3, label ='O3')
ax.scatter(BrO_V2_17.index, BrO_V2_17, marker='o', c='blue',  s=3,label ='V2 (2017-18)')
ax2.plot(Lat_V2_17.index,   Lat_V2_17, ls='--',    c='black', label ='Latitude')


#UL2 = BrO_V2_17_DM + BrO_V2_17_STD # find the upper limit
#LL2 = BrO_V2_17_DM - BrO_V2_17_STD # find the lower limit
#ax.plot(date2_DM, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date2_DM, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date2_DM, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2017,12,16),datetime(2018,1,12)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,25)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# # Format y-axis 3
# ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax3.yaxis.label.set_color('orange')
# ax3.tick_params(axis='y', which='both', colors='orange')
# ax3.set_ylim(0,35)
# ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('Daily BrO concentrations for CAMMPCAN 2017-19 and SIPEXII 2012 Voyages', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))
#ax3.spines["right"].set_color('orange')

# Plot the variables
#ax3.scatter(O3_V3_17.index, O3_V3_17,  marker='o', c='orange', s=3, label ='O3')
ax.scatter(BrO_V3_17.index, BrO_V3_17, marker='o', c='blue',   s=3,label ='V3 (2017-18)')
ax2.plot(Lat_V3_17.index,   Lat_V3_17, ls='--',    c='black',  label ='Latitude')


#UL3 = BrO_V3_17_DM + BrO_V3_17_STD # find the upper limit
#LL3 = BrO_V3_17_DM - BrO_V3_17_STD # find the lower limit
#ax.plot(date3_DM, UL3, c='blue', ls='--', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date3_DM, LL3, c='blue', ls='--', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date3_DM, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2018,1,16),datetime(2018,2,27)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,25)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
#ax2.axes.get_yaxis().set_visible(False)

# # Format y-axis 3
# ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax3.yaxis.label.set_color('orange')
# ax3.tick_params(axis='y', which='both', colors='orange')
# ax3.set_ylim(0,35)
# #ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))
#ax3.spines["left"].set_color('red')

# Plot the variables
#ax3.scatter(O3_V1_18.index, O3_V1_18,  marker='o', c='orange', s=3, label ='O3')
ax.scatter(BrO_V1_18.index, BrO_V1_18, marker='o', c='red',   s=3,label ='V1 (2018-19)')
ax2.plot(Lat_V1_18.index,   Lat_V1_18, ls='--',    c='black', label ='Latitude')


#UL4 = BrO_V1_18_DM + BrO_V1_18_STD # find the upper limit
#LL4 = BrO_V1_18_DM - BrO_V1_18_STD # find the lower limit
#ax.plot(date4_DM, UL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date4_DM, LL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date4_DM, UL4, LL4, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2018,10,27),datetime(2018,11,26)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,25)
#ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# # Format y-axis 3
# ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax3.yaxis.label.set_color('orange')
# ax3.tick_params(axis='y', which='both', colors='orange')
# ax3.set_ylim(0,35)
# ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))

# Plot the variables
#ax3.scatter(O3_V2_18.index, O3_V2_18,  marker='o', c='orange', s=3, label ='O3')
ax.scatter(BrO_V2_18.index, BrO_V2_18, marker='o', c='red',    s=3,label ='V2 (2018-19)')
ax2.plot(Lat_V2_18.index,   Lat_V2_18, ls='--',    c='black',  label ='Latitude')


#UL5 = BrO_V2_18_DM + BrO_V2_18_STD # find the upper limit
#LL5 = BrO_V2_18_DM - BrO_V2_18_STD # find the lower limit
#ax.plot(date5_DM, UL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date5_DM, LL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date5_DM, UL5, LL5, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2018,11,29),datetime(2019,1,8)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,25)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
#ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
#ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax3.yaxis.label.set_color('orange')
#ax3.tick_params(axis='y', which='both', colors='orange')
#ax3.set_ylim(0,35)
#ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#Plot the legend and title
#plt.title('BrO Daily Average (V2 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax3.spines["right"].set_position(("axes", 1.15))
# ax3.spines["right"].set_color('orange')

# Plot the variables
#ax3.scatter(O3_V3_18.index, O3_V3_18,  marker='o', c='orange', s=3, label ='O3')
ax.scatter(BrO_V3_18.index, BrO_V3_18, marker='o', c='red',    s=3,label ='V3 (2018-19)')
ax2.plot(Lat_V3_18.index,   Lat_V3_18, ls='--',    c='black',  label ='Latitude')


#UL6 = BrO_V3_18_DM + BrO_V3_18_STD # find the upper limit
#LL6 = BrO_V3_18_DM - BrO_V3_18_STD # find the lower limit
#ax.plot(date6_DM, UL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date6_DM, LL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date6_DM, UL6, LL6, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2019,1,18),datetime(2019,2,27)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,25)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
#ax2.axes.get_yaxis().set_visible(False)

# # Format y-axis 3
# ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax3.yaxis.label.set_color('orange')
# ax3.tick_params(axis='y', which='both', colors='orange')
# ax3.set_ylim(0,35)
# #ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 7
ax=plt.subplot(337) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
# ax3.spines["right"].set_position(("axes", 1.15))
# ax3.spines["right"].set_color('orange')
# ax3.spines["left"].set_color('green')       

# Plot the variables
#ax3.scatter(O3_SIPEXII.index, O3_SIPEXII,  marker='o', c='orange', s=3, label ='O3')
ax.scatter(BrO_SIPEXII.index, BrO_SIPEXII, marker='o', c='green',  s=3,label ='SIPEXII (2012)')
ax2.plot(Lat_SIPEXII.index,   Lat_SIPEXII, ls='--',    c='black',  label ='Latitude')


#UL7 = BrO_SIPEXII_DM + BrO_SIPEXII_STD # find the upper limit
#LL7 = BrO_SIPEXII_DM - BrO_SIPEXII_STD # find the lower limit
#ax.plot(date7_DM, UL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date7_DM, LL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date7_DM, UL7, LL7, facecolor='green', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2012,9,19),datetime(2012,11,14)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=10)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('green')
ax.tick_params(axis='y', which='both', colors='green')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)


# # Format y-axis 3
# ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax3.yaxis.label.set_color('orange')
# ax3.tick_params(axis='y', which='both', colors='orange')
# ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')
legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

# Custom Legend
custom_lines = [Line2D([0], [0], color='blue',   lw=4),
                Line2D([0], [0], color='red',  lw=4),
                Line2D([0], [0], color='green', lw=4),
                #Line2D([0], [0], color='orange',   lw=4),
                Line2D([0], [0], color='black',  lw=4),]
fig.legend(custom_lines, ['BrO (CAMMPCAN 2017-18)', 'BrO (CAMMPCAN 2018-19)', 'BrO (SIPEXII)', 'Latitude'], loc='upper left', bbox_to_anchor=(0.725, 0.25))
