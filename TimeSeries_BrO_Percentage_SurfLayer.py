#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:32:08 2020

@author: ncp532
"""

# Drawing packages
import matplotlib.pyplot as plt
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

# Data handing packages
import numpy as np
import pandas as pd
from scipy import signal, stats

# Date and Time handling package
import datetime as dt
from datetime import datetime,time, timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# DEFINE THE DATASET

# BrO
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv',index_col=0)       # BrO V1 (2017/18)
BrO_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv',index_col=0)       # BrO V2 (2017/18)
BrO_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv',index_col=0)       # BrO V3 (2017/18)

BrO_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv',index_col=0)       # BrO V1 (2018/19)
BrO_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv',index_col=0)       # BrO V2 (2018/19)
BrO_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv',index_col=0)       # BrO V3 (2018/19)

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv',index_col=0) # BrO SIPEXII (2012)

#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR RELATIVE ERROR 

# Calculate the Relative Error (>=0.6)
Filter1 = BrO_V1_17['err_surf_vmr'] / BrO_V1_17['surf_vmr(ppmv)']
Filter2 = BrO_V2_17['err_surf_vmr'] / BrO_V2_17['surf_vmr(ppmv)']
Filter3 = BrO_V3_17['err_surf_vmr'] / BrO_V3_17['surf_vmr(ppmv)']

Filter4 = BrO_V1_18['err_surf_vmr'] / BrO_V1_18['surf_vmr(ppmv)']
Filter5 = BrO_V2_18['err_surf_vmr'] / BrO_V2_18['surf_vmr(ppmv)']
Filter6 = BrO_V3_18['err_surf_vmr'] / BrO_V3_18['surf_vmr(ppmv)']

Filter7 = BrO_SIPEXII['err_surf_vmr'] / BrO_SIPEXII['surf_vmr(ppmv)']

# Apply the filter
V1_17F       = Filter1 < 0.6
BrO_V1_17T   = BrO_V1_17[V1_17F]

V2_17F       = Filter2 < 0.6
BrO_V2_17T   = BrO_V2_17[V2_17F]

V3_17F       = Filter3 < 0.6
BrO_V3_17T   = BrO_V3_17[V3_17F]

V1_18F       = Filter4 < 0.6
BrO_V1_18T   = BrO_V1_18[V1_18F]

V2_18F       = Filter5 < 0.6
BrO_V2_18T   = BrO_V2_18[V2_18F]

V3_18F       = Filter6 < 0.6
BrO_V3_18T   = BrO_V3_18[V3_18F]

SIPEXIIF     = Filter7 < 0.6
BrO_SIPEXIIT = BrO_SIPEXII[SIPEXIIF]

#------------------------------------------------------------------------------
# TRANSPOSE THE MAX-DOAS DATAFRAMES

# BrO
BrO_V1_17T   = BrO_V1_17T
BrO_V2_17T   = BrO_V2_17T
BrO_V3_17MT  = BrO_V3_17T
BrO_V3_17DT  = BrO_V3_17T

BrO_V1_18T   = BrO_V1_18T
BrO_V2_18T   = BrO_V2_18T
BrO_V3_18MT  = BrO_V3_18T
BrO_V3_18DT  = BrO_V3_18T

BrO_SIPEXIIT = BrO_SIPEXII

#------------------------------------------------------------------------------
# SET THE DATE

# BrO
BrO_V1_17T.index   = (pd.to_datetime(BrO_V1_17T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_17T.index   = (pd.to_datetime(BrO_V2_17T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_17MT.index  = (pd.to_datetime(BrO_V3_17MT.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_17DT.index  = (pd.to_datetime(BrO_V3_17DT.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_V1_18T.index   = (pd.to_datetime(BrO_V1_18T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_18T.index   = (pd.to_datetime(BrO_V2_18T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_18MT.index  = (pd.to_datetime(BrO_V3_18MT.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_18DT.index  = (pd.to_datetime(BrO_V3_18DT.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_SIPEXIIT.index = (pd.to_datetime(BrO_SIPEXIIT.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# REPLACE ERRONEOUS VALUES WITH NAN

# BrO
BrO_V1_17T   = BrO_V1_17T.replace(-9999.000000, np.nan)
BrO_V2_17T   = BrO_V2_17T.replace(-9999.000000, np.nan)
BrO_V3_17MT  = BrO_V3_17MT.replace(-9999.000000, np.nan)
BrO_V3_17DT  = BrO_V3_17DT.replace(-9999.000000, np.nan)

BrO_V1_18T   = BrO_V1_18T.replace(-9999.000000, np.nan)
BrO_V2_18T   = BrO_V2_18T.replace(-9999.000000, np.nan)
BrO_V3_18MT  = BrO_V3_18MT.replace(-9999.000000, np.nan)
BrO_V3_18DT  = BrO_V3_18DT.replace(-9999.000000, np.nan)

BrO_SIPEXIIT = BrO_SIPEXIIT.replace(9.67e-05,np.nan)
BrO_SIPEXIIT = BrO_SIPEXIIT.replace(7.67e-06,np.nan)
BrO_SIPEXIIT = BrO_SIPEXIIT.replace(7.67e-07,np.nan)
BrO_SIPEXIIT.loc[BrO_SIPEXIIT.isnull().any(axis=1), :] = np.nan # if any element in the row is nan, set the whole row to nan
BrO_SIPEXIIT = BrO_SIPEXIIT.replace(-9999.000000, np.nan)

#------------------------------------------------------------------------------
# Filter the datasets based on the date

#-----------------------------
# V1_17 Davis (14-22 Nov 2017)
#-----------------------------
start_date   = '2017-11-14'
end_date     = '2017-11-23'
# BrO
Davis        = (BrO_V1_17T.index >= start_date) & (BrO_V1_17T.index < end_date)
V1_17_BrO    = BrO_V1_17T[Davis]

#-----------------------------
# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
#-----------------------------
start_date1 = '2017-12-21'
end_date1 = '2017-12-23'
start_date2 = '2017-12-26'
end_date2 = '2018-01-6'
# BrO
Casey1       = (BrO_V2_17T.index >= start_date1) & (BrO_V2_17T.index < end_date1)
Casey2       = (BrO_V2_17T.index >= start_date2) & (BrO_V2_17T.index < end_date2)
V2_17_BrO1   = BrO_V2_17T[Casey1]
V2_17_BrO2   = BrO_V2_17T[Casey2]
V2_17_BrO    = pd.concat([V2_17_BrO1,V2_17_BrO2], axis =0)

#-----------------------------
# V3_17 Mawson (1-17 Feb 2018)
#-----------------------------
start_date    = '2018-02-01'
end_date      = '2018-02-18'
# BrO
Mawson        = (BrO_V3_17MT.index >= start_date) & (BrO_V3_17MT.index < end_date)
V3_17_BrOM    = BrO_V3_17MT[Mawson]

#-----------------------------
# V3_17 Davis (27-30 Jan 2018 and 19-21 Feb 2018)
#-----------------------------
start_date1   = '2018-01-27'
end_date1     = '2018-01-31'
start_date2   = '2018-02-19'
end_date2     = '2018-02-22'
# BrO
Davis1        = (BrO_V3_17DT.index >= start_date1) & (BrO_V3_17DT.index < end_date1)
Davis2        = (BrO_V3_17DT.index >= start_date2) & (BrO_V3_17DT.index < end_date2)
V3_17_BrO1    = BrO_V3_17DT[Davis1]
V3_17_BrO2    = BrO_V3_17DT[Davis2]
V3_17_BrOD    = pd.concat([V3_17_BrO1,V3_17_BrO2], axis =0)

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# BrO
Davis        = (BrO_V1_18T.index >= start_date) & (BrO_V1_18T.index < end_date)
V1_18_BrO    = BrO_V1_18T[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# BrO
Casey        = (BrO_V2_18T.index >= start_date) & (BrO_V2_18T.index < end_date)
V2_18_BrO    = BrO_V2_18T[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# BrO
Mawson        = (BrO_V3_18MT.index >= start_date) & (BrO_V3_18MT.index < end_date)
V3_18_BrOM    = BrO_V3_18MT[Mawson]

#-----------------------------
# V3_18 Davis (26-28 Jan 2019 and 19-20 Feb 2019)
#-----------------------------
start_date1   = '2019-01-26'
end_date1     = '2019-01-29'
start_date2   = '2019-02-19'
end_date2     = '2019-02-21'
# BrO
Davis1        = (BrO_V3_18DT.index >= start_date1) & (BrO_V3_18DT.index < end_date1)
Davis2        = (BrO_V3_18DT.index >= start_date2) & (BrO_V3_18DT.index < end_date2)
V3_18_BrO1    = BrO_V3_18DT[Davis1]
V3_18_BrO2    = BrO_V3_18DT[Davis2]
V3_18_BrOD    = pd.concat([V3_18_BrO1,V3_18_BrO2], axis =0)

#-----------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#-----------------------------
start_date     = '2012-09-23'
end_date       = '2012-11-12'
# BrO
SIPEX          = (BrO_SIPEXIIT.index >= start_date) & (BrO_SIPEXIIT.index < end_date)
SIPEXII_BrO    = BrO_SIPEXIIT[SIPEX]

#------------------------------------------------------------------------------
# SET THE VARIABLES

# Surface BrO
BrO_Surf_V1_17   = (V1_17_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V2_17   = (V2_17_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V3_17M  = (V3_17_BrOM['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2
BrO_Surf_V3_17D  = (V3_17_BrOD['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2

BrO_Surf_V1_18   = (V1_18_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V2_18   = (V2_18_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V3_18M  = (V3_18_BrOM['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2
BrO_Surf_V3_18D  = (V3_18_BrOD['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2

BrO_Surf_SIPEXII = (SIPEXII_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2

# LtCol BrO
BrO_LtCol_V1_17   = V1_17_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V2_17   = V2_17_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V3_17M  = V3_17_BrOM['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD
BrO_LtCol_V3_17D  = V3_17_BrOD['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD

BrO_LtCol_V1_18   = V1_18_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V2_18   = V2_18_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V3_18M  = V3_18_BrOM['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD
BrO_LtCol_V3_18D  = V3_18_BrOD['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD

BrO_LtCol_SIPEXII = SIPEXII_BrO['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD

#------------------------------------------------------------------------------
# CALCULATE THE PERCENTAGE OF BrO IN SURFACE LAYER

Perc_V1_17   = (BrO_Surf_V1_17   / BrO_LtCol_V1_17)*100
Perc_V2_17   = (BrO_Surf_V2_17   / BrO_LtCol_V2_17)*100
Perc_V3_17M  = (BrO_Surf_V3_17M  / BrO_LtCol_V3_17M)*100
Perc_V3_17D  = (BrO_Surf_V3_17D  / BrO_LtCol_V3_17D)*100

Perc_V1_18   = (BrO_Surf_V1_18   / BrO_LtCol_V1_18)*100
Perc_V2_18   = (BrO_Surf_V2_18   / BrO_LtCol_V2_18)*100
Perc_V3_18M  = (BrO_Surf_V3_18M  / BrO_LtCol_V3_18M)*100
Perc_V3_18D  = (BrO_Surf_V3_18D  / BrO_LtCol_V3_18D)*100

Perc_SIPEXII = (BrO_Surf_SIPEXII / BrO_LtCol_SIPEXII)*100

#------------------------------------------------------------------------------
# CALCULATE THE MEAN PERCENTAGE OF BrO IN SURFACE LAYER

Mean_Perc_V1_17  = np.mean(Perc_V1_17)
Mean_Perc_V2_17  = np.mean(Perc_V2_17)
Mean_Perc_V3_17M = np.mean(Perc_V3_17M)
Mean_Perc_V3_17D = np.mean(Perc_V3_17D)

Mean_Perc_V1_18  = np.mean(Perc_V1_18)
Mean_Perc_V2_18  = np.mean(Perc_V2_18)
Mean_Perc_V3_18M = np.mean(Perc_V3_18M)
Mean_Perc_V3_18D = np.mean(Perc_V3_18D)

Mean_Perc_SIPEXII = np.mean(Perc_SIPEXII)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN)

fig = plt.figure()

gs = gridspec.GridSpec(nrows=3,
                       ncols=4, 
                       figure=fig, 
                       width_ratios= [0.25,0.25,0.25,0.25],
                       height_ratios=[0.25, 0.25, 0.25],
                       hspace=0.3, wspace=0.35)

#-------------------------------------
# Graph 1 (V1 2017-18)
ax = plt.subplot(gs[0,0:2])
ax2 = ax.twinx()

# Plot surf and LTcol BrO
ax.plot(V1_17_BrO.index, BrO_Surf_V1_17,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_s$$_u$$_r$$_f$')  # Surf BrO
ax.plot(V1_17_BrO.index, BrO_LtCol_V1_17,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_L$$_T$$_c$$_o$$_l$') # LTcol BrO

# Plot perecntage of BrO in surface layer
ax2.plot(V1_17_BrO.index, Perc_V1_17, marker='o', c='g', markersize = 2.0, linestyle='none', label='% BrO <200m') # LTcol BrO

# Format x-axis
plt.xlim(datetime(2017,11,14),datetime(2017,11,23)) # V1 17 (14-22 Nov 2017)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.6)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,42)

# Plot the axis labels, legend and title
plt.title('V1 (2017-18)', fontsize=15, y=1.05)
ax.set_ylabel('BrO (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
#ax2.set_ylabel('BrO <200m (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#plt.legend(bbox_to_anchor=(0.85, 0.95), loc=2, borderaxespad=0.)

#-------------------------------------
# Graph 2 (V2 2017-18)
ax = plt.subplot(gs[1,0:2])
ax2 = ax.twinx()

# Plot BrO
ax.plot(V2_17_BrO.index, BrO_Surf_V2_17,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_s$$_u$$_r$$_f$')  # Surf BrO
ax.plot(V2_17_BrO.index, BrO_LtCol_V2_17,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_L$$_T$$_c$$_o$$_l$') # LTcol BrO

# Plot perecntage of BrO in surface layer
ax2.plot(V2_17_BrO.index, Perc_V2_17, marker='o', c='g', markersize = 2.0, linestyle='none', label='% BrO <200m') # LTcol BrO

# Format x-axis
plt.xlim(datetime(2017,12,21),datetime(2018,1,6)) # V2 17 (21-22 Dec 2017 & 26 Dec - 5 Jan 2018)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.6)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,42)

# Plot the axis labels, legend and title
plt.title('V2 (2017-18)', fontsize=15, y=1.05)
ax.set_ylabel('BrO (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
#ax2.set_ylabel('BrO <200m (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#plt.legend(bbox_to_anchor=(0.85, 0.95), loc=2, borderaxespad=0.)

#-------------------------------------
# Graph 3 (V3 2017-18)
ax = plt.subplot(gs[2,0:2])
ax2 = ax.twinx()

# Plot BrO
ax.plot(V3_17_BrOM.index, BrO_Surf_V3_17M,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_s$$_u$$_r$$_f$')  # Surf BrO
ax.plot(V3_17_BrOM.index, BrO_LtCol_V3_17M,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_L$$_T$$_c$$_o$$_l$') # LTcol BrO
ax.plot(V3_17_BrOD.index, BrO_Surf_V3_17D,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none')  # Surf BrO
ax.plot(V3_17_BrOD.index, BrO_LtCol_V3_17D,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none') # LTcol BrO

# Plot perecntage of BrO in surface layer
ax2.plot(V3_17_BrOM.index, Perc_V3_17M, marker='o', c='g', markersize = 2.0, linestyle='none', label='% BrO <200m') # LTcol BrO
ax2.plot(V3_17_BrOD.index, Perc_V3_17D, marker='o', c='g', markersize = 2.0, linestyle='none') # LTcol BrO

# Format x-axis
plt.xlim(datetime(2018,1,27),datetime(2018,2,22)) # V3 17 (27 Jan - 21 Feb 2018)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.6)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,42)

# Plot the axis labels, legend and title
plt.title('V3 (2017-18)', fontsize=15, y=1.05)
ax.set_ylabel('BrO (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
#ax2.set_ylabel('BrO <200m (%)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#plt.legend(bbox_to_anchor=(0.85, 0.95), loc=2, borderaxespad=0.)

#-------------------------------------
# Graph 4 (V1 2018-19)
ax = plt.subplot(gs[0,2:4])
ax2 = ax.twinx()

# Plot BrO
ln1 = ax.plot(V1_18_BrO.index, BrO_Surf_V1_18,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_s$$_u$$_r$$_f$')  # Surf BrO
ln2 = ax.plot(V1_18_BrO.index, BrO_LtCol_V1_18,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_L$$_T$$_c$$_o$$_l$') # LTcol BrO

# Plot perecntage of BrO in surface layer
ln3 = ax2.plot(V1_18_BrO.index, Perc_V1_18, marker='o', c='g', markersize = 2.0, linestyle='none', label='% BrO <200m') # LTcol BrO

# Format x-axis
plt.xlim(datetime(2018,11,7),datetime(2018,11,16)) # V1 18 (7-15 Nov 2018)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.6)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,42)

# Plot the axis labels, legend and title
plt.title('V1 (2018-19)', fontsize=15, y=1.05)
#ax.set_ylabel('BrO (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
ax2.set_ylabel('BrO <200m (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#plt.legend(bbox_to_anchor=(1.05, 1.0), loc=2, borderaxespad=0.)

# added these three lines
lns = ln1+ln2+ln3
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, bbox_to_anchor=(1.07, 1.0), loc=2)

#-------------------------------------
# Graph 5 (V2 2018-19)
ax = plt.subplot(gs[1,2:4])
ax2 = ax.twinx()

# Plot BrO
ax.plot(V2_18_BrO.index, BrO_Surf_V2_18,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_s$$_u$$_r$$_f$')  # Surf BrO
ax.plot(V2_18_BrO.index, BrO_LtCol_V2_18,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_L$$_T$$_c$$_o$$_l$') # LTcol BrO

# Plot perecntage of BrO in surface layer
ax2.plot(V2_18_BrO.index, Perc_V2_18, marker='o', c='g', markersize = 2.0, linestyle='none', label='% BrO <200m') # LTcol BrO

# Format x-axis
plt.xlim(datetime(2018,12,15),datetime(2018,12,31)) # V2 18 (15-30 Dec 2018)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.6)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,42)

# Plot the axis labels, legend and title
plt.title('V2 (2018-19)', fontsize=15, y=1.05)
#ax.set_ylabel('BrO (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
ax2.set_ylabel('BrO <200m (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#plt.legend(bbox_to_anchor=(0.85, 0.95), loc=2, borderaxespad=0.)

#-------------------------------------
# Graph 6 (V3 2018-19)
ax = plt.subplot(gs[2,2:4])
ax2 = ax.twinx()

# Plot BrO
ax.plot(V3_18_BrOM.index, BrO_Surf_V3_18M,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_s$$_u$$_r$$_f$')  # Surf BrO
ax.plot(V3_18_BrOM.index, BrO_LtCol_V3_18M,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none', label='BrO$_L$$_T$$_c$$_o$$_l$') # LTcol BrO
ax.plot(V3_18_BrOD.index, BrO_Surf_V3_18D,    marker='o', c='r', alpha=0.3, markersize = 2.0, linestyle='none')  # Surf BrO
ax.plot(V3_18_BrOD.index, BrO_LtCol_V3_18D,   marker='o', c='b', alpha=0.3, markersize = 2.0, linestyle='none') # LTcol BrO

# Plot perecntage of BrO in surface layer
ax2.plot(V3_18_BrOM.index, Perc_V3_18M, marker='o', c='g', markersize = 2.0, linestyle='none', label='% BrO <200m') # LTcol BrO
ax2.plot(V3_18_BrOD.index, Perc_V3_18D, marker='o', c='g', markersize = 2.0, linestyle='none') # LTcol BrO

# Format x-axis
plt.xlim(datetime(2019,1,26),datetime(2019,2,21)) # V3 18 (26 Jan 2019 - 20 Feb 2019)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.6)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,42)

# Plot the axis labels, legend and title
plt.title('V3 (2018-19)', fontsize=15, y=1.05)
#ax.set_ylabel('BrO (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
ax2.set_ylabel('BrO <200m (%)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#plt.legend(bbox_to_anchor=(0.85, 1.35), loc=2, borderaxespad=0.)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (SIPEXII)

fig = plt.figure()
ax = plt.subplot(111)
ax2 = ax.twinx()

# Plot BrO
ln1 = ax.plot(SIPEXII_BrO.index, BrO_Surf_SIPEXII,    marker='o', c='r', alpha=0.3, markersize = 4.0, linestyle='none', label='BrO$_s$$_u$$_r$$_f$')  # Surf BrO
ln2 = ax.plot(SIPEXII_BrO.index, BrO_LtCol_SIPEXII,   marker='o', c='b', alpha=0.3, markersize = 4.0, linestyle='none', label='BrO$_L$$_T$$_c$$_o$$_l$') # LTcol BrO

# Plot perecntage of BrO in surface layer
ln3 = ax2.plot(SIPEXII_BrO.index, Perc_SIPEXII, marker='o', c='g', markersize = 4.0, linestyle='none', label='% BrO <200m') # LTcol BrO                           # Error surf observations 

# Format x-axis
plt.xlim(datetime(2012,9,23),datetime(2012,11,12)) # SIPEXII (23 Sep - 11 Nov 2012)
xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax.tick_params(axis='x',pad=15)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.6)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(0,42)

# Plot the axis labels, legend and title
plt.title('SIPEXII (2012)', fontsize=15)
ax.set_ylabel('BrO (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
ax2.set_ylabel('BrO <200m (%)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#plt.legend(bbox_to_anchor=(0.85, 1.35), loc=2, borderaxespad=0.)

# added these three lines
lns = ln1+ln2+ln3
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, bbox_to_anchor=(1.02, 1.0), loc=2)
