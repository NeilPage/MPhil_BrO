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
V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V1/V1_BrO_QAQC.csv')
V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V2/V2_BrO_QAQC.csv')
V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V3/V3_BrO_QAQC.csv')

# CAMMPCAN 2018-19
V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V1/V1_BrO_QAQC.csv')
V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V2/V2_BrO_QAQC.csv')
V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V3/V3_BrO_QAQC.csv')

#------------------------------------------------------------------------------
# Define the variables

# CAMMPCAN (2017-18)
BrO_V1_17 = np.array(V1_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_V2_17 = np.array(V2_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_V3_17 = np.array(V3_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

# CAMMPCAN (2018-19)
BrO_V1_18 = np.array(V1_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_V2_18 = np.array(V2_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_V3_18 = np.array(V3_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

#------------------------------------------------------------------------------
# SET THE DATE AND TIME
#------------------------------------
# V1_17
dattim1 = np.array(V1_17['DateTime'])
#tim1 = np.array(V1_BrO['Time'])
#dattim1 = dat1+' '+tim1

#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    date1.append(datetime.strptime(dattim1[i],'%Y/%m/%d %H:%M:%S'))
#------------------------------------    
# V2_17
dattim2 = np.array(V2_17['DateTime'])
#tim2 = np.array(V2_BrO['Time'])
#dattim2 = dat+2' '+tim2

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%Y/%m/%d %H:%M:%S'))
#------------------------------------
# V3_17
dattim3 = np.array(V3_17['DateTime'])
#tim3 = np.array(V3_BrO['Time'])
#dattim3 = dat3+' '+tim3

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%Y/%m/%d %H:%M:%S'))
#------------------------------------
# V1_18
dattim4 = np.array(V1_18['DateTime'])
#tim4 = np.array(V1_BrO['Time'])
#dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    date4.append(datetime.strptime(dattim4[i],'%Y/%m/%d %H:%M:%S'))
#------------------------------------
# V2_18
dattim5 = np.array(V2_18['DateTime'])
#tim5 = np.array(V2_BrO['Time'])
#dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%Y/%m/%d %H:%M:%S'))
#------------------------------------
# V3_18
dattim6 = np.array(V3_18['DateTime'])
#tim6 = np.array(V3_BrO['Time'])
#dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    date6.append(datetime.strptime(dattim6[i],'%Y/%m/%d %H:%M:%S'))

#------------------------------------------------------------------------------
# CALCULATE THE BRO DAILY AVERAGE (MEAN)

# Function to calculate the daily mean
def dailyM(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('D').mean()
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

#------------------------------------------------------------------------------
# CALCULATE THE STANDARD DEVIATION FOR THE BRO DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def dailySTD(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('D').std()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Standard Deviations
BrO_V1_17_STD, date1_STD=dailySTD(BrO_V1_17[:],date1) # V1_17
BrO_V2_17_STD, date2_STD=dailySTD(BrO_V2_17[:],date2) # V2_17
BrO_V3_17_STD, date3_STD=dailySTD(BrO_V3_17[:],date3) # V3_17
BrO_V1_18_STD, date4_STDM=dailySTD(BrO_V1_18[:],date4) # V1_18
BrO_V2_18_STD, date5_STD=dailySTD(BrO_V2_18[:],date5) # V2_18
BrO_V3_18_STD, date6_STD=dailySTD(BrO_V3_18[:],date6) # V3_18

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(231) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(date1_DM, BrO_V1_17_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')
UL1 = BrO_V1_17_DM + BrO_V1_17_STD # find the upper limit
LL1 = BrO_V1_17_DM - BrO_V1_17_STD # find the lower limit
ax.plot(date1_DM, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date1_DM, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date1_DM, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# Format the axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)
#ax.tick_params(axis='x',pad=15)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 2
ax=plt.subplot(232) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(date2_DM, BrO_V2_17_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V2 (2017-18)')
UL2 = BrO_V2_17_DM + BrO_V2_17_STD # find the upper limit
LL2 = BrO_V2_17_DM - BrO_V2_17_STD # find the lower limit
ax.plot(date2_DM, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date2_DM, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date2_DM, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format the axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('BrO Daily Averages for CAMMPCAN 2017-18 and 2018-19 Voyages', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 3
ax=plt.subplot(233) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(date3_DM, BrO_V3_17_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V3 (2017-18)')
UL3 = BrO_V3_17_DM + BrO_V3_17_STD # find the upper limit
LL3 = BrO_V3_17_DM - BrO_V3_17_STD # find the lower limit
ax.plot(date3_DM, UL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date3_DM, LL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date3_DM, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format the axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 4
ax=plt.subplot(234) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(date4_DM, BrO_V1_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2018-19)')
UL4 = BrO_V1_18_DM + BrO_V1_18_STD # find the upper limit
LL4 = BrO_V1_18_DM - BrO_V1_18_STD # find the lower limit
ax.plot(date4_DM, UL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date4_DM, LL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date4_DM, UL4, LL4, facecolor='blue', alpha=0.3) # fill the distribution

# Format the axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 5
ax=plt.subplot(235) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(date5_DM, BrO_V2_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V2 (2018-19)')
UL5 = BrO_V2_18_DM + BrO_V2_18_STD # find the upper limit
LL5 = BrO_V2_18_DM - BrO_V2_18_STD # find the lower limit
ax.plot(date5_DM, UL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date5_DM, LL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date5_DM, UL5, LL5, facecolor='blue', alpha=0.3) # fill the distribution

# Format the axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V2 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 6
ax=plt.subplot(236) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
ax.plot(date6_DM, BrO_V3_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V3 (2018-19)')
UL6 = BrO_V3_18_DM + BrO_V3_18_STD # find the upper limit
LL6 = BrO_V3_18_DM - BrO_V3_18_STD # find the lower limit
ax.plot(date6_DM, UL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date6_DM, LL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date6_DM, UL6, LL6, facecolor='blue', alpha=0.3) # fill the distribution

# Format the axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')
