#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:39:27 2019

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
from scipy import signal, stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# V2_17 (2017-18)
V2_17_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_17_Data.csv',header=0,encoding = 'unicode_escape')
V2_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv')
V2_17_SI  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv')
V2_17_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv')
V2_17_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv')

#------------------------------------------------------------------------------
# Set the date

V2_17_BrO['DateTime'] = pd.to_datetime(V2_17_BrO['DateTime'], dayfirst=True)
V2_17_Met['DateTime'] = pd.to_datetime(V2_17_Met['DateTime'], dayfirst=True)
V2_17_SI['DateTime']  = pd.to_datetime(V2_17_SI['DateTime'],  dayfirst=True)
V2_17_Hg['DateTime']  = pd.to_datetime(V2_17_Hg['DateTime'],  dayfirst=True)
V2_17_O3['DateTime']  = pd.to_datetime(V2_17_O3['DateTime'],  dayfirst=True)

# set datetime as the index
V2_17_BrO = V2_17_BrO.set_index('DateTime')
V2_17_Met = V2_17_Met.set_index('DateTime')
V2_17_SI  = V2_17_SI.set_index('DateTime')
V2_17_Hg  = V2_17_Hg.set_index('DateTime')
V2_17_O3  = V2_17_O3.set_index('DateTime')

#------------------------------------------------------------------------------
# Resample all data to 20 min averages

V2_17_Met = V2_17_Met.resample('20T').mean()
V2_17_SI  = V2_17_SI.resample('20T').mean()
V2_17_Hg  = V2_17_Hg.resample('20T').mean()
V2_17_O3  = V2_17_O3.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

V2_17_Met.index = V2_17_Met.index - pd.Timedelta(minutes=10)
V2_17_SI.index  = V2_17_SI.index - pd.Timedelta(minutes=10)
V2_17_Hg.index  = V2_17_Hg.index - pd.Timedelta(minutes=10)
V2_17_O3.index  = V2_17_O3.index - pd.Timedelta(minutes=10)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

# V1_17 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V2_17_BrO['Time'] >= start_time) & (V2_17_BrO['Time'] < end_time)
V2_17_MM = V2_17_BrO[Midday]

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

V2_17F = (V2_17_MM['Filter'] < 0.6)
V2_17T = V2_17_MM[V2_17F]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1 = '2017-12-21'
end_date1 = '2017-12-23'
start_date2 = '2017-12-26'
end_date2 = '2018-01-6'
Casey1 = (V2_17T.index >= start_date1) & (V2_17T.index < end_date1)
Casey2 = (V2_17T.index >= start_date2) & (V2_17T.index < end_date2)
V2_17_Casey1 = V2_17T[Casey1]
V2_17_Casey2 = V2_17T[Casey2]
V2_17T = pd.concat([V2_17_Casey1,V2_17_Casey2], axis =0)

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

Data1 = pd.merge(left=V2_17T,right=V2_17_Met, how='left', left_index=True, right_index=True)
Data2 = pd.merge(left=Data1,right=V2_17_SI, how='left', left_index=True, right_index=True)
Data3 = pd.merge(left=Data2,right=V2_17_Hg, how='left', left_index=True, right_index=True)
Data4 = pd.merge(left=Data3,right=V2_17_O3, how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Define the variables

# BrO surface volume mixing ratio (VMR)
BrO = np.array(Data4['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv

# O3 (ppb)
O3 = np.array(Data4['O3_(ppb)_y']) # O3 (ppb)

# Solar Radiation (W/m2)
Sol_s = np.array(Data4['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p = np.array(Data4['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
Data4['MeanSol'] = Data4[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol = np.array(Data4['MeanSol'])

# Temperature (C)
Temp_s = np.array(Data4['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p = np.array(Data4['TEMP_AIR_PORT_DEGC_y']) # port side temperature
Data4['MeanTemp'] = Data4[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp = np.array(Data4['MeanTemp'])

# Wind Direction
WD_s = np.array(Data4['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p = np.array(Data4['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

# Wind Speed
WS_s = np.array(Data4['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p = np.array(Data4['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS = (WS_s + WS_p)/2 # Average the wind speed for port and starboard

# Vector Mean Wind Direction
WD_vect = ((WD_s * WS_s) / (WS_s + WS_p)) + ((WD_p * WS_p) / (WS_s + WS_p)) # Calculate the vector mean wind direction

# Hg0
Hg0 = np.array(Data4['ng/m3_y']) # Hg0

# Sea Ice Concentration
SI = np.array(Data4['Sea_Ice_Conc'])*100

# Relative Humidity
RH_s = np.array(Data4['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p = np.array(Data4['REL_HUMIDITY_PORT_PERCENT_y'])
RH = (RH_s + RH_p)/2

#------------------------------------------------------------------------------
# Scan for NaN values

# Pass 1 (Sol) 
finiteY1mask = np.isfinite(Sol) # Scan for NaN values
BrO = BrO[finiteY1mask] # Remove NaN values from BrO
O3 = O3[finiteY1mask] # Remove NaN values from Sol
Sol = Sol[finiteY1mask] # Remove NaN values from Sol
Temp = Temp[finiteY1mask] # Remove NaN values from Sol
WD_vect = WD_vect[finiteY1mask] # Remove NaN values from Sol
WS = WS[finiteY1mask] # Remove NaN values from Sol
Hg0 = Hg0[finiteY1mask] # Remove NaN values from Sol
SI = SI[finiteY1mask] # Remove NaN values from Sol

# Pass 2 (O3) 
finiteY2mask = np.isfinite(O3) # Scan for NaN values
BrO_O3 = BrO[finiteY2mask] # Remove NaN values from BrO
O3 = O3[finiteY2mask] # Remove NaN values from Temp
Sol_O3 = Sol[finiteY2mask] # Remove NaN values from Sol

# Pass 3 (Temp) 
finiteY3mask = np.isfinite(Temp) # Scan for NaN values
BrO_Temp = BrO[finiteY3mask] # Remove NaN values from BrO
Temp = Temp[finiteY3mask] # Remove NaN values from Temp
Sol_Temp = Sol[finiteY3mask] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
finiteY4mask = np.isfinite(WD_vect) # Scan for NaN values
BrO_WD = BrO[finiteY4mask] # Remove NaN values from BrO
WD_vect = WD_vect[finiteY4mask] # Remove NaN values from WD_vect
Sol_WD = Sol[finiteY4mask] # Remove NaN values from Sol

# Pass 5 (WS) 
finiteY5mask = np.isfinite(WS) # Scan for NaN values
BrO_WS = BrO[finiteY5mask] # Remove NaN values from BrO
WS = WS[finiteY5mask] # Remove NaN values from WS
Sol_WS = Sol[finiteY5mask] # Remove NaN values from Sol

# Pass 6 (Hg0) 
finiteY6mask = np.isfinite(Hg0) # Scan for NaN values
BrO_Hg0 = BrO[finiteY6mask] # Remove NaN values from BrO
Hg0 = Hg0[finiteY6mask] # Remove NaN values from SI
Sol_Hg0 = Sol[finiteY6mask] # Remove NaN values from Sol

# Pass 7 (SI Field) 
finiteY7mask = np.isfinite(SI) # Scan for NaN values
BrO_SI = BrO[finiteY7mask] # Remove NaN values from BrO
SI_SI = SI[finiteY7mask] # Remove NaN values from SI
Sol_SI = Sol[finiteY7mask] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)

# 1) Between O3 and BrO
r_rowD1, p_valueD1 = stats.pearsonr(O3,BrO_O3)
slopeD1, interceptD1, rD1, pD1, std_errD1= stats.linregress(O3,BrO_O3)

# 2) Between Temp and BrO
r_rowD2, p_valueD2 = stats.pearsonr(Temp,BrO)
slopeD2, interceptD2, rD2, pD2, std_errD2= stats.linregress(Temp,BrO)

# 3) Between Wind Direction and BrO
r_rowD3, p_valueD3 = stats.pearsonr(WD_vect,BrO_WD)
slopeD3, interceptD3, rD3, pD3, std_errD3= stats.linregress(WD_vect,BrO_WD)

# 4) Between Wind Speed and BrO
r_rowD4, p_valueD4 = stats.pearsonr(WS,BrO_WS)
slopeD4, interceptD4, rD4, pD4, std_errD4= stats.linregress(WS,BrO_WS)

# 5) Between Solar Radiation and BrO
r_rowD5, p_valueD5 = stats.pearsonr(Sol,BrO)
slopeD5, interceptD5, rD5, pD5, std_errD5= stats.linregress(Sol,BrO)

# 6) Between Hg0 and BrO
r_rowD6, p_valueD6 = stats.pearsonr(Hg0,BrO_Hg0)
slopeD6, interceptD6, rD6, pD6, std_errD6= stats.linregress(Hg0,BrO_Hg0)

# 7) Between SI and BrO
r_rowD7, p_valueD7 = stats.pearsonr(SI_SI,BrO_SI)
slopeD7, interceptD7, rD7, pD7, std_errD7= stats.linregress(SI_SI,BrO_SI)

#------------------------------------------------------------------------------
# PLOT THE GRAPH

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

# Graph 1
ax=plt.subplot(321) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(Temp_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
#norm = BoundaryNorm(np.arange(0,600,100), cmap.N)
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3, BrO_O3, edgecolors='none', marker='o', norm=norm, c=Sol_O3, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3, interceptD1 + slopeD1*O3, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.set_ylim(0, 0.07)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('O$_3$\n(ppbv)', fontsize=10)

#Plot the legend and title
plt.title('BrO vs O$_3$', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1))+" $\pm$"+str("%7.4f"%(std_errD1))+" pptv, r: "+str("%7.4f"%(rD1))+")", xy=(5.0,12.5), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(322) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(Temp_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp, BrO, edgecolors='none', marker='o', norm=norm, c=Sol, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp, interceptD2 + slopeD2*Temp, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.set_ylim(0, 0.07)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Temperature\n($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('BrO vs temperature', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2))+" $\pm$"+str("%7.4f"%(std_errD2))+" $^\circ$C, r: "+str("%7.4f"%(rD2))+")", xy=(-3.0,11.5), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(323) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(Temp_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect, BrO, edgecolors='none', marker='o', norm=norm, c=Sol, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect, interceptD3 + slopeD3*WD_vect, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.set_ylim(0, 0.07)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction\n($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('BrO vs wind vector direction', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3))+" $\pm$"+str("%7.4f"%(std_errD3))+" $^\circ$, r: "+str("%7.4f"%(rD3))+")", xy=(0.0,12.5), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(324) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(Temp_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS, BrO, edgecolors='none', marker='o', norm=norm, c=Sol, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS, interceptD4 + slopeD4*WS, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.set_ylim(0, 0.07)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Wind speed\n(m/s)', fontsize=10)

#Plot the legend and title
plt.title('BrO vs wind speed', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4))+" $\pm$"+str("%7.4f"%(std_errD4))+" m/s, r: "+str("%7.4f"%(rD4))+")", xy=(0.0,12.5), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(325) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(Temp_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol, BrO, edgecolors='none', marker='o', norm=norm, c=Sol, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol, interceptD5 + slopeD5*Sol, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
#ax.set_ylim(0, 0.07)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Solar radiation\n(W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('BrO vs solar radiation', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5))+" $\pm$"+str("%7.4f"%(std_errD5))+" W/m$^2$, r: "+str("%7.4f"%(rD5))+")", xy=(60.0,11.0), color='black', fontweight='bold')

##--------------------------------
## Graph 6
#ax=plt.subplot(326) # options graph 1 (vertical no, horizontal no, graph no)
#
## BrO VMR
##ax.plot(Temp_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
#cmap=plt.cm.rainbow
#norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
#plt.scatter(Hg0, BrO, edgecolors='none', marker='o', norm=norm, c=Sol, cmap=cmap)
#plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')
#
## Plot the regression line
#line6, = plt.plot(Hg0, interceptD6 + slopeD6*Hg0, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")
#
## Format x-axis
##ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
##x.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
## Format y-axis 1
#ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
##ax.set_ylim(0, 0.07)
##ax.tick_params(labelright=True)
##ax.yaxis.set_ticks_position('both')
##ax.xaxis.set_tick_position(pad=20)
#
## Plot the axis labels
#ax.set_ylabel('BrO\n(pptv)', fontsize=10)
#ax.set_xlabel('Hg$^0$\n(ng/m$^2$)', fontsize=10)
#
##Plot the legend and title
#plt.title('BrO vs Hg$^0$', fontsize=15)
#plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6))+" $\pm$ "+str("%7.4f"%(std_errD6))+" ng/m$^2$, r: "+str("%7.4f"%(rD6))+")", xy=(0.6,12.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(326) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(Temp_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI, BrO, edgecolors='none', marker='o', norm=norm, c=Sol, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI, interceptD7 + slopeD7*SI, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
#x.xaxis.set_minor_locator(ticker.MultipleLocator(1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1.0, 101.0)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration\n(%)', fontsize=10)

#Plot the legend and title
plt.title('BrO vs Sea Ice Concentration$^0$', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7))+" $\pm$"+str("%7.4f"%(std_errD7))+" %, r: "+str("%7.4f"%(rD7))+")", xy=(0.5,12.5), color='black', fontweight='bold')
