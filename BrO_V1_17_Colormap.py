#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:23:17 2018

@author: ncp532
"""

# File system packages
#from netCDF4 import Dataset				# function used to open single netcdf file
#from netCDF4 import MFDataset				# function used to open multiple netcdf files

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator, AutoMinorLocator
from matplotlib import gridspec

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
# V1_17 Davis (14-22 Nov 2017)
#---------------------------------

#---------
# BrO
#---------

# BrO VMR
V1_2017 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2017/18)

# BrO Error
V1_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/BrO_error/V1_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2017/18)

# Calculate the Relative Error (>=0.6)
Filter = V1_Error / V1_2017

# Apply the filter
V1_17F = Filter < 0.6
V1_17T = V1_2017[V1_17F]

#---------
# NO2
#---------

# NO2 VMR
NO2 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_NO2/V1_17_NO2_VMR.csv',index_col=0) # NO2 data for CAMPCANN V1 (2017/18)

# NO2 Error
NO2_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/NO2_error/V1_17_NO2_error.csv', index_col=0) # NO2 error data for CAMPCANN V1 (2017/18)

# Calculate the Relative Error (>=0.6)
Filter2 = NO2_Error / NO2

# Apply the filter
NO2F = Filter2 < 0.6
NO2T = NO2[NO2F]

#---------
# Aerosol
#---------

# Aerosol extinction at 338 nm (BrO)
AeroExt_338 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_Aerosol/V1_17_AeroExt_338.csv',index_col=0) # Aerosol extinction data at 338 nm for CAMPCANN V1 (2017/18)

# Aerosol extinction at 375 nm (NO2)
AeroExt_375 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_Aerosol/V1_17_AeroExt_375.csv',index_col=0) # Aerosol extinction data at 375 nm for CAMPCANN V1 (2017/18)

# Aerosol extinction wl at 360 nm
AeroExt_360 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_Aerosol/V1_17_AeroExt_wl_360.csv',index_col=0) # Aerosol extinction data at 360 nm for CAMPCANN V1 (2017/18)

#---------
# AOD
#---------

# BrO_AOD
BrO_AOD = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_AOD/V1_17_AOD_338.csv',index_col=0) # AOD data for CAMPCANN V1 (2017/18)

# NO2_AOD
NO2_AOD = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_AOD/V1_17_AOD_375.csv',index_col=0) # AOD data for CAMPCANN V1 (2017/18)

#---------
# SZA
#---------

DF4_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_SZA/V1_17_SZA.csv',index_col=0) # SZA data for CAMPCANN V1 (2017/18)

#------------------------------------------------------------------------------
# Filter the SZA for outliers

# def hampel_filter_pandas(input_series, window_size, n_sigmas=3):

#     k = 1.4826 # scale factor for Gaussian distribution
#     new_series = input_series.copy()

#     # helper lambda function 
#     MAD = lambda x: np.median(np.abs(x - np.median(x)))
    
#     rolling_median = input_series.rolling(window=2*window_size, center=True).median()
#     rolling_mad = k * input_series.rolling(window=2*window_size, center=True).apply(MAD)
#     diff = np.abs(input_series - rolling_median)

#     indices = list(np.argwhere(diff > (n_sigmas * rolling_mad)).flatten())
#     new_series[indices] = rolling_median[indices]
    
#     return new_series, indices

# res, detected_outliers = hampel_filter_pandas(DF4_SZA['SZA'],10)

# def evaluate_detection(series, true_indices, detected_indices):
    
#     # calculate metrics
#     tp = list(set(detected_outliers).intersection(set(true_indices)))
#     fp = list(set(detected_outliers).difference(set(true_indices)))
#     fn = list(set(true_indices).difference(set(detected_outliers)))
#     perc_detected = 100 * len(tp) / len(true_indices)
    
#     # create the plot
#     fix, ax = plt.subplots(2, 1)
    
#     ax[0].plot(np.arange(len(series)), series);
#     ax[0].scatter(true_indices, series[true_indices], c='g', label='true outlier')
#     ax[0].set_title('Original series')
#     ax[0].legend()
    
#     ax[1].plot(np.arange(len(series)), series);
#     ax[1].scatter(tp, series[tp], c='g', label='true positive')
#     ax[1].scatter(fp, series[fp], c='r', label='false positive')
#     ax[1].scatter(fn, series[fn], c='k', label='false negative')
#     ax[1].set_title('Algorithm results')
#     ax[1].legend()
    
#     # print out summary
#     print('-' * 25 + ' Summary ' + '-' * 25)
#     print(f'Outliers in the series: {len(true_indices)}')
#     print(f'Identified outliers: {len(detected_indices)}')
#     print(f'Correctly detected outliers: {len(tp)} ({perc_detected:.2f}% of all outliers).')
#     print('-' * 59)
    
#     return tp, fp, fn

# tp, fp, fn = evaluate_detection(DF4_SZA['SZA'], detected_outliers, detected_outliers)

# DF4_SZA = DF4_SZA.drop(DF4_SZA.index[[detected_outliers]]) 


def hampel(vals_orig, k=15, t0=3):
    '''
    vals: pandas series of values from which to remove outliers
    k: size of window (including the sample; 7 is equal to 3 on either side of value)
    '''
    #Make copy so original not edited
    vals=vals_orig.copy()    
    #Hampel Filter
    L= 1.4826
    rolling_median=vals.rolling(k).median()
    difference=np.abs(rolling_median-vals)
    median_abs_deviation=difference.rolling(k).median()
    threshold= t0 *L * median_abs_deviation
    outlier_idx=difference>threshold
    vals[outlier_idx]=np.nan
    return(vals)

DF4_SZA['SZA'] = hampel(DF4_SZA['SZA'])

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

#---------
# BrO
#---------

Date1 = V1_2017.columns.values

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

# BrO_AOD
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

#---------
# Aerosol
#---------

# Aerosol extinction at 338 nm (BrO)
Date6 =AeroExt_338.columns.values

##CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(Date6)):
    date6.append(datetime.strptime(Date6[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

# Aerosol extinction at 375 nm (NO2)
Date7 =AeroExt_375.columns.values

##CONVERT TO DATETIME FROM STRING
date7=[]
for i in range(len(Date7)):
    date7.append(datetime.strptime(Date7[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

# Aerosol extinction wl at 360 nm
Date8 =AeroExt_360.columns.values

##CONVERT TO DATETIME FROM STRING
date8=[]
for i in range(len(Date8)):
    date8.append(datetime.strptime(Date8[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))
    
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
# CAMMPCAN V1 2017-18
#---------------------------------

#---------
# BrO
#---------

# All
#y = V1_2017.index # set the values for the y-axis
#x = np.array(V1_2017.dtypes.index) # set the values for the x-axis
#z = V1_2017.copy() # identify the matrix containing the z-values (BrO in ppMv)

# Filtered
y = V1_17T.index # set the values for the y-axis
x = np.array(V1_17T.dtypes.index) # set the values for the x-axis
z = V1_17T.copy() # identify the matrix containing the z-values (BrO in ppMv)

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

#---------
# Aerosol
#---------

# Aerosol extinction at 338 nm (BrO)

# All
y3 = AeroExt_338.index # set the values for the y-axis
x3 = np.array(AeroExt_338.dtypes.index) # set the values for the x-axis
z3 = AeroExt_338.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z3[z3==-9999]=np.nan # set the erroneous values as NaN 
z3 = z3.loc[:] # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz3=np.ma.masked_where(np.isnan(z3),z3) 

# Aerosol extinction at 375 nm (NO2)

# All
y4 = AeroExt_375.index # set the values for the y-axis
x4 = np.array(AeroExt_375.dtypes.index) # set the values for the x-axis
z4 = AeroExt_375.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z4[z4==-9999]=np.nan # set the erroneous values as NaN 
z4 = z4.loc[:] # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz4=np.ma.masked_where(np.isnan(z4),z4) 

# Aerosol extinction wl at 360 nm

# All
y5 = AeroExt_360.index # set the values for the y-axis
x5 = np.array(AeroExt_360.dtypes.index) # set the values for the x-axis
z5 = AeroExt_360.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z5[z5==-9999]=np.nan # set the erroneous values as NaN 
z5 = z5.loc[:] # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz5=np.ma.masked_where(np.isnan(z5),z5) 

#------------------------------------------------------------------------------
# PLOT A COLORMAP OF BrO and NO2 CONCENTRATIONS

fig = plt.figure(figsize=(10,6))
plt.subplots_adjust(top=0.96,bottom=0.15,left=0.08,right=1.0,hspace=0.15)
gs = gridspec.GridSpec(ncols=1, nrows=2, width_ratios=[1])

#------------------------------
# Graph 1 (BrO)
ax  = fig.add_subplot(111) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
#ax.set_zorder(ax2.get_zorder()+1)
#ax.patch.set_visible(False)

cmap=plt.cm.jet
norm = BoundaryNorm(np.arange(0,11,1), cmap.N)

#plt.pcolormesh(date, y, mz, vmin=0, vmax=10, norm=norm, cmap=cmap)
col1 = ax.pcolormesh(date, y, mz, vmin=0, vmax=10, norm=norm, cmap=cmap)

# Plot the AOD and SZA
#ax2.plot(date3, AOD_338, marker='x', c='black', markersize = 3.0, ls='-', label ='AOD (338 nm)')
ax2.scatter(date3, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(date4, SZA, marker='x', c='magenta', markersize = 1.0, ls='None', label ='SZA')
#ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')

#plt.title('CAMMPCAN V1 2017-18 BrO VMR', fontsize=25)
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,23,0,0,5))

ax.set_ylabel('Altitude (km)', fontsize=20)
ax2.set_ylabel('AOD (338 nm)', fontsize=20)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=20)
ax.set_xlabel('Date', fontsize=20)
# set the limits of the plot to the limits of the data

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max',pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =20, labelpad=10)
clb1.ax.tick_params(labelsize=15)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

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
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))

ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20
ax.tick_params(labelsize=15)

# Rotates the labels to fit
fig.autofmt_xdate()

plt.show()

# #------------------------------
# # Graph 2 (NO2)
# #ax = plt.subplot(gs[0]) # options graph 2 (vertical no, horizontal no, graph no)
# ax  = fig.add_subplot(212) # options graph 2 (vertical no, horizontal no, graph no)
# ax2 = ax.twinx()
# ax3 = ax.twinx()
# ax3.set_zorder(ax.get_zorder()+1)
# ax3.patch.set_visible(False)
# ax2.set_zorder(ax3.get_zorder()+1)
# ax2.patch.set_visible(False)
# #ax.set_zorder(ax2.get_zorder()+1)
# #ax.patch.set_visible(False)

# cmap=plt.cm.jet
# norm = BoundaryNorm(np.arange(0,400,20), cmap.N)

# #plt.pcolormesh(date2, y2, mz2, vmin=0, vmax=390, norm=norm, cmap=cmap)
# col1 = ax.pcolormesh(date2, y2, mz2, vmin=0, vmax=390, norm=norm, cmap=cmap)

# # Plot the AOD and SZA
# #ax2.plot(date5, AOD_375, marker='x', c='black', markersize = 3.0, ls='-', label ='AOD (375 nm)')
# ax2.scatter(date5, AOD_375, marker='x', color='black', label ='AOD (375 nm)')
# #ax3.plot(date4, SZA, marker='x', c='Brown', markersize = 3.0, ls='-', label ='SZA')
# ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')

# #plt.title('CAMMPCAN V1 2017-18 NO$_2$ VMR', fontsize=25)
# plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,23,0,0,5))

# ax.set_ylabel('Altitude (km)', fontsize=20)
# ax2.set_ylabel('AOD (375 nm)', fontsize=20)
# ax3.set_ylabel('SZA ($^\circ$)', fontsize=20)
# ax.set_xlabel('Date', fontsize=20)
# # set the limits of the plot to the limits of the data

# # Format ColorBar
# clb1 = fig.colorbar(col1, extend='max',pad = 0.16)
# clb1.set_label(r"NO$_2$ (pptv)", fontsize =20, labelpad=10)
# clb1.ax.tick_params(labelsize=15)
# tick_locator = ticker.MaxNLocator(nbins=12)
# clb1.locator = tick_locator
# clb1.update_ticks()

# # Format y-axis (NO2)
# ax.yaxis.set_major_locator(ticker.IndexLocator(base=.2, offset=-.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax.set_ylim(0.1,3.0) # On Station
# ax.tick_params(axis='y', which='both', colors='Black', labelsize=15)

# # Format y-axis 2 (AOD)
# ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
# ax2.set_ylim(0,0.5) # On Station
# ax2.yaxis.label.set_color('Black')
# ax2.tick_params(axis='y', which='both', colors='Black', labelsize=15)

# # Format y-axis 3 (SZA)
# ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
# ax3.set_ylim(0,100) # On Station
# ax3.yaxis.label.set_color('magenta')
# ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=15)
# ax3.spines["right"].set_position(("axes", 1.12))
# ax3.spines["right"].set_color('magenta')

# # Format x-axis
# xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))

# ax.xaxis.labelpad = 20
# ax.yaxis.labelpad = 20
# ax.tick_params(labelsize=15)

# # Rotates the labels to fit
# fig.autofmt_xdate()

# plt.show()

# #------------------------------------------------------------------------------
# # PLOT A COLORMAP OF Aerosol Extinction at 338 nm (BrO)

# fig = plt.figure()
# plt.subplots_adjust(hspace=0.5)
# ax = plt.subplot(111)
# #ax2 = ax.twinx()
# #ax3 = ax.twinx()
# #ax3.set_zorder(ax.get_zorder()+1)
# #ax3.patch.set_visible(False)
# #ax2.set_zorder(ax3.get_zorder()+1)
# #ax2.patch.set_visible(False)
# #ax.set_zorder(ax2.get_zorder()+1)
# #ax.patch.set_visible(False)

# cmap=plt.cm.jet
# norm = BoundaryNorm(np.arange(0,0.55,0.05), cmap.N)

# plt.pcolormesh(date6, y3, mz3, vmin=0, vmax=0.5, norm=norm, cmap=cmap)
# ax.pcolormesh(date6, y3, mz3, vmin=0, vmax=0.5, norm=norm, cmap=cmap)

# # Plot the AOD and SZA
# #ax2.plot(date5, AOD_375, marker='x', c='black', markersize = 3.0, ls='-', label ='AOD (375 nm)')
# #ax2.scatter(date5, AOD_375, marker='x', color='black', label ='AOD (375 nm)')
# #ax3.plot(date4, SZA, marker='x', c='Brown', markersize = 3.0, ls='-', label ='SZA')
# #ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')

# #plt.title('CAMMPCAN V1 2017-18 NO$_2$ VMR', fontsize=25)
# plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,23,0,0,5))

# ax.set_ylabel('Altitude (km)', fontsize=20)
# #ax2.set_ylabel('AOD (375 nm)', fontsize=20)
# #ax3.set_ylabel('SZA ($^\circ$)', fontsize=20)
# ax.set_xlabel('Date', fontsize=20)
# # set the limits of the plot to the limits of the data

# # Format ColorBar
# clb = plt.colorbar(extend='max',pad = 0.13)
# clb.set_label(r"Aerosol extinction at 338 nm (km$^-1$)", fontsize =20, labelpad=10)
# clb.ax.tick_params(labelsize=15)
# tick_locator = ticker.MaxNLocator(nbins=10)
# clb.locator = tick_locator
# clb.update_ticks()

# #clb = plt.colorbar(extend='max')
# #clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=20)
# #clb.ax.tick_params(labelsize=15)
# #tick_locator = ticker.MaxNLocator(nbins=11)
# #clb.locator = tick_locator
# #clb.update_ticks()

# # Format y-axis (NO2)
# ax.yaxis.set_major_locator(ticker.IndexLocator(base=.2, offset=-.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# ax.set_ylim(0.1,3.0) # On Station
# ax.tick_params(axis='y', which='both', colors='Black', labelsize=15)

# ## Format y-axis 2 (AOD)
# #ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# #ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
# #ax2.set_ylim(0,0.5) # On Station
# #ax2.yaxis.label.set_color('Black')
# #ax2.tick_params(axis='y', which='both', colors='Black', labelsize=15)
# #
# ## Format y-axis 3 (SZA)
# #ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# #ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
# #ax3.set_ylim(0,100) # On Station
# #ax3.yaxis.label.set_color('magenta')
# #ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=15)
# #ax3.spines["right"].set_position(("axes", 1.12))
# #ax3.spines["right"].set_color('magenta')

# # Format x-axis
# xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# ax.xaxis.set_major_formatter(xmajor_formatter)
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=2)) # set the interval between dispalyed dates
# ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))

# ax.xaxis.labelpad = 20
# ax.yaxis.labelpad = 20
# ax.tick_params(labelsize=15)

# # Rotates the labels to fit
# fig.autofmt_xdate()

# plt.show()

# ##------------------------------------------------------------------------------
# ## PLOT A COLORMAP OF Aerosol Extinction at 375 nm (NO2)
# #
# #fig = plt.figure()
# #plt.subplots_adjust(hspace=0.5)
# #ax = plt.subplot(111)
# ##ax2 = ax.twinx()
# ##ax3 = ax.twinx()
# ##ax3.set_zorder(ax.get_zorder()+1)
# ##ax3.patch.set_visible(False)
# ##ax2.set_zorder(ax3.get_zorder()+1)
# ##ax2.patch.set_visible(False)
# ##ax.set_zorder(ax2.get_zorder()+1)
# ##ax.patch.set_visible(False)
# #
# #cmap=plt.cm.jet
# #norm = BoundaryNorm(np.arange(0,1.05,0.05), cmap.N)
# #
# #plt.pcolormesh(date7, y4, mz4, vmin=0, vmax=1.0, norm=norm, cmap=cmap)
# #ax.pcolormesh(date7, y4, mz4, vmin=0, vmax=1.0, norm=norm, cmap=cmap)
# #
# ## Plot the AOD and SZA
# ##ax2.plot(date5, AOD_375, marker='x', c='black', markersize = 3.0, ls='-', label ='AOD (375 nm)')
# ##ax2.scatter(date5, AOD_375, marker='x', color='black', label ='AOD (375 nm)')
# ##ax3.plot(date4, SZA, marker='x', c='Brown', markersize = 3.0, ls='-', label ='SZA')
# ##ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')
# #
# ##plt.title('CAMMPCAN V1 2017-18 NO$_2$ VMR', fontsize=25)
# #plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,23,0,0,5))
# #
# #ax.set_ylabel('Altitude (km)', fontsize=20)
# ##ax2.set_ylabel('AOD (375 nm)', fontsize=20)
# ##ax3.set_ylabel('SZA ($^\circ$)', fontsize=20)
# #ax.set_xlabel('Date', fontsize=20)
# ## set the limits of the plot to the limits of the data
# #
# ## Format ColorBar
# #clb = plt.colorbar(extend='max',pad = 0.16)
# #clb.set_label(r"Aerosol extinction at 375 nm (km$^-1$)", fontsize =20, labelpad=10)
# #clb.ax.tick_params(labelsize=15)
# #tick_locator = ticker.MaxNLocator(nbins=20)
# #clb.locator = tick_locator
# #clb.update_ticks()
# #
# ##clb = plt.colorbar(extend='max')
# ##clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=20)
# ##clb.ax.tick_params(labelsize=15)
# ##tick_locator = ticker.MaxNLocator(nbins=11)
# ##clb.locator = tick_locator
# ##clb.update_ticks()
# #
# ## Format y-axis (NO2)
# #ax.yaxis.set_major_locator(ticker.IndexLocator(base=.2, offset=-.2))
# #ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.1,3.0) # On Station
# #ax.tick_params(axis='y', which='both', colors='Black', labelsize=15)
# #
# ### Format y-axis 2 (AOD)
# ##ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ##ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
# ##ax2.set_ylim(0,0.5) # On Station
# ##ax2.yaxis.label.set_color('Black')
# ##ax2.tick_params(axis='y', which='both', colors='Black', labelsize=15)
# ##
# ### Format y-axis 3 (SZA)
# ##ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ##ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
# ##ax3.set_ylim(0,100) # On Station
# ##ax3.yaxis.label.set_color('magenta')
# ##ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=15)
# ##ax3.spines["right"].set_position(("axes", 1.12))
# ##ax3.spines["right"].set_color('magenta')
# #
# ## Format x-axis
# #xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_major_formatter(xmajor_formatter)
# #ax.xaxis.set_major_locator(mdates.DayLocator(interval=2)) # set the interval between dispalyed dates
# #ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
# #
# #ax.xaxis.labelpad = 20
# #ax.yaxis.labelpad = 20
# #ax.tick_params(labelsize=15)
# #
# ## Rotates the labels to fit
# #fig.autofmt_xdate()
# #
# #plt.show()
# #
# ##------------------------------------------------------------------------------
# ## PLOT A COLORMAP OF Aerosol Extinction wl at 360 nm
# #
# #fig = plt.figure()
# #plt.subplots_adjust(hspace=0.5)
# #ax = plt.subplot(111)
# ##ax2 = ax.twinx()
# ##ax3 = ax.twinx()
# ##ax3.set_zorder(ax.get_zorder()+1)
# ##ax3.patch.set_visible(False)
# ##ax2.set_zorder(ax3.get_zorder()+1)
# ##ax2.patch.set_visible(False)
# ##ax.set_zorder(ax2.get_zorder()+1)
# ##ax.patch.set_visible(False)
# #
# #cmap=plt.cm.jet
# #norm = BoundaryNorm(np.arange(0,1.05,0.05), cmap.N)
# #
# #plt.pcolormesh(date8, y5, mz5, vmin=0, vmax=1.0, norm=norm, cmap=cmap)
# #ax.pcolormesh(date8, y5, mz5, vmin=0, vmax=1.0, norm=norm, cmap=cmap)
# #
# ## Plot the AOD and SZA
# ##ax2.plot(date5, AOD_375, marker='x', c='black', markersize = 3.0, ls='-', label ='AOD (375 nm)')
# ##ax2.scatter(date5, AOD_375, marker='x', color='black', label ='AOD (375 nm)')
# ##ax3.plot(date4, SZA, marker='x', c='Brown', markersize = 3.0, ls='-', label ='SZA')
# ##ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')
# #
# ##plt.title('CAMMPCAN V1 2017-18 NO$_2$ VMR', fontsize=25)
# #plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,23,0,0,5))
# ##plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,28,0,0,5))
# #
# #ax.set_ylabel('Altitude (km)', fontsize=20)
# ##ax2.set_ylabel('AOD (375 nm)', fontsize=20)
# ##ax3.set_ylabel('SZA ($^\circ$)', fontsize=20)
# #ax.set_xlabel('Date', fontsize=20)
# ## set the limits of the plot to the limits of the data
# #
# ## Format ColorBar
# #clb = plt.colorbar(extend='max',pad = 0.16)
# #clb.set_label(r"Aerosol extinction wl at 360 nm (km$^-1$)", fontsize =20, labelpad=10)
# #clb.ax.tick_params(labelsize=15)
# #tick_locator = ticker.MaxNLocator(nbins=20)
# #clb.locator = tick_locator
# #clb.update_ticks()
# #
# ##clb = plt.colorbar(extend='max')
# ##clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=20)
# ##clb.ax.tick_params(labelsize=15)
# ##tick_locator = ticker.MaxNLocator(nbins=11)
# ##clb.locator = tick_locator
# ##clb.update_ticks()
# #
# ## Format y-axis (NO2)
# #ax.yaxis.set_major_locator(ticker.IndexLocator(base=.2, offset=-.2))
# #ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
# #ax.set_ylim(0.1,3.0) # On Station
# #ax.tick_params(axis='y', which='both', colors='Black', labelsize=15)
# #
# ### Format y-axis 2 (AOD)
# ##ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ##ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
# ##ax2.set_ylim(0,0.5) # On Station
# ##ax2.yaxis.label.set_color('Black')
# ##ax2.tick_params(axis='y', which='both', colors='Black', labelsize=15)
# ##
# ### Format y-axis 3 (SZA)
# ##ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
# ##ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
# ##ax3.set_ylim(0,100) # On Station
# ##ax3.yaxis.label.set_color('magenta')
# ##ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=15)
# ##ax3.spines["right"].set_position(("axes", 1.12))
# ##ax3.spines["right"].set_color('magenta')
# #
# ## Format x-axis
# #xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
# #ax.xaxis.set_major_formatter(xmajor_formatter)
# #ax.xaxis.set_major_locator(mdates.DayLocator(interval=2)) # set the interval between dispalyed dates
# #ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
# #
# #ax.xaxis.labelpad = 20
# #ax.yaxis.labelpad = 20
# #ax.tick_params(labelsize=15)
# #
# ## Rotates the labels to fit
# #fig.autofmt_xdate()
# #
# #plt.show()