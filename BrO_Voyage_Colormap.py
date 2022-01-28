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
from matplotlib.ticker import MaxNLocator

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import signal, stats

# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# OBSERVATIONS
# Retrieve the observational data


#---------------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#---------------------------------
#SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/BrO_VMR.csv',index_col=0) # BrO data for SIPEXII (2012)

#---------------------------------
# V1_17 Davis (14-22 Nov 2017)
#---------------------------------
V1_2017 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_VMR_V1.csv', index_col=0) # BrO data for CAMPCANN V1 (2017/18)

#---------------------------------
# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
#---------------------------------
#V2_2017 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_VMR_V2.csv', index_col=0) # BrO data for CAMPCANN V2 (2017/18)

#---------------------------------
# V3_17 Mawson (1-17 Feb 2018)
#---------------------------------
#V3_2017 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_VMR_V3.csv', index_col=0) # BrO data for CAMPCANN V3 (2017/18)

#---------------------------------
# V1_18 Davis (7-15 Nov 2018)
#---------------------------------
#V1_2018 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_VMR_V1.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)

#---------------------------------
# V2_18 Casey (15-30 Dec 2018)
#---------------------------------
#V2_2018 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_VMR_V2.csv', index_col=0) # BrO data for CAMPCANN V2 (2018/19)

#---------------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#---------------------------------
#V3_2018 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_VMR_V3.csv', index_col=0) # BrO data for CAMPCANN V3 (2018/19)

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

#Date1 = SIPEXII.columns.values
Date1 = V1_2017.columns.values
#Date1 = V2_2017.columns.values
#Date1 = V3_2017.columns.values
#Date1 = V1_2018.columns.values
#Date1 = V2_2018.columns.values
#Date1 = V3_2018.columns.values

#CONVERT TO DATETIME FROM STRING
date=[]
for i in range(len(Date1)):
    date.append(datetime.strptime(Date1[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------------------------------------------------
# SET UP THE VALUES TO PLOT

#---------------------------------
# SIPEXII
#---------------------------------
#y = SIPEXII.index # set the values for the y-axis
#x = np.array(SIPEXII.dtypes.index) # set the values for the x-axis
#z = SIPEXII.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
# CAMMPCAN 2017-18
#---------------------------------
y = V1_2017.index # set the values for the y-axis
x = np.array(V1_2017.dtypes.index) # set the values for the x-axis
z = V1_2017.copy() # identify the matrix containing the z-values (BrO in ppMv)

#y = V2_2017.index # set the values for the y-axis
#x = np.array(V2_2017.dtypes.index) # set the values for the x-axis
#z = V2_2017.copy() # identify the matrix containing the z-values (BrO in ppMv)

#y = V3_2017.index # set the values for the y-axis
#x = np.array(V3_2017.dtypes.index) # set the values for the x-axis
#z = V3_2017.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
# CAMMPCAN 2018-19
#---------------------------------
#y = V1_2018.index # set the values for the y-axis
#x = np.array(V1_2018.dtypes.index) # set the values for the x-axis
#z = V1_2018.copy() # identify the matrix containing the z-values (BrO in ppMv)

#y = V2_2018.index # set the values for the y-axis
#x = np.array(V2_2018.dtypes.index) # set the values for the x-axis
#z = V2_2018.copy() # identify the matrix containing the z-values (BrO in ppMv)

#y = V3_2018.index # set the values for the y-axis
#x = np.array(V3_2018.dtypes.index) # set the values for the x-axis
#z = V3_2018.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z[z==-9999]=np.nan # set the erroneous values as NaN 
z = z.loc[:]*1e6 # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz=np.ma.masked_where(np.isnan(z),z) 

#------------------------------------------------------------------------------
# PLOT A COLORMAP OF BrO CONCENTRATIONS

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)
ax=plt.subplot(111)

#plt.pcolormesh(date, y, mz, cmap='jet')
plt.pcolormesh(date, y, mz, vmin=0, vmax=15,cmap='jet')

#plt.title('SIPEXII BrO VMR', fontsize=25)
#plt.xlim(datetime(2012,9,23,0,1,0),datetime(2012,11,11,23,59,0))

plt.title('CAMMPCAN V1 2017-18 BrO VMR', fontsize=25)
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,22,23,59,0))

#plt.title('CAMMPCAN V2 2017-18 BrO VMR', fontsize=25)
#plt.xlim(datetime(2017,12,21,0,0,0),datetime(2018,1,5,23,59,0))

#plt.title('CAMMPCAN V3 2017-18 BrO VMR', fontsize=25)
#plt.xlim(datetime(2018,2,1,0,0,0),datetime(2018,2,17,23,59,0))

#plt.title('CAMMPCAN V1 2018-19 BrO VMR', fontsize=25)
#plt.xlim(datetime(2018,11,7,0,0,0),datetime(2018,11,15,23,59,0))

#plt.title('CAMMPCAN V2 2018-19 BrO VMR', fontsize=25)
#plt.xlim(datetime(2018,12,15,0,0,0),datetime(2018,12,30,23,59,0))

#plt.title('CAMMPCAN V3 2018-19 BrO VMR', fontsize=25)
#plt.xlim(datetime(2019,1,30,0,0,0),datetime(2019,2,9,23,59,0))

plt.ylabel('Altitude (km)', fontsize=20)
plt.xlabel('Date', fontsize=20)
# set the limits of the plot to the limits of the data

clb = plt.colorbar()
clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=20)
clb.ax.tick_params(labelsize=15)
# Setup the DateFormatter for the x axis
#date_format = mdates.DateFormatter('%H:%M:%S')
#ax.xaxis.set_major_formatter(date_format)
#ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))

# Format x-axis
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20
ax.tick_params(labelsize=15)

# Rotates the labels to fit
fig.autofmt_xdate()

plt.show()