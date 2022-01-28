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
#plt.subplots_adjust(hspace=0.5)

ax=fig.add_subplot(111) 

# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

# Graph 1
ax1=fig.add_subplot(421) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
#plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
#plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
#plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
#plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
#plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
#plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax1.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax1.xaxis.set_minor_formatter(xminor_formatter)
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
#ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax1.tick_params(pad=20)
#ax1.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax1.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax1.set_yscale('log')
#ax1.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
#plt.xlabel('01/11/2018', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 2
ax2=fig.add_subplot(422) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
#plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
#plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
#plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
#plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
#plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
#plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax2.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax2.xaxis.set_minor_formatter(xminor_formatter)
ax2.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
#ax2.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax2.tick_params(pad=20)
#ax2.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax2.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax2.set_yscale('log')
#ax2.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
#plt.xlabel('01/11/2018', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 3
ax3=fig.add_subplot(423) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
#plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
#plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
#plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
#plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
#plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
#plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax3.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax3.xaxis.set_minor_formatter(xminor_formatter)
ax3.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
#ax3.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax3.tick_params(pad=20)
#ax3.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax3.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax3.set_yscale('log')
#ax3.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
#plt.xlabel('01/11/2018', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 4
ax4=fig.add_subplot(424) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
#plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
#plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
#plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
#plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
#plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
#plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax4.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax4.xaxis.set_minor_formatter(xminor_formatter)
ax4.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
#ax4.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax4.tick_params(pad=20)
#ax4.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax4.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax4.set_yscale('log')
#ax4.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
#plt.xlabel('01/11/2018', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 5
ax5=fig.add_subplot(425) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
#plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
#plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
#plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
#plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
#plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
#plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax5.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax5.xaxis.set_minor_formatter(xminor_formatter)
ax5.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
#ax5.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax5.tick_params(pad=20)
#ax5.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax5.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax5.set_yscale('log')
#ax5.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
#plt.xlabel('01/11/2018', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 6
ax6=fig.add_subplot(426) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
#plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
#plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
#plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
#plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
#plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
#plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax6.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax6.xaxis.set_minor_formatter(xminor_formatter)
ax6.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # set the interval between dispalyed dates
#ax6.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
ax6.tick_params(pad=20)
#ax6.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax6.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax6.set_yscale('log')
#ax6.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
#plt.xlabel('01/11/2018', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 7
ax7=fig.add_subplot(427) # options graph 1 (vertical no, horizontal no, graph no)

# BrO Retrievals
# Plot the BrO retrievals
#plt.plot(DateM3, BrOM3, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-3 deg") #DegM3
#plt.plot(DateM2, BrOM2, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-2 deg") #DegM2
#plt.plot(DateM1, BrOM1, marker='o', markerfacecolor='none', color='red', linestyle='none', label="-1 deg") #DegM1
#plt.plot(Date0, BrO0, marker='o', markerfacecolor='none', color='blue', linestyle='none', label="0 deg") #Deg0
#plt.plot(Date1, BrO1, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="1 deg") #Deg1
#plt.plot(Date2, BrO2, marker='o', markerfacecolor='none', color='orange', linestyle='none', label="2 deg") #Deg2
#plt.plot(Date3, BrO3, marker='o', markerfacecolor='none', color='green', linestyle='none', label="3 deg") #Deg3
#plt.plot(Date4, BrO4, marker='o', markerfacecolor='none', color='red', linestyle='none', label="4 deg") #Deg4
#plt.plot(Date5, BrO5, marker='o', markerfacecolor='none', color='red', linestyle='none', label="5 deg") #Deg5
#plt.plot(Date10, BrO10, marker='o', markerfacecolor='none', color='purple', linestyle='none', label="10 deg") #Deg10
#plt.plot(Date20, BrO20, marker='o', markerfacecolor='none', color='maroon', linestyle='none', label="20 deg") #Deg20
plt.plot(Date40, BrO40, marker='o', markerfacecolor='none', color='pink', linestyle='none', label="40 deg") #Deg40
#plt.plot(Date90, BrO90, marker='o', markerfacecolor='none', color='red', linestyle='none', label="90 deg") #Deg90

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax7.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
#ax7.xaxis.set_minor_formatter(xminor_formatter)
ax7.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
#ax7.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax7.tick_params(pad=20)
#ax7.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax7.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax7.set_yscale('log')
#ax7.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
ax7.set_xlabel('Hour', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
#ax7.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Graph 8
ax8=fig.add_subplot(428) # options graph 1 (vertical no, horizontal no, graph no)

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

plt.xlim(datetime(2018,11,20,20,30,01),datetime(2018,11,22,12,59,59)) # set the date limits
#plt.xlim(datetime(2018,11,20,20,00,01),datetime(2018,11,22,12,59,59)) # set the date limits

#plt.xticks(rotation=35)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax8.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
#ax8.xaxis.set_minor_formatter(xminor_formatter)
ax8.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
#ax8.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
ax8.tick_params(pad=20)
#ax8.xaxis.set_ticks_position(pad=20)

#SETTINGS FOR STANDARD PLOT
ax8.set_ylim(-0.2e14,3.0e14)

#SETTINGS FOR LOG PLOT
#ax8.set_yscale('log')
#ax8.set_ylim(0.8e13,0.3e16)

# Plot the axis labels, legend and title
#plt.ylabel('dSCD (molec/cm$^2$)', fontsize=15)
ax8.set_xlabel('Hour', fontsize=15)
#plt.title("V3 dSCD BrO (336-357)", fontsize=20)
ax8.legend(bbox_to_anchor=(1.2, 0.9), loc='best', borderaxespad=0., ncol=1)

# Set common labels
ax.set_title("V2 dSCD BrO (336-357)", fontsize=25, y=1.05)
ax.set_xlabel('21/11/2018 to 22/11/2018', fontsize=20, labelpad=40)
ax.set_ylabel('dSCD (molec/cm$^2$)', fontsize=20, labelpad=25)