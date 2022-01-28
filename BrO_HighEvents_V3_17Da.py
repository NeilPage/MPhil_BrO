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

#---------
# BrO
#---------
# BrO VMR
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)

# BrO Error
Err_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/BrO_error/V1_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2018/19)

# Calculate the Relative Error (>=0.6)
Filter    = Err_V1_17 / BrO_V1_17

# Apply the filter
V1_17F    = Filter < 0.6
BrO_V1_17 = BrO_V1_17[V1_17F]

#---------
# Aerosol extinction at 338 nm (BrO)
#---------
AEC_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_Aerosol/V1_17_AeroExt_338.csv',index_col=0) # Aerosol extinction data at 338 nm for CAMPCANN V1 (2017/18)

#---------
# AOD
#---------
AOD_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_AOD/V1_17_AOD_338.csv',index_col=0) # AOD data for CAMMPCAN V1 (2018/19)

#---------
# SZA
#---------
SZA_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_SZA/V1_17_SZA.csv',index_col=0) # SZA data for CAMPCANN V1 (2018/19)

#---------
# MET
#---------
Met_V1_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V1_17_underway_60.csv', index_col=0)

#---------
# O3
#---------
O3_V1_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv')

#---------
# HYSPLIT
#---------
HYSPLIT_E1_2 = mpimg.imread('/Users/ncp532/Documents/Graphs/HYSPLIT/Event1_2_20171114.gif')
HYSPLIT_E3_4 = mpimg.imread('/Users/ncp532/Documents/Graphs/HYSPLIT/Event3_4_20171115.gif')
HYSPLIT_E5   = mpimg.imread('/Users/ncp532/Documents/Graphs/HYSPLIT/Event5_20171116.gif')
HYSPLIT_E6_7 = mpimg.imread('/Users/ncp532/Documents/Graphs/HYSPLIT/Event6_7_20171120.gif')
HYSPLIT_E8   = mpimg.imread('/Users/ncp532/Documents/Graphs/HYSPLIT/Event8_20171121.gif')

#------------------------------------------------------------------------------
# TRANSPOSE THE MAX-DOAS DATAFRAMES

BrO_V1_17 = BrO_V1_17.T
AEC_V1_17 = AEC_V1_17.T

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

#---------
# BrO
#---------
BrO_V1_17.index = (pd.to_datetime(BrO_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# Aerosol extinction at 338 nm (BrO)
#---------
AEC_V1_17.index = (pd.to_datetime(AEC_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# AOD
#---------
AOD_V1_17.index = (pd.to_datetime(AOD_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# SZA
#---------
SZA_V1_17.index = (pd.to_datetime(SZA_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# MET
#---------
Met_V1_17.index = (pd.to_datetime(Met_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# O3
#---------
O3_V1_17.index  = (pd.to_datetime(O3_V1_17.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
    
#------------------------------------------------------------------------------
# Filter the SZA for outliers

# Define the filter
def hampel(vals_orig, k=11, t0=3):
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

# Apply the filter
SZA_V1_17 = hampel(SZA_V1_17['SZA'])

#------------------------------------------------------------------------------
# Filter for the day required

SIPEXIITT = BrO_V1_17


# Event 1 and 2 (14 Nov 2017)
start_date = '2017-11-14'
end_date   = '2017-11-15'
Event1_2   = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event1_2M  = SIPEXIITT[Event1_2]

# Event 3 and 4 (15 Nov 2017)
start_date = '2017-11-15'
end_date   = '2017-11-16'
Event3_4   = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event3_4M  = SIPEXIITT[Event3_4]

# Event 5 (16 Nov 2017)
start_date = '2017-11-16'
end_date   = '2017-11-17'
Event5     = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event5M    = SIPEXIITT[Event5]

# Event 6 and 7 (20 Nov 2017)
start_date = '2017-11-20'
end_date   = '2017-11-21'
Event6_7   = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event6_7M  = SIPEXIITT[Event6_7]

# Event 8 (21 Nov 2017)
start_date = '2017-11-21'
end_date   = '2017-11-22'
Event8     = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event8M    = SIPEXIITT[Event8]

# Transpose the dataframes back again
Event1_2TT = Event1_2M.T
Event3_4TT = Event3_4M.T
Event5TT   = Event5M.T
Event6_7TT = Event6_7M.T
Event8TT   = Event8M.T

#------------------------------------------------------------------------------
# SET UP THE VALUES TO PLOT

#---------
# BrO
#---------
# Transpose BrO
BrO_V1_17 = BrO_V1_17.T

# All
#y = V1_2018.index # set the values for the y-axis
#x = np.array(V1_2018.dtypes.index) # set the values for the x-axis
#z = V1_2018.copy() # identify the matrix containing the z-values (BrO in ppMv)

# Filtered
y  = BrO_V1_17.index # set the values for the y-axis
x  = np.array(BrO_V1_17.dtypes.index) # set the values for the x-axis
z  = BrO_V1_17.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z[z==-9999]=np.nan # set the erroneous values as NaN 
z = z.loc[:]*1e6 # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz=np.ma.masked_where(np.isnan(z),z) 

#---------
# Aerosol extinction at 338 nm (BrO)
#---------
# Transpose AEC
AEC_V1_17 = AEC_V1_17.T

# All
y3 = AEC_V1_17.index # set the values for the y-axis
x3 = np.array(AEC_V1_17.dtypes.index) # set the values for the x-axis
z3 = AEC_V1_17.copy() # identify the matrix containing the z-values (BrO in ppMv)

z3[z3==-9999]=np.nan # set the erroneous values as NaN 
z3 = z3.loc[:] # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz3=np.ma.masked_where(np.isnan(z3),z3) 

#---------
# AOD
#---------
AOD_338 = np.array(AOD_V1_17['AOD'])

#---------
# SZA
#---------
SZA = SZA_V1_17

#---------
# MET
#---------
# Pressure
ATM_PRESS = np.array(Met_V1_17['atm_press_hpa'])

# Temperature
TEMP_P    = np.array(Met_V1_17['temp_air_port_degc'])
TEMP_S    = np.array(Met_V1_17['temp_air_strbrd_degc'])
TEMP      = (TEMP_P + TEMP_S) / 2

# Wind Speed
WSP_P     = np.array(Met_V1_17['wnd_spd_port_corr_knot'])   * 0.514444444 # Convert from knots to m/s
WSP_S     = np.array(Met_V1_17['wnd_spd_strbrd_corr_knot']) * 0.514444444 # Convert from knots to m/s
WSP       = (WSP_P + WSP_S) / 2

# Wind Direction
WDIR_P    = np.array(Met_V1_17['wnd_dir_port_corr_deg'])
WDIR_S    = np.array(Met_V1_17['wnd_dir_strbrd_corr_deg'])
WDIR      = (WDIR_P + WDIR_S) / 2

# Vector Mean Wind Direction
Met_V1_17['WD_vect'] = ((WDIR_S * WSP_S) / (WSP_S + WSP_P)) + ((WDIR_P * WSP_P) / (WSP_S + WSP_P))
WD_vect              = Met_V1_17['WD_vect']

# Relative Humidity
RH_P      = np.array(Met_V1_17['rel_humidity_port_percent'])
RH_S      = np.array(Met_V1_17['rel_humidity_strbrd_percent'])
RH        = (RH_P + RH_S) / 2

#---------
# O3
#---------

O3 = np.array(O3_V1_17['O3_(ppb)'])

#------------------------------------------------------------------------------
# Filter the datasets for the ships exhaust
# (remove data when wind direction is 60-190 degrees and wind speed below 5 knots)

DF_O3Met = pd.merge(left=O3_V1_17,right=Met_V1_17, how='left', left_index=True, right_index=True)

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
# Calculate the mean/StDev and median/MAD BrO VCD for each altitude 

# Event 1 and 2
Mean_Event1_2   = np.mean(Event1_2TT, axis=1) * 1e6
Median_Event1_2 = np.nanmedian(Event1_2TT, axis=1) * 1e6
StDev_Event1_2  = np.std(Event1_2TT, axis=1) * 1e6
MAD_Event1_2    = Event1_2TT.mad(axis=1, skipna='True') * 1e6
MAX_Event1_2    = np.max(Event1_2TT, axis=1) * 1e6
MIN_Event1_2    = np.min(Event1_2TT, axis=1) * 1e6

# Event 3 and 4
Mean_Event3_4   = np.mean(Event3_4TT, axis=1) * 1e6
Median_Event3_4 = np.nanmedian(Event3_4TT, axis=1) * 1e6
StDev_Event3_4  = np.std(Event3_4TT, axis=1) * 1e6
MAD_Event3_4    = Event3_4TT.mad(axis=1, skipna='True') * 1e6
MAX_Event3_4    = np.max(Event3_4TT, axis=1) * 1e6
MIN_Event3_4    = np.min(Event3_4TT, axis=1) * 1e6

# Event 5
Mean_Event5   = np.mean(Event5TT, axis=1) * 1e6
Median_Event5 = np.nanmedian(Event5TT, axis=1) * 1e6
StDev_Event5  = np.std(Event5TT, axis=1) * 1e6
MAD_Event5    = Event5TT.mad(axis=1, skipna='True') * 1e6
MAX_Event5    = np.max(Event5TT, axis=1) * 1e6
MIN_Event5    = np.min(Event5TT, axis=1) * 1e6

# Event 6 and 7
Mean_Event6_7   = np.mean(Event6_7TT, axis=1) * 1e6
Median_Event6_7 = np.nanmedian(Event6_7TT, axis=1) * 1e6
StDev_Event6_7  = np.std(Event6_7TT, axis=1) * 1e6
MAD_Event6_7    = Event6_7TT.mad(axis=1, skipna='True') * 1e6
MAX_Event6_7    = np.max(Event6_7TT, axis=1) * 1e6
MIN_Event6_7    = np.min(Event6_7TT, axis=1) * 1e6

# Event 8
Mean_Event8   = np.mean(Event8TT, axis=1) * 1e6
Median_Event8 = np.nanmedian(Event8TT, axis=1) * 1e6
StDev_Event8  = np.std(Event8TT, axis=1) * 1e6
MAD_Event8    = Event8TT.mad(axis=1, skipna='True') * 1e6
MAX_Event8    = np.max(Event8TT, axis=1) * 1e6
MIN_Event8    = np.min(Event8TT, axis=1) * 1e6

#------------------------------------------------------------------------------
# PLOT EVENT 1 and 2 (14 November 2017)
#------------------------------------------------------------------------------

fig = plt.figure(figsize=(10,6))
fig.suptitle('14 November 2017', fontsize=20, y=0.95)
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
col1 = ax.pcolormesh(x, y, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
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
ax.errorbar(MAX_Event1_2, MAX_Event1_2.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='Max BrO: 9.3 $\pm$ 1.5 pptv',   xerr=StDev_Event1_2,   capsize=2)

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,11.0)
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

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
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
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
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
ax.set_ylim(0,10) # On Station
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
ax3.set_ylim(-10,0) # On Station
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
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
ax3.scatter(Met_V1_17.index, RH, marker='o', s= 1.0, color='green')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
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
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,990) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Relative humidity)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(30,80) # On Station
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
ax.imshow(HYSPLIT_E1_2)

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

#------------------------------------------------------------------------------
# PLOT EVENT 3 and 4 (15 November 2017)
#------------------------------------------------------------------------------

fig = plt.figure(figsize=(10,6))
fig.suptitle('15 November 2017', fontsize=20, y=0.95)
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
col1 = ax.pcolormesh(x, y, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
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
ax.errorbar(MAX_Event3_4, MAX_Event3_4.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='Max BrO: 9.5 $\pm$ 1.4 pptv',   xerr=StDev_Event3_4,   capsize=2)

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,11.0)
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

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
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
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
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
ax.set_ylim(0,10) # On Station
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
ax3.set_ylim(-15,0) # On Station
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
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
ax3.scatter(Met_V1_17.index, RH, marker='o', s= 1.0, color='green')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
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
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(980,990) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Relative humidity)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(30,90) # On Station
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
ax.imshow(HYSPLIT_E3_4)

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

#------------------------------------------------------------------------------
# PLOT EVENT 5 (16 November 2017)
#------------------------------------------------------------------------------

fig = plt.figure(figsize=(10,6))
fig.suptitle('16 November 2017', fontsize=20, y=0.95)
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
col1 = ax.pcolormesh(x, y, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
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
ax.errorbar(MAX_Event5, MAX_Event5.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='Max BrO: 8.4 $\pm$ 1.3 pptv',   xerr=StDev_Event5,   capsize=2)

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,11.0)
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

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
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
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
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
ax.set_ylim(0,10) # On Station
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
ax3.set_ylim(-15,0) # On Station
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
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
ax3.scatter(Met_V1_17.index, RH, marker='o', s= 1.0, color='green')

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
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
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Relative humidity)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(30,90) # On Station
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
ax.imshow(HYSPLIT_E5)

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

#------------------------------------------------------------------------------
# PLOT EVENT 6 and 7 (20 November 2017)
#------------------------------------------------------------------------------

fig = plt.figure(figsize=(10,6))
fig.suptitle('20 November 2017', fontsize=20, y=0.95)
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
col1 = ax.pcolormesh(x, y, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
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
ax.errorbar(MAX_Event6_7, MAX_Event6_7.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='Max BrO: 8.8 $\pm$ 1.3 pptv',   xerr=StDev_Event6_7,   capsize=2)

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,11.0)
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

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
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
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
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
ax.set_ylim(0,10) # On Station
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
ax3.set_ylim(-10,0) # On Station
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
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
ax3.scatter(Met_V1_17.index, RH, marker='o', s= 1.0, color='green')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
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
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Relative humidity)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(40,90) # On Station
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
ax.imshow(HYSPLIT_E6_7)

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

#------------------------------------------------------------------------------
# PLOT EVENT 8 (21 November 2017)
#------------------------------------------------------------------------------

fig = plt.figure(figsize=(10,6))
fig.suptitle('21 November 2017', fontsize=20, y=0.95)
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
col1 = ax.pcolormesh(x, y, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
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
ax.errorbar(MAX_Event8, MAX_Event8.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='Max BrO: 8.3 $\pm$ 1.4 pptv',   xerr=StDev_Event8,   capsize=2)

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,11.0)
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

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
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
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
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
ax.set_ylim(0,10) # On Station
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
ax3.set_ylim(-15,0) # On Station
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
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
ax3.scatter(Met_V1_17.index, RH, marker='o', s= 1.0, color='green')

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
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
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Relative humidity)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(40,90) # On Station
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
ax.imshow(HYSPLIT_E8)

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
