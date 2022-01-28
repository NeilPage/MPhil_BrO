#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:56:34 2019

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
import glob

# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# Define the datasets

# MAX-DOAS Retrievals

#V1 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/MAX-DOAS/2018-19-v1_newBrOsettings.csv') # V1 BrO Slant Columns
V2 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/MAX-DOAS/2018-19-v2_newBrOsettings.csv') # V2 BrO Slant Columns 
#V2 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/MAX-DOAS/2018-19-v3_newBrOsettings.csv') # V3 BrO Slant Columns
#V4 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/MAX-DOAS/2018-19-v4_newBrOsettings.csv') # V4 BrO Slant Columns

#------------------------------------------------------------------------------
# SET THE DATE AND TIME
V2_date = np.array(V2['Date']) # Date for V2
V2_time = np.array(V2['Time']) # Time for V2
V2_datetime = V2_date+' '+V2_time

#CONVERT TO DATETIME FROM STRING
date=[]
for i in range(len(V2_datetime)):
    date.append(datetime.strptime(V2_datetime[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------------------------------------------------
# Define the variables

V2_BrO = np.array(V2['336-357.SlErr(BrO)'])
Rounded_EA = np.array(V2['Rounded EA'])

# SORT THE DATA INTO DIFFERENT ELEV ANGLES
DegM3 = np.where([i == -3 for i in Rounded_EA])[0]
DegM2 = np.where([i == -2 for i in Rounded_EA])[0]
DegM1 = np.where([i == -1 for i in Rounded_EA])[0]
Deg0 = np.where([i == 0 for i in Rounded_EA])[0]
Deg1 = np.where([i == 1 for i in Rounded_EA])[0]
Deg2 = np.where([i == 2 for i in Rounded_EA])[0]
Deg3 = np.where([i == 3 for i in Rounded_EA])[0]
Deg4 = np.where([i == 4 for i in Rounded_EA])[0]
Deg5 = np.where([i == 5 for i in Rounded_EA])[0]
Deg10 = np.where([i == 10 for i in Rounded_EA])[0]
Deg20 = np.where([i == 20 for i in Rounded_EA])[0]
Deg40 = np.where([i == 40 for i in Rounded_EA])[0]
Deg90 = np.where([i == 90 for i in Rounded_EA])[0]

# DegM3
DateM3 = np.array([date[i] for i in DegM3])
BrOM3 = np.array([V2_BrO[i] for i in DegM3])

# DegM2
DateM2 = np.array([date[i] for i in DegM2])
BrOM2 = np.array([V2_BrO[i] for i in DegM2])

# DegM1
DateM1 = np.array([date[i] for i in DegM1])
BrOM1 = np.array([V2_BrO[i] for i in DegM1])

# Deg0
Date0 = np.array([date[i] for i in Deg0])
BrO0 = np.array([V2_BrO[i] for i in Deg0])

# Deg1
Date1 = np.array([date[i] for i in Deg1])
BrO1 = np.array([V2_BrO[i] for i in Deg1])

# Deg2
Date2 = np.array([date[i] for i in Deg2])
BrO2 = np.array([V2_BrO[i] for i in Deg2])

# Deg3
Date3 = np.array([date[i] for i in Deg3])
BrO3 = np.array([V2_BrO[i] for i in Deg3])

# Deg4
Date4 = np.array([date[i] for i in Deg4])
BrO4 = np.array([V2_BrO[i] for i in Deg4])

# Deg5
Date5 = np.array([date[i] for i in Deg5])
BrO5 = np.array([V2_BrO[i] for i in Deg5])

# Deg10
Date10 = np.array([date[i] for i in Deg10])
BrO10 = np.array([V2_BrO[i] for i in Deg10])

# Deg20
Date20 = np.array([date[i] for i in Deg20])
BrO20 = np.array([V2_BrO[i] for i in Deg20])

# Deg40
Date40 = np.array([date[i] for i in Deg40])
BrO40 = np.array([V2_BrO[i] for i in Deg40])

# Deg90
Date90 = np.array([date[i] for i in Deg90])
BrO90 = np.array([V2_BrO[i] for i in Deg90])
#------------------------------------------------------------------------------
# Plot the axis for each graph
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

#plt.xlim(datetime(2018,11,1),datetime(2018,11,2)) # set the date limits
#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax.tick_params(pad=20)
#ax.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax.set_ylim(-0.8e14,20e14)

# Plot the axis labels, legend and title
plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
plt.xlabel('Date', fontsize=15)
plt.title("V3 dSCD BrO (336-357)", fontsize=20)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 2
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

#plt.xlim(datetime(2018,11,1,00,00,00),datetime(2018,11,1,23,59,59)) # set the date limits
#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax.tick_params(pad=20)
#ax.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR LOG PLOT
ax.set_yscale('log')
ax.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
plt.xlabel('Date', fontsize=15)
plt.title("V3 dSCD BrO (336-357)", fontsize=20)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)