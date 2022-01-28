#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:39:27 2019

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
from scipy import signal, stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_Filtered.csv') 
V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_Filtered.csv')
V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_Filtered.csv')
V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_Filtered.csv')
V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_Filtered.csv')
V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_Filtered.csv')

## When less than 65S
#is_65=V1_18['LATITUDE']<=-65
#V1_18=V1_18[is_65]

#------------------------------------------------------------------------------
# Filter for when Solar Radiation greater than 100 W/m2

#--------------------
# V1 (2017-18)
Sol_s1_17 = np.array(V1_17['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p1_17 = np.array(V1_17['RAD_SLR_PORT_WPERM2']) # port side solar radiation
V1_17['MeanSol'] = V1_17[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_17 = np.array(V1_17['MeanSol'])

## apply the filter (>100 W/m2)
#is_sol=V1_17['MeanSol']>100
#V1_17=V1_17[is_sol]

#--------------------
# V2 (2017-18)
Sol_s2_17 = np.array(V2_17['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p2_17 = np.array(V2_17['RAD_SLR_PORT_WPERM2']) # port side solar radiation
V2_17['MeanSol'] = V2_17[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_17 = np.array(V2_17['MeanSol'])

## apply the filter (>100 W/m2)
#is_sol=V2_17['MeanSol']>100
#V2_17=V2_17[is_sol]

#--------------------
# V3 (2017-18)
Sol_s3_17 = np.array(V3_17['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p3_17 = np.array(V3_17['RAD_SLR_PORT_WPERM2']) # port side solar radiation
V3_17['MeanSol'] = V3_17[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_17 = np.array(V3_17['MeanSol'])

## apply the filter (>100 W/m2)
#is_sol=V3_17['MeanSol']>100
#V3_18=V3_17[is_sol]

#--------------------
# V1 (2018-19)
Sol_s1_18 = np.array(V1_18['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p1_18 = np.array(V1_18['RAD_SLR_PORT_WPERM2']) # port side solar radiation
V1_18['MeanSol'] = V1_18[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_18 = np.array(V1_18['MeanSol'])

## apply the filter (>100 W/m2)
#is_sol=V1_18['MeanSol']>100
#V1_18=V1_18[is_sol]

#--------------------
# V2 (2018-19)
Sol_s2_18 = np.array(V2_18['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p2_18 = np.array(V2_18['RAD_SLR_PORT_WPERM2']) # port side solar radiation
V2_18['MeanSol'] = V2_18[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_18 = np.array(V2_18['MeanSol'])

## apply the filter (>100 W/m2)
#is_sol=V2_18['MeanSol']>100
#V2_18=V2_18[is_sol]

#--------------------
# V3 (2018-19)
Sol_s3_18 = np.array(V3_18['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p3_18 = np.array(V3_18['RAD_SLR_PORT_WPERM2']) # port side solar radiation
V3_18['MeanSol'] = V3_18[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_18 = np.array(V3_18['MeanSol'])

## apply the filter (>100 W/m2)
#is_sol=V3_18['MeanSol']>100
#V3_18=V3_18[is_sol]

#------------------------------------------------------------------------------
# Define the variables

# V1 (2017-18)
# BrO surface volume mixing ratio (VMR)
BrO_vmr_V1_17 = np.array(V1_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv
# Sea Ice Concentration
SeaIce_V1_17 = np.array(V1_17['Sea_Ice_Conc'])*100

# V2 (2017-18)
# BrO surface volume mixing ratio (VMR)
BrO_vmr_V2_17 = np.array(V2_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv
# Sea Ice Concentration
SeaIce_V2_17 = np.array(V2_17['Sea_Ice_Conc'])*100

# V3 (2017-18)
# BrO surface volume mixing ratio (VMR)
BrO_vmr_V3_17 = np.array(V3_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv
# Sea Ice Concentration
SeaIce_V3_17 = np.array(V3_17['Sea_Ice_Conc'])*100

# V1 (2018-19)
# BrO surface volume mixing ratio (VMR)
BrO_vmr_V1_18 = np.array(V1_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv
# Sea Ice Concentration
SeaIce_V1_18 = np.array(V1_18['Sea_Ice_Conc'])*100

# V2 (2018-19)
# BrO surface volume mixing ratio (VMR)
BrO_vmr_V2_18 = np.array(V2_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv
# Sea Ice Concentration
SeaIce_V2_18 = np.array(V2_18['Sea_Ice_Conc'])*100

# V3 (2018-19)
# BrO surface volume mixing ratio (VMR)
BrO_vmr_V3_18 = np.array(V3_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv
# Sea Ice Concentration
SeaIce_V3_18 = np.array(V3_18['Sea_Ice_Conc'])*100

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)
# Between Sea Ice Cover and BrO Concentration

# V1 (2017-18)
r_rowD1, p_valueD1 = stats.pearsonr(SeaIce_V1_17,BrO_vmr_V1_17)
slopeD1, interceptD1, rD1, pD1, std_errD1= stats.linregress(SeaIce_V1_17,BrO_vmr_V1_17)

# V2 (2017-18)
r_rowD2, p_valueD2 = stats.pearsonr(SeaIce_V2_17,BrO_vmr_V2_17)
slopeD2, interceptD2, rD2, pD2, std_errD2= stats.linregress(SeaIce_V2_17,BrO_vmr_V2_17)

# V3 (2017-18)
r_rowD3, p_valueD3 = stats.pearsonr(SeaIce_V3_17,BrO_vmr_V3_17)
slopeD3, interceptD3, rD3, pD3, std_errD3= stats.linregress(SeaIce_V3_17,BrO_vmr_V3_17)

# V1 (2018-19)
r_rowD4, p_valueD4 = stats.pearsonr(SeaIce_V1_18,BrO_vmr_V1_18)
slopeD4, interceptD4, rD4, pD4, std_errD4= stats.linregress(SeaIce_V1_18,BrO_vmr_V1_18)

# V2 (2018-19)
# Scan for NaN values
finiteY1mask = np.isfinite(BrO_vmr_V2_18) # Scan for NaN values
SeaIceClean = SeaIce_V2_18[finiteY1mask]     # Remove NaN values from Hg0_V1_18
BrOClean = BrO_vmr_V2_18[finiteY1mask] # Remove NaN values from BrO_V1_18
SolClean = Sol_V2_18[finiteY1mask] # Remove NaN values from Sol_V1_18
r_rowD5, p_valueD5 = stats.pearsonr(SeaIceClean,BrOClean)
slopeD5, interceptD5, rD5, pD5, std_errD5= stats.linregress(SeaIceClean,BrOClean)

# V3 (2018-19)
r_rowD6, p_valueD6 = stats.pearsonr(SeaIce_V3_18,BrO_vmr_V3_18)
slopeD6, interceptD6, rD6, pD6, std_errD6= stats.linregress(SeaIce_V3_18,BrO_vmr_V3_18)

#------------------------------------------------------------------------------
# PLOT THE GRAPH

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(231) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(SeaIce_V1_17, BrO_vmr_V1_17, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SeaIce_V1_17, BrO_vmr_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_V1_17, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
#line1, = plt.plot(SeaIce_V1_17, interceptD1 + slopeD1*Sol_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-1, 100)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0, 115)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Sea ice concentration\n(%)', fontsize=10)

#Plot the legend and title
plt.title('CAMMPCAN V1 2017-18', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD5))+"$\pm$ "+str("%7.4f"%(std_errD5))+" W/m$^2$, r: "+str("%7.4f"%(rD5))+")", xy=(600.0,18.0), color='black', fontweight='bold')

#------------------------------
# Graph 2
ax=plt.subplot(232) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(SeaIce_V2_17, BrO_vmr_V2_17, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SeaIce_V2_17, BrO_vmr_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_V2_17, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
#line2, = plt.plot(SeaIce_V2_17, interceptD2 + slopeD2*Sol_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-1, 100)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0, 115)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Sea ice concentration\n(%)', fontsize=10)

#Plot the legend and title
plt.title('CAMMPCAN V2 2017-18', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD5))+"$\pm$ "+str("%7.4f"%(std_errD5))+" W/m$^2$, r: "+str("%7.4f"%(rD5))+")", xy=(600.0,18.0), color='black', fontweight='bold')

#------------------------------
# Graph 3
ax=plt.subplot(233) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(SeaIce_V3_17, BrO_vmr_V3_17, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SeaIce_V3_17, BrO_vmr_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_V3_17, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
#line3, = plt.plot(SeaIce_V3_17, interceptD3 + slopeD3*Sol_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-1, 100)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0, 115)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Sea ice concentration\n(%)', fontsize=10)

#Plot the legend and title
plt.title('CAMMPCAN V3 2017-18', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD5))+"$\pm$ "+str("%7.4f"%(std_errD5))+" W/m$^2$, r: "+str("%7.4f"%(rD5))+")", xy=(600.0,18.0), color='black', fontweight='bold')

#------------------------------
# Graph 4
ax=plt.subplot(234) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(SeaIce_V1_18, BrO_vmr_V1_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SeaIce_V1_18, BrO_vmr_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_V1_18, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
#line4, = plt.plot(SeaIce_V1_18, interceptD4 + slopeD4*Sol_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-1, 100)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0, 115)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Sea ice concentration\n(%)', fontsize=10)

#Plot the legend and title
plt.title('CAMMPCAN V1 2018-19', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD5))+"$\pm$ "+str("%7.4f"%(std_errD5))+" W/m$^2$, r: "+str("%7.4f"%(rD5))+")", xy=(600.0,18.0), color='black', fontweight='bold')

#------------------------------
# Graph 5
ax=plt.subplot(235) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(SeaIce_V2_18, BrO_vmr_V2_18, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SeaIce_V2_18, BrO_vmr_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_V2_18, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
#line5, = plt.plot(SeaIce_V2_18, interceptD5 + slopeD5*Sol_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-1, 100)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0, 115)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Sea ice concentration\n(%)', fontsize=10)

#Plot the legend and title
plt.title('CAMMPCAN V2 2018-19', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD5))+"$\pm$ "+str("%7.4f"%(std_errD5))+" W/m$^2$, r: "+str("%7.4f"%(rD5))+")", xy=(600.0,18.0), color='black', fontweight='bold')

#------------------------------
# Graph 6
ax=plt.subplot(236) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
#ax.plot(SeaIce_V3_17, BrO_vmr_V3_17, marker='o', c='red', markersize = 3.0, linestyle='None')
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SeaIce_V3_18, BrO_vmr_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_V3_18, cmap=cmap)
plt.colorbar(label='Solar\nradiation\n(W/m$^2$)')

# Plot the regression line
#line6, = plt.plot(SeaIce_V3_18, interceptD6 + slopeD6*Sol_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-1, 100)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0, 115)
#ax.tick_params(labelright=True)
#ax.yaxis.set_ticks_position('both')
#ax.xaxis.set_tick_position(pad=20)

# Plot the axis labels
ax.set_ylabel('BrO\n(pptv)', fontsize=10)
ax.set_xlabel('Sea ice concentration\n(%)', fontsize=10)

#Plot the legend and title
plt.title('CAMMPCAN V3 2018-19', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD5))+"$\pm$ "+str("%7.4f"%(std_errD5))+" W/m$^2$, r: "+str("%7.4f"%(rD5))+")", xy=(600.0,18.0), color='black', fontweight='bold')
