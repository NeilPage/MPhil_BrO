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
from matplotlib import gridspec
import matplotlib.image as mpimg

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
V1_2018 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)

# BrO Error
V1_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/BrO_error/V3_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2018/19)

# Calculate the Relative Error (>=0.6)
Filter = V1_Error / V1_2018

# Apply the filter
V1_18F = Filter < 0.6
V1_18T = V1_2018[V1_18F]

#---------
# NO2
#---------

# NO2 VMR
NO2 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_NO2/V3_17_NO2_VMR.csv',index_col=0) # NO2 data for CAMPCANN V1 (2018/19)

# NO2 Error
NO2_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/NO2_error/V3_17_NO2_error.csv', index_col=0) # NO2 error data for CAMPCANN V1 (2018/19)

# Calculate the Relative Error (>=0.6)
Filter2 = NO2_Error / NO2

# Apply the filter
NO2F = Filter2 < 0.6
NO2T = NO2[NO2F]

#---------
# Aerosol
#---------

# Aerosol extinction at 338 nm (BrO)
AeroExt_338 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_Aerosol/V3_17_AeroExt_338.csv',index_col=0) # Aerosol extinction data at 338 nm for CAMPCANN V1 (2017/18)

# Aerosol extinction at 375 nm (NO2)
#AeroExt_375 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_Aerosol/V3_17_AeroExt_375.csv',index_col=0) # Aerosol extinction data at 375 nm for CAMPCANN V1 (2017/18)

# Aerosol extinction wl at 360 nm
AeroExt_360 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_Aerosol/V3_17_AeroExt_wl_360.csv',index_col=0) # Aerosol extinction data at 360 nm for CAMPCANN V1 (2017/18)


#---------
# AOD
#---------

# BrO AOD
BrO_AOD = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_AOD/V3_17_AOD_338.csv',index_col=0) # AOD data for CAMMPCAN V1 (2018/19)

# NO2_AOD
NO2_AOD = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_AOD/V3_17_AOD_375.csv',index_col=0) # AOD data for CAMMPCAN V1 (2018/19)

#---------
# SZA
#---------

DF4_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_SZA/V3_17_SZA.csv',index_col=0) # SZA data for CAMPCANN V1 (2018/19)

#---------
# MET
#---------

SIPEXII_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv', index_col=0) #SIPEXII_underway_60.csv') 

#---------
# O3
#---------

SIPEXII_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv')

#---------
# HYSPLIT
#---------

HYSPLIT_E11 = mpimg.imread('/Users/ncp532/Desktop/Graphs/HYSPLIT/Event11_20180127.gif')

#------------------------------------------------------------------------------
# Filter the SZA for outliers

def hampel_filter_pandas(input_series, window_size, n_sigmas=3):

    k = 1.4826 # scale factor for Gaussian distribution
    new_series = input_series.copy()

    # helper lambda function 
    MAD = lambda x: np.median(np.abs(x - np.median(x)))
    
    rolling_median = input_series.rolling(window=2*window_size, center=True).median()
    rolling_mad = k * input_series.rolling(window=2*window_size, center=True).apply(MAD)
    diff = np.abs(input_series - rolling_median)

    indices = list(np.argwhere(diff > (n_sigmas * rolling_mad)).flatten())
    new_series[indices] = rolling_median[indices]
    
    return new_series, indices

res, detected_outliers = hampel_filter_pandas(DF4_SZA['SZA'],10)

def evaluate_detection(series, true_indices, detected_indices):
    
    # calculate metrics
    tp = list(set(detected_outliers).intersection(set(true_indices)))
    fp = list(set(detected_outliers).difference(set(true_indices)))
    fn = list(set(true_indices).difference(set(detected_outliers)))
    perc_detected = 100 * len(tp) / len(true_indices)
    
    # create the plot
    fix, ax = plt.subplots(2, 1)
    
    ax[0].plot(np.arange(len(series)), series);
    ax[0].scatter(true_indices, series[true_indices], c='g', label='true outlier')
    ax[0].set_title('Original series')
    ax[0].legend()
    
    ax[1].plot(np.arange(len(series)), series);
    ax[1].scatter(tp, series[tp], c='g', label='true positive')
    ax[1].scatter(fp, series[fp], c='r', label='false positive')
    ax[1].scatter(fn, series[fn], c='k', label='false negative')
    ax[1].set_title('Algorithm results')
    ax[1].legend()
    
    # print out summary
    print('-' * 25 + ' Summary ' + '-' * 25)
    print(f'Outliers in the series: {len(true_indices)}')
    print(f'Identified outliers: {len(detected_indices)}')
    print(f'Correctly detected outliers: {len(tp)} ({perc_detected:.2f}% of all outliers).')
    print('-' * 59)
    
    return tp, fp, fn

tp, fp, fn = evaluate_detection(DF4_SZA['SZA'], detected_outliers, detected_outliers)

DF4_SZA = DF4_SZA.drop(DF4_SZA.index[[detected_outliers]])

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
dat3  = np.array(BrO_AOD['Date'])
tim3  = np.array(BrO_AOD['Time'])
Date3 = dat3+' '+tim3

##CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(Date3)):
    date3.append(datetime.strptime(Date3[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

# NO2_AOD
dat5  = np.array(NO2_AOD['Date'])
tim5  = np.array(NO2_AOD['Time'])
Date5 = dat5+' '+tim5

##CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(Date5)):
    date5.append(datetime.strptime(Date5[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

#---------
# SZA
#---------

dat4  = np.array(DF4_SZA['Date'])
tim4  = np.array(DF4_SZA['Time'])
Date4 = dat4+' '+tim4

##CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(Date4)):
    date4.append(datetime.strptime(Date4[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

#---------
# MET
#---------

dat6  = np.array(SIPEXII_Met['Date'])
tim6  = np.array(SIPEXII_Met['Time'])
Date6 = dat6+' '+tim6

##CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(Date6)):
    date6.append(datetime.strptime(Date6[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=8))

#---------
# O3
#---------

dat7  = np.array(SIPEXII_O3['Date'])
tim7  = np.array(SIPEXII_O3['Time'])
Date7 = dat7+' '+tim7

##CONVERT TO DATETIME FROM STRING
date7=[]
for i in range(len(Date7)):
    date7.append(datetime.strptime(Date7[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=8))

#---------
# Aerosol
#---------

# Aerosol extinction at 338 nm (BrO)
Date8 =AeroExt_338.columns.values

#CONVERT TO DATETIME FROM STRING
date8=[]
for i in range(len(Date8)):
    date8.append(datetime.strptime(Date8[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))

## Aerosol extinction at 375 nm (NO2)
#Date9 =AeroExt_375.columns.values
#
##CONVERT TO DATETIME FROM STRING
#date9=[]
#for i in range(len(Date9)):
#    date9.append(datetime.strptime(Date9[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=8))

# Aerosol extinction wl at 360 nm
Date10 =AeroExt_360.columns.values

#CONVERT TO DATETIME FROM STRING
date10=[]
for i in range(len(Date10)):
    date10.append(datetime.strptime(Date10[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=7))
    
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
y  = V1_18T.index # set the values for the y-axis
yT = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8])
x  = np.array(V1_18T.dtypes.index) # set the values for the x-axis
z  = V1_18T.copy() # identify the matrix containing the z-values (BrO in ppMv)

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
# Aerosol
#---------
# Aerosol extinction at 338 nm (BrO)

# All
y3 = AeroExt_338.index # set the values for the y-axis
x3 = np.array(AeroExt_338.dtypes.index) # set the values for the x-axis
z3 = AeroExt_338.copy() # identify the matrix containing the z-values (BrO in ppMv)

z3[z3==-9999]=np.nan # set the erroneous values as NaN 
z3 = z3.loc[:] # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz3=np.ma.masked_where(np.isnan(z3),z3) 

##---------------------------------
## Aerosol extinction at 375 nm (NO2)
#
## All
#y4 = AeroExt_375.index # set the values for the y-axis
#x4 = np.array(AeroExt_375.dtypes.index) # set the values for the x-axis
#z4 = AeroExt_375.copy() # identify the matrix containing the z-values (BrO in ppMv)
#
#z4[z4==-9999]=np.nan # set the erroneous values as NaN 
#z4 = z4.loc[:] # change from ppMv to pptv
#
## when you plot colormaps it changes Nan values to 0.
## Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
#mz4=np.ma.masked_where(np.isnan(z4),z4) 

#---------------------------------
# Aerosol extinction wl at 360 nm

# All
y5 = AeroExt_360.index # set the values for the y-axis
x5 = np.array(AeroExt_360.dtypes.index) # set the values for the x-axis
z5 = AeroExt_360.copy() # identify the matrix containing the z-values (BrO in ppMv)

z5[z5==-9999]=np.nan # set the erroneous values as NaN 
z5 = z5.loc[:] # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz5=np.ma.masked_where(np.isnan(z5),z5) 

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
# MET
#---------

# Pressure
ATM_PRESS = np.array(SIPEXII_Met['ATM_PRESS_HPA'])

# Temperature
TEMP_P    = np.array(SIPEXII_Met['TEMP_AIR_PORT_DEGC'])
TEMP_S    = np.array(SIPEXII_Met['TEMP_AIR_STRBRD_DEGC'])
TEMP      = (TEMP_P+TEMP_S)/2

# Wind Speed
WSP_P     = np.array(SIPEXII_Met['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WSP_S     = np.array(SIPEXII_Met['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WSP       = (WSP_P+WSP_S)/2

# Wind Direction
WDIR_P    = np.array(SIPEXII_Met['WND_DIR_PORT_CORR_DEG'])
WDIR_S    = np.array(SIPEXII_Met['WND_DIR_STRBD_CORR_DEG'])
WDIR      = (WDIR_P+WDIR_S)/2

# Vector Mean Wind Direction
SIPEXII_Met['WD_vect'] = ((WDIR_S * WSP_S) / (WSP_S + WSP_P)) + ((WDIR_P * WSP_P) / (WSP_S + WSP_P))
WD_vect                = SIPEXII_Met['WD_vect']

# Relative Humidity
RH_P      = np.array(SIPEXII_Met['REL_HUMIDITY_PORT_PERCENT'])
RH_S      = np.array(SIPEXII_Met['REL_HUMIDITY_STRBRD_PERCENT'])
RH        = (RH_P+RH_S)/2

#---------
# O3
#---------

O3 = np.array(SIPEXII_O3['O3_(ppb)'])

#------------------------------------------------------------------------------
# Filter the datasets for the ships exhaust
# (remove data when wind direction is 60-190 degrees and wind speed below 5 knots)

DF_O3Met = pd.merge(left=SIPEXII_O3,right=SIPEXII_Met, how='left', left_index=True, right_index=True)

# O3 (remove data when wind direction is 90-270 degrees)
O3_90 = DF_O3Met['WD_vect'] <=90 # <=90
D10 = DF_O3Met[O3_90]
O3_270 = DF_O3Met['WD_vect'] >=270 # >=270 
D11 = DF_O3Met[O3_270]
DFO3 = pd.concat([D10,D11],axis=0)

# Step 3 (Remove data when wind speed is below 5 knots (or 2.57222222 m/s))
O3_5knot = DFO3['WD_vect'] >=2.57222222
DFO3 = DFO3[O3_5knot]

#------------------------------------------------------------------------------
# Filter for the day required

SIPEXIIT = V1_18T
SIPEXIIT.columns = (pd.to_datetime(V1_18T.columns, format='%d/%m/%Y %H:%M:%S')+ timedelta(hours=8)) # SIPEXII timezone is UT+8

# Transpose the dataframe
SIPEXIITT = SIPEXIIT.T

# Event 11 (27 Jan 2018)
start_date = '2018-01-27'
end_date   = '2018-01-28'
Event11    = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event11M   = SIPEXIITT[Event11]


# Transpose the dataframes back again
Event11TT = Event11M.T

#------------------------------------------------------------------------------
# Calculate the mean/StDev and median/MAD BrO VCD for each altitude 

# Event 11
Mean_Event11   = np.mean(Event11TT, axis=1) * 1e6
Median_Event11 = np.median(Event11TT, axis=1) * 1e6
StDev_Event11  = np.std(Event11TT, axis=1) * 1e6
MAD_Event11    = Event11TT.mad(axis=1, skipna='True') * 1e6
MAX_Event11    = np.max(Event11TT, axis=1) * 1e6

#------------------------------------------------------------------------------
# PLOT EVENT 11 (27 January 2018)
#------------------------------------------------------------------------------

fig = plt.figure(figsize=(10,6))
fig.suptitle('27 January 2018', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(date, yT, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(date3, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')

# Format x-axis
plt.xlim(datetime(2018,1,27,0,0,0),datetime(2018,1,27,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
ax.errorbar(MAX_Event11, MAX_Event11.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='Max BrO: 15.4 $\pm$ 1.9 pptv',   xerr=StDev_Event11,   capsize=2)

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(2.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
ax.set_xlim(0,18.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend(loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(date8, yT, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot AEC at 360nm (BrO)
#col1 = ax.pcolormesh(date10, yT, mz5, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(date3, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.scatter(date4, SZA, marker='x', color='magenta', label ='SZA')

# Format x-axis
plt.xlim(datetime(2018,1,27,0,0,0),datetime(2018,1,27,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(date6,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(date6, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(date6, TEMP, marker='o', s= 1.0, color='blue')

# Format x-axis
plt.xlim(datetime(2018,1,27,0,0,0),datetime(2018,1,27,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,20) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-5,5) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(date7, O3,  marker='o', s= 1.0, color='black')
ax2.scatter(date6, ATM_PRESS, marker='o', s= 1.0, color='orange')
ax3.scatter(date6, RH, marker='o', s= 1.0, color='green')

# Format x-axis
plt.xlim(datetime(2018,1,27,0,0,0),datetime(2018,1,27,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,30) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(980,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Relative humidity)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(40,100) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 6 (HYSPLIT back trajectory)
ax = fig.add_subplot(gs[1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot the HYSPLIT image
ax.imshow(HYSPLIT_E11)

# Turn off the image axis
plt.axis('off')

# Adjust the position of the image
box = ax.get_position()
box.y0 = box.y0 - 0.04
box.y1 = box.y1 - 0.04
ax.set_position(box)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.075, 0.875, "f", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
