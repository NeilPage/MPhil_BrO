#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:21:15 2019

@author: ncp532
"""

# Date and Time handling package
from datetime import datetime	# functions to handle date and time

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# BrO Data
V3_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII_F.csv')

# NO2 Data
#V3_NO2 = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_NO2_QAQC.csv')

# O3 Data
V3_O3 = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv')

# Met data
V3_Met = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/201213001.csv') #SIPEXII_underway_60.csv') 

# Hg Data
V3_Hg = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_Lat_Long.csv')

#------------------------------------------------------------------------------
# FIX UP THE BrO DATASET

# Set the date
V3_BrO['DateTime'] = pd.to_datetime(V3_BrO['DateTime'])

# Filter the datasets for midday hours only
# SIPEXII (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V3_BrO['Time'] >= start_time) & (V3_BrO['Time'] < end_time)
V3_BrO_MM = V3_BrO[Midday]

# Filter dataframe for when filter is less than 60%
V3_BrOF = (V3_BrO_MM['Filter'] < 0.6)
V3_BrO = V3_BrO_MM[V3_BrOF]

#------------------------------------------------------------------------------
# RESAMPLE DATASETS TOO 1 MIN RESOLUTION

# BrO Data  
V3_BrO['DateTime'] = pd.to_datetime(V3_BrO['DateTime'], format='%d/%m/%Y %H:%M:%S')
V3_BrO = V3_BrO.set_index('DateTime')
V3_BrO = V3_BrO.resample('1T').bfill()

# NO2 Data  
#V3_NO2['DateTime'] = pd.to_datetime(V3_NO2['DateTime'], format='%d/%m/%Y %H:%M:%S')
#V3_NO2 = V3_NO2.set_index('DateTime')
#V3_NO2 = V3_NO2.resample('1T').bfill()

# O3 Data  
V3_O3['DateTime'] = pd.to_datetime(V3_O3['DateTime'], format='%d/%m/%Y %H:%M:%S')
V3_O3 = V3_O3.set_index('DateTime')

# Met Data  
V3_Met['DateTime'] = pd.to_datetime(V3_Met['DateTime'], format='%d/%m/%Y %H:%M:%S')
V3_Met = V3_Met.set_index('DateTime')

#------------------------------------------------------------------------------
# Add the Vector Mean Wind Direction to the Met data

# Latitude / Longitude
Lat_V1_18 = np.array(V3_Met['LATITUDE'])
Long_V1_18 = np.array(V3_Met['LONGITUDE'])

# Wind Direction
WD_s1_18 = np.array(V3_Met['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p1_18 = np.array(V3_Met['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

# Wind Speed
WS_s1_18 = np.array(V3_Met['WND_SPD_STRBD_CORR_KNOT']) # starboard side wind speed (correlated)
WS_s1_18 = WS_s1_18 * 0.514444444 # Convert from knots to m/s
WS_p1_18 = np.array(V3_Met['WND_SPD_PORT_CORR_KNOT']) # port side wind speed (correlated)
WS_p1_18 = WS_p1_18 * 0.514444444 # Convert from knots to m/s
V3_Met['WS_1_18'] = ((WS_s1_18 + WS_p1_18)/2) # Average the wind speed for port and starboard
WS_1_18 = np.array(V3_Met['WS_1_18'])

V3_Met['WD_vect'] = ((WD_s1_18 * WS_s1_18) / (WS_s1_18 + WS_p1_18)) + ((WD_p1_18 * WS_p1_18) / (WS_s1_18 + WS_p1_18))
WD_vect1_18 = np.array(V3_Met['WD_vect'])

#------------------------------------------------------------------------------
# Filter the datasets for the ships exhaust
# (remove data when wind direction is 60-190 degrees and wind speed below 5 knots)

# Step 1 (Merge datasets to filter with the Met data)
D3 = pd.merge(left=V3_BrO,right=V3_Met, how='left', left_index=True, right_index=True)
#D4 = pd.merge(left=V3_NO2,right=V3_Met, how='left', left_index=True, right_index=True)
D5 = pd.merge(left=V3_O3,right=V3_Met, how='left', left_index=True, right_index=True)

# Step 2 (Remove data when wind direction is between 60-190 degrees)
# When less than 65S
# BrO (remove data when wind direction is 60-190 degrees)
BrO_60 = D3['WD_vect'] <=60 
D6 = D3[BrO_60]
BrO_190 = D3['WD_vect'] >=190 
D7 = D3[BrO_190]
DBrO = pd.concat([D6,D7],axis=0)
# NO2 (remove data when wind direction is 60-190 degrees)
#NO2_60 = D4['WD_vect'] <=60 
#D8 = D4[NO2_60]
#NO2_190 = D4['WD_vect'] >=190 
#D9 = D4[NO2_190]
#DNO2 = pd.concat([D8,D9],axis=0)
# O3 (remove data when wind direction is 90-270 degrees)
O3_90 = D5['WD_vect'] <=90 # <=90
D10 = D5[O3_90]
O3_270 = D5['WD_vect'] >=270 # >=270 
D11 = D5[O3_270]
DO3 = pd.concat([D10,D11],axis=0)

# Step 3 (Remove data when wind speed is below 5 knots (or 2.57222222 m/s))
BrO_5knot = DBrO['WD_vect'] >=2.57222222
DBrO = DBrO[BrO_5knot]

#NO2_5knot = DNO2['WD_vect'] >=2.57222222 
#DNO2 = DNO2[NO2_5knot]

O3_5knot = DO3['WD_vect'] >=2.57222222
DO3 = DO3[O3_5knot]

#------------------------------------------------------------------------------
# Define the variables

# Latitude / Longitude
Lat_V1_18 = np.array(V3_Met['LATITUDE'])
Long_V1_18 = np.array(V3_Met['LONGITUDE'])

# BrO surface volume mixing ratio (VMR)
BrO_vmr_V1_18 = np.array(DBrO['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_2 = np.array(V3_BrO['surf_vmr(ppmv)']) * 1e6

# NO2 surface volume mixing ratio (VMR)
#NO2_vmr_V1_18 = np.array(DNO2['surf_vmr(ppmv)']) * 1e3 # convert from ppmv to ppbv
#NO2_2 = np.array(V3_NO2['surf_vmr(ppmv)']) * 1e3

# Solar Radiation (W/m2)
Sol_s1_18 = np.array(V3_Met['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p1_18 = np.array(V3_Met['RAD_SLR_PORT_WPERM2']) # port side solar radiation
Sol_V1_18 = (Sol_s1_18 + Sol_p1_18)/2 # Average the Solar Radiation for port and starboard

# Temperature (C)
Temp_s1_18 = np.array(V3_Met['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p1_18 = np.array(V3_Met['TEMP_AIR_PORT_DEGC']) # port side temperature
Temp_V1_18 = (Temp_s1_18 + Temp_p1_18)/2 # Average the temperature for port and starboard

# Relative Humidity (RH)
RH_s1_18 = np.array(V3_Met['REL_HUMIDITY_STRBRD_PERCENT']) # starboard side relative humidity (%)
RH_p1_18 = np.array(V3_Met['REL_HUMIDITY_PORT_PERCENT']) # port side relative humidity (%)
RH_V1_18 = (RH_s1_18 + RH_p1_18)/2 # Average the RH for port and starboard (%)

# Atmospheric pressure (hPa)
Pres_s1_18 = np.array(V3_Met['ATM_PRESS_HPA']) # Atmospheric Pressure (hPa)

# O3 (ppb)
O3_V1_18 = np.array(DO3['O3_(ppb)']) # all O3 data
O3_2 = np.array(V3_O3['O3_(ppb)']) # all O3 data

# Hg Data
Hg0_V1_18 = np.array(V3_Hg['ng/m3']) # Hg0

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

# V1_BrO
dat = np.array(DBrO['Date_x'])
tim = np.array(DBrO['Time_x'])
dattim = dat+' '+tim

#CONVERT TO DATETIME FROM STRING
date=[]
for i in range(len(dattim)):
    date.append(datetime.strptime(dattim[i],'%d/%m/%Y %H:%M:%S'))

# V1_O3
dat2 = np.array(DO3['Date_x'])
tim2 = np.array(DO3['Time_x'])
dattim2 = dat2+' '+tim2

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S'))

# V1_Met
dat3 = np.array(V3_Met['Date'])
tim3 = np.array(V3_Met['Time'])
dattim3 = dat3+' '+tim3

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S'))

# V1_NO2
#dat4 = np.array(DNO2['Date_x'])
#tim4 = np.array(DNO2['Time_x'])
#dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
#date4=[]
#for i in range(len(dattim4)):
#    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S'))

# V1_Hg0
dat5 = np.array(V3_Hg['Date'])
tim5 = np.array(V3_Hg['Time'])
dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S'))

# BrO_2
dat6 = np.array(V3_BrO['Date'])
tim6 = np.array(V3_BrO['Time'])
dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    date6.append(datetime.strptime(dattim6[i],'%d/%m/%Y %H:%M:%S'))

# NO2_2
#dat7 = np.array(V3_NO2['Date'])
#tim7 = np.array(V3_NO2['Time'])
#dattim7 = dat7+' '+tim7

#CONVERT TO DATETIME FROM STRING
#date7=[]
#for i in range(len(dattim7)):
#    date7.append(datetime.strptime(dattim7[i],'%d/%m/%Y %H:%M:%S'))
    
# O3_2
dat8 = np.array(V3_O3['Date'])
tim8 = np.array(V3_O3['Time'])
dattim8 = dat8+' '+tim8

#CONVERT TO DATETIME FROM STRING
date8=[]
for i in range(len(dattim8)):
    date8.append(datetime.strptime(dattim8[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(711) # options graph 1 (vertical no, horizontal no, graph no)
#ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.08))

# BrO & Hg
ax.plot(date, BrO_vmr_V1_18, marker='+', c='blue', markersize = 3.0, linestyle='None')
#ax.plot(date6, BrO_2, marker='+', c='blue', markersize = 3.0, linestyle='None')
#ax2.plot(date5, Hg0_V1_18, marker='+', c='brown', markersize = 3.0, linestyle='None')
#ax3.plot(date5, RM_V1_18, marker='+', c='black', markersize = 3.0, linestyle='None')
#ax3.fill_between(date5, RM_V1_18 - RM_StDev, RM_V1_18 - RM_StDev, color='black', alpha=0.4)

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(3))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)
ax.tick_params(labelright=True)
ax.yaxis.set_ticks_position('both')
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')

# Format y-axis 2
#ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax2.yaxis.label.set_color('brown')
#ax2.tick_params(axis='y', which='both', colors='brown')
#ax2.set_ylim(0,1.5)
#
## Format y-axis 3
#ax3.yaxis.set_major_locator(ticker.MultipleLocator(25))
#ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax3.yaxis.label.set_color('black')
#ax3.tick_params(axis='y', which='both', colors='black')
#ax3.set_ylim(0,100)
#
## Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
#ax2.set_ylabel('Hg$^0$\n(ng m$^-$$^3$)', fontsize=10)
#ax3.set_ylabel('RM\n(pg m$^-$$^3$)', fontsize=10)
#Plot the legend and title
plt.title('Time series for SIPEXII (2012)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#------------------------------
# Graph 2
ax=plt.subplot(712) # options graph 1 (vertical no, horizontal no, graph no)
#ax2 = ax.twinx()

# NO2 & O3
ax.plot(date2, O3_V1_18, marker='+', c='red', markersize = 3.0, linestyle='None')
#ax.plot(date8, O3_2, marker='+', c='red', markersize = 3.0, linestyle='None')
#ax.plot(date2, O3_1000, marker='+', c='red', markersize = 3.0, linestyle='None')
#ax.plot(date2, O3_100, marker='+', c='red', markersize = 3.0, linestyle='None')
#ax.plot(date2, O3_65, marker='+', c='red', markersize = 3.0, linestyle='None')
#ax2.plot(date4, NO2_vmr_V1_18, marker='+', c='green', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.tick_params(labelright=True)
ax.yaxis.set_ticks_position('both')
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,35)

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
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

##------------------------------
## Graph 3
#ax=plt.subplot(813) # options graph 1 (vertical no, horizontal no, graph no)
#
## CO MIXING RATIO ppmv
##ax.plot(date2, CO_V1_18, marker='+', c='grey', markersize = 3.0, linestyle='None')
##ax.plot(date2, CO_1000, marker='+', c='grey', markersize = 3.0, linestyle='None')
##ax.plot(date2, CO_100, marker='+', c='grey', markersize = 3.0, linestyle='None')
##ax.plot(date2, CO_65, marker='+', c='grey', markersize = 3.0, linestyle='None')
#ax.plot(date4, NO2_vmr_V1_18, marker='+', c='green', markersize = 3.0, linestyle='None')
##ax.plot(date7, NO2_2, marker='+', c='green', markersize = 3.0, linestyle='None')
#
## Format x-axis
##plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
#plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
#xmajor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_major_formatter(xmajor_formatter)
##xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
##ax.xaxis.set_minor_formatter(xminor_formatter)
#ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
##ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#
## Format y-axis 1
##ax.set_yscale('log')
##ax.set_ylim(4e-2,5e1)
##ax.set_ylim(48,68) # CO
##ax.yaxis.set_major_locator(ticker.MultipleLocator(5)) # CO
##ax.yaxis.set_minor_locator(ticker.MultipleLocator(1)) # CO
#ax.yaxis.set_major_locator(ticker.MultipleLocator(1)) # NO2
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1)) # NO2
##ax.set_yticks([1e-1,1e1])
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
##ax.yaxis.label.set_color('grey') # CO
##ax.tick_params(axis='y', which='both', colors='grey') # CO
#ax.yaxis.label.set_color('green') # NO2
#ax.tick_params(axis='y', which='both', colors='green') # NO2
##ax2.set_ylim(0,3)
## Plot the axis labels, legend and title
##ax.set_ylabel('CO\n(ppbv)', fontsize=10)
#ax.set_ylabel('NO$_2$ VMR\n(ppbv)', fontsize=10)
##Plot the legend and title
##plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#------------------------------
# Graph 4
ax=plt.subplot(713) # options graph 1 (vertical no, horizontal no, graph no0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

# Relative humidity
plt.plot(date3, RH_V1_18, marker='+', c='magenta', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
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
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#------------------------------
# Graph 5
ax=plt.subplot(714) # options graph 1 (vertical no, horizontal no, graph no)

# Latitude
plt.plot(date3, Lat_V1_18, marker='+', c='purple', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
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
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#------------------------------
# Graph 6
ax=plt.subplot(715) # options graph 1 (vertical no, horizontal no, graph no)

# Solar radiation
plt.plot(date3, Sol_V1_18, marker='+', c='orange', markersize = 3.0, linestyle='None')

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
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
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#------------------------------
# Graph 7
ax=plt.subplot(716) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Temperature and Pressure
ax.plot(date3, Temp_V1_18, marker='+', c='black', markersize = 3.0, linestyle='None') # Temperature
ax2.plot(date3, Pres_s1_18, marker='+', c='deepskyblue', markersize = 3.0, linestyle='None') # Atmospheric Pressure

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
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
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#------------------------------
# Graph 8
ax=plt.subplot(717) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Wind Direction and Wind Speed
a = ax.plot(date3, WD_vect1_18, marker='+', c='green', markersize = 3.0, linestyle='None') # Wind Direction
b = ax2.plot(date3, WS_1_18, marker='+', c='cyan', markersize = 3.0, linestyle='None') # Wind Speed

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2012,9,13),datetime(2012,11,17)) # all dates
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
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.subplots_adjust(left=0.2,right=0.9)