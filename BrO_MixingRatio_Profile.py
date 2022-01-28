#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:23:17 2018

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
from matplotlib.ticker import MaxNLocator, AutoMinorLocator

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import signal, stats

# Date and Time handling package
import datetime as dt
from datetime import datetime,time, timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# OBSERVATIONS
# Retrieve the observational data

#---------------------------------
# V1_17 Davis (14-22 Nov 2017)
#---------------------------------

# BrO VMR
V1_2017 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2017/18)

# BrO Error
V1_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/BrO_error/V1_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2017/18)

# Calculate the Relative Error (>=0.6)
Filter = V1_Error / V1_2017

# Apply the filter
V1_17F = Filter < 0.6
V1_17T = V1_2017[V1_17F]

#---------------------------------
# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
#---------------------------------

V2_2017 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V2 (2017/18)

# BrO Error
V2_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/BrO_error/V2_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V2 (2017/18)

# Calculate the Relative Error (>=0.6)
Filter = V2_Error / V2_2017

# Apply the filter
V2_17F = Filter < 0.6
V2_17T = V2_2017[V2_17F]

#---------------------------------
# V3_17 Mawson (1-17 Feb 2018)
#---------------------------------

# BrO VMR
V3_2017 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V3 (2017/18)

# BrO Error
V3_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/BrO_error/V3_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V3 (2017/18)

# Calculate the Relative Error (>=0.6)
Filter = V3_Error / V3_2017

# Apply the filter
V3_17F = Filter < 0.6
V3_17T = V3_2017[V3_17F]

#---------------------------------
# V1_18 Davis (7-15 Nov 2018)
#---------------------------------

# BrO VMR
V1_2018 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)

# BrO Error
V1_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/BrO_error/V1_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2018/19)

# Calculate the Relative Error (>=0.6)
Filter = V1_Error / V1_2018

# Apply the filter
V1_18F = Filter < 0.6
V1_18T = V1_2018[V1_18F]

#---------------------------------
# V2_18 Casey (15-30 Dec 2018)
#---------------------------------

# BrO VMR
V2_2018 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V2 (2018/19)

# BrO Error
V2_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/BrO_error/V2_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V2 (2017/18)

# Calculate the Relative Error (>=0.6)
Filter = V2_Error / V2_2018

# Apply the filter
V2_18F = Filter < 0.6
V2_18T = V2_2018[V2_18F]

#---------------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#---------------------------------

# BrO VMR
V3_2018 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V3 (2018/19)

# BrO Error
V3_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/BrO_error/V3_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2017/18)

# Calculate the Relative Error (>=0.6)
Filter = V3_Error / V3_2018

# Apply the filter
V3_18F = Filter < 0.6
V3_18T = V3_2018[V3_18F]

#---------------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#---------------------------------

# BrO VMR
SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_VMR.csv',index_col=0) # BrO data for SIPEXII (2012)

# BrO Error
SIPEXII_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/BrO_error/SIPEXII_BrO_error.csv', index_col=0) # BrO error data for SIPEXII (2012)

# Calculate the Relative Error (>=0.6)
Filter = SIPEXII_Error / SIPEXII

# Apply the filter
SIPEXIIF = Filter < 0.6
SIPEXIIT = SIPEXII[SIPEXIIF]

#------------------------------------------------------------------------------
# Set the date

V1_17T.columns   = (pd.to_datetime(V1_17T.columns)+ timedelta(hours=7)) # Davis timezone is UT+7
V2_17T.columns   = (pd.to_datetime(V2_17T.columns)+ timedelta(hours=8)) # Casey timezone is UT+8
V3_17T.columns   = (pd.to_datetime(V3_17T.columns)+ timedelta(hours=5)) # Mawson timezone is UT+5
V1_18T.columns   = (pd.to_datetime(V1_18T.columns)+ timedelta(hours=7)) # Davis timezone is UT+7
V2_18T.columns   = (pd.to_datetime(V2_18T.columns)+ timedelta(hours=8)) # Casey timezone is UT+8
V3_18T.columns   = (pd.to_datetime(V3_18T.columns)+ timedelta(hours=5)) # Mawson timezone is UT+5
SIPEXIIT.columns = (pd.to_datetime(SIPEXIIT.columns)+ timedelta(hours=8)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# Transpose the dataframe

V1_17TT   = V1_17T.T
V2_17TT   = V2_17T.T
V3_17TT   = V3_17T.T
V1_18TT   = V1_18T.T
V2_18TT   = V2_18T.T
V3_18TT   = V3_18T.T
SIPEXIITT = SIPEXIIT.T

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

## V1_17 Davis (07:00 to 18:00)
#start_time = '07:00:00'
#end_time = '18:00:00'
#Midday = (V1_2017_T['Time'] > start_time) & (V1_2017_T['Time'] < end_time)
#V1_2017_T = V1_2017_T[Midday]
#V1_2017 = V1_2017_T.T

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# V1_17 Davis (14-22 Nov 2017)
start_date = '2017-11-14'
end_date = '2017-11-23'
Davis = (V1_17TT.index >= start_date) & (V1_17TT.index < end_date)
V1_17M = V1_17TT[Davis]

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1 = '2017-12-21'
end_date1 = '2017-12-23'
start_date2 = '2017-12-26'
end_date2 = '2018-01-6'
Casey1 = (V2_17TT.index >= start_date1) & (V2_17TT.index < end_date1)
Casey2 = (V2_17TT.index >= start_date2) & (V2_17TT.index < end_date2)
V2_17_Casey1 = V2_17TT[Casey1]
V2_17_Casey2 = V2_17TT[Casey2]
V2_17M = pd.concat([V2_17_Casey1,V2_17_Casey2], axis =0)

# V3_17 Davis (27-30 Jan 2018 and 19-21 Feb 2018)
start_date1 = '2018-01-27'
end_date1 = '2018-01-31'
start_date2 = '2018-02-19'
end_date2 = '2018-02-22'
Davis1 = (V3_17TT.index >= start_date1) & (V3_17TT.index < end_date1)
Davis2 = (V3_17TT.index >= start_date2) & (V3_17TT.index < end_date2)
V3_17_Davis1 = V3_17TT[Davis1]
V3_17_Davis2 = V3_17TT[Davis2]
V3_17M = pd.concat([V3_17_Davis1,V3_17_Davis2], axis =0)

# V1_18 Davis (7-15 Nov 2018)
start_date = '2018-11-07'
end_date = '2018-11-16'
Davis = (V1_18TT.index >= start_date) & (V1_18TT.index < end_date)
V1_18M = V1_18TT[Davis]

# V2_18 Casey (15-30 Dec 2018)
start_date = '2018-12-15'
end_date = '2018-12-31'
Casey = (V2_18TT.index >= start_date) & (V2_18TT.index < end_date)
V2_18M = V2_18TT[Casey]

# V3_18 Davis (26-28 Jan 2019 and 19-20 Feb 2019)
start_date1 = '2019-01-26'
end_date1 = '2019-01-29'
start_date2 = '2019-02-19'
end_date2 = '2019-02-21'
Davis1 = (V3_18TT.index >= start_date1) & (V3_18TT.index < end_date1)
Davis2 = (V3_18TT.index >= start_date2) & (V3_18TT.index < end_date2)
V3_18_Davis1 = V3_18TT[Davis1]
V3_18_Davis2 = V3_18TT[Davis2]
V3_18M = pd.concat([V3_17_Davis1,V3_17_Davis2], axis =0)

# SIPEXII (23 Sep to 11 Nov 2012)
start_date = '2012-09-23'
end_date = '2012-11-11'
SIPEX = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
SIPEXIIM = SIPEXIITT[SIPEX]

#------------------------------------------------------------------------------
# Transpose the dataframe back again

V1_17TT   = V1_17M.T
V2_17TT   = V2_17M.T
V3_17TT   = V3_17M.T
V1_18TT   = V1_18M.T
V2_18TT   = V2_18M.T
V3_18TT   = V3_18M.T
SIPEXIITT = SIPEXIIM.T

#------------------------------------------------------------------------------
# Calculate the mean/median BrO VCD for each altitude 

#---------
# MEAN (All)
#---------
Mean_V1_17   = np.mean(V1_17T,   axis=1) * 1e6
Mean_V2_17   = np.mean(V2_17T,   axis=1) * 1e6
Mean_V3_17   = np.mean(V3_17T,   axis=1) * 1e6
Mean_V1_18   = np.mean(V1_18T,   axis=1) * 1e6
Mean_V2_18   = np.mean(V2_18T,   axis=1) * 1e6
Mean_V3_18   = np.mean(V3_18T,   axis=1) * 1e6
Mean_SIPEXII = np.mean(SIPEXIIT, axis=1) * 1e6

#---------
# MEDIAN (All)
#---------
Median_V1_17   = np.nanmedian(V1_17T,   axis=1) * 1e6
Median_V2_17   = np.nanmedian(V2_17T,   axis=1) * 1e6
Median_V3_17   = np.nanmedian(V3_17T,   axis=1) * 1e6
Median_V1_18   = np.nanmedian(V1_18T,   axis=1) * 1e6
Median_V2_18   = np.nanmedian(V2_18T,   axis=1) * 1e6
Median_V3_18   = np.nanmedian(V3_18T,   axis=1) * 1e6
Median_SIPEXII = np.nanmedian(SIPEXIIT, axis=1) * 1e6

#---------
# MEAN (Station)
#---------
Mean_V1_17S   = np.mean(V1_17TT,   axis=1) * 1e6
Mean_V2_17S   = np.mean(V2_17TT,   axis=1) * 1e6
Mean_V3_17S   = np.mean(V3_17TT,   axis=1) * 1e6
Mean_V1_18S   = np.mean(V1_18TT,   axis=1) * 1e6
Mean_V2_18S   = np.mean(V2_18TT,   axis=1) * 1e6
Mean_V3_18S   = np.mean(V3_18TT,   axis=1) * 1e6
Mean_SIPEXIIS = np.mean(SIPEXIITT, axis=1) * 1e6

#---------
# MEDIAN (Station)
#---------
Median_V1_17S   = np.nanmedian(V1_17TT,   axis=1) * 1e6
Median_V2_17S   = np.nanmedian(V2_17TT,   axis=1) * 1e6
Median_V3_17S   = np.nanmedian(V3_17TT,   axis=1) * 1e6
Median_V1_18S   = np.nanmedian(V1_18TT,   axis=1) * 1e6
Median_V2_18S   = np.nanmedian(V2_18TT,   axis=1) * 1e6
Median_V3_18S   = np.nanmedian(V3_18TT,   axis=1) * 1e6
Median_SIPEXIIS = np.nanmedian(SIPEXIITT, axis=1) * 1e6

#------------------------------------------------------------------------------
# Calculate the StDev/MAD for each altitude 

#---------
# StDev (All)
#---------
StDev_V1_17   = np.std(V1_17T,   axis=1) * 1e6
StDev_V2_17   = np.std(V2_17T,   axis=1) * 1e6
StDev_V3_17   = np.std(V3_17T,   axis=1) * 1e6
StDev_V1_18   = np.std(V1_18T,   axis=1) * 1e6
StDev_V2_18   = np.std(V2_18T,   axis=1) * 1e6
StDev_V3_18   = np.std(V3_18T,   axis=1) * 1e6
StDev_SIPEXII = np.std(SIPEXIIT, axis=1) * 1e6

#---------
# MAD (All)
#---------
MAD_V1_17   = V1_17T.mad(axis=1,   skipna='True') * 1e6
MAD_V2_17   = V2_17T.mad(axis=1,   skipna='True') * 1e6
MAD_V3_17   = V3_17T.mad(axis=1,   skipna='True') * 1e6
MAD_V1_18   = V1_18T.mad(axis=1,   skipna='True') * 1e6
MAD_V2_18   = V2_18T.mad(axis=1,   skipna='True') * 1e6
MAD_V3_18   = V3_18T.mad(axis=1,   skipna='True') * 1e6
MAD_SIPEXII = SIPEXIIT.mad(axis=1, skipna='True') * 1e6

#---------
# StDev (Station)
#---------
StDev_V1_17S   = np.std(V1_17TT,   axis=1) * 1e6
StDev_V2_17S   = np.std(V2_17TT,   axis=1) * 1e6
StDev_V3_17S   = np.std(V3_17TT,   axis=1) * 1e6
StDev_V1_18S   = np.std(V1_18TT,   axis=1) * 1e6
StDev_V2_18S   = np.std(V2_18TT,   axis=1) * 1e6
StDev_V3_18S   = np.std(V3_18TT,   axis=1) * 1e6
StDev_SIPEXIIS = np.std(SIPEXIITT, axis=1) * 1e6

#---------
# MAD (Station)
#---------
MAD_V1_17S   = V1_17TT.mad(axis=1,   skipna='True') * 1e6
MAD_V2_17S   = V2_17TT.mad(axis=1,   skipna='True') * 1e6
MAD_V3_17S   = V3_17TT.mad(axis=1,   skipna='True') * 1e6
MAD_V1_18S   = V1_18TT.mad(axis=1,   skipna='True') * 1e6
MAD_V2_18S   = V2_18TT.mad(axis=1,   skipna='True') * 1e6
MAD_V3_18S   = V3_18TT.mad(axis=1,   skipna='True') * 1e6
MAD_SIPEXIIS = SIPEXIITT.mad(axis=1, skipna='True') * 1e6

#------------------------------------------------------------------------------
# Build new dataframes for the mean/median

#---------
# MEAN (All)
#---------
Mean_all = np.column_stack((Mean_V1_17, Mean_V2_17, Mean_V3_17, Mean_V1_18, Mean_V2_18, Mean_V3_18, Mean_SIPEXII, Mean_SIPEXII))
Mean_all = pd.DataFrame.from_dict(Mean_all)
Mean_all.columns = ['V1_17', 'V2_17', 'V3_17', 'V1_18', 'V2_18', 'V3_18', 'SIPEXII','']
Mean_all.index = ['0.1','0.3','0.5','0.7','0.9','1.1','1.3','1.5','1.7','1.9','2.1','2.3','2.5','2.7','2.9','3.1','3.3','3.5','3.7','3.9']

#---------
# MEDIAN (All)
#---------
Median_all = np.column_stack((Median_V1_17, Median_V2_17, Median_V3_17, Median_V1_18, Median_V2_18, Median_V3_18, Median_SIPEXII, Median_SIPEXII))
Median_all = pd.DataFrame.from_dict(Median_all)
Median_all.columns = ['V1_17', 'V2_17', 'V3_17', 'V1_18', 'V2_18', 'V3_18', 'SIPEXII','']
Median_all.index = ['0.1','0.3','0.5','0.7','0.9','1.1','1.3','1.5','1.7','1.9','2.1','2.3','2.5','2.7','2.9','3.1','3.3','3.5','3.7','3.9']

#---------
# MEAN (Station)
#---------
Mean_allS = np.column_stack((Mean_V1_17S, Mean_V2_17S, Mean_V3_17S, Mean_V1_18S, Mean_V2_18S, Mean_V3_18S, Mean_SIPEXIIS, Mean_SIPEXIIS))
Mean_allS = pd.DataFrame.from_dict(Mean_allS)
Mean_allS.columns = ['V1_17', 'V2_17', 'V3_17', 'V1_18', 'V2_18', 'V3_18', 'SIPEXII','']
Mean_allS.index = ['0.1','0.3','0.5','0.7','0.9','1.1','1.3','1.5','1.7','1.9','2.1','2.3','2.5','2.7','2.9','3.1','3.3','3.5','3.7','3.9']

#---------
# MEDIAN (Station)
#---------
Median_allS = np.column_stack((Median_V1_17S, Median_V2_17S, Median_V3_17S, Median_V1_18S, Median_V2_18S, Median_V3_18S, Median_SIPEXIIS, Median_SIPEXIIS))
Median_allS = pd.DataFrame.from_dict(Median_allS)
Median_allS.columns = ['V1_17', 'V2_17', 'V3_17', 'V1_18', 'V2_18', 'V3_18', 'SIPEXII','']
Median_allS.index = ['0.1','0.3','0.5','0.7','0.9','1.1','1.3','1.5','1.7','1.9','2.1','2.3','2.5','2.7','2.9','3.1','3.3','3.5','3.7','3.9']

#------------------------------------------------------------------------------
# PLOT THE BrO MIXING RATIO PROFILE

fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1 (MEAN BrO)
ax = plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

cmap=plt.cm.jet
norm = BoundaryNorm(np.arange(0,5.25,0.25), cmap.N)

# Mean
ax.errorbar(Mean_V1_17S,   Mean_V1_17S.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='V1 (2017/18)',   xerr=StDev_V1_17S,   capsize=2)
ax.errorbar(Mean_V2_17S,   Mean_V2_17S.index,   marker='o', c='red',    markersize = 3.0, ls='-', label ='V2 (2017/18)',   xerr=StDev_V2_17S,   capsize=2)
ax.errorbar(Mean_V3_17S,   Mean_V3_17S.index,   marker='o', c='blue',   markersize = 3.0, ls='-', label ='V3 (2017/18)',   xerr=StDev_V3_17S,   capsize=2)
ax.errorbar(Mean_V1_18S,   Mean_V1_18S.index,   marker='o', c='green',  markersize = 3.0, ls='-', label ='V1 (2018/19)',   xerr=StDev_V1_18S,   capsize=2)
ax.errorbar(Mean_V2_18S,   Mean_V2_18S.index,   marker='o', c='yellow', markersize = 3.0, ls='-', label ='V2 (2018/19)',   xerr=StDev_V2_18S,   capsize=2)
ax.errorbar(Mean_V3_18S,   Mean_V3_18S.index,   marker='o', c='purple', markersize = 3.0, ls='-', label ='V3 (2018/19)',   xerr=StDev_V3_18S,   capsize=2)
ax.errorbar(Mean_SIPEXIIS, Mean_SIPEXIIS.index, marker='o', c='cyan',   markersize = 3.0, ls='-', label ='SIPEXII (2012)', xerr=StDev_SIPEXIIS, capsize=2)

ax.set_ylabel('Altitude (km)', fontsize=20)
ax.set_xlabel('BrO (pptv)', fontsize=20)

# Plot Title
plt.title('Mean BrO Mixing Ratio Profile', fontsize=25, pad=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,5.0)
ax.xaxis.labelpad = 10

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.7)
ax.yaxis.labelpad = 10

# Format axis labels
ax.tick_params(labelsize=15)

#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper right', fontsize=15)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

plt.show()

#------------------------------
# Graph 2 (MEDIAN BrO)
ax = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

cmap=plt.cm.jet
norm = BoundaryNorm(np.arange(0,5.25,0.25), cmap.N)

# Median
ax.errorbar(Median_V1_17S,   Mean_V1_17S.index,   marker='o', c='black',  markersize = 3.0, ls='-', label ='V1 (2017/18)',   xerr=MAD_V1_17S,   capsize=2)
ax.errorbar(Median_V2_17S,   Mean_V2_17S.index,   marker='o', c='red',    markersize = 3.0, ls='-', label ='V2 (2017/18)',   xerr=MAD_V2_17S,   capsize=2)
ax.errorbar(Median_V3_17S,   Mean_V3_17S.index,   marker='o', c='blue',   markersize = 3.0, ls='-', label ='V3 (2017/18)',   xerr=MAD_V3_17S,   capsize=2)
ax.errorbar(Median_V1_18S,   Mean_V1_18S.index,   marker='o', c='green',  markersize = 3.0, ls='-', label ='V1 (2018/19)',   xerr=MAD_V1_18S,   capsize=2)
ax.errorbar(Median_V2_18S,   Mean_V2_18S.index,   marker='o', c='yellow', markersize = 3.0, ls='-', label ='V2 (2018/19)',   xerr=MAD_V2_18S,   capsize=2)
ax.errorbar(Median_V3_18S,   Mean_V3_18S.index,   marker='o', c='purple', markersize = 3.0, ls='-', label ='V3 (2018/19)',   xerr=MAD_V3_18S,   capsize=2)
ax.errorbar(Median_SIPEXIIS, Mean_SIPEXIIS.index, marker='o', c='cyan',   markersize = 3.0, ls='-', label ='SIPEXII (2012)', xerr=MAD_SIPEXIIS, capsize=2)

ax.set_ylabel('Altitude (km)', fontsize=20)
ax.set_xlabel('BrO (pptv)', fontsize=20)

# Plot Title
plt.title('Median BrO Mixing Ratio Profile', fontsize=25, pad=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,5.0)
ax.xaxis.labelpad = 10

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2.7)
ax.yaxis.labelpad = 10

# Format axis labels
ax.tick_params(labelsize=15)

#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper right', fontsize=15)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

plt.show()