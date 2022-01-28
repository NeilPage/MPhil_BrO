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
from datetime import datetime,time, timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# OBSERVATIONS
# Retrieve the observational data

# SIPEXII
SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/BrO_Retrieval/all_BrO/all_BrO_vmr_prof_20120928.dat', sep='\s+', index_col=0) # BrO data for SIPEXII (2012)

# CAMMPCAN 2017-18
#V1_2017__18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_Retrieval_V1/all_BrO_vmr_V1/all_BrO_vmr_prof_20171028.dat', sep='\s+', index_col=0) # BrO data for CAMPCANN V1 (2017/18)
#V2_2017_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_Retrieval_V2/all_BrO_vmr_V1/all_BrO_vmr_prof_20171028.dat', sep='\s+', index_col=0) # BrO data for CAMPCANN V2 (2017/18)
#V3_2017_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_Retrieval_V3/all_BrO_vmr_V1/all_BrO_vmr_prof_20171028.dat', sep='\s+', index_col=0) # BrO data for CAMPCANN V3 (2017/18)

# CAMMPCAN 2018-19
#V1_2018_19 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_Retrieval_V1/all_BrO/all_BrO_vmr_prof_20181028.dat', sep='\s+', index_col=0) # BrO data for CAMPCANN V1 (2018/19)
#V2_2018_19 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_Retrieval_V2/all_BrO/all_BrO_vmr_prof_20181028.dat', sep='\s+', index_col=0) # BrO data for CAMPCANN V2 (2018/19)
#V3_2018_19 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_Retrieval_V3/all_BrO/all_BrO_vmr_prof_20181028.dat', sep='\s+', index_col=0) # BrO data for CAMPCANN V3 (2018/19)

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

d0 = datetime(2012,9,28,0,10,0)
end = datetime(2012,9,28,23,59,59)
step = timedelta(minutes=20)

date = []

date3 = str(date)
#date3 = datetime.strptime(date3, '%Y-%m-%d %H:%M:%S')

while d0 < end:
    date.append(d0.strftime('%Y-%m-%d %H:%M:%S'))
    d0 += step

#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(date)):
    #date1.append(datetime.strptime(date[i],'%Y-%m-%d %H:%M:%S')+ timedelta(hours=7)) # Davis
    date1.append(datetime.strptime(date[i],'%Y-%m-%d %H:%M:%S')+ timedelta(hours=8)) # Casey, SIPEXII, PCAN
    #date1.append(datetime.strptime(date[i],'%Y-%m-%d %H:%M:%S')+ timedelta(hours=5)) # Mawson

date2 = mdates.date2num(date1)

#------------------------------------------------------------------------------
# SET UP THE VALUES TO PLOT

## SIPEXII
y = SIPEXII.index # set the values for the y-axis
x = np.array(SIPEXII.dtypes.index) # set the values for the x-axis

z = SIPEXII.copy() # identify the matrix containing the z-values (BrO in ppMv)
z[z==-9999]=np.nan # set the erroneous values as NaN 
z = z.loc[:]*1e6 # change from ppMv to pptv

# CAMMPCAN
#y = V1_2018_19.index # set the values for the y-axis
#x = np.array(V1_2018_19.dtypes.index) # set the values for the x-axis

#z = V1_2018_19.copy() # identify the matrix containing the z-values (BrO in ppMv)
#z[z==-9999]=np.nan # set the erroneous values as NaN 
#z = z.loc[:]*1e6 # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz=np.ma.masked_where(np.isnan(z),z) 

#------------------------------------------------------------------------------
# PLOT A COLORMAP OF BrO CONCENTRATIONS

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)
ax=plt.subplot(111)


cmap=plt.cm.jet
norm = BoundaryNorm(np.arange(0,20,1), cmap.N)

#plt.pcolormesh(date, y, mz, cmap='jet')
plt.pcolormesh(date2, y, mz, vmin=0, vmax=20,norm=norm,cmap=cmap)

#plt.pcolormesh(date2, y, mz, cmap='jet')
plt.title('BrO VCD (28 Sep 2012)', fontsize=25)
plt.ylabel('Altitude (km)', fontsize=20)
plt.xlabel('Time (UT)', fontsize=20)
# set the limits of the plot to the limits of the data

clb = plt.colorbar()
clb.set_label(r"BrO (pptv)", fontsize =20, labelpad=20)
clb.ax.tick_params(labelsize=15)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
locs = ax.yaxis.get_ticklocs()
#locs = np.array([0.1,0.5,0.9,1.3,1.7,2.1,2.5,2.9,3.3,3.7])
locs = np.array([0.1,0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1,2.3,2.5,2.7,2.9,3.1,3.3,3.5,3.7,3.9])
ax.set_yticks(locs)

ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

# Setup the DateFormatter for the x axis
date_format = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(date_format)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=20))
#ax.xaxis.set_xlim(datetime(2012,9,28,0,0,0),datetime(2012,9,28,23,59,59))
#ax.set_xlim([datetime(2012,9,28,0,0,0),datetime(2012,9,28,23,59,59)])

ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20
ax.tick_params(labelsize=15)

# Rotates the labels to fit
fig.autofmt_xdate()

plt.show()