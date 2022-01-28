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
from scipy import stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# CAMMPCAN 2017-18
V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_17_Data.csv',header=0,encoding = 'unicode_escape')
O3_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv')
Hg_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_Lat_Long_17-18.csv')

V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_17_Data.csv',header=0,encoding = 'unicode_escape')
O3_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv')
Hg_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_Lat_Long_17-18.csv')

V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_17_Data.csv',header=0,encoding = 'unicode_escape')
O3_V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv')
Hg_V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_Lat_Long_17-18.csv')

# CAMMPCAN 2018-19
V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_18_Data.csv',header=0,encoding = 'unicode_escape')
O3_V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V1_O3_1min.csv')
Hg_V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_Lat_Long_18-19.csv')

V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_18_Data.csv',header=0,encoding = 'unicode_escape')
O3_V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V2_O3_1min.csv')
Hg_V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_Lat_Long_18-19.csv')

V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_18_Data.csv',header=0,encoding = 'unicode_escape')
O3_V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V3_O3_1min.csv')
Hg_V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_Lat_Long_18-19.csv')

# SIPEXII 2012
SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/SIPEXII_Data.csv',header=0,encoding = 'unicode_escape')
O3_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv')
Hg_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_Lat_Long.csv')

#------------------------------------------------------------------------------
# Set the date

V1_17['DateTime'] = pd.to_datetime(V1_17['DateTime']) # Davis timezone is UT+7
V2_17['DateTime'] = pd.to_datetime(V2_17['DateTime']) # Casey timezone is UT+8
V3_17['DateTime'] = pd.to_datetime(V3_17['DateTime']) # Mawson timezone is UT+5
V1_18['DateTime'] = pd.to_datetime(V1_18['DateTime']) # Davis timezone is UT+7
V2_18['DateTime'] = pd.to_datetime(V2_18['DateTime']) # Casey timezone is UT+8
V3_18['DateTime'] = pd.to_datetime(V3_18['DateTime']) # Mawson timezone is UT+5
SIPEXII['DateTime'] = pd.to_datetime(SIPEXII['DateTime']) # SIPEXII timezone is UT+5

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

#-----------------------------
# CAMMPCAN 2017-18
#-----------------------------
# V1_17 Davis (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V1_17['Time'] >= start_time) & (V1_17['Time'] < end_time)
V1_17_MM = V1_17[Midday]

# V2_17 Casey (08:00 to 16:00)
start_time = '08:00:00'
end_time = '16:00:00'
Midday = (V2_17['Time'] >= start_time) & (V2_17['Time'] < end_time)
V2_17_MM = V2_17[Midday]

# V3_17 Mawson (08:00 to 18:00)
start_time = '08:00:00'
end_time = '18:00:00'
Midday = (V3_17['Time'] >= start_time) & (V3_17['Time'] < end_time)
V3_17_MM = V3_17[Midday]

#-----------------------------
# CAMMPCAN 2018-19
#-----------------------------
# V1_18 Davis (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V1_18['Time'] >= start_time) & (V1_18['Time'] < end_time)
V1_18_MM = V1_18[Midday]

# V2_18 Casey (08:00 to 16:00)
start_time = '08:00:00'
end_time = '16:00:00'
Midday = (V2_18['Time'] >= start_time) & (V2_18['Time'] < end_time)
V2_18_MM = V2_18[Midday]

# V3_18 Mawson (08:00 to 18:00)
start_time = '08:00:00'
end_time = '18:00:00'
Midday = (V3_18['Time'] >= start_time) & (V3_18['Time'] < end_time)
V3_18_MM = V3_18[Midday]

#-----------------------------
# SIPEXII 2012
#-----------------------------
# SIPEXII (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (SIPEXII['Time'] >= start_time) & (SIPEXII['Time'] < end_time)
SIPEXII_MM = SIPEXII[Midday]

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

V1_17F = (V1_17_MM['Filter'] < 0.6)
V1_17T = V1_17_MM[V1_17F]

V2_17F = (V2_17_MM['Filter'] < 0.6)
V2_17T = V2_17_MM[V2_17F]

V3_17F = (V3_17_MM['Filter'] < 0.6)
V3_17T = V3_17_MM[V3_17F]

V1_18F = (V1_18_MM['Filter'] < 0.6)
V1_18T = V1_18_MM[V1_18F]

V2_18F = (V2_18_MM['Filter'] < 0.6)
V2_18T = V2_18_MM[V2_18F]

V3_18F = (V3_18_MM['Filter'] < 0.6)
V3_18T = V3_18_MM[V3_18F]

SIPEXIIF = (SIPEXII_MM['Filter'] < 0.6)
SIPEXIIT = SIPEXII_MM[SIPEXIIF]

#------------------------------------------------------------------------------
# Define the variables

# CAMMPCAN (2017-18)
BrO_V1_17 = np.array(V1_17T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V1_17 = np.array(V1_17T['LATITUDE'])
O3_V1_17a = np.array(V1_17T['O3_(ppb)'])
O3_V1_17b = np.array(O3_V1_17['O3_(ppb)'])
Hg0_V1_17 = np.array(Hg_V1_17['ng/m3'])

BrO_V2_17 = np.array(V2_17T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V2_17 = np.array(V2_17T['LATITUDE'])
O3_V2_17a = np.array(V2_17T['O3_(ppb)'])
O3_V2_17b = np.array(O3_V2_17['O3_(ppb)'])
Hg0_V2_17 = np.array(Hg_V2_17['ng/m3'])

BrO_V3_17 = np.array(V3_17T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V3_17 = np.array(V3_17T['LATITUDE'])
O3_V3_17a = np.array(V3_17T['O3_(ppb)'])
O3_V3_17b = np.array(O3_V3_17['O3_(ppb)'])
Hg0_V3_17 = np.array(Hg_V3_17['ng/m3'])

# CAMMPCAN (2018-19)
BrO_V1_18 = np.array(V1_18T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V1_18 = np.array(V1_18T['LATITUDE'])
O3_V1_18a = np.array(V1_18T['O3_(ppb)'])
O3_V1_18b = np.array(O3_V1_18['O3'])
Hg0_V1_18 = np.array(Hg_V1_18['ng/m3'])

BrO_V2_18 = np.array(V2_18T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V2_18 = np.array(V2_18T['LATITUDE'])
O3_V2_18a = np.array(V2_18T['O3_(ppb)'])
O3_V2_18b = np.array(O3_V2_18['O3'])
Hg0_V2_18 = np.array(Hg_V2_18['ng/m3'])

BrO_V3_18 = np.array(V3_18T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V3_18 = np.array(V3_18T['LATITUDE'])
O3_V3_18a = np.array(V3_18T['O3_(ppb)'])
O3_V3_18b = np.array(O3_V3_18['O3'])
Hg0_V3_18 = np.array(Hg_V3_18['ng/m3'])

# SIPEXII (2012)
BrO_SIPEXII = np.array(SIPEXIIT['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_SIPEXII = np.array(SIPEXIIT['LATITUDE'])
O3_SIPEXIIa = np.array(SIPEXIIT['O3_(ppb)'])
O3_SIPEXIIb = np.array(O3_SIPEXII['O3_(ppb)'])
Hg0_SIPEXII = np.array(Hg_SIPEXII['ng/m3'])

#------------------------------------------------------------------------------
# SET THE DATE AND TIME
#------------------------------------
# V1_17
dat1 = np.array(V1_17T['Date'])
tim1 = np.array(V1_17T['Time'])
dattim1 = dat1+' '+tim1

#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    date1.append(datetime.strptime(dattim1[i],'%d/%m/%Y %H:%M:%S')) # midday data    

# V1_17_O3
dattimO31 = np.array(O3_V1_17['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateO31=[]
for i in range(len(dattimO31)):
    dateO31.append(datetime.strptime(dattimO31[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=7))

# V1_17_Hg
dattimHg1 = np.array(Hg_V1_17['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateHg1=[]
for i in range(len(dattimHg1)):
    dateHg1.append(datetime.strptime(dattimHg1[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=7))

#------------------------------------    
# V2_17
dat2 = np.array(V2_17T['Date'])
tim2 = np.array(V2_17T['Time'])
dattim2 = dat2+' '+tim2

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V2_17_O3
dattimO32 = np.array(O3_V2_17['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateO32=[]
for i in range(len(dattimO32)):
    dateO32.append(datetime.strptime(dattimO32[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=8))
 
# V2_17_Hg
dattimHg2 = np.array(Hg_V2_17['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateHg2=[]
for i in range(len(dattimHg2)):
    dateHg2.append(datetime.strptime(dattimHg2[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=8))
    
#------------------------------------
# V3_17
dat3 = np.array(V3_17T['Date'])
tim3 = np.array(V3_17T['Time'])
dattim3 = dat3+' '+tim3

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V3_17_O3
dattimO33 = np.array(O3_V3_17['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateO33=[]
for i in range(len(dattimO33)):
    dateO33.append(datetime.strptime(dattimO33[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=5))

# V3_17_Hg
dattimHg3 = np.array(Hg_V3_17['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateHg3=[]
for i in range(len(dattimHg3)):
    dateHg3.append(datetime.strptime(dattimHg3[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=5))
    
#------------------------------------
# V1_18
dat4 = np.array(V1_18T['Date'])
tim4 = np.array(V1_18T['Time'])
dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V1_18_O3
dattimO34 = np.array(O3_V1_18['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateO34=[]
for i in range(len(dattimO34)):
    dateO34.append(datetime.strptime(dattimO34[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=7))

# V1_18_Hg
dattimHg4 = np.array(Hg_V1_18['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateHg4=[]
for i in range(len(dattimHg4)):
    dateHg4.append(datetime.strptime(dattimHg4[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=7))

#------------------------------------
# V2_18
dat5 = np.array(V2_18T['Date'])
tim5 = np.array(V2_18T['Time'])
dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V2_18_O3
dattimO35 = np.array(O3_V2_18['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateO35=[]
for i in range(len(dattimO35)):
    dateO35.append(datetime.strptime(dattimO35[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=8))

# V2_18_Hg
dattimHg5 = np.array(Hg_V2_18['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateHg5=[]
for i in range(len(dattimHg5)):
    dateHg5.append(datetime.strptime(dattimHg5[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=8))
    
#------------------------------------
# V3_18
dat6 = np.array(V3_18T['Date'])
tim6 = np.array(V3_18T['Time'])
dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    date6.append(datetime.strptime(dattim6[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V3_18_O3
dattimO36 = np.array(O3_V3_18['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateO36=[]
for i in range(len(dattimO36)):
    dateO36.append(datetime.strptime(dattimO36[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=5))

# V3_18_Hg
dattimHg6 = np.array(Hg_V3_18['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateHg6=[]
for i in range(len(dattimHg6)):
    dateHg6.append(datetime.strptime(dattimHg6[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=5))
    
#------------------------------------
# SIPEXII
dat7 = np.array(SIPEXIIT['Date'])
tim7 = np.array(SIPEXIIT['Time'])
dattim7 = dat7+' '+tim7

#CONVERT TO DATETIME FROM STRING
date7=[]
for i in range(len(dattim7)):
    date7.append(datetime.strptime(dattim7[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# SIPEXII_O3
dattimO37 = np.array(O3_SIPEXII['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateO37=[]
for i in range(len(dattimO37)):
    dateO37.append(datetime.strptime(dattimO37[i],'%d/%m/%Y %H:%M:%S'))#+ timedelta(hours=8))
 
# SIPEXII_Hg
dattimHg7 = np.array(Hg_SIPEXII['DateTime'])

#CONVERT TO DATETIME FROM STRING
dateHg7=[]
for i in range(len(dattimHg7)):
    dateHg7.append(datetime.strptime(dattimHg7[i],'%d/%m/%Y %H:%M:%S')+ timedelta(hours=8))
    
#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax.set_zorder(ax2.get_zorder()+1)
ax.patch.set_visible(False)

# Plot the variables
ax.plot(date2, BrO_V2_17, marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)')
ax2.plot(dateHg2, Hg0_V2_17, ls='--', c='black', label ='Hg$^0$\n(ng m$^-$$^3$)')
#ax3.plot(date2, O3_V2_17a, ls='--', c='orange', label ='O3')
ax3.plot(dateO32, O3_V2_17b, ls='--', c='orange', label ='O3')
#UL1 = BrO_V1_17_DM + BrO_V1_17_STD # find the upper limit
#LL1 = BrO_V1_17_DM - BrO_V1_17_STD # find the lower limit
#ax.plot(date1_DM, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date1_DM, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date1_DM, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2018,1,2),datetime(2018,1,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(0,1.0)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax2.set_ylabel('Hg$^0$ (ng m$^-$$^3$)', fontsize=10)
ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('Event 1', fontsize=20, y=1.1)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')
#legend.get_frame().set_facecolor('#00FFCC')
#legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax.set_zorder(ax2.get_zorder()+1)
ax.patch.set_visible(False)

# Plot the variables
ax.plot(date3, BrO_V3_17, marker='o', c='blue', markersize = 3.0, ls='-', label ='V2 (2017-18)')
ax2.plot(dateHg3, Hg0_V3_17, ls='--', c='black', label ='Hg$^0$\n(ng m$^-$$^3$)')
#ax3.plot(date3, O3_V3_17a, ls='--', c='orange', label ='O3')
ax3.plot(dateO33, O3_V3_17b, ls='--', c='orange', label ='O3')
#UL2 = BrO_V2_17_DM + BrO_V2_17_STD # find the upper limit
#LL2 = BrO_V2_17_DM - BrO_V2_17_STD # find the lower limit
#ax.plot(date2_DM, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date2_DM, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date2_DM, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2018,1,27),datetime(2018,1,28)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(0,1.0)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Hg$^0$ (ng m$^-$$^3$)', fontsize=10)
ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('Event 2', fontsize=20, y=1.1)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')
#legend.get_frame().set_facecolor('#00FFCC')
#legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax.set_zorder(ax2.get_zorder()+1)
ax.patch.set_visible(False)

# Plot the variables
ax.plot(date3, BrO_V3_17, marker='o', c='blue', markersize = 3.0, ls='-', label ='V3 (2017-18)')
ax2.plot(dateHg3, Hg0_V3_17, ls='--', c='black', label ='Hg$^0$\n(ng m$^-$$^3$)')
#ax3.plot(date3, O3_V3_17a, ls='--', c='orange', label ='O3')
ax3.plot(dateO33, O3_V3_17b, ls='--', c='orange', label ='O3')
#UL3 = BrO_V3_17_DM + BrO_V3_17_STD # find the upper limit
#LL3 = BrO_V3_17_DM - BrO_V3_17_STD # find the lower limit
#ax.plot(date3_DM, UL3, c='blue', ls='--', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date3_DM, LL3, c='blue', ls='--', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date3_DM, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2018,2,1),datetime(2018,2,2)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(0,1.0)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Hg$^0$ (ng m$^-$$^3$)', fontsize=10)
ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('Event 3', fontsize=20, y=1.1)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')
#legend.get_frame().set_facecolor('#00FFCC')
#legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax.set_zorder(ax2.get_zorder()+1)
ax.patch.set_visible(False)

# Plot the variables
ax.plot(date4, BrO_V1_18, marker='o', c='red', markersize = 3.0, ls='-', label ='V1 (2018-19)')
ax2.plot(dateHg4, Hg0_V1_18, ls='--', c='black', label ='Hg$^0$\n(ng m$^-$$^3$)')
#ax3.plot(date4, O3_V1_18a, ls='--', c='orange', label ='O3')
ax3.plot(dateO34, O3_V1_18b, ls='--', c='orange', label ='O3')
#UL4 = BrO_V1_18_DM + BrO_V1_18_STD # find the upper limit
#LL4 = BrO_V1_18_DM - BrO_V1_18_STD # find the lower limit
#ax.plot(date4_DM, UL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date4_DM, LL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date4_DM, UL4, LL4, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2018,11,7),datetime(2018,11,8)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(0,1.0)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Hg$^0$ (ng m$^-$$^3$)', fontsize=10)
ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('Event 4', fontsize=20, y=1.1)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')
#legend.get_frame().set_facecolor('#00FFCC')
#legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax.set_zorder(ax2.get_zorder()+1)
ax.patch.set_visible(False)

# Plot the variables
ax.plot(date6, BrO_V3_18, marker='o', c='red', markersize = 3.0, ls='-', label ='V2 (2018-19)')
ax2.plot(dateHg6, Hg0_V3_18, ls='--', c='black', label ='Hg$^0$\n(ng m$^-$$^3$)')
#ax3.plot(date6, O3_V3_18a, ls='--', c='orange', label ='O3')
ax3.plot(dateO36, O3_V3_18b, ls='--', c='orange', label ='O3')
#UL5 = BrO_V2_18_DM + BrO_V2_18_STD # find the upper limit
#LL5 = BrO_V2_18_DM - BrO_V2_18_STD # find the lower limit
#ax.plot(date5_DM, UL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date5_DM, LL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date5_DM, UL5, LL5, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2019,1,25),datetime(2019,1,26)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(0,1.0)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Hg$^0$ (ng m$^-$$^3$)', fontsize=10)
ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('Event 5', fontsize=20, y=1.1)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')
#legend.get_frame().set_facecolor('#00FFCC')
#legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax.set_zorder(ax2.get_zorder()+1)
ax.patch.set_visible(False)

# Plot the variables
ax.plot(date6, BrO_V3_18, marker='o', c='red', markersize = 3.0, ls='-', label ='V3 (2018-19)')
ax2.plot(dateHg6, Hg0_V3_18, ls='--', c='black', label ='Hg$^0$\n(ng m$^-$$^3$)')
#ax3.plot(date6, O3_V3_18a, ls='--', c='orange', label ='O3')
ax3.plot(dateO36, O3_V3_18b, ls='--', c='orange', label ='O3')
#UL6 = BrO_V3_18_DM + BrO_V3_18_STD # find the upper limit
#LL6 = BrO_V3_18_DM - BrO_V3_18_STD # find the lower limit
#ax.plot(date6_DM, UL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date6_DM, LL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date6_DM, UL6, LL6, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2019,2,2),datetime(2019,2,3)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(0,1.0)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Hg$^0$ (ng m$^-$$^3$)', fontsize=10)
ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('Event 6', fontsize=20, y=1.1)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')
#legend.get_frame().set_facecolor('#00FFCC')
#legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)
ax.set_zorder(ax2.get_zorder()+1)
ax.patch.set_visible(False)

# Plot the variables
ax.plot(date7, BrO_SIPEXII, marker='o', c='green', markersize = 3.0, ls='-', label ='SIPEXII (2012)')
ax2.plot(dateHg7, Hg0_SIPEXII, ls='--', c='black', label ='Hg$^0$ (ng m$^-$$^3$)')
#ax3.plot(date7, O3_SIPEXIIa, ls='--', c='orange', label ='O3')
ax3.plot(dateO37, O3_SIPEXIIb, ls='--', c='orange', label ='O3')
#UL7 = BrO_SIPEXII_DM + BrO_SIPEXII_STD # find the upper limit
#LL7 = BrO_SIPEXII_DM - BrO_SIPEXII_STD # find the lower limit
#ax.plot(date7_DM, UL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
#ax.plot(date7_DM, LL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
#ax.fill_between(date7_DM, UL7, LL7, facecolor='green', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
plt.xlim(datetime(2012,9,28),datetime(2012,9,29)) # all dates
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('green')
ax.tick_params(axis='y', which='both', colors='green')
ax.set_ylim(0,25)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(0,1.5)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.label.set_color('orange')
ax3.tick_params(axis='y', which='both', colors='orange')
ax3.set_ylim(0,35)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Hg$^0$ (ng m$^-$$^3$)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
ax3.set_ylabel('O$_3$ (ppbv)', fontsize=10)
#Plot the legend and title
plt.title('Event 7', fontsize=20, y=1.1)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#legend = ax.legend(loc='upper left')
#legend.get_frame().set_facecolor('#00FFCC')
#legend.get_frame().set_alpha(0.9)
