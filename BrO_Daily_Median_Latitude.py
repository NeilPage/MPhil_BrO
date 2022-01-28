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

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# CAMMPCAN 2017-18
V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V1/V1_BrO_QAQC_Time.csv')
V1_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv') 

V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V2/V2_BrO_QAQC_Time.csv')
V2_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv') 

V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V3/V3_BrO_QAQC_Time.csv')
V3_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv') 

# CAMMPCAN 2018-19
V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V1/V1_BrO_QAQC_Time.csv')
V1_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv') 

V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V2/V2_BrO_QAQC_Time.csv')
V2_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv') 

V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V3/V3_BrO_QAQC_Time.csv')
V3_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv') 

#------------------------------------------------------------------------------
# Define the variables

# CAMMPCAN (2017-18)
BrO_V1_17 = np.array(V1_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V1_17 = np.array(V1_17_Met['LATITUDE'])

BrO_V2_17 = np.array(V2_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V2_17 = np.array(V2_17_Met['LATITUDE'])

BrO_V3_17 = np.array(V3_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V3_17 = np.array(V3_17_Met['LATITUDE'])

# CAMMPCAN (2018-19)
BrO_V1_18 = np.array(V1_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V1_18 = np.array(V1_18_Met['LATITUDE'])

BrO_V2_18 = np.array(V2_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V2_18 = np.array(V2_18_Met['LATITUDE'])

BrO_V3_18 = np.array(V3_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V3_18 = np.array(V3_18_Met['LATITUDE'])

#------------------------------------------------------------------------------
# SET THE DATE AND TIME
#------------------------------------
V1_17['Date_Time'] = V1_17['DateTime']
V1_17['Date_Time'] = pd.to_datetime(V1_17['Date_Time'])
V1_17 = V1_17.sort_values('Date_Time').set_index('Date_Time')

# V1_17
dattim1 = np.array(V1_17['DateTime'])
#tim1 = np.array(V1_BrO['Time'])
#dattim1 = dat1+' '+tim1

#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    date1.append(datetime.strptime(dattim1[i],'%d/%m/%Y %H:%M:%S'))

# V1_17_Met
datM1 = np.array(V1_17_Met['Date'])
timM1 = np.array(V1_17_Met['Time'])
dattimM1 = datM1+' '+timM1

#CONVERT TO DATETIME FROM STRING
dateM1=[]
for i in range(len(dattimM1)):
    dateM1.append(datetime.strptime(dattimM1[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------    
V2_17['Date_Time'] = V2_17['DateTime']
V2_17['Date_Time'] = pd.to_datetime(V2_17['Date_Time'])
V2_17 = V2_17.sort_values('Date_Time').set_index('Date_Time')

# V2_17
dattim2 = np.array(V2_17['DateTime'])
#tim2 = np.array(V2_BrO['Time'])
#dattim2 = dat+2' '+tim2

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S'))

# V2_17_Met
datM2 = np.array(V2_17_Met['Date'])
timM2 = np.array(V2_17_Met['Time'])
dattimM2 = datM2+' '+timM2

#CONVERT TO DATETIME FROM STRING
dateM2=[]
for i in range(len(dattimM2)):
    dateM2.append(datetime.strptime(dattimM2[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------
V3_17['Date_Time'] = V3_17['DateTime']
V3_17['Date_Time'] = pd.to_datetime(V3_17['Date_Time'])
V3_17 = V3_17.sort_values('Date_Time').set_index('Date_Time')

# V3_17
dattim3 = np.array(V3_17['DateTime'])
#tim3 = np.array(V3_BrO['Time'])
#dattim3 = dat3+' '+tim3

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S'))

# V3_17_Met
datM3 = np.array(V3_17_Met['Date'])
timM3 = np.array(V3_17_Met['Time'])
dattimM3 = datM3+' '+timM3

#CONVERT TO DATETIME FROM STRING
dateM3=[]
for i in range(len(dattimM3)):
    dateM3.append(datetime.strptime(dattimM3[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------
V1_18['Date_Time'] = V1_18['DateTime']
V1_18['Date_Time'] = pd.to_datetime(V1_18['Date_Time'])
V1_18 = V1_18.sort_values('Date_Time').set_index('Date_Time')

# V1_18
dattim4 = np.array(V1_18['DateTime'])
#tim4 = np.array(V1_BrO['Time'])
#dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S'))

# V1_18_Met
datM4 = np.array(V1_18_Met['Date'])
timM4 = np.array(V1_18_Met['Time'])
dattimM4 = datM4+' '+timM4

#CONVERT TO DATETIME FROM STRING
dateM4=[]
for i in range(len(dattimM4)):
    dateM4.append(datetime.strptime(dattimM4[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------
V2_18['Date_Time'] = V2_18['DateTime']
V2_18['Date_Time'] = pd.to_datetime(V2_18['Date_Time'])
V2_18 = V2_18.sort_values('Date_Time').set_index('Date_Time')

# V2_18
dattim5 = np.array(V2_18['DateTime'])
#tim5 = np.array(V2_BrO['Time'])
#dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S'))

# V2_18_Met
datM5 = np.array(V2_18_Met['Date'])
timM5 = np.array(V2_18_Met['Time'])
dattimM5 = datM5+' '+timM5

#CONVERT TO DATETIME FROM STRING
dateM5=[]
for i in range(len(dattimM5)):
    dateM5.append(datetime.strptime(dattimM5[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------
V3_18['Date_Time'] = V3_18['DateTime']
V3_18['Date_Time'] = pd.to_datetime(V3_18['Date_Time'])
V3_18 = V3_18.sort_values('Date_Time').set_index('Date_Time')

# V3_18
dattim6 = np.array(V3_18['DateTime'])
#tim6 = np.array(V3_BrO['Time'])
#dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    date6.append(datetime.strptime(dattim6[i],'%d/%m/%Y %H:%M:%S'))

# V3_18_Met
datM6 = np.array(V3_18_Met['Date'])
timM6 = np.array(V3_18_Met['Time'])
dattimM6 = datM6+' '+timM6

#CONVERT TO DATETIME FROM STRING
dateM6=[]
for i in range(len(dattimM6)):
    dateM6.append(datetime.strptime(dattimM6[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------------------------------------------------
# CALCULATE THE BRO DAILY MEDIAN

# Function to calculate the daily mean
def dailyM(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('D').median()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Daily Means
BrO_V1_17_DM, date1_DM=dailyM(BrO_V1_17[:],date1) # V1_17
BrO_V2_17_DM, date2_DM=dailyM(BrO_V2_17[:],date2) # V2_17
BrO_V3_17_DM, date3_DM=dailyM(BrO_V3_17[:],date3) # V3_17
BrO_V1_18_DM, date4_DM=dailyM(BrO_V1_18[:],date4) # V1_18
BrO_V2_18_DM, date5_DM=dailyM(BrO_V2_18[:],date5) # V2_18
BrO_V3_18_DM, date6_DM=dailyM(BrO_V3_18[:],date6) # V3_18

# Latitude Daily Means
Lat_V1_17_DM, dateM1_DM=dailyM(Lat_V1_17[:],dateM1) # V1_17
Lat_V2_17_DM, dateM2_DM=dailyM(Lat_V2_17[:],dateM2) # V2_17
Lat_V3_17_DM, dateM3_DM=dailyM(Lat_V3_17[:],dateM3) # V3_17
Lat_V1_18_DM, dateM4_DM=dailyM(Lat_V1_18[:],dateM4) # V1_18
Lat_V2_18_DM, dateM5_DM=dailyM(Lat_V2_18[:],dateM5) # V2_18
Lat_V3_18_DM, dateM6_DM=dailyM(Lat_V3_18[:],dateM6) # V3_18

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN ABSOLUTE DEVIATION FOR THE BRO DAILY MEDIAN
# MAD = median(| x - median(x)|)

#------------------------------------
# V1_17

# 1) Find the median
V1_17_MEDIAN = (V1_17['surf_vmr(ppmv)'].rolling('1d').median())*1e6
# 2) subtract the median from each value in X
V1_17_X = np.array(V1_17['surf_vmr(ppmv)']) * 1e6 
V1_17_X_M = V1_17_X - V1_17_MEDIAN
# 3) find the absolute value for the difference
V1_17_ABS = V1_17_X_M.abs()
# 4) find the median of the absolute difference
V1_17_MAD = V1_17_ABS.rolling('1d').median()
V1_17_MAD = V1_17_MAD.resample('1d').mean() # convert the MAD to a daily value
V1_17_MAD = np.array(V1_17_MAD[:]) # convert from pandas.df to np.array
#V1_17_MAD = V1_17_MAD[~np.isnan(V1_17_MAD)]

#------------------------------------
# V2_17

# 1) Find the median
V2_17_MEDIAN = (V2_17['surf_vmr(ppmv)'].rolling('1d').median())*1e6
# 2) subtract the median from each value in X
V2_17_X = np.array(V2_17['surf_vmr(ppmv)']) * 1e6 
V2_17_X_M = V2_17_X - V2_17_MEDIAN
# 3) find the absolute value for the difference
V2_17_ABS = V2_17_X_M.abs()
# 4) find the median of the absolute difference
V2_17_MAD = V2_17_ABS.rolling('1d').median()
V2_17_MAD = V2_17_MAD.resample('1d').mean() # convert the MAD to a daily value
V2_17_MAD = np.array(V2_17_MAD[:]) # convert from pandas.df to np.array

#------------------------------------
# V3_17

# 1) Find the median
V3_17_MEDIAN = (V3_17['surf_vmr(ppmv)'].rolling('1d').median())*1e6
# 2) subtract the median from each value in X
V3_17_X = np.array(V3_17['surf_vmr(ppmv)']) * 1e6 
V3_17_X_M = V3_17_X - V3_17_MEDIAN
# 3) find the absolute value for the difference
V3_17_ABS = V3_17_X_M.abs()
# 4) find the median of the absolute difference
V3_17_MAD = V3_17_ABS.rolling('1d').median()
V3_17_MAD = V3_17_MAD.resample('1d').mean() # convert the MAD to a daily value
V3_17_MAD = np.array(V3_17_MAD[:]) # convert from pandas.df to np.array

#------------------------------------
# V1_18

# 1) Find the median
V1_18_MEDIAN = (V1_18['surf_vmr(ppmv)'].rolling('1d').median())*1e6
# 2) subtract the median from each value in X
V1_18_X = np.array(V1_18['surf_vmr(ppmv)']) * 1e6 
V1_18_X_M = V1_18_X - V1_18_MEDIAN
# 3) find the absolute value for the difference
V1_18_ABS = V1_18_X_M.abs()
# 4) find the median of the absolute difference
V1_18_MAD = V1_18_ABS.rolling('1d').median()
V1_18_MAD = V1_18_MAD.resample('1d').mean() # convert the MAD to a daily value
V1_18_MAD = np.array(V1_18_MAD[:]) # convert from pandas.df to np.array

#------------------------------------
# V2_18

# 1) Find the median
V2_18_MEDIAN = (V2_18['surf_vmr(ppmv)'].rolling('1d').median())*1e6
# 2) subtract the median from each value in X
V2_18_X = np.array(V2_18['surf_vmr(ppmv)']) * 1e6 
V2_18_X_M = V2_18_X - V2_18_MEDIAN
# 3) find the absolute value for the difference
V2_18_ABS = V2_18_X_M.abs()
# 4) find the median of the absolute difference
V2_18_MAD = V2_18_ABS.rolling('1d').median()
V2_18_MAD = V2_18_MAD.resample('1d').mean() # convert the MAD to a daily value
V2_18_MAD = np.array(V2_18_MAD[:]) # convert from pandas.df to np.array

#------------------------------------
# V3_18

# 1) Find the median
V3_18_MEDIAN = (V3_18['surf_vmr(ppmv)'].rolling('1d').median())*1e6
# 2) subtract the median from each value in X
V3_18_X = np.array(V3_18['surf_vmr(ppmv)']) * 1e6 
V3_18_X_M = V3_18_X - V3_18_MEDIAN
# 3) find the absolute value for the difference
V3_18_ABS = V3_18_X_M.abs()
# 4) find the median of the absolute difference
V3_18_MAD = V3_18_ABS.rolling('1d').median()
V3_18_MAD = V3_18_MAD.resample('1d').mean() # convert the MAD to a daily value
V3_18_MAD = np.array(V3_18_MAD[:]) # convert from pandas.df to np.array

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(231) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date1_DM, BrO_V1_17_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')
ax2.plot(dateM1_DM, Lat_V1_17_DM, ls='--', c='black', label ='Latitude')

UL1 = BrO_V1_17_DM + V1_17_MAD # find the upper limit
LL1 = BrO_V1_17_DM - V1_17_MAD # find the lower limit
ax.plot(date1_DM, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date1_DM, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date1_DM, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
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
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2
ax=plt.subplot(232) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date2_DM, BrO_V2_17_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V2 (2017-18)')
ax2.plot(dateM2_DM, Lat_V2_17_DM, ls='--', c='black', label ='Latitude')

UL2 = BrO_V2_17_DM + V2_17_MAD # find the upper limit
LL2 = BrO_V2_17_DM - V2_17_MAD # find the lower limit
ax.plot(date2_DM, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date2_DM, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date2_DM, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
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
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('BrO Daily Median for CAMMPCAN 2017-18 and 2018-19 Voyages', fontsize=25, y=1.05)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 3
ax=plt.subplot(233) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date3_DM, BrO_V3_17_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V3 (2017-18)')
ax2.plot(dateM3_DM, Lat_V3_17_DM, ls='--', c='black', label ='Latitude')

UL3 = BrO_V3_17_DM + V3_17_MAD # find the upper limit
LL3 = BrO_V3_17_DM - V3_17_MAD # find the lower limit
ax.plot(date3_DM, UL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date3_DM, LL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date3_DM, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
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
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 4
ax=plt.subplot(234) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date4_DM, BrO_V1_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2018-19)')
ax2.plot(dateM4_DM, Lat_V1_18_DM, ls='--', c='black', label ='Latitude')

UL4 = BrO_V1_18_DM + V1_18_MAD # find the upper limit
LL4 = BrO_V1_18_DM - V1_18_MAD # find the lower limit
ax.plot(date4_DM, UL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date4_DM, LL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date4_DM, UL4, LL4, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
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
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 5
ax=plt.subplot(235) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date5_DM, BrO_V2_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V2 (2018-19)')
ax2.plot(dateM5_DM, Lat_V2_18_DM, ls='--', c='black', label ='Latitude')

UL5 = BrO_V2_18_DM + V2_18_MAD # find the upper limit
LL5 = BrO_V2_18_DM - V2_18_MAD # find the lower limit
ax.plot(date5_DM, UL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date5_DM, LL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date5_DM, UL5, LL5, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
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
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V2 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 6
ax=plt.subplot(236) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date6_DM, BrO_V3_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V3 (2018-19)')
ax2.plot(dateM6_DM, Lat_V3_18_DM, ls='--', c='black', label ='Latitude')

UL6 = BrO_V3_18_DM + V3_18_MAD # find the upper limit
LL6 = BrO_V3_18_DM - V3_18_MAD # find the lower limit
ax.plot(date6_DM, UL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date6_DM, LL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date6_DM, UL6, LL6, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
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
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')
