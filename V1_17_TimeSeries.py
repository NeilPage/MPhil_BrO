#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:21:15 2019

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

# BrO Data
V1_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Data.csv')

# NO2 Data
V1_NO2 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_Filtered_NO2.csv')

# O3 Data
V1_O3 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv')

# Met data
V1_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv') 
V1_Met.drop_duplicates(subset ="DateTime",keep = False, inplace = True) # remove duplicate rows

# Hg Data
V1_Hg = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_Lat_Long_17-18.csv')

#------------------------------------------------------------------------------
# FIX UP THE BrO DATASET

# Set the date
V1_BrO['DateTime'] = pd.to_datetime(V1_BrO['DateTime'])

# V1_17 Davis (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V1_BrO['Time'] >= start_time) & (V1_BrO['Time'] < end_time)
V1_BrO_MM = V1_BrO[Midday]

# Filter dataframe for when filter is less than 60%
V1_BrOF = (V1_BrO_MM['Filter'] < 0.6)
V1_BrOT = V1_BrO_MM[V1_BrOF]

#------------------------------------------------------------------------------
# Define the variables

# Latitude / Longitude
Lat = np.array(V1_Met['LATITUDE'])
Long = np.array(V1_Met['LONGITUDE'])

# Wind Direction
WD_s = np.array(V1_Met['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p = np.array(V1_Met['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

# Wind Speed
WS_s = np.array(V1_Met['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p = np.array(V1_Met['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS = (WS_s + WS_p)/2 # Average the wind speed for port and starboard

# Vector Mean Wind Direction
WD_vect = ((WD_s * WS_s) / (WS_s + WS_p)) + ((WD_p * WS_p) / (WS_s + WS_p)) # Calculate the vector mean wind direction

# BrO surface volume mixing ratio (VMR)
BrO = np.array(V1_BrOT['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

# NO2 surface volume mixing ratio (VMR)
NO2 = np.array(V1_NO2['surf_vmr(ppmv)']) * 1e3 # convert from ppmv to ppbv

# Solar Radiation (W/m2)
Sol_s = np.array(V1_Met['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p = np.array(V1_Met['RAD_SLR_PORT_WPERM2']) # port side solar radiation
Sol = np.array(V1_Met['Rad_Average'])

# Temperature (C)
Temp_s = np.array(V1_Met['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p = np.array(V1_Met['TEMP_AIR_PORT_DEGC']) # port side temperature
Temp = (Temp_s + Temp_p)/2 # Average the temperature for port and starboard

# Relative Humidity (RH)
RH_s = np.array(V1_Met['REL_HUMIDITY_STRBRD_PERCENT']) # starboard side relative humidity (%)
RH_p = np.array(V1_Met['REL_HUMIDITY_PORT_PERCENT']) # port side relative humidity (%)
RH = (RH_s + RH_p)/2 # Average the RH for port and starboard (%)

# Atmospheric pressure (hPa)
Pres = np.array(V1_Met['ATM_PRESS_HPA']) # Atmospheric Pressure (hPa)

# O3 (ppb)
O3 = np.array(V1_O3['O3_(ppb)']) # all O3 data

# Hg Data
Hg0 = np.array(V1_Hg['ng/m3']) # Hg0

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

# V1_BrO
dat = np.array(V1_BrOT['Date'])
tim = np.array(V1_BrOT['Time'])
dattim = dat+' '+tim

#CONVERT TO DATETIME FROM STRING
date=[]
for i in range(len(dattim)):
    date.append(datetime.strptime(dattim[i],'%d/%m/%Y %H:%M:%S'))

# V1_O3
dat2 = np.array(V1_O3['Date'])
tim2 = np.array(V1_O3['Time'])
dattim2 = dat2+' '+tim2

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S'))

# V1_Met
dat4 = np.array(V1_Met['Date'])
tim4 = np.array(V1_Met['Time'])
dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S'))

# V1_NO2
dat5 = np.array(V1_NO2['Date'])
tim5 = np.array(V1_NO2['Time'])
dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S'))

# V1_Hg0
dat6 = np.array(V1_Hg['Date'])
tim6 = np.array(V1_Hg['Time'])
dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    date6.append(datetime.strptime(dattim6[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(711) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# BrO & Hg
ax.plot(date, BrO, marker='+', c='blue', markersize = 3.0, linestyle='None')
#ax2.plot(date6, Hg0_V1_18, marker='+', c='brown', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,10,29),datetime(2017,12,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')

## Format y-axis 2
#ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax2.yaxis.label.set_color('brown')
#ax2.tick_params(axis='y', which='both', colors='brown')
#ax2.set_ylim(0,1.5)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
#ax2.set_ylabel('Hg$^0$\n(ng m$^-$$^3$)', fontsize=10)
#Plot the legend and title
plt.title('Time series for V1 (CAMMPCAN 2017-18)', fontsize=25, y=1.2)

#------------------------------
# Graph 2
ax=plt.subplot(712) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# NO2 & O3
ax.plot(date2, O3, marker='+', c='red', markersize = 3.0, linestyle='None')
#--------------------
ax2.plot(date4, WD_vect, marker='+', c='green', markersize = 3.0, linestyle='None') # WD Vect
#--------------------
#ax2.plot(date5, NO2_vmr_V1_18, marker='+', c='green', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,10,29),datetime(2017,12,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,35)

#--------------------
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(30))
#ax.set_ylim(0, 0.07)
ax2.yaxis.label.set_color('green')
ax2.tick_params(axis='y', which='both', colors='green')
#--------------------

# Format y-axis 2
#ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))
#ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)
#ax2.yaxis.label.set_color('green')
#ax2.tick_params(axis='y', which='both', colors='green')
#ax2.set_ylim(0,3)

# Plot the axis labels, legend and title
ax.set_ylabel('O$_3$\n(ppb)', fontsize=10)
#ax2.set_ylabel('NO2 VMR\n(ppbv)', fontsize=10)
#Plot the legend and title

#------------------------------
# Graph 3
ax=plt.subplot(713) # options graph 1 (vertical no, horizontal no, graph no)

# Relative humidity
plt.plot(date4, RH, marker='+', c='magenta', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,10,29),datetime(2017,12,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.tick_params(labelright=True)
ax.yaxis.set_ticks_position('both')
ax.yaxis.label.set_color('magenta')
ax.tick_params(axis='y', which='both', colors='magenta')

# Plot the axis labels, legend and title
plt.ylabel('Relative\nhumidity\n(%)', fontsize=10)

#------------------------------
# Graph 4
ax=plt.subplot(714) # options graph 1 (vertical no, horizontal no, graph no)

# Latitude
plt.plot(date4, Lat, marker='+', c='purple', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,10,29),datetime(2017,12,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.tick_params(labelright=True)
ax.yaxis.set_ticks_position('both')
ax.yaxis.label.set_color('purple')
ax.tick_params(axis='y', which='both', colors='purple')

# Plot the axis labels, legend and title
plt.ylabel('Latitude\n($^\circ$S)', fontsize=10)

#------------------------------
# Graph 5
ax=plt.subplot(715) # options graph 1 (vertical no, horizontal no, graph no)

# Solar radiation
plt.plot(date4, Sol, marker='+', c='orange', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,10,29),datetime(2017,12,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(250))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0, )
ax.tick_params(labelright=True)
ax.yaxis.set_ticks_position('both')
ax.yaxis.label.set_color('orange')
ax.tick_params(axis='y', which='both', colors='orange')

# Plot the axis labels, legend and title
plt.ylabel('Solar\nradiation\n(W/m$^2$)', fontsize=10)

#------------------------------
# Graph 6
ax=plt.subplot(716) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Temperature and Pressure
ax.plot(date4, Temp, marker='+', c='black', markersize = 3.0, linestyle='None') # Temperature
ax2.plot(date4, Pres, marker='+', c='deepskyblue', markersize = 3.0, linestyle='None') # Atmospheric Pressure

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,10,29),datetime(2017,12,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x', pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('black')
ax.tick_params(axis='y', which='both', colors='black')
ax.set_ylim(-16,21)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.yaxis.label.set_color('deepskyblue')
ax2.tick_params(axis='y', which='both', colors='deepskyblue')
ax2.set_ylim(935,1025)

# Plot the axis labels, legend and title
ax.set_ylabel('Temperature\n($^\circ$C)', fontsize=10)
ax2.set_ylabel('Atmospheric\nPressure\n(hPa)', fontsize=10)

#------------------------------
# Graph 7
ax=plt.subplot(717) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Wind Direction and Wind Speed
a = ax.plot(date4, WD_vect, marker='+', c='green', markersize = 3.0, linestyle='None') # Wind Direction
b = ax2.plot(date4, WS, marker='+', c='cyan', markersize = 3.0, linestyle='None') # Wind Speed

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,10,29),datetime(2017,12,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(30))
#ax.set_ylim(0, 0.07)
ax.yaxis.label.set_color('green')
ax.tick_params(axis='y', which='both', colors='green')

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('cyan')
ax2.tick_params(axis='y', which='both', colors='cyan')

# Plot the axis labels, legend and title
ax.set_ylabel('Wind\nDirection\n($^\circ$S)', fontsize=10)
ax2.set_ylabel('Wind\nSpeed\n(m/s)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
plt.subplots_adjust(left=0.2,right=0.9)