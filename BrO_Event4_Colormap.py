#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:23:17 2018

@author: ncp532
"""

# File system packages
from netCDF4 import Dataset				# function used to open single netcdf file
from netCDF4 import MFDataset				# function used to open multiple netcdf files

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator, AutoMinorLocator

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import signal, stats

# Date and Time handling package
import datetime as dt
from datetime import datetime,time, timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# OBSERVATIONS
# Retrieve the observational data

#---------------------------------
# V1_18 Davis (7-15 Nov 2018)
#---------------------------------

#---------
# BrO
#---------

# BrO VMR
V1_2018 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)

# BrO Error
V1_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/BrO_error/V1_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2018/19)

# Calculate the Relative Error (>=0.6)
Filter = V1_Error / V1_2018

# Apply the filter
V1_18F = Filter < 0.6
V1_18T = V1_2018[V1_18F]

#---------
# NO2
#---------

# NO2 VMR
NO2 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_NO2/V1_18_NO2_VMR.csv',index_col=0) # NO2 data for CAMPCANN V1 (2018/19)

# NO2 Error
NO2_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/NO2_error/V1_18_NO2_error.csv', index_col=0) # NO2 error data for CAMPCANN V1 (2018/19)

# Calculate the Relative Error (>=0.6)
Filter2 = NO2_Error / NO2

# Apply the filter
NO2F = Filter2 < 0.6
NO2T = NO2[NO2F]

#---------
# AOD
#---------

# BrO AOD
BrO_AOD = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_AOD/V1_18_AOD_338.csv',index_col=0) # AOD data for CAMMPCAN V1 (2018/19)

# NO2_AOD
NO2_AOD = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_AOD/V1_18_AOD_375.csv',index_col=0) # AOD data for CAMMPCAN V1 (2018/19)

#---------
# SZA
#---------

DF4_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_SZA/V1_18_SZA.csv',index_col=0) # SZA data for CAMPCANN V1 (2018/19)

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

#---------
# BrO
#---------

Date1 = V1_2018.columns.values

##CONVERT TO DATETIME FROM STRING
date=[]
for i in range(len(Date1)):
    date.append(datetime.strptime(Date1[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

#---------
# NO2
#---------

Date2 = NO2.columns.values

##CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(Date2)):
    date2.append(datetime.strptime(Date2[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

#---------
# AOD
#---------

# BrO AOD
dat3 = np.array(BrO_AOD['Date'])
tim3 = np.array(BrO_AOD['Time'])
Date3 = dat3+' '+tim3

##CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(Date3)):
    date3.append(datetime.strptime(Date3[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

# NO2_AOD
dat5 = np.array(NO2_AOD['Date'])
tim5 = np.array(NO2_AOD['Time'])
Date5 = dat5+' '+tim5

##CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(Date5)):
    date5.append(datetime.strptime(Date5[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

#---------
# SZA
#---------

dat4 = np.array(DF4_SZA['Date'])
tim4 = np.array(DF4_SZA['Time'])
Date4 = dat4+' '+tim4

##CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(Date4)):
    date4.append(datetime.strptime(Date4[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))
    
#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

## V1_17 Davis (07:00 to 18:00)
#start_time = '07:00:00'
#end_time = '18:00:00'
#Midday = (V1_2017_T['Time'] > start_time) & (V1_2017_T['Time'] < end_time)
#V1_2017_T = V1_2017_T[Midday]
#V1_2017 = V1_2017_T.T

#------------------------------------------------------------------------------
# SET UP THE VALUES TO PLOT

#---------------------------------
# CAMMPCAN V1 2018-19
#---------------------------------

#---------
# BrO
#---------

# All
#y = V1_2018.index # set the values for the y-axis
#x = np.array(V1_2018.dtypes.index) # set the values for the x-axis
#z = V1_2018.copy() # identify the matrix containing the z-values (BrO in ppMv)

# Filtered
y = V1_18T.index # set the values for the y-axis
x = np.array(V1_18T.dtypes.index) # set the values for the x-axis
z = V1_18T.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z[z==-9999]=np.nan # set the erroneous values as NaN 
z = z.loc[:]*1e6 # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz=np.ma.masked_where(np.isnan(z),z) 

#---------
# NO2
#---------

# All
#y2 = NO2.index # set the values for the y-axis
#x2 = np.array(NO2.dtypes.index) # set the values for the x-axis
#z2 = NO2.copy() # identify the matrix containing the z-values (BrO in ppMv)

# Filtered
y2 = NO2T.index # set the values for the y-axis
x2 = np.array(NO2T.dtypes.index) # set the values for the x-axis
z2 = NO2T.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z2[z2==-9999]=np.nan # set the erroneous values as NaN 
z2 = z2.loc[:]*1e6 # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz2=np.ma.masked_where(np.isnan(z2),z2)

#---------
# AOD
#---------

AOD_338 = np.array(BrO_AOD['AOD'])
AOD_375 = np.array(NO2_AOD['AOD'])

#---------
# SZA
#---------

SZA = np.array(DF4_SZA['SZA'])

#------------------------------------------------------------------------------
# PLOT A COLORMAP OF BrO CONCENTRATIONS

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)
ax = plt.subplot(111)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
#ax.set_zorder(ax2.get_zorder()+1)
#ax.patch.set_visible(False)

cmap=plt.cm.jet
norm = BoundaryNorm(np.arange(0,16,1), cmap.N)

plt.pcolormesh(date, y, mz, vmin=0, vmax=15.5, norm=norm, cmap=cmap)
ax.pcolormesh(date, y, mz, vmin=0, vmax=15.5, norm=norm, cmap=cmap)

# Plot the AOD and SZA
#ax2.plot(date3, AOD_338, marker='x', c='black', markersize = 3.0, ls='-', label ='AOD (338 nm)')
ax2.scatter(date3, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
#ax3.plot(date4, SZA, marker='x', c='Brown', markersize = 3.0, ls='-', label ='SZA')
ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')

#plt.title('CAMMPCAN V1 2018-19 BrO VMR', fontsize=25)
plt.xlim(datetime(2018,11,7,0,0,0),datetime(2018,11,7,23,59,59))

ax.set_ylabel('Altitude (km)', fontsize=20)
ax2.set_ylabel('AOD  (338 nm)', fontsize=20)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=20)
ax.set_xlabel('Time', fontsize=20)
# set the limits of the plot to the limits of the data

# Format ColorBar
clb = plt.colorbar(extend='max',pad = 0.16)
clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=10)
clb.ax.tick_params(labelsize=15)
tick_locator = ticker.MaxNLocator(nbins=16)
clb.locator = tick_locator
clb.update_ticks()

#clb = plt.colorbar(extend='max')
#clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=20)
#clb.ax.tick_params(labelsize=15)
#tick_locator = ticker.MaxNLocator(nbins=11)
#clb.locator = tick_locator
#clb.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.IndexLocator(base=.2, offset=-.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0.1,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=15)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=15)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=15)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=20))

ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20
ax.tick_params(labelsize=15)

# Rotates the labels to fit
fig.autofmt_xdate()

plt.show()

#------------------------------------------------------------------------------
# PLOT A COLORMAP OF NO2 CONCENTRATIONS

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)
ax = plt.subplot(111)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
#ax.set_zorder(ax2.get_zorder()+1)
#ax.patch.set_visible(False)

cmap=plt.cm.jet
norm = BoundaryNorm(np.arange(0,400,20), cmap.N)

plt.pcolormesh(date2, y2, mz2, vmin=0, vmax=390, norm=norm, cmap=cmap)
ax.pcolormesh(date2, y2, mz2, vmin=0, vmax=390, norm=norm, cmap=cmap)

# Plot the AOD and SZA
#ax2.plot(date3, AOD_338, marker='x', c='black', markersize = 3.0, ls='-', label ='AOD (338 nm)')
ax2.scatter(date5, AOD_375, marker='x', color='black', label ='AOD (375 nm)')
#ax3.plot(date4, SZA, marker='x', c='Brown', markersize = 3.0, ls='-', label ='SZA')
ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')

#plt.title('CAMMPCAN V1 2018-19 NO$_2$ VMR', fontsize=25)
plt.xlim(datetime(2018,11,7,0,0,0),datetime(2018,11,7,23,59,59))

ax.set_ylabel('Altitude (km)', fontsize=20)
ax2.set_ylabel('AOD (375 nm)', fontsize=20)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=20)
ax.set_xlabel('Time', fontsize=20)
# set the limits of the plot to the limits of the data

# Format ColorBar
clb = plt.colorbar(extend='max',pad = 0.16)
clb.set_label(r"NO$_2$ (pptv)", fontsize =20, labelpad=10)
clb.ax.tick_params(labelsize=15)
tick_locator = ticker.MaxNLocator(nbins=20)
clb.locator = tick_locator
clb.update_ticks()

#clb = plt.colorbar(extend='max')
#clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=20)
#clb.ax.tick_params(labelsize=15)
#tick_locator = ticker.MaxNLocator(nbins=11)
#clb.locator = tick_locator
#clb.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.IndexLocator(base=.2, offset=-.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0.1,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=15)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=15)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=15)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=20))

ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20
ax.tick_params(labelsize=15)

# Rotates the labels to fit
fig.autofmt_xdate()

plt.show()