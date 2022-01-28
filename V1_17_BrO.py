#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:13:46 2019

@author: ncp532
"""
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
V1_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_F.csv')

# NO2 Data
V1_NO2 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V1/V1_NO2_QAQC.csv')

# O3 Data
#V1_O3 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv') 
V1_O3 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/ARM_O3_CO_N2O.csv')

# Met data
V1_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv') 

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
V1_BrOF = (V1_BrO['Filter'] < 0.6)
V1_BrOT = V1_BrO[V1_BrOF]

#------------------------------------------------------------------------------
# Define the variables

# CAMMPCAN (2018-19)
# V1----------------
# Latitude / Longitude
Lat_V1_18 = np.array(V1_Met['LATITUDE'])
Long_V1_18 = np.array(V1_Met['LONGITUDE'])
# Wind Direction
WD_s1_18 = np.array(V1_Met['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p1_18 = np.array(V1_Met['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)
# Wind Speed
WS_s1_18 = np.array(V1_Met['WND_SPD_STRBD_CORR_KNOT']) # starboard side wind speed (correlated)
WS_s1_18 = WS_s1_18 * 0.514444444 # Convert from knots to m/s
WS_p1_18 = np.array(V1_Met['WND_SPD_PORT_CORR_KNOT']) # port side wind speed (correlated)
WS_p1_18 = WS_p1_18 * 0.514444444 # Convert from knots to m/s
WS_1_18 = (WS_s1_18 + WS_p1_18)/2 # Average the wind speed for port and starboard
# Vector Mean Wind Direction
WD_vect1_18 = ((WD_s1_18 * WS_s1_18) / (WS_s1_18 + WS_p1_18)) + ((WD_p1_18 * WS_p1_18) / (WS_s1_18 + WS_p1_18)) # Calculate the vector mean wind direction
# BrO surface volume mixing ratio (VMR)
BrO_vmr_V1_18 = np.array(V1_BrOT['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

# NO2 surface volume mixing ratio (VMR)
NO2_vmr_V1_18 = np.array(V1_NO2['surf_vmr(ppmv)'])
NO2_vmr_V1_18 = NO2_vmr_V1_18 * 1e3 # convert from ppmv to ppbv
# BrO vertical column density (VCD)
NO2_vcd_V1_18 = np.array(V1_NO2['NO2_VCD(molec/cm^2)'])
# Solar Radiation (W/m2)
Sol_s1_18 = np.array(V1_Met['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p1_18 = np.array(V1_Met['RAD_SLR_PORT_WPERM2']) # port side solar radiation
Sol_V1_18 = np.array(V1_Met['Rad_Average'])
# Temperature (C)
Temp_s1_18 = np.array(V1_Met['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p1_18 = np.array(V1_Met['TEMP_AIR_PORT_DEGC']) # port side temperature
Temp_V1_18 = (Temp_s1_18 + Temp_p1_18)/2 # Average the temperature for port and starboard
# Relative Humidity (RH)
RH_s1_18 = np.array(V1_Met['REL_HUMIDITY_STRBRD_PERCENT']) # starboard side relative humidity (%)
RH_p1_18 = np.array(V1_Met['REL_HUMIDITY_PORT_PERCENT']) # port side relative humidity (%)
RH_V1_18 = (RH_s1_18 + RH_p1_18)/2 # Average the RH for port and starboard (%)
# Atmospheric pressure (hPa)
Pres_s1_18 = np.array(V1_Met['ATM_PRESS_HPA']) # Atmospheric Pressure (hPa)
# O3 (ppb)
O3_V1_18 = np.array(V1_O3['O3_(ppb)']) # all O3 data
O3_1000 = np.array(V1_O3['O3_1000']) # Filter O3 for when CO is greater than 1000 ppb
O3_100 = np.array(V1_O3['O3_100']) # Filter O3 for when CO is greater than 100 ppb
O3_65 = np.array(V1_O3['O3_65']) # Filter O3 for when CO is greater than 65 ppb
# CO ()
CO_V1_18 = np.array(V1_O3['CO_Dry']) # CO ()
CO_1000 = np.array(V1_O3['CO_1000']) # Filter CO for when CO is greater than 1000 ppb
CO_100 = np.array(V1_O3['CO_100']) # Filter CO for when CO is greater than 100 ppb
CO_65 = np.array(V1_O3['CO_65']) # Filter CO for when CO is greater than 65 ppb

# Hg Data
Hg0_V1_18 = np.array(V1_Hg['ng/m3']) # Hg0
RM_V1_18 = np.array(V1_Hg['RM_pg/m3']) # RM
RM_StDev = np.array(V1_Hg['RM_StDev']) # RM StDev

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
dat3 = np.array(V1_Met['Date'])
tim3 = np.array(V1_Met['Time'])
dattim3 = dat3+' '+tim3

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S'))

# V1_NO2
dat4 = np.array(V1_NO2['Date'])
tim4 = np.array(V1_NO2['Time'])
dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S'))

# V1_Hg0
dat5 = np.array(V1_Hg['Date'])
tim5 = np.array(V1_Hg['Time'])
dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(111) # options graph 1 (vertical no, horizontal no, graph no)
#ax2 = ax.twinx()
#ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.08))

# BrO & Hg
ax.plot(date, BrO_vmr_V1_18, marker='+', c='blue', markersize = 5.0, linestyle='None')
#ax2.plot(date5, Hg0_V1_18, marker='+', c='brown', markersize = 3.0, linestyle='None')
#ax3.plot(date5, RM_V1_18, marker='+', c='black', markersize = 3.0, linestyle='None')
#ax3.fill_between(date5, RM_V1_18 - RM_StDev, RM_V1_18 - RM_StDev, color='black', alpha=0.4)

# Format x-axis
#plt.xlim(datetime(2017,11,13),datetime(2017,11,23)) # at Davis station
plt.xlim(datetime(2017,11,14),datetime(2017,11,22)) # all dates
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,10)

## Format y-axis 2
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

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR\n(pptv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#ax2.set_ylabel('Hg$^0$\n(ng m$^-$$^3$)', fontsize=10)
#ax3.set_ylabel('RM\n(pg m$^-$$^3$)', fontsize=10)
#Plot the legend and title
plt.title('BrO concentration for V1 2017 (14th - 22nd Nov 2017)', fontsize=25, y=1.2)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)