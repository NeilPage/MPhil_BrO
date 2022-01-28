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

# V1_17 (2017-18)
V1_17_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_17_Data.csv',header=0,encoding = 'unicode_escape')
V1_17_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2017/18)
V1_17_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/BrO_error/V1_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2017/18)
V1_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv')
V1_17_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv')
V1_17_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv')
V1_17_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv')

# V2_17 (2017-18)
V2_17_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_17_Data.csv',header=0,encoding = 'unicode_escape')
V2_17_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V2 (2017/18)
V2_17_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/BrO_error/V2_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V2 (2017/18)
V2_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv')
V2_17_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv')
V2_17_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv')
V2_17_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv')

# V3_17 (2017-18)
V3_17_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_17_Data.csv',header=0,encoding = 'unicode_escape')
V3_17_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V3 (2017/18)
V3_17_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/BrO_error/V3_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V3 (2017/18)
V3_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv')
V3_17_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv')
V3_17_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv')
V3_17_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv')

# V1_18 (2018-19)
V1_18_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_18_Data.csv',header=0,encoding = 'unicode_escape')
V1_18_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)
V1_18_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/BrO_error/V1_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2018/19)
V1_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv')
V1_18_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv')
V1_18_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv')
V1_18_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V1_O3_1min.csv')

# V2_18 (2018-19)
V2_18_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_18_Data.csv',header=0,encoding = 'unicode_escape')
V2_18_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V2 (2018/19)
V2_18_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/BrO_error/V2_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V2 (2018/19)
V2_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv')
V2_18_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv')
V2_18_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv')
V2_18_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V2_O3_1min.csv')

# V3_18 (2018-19)
V3_18_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_18_Data.csv',header=0,encoding = 'unicode_escape')
V3_18_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V3 (2018/19)
V3_18_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/BrO_error/V3_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V3 (2018/19)
V3_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv')
V3_18_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv')
V3_18_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv')
V3_18_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V3_O3_1min.csv')

#------------------------------------------------------------------------------
# Calculate the Relative Error (>=0.6)

# Define the filter
Filter_V1_17   = V1_17_Error   / V1_17_VMR
Filter_V2_17   = V2_17_Error   / V2_17_VMR
Filter_V3_17   = V3_17_Error   / V3_17_VMR
Filter_V1_18   = V1_18_Error   / V1_18_VMR
Filter_V2_18   = V2_18_Error   / V2_18_VMR
Filter_V3_18   = V3_18_Error   / V3_18_VMR

# Apply the filter
V1_17F      = Filter_V1_17 < 0.6
V1_17_VMR   = V1_17_VMR[V1_17F]

V2_17F      = Filter_V2_17 < 0.6
V2_17_VMR   = V2_17_VMR[V2_17F]

V3_17F      = Filter_V3_17 < 0.6
V3_17_VMR   = V3_17_VMR[V3_17F]

V1_18F      = Filter_V1_18 < 0.6
V1_18_VMR   = V1_18_VMR[V1_18F]

V2_18F      = Filter_V2_18 < 0.6
V2_18_VMR   = V2_18_VMR[V2_18F]

V3_18F      = Filter_V3_18 < 0.6
V3_18_VMR   = V3_18_VMR[V3_18F]

#------------------------------------------------------------------------------
# Set the date

# V1_17 (2017-18)
V1_17_BrO['DateTime']   = pd.to_datetime(V1_17_BrO['DateTime'], dayfirst=True)
V1_17_VMR.columns       = (pd.to_datetime(V1_17_VMR.columns, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
V1_17_Met['DateTime']   = pd.to_datetime(V1_17_Met['DateTime'], dayfirst=True)
V1_17_SI['DateTime']    = pd.to_datetime(V1_17_SI['DateTime'],  dayfirst=True)
V1_17_Hg['DateTime']    = pd.to_datetime(V1_17_Hg['DateTime'],  dayfirst=True)
V1_17_O3['DateTime']    = pd.to_datetime(V1_17_O3['DateTime'],  dayfirst=True)

# V2_17 (2017-18)
V2_17_BrO['DateTime']   = pd.to_datetime(V2_17_BrO['DateTime'], dayfirst=True)
V2_17_VMR.columns       = (pd.to_datetime(V2_17_VMR.columns, dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
V2_17_Met['DateTime']   = pd.to_datetime(V2_17_Met['DateTime'], dayfirst=True)
V2_17_SI['DateTime']    = pd.to_datetime(V2_17_SI['DateTime'],  dayfirst=True)
V2_17_Hg['DateTime']    = pd.to_datetime(V2_17_Hg['DateTime'],  dayfirst=True)
V2_17_O3['DateTime']    = pd.to_datetime(V2_17_O3['DateTime'],  dayfirst=True)

# V3_17 (2017-18)
V3_17_BrO['DateTime']   = pd.to_datetime(V3_17_BrO['DateTime'], dayfirst=True)
V3_17_VMR.columns       = (pd.to_datetime(V3_17_VMR.columns, dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
V3_17_Met['DateTime']   = pd.to_datetime(V3_17_Met['DateTime'], dayfirst=True)
V3_17_SI['DateTime']    = pd.to_datetime(V3_17_SI['DateTime'],  dayfirst=True)
V3_17_Hg['DateTime']    = pd.to_datetime(V3_17_Hg['DateTime'],  dayfirst=True)
V3_17_O3['DateTime']    = pd.to_datetime(V3_17_O3['DateTime'],  dayfirst=True)

# V1_18 (2018-19)
V1_18_BrO['DateTime']   = pd.to_datetime(V1_18_BrO['DateTime'], dayfirst=True)
V1_18_VMR.columns       = (pd.to_datetime(V1_18_VMR.columns, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
V1_18_Met['DateTime']   = pd.to_datetime(V1_18_Met['DateTime'], dayfirst=True)
V1_18_SI['DateTime']    = pd.to_datetime(V1_18_SI['DateTime'],  dayfirst=True)
V1_18_Hg['DateTime']    = pd.to_datetime(V1_18_Hg['DateTime'],  dayfirst=True)
V1_18_O3['DateTime']    = pd.to_datetime(V1_18_O3['DateTime'],  dayfirst=True)

# V2_18 (2018-19)
V2_18_BrO['DateTime']   = pd.to_datetime(V2_18_BrO['DateTime'], dayfirst=True)
V2_18_VMR.columns       = (pd.to_datetime(V2_18_VMR.columns, dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
V2_18_Met['DateTime']   = pd.to_datetime(V2_18_Met['DateTime'], dayfirst=True)
V2_18_SI['DateTime']    = pd.to_datetime(V2_18_SI['DateTime'],  dayfirst=True)
V2_18_Hg['DateTime']    = pd.to_datetime(V2_18_Hg['DateTime'],  dayfirst=True)
V2_18_O3['DateTime']    = pd.to_datetime(V2_18_O3['DateTime'],  dayfirst=True)

# V3_18 (2018-19)
V3_18_BrO['DateTime']   = pd.to_datetime(V3_18_BrO['DateTime'], dayfirst=True)
V3_18_VMR.columns       = (pd.to_datetime(V3_18_VMR.columns, dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
V3_18_Met['DateTime']   = pd.to_datetime(V3_18_Met['DateTime'], dayfirst=True)
V3_18_SI['DateTime']    = pd.to_datetime(V3_18_SI['DateTime'],  dayfirst=True)
V3_18_Hg['DateTime']    = pd.to_datetime(V3_18_Hg['DateTime'],  dayfirst=True)
V3_18_O3['DateTime']    = pd.to_datetime(V3_18_O3['DateTime'],  dayfirst=True)

#------------------------------------------------------------------------------
# Transpose the VMR dataframes

V1_17TT   = V1_17_VMR.T
V2_17TT   = V2_17_VMR.T
V3_17TT   = V3_17_VMR.T
V1_18TT   = V1_18_VMR.T
V2_18TT   = V2_18_VMR.T
V3_18TT   = V3_18_VMR.T

#------------------------------------------------------------------------------
# Add columns for DateTime, Date and Time

# DateTime
V1_17TT['DateTime']   = V1_17TT.index
V2_17TT['DateTime']   = V2_17TT.index
V3_17TT['DateTime']   = V3_17TT.index
V1_18TT['DateTime']   = V1_18TT.index
V2_18TT['DateTime']   = V2_18TT.index
V3_18TT['DateTime']   = V3_18TT.index

# Date
V1_17TT['Date']   = V1_17TT['DateTime'].dt.date
V2_17TT['Date']   = V2_17TT['DateTime'].dt.date
V3_17TT['Date']   = V3_17TT['DateTime'].dt.date
V1_18TT['Date']   = V1_18TT['DateTime'].dt.date
V2_18TT['Date']   = V2_18TT['DateTime'].dt.date
V3_18TT['Date']   = V3_18TT['DateTime'].dt.date

# Time
V1_17TT['Time']   = V1_17TT['DateTime'].dt.time
V2_17TT['Time']   = V2_17TT['DateTime'].dt.time
V3_17TT['Time']   = V3_17TT['DateTime'].dt.time
V1_18TT['Time']   = V1_18TT['DateTime'].dt.time
V2_18TT['Time']   = V2_18TT['DateTime'].dt.time
V3_18TT['Time']   = V3_18TT['DateTime'].dt.time

#------------------------------------------------------------------------------
# set datetime as the index

# V1_17 (2017-18)
V1_17_BrO   = V1_17_BrO.set_index('DateTime')
V1_17_Met   = V1_17_Met.set_index('DateTime')
V1_17_SI    = V1_17_SI.set_index('DateTime')
V1_17_Hg    = V1_17_Hg.set_index('DateTime')
V1_17_O3    = V1_17_O3.set_index('DateTime')

# V2_17 (2017-18)
V2_17_BrO   = V2_17_BrO.set_index('DateTime')
V2_17_Met   = V2_17_Met.set_index('DateTime')
V2_17_SI    = V2_17_SI.set_index('DateTime')
V2_17_Hg    = V2_17_Hg.set_index('DateTime')
V2_17_O3    = V2_17_O3.set_index('DateTime')

# V3_17 (2017-18)
V3_17_BrO   = V3_17_BrO.set_index('DateTime')
V3_17_Met   = V3_17_Met.set_index('DateTime')
V3_17_SI    = V3_17_SI.set_index('DateTime')
V3_17_Hg    = V3_17_Hg.set_index('DateTime')
V3_17_O3    = V3_17_O3.set_index('DateTime')

# V1_18 (2018-19)
V1_18_BrO   = V1_18_BrO.set_index('DateTime')
V1_18_Met   = V1_18_Met.set_index('DateTime')
V1_18_SI    = V1_18_SI.set_index('DateTime')
V1_18_Hg    = V1_18_Hg.set_index('DateTime')
V1_18_O3    = V1_18_O3.set_index('DateTime')

# V2_18 (2018-19)
V2_18_BrO   = V2_18_BrO.set_index('DateTime')
V2_18_Met   = V2_18_Met.set_index('DateTime')
V2_18_SI    = V2_18_SI.set_index('DateTime')
V2_18_Hg    = V2_18_Hg.set_index('DateTime')
V2_18_O3    = V2_18_O3.set_index('DateTime')

# V3_18 (2018-19)
V3_18_BrO   = V3_18_BrO.set_index('DateTime')
V3_18_Met   = V3_18_Met.set_index('DateTime')
V3_18_SI    = V3_18_SI.set_index('DateTime')
V3_18_Hg    = V3_18_Hg.set_index('DateTime')
V3_18_O3    = V3_18_O3.set_index('DateTime')

#------------------------------------------------------------------------------
# Resample all data to 20 min averages

# V1_17 (2017-18)
V1_17_Met   = V1_17_Met.resample('20T').mean()
V1_17_SI    = V1_17_SI.resample('20T').mean()
V1_17_Hg    = V1_17_Hg.resample('20T').mean()
V1_17_O3    = V1_17_O3.resample('20T').mean()

# V2_17 (2017-18)
V2_17_Met   = V2_17_Met.resample('20T').mean()
V2_17_SI    = V2_17_SI.resample('20T').mean()
V2_17_Hg    = V2_17_Hg.resample('20T').mean()
V2_17_O3    = V2_17_O3.resample('20T').mean()

# V3_17 (2017-18)
V3_17_Met   = V3_17_Met.resample('20T').mean()
V3_17_SI    = V3_17_SI.resample('20T').mean()
V3_17_Hg    = V3_17_Hg.resample('20T').mean()
V3_17_O3    = V3_17_O3.resample('20T').mean()

# V1_18 (2018-19)
V1_18_Met   = V1_18_Met.resample('20T').mean()
V1_18_SI    = V1_18_SI.resample('20T').mean()
V1_18_Hg    = V1_18_Hg.resample('20T').mean()
V1_18_O3    = V1_18_O3.resample('20T').mean()

# V2_18 (2018-19)
V2_18_Met   = V2_18_Met.resample('20T').mean()
V2_18_SI    = V2_18_SI.resample('20T').mean()
V2_18_Hg    = V2_18_Hg.resample('20T').mean()
V2_18_O3    = V2_18_O3.resample('20T').mean()

# V3_18 (2018-19)
V3_18_Met   = V3_18_Met.resample('20T').mean()
V3_18_SI    = V3_18_SI.resample('20T').mean()
V3_18_Hg    = V3_18_Hg.resample('20T').mean()
V3_18_O3    = V3_18_O3.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

# V1_17 (2017-18)
V1_17_Met.index   = V1_17_Met.index   - pd.Timedelta(minutes=10)
V1_17_SI.index    = V1_17_SI.index    - pd.Timedelta(minutes=10)
V1_17_Hg.index    = V1_17_Hg.index    - pd.Timedelta(minutes=10)
V1_17_O3.index    = V1_17_O3.index    - pd.Timedelta(minutes=10)

# V2_17 (2017-18)
V2_17_Met.index   = V2_17_Met.index   - pd.Timedelta(minutes=10)
V2_17_SI.index    = V2_17_SI.index    - pd.Timedelta(minutes=10)
V2_17_Hg.index    = V2_17_Hg.index    - pd.Timedelta(minutes=10)
V2_17_O3.index    = V2_17_O3.index    - pd.Timedelta(minutes=10)

# V3_17 (2017-18)
V3_17_Met.index   = V3_17_Met.index   - pd.Timedelta(minutes=10)
V3_17_SI.index    = V3_17_SI.index    - pd.Timedelta(minutes=10)
V3_17_Hg.index    = V3_17_Hg.index    - pd.Timedelta(minutes=10)
V3_17_O3.index    = V3_17_O3.index    - pd.Timedelta(minutes=10)

# V1_18 (2018-19)
V1_18_Met.index   = V1_18_Met.index   - pd.Timedelta(minutes=10)
V1_18_SI.index    = V1_18_SI.index    - pd.Timedelta(minutes=10)
V1_18_Hg.index    = V1_18_Hg.index    - pd.Timedelta(minutes=10)
V1_18_O3.index    = V1_18_O3.index    - pd.Timedelta(minutes=10)

# V2_18 (2018-19)
V2_18_Met.index   = V2_18_Met.index   - pd.Timedelta(minutes=10)
V2_18_SI.index    = V2_18_SI.index    - pd.Timedelta(minutes=10)
V2_18_Hg.index    = V2_18_Hg.index    - pd.Timedelta(minutes=10)
V2_18_O3.index    = V2_18_O3.index    - pd.Timedelta(minutes=10)

# V3_18 (2018-19)
V3_18_Met.index   = V3_18_Met.index   - pd.Timedelta(minutes=10)
V3_18_SI.index    = V3_18_SI.index    - pd.Timedelta(minutes=10)
V3_18_Hg.index    = V3_18_Hg.index    - pd.Timedelta(minutes=10)
V3_18_O3.index    = V3_18_O3.index    - pd.Timedelta(minutes=10)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

#-----------------------
# V1_17 (07:00 to 18:00)
#-----------------------
# BrO
start_time = '07:00:00'
end_time   = '18:00:00'
Midday_BrO = (V1_17_BrO['Time'] >= start_time) & (V1_17_BrO['Time'] < end_time)
V1_17_MM   = V1_17_BrO[Midday_BrO]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V1_17TT['Time'] >= start_time) & (V1_17TT['Time'] < end_time)
V1_17M     = V1_17TT[Midday_VMR]

#-----------------------
# V2_17 (07:00 to 18:00)
#-----------------------
start_time = '07:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (V2_17_BrO['Time'] >= start_time) & (V2_17_BrO['Time'] < end_time)
V2_17_MM   = V2_17_BrO[Midday]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V2_17TT['Time'] >= start_time) & (V2_17TT['Time'] < end_time)
V2_17M     = V2_17TT[Midday_VMR]

#-----------------------
# V3_17 (07:00 to 18:00)
#-----------------------
start_time = '07:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (V3_17_BrO['Time'] >= start_time) & (V3_17_BrO['Time'] < end_time)
V3_17_MM   = V3_17_BrO[Midday]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V3_17TT['Time'] >= start_time) & (V3_17TT['Time'] < end_time)
V3_17M     = V3_17TT[Midday_VMR]

#-----------------------
# V1_18 (07:00 to 18:00)
#-----------------------
start_time = '07:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (V1_18_BrO['Time'] >= start_time) & (V1_18_BrO['Time'] < end_time)
V1_18_MM   = V1_18_BrO[Midday]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V1_18TT['Time'] >= start_time) & (V1_18TT['Time'] < end_time)
V1_18M     = V1_18TT[Midday_VMR]

#-----------------------
# V2_18 (07:00 to 18:00)
#-----------------------
start_time = '07:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (V2_18_BrO['Time'] >= start_time) & (V2_18_BrO['Time'] < end_time)
V2_18_MM   = V2_18_BrO[Midday]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V2_18TT['Time'] >= start_time) & (V2_18TT['Time'] < end_time)
V2_18M     = V2_18TT[Midday_VMR]

#-----------------------
# V3_18 (07:00 to 18:00)
#-----------------------
start_time = '07:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (V3_18_BrO['Time'] >= start_time) & (V3_18_BrO['Time'] < end_time)
V3_18_MM   = V3_18_BrO[Midday]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V3_18TT['Time'] >= start_time) & (V3_18TT['Time'] < end_time)
V3_18M     = V3_18TT[Midday_VMR]

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

# V1_17 (2017-18)
V1_17F   = (V1_17_MM['Filter'] < 0.6)
V1_17T   = V1_17_MM[V1_17F]

# V2_17 (2017-18)
V2_17F   = (V2_17_MM['Filter'] < 0.6)
V2_17T   = V2_17_MM[V2_17F]

# V3_17 (2017-18)
V3_17F   = (V3_17_MM['Filter'] < 0.6)
V3_17T   = V3_17_MM[V3_17F]

# V1_18 (2018-19)
V1_18F   = (V1_18_MM['Filter'] < 0.6)
V1_18T   = V1_18_MM[V1_18F]

# V2_18 (2018-19)
V2_18F   = (V2_18_MM['Filter'] < 0.6)
V2_18T   = V2_18_MM[V2_18F]

# V3_18 (2018-19)
V3_18F   = (V3_18_MM['Filter'] < 0.6)
V3_18T   = V3_18_MM[V3_18F]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# V1_17 Davis (14-22 Nov 2017)
start_date   = '2017-11-14'
end_date     = '2017-11-23'
# BrO
Davis_BrO    = (V1_17T.index >= start_date) & (V1_17T.index < end_date)
V1_17T       = V1_17T[Davis_BrO]
# VMR
Davis_VMR    = (V1_17M.index >= start_date) & (V1_17M.index < end_date)
V1_17M       = V1_17M[Davis_VMR]

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1  = '2017-12-21'
end_date1    = '2017-12-23'
start_date2  = '2017-12-26'
end_date2    = '2018-01-6'
# BrO
Casey1_BrO       = (V2_17T.index >= start_date1) & (V2_17T.index < end_date1)
Casey2_BrO       = (V2_17T.index >= start_date2) & (V2_17T.index < end_date2)
V2_17_Casey1_BrO = V2_17T[Casey1_BrO]
V2_17_Casey2_BrO = V2_17T[Casey2_BrO]
V2_17T           = pd.concat([V2_17_Casey1_BrO,V2_17_Casey2_BrO], axis =0)
# VMR
Casey1_VMR       = (V2_17M.index >= start_date1) & (V2_17M.index < end_date1)
Casey2_VMR       = (V2_17M.index >= start_date2) & (V2_17M.index < end_date2)
V2_17_Casey1_VMR = V2_17M[Casey1_VMR]
V2_17_Casey2_VMR = V2_17M[Casey2_VMR]
V2_17M           = pd.concat([V2_17_Casey1_VMR,V2_17_Casey2_VMR], axis =0)

# V3_17 Mawson (1-17 Feb 2018)
start_date   = '2018-02-01'
end_date     = '2018-02-18'
# BrO
Mawson_BrO   = (V3_17T.index >= start_date) & (V3_17T.index < end_date)
V3_17T       = V3_17T[Mawson_BrO]
# VMR
Mawson_VMR   = (V3_17M.index >= start_date) & (V3_17M.index < end_date)
V3_17M       = V3_17M[Mawson_VMR]

# V1_18 Davis (7-15 Nov 2018)
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# BrO
Davis_BrO    = (V1_18T.index >= start_date) & (V1_18T.index < end_date)
V1_18T       = V1_18T[Davis_BrO]
# VMR
Davis_VMR    = (V1_18M.index >= start_date) & (V1_18M.index < end_date)
V1_18M       = V1_18M[Davis_VMR]

# V2_18 Casey (15-30 Dec 2018)
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# BrO
Casey_BrO    = (V2_18T.index >= start_date) & (V2_18T.index < end_date)
V2_18T       = V2_18T[Casey_BrO]
# VMR
Casey_VMR    = (V2_18M.index >= start_date) & (V2_18M.index < end_date)
V2_18M       = V2_18M[Casey_VMR]

# V3_18 Mawson (30 Jan - 9 Feb 2019)
start_date   = '2019-01-30'
end_date     = '2019-02-10'
# BrO
Mawson_BrO   = (V3_18T.index >= start_date) & (V3_18T.index < end_date)
V3_18T       = V3_18T[Mawson_BrO]
# VMR
Mawson_VMR   = (V3_18M.index >= start_date) & (V3_18M.index < end_date)
V3_18M       = V3_18M[Mawson_VMR]

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

# V1_17 (2017-18)
D1_V1_17   = pd.merge(left=V1_17M,    right=V1_17_Met,    how='left', left_index=True, right_index=True)
D2_V1_17   = pd.merge(left=D1_V1_17,   right=V1_17_SI,    how='left', left_index=True, right_index=True)
D3_V1_17   = pd.merge(left=D2_V1_17,   right=V1_17_Hg,    how='left', left_index=True, right_index=True)
D4_V1_17   = pd.merge(left=D3_V1_17,   right=V1_17_O3,    how='left', left_index=True, right_index=True)

# V2_17 (2017-18)
D1_V2_17   = pd.merge(left=V2_17M,     right=V2_17_Met,   how='left', left_index=True, right_index=True)
D2_V2_17   = pd.merge(left=D1_V2_17,   right=V2_17_SI,    how='left', left_index=True, right_index=True)
D3_V2_17   = pd.merge(left=D2_V2_17,   right=V2_17_Hg,    how='left', left_index=True, right_index=True)
D4_V2_17   = pd.merge(left=D3_V2_17,   right=V2_17_O3,    how='left', left_index=True, right_index=True)

# V3_17 (2017-18)
D1_V3_17   = pd.merge(left=V3_17M,     right=V3_17_Met,   how='left', left_index=True, right_index=True)
D2_V3_17   = pd.merge(left=D1_V3_17,   right=V3_17_SI,    how='left', left_index=True, right_index=True)
D3_V3_17   = pd.merge(left=D2_V3_17,   right=V3_17_Hg,    how='left', left_index=True, right_index=True)
D4_V3_17   = pd.merge(left=D3_V3_17,   right=V3_17_O3,    how='left', left_index=True, right_index=True)

# V1_18 (2018-19)
D1_V1_18   = pd.merge(left=V1_18M,     right=V1_18_Met,   how='left', left_index=True, right_index=True)
D2_V1_18   = pd.merge(left=D1_V1_18,   right=V1_18_SI,    how='left', left_index=True, right_index=True)
D3_V1_18   = pd.merge(left=D2_V1_18,   right=V1_18_Hg,    how='left', left_index=True, right_index=True)
D4_V1_18   = pd.merge(left=D3_V1_18,   right=V1_18_O3,    how='left', left_index=True, right_index=True)

# V2_18 (2018-19)
D1_V2_18   = pd.merge(left=V2_18M,     right=V2_18_Met,   how='left', left_index=True, right_index=True)
D2_V2_18   = pd.merge(left=D1_V2_18,   right=V2_18_SI,    how='left', left_index=True, right_index=True)
D3_V2_18   = pd.merge(left=D2_V2_18,   right=V2_18_Hg,    how='left', left_index=True, right_index=True)
D4_V2_18   = pd.merge(left=D3_V2_18,   right=V2_18_O3,    how='left', left_index=True, right_index=True)

# V3_18 (2018-19)
D1_V3_18   = pd.merge(left=V3_18M,     right=V3_18_Met,   how='left', left_index=True, right_index=True)
D2_V3_18   = pd.merge(left=D1_V3_18,   right=V3_18_SI,    how='left', left_index=True, right_index=True)
D3_V3_18   = pd.merge(left=D2_V3_18,   right=V3_18_Hg,    how='left', left_index=True, right_index=True)
D4_V3_18   = pd.merge(left=D3_V3_18,   right=V3_18_O3,    how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Calculate the Wind Speed average

WS_s_V1_17           = np.array(D4_V1_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17           = np.array(D4_V1_17['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D4_V1_17['WS_Avg']   = (WS_s_V1_17 + WS_p_V1_17)/2 # Average the wind speed for port and starboard

WS_s_V2_17           = np.array(D4_V2_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17           = np.array(D4_V2_17['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D4_V2_17['WS_Avg']   = (WS_s_V2_17 + WS_p_V2_17)/2 # Average the wind speed for port and starboard

WS_s_V3_17           = np.array(D4_V3_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17           = np.array(D4_V3_17['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D4_V3_17['WS_Avg']   = (WS_s_V3_17 + WS_p_V3_17)/2 # Average the wind speed for port and starboard

WS_s_V1_18           = np.array(D4_V1_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18           = np.array(D4_V1_18['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D4_V1_18['WS_Avg']   = (WS_s_V1_18 + WS_p_V1_18)/2 # Average the wind speed for port and starboard

WS_s_V2_18           = np.array(D4_V2_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18           = np.array(D4_V2_18['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D4_V2_18['WS_Avg']   = (WS_s_V2_18 + WS_p_V2_18)/2 # Average the wind speed for port and starboard

WS_s_V3_18           = np.array(D4_V3_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18           = np.array(D4_V3_18['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D4_V3_18['WS_Avg']   = (WS_s_V3_18 + WS_p_V3_18)/2 # Average the wind speed for port and starboard

#------------------------------------------------------------------------------
# Seperate the data into low (<=7 m/s) and high (>7 m/s) wind speeds

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
V1_17_LWS   = (D4_V1_17['WS_Avg'] <= 7)
D4_V1_17L   = D4_V1_17[V1_17_LWS]

V2_17_LWS   = (D4_V2_17['WS_Avg'] <= 7)
D4_V2_17L   = D4_V2_17[V2_17_LWS]

V3_17_LWS   = (D4_V3_17['WS_Avg'] <= 7)
D4_V3_17L   = D4_V3_17[V3_17_LWS]

V1_18_LWS   = (D4_V1_18['WS_Avg'] <= 7)
D4_V1_18L   = D4_V1_18[V1_18_LWS]

V2_18_LWS   = (D4_V2_18['WS_Avg'] <= 7)
D4_V2_18L   = D4_V2_18[V2_18_LWS]

V3_18_LWS   = (D4_V3_18['WS_Avg'] <= 7)
D4_V3_18L   = D4_V3_18[V3_18_LWS]

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
V1_17_HWS   = (D4_V1_17['WS_Avg'] > 7)
D4_V1_17H   = D4_V1_17[V1_17_HWS]

V2_17_HWS   = (D4_V2_17['WS_Avg'] > 7)
D4_V2_17H   = D4_V2_17[V2_17_HWS]

V3_17_HWS   = (D4_V3_17['WS_Avg'] > 7)
D4_V3_17H   = D4_V3_17[V3_17_HWS]

V1_18_HWS   = (D4_V1_18['WS_Avg'] > 7)
D4_V1_18H   = D4_V1_18[V1_18_HWS]

V2_18_HWS   = (D4_V2_18['WS_Avg'] > 7)
D4_V2_18H   = D4_V2_18[V2_18_HWS]

V3_18_HWS   = (D4_V3_18['WS_Avg'] > 7)
D4_V3_18H   = D4_V3_18[V3_18_HWS]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover is >= 30%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17F1L   = (D4_V1_17L['Sea_Ice_Conc'] >= 0.3)
D4_V1_17L  = D4_V1_17L[V1_17F1L]

V2_17F1L   = (D4_V2_17L['Sea_Ice_Conc'] >= 0.3)
D4_V2_17L  = D4_V2_17L[V2_17F1L]

V3_17F1L   = (D4_V3_17L['Sea_Ice_Conc'] >= 0.3)
D4_V3_17L  = D4_V3_17L[V3_17F1L]

V1_18F1L   = (D4_V1_18L['Sea_Ice_Conc'] >= 0.3)
D4_V1_18L  = D4_V1_18L[V1_18F1L]

V2_18F1L   = (D4_V2_18L['Sea_Ice_Conc'] >= 0.3)
D4_V2_18L  = D4_V2_18L[V2_18F1L]

V3_18F1L   = (D4_V3_18L['Sea_Ice_Conc'] >= 0.3)
D4_V3_18L  = D4_V3_18L[V3_18F1L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17F1H   = (D4_V1_17H['Sea_Ice_Conc'] >= 0.3)
D4_V1_17H  = D4_V1_17H[V1_17F1H]

V2_17F1H   = (D4_V2_17H['Sea_Ice_Conc'] >= 0.3)
D4_V2_17H  = D4_V2_17H[V2_17F1H]

V3_17F1H   = (D4_V3_17H['Sea_Ice_Conc'] >= 0.3)
D4_V3_17H  = D4_V3_17H[V3_17F1H]

V1_18F1H   = (D4_V1_18H['Sea_Ice_Conc'] >= 0.3)
D4_V1_18H  = D4_V1_18H[V1_18F1H]

V2_18F1H   = (D4_V2_18H['Sea_Ice_Conc'] >= 0.3)
D4_V2_18H  = D4_V2_18H[V2_18F1H]

V3_18F1H   = (D4_V3_18H['Sea_Ice_Conc'] >= 0.3)
D4_V3_18H  = D4_V3_18H[V3_18F1H]

#------------------------------------------------------------------------------
# Define the variables
#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# Surface Layer
BrO_V1_17LS   = np.array(D4_V1_17L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17LS   = np.array(D4_V2_17L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17LS   = np.array(D4_V3_17L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18LS   = np.array(D4_V1_18L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18LS   = np.array(D4_V2_18L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18LS   = np.array(D4_V3_18L[0.1])   * 1e6 # convert from ppmv to ppbv

# Boundary Layer
BrO_V1_17LB   = np.array(D4_V1_17L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17LB   = np.array(D4_V2_17L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17LB   = np.array(D4_V3_17L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18LB   = np.array(D4_V1_18L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18LB   = np.array(D4_V2_18L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18LB   = np.array(D4_V3_18L[0.3])   * 1e6 # convert from ppmv to ppbv

#--------------------------------
# O3 (ppb)
O3_V1_17L   = np.array(D4_V1_17L['O3_(ppb)']) # O3 (ppb)
O3_V2_17L   = np.array(D4_V2_17L['O3_(ppb)']) # O3 (ppb)
O3_V3_17L   = np.array(D4_V3_17L['O3_(ppb)']) # O3 (ppb)
O3_V1_18L   = np.array(D4_V1_18L['O3']) # O3 (ppb)
O3_V2_18L   = np.array(D4_V2_18L['O3']) # O3 (ppb)
O3_V3_18L   = np.array(D4_V3_18L['O3']) # O3 (ppb)

#--------------------------------
# Solar Radiation (W/m2)
Sol_s_V1_17L           = np.array(D4_V1_17L['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V1_17L           = np.array(D4_V1_17L['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V1_17L['MeanSol']   = D4_V1_17L[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_17L             = np.array(D4_V1_17L['MeanSol'])

Sol_s_V2_17L           = np.array(D4_V2_17L['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V2_17L           = np.array(D4_V2_17L['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V2_17L['MeanSol']   = D4_V2_17L[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_17L             = np.array(D4_V2_17L['MeanSol'])

Sol_s_V3_17L           = np.array(D4_V3_17L['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V3_17L           = np.array(D4_V3_17L['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V3_17L['MeanSol']   = D4_V3_17L[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_17L             = np.array(D4_V3_17L['MeanSol'])

Sol_s_V1_18L           = np.array(D4_V1_18L['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V1_18L           = np.array(D4_V1_18L['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V1_18L['MeanSol']   = D4_V1_18L[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_18L             = np.array(D4_V1_18L['MeanSol'])

Sol_s_V2_18L           = np.array(D4_V2_18L['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V2_18L           = np.array(D4_V2_18L['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V2_18L['MeanSol']   = D4_V2_18L[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_18L             = np.array(D4_V2_18L['MeanSol'])

Sol_s_V3_18L           = np.array(D4_V3_18L['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V3_18L           = np.array(D4_V3_18L['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V3_18L['MeanSol']   = D4_V3_18L[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_18L             = np.array(D4_V3_18L['MeanSol'])

#--------------------------------
# Temperature (C)

Temp_s_V1_17L           = np.array(D4_V1_17L['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V1_17L           = np.array(D4_V1_17L['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V1_17L['MeanTemp']   = D4_V1_17L[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_17L             = np.array(D4_V1_17L['MeanTemp'])

Temp_s_V2_17L           = np.array(D4_V2_17L['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V2_17L           = np.array(D4_V2_17L['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V2_17L['MeanTemp']   = D4_V2_17L[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_17L             = np.array(D4_V2_17L['MeanTemp'])

Temp_s_V3_17L           = np.array(D4_V3_17L['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V3_17L           = np.array(D4_V3_17L['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V3_17L['MeanTemp']   = D4_V3_17L[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_17L             = np.array(D4_V3_17L['MeanTemp'])

Temp_s_V1_18L           = np.array(D4_V1_18L['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V1_18L           = np.array(D4_V1_18L['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V1_18L['MeanTemp']   = D4_V1_18L[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_18L             = np.array(D4_V1_18L['MeanTemp'])

Temp_s_V2_18L           = np.array(D4_V2_18L['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V2_18L           = np.array(D4_V2_18L['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V2_18L['MeanTemp']   = D4_V2_18L[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_18L             = np.array(D4_V2_18L['MeanTemp'])

Temp_s_V3_18L           = np.array(D4_V3_18L['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V3_18L           = np.array(D4_V3_18L['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V3_18L['MeanTemp']   = D4_V3_18L[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_18L             = np.array(D4_V3_18L['MeanTemp'])

#--------------------------------
# Wind Direction

WD_s_V1_17L   = np.array(D4_V1_17L['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V1_17L   = np.array(D4_V1_17L['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V2_17L   = np.array(D4_V2_17L['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V2_17L   = np.array(D4_V2_17L['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V3_17L   = np.array(D4_V3_17L['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V3_17L   = np.array(D4_V3_17L['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V1_18L   = np.array(D4_V1_18L['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V1_18L   = np.array(D4_V1_18L['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V2_18L   = np.array(D4_V2_18L['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V2_18L   = np.array(D4_V2_18L['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V3_18L   = np.array(D4_V3_18L['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V3_18L   = np.array(D4_V3_18L['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

#--------------------------------
# Wind Speed

WS_s_V1_17L   = np.array(D4_V1_17L['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17L   = np.array(D4_V1_17L['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
WS_V1_17L     = (WS_s_V1_17L + WS_p_V1_17L)/2 # Average the wind speed for port and starboard

WS_s_V2_17L   = np.array(D4_V2_17L['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17L   = np.array(D4_V2_17L['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
WS_V2_17L     = (WS_s_V2_17L + WS_p_V2_17L)/2 # Average the wind speed for port and starboard

WS_s_V3_17L   = np.array(D4_V3_17L['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17L   = np.array(D4_V3_17L['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
WS_V3_17L     = (WS_s_V3_17L + WS_p_V3_17L)/2 # Average the wind speed for port and starboard

WS_s_V1_18L   = np.array(D4_V1_18L['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18L   = np.array(D4_V1_18L['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
WS_V1_18L     = (WS_s_V1_18L + WS_p_V1_18L)/2 # Average the wind speed for port and starboard

WS_s_V2_18L   = np.array(D4_V2_18L['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18L   = np.array(D4_V2_18L['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
WS_V2_18L     = (WS_s_V2_18L + WS_p_V2_18L)/2 # Average the wind speed for port and starboard

WS_s_V3_18L   = np.array(D4_V3_18L['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18L   = np.array(D4_V3_18L['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
WS_V3_18L     = (WS_s_V3_18L + WS_p_V3_18L)/2 # Average the wind speed for port and starboard

#--------------------------------
# Vector Mean Wind Direction

WD_vect_V1_17L   = ((WD_s_V1_17L   * WS_s_V1_17L)   / (WS_s_V1_17L   + WS_p_V1_17L))   + ((WD_p_V1_17L   * WS_p_V1_17L)   / (WS_s_V1_17L   + WS_p_V1_17L)) # Calculate the vector mean wind direction
WD_vect_V2_17L   = ((WD_s_V2_17L   * WS_s_V2_17L)   / (WS_s_V2_17L   + WS_p_V2_17L))   + ((WD_p_V2_17L   * WS_p_V2_17L)   / (WS_s_V2_17L   + WS_p_V2_17L)) # Calculate the vector mean wind direction
WD_vect_V3_17L   = ((WD_s_V3_17L   * WS_s_V3_17L)   / (WS_s_V3_17L   + WS_p_V3_17L))   + ((WD_p_V3_17L   * WS_p_V3_17L)   / (WS_s_V3_17L   + WS_p_V3_17L)) # Calculate the vector mean wind direction
WD_vect_V1_18L   = ((WD_s_V1_18L   * WS_s_V1_18L)   / (WS_s_V1_18L   + WS_p_V1_18L))   + ((WD_p_V1_18L   * WS_p_V1_18L)   / (WS_s_V1_18L   + WS_p_V1_18L)) # Calculate the vector mean wind direction
WD_vect_V2_18L   = ((WD_s_V2_18L   * WS_s_V2_18L)   / (WS_s_V2_18L   + WS_p_V2_18L))   + ((WD_p_V2_18L   * WS_p_V2_18L)   / (WS_s_V2_18L   + WS_p_V2_18L)) # Calculate the vector mean wind direction
WD_vect_V3_18L   = ((WD_s_V3_18L   * WS_s_V3_18L)   / (WS_s_V3_18L   + WS_p_V3_18L))   + ((WD_p_V3_18L   * WS_p_V3_18L)   / (WS_s_V3_18L   + WS_p_V3_18L)) # Calculate the vector mean wind direction

#--------------------------------
# Hg0

Hg0_V1_17L   = np.array(D4_V1_17L['ng/m3']) # Hg0
Hg0_V2_17L   = np.array(D4_V2_17L['ng/m3']) # Hg0
Hg0_V3_17L   = np.array(D4_V3_17L['ng/m3']) # Hg0
Hg0_V1_18L   = np.array(D4_V1_18L['ng/m3']) # Hg0
Hg0_V2_18L   = np.array(D4_V2_18L['ng/m3']) # Hg0
Hg0_V3_18L   = np.array(D4_V3_18L['ng/m3']) # Hg0

#--------------------------------
# Sea Ice Concentration

SI_V1_17L   = np.array(D4_V1_17L['Sea_Ice_Conc'])*100
SI_V2_17L   = np.array(D4_V2_17L['Sea_Ice_Conc'])*100
SI_V3_17L   = np.array(D4_V3_17L['Sea_Ice_Conc'])*100
SI_V1_18L   = np.array(D4_V1_18L['Sea_Ice_Conc'])*100
SI_V2_18L   = np.array(D4_V2_18L['Sea_Ice_Conc'])*100
SI_V3_18L   = np.array(D4_V3_18L['Sea_Ice_Conc'])*100

#--------------------------------
# Relative Humidity

RH_s_V1_17L   = np.array(D4_V1_17L['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V1_17L   = np.array(D4_V1_17L['REL_HUMIDITY_PORT_PERCENT'])
RH_V1_17L     = (RH_s_V1_17L + RH_p_V1_17L)/2

RH_s_V2_17L   = np.array(D4_V2_17L['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V2_17L   = np.array(D4_V2_17L['REL_HUMIDITY_PORT_PERCENT'])
RH_V2_17L     = (RH_s_V2_17L + RH_p_V2_17L)/2

RH_s_V3_17L   = np.array(D4_V3_17L['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V3_17L   = np.array(D4_V3_17L['REL_HUMIDITY_PORT_PERCENT'])
RH_V3_17L     = (RH_s_V3_17L + RH_p_V3_17L)/2

RH_s_V1_18L   = np.array(D4_V1_18L['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V1_18L   = np.array(D4_V1_18L['REL_HUMIDITY_PORT_PERCENT'])
RH_V1_18L     = (RH_s_V1_18L + RH_p_V1_18L)/2

RH_s_V2_18L   = np.array(D4_V2_18L['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V2_18L   = np.array(D4_V2_18L['REL_HUMIDITY_PORT_PERCENT'])
RH_V2_18L     = (RH_s_V2_18L + RH_p_V2_18L)/2

RH_s_V3_18L   = np.array(D4_V3_18L['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V3_18L   = np.array(D4_V3_18L['REL_HUMIDITY_PORT_PERCENT'])
RH_V3_18L     = (RH_s_V3_18L + RH_p_V3_18L)/2

#------------------------------------------------------------------------------
# Define the variables
#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# Surface Layer 
BrO_V1_17HS   = np.array(D4_V1_17H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17HS   = np.array(D4_V2_17H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17HS   = np.array(D4_V3_17H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18HS   = np.array(D4_V1_18H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18HS   = np.array(D4_V2_18H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18HS   = np.array(D4_V3_18H[0.1])   * 1e6 # convert from ppmv to ppbv

# Boundary Layer 
BrO_V1_17HB   = np.array(D4_V1_17H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17HB   = np.array(D4_V2_17H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17HB   = np.array(D4_V3_17H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18HB   = np.array(D4_V1_18H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18HB   = np.array(D4_V2_18H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18HB   = np.array(D4_V3_18H[0.3])   * 1e6 # convert from ppmv to ppbv

#--------------------------------
# O3 (ppb)
O3_V1_17H   = np.array(D4_V1_17H['O3_(ppb)']) # O3 (ppb)
O3_V2_17H   = np.array(D4_V2_17H['O3_(ppb)']) # O3 (ppb)
O3_V3_17H   = np.array(D4_V3_17H['O3_(ppb)']) # O3 (ppb)
O3_V1_18H   = np.array(D4_V1_18H['O3']) # O3 (ppb)
O3_V2_18H   = np.array(D4_V2_18H['O3']) # O3 (ppb)
O3_V3_18H   = np.array(D4_V3_18H['O3']) # O3 (ppb)

#--------------------------------
# Solar Radiation (W/m2)
Sol_s_V1_17H           = np.array(D4_V1_17H['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V1_17H           = np.array(D4_V1_17H['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V1_17H['MeanSol']   = D4_V1_17H[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_17H             = np.array(D4_V1_17H['MeanSol'])

Sol_s_V2_17H           = np.array(D4_V2_17H['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V2_17H           = np.array(D4_V2_17H['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V2_17H['MeanSol']   = D4_V2_17H[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_17H             = np.array(D4_V2_17H['MeanSol'])

Sol_s_V3_17H           = np.array(D4_V3_17H['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V3_17H           = np.array(D4_V3_17H['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V3_17H['MeanSol']   = D4_V3_17H[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_17H             = np.array(D4_V3_17H['MeanSol'])

Sol_s_V1_18H           = np.array(D4_V1_18H['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V1_18H           = np.array(D4_V1_18H['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V1_18H['MeanSol']   = D4_V1_18H[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_18H             = np.array(D4_V1_18H['MeanSol'])

Sol_s_V2_18H           = np.array(D4_V2_18H['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V2_18H           = np.array(D4_V2_18H['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V2_18H['MeanSol']   = D4_V2_18H[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_18H             = np.array(D4_V2_18H['MeanSol'])

Sol_s_V3_18H           = np.array(D4_V3_18H['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_V3_18H           = np.array(D4_V3_18H['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_V3_18H['MeanSol']   = D4_V3_18H[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_18H             = np.array(D4_V3_18H['MeanSol'])

#--------------------------------
# Temperature (C)

Temp_s_V1_17H           = np.array(D4_V1_17H['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V1_17H           = np.array(D4_V1_17H['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V1_17H['MeanTemp']   = D4_V1_17H[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_17H             = np.array(D4_V1_17H['MeanTemp'])

Temp_s_V2_17H           = np.array(D4_V2_17H['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V2_17H           = np.array(D4_V2_17H['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V2_17H['MeanTemp']   = D4_V2_17H[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_17H             = np.array(D4_V2_17H['MeanTemp'])

Temp_s_V3_17H           = np.array(D4_V3_17H['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V3_17H           = np.array(D4_V3_17H['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V3_17H['MeanTemp']   = D4_V3_17H[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_17H             = np.array(D4_V3_17H['MeanTemp'])

Temp_s_V1_18H           = np.array(D4_V1_18H['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V1_18H           = np.array(D4_V1_18H['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V1_18H['MeanTemp']   = D4_V1_18H[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_18H             = np.array(D4_V1_18H['MeanTemp'])

Temp_s_V2_18H           = np.array(D4_V2_18H['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V2_18H           = np.array(D4_V2_18H['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V2_18H['MeanTemp']   = D4_V2_18H[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_18H             = np.array(D4_V2_18H['MeanTemp'])

Temp_s_V3_18H           = np.array(D4_V3_18H['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_V3_18H           = np.array(D4_V3_18H['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_V3_18H['MeanTemp']   = D4_V3_18H[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_18H             = np.array(D4_V3_18H['MeanTemp'])

#--------------------------------
# Wind Direction

WD_s_V1_17H   = np.array(D4_V1_17H['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V1_17H   = np.array(D4_V1_17H['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V2_17H   = np.array(D4_V2_17H['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V2_17H   = np.array(D4_V2_17H['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V3_17H   = np.array(D4_V3_17H['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V3_17H   = np.array(D4_V3_17H['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V1_18H   = np.array(D4_V1_18H['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V1_18H   = np.array(D4_V1_18H['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V2_18H   = np.array(D4_V2_18H['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V2_18H   = np.array(D4_V2_18H['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

WD_s_V3_18H   = np.array(D4_V3_18H['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_V3_18H   = np.array(D4_V3_18H['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

#--------------------------------
# Wind Speed

WS_s_V1_17H   = np.array(D4_V1_17H['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17H   = np.array(D4_V1_17H['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_V1_17H     = (WS_s_V1_17H + WS_p_V1_17H)/2 # Average the wind speed for port and starboard

WS_s_V2_17H   = np.array(D4_V2_17H['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17H   = np.array(D4_V2_17H['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_V2_17H     = (WS_s_V2_17H + WS_p_V2_17H)/2 # Average the wind speed for port and starboard

WS_s_V3_17H   = np.array(D4_V3_17H['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17H   = np.array(D4_V3_17H['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_V3_17H     = (WS_s_V3_17H + WS_p_V3_17H)/2 # Average the wind speed for port and starboard

WS_s_V1_18H   = np.array(D4_V1_18H['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18H   = np.array(D4_V1_18H['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_V1_18H     = (WS_s_V1_18H + WS_p_V1_18H)/2 # Average the wind speed for port and starboard

WS_s_V2_18H   = np.array(D4_V2_18H['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18H   = np.array(D4_V2_18H['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_V2_18H     = (WS_s_V2_18H + WS_p_V2_18H)/2 # Average the wind speed for port and starboard

WS_s_V3_18H   = np.array(D4_V3_18H['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18H   = np.array(D4_V3_18H['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_V3_18H     = (WS_s_V3_18H + WS_p_V3_18H)/2 # Average the wind speed for port and starboard

#--------------------------------
# Vector Mean Wind Direction

WD_vect_V1_17H   = ((WD_s_V1_17H   * WS_s_V1_17H)   / (WS_s_V1_17H   + WS_p_V1_17H))   + ((WD_p_V1_17H   * WS_p_V1_17H)   / (WS_s_V1_17H   + WS_p_V1_17H)) # Calculate the vector mean wind direction
WD_vect_V2_17H   = ((WD_s_V2_17H   * WS_s_V2_17H)   / (WS_s_V2_17H   + WS_p_V2_17H))   + ((WD_p_V2_17H   * WS_p_V2_17H)   / (WS_s_V2_17H   + WS_p_V2_17H)) # Calculate the vector mean wind direction
WD_vect_V3_17H   = ((WD_s_V3_17H   * WS_s_V3_17H)   / (WS_s_V3_17H   + WS_p_V3_17H))   + ((WD_p_V3_17H   * WS_p_V3_17H)   / (WS_s_V3_17H   + WS_p_V3_17H)) # Calculate the vector mean wind direction
WD_vect_V1_18H   = ((WD_s_V1_18H   * WS_s_V1_18H)   / (WS_s_V1_18H   + WS_p_V1_18H))   + ((WD_p_V1_18H   * WS_p_V1_18H)   / (WS_s_V1_18H   + WS_p_V1_18H)) # Calculate the vector mean wind direction
WD_vect_V2_18H   = ((WD_s_V2_18H   * WS_s_V2_18H)   / (WS_s_V2_18H   + WS_p_V2_18H))   + ((WD_p_V2_18H   * WS_p_V2_18H)   / (WS_s_V2_18H   + WS_p_V2_18H)) # Calculate the vector mean wind direction
WD_vect_V3_18H   = ((WD_s_V3_18H   * WS_s_V3_18H)   / (WS_s_V3_18H   + WS_p_V3_18H))   + ((WD_p_V3_18H   * WS_p_V3_18H)   / (WS_s_V3_18H   + WS_p_V3_18H)) # Calculate the vector mean wind direction

#--------------------------------
# Hg0

Hg0_V1_17H   = np.array(D4_V1_17H['ng/m3']) # Hg0
Hg0_V2_17H   = np.array(D4_V2_17H['ng/m3']) # Hg0
Hg0_V3_17H   = np.array(D4_V3_17H['ng/m3']) # Hg0
Hg0_V1_18H   = np.array(D4_V1_18H['ng/m3']) # Hg0
Hg0_V2_18H   = np.array(D4_V2_18H['ng/m3']) # Hg0
Hg0_V3_18H   = np.array(D4_V3_18H['ng/m3']) # Hg0

#--------------------------------
# Sea Ice Concentration

SI_V1_17H   = np.array(D4_V1_17H['Sea_Ice_Conc'])   * 100
SI_V2_17H   = np.array(D4_V2_17H['Sea_Ice_Conc'])   * 100
SI_V3_17H   = np.array(D4_V3_17H['Sea_Ice_Conc'])   * 100
SI_V1_18H   = np.array(D4_V1_18H['Sea_Ice_Conc'])   * 100
SI_V2_18H   = np.array(D4_V2_18H['Sea_Ice_Conc'])   * 100
SI_V3_18H   = np.array(D4_V3_18H['Sea_Ice_Conc'])   * 100

#--------------------------------
# Relative Humidity

RH_s_V1_17H   = np.array(D4_V1_17H['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V1_17H   = np.array(D4_V1_17H['REL_HUMIDITY_PORT_PERCENT'])
RH_V1_17H     = (RH_s_V1_17H + RH_p_V1_17H)/2

RH_s_V2_17H   = np.array(D4_V2_17H['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V2_17H   = np.array(D4_V2_17H['REL_HUMIDITY_PORT_PERCENT'])
RH_V2_17H     = (RH_s_V2_17H + RH_p_V2_17H)/2

RH_s_V3_17H   = np.array(D4_V3_17H['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V3_17H   = np.array(D4_V3_17H['REL_HUMIDITY_PORT_PERCENT'])
RH_V3_17H     = (RH_s_V3_17H + RH_p_V3_17H)/2

RH_s_V1_18H   = np.array(D4_V1_18H['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V1_18H   = np.array(D4_V1_18H['REL_HUMIDITY_PORT_PERCENT'])
RH_V1_18H     = (RH_s_V1_18H + RH_p_V1_18H)/2

RH_s_V2_18H   = np.array(D4_V2_18H['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V2_18H   = np.array(D4_V2_18H['REL_HUMIDITY_PORT_PERCENT'])
RH_V2_18H     = (RH_s_V2_18H + RH_p_V2_18H)/2

RH_s_V3_18H   = np.array(D4_V3_18H['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_V3_18H   = np.array(D4_V3_18H['REL_HUMIDITY_PORT_PERCENT'])
RH_V3_18H     = (RH_s_V3_18H + RH_p_V3_18H)/2

#------------------------------------------------------------------------------
# Concate the variables from each voyage

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOLS = np.concatenate((BrO_V1_17LS, BrO_V2_17LS, BrO_V3_17LS, BrO_V1_18LS, BrO_V2_18LS, BrO_V3_18LS), axis=0)

# BrO boundary volume mixing ratio (VMR)
BrOLB = np.concatenate((BrO_V1_17LB, BrO_V2_17LB, BrO_V3_17LB, BrO_V1_18LB, BrO_V2_18LB, BrO_V3_18LB), axis=0)

# O3 (ppb)
O3L = np.concatenate((O3_V1_17L, O3_V2_17L, O3_V3_17L, O3_V1_18L, O3_V2_18L, O3_V3_18L), axis=0)

# Solar Radiation (W/m2)
SolL = np.concatenate((Sol_V1_17L, Sol_V2_17L, Sol_V3_17L, Sol_V1_18L, Sol_V2_18L, Sol_V3_18L), axis=0)

# Temperature (C)
TempL = np.concatenate((Temp_V1_17L, Temp_V2_17L, Temp_V3_17L, Temp_V1_18L, Temp_V2_18L, Temp_V3_18L), axis=0)

# Wind Speed
WSL = np.concatenate((WS_V1_17L, WS_V2_17L, WS_V3_17L, WS_V1_18L, WS_V2_18L, WS_V3_18L), axis=0)

# Vector Mean Wind Direction
WD_vectL = np.concatenate((WD_vect_V1_17L, WD_vect_V2_17L, WD_vect_V3_17L, WD_vect_V1_18L, WD_vect_V2_18L, WD_vect_V3_18L), axis=0)

# Hg0
Hg0L = np.concatenate((Hg0_V1_17L, Hg0_V2_17L, Hg0_V3_17L, Hg0_V1_18L, Hg0_V2_18L, Hg0_V3_18L), axis=0)

# Sea Ice Concentration
SIL = np.concatenate((SI_V1_17L, SI_V2_17L, SI_V3_17L, SI_V1_18L, SI_V2_18L, SI_V3_18L), axis=0)

# Relative Humidity
RHL = np.concatenate((RH_V1_17L, RH_V2_17L, RH_V3_17L, RH_V1_18L, RH_V2_18L, RH_V3_18L), axis=0)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOHS = np.concatenate((BrO_V1_17HS, BrO_V2_17HS, BrO_V3_17HS, BrO_V1_18HS, BrO_V2_18HS, BrO_V3_18HS), axis=0)

# BrO boundary volume mixing ratio (VMR)
BrOHB = np.concatenate((BrO_V1_17HB, BrO_V2_17HB, BrO_V3_17HB, BrO_V1_18HB, BrO_V2_18HB, BrO_V3_18HB), axis=0)

# O3 (ppb)
O3H = np.concatenate((O3_V1_17H, O3_V2_17H, O3_V3_17H, O3_V1_18H, O3_V2_18H, O3_V3_18H), axis=0)

# Solar Radiation (W/m2)
SolH = np.concatenate((Sol_V1_17H, Sol_V2_17H, Sol_V3_17H, Sol_V1_18H, Sol_V2_18H, Sol_V3_18H), axis=0)

# Temperature (C)
TempH = np.concatenate((Temp_V1_17H, Temp_V2_17H, Temp_V3_17H, Temp_V1_18H, Temp_V2_18H, Temp_V3_18H), axis=0)

# Wind Speed
WSH = np.concatenate((WS_V1_17H, WS_V2_17H, WS_V3_17H, WS_V1_18H, WS_V2_18H, WS_V3_18H), axis=0)

# Vector Mean Wind Direction
WD_vectH = np.concatenate((WD_vect_V1_17H, WD_vect_V2_17H, WD_vect_V3_17H, WD_vect_V1_18H, WD_vect_V2_18H, WD_vect_V3_18H), axis=0)

# Hg0
Hg0H = np.concatenate((Hg0_V1_17H, Hg0_V2_17H, Hg0_V3_17H, Hg0_V1_18H, Hg0_V2_18H, Hg0_V3_18H), axis=0)

# Sea Ice Concentration
SIH = np.concatenate((SI_V1_17H, SI_V2_17H, SI_V3_17H, SI_V1_18H, SI_V2_18H, SI_V3_18H), axis=0)

# Relative Humidity
RHH = np.concatenate((RH_V1_17H, RH_V2_17H, RH_V3_17H, RH_V1_18H, RH_V2_18H, RH_V3_18H), axis=0)

#------------------------------------------------------------------------------
# Scan for NaN values
#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V1_17_Y1maskLS   = np.isfinite(BrO_V1_17LS) # Scan for NaN values
BrO_V1_17LS      = BrO_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from BrO
O3_V1_17LS       = O3_V1_17L[V1_17_Y1maskLS] # Remove NaN values from Sol
Sol_V1_17LS      = Sol_V1_17L[V1_17_Y1maskLS] # Remove NaN values from Sol
Temp_V1_17LS     = Temp_V1_17L[V1_17_Y1maskLS] # Remove NaN values from Sol
WD_vect_V1_17LS  = WD_vect_V1_17L[V1_17_Y1maskLS] # Remove NaN values from Sol
WS_V1_17LS       = WS_V1_17L[V1_17_Y1maskLS] # Remove NaN values from Sol
Hg0_V1_17LS      = Hg0_V1_17L[V1_17_Y1maskLS] # Remove NaN values from Sol
SI_V1_17LS       = SI_V1_17L[V1_17_Y1maskLS] # Remove NaN values from Sol
RH_V1_17LS       = RH_V1_17L[V1_17_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
V1_17_Y1maskLS   = np.isfinite(Sol_V1_17LS) # Scan for NaN values
BrO_V1_17LS      = BrO_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from BrO
O3_V1_17LS       = O3_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from Sol
Sol_V1_17LS      = Sol_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from Sol
Temp_V1_17LS     = Temp_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from Sol
WD_vect_V1_17LS  = WD_vect_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from Sol
WS_V1_17LS       = WS_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from Sol
Hg0_V1_17LS      = Hg0_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from Sol
SI_V1_17LS       = SI_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from Sol
RH_V1_17LS       = RH_V1_17LS[V1_17_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
V1_17_Y2maskLS   = np.isfinite(O3_V1_17LS) # Scan for NaN values
BrO_O3_V1_17LS   = BrO_V1_17LS[V1_17_Y2maskLS] # Remove NaN values from BrO
O3_V1_17LS       = O3_V1_17LS[V1_17_Y2maskLS] # Remove NaN values from Temp
Sol_O3_V1_17LS   = Sol_V1_17LS[V1_17_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_17_Y3maskLS   = np.isfinite(Temp_V1_17LS) # Scan for NaN values
BrO_Temp_V1_17LS = BrO_V1_17LS[V1_17_Y3maskLS] # Remove NaN values from BrO
Temp_V1_17LS     = Temp_V1_17LS[V1_17_Y3maskLS] # Remove NaN values from Temp
Sol_Temp_V1_17LS = Sol_V1_17LS[V1_17_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_17_Y4maskLS   = np.isfinite(WD_vect_V1_17LS) # Scan for NaN values
BrO_WD_V1_17LS   = BrO_V1_17LS[V1_17_Y4maskLS] # Remove NaN values from BrO
WD_vect_V1_17LS  = WD_vect_V1_17LS[V1_17_Y4maskLS] # Remove NaN values from WD_vect
Sol_WD_V1_17LS   = Sol_V1_17LS[V1_17_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_17_Y5maskLS   = np.isfinite(WS_V1_17LS) # Scan for NaN values
BrO_WS_V1_17LS   = BrO_V1_17LS[V1_17_Y5maskLS] # Remove NaN values from BrO
WS_V1_17LS       = WS_V1_17LS[V1_17_Y5maskLS] # Remove NaN values from WS
Sol_WS_V1_17LS   = Sol_V1_17LS[V1_17_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_17_Y6maskLS   = np.isfinite(Hg0_V1_17LS) # Scan for NaN values
BrO_Hg0_V1_17LS  = BrO_V1_17LS[V1_17_Y6maskLS] # Remove NaN values from BrO
Hg0_V1_17LS      = Hg0_V1_17LS[V1_17_Y6maskLS] # Remove NaN values from SI
Sol_Hg0_V1_17LS  = Sol_V1_17LS[V1_17_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_17_Y7maskLS   = np.isfinite(SI_V1_17LS) # Scan for NaN values
BrO_SI_V1_17LS   = BrO_V1_17LS[V1_17_Y7maskLS] # Remove NaN values from BrO
SI_SI_V1_17LS    = SI_V1_17LS[V1_17_Y7maskLS] # Remove NaN values from SI
Sol_SI_V1_17LS   = Sol_V1_17LS[V1_17_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_17_Y8maskLS   = np.isfinite(RH_V1_17LS) # Scan for NaN values
BrO_RH_V1_17LS   = BrO_V1_17LS[V1_17_Y8maskLS] # Remove NaN values from BrO
RH_V1_17LS       = RH_V1_17LS[V1_17_Y8maskLS] # Remove NaN values from RH
Sol_RH_V1_17LS   = Sol_V1_17LS[V1_17_Y8maskLS] # Remove NaN values from Sol

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V2_17_Y1maskLS   = np.isfinite(BrO_V2_17LS) # Scan for NaN values
BrO_V2_17LS      = BrO_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from BrO
O3_V2_17LS       = O3_V2_17L[V2_17_Y1maskLS] # Remove NaN values from Sol
Sol_V2_17LS      = Sol_V2_17L[V2_17_Y1maskLS] # Remove NaN values from Sol
Temp_V2_17LS     = Temp_V2_17L[V2_17_Y1maskLS] # Remove NaN values from Sol
WD_vect_V2_17LS  = WD_vect_V2_17L[V2_17_Y1maskLS] # Remove NaN values from Sol
WS_V2_17LS       = WS_V2_17L[V2_17_Y1maskLS] # Remove NaN values from Sol
Hg0_V2_17LS      = Hg0_V2_17L[V2_17_Y1maskLS] # Remove NaN values from Sol
SI_V2_17LS       = SI_V2_17L[V2_17_Y1maskLS] # Remove NaN values from Sol
RH_V2_17LS       = RH_V2_17L[V2_17_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_17_Y1maskLS   = np.isfinite(Sol_V2_17LS) # Scan for NaN values
BrO_V2_17LS      = BrO_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from BrO
O3_V2_17LS       = O3_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from Sol
Sol_V2_17LS      = Sol_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from Sol
Temp_V2_17LS     = Temp_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from Sol
WD_vect_V2_17LS  = WD_vect_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from Sol
WS_V2_17LS       = WS_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from Sol
Hg0_V2_17LS      = Hg0_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from Sol
SI_V2_17LS       = SI_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from Sol
RH_V2_17LS       = RH_V2_17LS[V2_17_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
V2_17_Y2maskLS   = np.isfinite(O3_V2_17LS) # Scan for NaN values
BrO_O3_V2_17LS   = BrO_V2_17LS[V2_17_Y2maskLS] # Remove NaN values from BrO
O3_V2_17LS       = O3_V2_17LS[V2_17_Y2maskLS] # Remove NaN values from Temp
Sol_O3_V2_17LS   = Sol_V2_17LS[V2_17_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_17_Y3maskLS   = np.isfinite(Temp_V2_17LS) # Scan for NaN values
BrO_Temp_V2_17LS = BrO_V2_17LS[V2_17_Y3maskLS] # Remove NaN values from BrO
Temp_V2_17LS     = Temp_V2_17LS[V2_17_Y3maskLS] # Remove NaN values from Temp
Sol_Temp_V2_17LS = Sol_V2_17LS[V2_17_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_17_Y4maskLS   = np.isfinite(WD_vect_V2_17LS) # Scan for NaN values
BrO_WD_V2_17LS   = BrO_V2_17LS[V2_17_Y4maskLS] # Remove NaN values from BrO
WD_vect_V2_17LS  = WD_vect_V2_17LS[V2_17_Y4maskLS] # Remove NaN values from WD_vect
Sol_WD_V2_17LS   = Sol_V2_17LS[V2_17_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_17_Y5maskLS   = np.isfinite(WS_V2_17LS) # Scan for NaN values
BrO_WS_V2_17LS   = BrO_V2_17LS[V2_17_Y5maskLS] # Remove NaN values from BrO
WS_V2_17LS       = WS_V2_17LS[V2_17_Y5maskLS] # Remove NaN values from WS
Sol_WS_V2_17LS   = Sol_V2_17LS[V2_17_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_17_Y6maskLS   = np.isfinite(Hg0_V2_17LS) # Scan for NaN values
BrO_Hg0_V2_17LS  = BrO_V2_17LS[V2_17_Y6maskLS] # Remove NaN values from BrO
Hg0_V2_17LS      = Hg0_V2_17LS[V2_17_Y6maskLS] # Remove NaN values from SI
Sol_Hg0_V2_17LS  = Sol_V2_17LS[V2_17_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_17_Y7maskLS   = np.isfinite(SI_V2_17LS) # Scan for NaN values
BrO_SI_V2_17LS   = BrO_V2_17LS[V2_17_Y7maskLS] # Remove NaN values from BrO
SI_SI_V2_17LS    = SI_V2_17LS[V2_17_Y7maskLS] # Remove NaN values from SI
Sol_SI_V2_17LS   = Sol_V2_17LS[V2_17_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_17_Y8maskLS   = np.isfinite(RH_V2_17LS) # Scan for NaN values
BrO_RH_V2_17LS   = BrO_V2_17LS[V2_17_Y8maskLS] # Remove NaN values from BrO
RH_V2_17LS       = RH_V2_17LS[V2_17_Y8maskLS] # Remove NaN values from WS
Sol_RH_V2_17LS   = Sol_V2_17LS[V2_17_Y8maskLS] # Remove NaN values from Sol

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V3_17_Y1maskLS   = np.isfinite(BrO_V3_17LS) # Scan for NaN values
BrO_V3_17LS      = BrO_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from BrO
O3_V3_17LS       = O3_V3_17L[V3_17_Y1maskLS] # Remove NaN values from Sol
Sol_V3_17LS      = Sol_V3_17L[V3_17_Y1maskLS] # Remove NaN values from Sol
Temp_V3_17LS     = Temp_V3_17L[V3_17_Y1maskLS] # Remove NaN values from Sol
WD_vect_V3_17LS  = WD_vect_V3_17L[V3_17_Y1maskLS] # Remove NaN values from Sol
WS_V3_17LS       = WS_V3_17L[V3_17_Y1maskLS] # Remove NaN values from Sol
Hg0_V3_17LS      = Hg0_V3_17L[V3_17_Y1maskLS] # Remove NaN values from Sol
SI_V3_17LS       = SI_V3_17L[V3_17_Y1maskLS] # Remove NaN values from Sol
RH_V3_17LS       = RH_V3_17L[V3_17_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_17_Y1maskLS   = np.isfinite(Sol_V3_17LS) # Scan for NaN values
BrO_V3_17LS      = BrO_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from BrO
O3_V3_17LS       = O3_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from Sol
Sol_V3_17LS      = Sol_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from Sol
Temp_V3_17LS     = Temp_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from Sol
WD_vect_V3_17LS  = WD_vect_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from Sol
WS_V3_17LS       = WS_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from Sol
Hg0_V3_17LS      = Hg0_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from Sol
SI_V3_17LS       = SI_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from Sol
RH_V3_17LS       = RH_V3_17LS[V3_17_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
V3_17_Y2maskLS   = np.isfinite(O3_V3_17LS) # Scan for NaN values
BrO_O3_V3_17LS   = BrO_V3_17LS[V3_17_Y2maskLS] # Remove NaN values from BrO
O3_V3_17LS       = O3_V3_17LS[V3_17_Y2maskLS] # Remove NaN values from Temp
Sol_O3_V3_17LS   = Sol_V3_17LS[V3_17_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_17_Y3maskLS   = np.isfinite(Temp_V3_17LS) # Scan for NaN values
BrO_Temp_V3_17LS = BrO_V3_17LS[V3_17_Y3maskLS] # Remove NaN values from BrO
Temp_V3_17LS     = Temp_V3_17LS[V3_17_Y3maskLS] # Remove NaN values from Temp
Sol_Temp_V3_17LS = Sol_V3_17LS[V3_17_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_17_Y4maskLS   = np.isfinite(WD_vect_V3_17LS) # Scan for NaN values
BrO_WD_V3_17LS   = BrO_V3_17LS[V3_17_Y4maskLS] # Remove NaN values from BrO
WD_vect_V3_17LS  = WD_vect_V3_17LS[V3_17_Y4maskLS] # Remove NaN values from WD_vect
Sol_WD_V3_17LS   = Sol_V3_17LS[V3_17_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_17_Y5maskLS   = np.isfinite(WS_V3_17LS) # Scan for NaN values
BrO_WS_V3_17LS   = BrO_V3_17LS[V3_17_Y5maskLS] # Remove NaN values from BrO
WS_V3_17LS       = WS_V3_17LS[V3_17_Y5maskLS] # Remove NaN values from WS
Sol_WS_V3_17LS   = Sol_V3_17LS[V3_17_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_17_Y6maskLS   = np.isfinite(Hg0_V3_17LS) # Scan for NaN values
BrO_Hg0_V3_17LS  = BrO_V3_17LS[V3_17_Y6maskLS] # Remove NaN values from BrO
Hg0_V3_17LS      = Hg0_V3_17LS[V3_17_Y6maskLS] # Remove NaN values from SI
Sol_Hg0_V3_17LS  = Sol_V3_17LS[V3_17_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_17_Y7maskLS   = np.isfinite(SI_V3_17LS) # Scan for NaN values
BrO_SI_V3_17LS   = BrO_V3_17LS[V3_17_Y7maskLS] # Remove NaN values from BrO
SI_SI_V3_17LS    = SI_V3_17LS[V3_17_Y7maskLS] # Remove NaN values from SI
Sol_SI_V3_17LS   = Sol_V3_17LS[V3_17_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_17_Y8maskLS   = np.isfinite(RH_V3_17LS) # Scan for NaN values
BrO_RH_V3_17LS   = BrO_V3_17LS[V3_17_Y8maskLS] # Remove NaN values from BrO
RH_V3_17LS       = RH_V3_17LS[V3_17_Y8maskLS] # Remove NaN values from WS
Sol_RH_V3_17LS   = Sol_V3_17LS[V3_17_Y8maskLS] # Remove NaN values from Sol

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (BrO)
V1_18_Y1maskLS   = np.isfinite(BrO_V1_18LS) # Scan for NaN values
BrO_V1_18LS      = BrO_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from BrO
O3_V1_18LS       = O3_V1_18L[V1_18_Y1maskLS] # Remove NaN values from Sol
Sol_V1_18LS      = Sol_V1_18L[V1_18_Y1maskLS] # Remove NaN values from Sol
Temp_V1_18LS     = Temp_V1_18L[V1_18_Y1maskLS] # Remove NaN values from Sol
WD_vect_V1_18LS  = WD_vect_V1_18L[V1_18_Y1maskLS] # Remove NaN values from Sol
WS_V1_18LS       = WS_V1_18L[V1_18_Y1maskLS] # Remove NaN values from Sol
Hg0_V1_18LS      = Hg0_V1_18L[V1_18_Y1maskLS] # Remove NaN values from Sol
SI_V1_18LS       = SI_V1_18L[V1_18_Y1maskLS] # Remove NaN values from Sol
RH_V1_18LS       = RH_V1_18L[V1_18_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
V1_18_Y1maskLS   = np.isfinite(Sol_V1_18LS) # Scan for NaN values
BrO_V1_18LS      = BrO_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from BrO
O3_V1_18LS       = O3_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from Sol
Sol_V1_18LS      = Sol_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from Sol
Temp_V1_18LS     = Temp_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from Sol
WD_vect_V1_18LS  = WD_vect_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from Sol
WS_V1_18LS       = WS_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from Sol
Hg0_V1_18LS      = Hg0_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from Sol
SI_V1_18LS       = SI_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from Sol
RH_V1_18LS       = RH_V1_18LS[V1_18_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
V1_18_Y2maskLS   = np.isfinite(O3_V1_18LS) # Scan for NaN values
BrO_O3_V1_18LS   = BrO_V1_18LS[V1_18_Y2maskLS] # Remove NaN values from BrO
O3_V1_18LS       = O3_V1_18LS[V1_18_Y2maskLS] # Remove NaN values from Temp
Sol_O3_V1_18LS   = Sol_V1_18LS[V1_18_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_18_Y3maskLS   = np.isfinite(Temp_V1_18LS) # Scan for NaN values
BrO_Temp_V1_18LS = BrO_V1_18LS[V1_18_Y3maskLS] # Remove NaN values from BrO
Temp_V1_18LS     = Temp_V1_18LS[V1_18_Y3maskLS] # Remove NaN values from Temp
Sol_Temp_V1_18LS = Sol_V1_18LS[V1_18_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_18_Y4maskLS   = np.isfinite(WD_vect_V1_18LS) # Scan for NaN values
BrO_WD_V1_18LS   = BrO_V1_18LS[V1_18_Y4maskLS] # Remove NaN values from BrO
WD_vect_V1_18LS  = WD_vect_V1_18LS[V1_18_Y4maskLS] # Remove NaN values from WD_vect
Sol_WD_V1_18LS   = Sol_V1_18LS[V1_18_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_18_Y5maskLS   = np.isfinite(WS_V1_18LS) # Scan for NaN values
BrO_WS_V1_18LS   = BrO_V1_18LS[V1_18_Y5maskLS] # Remove NaN values from BrO
WS_V1_18LS       = WS_V1_18LS[V1_18_Y5maskLS] # Remove NaN values from WS
Sol_WS_V1_18LS   = Sol_V1_18LS[V1_18_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_18_Y6maskLS   = np.isfinite(Hg0_V1_18LS) # Scan for NaN values
BrO_Hg0_V1_18LS  = BrO_V1_18LS[V1_18_Y6maskLS] # Remove NaN values from BrO
Hg0_V1_18LS      = Hg0_V1_18LS[V1_18_Y6maskLS] # Remove NaN values from SI
Sol_Hg0_V1_18LS  = Sol_V1_18LS[V1_18_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_18_Y7maskLS   = np.isfinite(SI_V1_18LS) # Scan for NaN values
BrO_SI_V1_18LS   = BrO_V1_18LS[V1_18_Y7maskLS] # Remove NaN values from BrO
SI_SI_V1_18LS    = SI_V1_18LS[V1_18_Y7maskLS] # Remove NaN values from SI
Sol_SI_V1_18LS   = Sol_V1_18LS[V1_18_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_18_Y8maskLS   = np.isfinite(RH_V1_18LS) # Scan for NaN values
BrO_RH_V1_18LS   = BrO_V1_18LS[V1_18_Y8maskLS] # Remove NaN values from BrO
RH_V1_18LS       = RH_V1_18LS[V1_18_Y8maskLS] # Remove NaN values from WS
Sol_RH_V1_18LS   = Sol_V1_18LS[V1_18_Y8maskLS] # Remove NaN values from Sol

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (BrO)
V2_18_Y1maskLS   = np.isfinite(BrO_V2_18LS) # Scan for NaN values
BrO_V2_18LS      = BrO_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from BrO
O3_V2_18LS       = O3_V2_18L[V2_18_Y1maskLS] # Remove NaN values from Sol
Sol_V2_18LS      = Sol_V2_18L[V2_18_Y1maskLS] # Remove NaN values from Sol
Temp_V2_18LS     = Temp_V2_18L[V2_18_Y1maskLS] # Remove NaN values from Sol
WD_vect_V2_18LS  = WD_vect_V2_18L[V2_18_Y1maskLS] # Remove NaN values from Sol
WS_V2_18LS       = WS_V2_18L[V2_18_Y1maskLS] # Remove NaN values from Sol
Hg0_V2_18LS      = Hg0_V2_18L[V2_18_Y1maskLS] # Remove NaN values from Sol
SI_V2_18LS       = SI_V2_18L[V2_18_Y1maskLS] # Remove NaN values from Sol
RH_V2_18LS       = RH_V2_18L[V2_18_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_18_Y1maskLS   = np.isfinite(Sol_V2_18LS) # Scan for NaN values
BrO_V2_18LS      = BrO_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from BrO
O3_V2_18LS       = O3_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from Sol
Sol_V2_18LS      = Sol_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from Sol
Temp_V2_18LS     = Temp_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from Sol
WD_vect_V2_18LS  = WD_vect_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from Sol
WS_V2_18LS       = WS_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from Sol
Hg0_V2_18LS      = Hg0_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from Sol
SI_V2_18LS       = SI_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from Sol
RH_V2_18LS       = RH_V2_18LS[V2_18_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
V2_18_Y2maskLS   = np.isfinite(O3_V2_18LS) # Scan for NaN values
BrO_O3_V2_18LS   = BrO_V2_18LS[V2_18_Y2maskLS] # Remove NaN values from BrO
O3_V2_18LS       = O3_V2_18LS[V2_18_Y2maskLS] # Remove NaN values from Temp
Sol_O3_V2_18LS   = Sol_V2_18LS[V2_18_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_18_Y3maskLS   = np.isfinite(Temp_V2_18LS) # Scan for NaN values
BrO_Temp_V2_18LS = BrO_V2_18LS[V2_18_Y3maskLS] # Remove NaN values from BrO
Temp_V2_18LS     = Temp_V2_18LS[V2_18_Y3maskLS] # Remove NaN values from Temp
Sol_Temp_V2_18LS = Sol_V2_18LS[V2_18_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_18_Y4maskLS   = np.isfinite(WD_vect_V2_18LS) # Scan for NaN values
BrO_WD_V2_18LS   = BrO_V2_18LS[V2_18_Y4maskLS] # Remove NaN values from BrO
WD_vect_V2_18LS  = WD_vect_V2_18LS[V2_18_Y4maskLS] # Remove NaN values from WD_vect
Sol_WD_V2_18LS   = Sol_V2_18LS[V2_18_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_18_Y5maskLS   = np.isfinite(WS_V2_18LS) # Scan for NaN values
BrO_WS_V2_18LS   = BrO_V2_18LS[V2_18_Y5maskLS] # Remove NaN values from BrO
WS_V2_18LS       = WS_V2_18LS[V2_18_Y5maskLS] # Remove NaN values from WS
Sol_WS_V2_18LS   = Sol_V2_18LS[V2_18_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_18_Y6maskLS   = np.isfinite(Hg0_V2_18LS) # Scan for NaN values
BrO_Hg0_V2_18LS  = BrO_V2_18LS[V2_18_Y6maskLS] # Remove NaN values from BrO
Hg0_V2_18LS      = Hg0_V2_18LS[V2_18_Y6maskLS] # Remove NaN values from SI
Sol_Hg0_V2_18LS  = Sol_V2_18LS[V2_18_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_18_Y7maskLS   = np.isfinite(SI_V2_18LS) # Scan for NaN values
BrO_SI_V2_18LS   = BrO_V2_18LS[V2_18_Y7maskLS] # Remove NaN values from BrO
SI_SI_V2_18LS    = SI_V2_18LS[V2_18_Y7maskLS] # Remove NaN values from SI
Sol_SI_V2_18LS   = Sol_V2_18LS[V2_18_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_18_Y8maskLS   = np.isfinite(RH_V2_18LS) # Scan for NaN values
BrO_RH_V2_18LS   = BrO_V2_18LS[V2_18_Y8maskLS] # Remove NaN values from BrO
RH_V2_18LS       = RH_V2_18LS[V2_18_Y8maskLS] # Remove NaN values from WS
Sol_RH_V2_18LS   = Sol_V2_18LS[V2_18_Y8maskLS] # Remove NaN values from Sol

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (BrO) 
V3_18_Y1maskLS   = np.isfinite(BrO_V3_18LS) # Scan for NaN values
BrO_V3_18LS      = BrO_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from BrO
O3_V3_18LS       = O3_V3_18L[V3_18_Y1maskLS] # Remove NaN values from Sol
Sol_V3_18LS      = Sol_V3_18L[V3_18_Y1maskLS] # Remove NaN values from Sol
Temp_V3_18LS     = Temp_V3_18L[V3_18_Y1maskLS] # Remove NaN values from Sol
WD_vect_V3_18LS  = WD_vect_V3_18L[V3_18_Y1maskLS] # Remove NaN values from Sol
WS_V3_18LS       = WS_V3_18L[V3_18_Y1maskLS] # Remove NaN values from Sol
Hg0_V3_18LS      = Hg0_V3_18L[V3_18_Y1maskLS] # Remove NaN values from Sol
SI_V3_18LS       = SI_V3_18L[V3_18_Y1maskLS] # Remove NaN values from Sol
RH_V3_18LS       = RH_V3_18L[V3_18_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_18_Y1maskLS   = np.isfinite(Sol_V3_18LS) # Scan for NaN values
BrO_V3_18LS      = BrO_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from BrO
O3_V3_18LS       = O3_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from Sol
Sol_V3_18LS      = Sol_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from Sol
Temp_V3_18LS     = Temp_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from Sol
WD_vect_V3_18LS  = WD_vect_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from Sol
WS_V3_18LS       = WS_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from Sol
Hg0_V3_18LS      = Hg0_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from Sol
SI_V3_18LS       = SI_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from Sol
RH_V3_18LS       = RH_V3_18LS[V3_18_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
V3_18_Y2maskLS   = np.isfinite(O3_V3_18LS) # Scan for NaN values
BrO_O3_V3_18LS   = BrO_V3_18LS[V3_18_Y2maskLS] # Remove NaN values from BrO
O3_V3_18LS       = O3_V3_18LS[V3_18_Y2maskLS] # Remove NaN values from Temp
Sol_O3_V3_18LS   = Sol_V3_18LS[V3_18_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_18_Y3maskLS   = np.isfinite(Temp_V3_18LS) # Scan for NaN values
BrO_Temp_V3_18LS = BrO_V3_18LS[V3_18_Y3maskLS] # Remove NaN values from BrO
Temp_V3_18LS     = Temp_V3_18LS[V3_18_Y3maskLS] # Remove NaN values from Temp
Sol_Temp_V3_18LS = Sol_V3_18LS[V3_18_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_18_Y4maskLS   = np.isfinite(WD_vect_V3_18LS) # Scan for NaN values
BrO_WD_V3_18LS   = BrO_V3_18LS[V3_18_Y4maskLS] # Remove NaN values from BrO
WD_vect_V3_18LS  = WD_vect_V3_18LS[V3_18_Y4maskLS] # Remove NaN values from WD_vect
Sol_WD_V3_18LS   = Sol_V3_18LS[V3_18_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_18_Y5maskLS   = np.isfinite(WS_V3_18LS) # Scan for NaN values
BrO_WS_V3_18LS   = BrO_V3_18LS[V3_18_Y5maskLS] # Remove NaN values from BrO
WS_V3_18LS       = WS_V3_18LS[V3_18_Y5maskLS] # Remove NaN values from WS
Sol_WS_V3_18LS   = Sol_V3_18LS[V3_18_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_18_Y6maskLS   = np.isfinite(Hg0_V3_18LS) # Scan for NaN values
BrO_Hg0_V3_18LS  = BrO_V3_18LS[V3_18_Y6maskLS] # Remove NaN values from BrO
Hg0_V3_18LS      = Hg0_V3_18LS[V3_18_Y6maskLS] # Remove NaN values from SI
Sol_Hg0_V3_18LS  = Sol_V3_18LS[V3_18_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_18_Y7maskLS   = np.isfinite(SI_V3_18LS) # Scan for NaN values
BrO_SI_V3_18LS   = BrO_V3_18LS[V3_18_Y7maskLS] # Remove NaN values from BrO
SI_SI_V3_18LS    = SI_V3_18LS[V3_18_Y7maskLS] # Remove NaN values from SI
Sol_SI_V3_18LS   = Sol_V3_18LS[V3_18_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_18_Y8maskLS   = np.isfinite(RH_V3_18LS) # Scan for NaN values
BrO_RH_V3_18LS   = BrO_V3_18LS[V3_18_Y8maskLS] # Remove NaN values from BrO
RH_V3_18LS       = RH_V3_18LS[V3_18_Y8maskLS] # Remove NaN values from WS
Sol_RH_V3_18LS   = Sol_V3_18LS[V3_18_Y8maskLS] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskLS  = np.isfinite(BrOLS) # Scan for NaN values
BrOLS         = BrOLS[ALL_Y1maskLS] # Remove NaN values from BrO
O3LS          = O3L[ALL_Y1maskLS] # Remove NaN values from Sol
SolLS         = SolL[ALL_Y1maskLS] # Remove NaN values from Sol
TempLS        = TempL[ALL_Y1maskLS] # Remove NaN values from Sol
WD_vectLS     = WD_vectL[ALL_Y1maskLS] # Remove NaN values from Sol
WSLS          = WSL[ALL_Y1maskLS] # Remove NaN values from Sol
Hg0LS         = Hg0L[ALL_Y1maskLS] # Remove NaN values from Sol
SILS          = SIL[ALL_Y1maskLS] # Remove NaN values from Sol
RHLS          = RHL[ALL_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
ALL_Y1maskLS  = np.isfinite(SolLS) # Scan for NaN values
BrOLS         = BrOLS[ALL_Y1maskLS] # Remove NaN values from BrO
O3LS          = O3LS[ALL_Y1maskLS] # Remove NaN values from Sol
SolLS         = SolLS[ALL_Y1maskLS] # Remove NaN values from Sol
TempLS        = TempLS[ALL_Y1maskLS] # Remove NaN values from Sol
WD_vectLS     = WD_vectLS[ALL_Y1maskLS] # Remove NaN values from Sol
WSLS          = WSLS[ALL_Y1maskLS] # Remove NaN values from Sol
Hg0LS         = Hg0LS[ALL_Y1maskLS] # Remove NaN values from Sol
SILS          = SILS[ALL_Y1maskLS] # Remove NaN values from Sol
RHLS          = RHLS[ALL_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
ALL_Y2maskLS  = np.isfinite(O3LS) # Scan for NaN values
BrO_O3LS      = BrOLS[ALL_Y2maskLS] # Remove NaN values from BrO
O3LS          = O3LS[ALL_Y2maskLS] # Remove NaN values from Temp
Sol_O3LS      = SolLS[ALL_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskLS  = np.isfinite(TempLS) # Scan for NaN values
BrO_TempLS    = BrOLS[ALL_Y3maskLS] # Remove NaN values from BrO
TempLS        = TempLS[ALL_Y3maskLS] # Remove NaN values from Temp
Sol_TempLS    = SolLS[ALL_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskLS  = np.isfinite(WD_vectLS) # Scan for NaN values
BrO_WDLS      = BrOLS[ALL_Y4maskLS] # Remove NaN values from BrO
WD_vectLS     = WD_vectLS[ALL_Y4maskLS] # Remove NaN values from WD_vect
Sol_WDLS      = SolLS[ALL_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskLS  = np.isfinite(WSLS) # Scan for NaN values
BrO_WSLS      = BrOLS[ALL_Y5maskLS] # Remove NaN values from BrO
WSLS          = WSLS[ALL_Y5maskLS] # Remove NaN values from WS
Sol_WSLS      = SolLS[ALL_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskLS  = np.isfinite(Hg0LS) # Scan for NaN values
BrO_Hg0LS     = BrOLS[ALL_Y6maskLS] # Remove NaN values from BrO
Hg0LS         = Hg0LS[ALL_Y6maskLS] # Remove NaN values from SI
Sol_Hg0LS     = SolLS[ALL_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskLS  = np.isfinite(SILS) # Scan for NaN values
BrO_SILS      = BrOLS[ALL_Y7maskLS] # Remove NaN values from BrO
SI_SILS       = SILS[ALL_Y7maskLS] # Remove NaN values from SI
Sol_SILS      = SolLS[ALL_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskLS  = np.isfinite(RHLS) # Scan for NaN values
BrO_RHLS      = BrOLS[ALL_Y8maskLS] # Remove NaN values from BrO
RHLS          = RHLS[ALL_Y8maskLS] # Remove NaN values from RH
Sol_RHLS      = SolLS[ALL_Y8maskLS] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#------------------------------------

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V1_17_Y1maskHS   = np.isfinite(BrO_V1_17HS) # Scan for NaN values
BrO_V1_17HS      = BrO_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from BrO
O3_V1_17HS       = O3_V1_17H[V1_17_Y1maskHS] # Remove NaN values from Sol
Sol_V1_17HS      = Sol_V1_17H[V1_17_Y1maskHS] # Remove NaN values from Sol
Temp_V1_17HS     = Temp_V1_17H[V1_17_Y1maskHS] # Remove NaN values from Sol
WD_vect_V1_17HS  = WD_vect_V1_17H[V1_17_Y1maskHS] # Remove NaN values from Sol
WS_V1_17HS       = WS_V1_17H[V1_17_Y1maskHS] # Remove NaN values from Sol
Hg0_V1_17HS      = Hg0_V1_17H[V1_17_Y1maskHS] # Remove NaN values from Sol
SI_V1_17HS       = SI_V1_17H[V1_17_Y1maskHS] # Remove NaN values from Sol
RH_V1_17HS       = RH_V1_17H[V1_17_Y1maskHS] # Remove NaN values from RH

# Pass 1 (Sol) 
V1_17_Y1maskHS   = np.isfinite(Sol_V1_17HS) # Scan for NaN values
BrO_V1_17HS      = BrO_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from BrO
O3_V1_17HS       = O3_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from Sol
Sol_V1_17HS      = Sol_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from Sol
Temp_V1_17HS     = Temp_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from Sol
WD_vect_V1_17HS  = WD_vect_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from Sol
WS_V1_17HS       = WS_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from Sol
Hg0_V1_17HS      = Hg0_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from Sol
SI_V1_17HS       = SI_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from Sol
RH_V1_17HS       = RH_V1_17HS[V1_17_Y1maskHS] # Remove NaN values from RH

# Pass 2 (O3) 
V1_17_Y2maskHS   = np.isfinite(O3_V1_17HS) # Scan for NaN values
BrO_O3_V1_17HS   = BrO_V1_17HS[V1_17_Y2maskHS] # Remove NaN values from BrO
O3_V1_17HS       = O3_V1_17HS[V1_17_Y2maskHS] # Remove NaN values from Temp
Sol_O3_V1_17S    = Sol_V1_17HS[V1_17_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_17_Y3maskHS   = np.isfinite(Temp_V1_17HS) # Scan for NaN values
BrO_Temp_V1_17HS = BrO_V1_17HS[V1_17_Y3maskHS] # Remove NaN values from BrO
Temp_V1_17HS     = Temp_V1_17HS[V1_17_Y3maskHS] # Remove NaN values from Temp
Sol_Temp_V1_17HS = Sol_V1_17HS[V1_17_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_17_Y4maskHS   = np.isfinite(WD_vect_V1_17HS) # Scan for NaN values
BrO_WD_V1_17HS   = BrO_V1_17HS[V1_17_Y4maskHS] # Remove NaN values from BrO
WD_vect_V1_17HS  = WD_vect_V1_17HS[V1_17_Y4maskHS] # Remove NaN values from WD_vect
Sol_WD_V1_17HS   = Sol_V1_17HS[V1_17_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_17_Y5maskHS   = np.isfinite(WS_V1_17HS) # Scan for NaN values
BrO_WS_V1_17HS   = BrO_V1_17HS[V1_17_Y5maskHS] # Remove NaN values from BrO
WS_V1_17HS       = WS_V1_17HS[V1_17_Y5maskHS] # Remove NaN values from WS
Sol_WS_V1_17HS   = Sol_V1_17HS[V1_17_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_17_Y6maskHS   = np.isfinite(Hg0_V1_17HS) # Scan for NaN values
BrO_Hg0_V1_17HS  = BrO_V1_17HS[V1_17_Y6maskHS] # Remove NaN values from BrO
Hg0_V1_17HS      = Hg0_V1_17HS[V1_17_Y6maskHS] # Remove NaN values from SI
Sol_Hg0_V1_17HS  = Sol_V1_17HS[V1_17_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_17_Y7maskHS   = np.isfinite(SI_V1_17HS) # Scan for NaN values
BrO_SI_V1_17HS   = BrO_V1_17HS[V1_17_Y7maskHS] # Remove NaN values from BrO
SI_SI_V1_17HS    = SI_V1_17HS[V1_17_Y7maskHS] # Remove NaN values from SI
Sol_SI_V1_17HS   = Sol_V1_17HS[V1_17_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_17_Y8maskHS   = np.isfinite(RH_V1_17HS) # Scan for NaN values
BrO_RH_V1_17HS   = BrO_V1_17HS[V1_17_Y8maskHS] # Remove NaN values from BrO
RH_V1_17HS       = RH_V1_17HS[V1_17_Y8maskHS] # Remove NaN values from WS
Sol_RH_V1_17HS   = Sol_V1_17HS[V1_17_Y8maskHS] # Remove NaN values from Sol

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V2_17_Y1maskHS   = np.isfinite(BrO_V2_17HS) # Scan for NaN values
BrO_V2_17HS      = BrO_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from BrO
O3_V2_17HS       = O3_V2_17H[V2_17_Y1maskHS] # Remove NaN values from Sol
Sol_V2_17HS      = Sol_V2_17H[V2_17_Y1maskHS] # Remove NaN values from Sol
Temp_V2_17HS     = Temp_V2_17H[V2_17_Y1maskHS] # Remove NaN values from Sol
WD_vect_V2_17HS  = WD_vect_V2_17H[V2_17_Y1maskHS] # Remove NaN values from Sol
WS_V2_17HS       = WS_V2_17H[V2_17_Y1maskHS] # Remove NaN values from Sol
Hg0_V2_17HS      = Hg0_V2_17H[V2_17_Y1maskHS] # Remove NaN values from Sol
SI_V2_17HS       = SI_V2_17H[V2_17_Y1maskHS] # Remove NaN values from Sol
RH_V2_17HS       = RH_V2_17H[V2_17_Y1maskHS] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_17_Y1maskHS   = np.isfinite(Sol_V2_17HS) # Scan for NaN values
BrO_V2_17HS      = BrO_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from BrO
O3_V2_17HS       = O3_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from Sol
Sol_V2_17HS      = Sol_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from Sol
Temp_V2_17HS     = Temp_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from Sol
WD_vect_V2_17HS  = WD_vect_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from Sol
WS_V2_17HS       = WS_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from Sol
Hg0_V2_17HS      = Hg0_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from Sol
SI_V2_17HS       = SI_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from Sol
RH_V2_17HS       = RH_V2_17HS[V2_17_Y1maskHS] # Remove NaN values from RH

# Pass 2 (O3) 
V2_17_Y2maskHS   = np.isfinite(O3_V2_17HS) # Scan for NaN values
BrO_O3_V2_17HS   = BrO_V2_17HS[V2_17_Y2maskHS] # Remove NaN values from BrO
O3_V2_17HS       = O3_V2_17HS[V2_17_Y2maskHS] # Remove NaN values from Temp
Sol_O3_V2_17HS   = Sol_V2_17HS[V2_17_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_17_Y3maskHS   = np.isfinite(Temp_V2_17HS) # Scan for NaN values
BrO_Temp_V2_17HS = BrO_V2_17HS[V2_17_Y3maskHS] # Remove NaN values from BrO
Temp_V2_17HS     = Temp_V2_17HS[V2_17_Y3maskHS] # Remove NaN values from Temp
Sol_Temp_V2_17HS = Sol_V2_17HS[V2_17_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_17_Y4maskHS   = np.isfinite(WD_vect_V2_17HS) # Scan for NaN values
BrO_WD_V2_17HS   = BrO_V2_17HS[V2_17_Y4maskHS] # Remove NaN values from BrO
WD_vect_V2_17HS  = WD_vect_V2_17HS[V2_17_Y4maskHS] # Remove NaN values from WD_vect
Sol_WD_V2_17HS   = Sol_V2_17HS[V2_17_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_17_Y5maskHS   = np.isfinite(WS_V2_17HS) # Scan for NaN values
BrO_WS_V2_17HS   = BrO_V2_17HS[V2_17_Y5maskHS] # Remove NaN values from BrO
WS_V2_17HS       = WS_V2_17HS[V2_17_Y5maskHS] # Remove NaN values from WS
Sol_WS_V2_17HS   = Sol_V2_17HS[V2_17_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_17_Y6maskHS   = np.isfinite(Hg0_V2_17HS) # Scan for NaN values
BrO_Hg0_V2_17HS  = BrO_V2_17HS[V2_17_Y6maskHS] # Remove NaN values from BrO
Hg0_V2_17HS      = Hg0_V2_17HS[V2_17_Y6maskHS] # Remove NaN values from SI
Sol_Hg0_V2_17HS  = Sol_V2_17HS[V2_17_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_17_Y7maskHS   = np.isfinite(SI_V2_17HS) # Scan for NaN values
BrO_SI_V2_17HS   = BrO_V2_17HS[V2_17_Y7maskHS] # Remove NaN values from BrO
SI_SI_V2_17HS    = SI_V2_17HS[V2_17_Y7maskHS] # Remove NaN values from SI
Sol_SI_V2_17HS   = Sol_V2_17HS[V2_17_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_17_Y8maskHS   = np.isfinite(RH_V2_17HS) # Scan for NaN values
BrO_RH_V2_17HS   = BrO_V2_17HS[V2_17_Y8maskHS] # Remove NaN values from BrO
RH_V2_17HS       = RH_V2_17HS[V2_17_Y8maskHS] # Remove NaN values from WS
Sol_RH_V2_17HS   = Sol_V2_17HS[V2_17_Y8maskHS] # Remove NaN values from Sol

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V3_17_Y1maskHS   = np.isfinite(BrO_V3_17HS) # Scan for NaN values
BrO_V3_17HS      = BrO_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from BrO
O3_V3_17HS       = O3_V3_17H[V3_17_Y1maskHS] # Remove NaN values from Sol
Sol_V3_17HS      = Sol_V3_17H[V3_17_Y1maskHS] # Remove NaN values from Sol
Temp_V3_17HS     = Temp_V3_17H[V3_17_Y1maskHS] # Remove NaN values from Sol
WD_vect_V3_17HS  = WD_vect_V3_17H[V3_17_Y1maskHS] # Remove NaN values from Sol
WS_V3_17HS       = WS_V3_17H[V3_17_Y1maskHS] # Remove NaN values from Sol
Hg0_V3_17HS      = Hg0_V3_17H[V3_17_Y1maskHS] # Remove NaN values from Sol
SI_V3_17HS       = SI_V3_17H[V3_17_Y1maskHS] # Remove NaN values from Sol
RH_V3_17HS       = RH_V3_17H[V3_17_Y1maskHS] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_17_Y1maskHS   = np.isfinite(Sol_V3_17HS) # Scan for NaN values
BrO_V3_17HS      = BrO_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from BrO
O3_V3_17HS       = O3_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from Sol
Sol_V3_17HS      = Sol_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from Sol
Temp_V3_17HS     = Temp_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from Sol
WD_vect_V3_17HS  = WD_vect_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from Sol
WS_V3_17HS       = WS_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from Sol
Hg0_V3_17HS      = Hg0_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from Sol
SI_V3_17HS       = SI_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from Sol
RH_V3_17HS       = RH_V3_17HS[V3_17_Y1maskHS] # Remove NaN values from RH

# Pass 2 (O3) 
V3_17_Y2maskHS   = np.isfinite(O3_V3_17HS) # Scan for NaN values
BrO_O3_V3_17HS   = BrO_V3_17HS[V3_17_Y2maskHS] # Remove NaN values from BrO
O3_V3_17HS       = O3_V3_17HS[V3_17_Y2maskHS] # Remove NaN values from Temp
Sol_O3_V3_17HS   = Sol_V3_17HS[V3_17_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_17_Y3maskHS   = np.isfinite(Temp_V3_17HS) # Scan for NaN values
BrO_Temp_V3_17HS = BrO_V3_17HS[V3_17_Y3maskHS] # Remove NaN values from BrO
Temp_V3_17HS     = Temp_V3_17HS[V3_17_Y3maskHS] # Remove NaN values from Temp
Sol_Temp_V3_17HS = Sol_V3_17HS[V3_17_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_17_Y4maskHS   = np.isfinite(WD_vect_V3_17HS) # Scan for NaN values
BrO_WD_V3_17HS   = BrO_V3_17HS[V3_17_Y4maskHS] # Remove NaN values from BrO
WD_vect_V3_17HS  = WD_vect_V3_17HS[V3_17_Y4maskHS] # Remove NaN values from WD_vect
Sol_WD_V3_17HS   = Sol_V3_17HS[V3_17_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_17_Y5maskHS   = np.isfinite(WS_V3_17HS) # Scan for NaN values
BrO_WS_V3_17HS   = BrO_V3_17HS[V3_17_Y5maskHS] # Remove NaN values from BrO
WS_V3_17HS       = WS_V3_17HS[V3_17_Y5maskHS] # Remove NaN values from WS
Sol_WS_V3_17HS   = Sol_V3_17HS[V3_17_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_17_Y6maskHS   = np.isfinite(Hg0_V3_17HS) # Scan for NaN values
BrO_Hg0_V3_17HS  = BrO_V3_17HS[V3_17_Y6maskHS] # Remove NaN values from BrO
Hg0_V3_17HS      = Hg0_V3_17HS[V3_17_Y6maskHS] # Remove NaN values from SI
Sol_Hg0_V3_17HS  = Sol_V3_17HS[V3_17_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_17_Y7maskHS   = np.isfinite(SI_V3_17HS) # Scan for NaN values
BrO_SI_V3_17HS   = BrO_V3_17HS[V3_17_Y7maskHS] # Remove NaN values from BrO
SI_SI_V3_17HS    = SI_V3_17HS[V3_17_Y7maskHS] # Remove NaN values from SI
Sol_SI_V3_17HS   = Sol_V3_17HS[V3_17_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_17_Y8maskHS   = np.isfinite(RH_V3_17HS) # Scan for NaN values
BrO_RH_V3_17HS   = BrO_V3_17HS[V3_17_Y8maskHS] # Remove NaN values from BrO
RH_V3_17HS       = RH_V3_17HS[V3_17_Y8maskHS] # Remove NaN values from WS
Sol_RH_V3_17HS   = Sol_V3_17HS[V3_17_Y8maskHS] # Remove NaN values from Sol

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (BrO)
V1_18_Y1maskHS   = np.isfinite(BrO_V1_18HS) # Scan for NaN values
BrO_V1_18HS      = BrO_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from BrO
O3_V1_18HS       = O3_V1_18H[V1_18_Y1maskHS] # Remove NaN values from Sol
Sol_V1_18HS      = Sol_V1_18H[V1_18_Y1maskHS] # Remove NaN values from Sol
Temp_V1_18HS     = Temp_V1_18H[V1_18_Y1maskHS] # Remove NaN values from Sol
WD_vect_V1_18HS  = WD_vect_V1_18H[V1_18_Y1maskHS] # Remove NaN values from Sol
WS_V1_18HS       = WS_V1_18H[V1_18_Y1maskHS] # Remove NaN values from Sol
Hg0_V1_18HS      = Hg0_V1_18H[V1_18_Y1maskHS] # Remove NaN values from Sol
SI_V1_18HS       = SI_V1_18H[V1_18_Y1maskHS] # Remove NaN values from Sol
RH_V1_18HS       = RH_V1_18H[V1_18_Y1maskHS] # Remove NaN values from RH

# Pass 1 (Sol)
V1_18_Y1maskHS   = np.isfinite(Sol_V1_18HS) # Scan for NaN values
BrO_V1_18HS      = BrO_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from BrO
O3_V1_18HS       = O3_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from Sol
Sol_V1_18HS      = Sol_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from Sol
Temp_V1_18HS     = Temp_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from Sol
WD_vect_V1_18HS  = WD_vect_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from Sol
WS_V1_18HS       = WS_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from Sol
Hg0_V1_18HS      = Hg0_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from Sol
SI_V1_18HS       = SI_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from Sol
RH_V1_18HS       = RH_V1_18HS[V1_18_Y1maskHS] # Remove NaN values from RH

# Pass 2 (O3) 
V1_18_Y2maskHS   = np.isfinite(O3_V1_18HS) # Scan for NaN values
BrO_O3_V1_18HS   = BrO_V1_18HS[V1_18_Y2maskHS] # Remove NaN values from BrO
O3_V1_18HS       = O3_V1_18HS[V1_18_Y2maskHS] # Remove NaN values from Temp
Sol_O3_V1_18HS   = Sol_V1_18HS[V1_18_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_18_Y3maskHS   = np.isfinite(Temp_V1_18HS) # Scan for NaN values
BrO_Temp_V1_18HS = BrO_V1_18HS[V1_18_Y3maskHS] # Remove NaN values from BrO
Temp_V1_18HS     = Temp_V1_18HS[V1_18_Y3maskHS] # Remove NaN values from Temp
Sol_Temp_V1_18HS = Sol_V1_18HS[V1_18_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_18_Y4maskHS   = np.isfinite(WD_vect_V1_18HS) # Scan for NaN values
BrO_WD_V1_18HS   = BrO_V1_18HS[V1_18_Y4maskHS] # Remove NaN values from BrO
WD_vect_V1_18HS  = WD_vect_V1_18HS[V1_18_Y4maskHS] # Remove NaN values from WD_vect
Sol_WD_V1_18HS   = Sol_V1_18HS[V1_18_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_18_Y5maskHS   = np.isfinite(WS_V1_18HS) # Scan for NaN values
BrO_WS_V1_18HS   = BrO_V1_18HS[V1_18_Y5maskHS] # Remove NaN values from BrO
WS_V1_18HS       = WS_V1_18HS[V1_18_Y5maskHS] # Remove NaN values from WS
Sol_WS_V1_18HS   = Sol_V1_18HS[V1_18_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_18_Y6maskHS   = np.isfinite(Hg0_V1_18HS) # Scan for NaN values
BrO_Hg0_V1_18HS  = BrO_V1_18HS[V1_18_Y6maskHS] # Remove NaN values from BrO
Hg0_V1_18HS      = Hg0_V1_18HS[V1_18_Y6maskHS] # Remove NaN values from SI
Sol_Hg0_V1_18HS  = Sol_V1_18HS[V1_18_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_18_Y7maskHS   = np.isfinite(SI_V1_18HS) # Scan for NaN values
BrO_SI_V1_18HS   = BrO_V1_18HS[V1_18_Y7maskHS] # Remove NaN values from BrO
SI_SI_V1_18HS    = SI_V1_18HS[V1_18_Y7maskHS] # Remove NaN values from SI
Sol_SI_V1_18HS   = Sol_V1_18HS[V1_18_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_18_Y8maskHS   = np.isfinite(RH_V1_18HS) # Scan for NaN values
BrO_RH_V1_18HS   = BrO_V1_18HS[V1_18_Y8maskHS] # Remove NaN values from BrO
RH_V1_18HS       = RH_V1_18HS[V1_18_Y8maskHS] # Remove NaN values from WS
Sol_RH_V1_18HS   = Sol_V1_18HS[V1_18_Y8maskHS] # Remove NaN values from Sol

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (BrO) 
V2_18_Y1maskHS   = np.isfinite(BrO_V2_18HS) # Scan for NaN values
BrO_V2_18HS      = BrO_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from BrO
O3_V2_18HS       = O3_V2_18H[V2_18_Y1maskHS] # Remove NaN values from Sol
Sol_V2_18HS      = Sol_V2_18H[V2_18_Y1maskHS] # Remove NaN values from Sol
Temp_V2_18HS     = Temp_V2_18H[V2_18_Y1maskHS] # Remove NaN values from Sol
WD_vect_V2_18HS  = WD_vect_V2_18H[V2_18_Y1maskHS] # Remove NaN values from Sol
WS_V2_18HS       = WS_V2_18H[V2_18_Y1maskHS] # Remove NaN values from Sol
Hg0_V2_18HS      = Hg0_V2_18H[V2_18_Y1maskHS] # Remove NaN values from Sol
SI_V2_18HS       = SI_V2_18H[V2_18_Y1maskHS] # Remove NaN values from Sol
RH_V2_18HS       = RH_V2_18H[V2_18_Y1maskHS] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_18_Y1maskHS   = np.isfinite(Sol_V2_18HS) # Scan for NaN values
BrO_V2_18HS      = BrO_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from BrO
O3_V2_18HS       = O3_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from Sol
Sol_V2_18HS      = Sol_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from Sol
Temp_V2_18HS     = Temp_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from Sol
WD_vect_V2_18HS  = WD_vect_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from Sol
WS_V2_18HS       = WS_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from Sol
Hg0_V2_18HS      = Hg0_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from Sol
SI_V2_18HS       = SI_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from Sol
RH_V2_18HS       = RH_V2_18HS[V2_18_Y1maskHS] # Remove NaN values from RH

# Pass 2 (O3) 
V2_18_Y2maskHS   = np.isfinite(O3_V2_18HS) # Scan for NaN values
BrO_O3_V2_18HS   = BrO_V2_18HS[V2_18_Y2maskHS] # Remove NaN values from BrO
O3_V2_18HS       = O3_V2_18HS[V2_18_Y2maskHS] # Remove NaN values from Temp
Sol_O3_V2_18HS   = Sol_V2_18HS[V2_18_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_18_Y3maskHS   = np.isfinite(Temp_V2_18HS) # Scan for NaN values
BrO_Temp_V2_18HS = BrO_V2_18HS[V2_18_Y3maskHS] # Remove NaN values from BrO
Temp_V2_18HS     = Temp_V2_18HS[V2_18_Y3maskHS] # Remove NaN values from Temp
Sol_Temp_V2_18HS = Sol_V2_18HS[V2_18_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_18_Y4maskHS   = np.isfinite(WD_vect_V2_18HS) # Scan for NaN values
BrO_WD_V2_18HS   = BrO_V2_18HS[V2_18_Y4maskHS] # Remove NaN values from BrO
WD_vect_V2_18HS  = WD_vect_V2_18HS[V2_18_Y4maskHS] # Remove NaN values from WD_vect
Sol_WD_V2_18HS   = Sol_V2_18HS[V2_18_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_18_Y5maskHS   = np.isfinite(WS_V2_18HS) # Scan for NaN values
BrO_WS_V2_18HS   = BrO_V2_18HS[V2_18_Y5maskHS] # Remove NaN values from BrO
WS_V2_18HS       = WS_V2_18HS[V2_18_Y5maskHS] # Remove NaN values from WS
Sol_WS_V2_18HS   = Sol_V2_18HS[V2_18_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_18_Y6maskHS   = np.isfinite(Hg0_V2_18HS) # Scan for NaN values
BrO_Hg0_V2_18HS  = BrO_V2_18HS[V2_18_Y6maskHS] # Remove NaN values from BrO
Hg0_V2_18HS      = Hg0_V2_18HS[V2_18_Y6maskHS] # Remove NaN values from SI
Sol_Hg0_V2_18HS  = Sol_V2_18HS[V2_18_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_18_Y7maskHS   = np.isfinite(SI_V2_18HS) # Scan for NaN values
BrO_SI_V2_18HS   = BrO_V2_18HS[V2_18_Y7maskHS] # Remove NaN values from BrO
SI_SI_V2_18HS    = SI_V2_18HS[V2_18_Y7maskHS] # Remove NaN values from SI
Sol_SI_V2_18HS   = Sol_V2_18HS[V2_18_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_18_Y8maskHS   = np.isfinite(RH_V2_18HS) # Scan for NaN values
BrO_RH_V2_18HS   = BrO_V2_18HS[V2_18_Y8maskHS] # Remove NaN values from BrO
RH_V2_18HS       = RH_V2_18HS[V2_18_Y8maskHS] # Remove NaN values from WS
Sol_RH_V2_18HS   = Sol_V2_18HS[V2_18_Y8maskHS] # Remove NaN values from Sol

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (BrO) 
V3_18_Y1maskHS   = np.isfinite(BrO_V3_18HS) # Scan for NaN values
BrO_V3_18HS      = BrO_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from BrO
O3_V3_18HS       = O3_V3_18H[V3_18_Y1maskHS] # Remove NaN values from Sol
Sol_V3_18HS      = Sol_V3_18H[V3_18_Y1maskHS] # Remove NaN values from Sol
Temp_V3_18HS     = Temp_V3_18H[V3_18_Y1maskHS] # Remove NaN values from Sol
WD_vect_V3_18HS  = WD_vect_V3_18H[V3_18_Y1maskHS] # Remove NaN values from Sol
WS_V3_18HS       = WS_V3_18H[V3_18_Y1maskHS] # Remove NaN values from Sol
Hg0_V3_18HS      = Hg0_V3_18H[V3_18_Y1maskHS] # Remove NaN values from Sol
SI_V3_18HS       = SI_V3_18H[V3_18_Y1maskHS] # Remove NaN values from Sol
RH_V3_18HS       = RH_V3_18H[V3_18_Y1maskHS] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_18_Y1maskHS   = np.isfinite(Sol_V3_18HS) # Scan for NaN values
BrO_V3_18HS      = BrO_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from BrO
O3_V3_18HS       = O3_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from Sol
Sol_V3_18HS      = Sol_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from Sol
Temp_V3_18HS     = Temp_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from Sol
WD_vect_V3_18HS  = WD_vect_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from Sol
WS_V3_18HS       = WS_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from Sol
Hg0_V3_18HS      = Hg0_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from Sol
SI_V3_18HS       = SI_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from Sol
RH_V3_18HS       = RH_V3_18HS[V3_18_Y1maskHS] # Remove NaN values from RH

# Pass 2 (O3) 
V3_18_Y2maskHS   = np.isfinite(O3_V3_18HS) # Scan for NaN values
BrO_O3_V3_18HS   = BrO_V3_18HS[V3_18_Y2maskHS] # Remove NaN values from BrO
O3_V3_18HS       = O3_V3_18HS[V3_18_Y2maskHS] # Remove NaN values from Temp
Sol_O3_V3_18HS   = Sol_V3_18HS[V3_18_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_18_Y3maskHS   = np.isfinite(Temp_V3_18HS) # Scan for NaN values
BrO_Temp_V3_18HS = BrO_V3_18HS[V3_18_Y3maskHS] # Remove NaN values from BrO
Temp_V3_18HS     = Temp_V3_18HS[V3_18_Y3maskHS] # Remove NaN values from Temp
Sol_Temp_V3_18HS = Sol_V3_18HS[V3_18_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_18_Y4maskHS   = np.isfinite(WD_vect_V3_18HS) # Scan for NaN values
BrO_WD_V3_18HS   = BrO_V3_18HS[V3_18_Y4maskHS] # Remove NaN values from BrO
WD_vect_V3_18HS  = WD_vect_V3_18HS[V3_18_Y4maskHS] # Remove NaN values from WD_vect
Sol_WD_V3_18HS   = Sol_V3_18HS[V3_18_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_18_Y5maskHS   = np.isfinite(WS_V3_18HS) # Scan for NaN values
BrO_WS_V3_18HS   = BrO_V3_18HS[V3_18_Y5maskHS] # Remove NaN values from BrO
WS_V3_18HS       = WS_V3_18HS[V3_18_Y5maskHS] # Remove NaN values from WS
Sol_WS_V3_18HS   = Sol_V3_18HS[V3_18_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_18_Y6maskHS   = np.isfinite(Hg0_V3_18HS) # Scan for NaN values
BrO_Hg0_V3_18HS  = BrO_V3_18HS[V3_18_Y6maskHS] # Remove NaN values from BrO
Hg0_V3_18HS      = Hg0_V3_18HS[V3_18_Y6maskHS] # Remove NaN values from SI
Sol_Hg0_V3_18HS  = Sol_V3_18HS[V3_18_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_18_Y7maskHS   = np.isfinite(SI_V3_18HS) # Scan for NaN values
BrO_SI_V3_18HS   = BrO_V3_18HS[V3_18_Y7maskHS] # Remove NaN values from BrO
SI_SI_V3_18HS    = SI_V3_18HS[V3_18_Y7maskHS] # Remove NaN values from SI
Sol_SI_V3_18HS   = Sol_V3_18HS[V3_18_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_18_Y8maskHS   = np.isfinite(RH_V3_18HS) # Scan for NaN values
BrO_RH_V3_18HS   = BrO_V3_18HS[V3_18_Y8maskHS] # Remove NaN values from BrO
RH_V3_18HS       = RH_V3_18HS[V3_18_Y8maskHS] # Remove NaN values from WS
Sol_RH_V3_18HS   = Sol_V3_18HS[V3_18_Y8maskHS] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskHS   = np.isfinite(BrOHS) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHS] # Remove NaN values from BrO
O3HS           = O3H[ALL_Y1maskHS] # Remove NaN values from Sol
SolHS          = SolH[ALL_Y1maskHS] # Remove NaN values from Sol
TempHS         = TempH[ALL_Y1maskHS] # Remove NaN values from Sol
WD_vectHS      = WD_vectH[ALL_Y1maskHS] # Remove NaN values from Sol
WSHS           = WSH[ALL_Y1maskHS] # Remove NaN values from Sol
Hg0HS          = Hg0H[ALL_Y1maskHS] # Remove NaN values from Sol
SIHS           = SIH[ALL_Y1maskHS] # Remove NaN values from Sol
RHHS          = RHH[ALL_Y1maskHS] # Remove NaN values from WS

# Pass 1 (Sol) 
ALL_Y1maskHS   = np.isfinite(SolHS) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHS] # Remove NaN values from BrO
O3HS           = O3HS[ALL_Y1maskHS] # Remove NaN values from Sol
SolHS          = SolHS[ALL_Y1maskHS] # Remove NaN values from Sol
TempHS         = TempHS[ALL_Y1maskHS] # Remove NaN values from Sol
WD_vectHS      = WD_vectHS[ALL_Y1maskHS] # Remove NaN values from Sol
WSHS           = WSHS[ALL_Y1maskHS] # Remove NaN values from Sol
Hg0HS          = Hg0HS[ALL_Y1maskHS] # Remove NaN values from Sol
SIHS           = SIHS[ALL_Y1maskHS] # Remove NaN values from Sol
RHHS          = RHHS[ALL_Y1maskHS] # Remove NaN values from WS

# Pass 2 (O3) 
ALL_Y2maskHS   = np.isfinite(O3HS) # Scan for NaN values
BrO_O3HS       = BrOHS[ALL_Y2maskHS] # Remove NaN values from BrO
O3HS           = O3HS[ALL_Y2maskHS] # Remove NaN values from Temp
Sol_O3HS       = SolHS[ALL_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskHS   = np.isfinite(TempHS) # Scan for NaN values
BrO_TempHS     = BrOHS[ALL_Y3maskHS] # Remove NaN values from BrO
TempHS         = TempHS[ALL_Y3maskHS] # Remove NaN values from Temp
Sol_TempS      = SolHS[ALL_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskHS   = np.isfinite(WD_vectHS) # Scan for NaN values
BrO_WDHS       = BrOHS[ALL_Y4maskHS] # Remove NaN values from BrO
WD_vectHS      = WD_vectHS[ALL_Y4maskHS] # Remove NaN values from WD_vect
Sol_WDHS       = SolHS[ALL_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskHS   = np.isfinite(WSHS) # Scan for NaN values
BrO_WSHS       = BrOHS[ALL_Y5maskHS] # Remove NaN values from BrO
WSHS           = WSHS[ALL_Y5maskHS] # Remove NaN values from WS
Sol_WSHS       = SolHS[ALL_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskHS   = np.isfinite(Hg0HS) # Scan for NaN values
BrO_Hg0HS      = BrOHS[ALL_Y6maskHS] # Remove NaN values from BrO
Hg0HS          = Hg0HS[ALL_Y6maskHS] # Remove NaN values from SI
Sol_Hg0HS      = SolHS[ALL_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskHS   = np.isfinite(SIHS) # Scan for NaN values
BrO_SIHS       = BrOHS[ALL_Y7maskHS] # Remove NaN values from BrO
SI_SIHS        = SIHS[ALL_Y7maskHS] # Remove NaN values from SI
Sol_SIHS       = SolHS[ALL_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskHS  = np.isfinite(RHHS) # Scan for NaN values
BrO_RHHS      = BrOHS[ALL_Y8maskHS] # Remove NaN values from BrO
RHHS          = RHHS[ALL_Y8maskHS] # Remove NaN values from WS
Sol_RHHS      = SolHS[ALL_Y8maskHS] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V1_17_Y1maskLB   = np.isfinite(BrO_V1_17LB) # Scan for NaN values
BrO_V1_17LB      = BrO_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from BrO
O3_V1_17LB       = O3_V1_17L[V1_17_Y1maskLB] # Remove NaN values from Sol
Sol_V1_17LB      = Sol_V1_17L[V1_17_Y1maskLB] # Remove NaN values from Sol
Temp_V1_17LB     = Temp_V1_17L[V1_17_Y1maskLB] # Remove NaN values from Sol
WD_vect_V1_17LB  = WD_vect_V1_17L[V1_17_Y1maskLB] # Remove NaN values from Sol
WS_V1_17LB       = WS_V1_17L[V1_17_Y1maskLB] # Remove NaN values from Sol
Hg0_V1_17LB      = Hg0_V1_17L[V1_17_Y1maskLB] # Remove NaN values from Sol
SI_V1_17LB       = SI_V1_17L[V1_17_Y1maskLB] # Remove NaN values from Sol
RH_V1_17LB       = RH_V1_17L[V1_17_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
V1_17_Y1maskLB   = np.isfinite(Sol_V1_17LB) # Scan for NaN values
BrO_V1_17LB      = BrO_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from BrO
O3_V1_17LB       = O3_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from Sol
Sol_V1_17LB      = Sol_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from Sol
Temp_V1_17LB     = Temp_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from Sol
WD_vect_V1_17LB  = WD_vect_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from Sol
WS_V1_17LB       = WS_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from Sol
Hg0_V1_17LB      = Hg0_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from Sol
SI_V1_17LB       = SI_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from Sol
RH_V1_17LB       = RH_V1_17LB[V1_17_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
V1_17_Y2maskLB   = np.isfinite(O3_V1_17LB) # Scan for NaN values
BrO_O3_V1_17LB   = BrO_V1_17LB[V1_17_Y2maskLB] # Remove NaN values from BrO
O3_V1_17LB       = O3_V1_17LB[V1_17_Y2maskLB] # Remove NaN values from Temp
Sol_O3_V1_17LB   = Sol_V1_17LB[V1_17_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_17_Y3maskLB   = np.isfinite(Temp_V1_17LB) # Scan for NaN values
BrO_Temp_V1_17LB = BrO_V1_17LB[V1_17_Y3maskLB] # Remove NaN values from BrO
Temp_V1_17LB     = Temp_V1_17LB[V1_17_Y3maskLB] # Remove NaN values from Temp
Sol_Temp_V1_17LB = Sol_V1_17LB[V1_17_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_17_Y4maskLB   = np.isfinite(WD_vect_V1_17LB) # Scan for NaN values
BrO_WD_V1_17LB   = BrO_V1_17LB[V1_17_Y4maskLB] # Remove NaN values from BrO
WD_vect_V1_17LB  = WD_vect_V1_17LB[V1_17_Y4maskLB] # Remove NaN values from WD_vect
Sol_WD_V1_17LB   = Sol_V1_17LB[V1_17_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_17_Y5maskLB   = np.isfinite(WS_V1_17LB) # Scan for NaN values
BrO_WS_V1_17LB   = BrO_V1_17LB[V1_17_Y5maskLB] # Remove NaN values from BrO
WS_V1_17LB       = WS_V1_17LB[V1_17_Y5maskLB] # Remove NaN values from WS
Sol_WS_V1_17LB   = Sol_V1_17LB[V1_17_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_17_Y6maskLB   = np.isfinite(Hg0_V1_17LB) # Scan for NaN values
BrO_Hg0_V1_17LB  = BrO_V1_17LB[V1_17_Y6maskLB] # Remove NaN values from BrO
Hg0_V1_17LB      = Hg0_V1_17LB[V1_17_Y6maskLB] # Remove NaN values from SI
Sol_Hg0_V1_17LB  = Sol_V1_17LB[V1_17_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_17_Y7maskLB   = np.isfinite(SI_V1_17LB) # Scan for NaN values
BrO_SI_V1_17LB   = BrO_V1_17LB[V1_17_Y7maskLB] # Remove NaN values from BrO
SI_SI_V1_17LB    = SI_V1_17LB[V1_17_Y7maskLB] # Remove NaN values from SI
Sol_SI_V1_17LB   = Sol_V1_17LB[V1_17_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_17_Y8maskLB   = np.isfinite(RH_V1_17LB) # Scan for NaN values
BrO_RH_V1_17LB   = BrO_V1_17LB[V1_17_Y8maskLB] # Remove NaN values from BrO
RH_V1_17LB       = RH_V1_17LB[V1_17_Y8maskLB] # Remove NaN values from RH
Sol_RH_V1_17LB   = Sol_V1_17LB[V1_17_Y8maskLB] # Remove NaN values from Sol

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V2_17_Y1maskLB   = np.isfinite(BrO_V2_17LB) # Scan for NaN values
BrO_V2_17LB      = BrO_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from BrO
O3_V2_17LB       = O3_V2_17L[V2_17_Y1maskLB] # Remove NaN values from Sol
Sol_V2_17LB      = Sol_V2_17L[V2_17_Y1maskLB] # Remove NaN values from Sol
Temp_V2_17LB     = Temp_V2_17L[V2_17_Y1maskLB] # Remove NaN values from Sol
WD_vect_V2_17LB  = WD_vect_V2_17L[V2_17_Y1maskLB] # Remove NaN values from Sol
WS_V2_17LB       = WS_V2_17L[V2_17_Y1maskLB] # Remove NaN values from Sol
Hg0_V2_17LB      = Hg0_V2_17L[V2_17_Y1maskLB] # Remove NaN values from Sol
SI_V2_17LB       = SI_V2_17L[V2_17_Y1maskLB] # Remove NaN values from Sol
RH_V2_17LB       = RH_V2_17L[V2_17_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_17_Y1maskLB   = np.isfinite(Sol_V2_17LB) # Scan for NaN values
BrO_V2_17LB      = BrO_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from BrO
O3_V2_17LB       = O3_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from Sol
Sol_V2_17LB      = Sol_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from Sol
Temp_V2_17LB     = Temp_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from Sol
WD_vect_V2_17LB  = WD_vect_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from Sol
WS_V2_17LB       = WS_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from Sol
Hg0_V2_17LB      = Hg0_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from Sol
SI_V2_17LB       = SI_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from Sol
RH_V2_17LB       = RH_V2_17LB[V2_17_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
V2_17_Y2maskLB   = np.isfinite(O3_V2_17LB) # Scan for NaN values
BrO_O3_V2_17LB   = BrO_V2_17LB[V2_17_Y2maskLB] # Remove NaN values from BrO
O3_V2_17LB       = O3_V2_17LB[V2_17_Y2maskLB] # Remove NaN values from Temp
Sol_O3_V2_17LB   = Sol_V2_17LB[V2_17_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_17_Y3maskLB   = np.isfinite(Temp_V2_17LB) # Scan for NaN values
BrO_Temp_V2_17LB = BrO_V2_17LB[V2_17_Y3maskLB] # Remove NaN values from BrO
Temp_V2_17LB     = Temp_V2_17LB[V2_17_Y3maskLB] # Remove NaN values from Temp
Sol_Temp_V2_17LB = Sol_V2_17LB[V2_17_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_17_Y4maskLB   = np.isfinite(WD_vect_V2_17LB) # Scan for NaN values
BrO_WD_V2_17LB   = BrO_V2_17LB[V2_17_Y4maskLB] # Remove NaN values from BrO
WD_vect_V2_17LB  = WD_vect_V2_17LB[V2_17_Y4maskLB] # Remove NaN values from WD_vect
Sol_WD_V2_17LB   = Sol_V2_17LB[V2_17_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_17_Y5maskLB   = np.isfinite(WS_V2_17LB) # Scan for NaN values
BrO_WS_V2_17LB   = BrO_V2_17LB[V2_17_Y5maskLB] # Remove NaN values from BrO
WS_V2_17LB       = WS_V2_17LB[V2_17_Y5maskLB] # Remove NaN values from WS
Sol_WS_V2_17LB   = Sol_V2_17LB[V2_17_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_17_Y6maskLB   = np.isfinite(Hg0_V2_17LB) # Scan for NaN values
BrO_Hg0_V2_17LB  = BrO_V2_17LB[V2_17_Y6maskLB] # Remove NaN values from BrO
Hg0_V2_17LB      = Hg0_V2_17LB[V2_17_Y6maskLB] # Remove NaN values from SI
Sol_Hg0_V2_17LB  = Sol_V2_17LB[V2_17_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_17_Y7maskLB   = np.isfinite(SI_V2_17LB) # Scan for NaN values
BrO_SI_V2_17LB   = BrO_V2_17LB[V2_17_Y7maskLB] # Remove NaN values from BrO
SI_SI_V2_17LB    = SI_V2_17LB[V2_17_Y7maskLB] # Remove NaN values from SI
Sol_SI_V2_17LB   = Sol_V2_17LB[V2_17_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_17_Y8maskLB   = np.isfinite(RH_V2_17LB) # Scan for NaN values
BrO_RH_V2_17LB   = BrO_V2_17LB[V2_17_Y8maskLB] # Remove NaN values from BrO
RH_V2_17LB       = RH_V2_17LB[V2_17_Y8maskLB] # Remove NaN values from WS
Sol_RH_V2_17LB   = Sol_V2_17LB[V2_17_Y8maskLB] # Remove NaN values from Sol

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V3_17_Y1maskLB   = np.isfinite(BrO_V3_17LB) # Scan for NaN values
BrO_V3_17LB      = BrO_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from BrO
O3_V3_17LB       = O3_V3_17L[V3_17_Y1maskLB] # Remove NaN values from Sol
Sol_V3_17LB      = Sol_V3_17L[V3_17_Y1maskLB] # Remove NaN values from Sol
Temp_V3_17LB     = Temp_V3_17L[V3_17_Y1maskLB] # Remove NaN values from Sol
WD_vect_V3_17LB  = WD_vect_V3_17L[V3_17_Y1maskLB] # Remove NaN values from Sol
WS_V3_17LB       = WS_V3_17L[V3_17_Y1maskLB] # Remove NaN values from Sol
Hg0_V3_17LB      = Hg0_V3_17L[V3_17_Y1maskLB] # Remove NaN values from Sol
SI_V3_17LB       = SI_V3_17L[V3_17_Y1maskLB] # Remove NaN values from Sol
RH_V3_17LB       = RH_V3_17L[V3_17_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_17_Y1maskLB   = np.isfinite(Sol_V3_17LB) # Scan for NaN values
BrO_V3_17LB      = BrO_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from BrO
O3_V3_17LB       = O3_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from Sol
Sol_V3_17LB      = Sol_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from Sol
Temp_V3_17LB     = Temp_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from Sol
WD_vect_V3_17LB  = WD_vect_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from Sol
WS_V3_17LB       = WS_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from Sol
Hg0_V3_17LB      = Hg0_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from Sol
SI_V3_17LB       = SI_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from Sol
RH_V3_17LB       = RH_V3_17LB[V3_17_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
V3_17_Y2maskLB   = np.isfinite(O3_V3_17LB) # Scan for NaN values
BrO_O3_V3_17LB   = BrO_V3_17LB[V3_17_Y2maskLB] # Remove NaN values from BrO
O3_V3_17LB       = O3_V3_17LB[V3_17_Y2maskLB] # Remove NaN values from Temp
Sol_O3_V3_17LB   = Sol_V3_17LB[V3_17_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_17_Y3maskLB   = np.isfinite(Temp_V3_17LB) # Scan for NaN values
BrO_Temp_V3_17LB = BrO_V3_17LB[V3_17_Y3maskLB] # Remove NaN values from BrO
Temp_V3_17LB     = Temp_V3_17LB[V3_17_Y3maskLB] # Remove NaN values from Temp
Sol_Temp_V3_17LB = Sol_V3_17LB[V3_17_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_17_Y4maskLB   = np.isfinite(WD_vect_V3_17LB) # Scan for NaN values
BrO_WD_V3_17LB   = BrO_V3_17LB[V3_17_Y4maskLB] # Remove NaN values from BrO
WD_vect_V3_17LB  = WD_vect_V3_17LB[V3_17_Y4maskLB] # Remove NaN values from WD_vect
Sol_WD_V3_17LB   = Sol_V3_17LB[V3_17_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_17_Y5maskLB   = np.isfinite(WS_V3_17LB) # Scan for NaN values
BrO_WS_V3_17LB   = BrO_V3_17LB[V3_17_Y5maskLB] # Remove NaN values from BrO
WS_V3_17LB       = WS_V3_17LB[V3_17_Y5maskLB] # Remove NaN values from WS
Sol_WS_V3_17LB   = Sol_V3_17LB[V3_17_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_17_Y6maskLB   = np.isfinite(Hg0_V3_17LB) # Scan for NaN values
BrO_Hg0_V3_17LB  = BrO_V3_17LB[V3_17_Y6maskLB] # Remove NaN values from BrO
Hg0_V3_17LB      = Hg0_V3_17LB[V3_17_Y6maskLB] # Remove NaN values from SI
Sol_Hg0_V3_17LB  = Sol_V3_17LB[V3_17_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_17_Y7maskLB   = np.isfinite(SI_V3_17LB) # Scan for NaN values
BrO_SI_V3_17LB   = BrO_V3_17LB[V3_17_Y7maskLB] # Remove NaN values from BrO
SI_SI_V3_17LB    = SI_V3_17LB[V3_17_Y7maskLB] # Remove NaN values from SI
Sol_SI_V3_17LB   = Sol_V3_17LB[V3_17_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_17_Y8maskLB   = np.isfinite(RH_V3_17LB) # Scan for NaN values
BrO_RH_V3_17LB   = BrO_V3_17LB[V3_17_Y8maskLB] # Remove NaN values from BrO
RH_V3_17LB       = RH_V3_17LB[V3_17_Y8maskLB] # Remove NaN values from WS
Sol_RH_V3_17LB   = Sol_V3_17LB[V3_17_Y8maskLB] # Remove NaN values from Sol

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (BrO)
V1_18_Y1maskLB   = np.isfinite(BrO_V1_18LB) # Scan for NaN values
BrO_V1_18LB      = BrO_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from BrO
O3_V1_18LB       = O3_V1_18L[V1_18_Y1maskLB] # Remove NaN values from Sol
Sol_V1_18LB      = Sol_V1_18L[V1_18_Y1maskLB] # Remove NaN values from Sol
Temp_V1_18LB     = Temp_V1_18L[V1_18_Y1maskLB] # Remove NaN values from Sol
WD_vect_V1_18LB  = WD_vect_V1_18L[V1_18_Y1maskLB] # Remove NaN values from Sol
WS_V1_18LB       = WS_V1_18L[V1_18_Y1maskLB] # Remove NaN values from Sol
Hg0_V1_18LB      = Hg0_V1_18L[V1_18_Y1maskLB] # Remove NaN values from Sol
SI_V1_18LB       = SI_V1_18L[V1_18_Y1maskLB] # Remove NaN values from Sol
RH_V1_18LB       = RH_V1_18L[V1_18_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
V1_18_Y1maskLB   = np.isfinite(Sol_V1_18LB) # Scan for NaN values
BrO_V1_18LB      = BrO_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from BrO
O3_V1_18LB       = O3_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from Sol
Sol_V1_18LB      = Sol_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from Sol
Temp_V1_18LB     = Temp_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from Sol
WD_vect_V1_18LB  = WD_vect_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from Sol
WS_V1_18LB       = WS_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from Sol
Hg0_V1_18LB      = Hg0_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from Sol
SI_V1_18LB       = SI_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from Sol
RH_V1_18LB       = RH_V1_18LB[V1_18_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
V1_18_Y2maskLB   = np.isfinite(O3_V1_18LB) # Scan for NaN values
BrO_O3_V1_18LB   = BrO_V1_18LB[V1_18_Y2maskLB] # Remove NaN values from BrO
O3_V1_18LB       = O3_V1_18LB[V1_18_Y2maskLB] # Remove NaN values from Temp
Sol_O3_V1_18LB   = Sol_V1_18LB[V1_18_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_18_Y3maskLB   = np.isfinite(Temp_V1_18LB) # Scan for NaN values
BrO_Temp_V1_18LB = BrO_V1_18LB[V1_18_Y3maskLB] # Remove NaN values from BrO
Temp_V1_18LB     = Temp_V1_18LB[V1_18_Y3maskLB] # Remove NaN values from Temp
Sol_Temp_V1_18LB = Sol_V1_18LB[V1_18_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_18_Y4maskLB   = np.isfinite(WD_vect_V1_18LB) # Scan for NaN values
BrO_WD_V1_18LB   = BrO_V1_18LB[V1_18_Y4maskLB] # Remove NaN values from BrO
WD_vect_V1_18LB  = WD_vect_V1_18LB[V1_18_Y4maskLB] # Remove NaN values from WD_vect
Sol_WD_V1_18LB   = Sol_V1_18LB[V1_18_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_18_Y5maskLB   = np.isfinite(WS_V1_18LB) # Scan for NaN values
BrO_WS_V1_18LB   = BrO_V1_18LB[V1_18_Y5maskLB] # Remove NaN values from BrO
WS_V1_18LB       = WS_V1_18LB[V1_18_Y5maskLB] # Remove NaN values from WS
Sol_WS_V1_18LB   = Sol_V1_18LB[V1_18_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_18_Y6maskLB   = np.isfinite(Hg0_V1_18LB) # Scan for NaN values
BrO_Hg0_V1_18LB  = BrO_V1_18LB[V1_18_Y6maskLB] # Remove NaN values from BrO
Hg0_V1_18LB      = Hg0_V1_18LB[V1_18_Y6maskLB] # Remove NaN values from SI
Sol_Hg0_V1_18LB  = Sol_V1_18LB[V1_18_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_18_Y7maskLB   = np.isfinite(SI_V1_18LB) # Scan for NaN values
BrO_SI_V1_18LB   = BrO_V1_18LB[V1_18_Y7maskLB] # Remove NaN values from BrO
SI_SI_V1_18LB    = SI_V1_18LB[V1_18_Y7maskLB] # Remove NaN values from SI
Sol_SI_V1_18LB   = Sol_V1_18LB[V1_18_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_18_Y8maskLB   = np.isfinite(RH_V1_18LB) # Scan for NaN values
BrO_RH_V1_18LB   = BrO_V1_18LB[V1_18_Y8maskLB] # Remove NaN values from BrO
RH_V1_18LB       = RH_V1_18LB[V1_18_Y8maskLB] # Remove NaN values from WS
Sol_RH_V1_18LB   = Sol_V1_18LB[V1_18_Y8maskLB] # Remove NaN values from Sol

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (BrO)
V2_18_Y1maskLB   = np.isfinite(BrO_V2_18LB) # Scan for NaN values
BrO_V2_18LB      = BrO_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from BrO
O3_V2_18LB       = O3_V2_18L[V2_18_Y1maskLB] # Remove NaN values from Sol
Sol_V2_18LB      = Sol_V2_18L[V2_18_Y1maskLB] # Remove NaN values from Sol
Temp_V2_18LB     = Temp_V2_18L[V2_18_Y1maskLB] # Remove NaN values from Sol
WD_vect_V2_18LB  = WD_vect_V2_18L[V2_18_Y1maskLB] # Remove NaN values from Sol
WS_V2_18LB       = WS_V2_18L[V2_18_Y1maskLB] # Remove NaN values from Sol
Hg0_V2_18LB      = Hg0_V2_18L[V2_18_Y1maskLB] # Remove NaN values from Sol
SI_V2_18LB       = SI_V2_18L[V2_18_Y1maskLB] # Remove NaN values from Sol
RH_V2_18LB       = RH_V2_18L[V2_18_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_18_Y1maskLB   = np.isfinite(Sol_V2_18LB) # Scan for NaN values
BrO_V2_18LB      = BrO_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from BrO
O3_V2_18LB       = O3_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from Sol
Sol_V2_18LB      = Sol_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from Sol
Temp_V2_18LB     = Temp_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from Sol
WD_vect_V2_18LB  = WD_vect_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from Sol
WS_V2_18LB       = WS_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from Sol
Hg0_V2_18LB      = Hg0_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from Sol
SI_V2_18LB       = SI_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from Sol
RH_V2_18LB       = RH_V2_18LB[V2_18_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
V2_18_Y2maskLB   = np.isfinite(O3_V2_18LB) # Scan for NaN values
BrO_O3_V2_18LB   = BrO_V2_18LB[V2_18_Y2maskLB] # Remove NaN values from BrO
O3_V2_18LB       = O3_V2_18LB[V2_18_Y2maskLB] # Remove NaN values from Temp
Sol_O3_V2_18LB   = Sol_V2_18LB[V2_18_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_18_Y3maskLB   = np.isfinite(Temp_V2_18LB) # Scan for NaN values
BrO_Temp_V2_18LB = BrO_V2_18LB[V2_18_Y3maskLB] # Remove NaN values from BrO
Temp_V2_18LB     = Temp_V2_18LB[V2_18_Y3maskLB] # Remove NaN values from Temp
Sol_Temp_V2_18LB = Sol_V2_18LB[V2_18_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_18_Y4maskLB   = np.isfinite(WD_vect_V2_18LB) # Scan for NaN values
BrO_WD_V2_18LB   = BrO_V2_18LB[V2_18_Y4maskLB] # Remove NaN values from BrO
WD_vect_V2_18LB  = WD_vect_V2_18LB[V2_18_Y4maskLB] # Remove NaN values from WD_vect
Sol_WD_V2_18LB   = Sol_V2_18LB[V2_18_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_18_Y5maskLB   = np.isfinite(WS_V2_18LB) # Scan for NaN values
BrO_WS_V2_18LB   = BrO_V2_18LB[V2_18_Y5maskLB] # Remove NaN values from BrO
WS_V2_18LB       = WS_V2_18LB[V2_18_Y5maskLB] # Remove NaN values from WS
Sol_WS_V2_18LB   = Sol_V2_18LB[V2_18_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_18_Y6maskLB   = np.isfinite(Hg0_V2_18LB) # Scan for NaN values
BrO_Hg0_V2_18LB  = BrO_V2_18LB[V2_18_Y6maskLB] # Remove NaN values from BrO
Hg0_V2_18LB      = Hg0_V2_18LB[V2_18_Y6maskLB] # Remove NaN values from SI
Sol_Hg0_V2_18LB  = Sol_V2_18LB[V2_18_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_18_Y7maskLB   = np.isfinite(SI_V2_18LB) # Scan for NaN values
BrO_SI_V2_18LB   = BrO_V2_18LB[V2_18_Y7maskLB] # Remove NaN values from BrO
SI_SI_V2_18LB    = SI_V2_18LB[V2_18_Y7maskLB] # Remove NaN values from SI
Sol_SI_V2_18LB   = Sol_V2_18LB[V2_18_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_18_Y8maskLB   = np.isfinite(RH_V2_18LB) # Scan for NaN values
BrO_RH_V2_18LB   = BrO_V2_18LB[V2_18_Y8maskLB] # Remove NaN values from BrO
RH_V2_18LB       = RH_V2_18LB[V2_18_Y8maskLB] # Remove NaN values from WS
Sol_RH_V2_18LB   = Sol_V2_18LB[V2_18_Y8maskLB] # Remove NaN values from Sol

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (BrO) 
V3_18_Y1maskLB   = np.isfinite(BrO_V3_18LB) # Scan for NaN values
BrO_V3_18LB      = BrO_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from BrO
O3_V3_18LB       = O3_V3_18L[V3_18_Y1maskLB] # Remove NaN values from Sol
Sol_V3_18LB      = Sol_V3_18L[V3_18_Y1maskLB] # Remove NaN values from Sol
Temp_V3_18LB     = Temp_V3_18L[V3_18_Y1maskLB] # Remove NaN values from Sol
WD_vect_V3_18LB  = WD_vect_V3_18L[V3_18_Y1maskLB] # Remove NaN values from Sol
WS_V3_18LB       = WS_V3_18L[V3_18_Y1maskLB] # Remove NaN values from Sol
Hg0_V3_18LB      = Hg0_V3_18L[V3_18_Y1maskLB] # Remove NaN values from Sol
SI_V3_18LB       = SI_V3_18L[V3_18_Y1maskLB] # Remove NaN values from Sol
RH_V3_18LB       = RH_V3_18L[V3_18_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_18_Y1maskLB   = np.isfinite(Sol_V3_18LB) # Scan for NaN values
BrO_V3_18LB      = BrO_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from BrO
O3_V3_18LB       = O3_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from Sol
Sol_V3_18LB      = Sol_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from Sol
Temp_V3_18LB     = Temp_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from Sol
WD_vect_V3_18LB  = WD_vect_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from Sol
WS_V3_18LB       = WS_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from Sol
Hg0_V3_18LB      = Hg0_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from Sol
SI_V3_18LB       = SI_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from Sol
RH_V3_18LB       = RH_V3_18LB[V3_18_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
V3_18_Y2maskLB   = np.isfinite(O3_V3_18LB) # Scan for NaN values
BrO_O3_V3_18LB   = BrO_V3_18LB[V3_18_Y2maskLB] # Remove NaN values from BrO
O3_V3_18LB       = O3_V3_18LB[V3_18_Y2maskLB] # Remove NaN values from Temp
Sol_O3_V3_18LB   = Sol_V3_18LB[V3_18_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_18_Y3maskLB   = np.isfinite(Temp_V3_18LB) # Scan for NaN values
BrO_Temp_V3_18LB = BrO_V3_18LB[V3_18_Y3maskLB] # Remove NaN values from BrO
Temp_V3_18LB     = Temp_V3_18LB[V3_18_Y3maskLB] # Remove NaN values from Temp
Sol_Temp_V3_18LB = Sol_V3_18LB[V3_18_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_18_Y4maskLB   = np.isfinite(WD_vect_V3_18LB) # Scan for NaN values
BrO_WD_V3_18LB   = BrO_V3_18LB[V3_18_Y4maskLB] # Remove NaN values from BrO
WD_vect_V3_18LB  = WD_vect_V3_18LB[V3_18_Y4maskLB] # Remove NaN values from WD_vect
Sol_WD_V3_18LB   = Sol_V3_18LB[V3_18_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_18_Y5maskLB   = np.isfinite(WS_V3_18LB) # Scan for NaN values
BrO_WS_V3_18LB   = BrO_V3_18LB[V3_18_Y5maskLB] # Remove NaN values from BrO
WS_V3_18LB       = WS_V3_18LB[V3_18_Y5maskLB] # Remove NaN values from WS
Sol_WS_V3_18LB   = Sol_V3_18LB[V3_18_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_18_Y6maskLB   = np.isfinite(Hg0_V3_18LB) # Scan for NaN values
BrO_Hg0_V3_18LB  = BrO_V3_18LB[V3_18_Y6maskLB] # Remove NaN values from BrO
Hg0_V3_18LB      = Hg0_V3_18LB[V3_18_Y6maskLB] # Remove NaN values from SI
Sol_Hg0_V3_18LB  = Sol_V3_18LB[V3_18_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_18_Y7maskLB   = np.isfinite(SI_V3_18LB) # Scan for NaN values
BrO_SI_V3_18LB   = BrO_V3_18LB[V3_18_Y7maskLB] # Remove NaN values from BrO
SI_SI_V3_18LB    = SI_V3_18LB[V3_18_Y7maskLB] # Remove NaN values from SI
Sol_SI_V3_18LB   = Sol_V3_18LB[V3_18_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_18_Y8maskLB   = np.isfinite(RH_V3_18LB) # Scan for NaN values
BrO_RH_V3_18LB   = BrO_V3_18LB[V3_18_Y8maskLB] # Remove NaN values from BrO
RH_V3_18LB       = RH_V3_18LB[V3_18_Y8maskLB] # Remove NaN values from WS
Sol_RH_V3_18LB   = Sol_V3_18LB[V3_18_Y8maskLB] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskLB  = np.isfinite(BrOLB) # Scan for NaN values
BrOLB         = BrOLB[ALL_Y1maskLB] # Remove NaN values from BrO
O3LB          = O3L[ALL_Y1maskLB] # Remove NaN values from Sol
SolLB         = SolL[ALL_Y1maskLB] # Remove NaN values from Sol
TempLB        = TempL[ALL_Y1maskLB] # Remove NaN values from Sol
WD_vectLB     = WD_vectL[ALL_Y1maskLB] # Remove NaN values from Sol
WSLB          = WSL[ALL_Y1maskLB] # Remove NaN values from Sol
Hg0LB         = Hg0L[ALL_Y1maskLB] # Remove NaN values from Sol
SILB          = SIL[ALL_Y1maskLB] # Remove NaN values from Sol
RHLB          = RHL[ALL_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
ALL_Y1maskLB  = np.isfinite(SolLB) # Scan for NaN values
BrOLB         = BrOLB[ALL_Y1maskLB] # Remove NaN values from BrO
O3LB          = O3LB[ALL_Y1maskLB] # Remove NaN values from Sol
SolLB         = SolLB[ALL_Y1maskLB] # Remove NaN values from Sol
TempLB        = TempLB[ALL_Y1maskLB] # Remove NaN values from Sol
WD_vectLB     = WD_vectLB[ALL_Y1maskLB] # Remove NaN values from Sol
WSLB          = WSLB[ALL_Y1maskLB] # Remove NaN values from Sol
Hg0LB         = Hg0LB[ALL_Y1maskLB] # Remove NaN values from Sol
SILB          = SILB[ALL_Y1maskLB] # Remove NaN values from Sol
RHLB          = RHLB[ALL_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
ALL_Y2maskLB  = np.isfinite(O3LB) # Scan for NaN values
BrO_O3LB      = BrOLB[ALL_Y2maskLB] # Remove NaN values from BrO
O3LB          = O3LB[ALL_Y2maskLB] # Remove NaN values from Temp
Sol_O3LB      = SolLB[ALL_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskLB  = np.isfinite(TempLB) # Scan for NaN values
BrO_TempLB    = BrOLB[ALL_Y3maskLB] # Remove NaN values from BrO
TempLB        = TempLB[ALL_Y3maskLB] # Remove NaN values from Temp
Sol_TempLB    = SolLB[ALL_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskLB  = np.isfinite(WD_vectLB) # Scan for NaN values
BrO_WDLB      = BrOLB[ALL_Y4maskLB] # Remove NaN values from BrO
WD_vectLB     = WD_vectLB[ALL_Y4maskLB] # Remove NaN values from WD_vect
Sol_WDLB      = SolLB[ALL_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskLB  = np.isfinite(WSLB) # Scan for NaN values
BrO_WSLB      = BrOLB[ALL_Y5maskLB] # Remove NaN values from BrO
WSLB          = WSLB[ALL_Y5maskLB] # Remove NaN values from WS
Sol_WSLB      = SolLB[ALL_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskLB  = np.isfinite(Hg0LB) # Scan for NaN values
BrO_Hg0LB     = BrOLB[ALL_Y6maskLB] # Remove NaN values from BrO
Hg0LB         = Hg0LB[ALL_Y6maskLB] # Remove NaN values from SI
Sol_Hg0LB     = SolLB[ALL_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskLB  = np.isfinite(SILB) # Scan for NaN values
BrO_SILB      = BrOLB[ALL_Y7maskLB] # Remove NaN values from BrO
SI_SILB       = SILB[ALL_Y7maskLB] # Remove NaN values from SI
Sol_SILB      = SolLB[ALL_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskLB  = np.isfinite(RHLB) # Scan for NaN values
BrO_RHLB      = BrOLB[ALL_Y8maskLB] # Remove NaN values from BrO
RHLB          = RHLB[ALL_Y8maskLB] # Remove NaN values from RH
Sol_RHLB      = SolLB[ALL_Y8maskLB] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V1_17_Y1maskHB   = np.isfinite(BrO_V1_17HB) # Scan for NaN values
BrO_V1_17HB      = BrO_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from BrO
O3_V1_17HB       = O3_V1_17H[V1_17_Y1maskHB] # Remove NaN values from Sol
Sol_V1_17HB      = Sol_V1_17H[V1_17_Y1maskHB] # Remove NaN values from Sol
Temp_V1_17HB     = Temp_V1_17H[V1_17_Y1maskHB] # Remove NaN values from Sol
WD_vect_V1_17HB  = WD_vect_V1_17H[V1_17_Y1maskHB] # Remove NaN values from Sol
WS_V1_17HB       = WS_V1_17H[V1_17_Y1maskHB] # Remove NaN values from Sol
Hg0_V1_17HB      = Hg0_V1_17H[V1_17_Y1maskHB] # Remove NaN values from Sol
SI_V1_17HB       = SI_V1_17H[V1_17_Y1maskHB] # Remove NaN values from Sol
RH_V1_17HB       = RH_V1_17H[V1_17_Y1maskHB] # Remove NaN values from RH

# Pass 1 (Sol) 
V1_17_Y1maskHB   = np.isfinite(Sol_V1_17HB) # Scan for NaN values
BrO_V1_17HB      = BrO_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from BrO
O3_V1_17HB       = O3_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from Sol
Sol_V1_17HB      = Sol_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from Sol
Temp_V1_17HB     = Temp_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from Sol
WD_vect_V1_17HB  = WD_vect_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from Sol
WS_V1_17HB       = WS_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from Sol
Hg0_V1_17HB      = Hg0_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from Sol
SI_V1_17HB       = SI_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from Sol
RH_V1_17HB       = RH_V1_17HB[V1_17_Y1maskHB] # Remove NaN values from RH

# Pass 2 (O3) 
V1_17_Y2maskHB   = np.isfinite(O3_V1_17HB) # Scan for NaN values
BrO_O3_V1_17HB   = BrO_V1_17HB[V1_17_Y2maskHB] # Remove NaN values from BrO
O3_V1_17HB       = O3_V1_17HB[V1_17_Y2maskHB] # Remove NaN values from Temp
Sol_O3_V1_17HB    = Sol_V1_17HB[V1_17_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_17_Y3maskHB   = np.isfinite(Temp_V1_17HB) # Scan for NaN values
BrO_Temp_V1_17HB = BrO_V1_17HB[V1_17_Y3maskHB] # Remove NaN values from BrO
Temp_V1_17HB     = Temp_V1_17HB[V1_17_Y3maskHB] # Remove NaN values from Temp
Sol_Temp_V1_17HB = Sol_V1_17HB[V1_17_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_17_Y4maskHB   = np.isfinite(WD_vect_V1_17HB) # Scan for NaN values
BrO_WD_V1_17HB   = BrO_V1_17HB[V1_17_Y4maskHB] # Remove NaN values from BrO
WD_vect_V1_17HB  = WD_vect_V1_17HB[V1_17_Y4maskHB] # Remove NaN values from WD_vect
Sol_WD_V1_17HB   = Sol_V1_17HB[V1_17_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_17_Y5maskHB   = np.isfinite(WS_V1_17HB) # Scan for NaN values
BrO_WS_V1_17HB   = BrO_V1_17HB[V1_17_Y5maskHB] # Remove NaN values from BrO
WS_V1_17HB       = WS_V1_17HB[V1_17_Y5maskHB] # Remove NaN values from WS
Sol_WS_V1_17HB   = Sol_V1_17HB[V1_17_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_17_Y6maskHB   = np.isfinite(Hg0_V1_17HB) # Scan for NaN values
BrO_Hg0_V1_17HB  = BrO_V1_17HB[V1_17_Y6maskHB] # Remove NaN values from BrO
Hg0_V1_17HB      = Hg0_V1_17HB[V1_17_Y6maskHB] # Remove NaN values from SI
Sol_Hg0_V1_17HB  = Sol_V1_17HB[V1_17_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_17_Y7maskHB   = np.isfinite(SI_V1_17HB) # Scan for NaN values
BrO_SI_V1_17HB   = BrO_V1_17HB[V1_17_Y7maskHB] # Remove NaN values from BrO
SI_SI_V1_17HB    = SI_V1_17HB[V1_17_Y7maskHB] # Remove NaN values from SI
Sol_SI_V1_17HB   = Sol_V1_17HB[V1_17_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_17_Y8maskHB   = np.isfinite(RH_V1_17HB) # Scan for NaN values
BrO_RH_V1_17HB   = BrO_V1_17HB[V1_17_Y8maskHB] # Remove NaN values from BrO
RH_V1_17HB       = RH_V1_17HB[V1_17_Y8maskHB] # Remove NaN values from WS
Sol_RH_V1_17HB   = Sol_V1_17HB[V1_17_Y8maskHB] # Remove NaN values from Sol

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V2_17_Y1maskHB   = np.isfinite(BrO_V2_17HB) # Scan for NaN values
BrO_V2_17HB      = BrO_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from BrO
O3_V2_17HB       = O3_V2_17H[V2_17_Y1maskHB] # Remove NaN values from Sol
Sol_V2_17HB      = Sol_V2_17H[V2_17_Y1maskHB] # Remove NaN values from Sol
Temp_V2_17HB     = Temp_V2_17H[V2_17_Y1maskHB] # Remove NaN values from Sol
WD_vect_V2_17HB  = WD_vect_V2_17H[V2_17_Y1maskHB] # Remove NaN values from Sol
WS_V2_17HB       = WS_V2_17H[V2_17_Y1maskHB] # Remove NaN values from Sol
Hg0_V2_17HB      = Hg0_V2_17H[V2_17_Y1maskHB] # Remove NaN values from Sol
SI_V2_17HB       = SI_V2_17H[V2_17_Y1maskHB] # Remove NaN values from Sol
RH_V2_17HB       = RH_V2_17H[V2_17_Y1maskHB] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_17_Y1maskHB   = np.isfinite(Sol_V2_17HB) # Scan for NaN values
BrO_V2_17HB      = BrO_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from BrO
O3_V2_17HB       = O3_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from Sol
Sol_V2_17HB      = Sol_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from Sol
Temp_V2_17HB     = Temp_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from Sol
WD_vect_V2_17HB  = WD_vect_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from Sol
WS_V2_17HB       = WS_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from Sol
Hg0_V2_17HB      = Hg0_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from Sol
SI_V2_17HB       = SI_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from Sol
RH_V2_17HB       = RH_V2_17HB[V2_17_Y1maskHB] # Remove NaN values from RH

# Pass 2 (O3) 
V2_17_Y2maskHB   = np.isfinite(O3_V2_17HB) # Scan for NaN values
BrO_O3_V2_17HB   = BrO_V2_17HB[V2_17_Y2maskHB] # Remove NaN values from BrO
O3_V2_17HB       = O3_V2_17HB[V2_17_Y2maskHB] # Remove NaN values from Temp
Sol_O3_V2_17HB   = Sol_V2_17HB[V2_17_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_17_Y3maskHB   = np.isfinite(Temp_V2_17HB) # Scan for NaN values
BrO_Temp_V2_17HB = BrO_V2_17HB[V2_17_Y3maskHB] # Remove NaN values from BrO
Temp_V2_17HB     = Temp_V2_17HB[V2_17_Y3maskHB] # Remove NaN values from Temp
Sol_Temp_V2_17HB = Sol_V2_17HB[V2_17_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_17_Y4maskHB   = np.isfinite(WD_vect_V2_17HB) # Scan for NaN values
BrO_WD_V2_17HB   = BrO_V2_17HB[V2_17_Y4maskHB] # Remove NaN values from BrO
WD_vect_V2_17HB  = WD_vect_V2_17HB[V2_17_Y4maskHB] # Remove NaN values from WD_vect
Sol_WD_V2_17HB   = Sol_V2_17HB[V2_17_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_17_Y5maskHB   = np.isfinite(WS_V2_17HB) # Scan for NaN values
BrO_WS_V2_17HB   = BrO_V2_17HB[V2_17_Y5maskHB] # Remove NaN values from BrO
WS_V2_17HB       = WS_V2_17HB[V2_17_Y5maskHB] # Remove NaN values from WS
Sol_WS_V2_17HB   = Sol_V2_17HB[V2_17_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_17_Y6maskHB   = np.isfinite(Hg0_V2_17HB) # Scan for NaN values
BrO_Hg0_V2_17HB  = BrO_V2_17HB[V2_17_Y6maskHB] # Remove NaN values from BrO
Hg0_V2_17HB      = Hg0_V2_17HB[V2_17_Y6maskHB] # Remove NaN values from SI
Sol_Hg0_V2_17HB  = Sol_V2_17HB[V2_17_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_17_Y7maskHB   = np.isfinite(SI_V2_17HB) # Scan for NaN values
BrO_SI_V2_17HB   = BrO_V2_17HB[V2_17_Y7maskHB] # Remove NaN values from BrO
SI_SI_V2_17HB    = SI_V2_17HB[V2_17_Y7maskHB] # Remove NaN values from SI
Sol_SI_V2_17HB   = Sol_V2_17HB[V2_17_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_17_Y8maskHB   = np.isfinite(RH_V2_17HB) # Scan for NaN values
BrO_RH_V2_17HB   = BrO_V2_17HB[V2_17_Y8maskHB] # Remove NaN values from BrO
RH_V2_17HB       = RH_V2_17HB[V2_17_Y8maskHB] # Remove NaN values from WS
Sol_RH_V2_17HB   = Sol_V2_17HB[V2_17_Y8maskHB] # Remove NaN values from Sol

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (BrO) 
V3_17_Y1maskHB   = np.isfinite(BrO_V3_17HB) # Scan for NaN values
BrO_V3_17HB      = BrO_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from BrO
O3_V3_17HB       = O3_V3_17H[V3_17_Y1maskHB] # Remove NaN values from Sol
Sol_V3_17HB      = Sol_V3_17H[V3_17_Y1maskHB] # Remove NaN values from Sol
Temp_V3_17HB     = Temp_V3_17H[V3_17_Y1maskHB] # Remove NaN values from Sol
WD_vect_V3_17HB  = WD_vect_V3_17H[V3_17_Y1maskHB] # Remove NaN values from Sol
WS_V3_17HB       = WS_V3_17H[V3_17_Y1maskHB] # Remove NaN values from Sol
Hg0_V3_17HB      = Hg0_V3_17H[V3_17_Y1maskHB] # Remove NaN values from Sol
SI_V3_17HB       = SI_V3_17H[V3_17_Y1maskHB] # Remove NaN values from Sol
RH_V3_17HB       = RH_V3_17H[V3_17_Y1maskHB] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_17_Y1maskHB   = np.isfinite(Sol_V3_17HB) # Scan for NaN values
BrO_V3_17HB      = BrO_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from BrO
O3_V3_17HB       = O3_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from Sol
Sol_V3_17HB      = Sol_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from Sol
Temp_V3_17HB     = Temp_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from Sol
WD_vect_V3_17HB  = WD_vect_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from Sol
WS_V3_17HB       = WS_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from Sol
Hg0_V3_17HB      = Hg0_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from Sol
SI_V3_17HB       = SI_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from Sol
RH_V3_17HB       = RH_V3_17HB[V3_17_Y1maskHB] # Remove NaN values from RH

# Pass 2 (O3) 
V3_17_Y2maskHB   = np.isfinite(O3_V3_17HB) # Scan for NaN values
BrO_O3_V3_17HB   = BrO_V3_17HB[V3_17_Y2maskHB] # Remove NaN values from BrO
O3_V3_17HB       = O3_V3_17HB[V3_17_Y2maskHB] # Remove NaN values from Temp
Sol_O3_V3_17HB   = Sol_V3_17HB[V3_17_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_17_Y3maskHB   = np.isfinite(Temp_V3_17HB) # Scan for NaN values
BrO_Temp_V3_17HB = BrO_V3_17HB[V3_17_Y3maskHB] # Remove NaN values from BrO
Temp_V3_17HB     = Temp_V3_17HB[V3_17_Y3maskHB] # Remove NaN values from Temp
Sol_Temp_V3_17HB = Sol_V3_17HB[V3_17_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_17_Y4maskHB   = np.isfinite(WD_vect_V3_17HB) # Scan for NaN values
BrO_WD_V3_17HB   = BrO_V3_17HB[V3_17_Y4maskHB] # Remove NaN values from BrO
WD_vect_V3_17HB  = WD_vect_V3_17HB[V3_17_Y4maskHB] # Remove NaN values from WD_vect
Sol_WD_V3_17HB   = Sol_V3_17HB[V3_17_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_17_Y5maskHB   = np.isfinite(WS_V3_17HB) # Scan for NaN values
BrO_WS_V3_17HB   = BrO_V3_17HB[V3_17_Y5maskHB] # Remove NaN values from BrO
WS_V3_17HB       = WS_V3_17HB[V3_17_Y5maskHB] # Remove NaN values from WS
Sol_WS_V3_17HB   = Sol_V3_17HB[V3_17_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_17_Y6maskHB   = np.isfinite(Hg0_V3_17HB) # Scan for NaN values
BrO_Hg0_V3_17HB  = BrO_V3_17HB[V3_17_Y6maskHB] # Remove NaN values from BrO
Hg0_V3_17HB      = Hg0_V3_17HB[V3_17_Y6maskHB] # Remove NaN values from SI
Sol_Hg0_V3_17HB  = Sol_V3_17HB[V3_17_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_17_Y7maskHB   = np.isfinite(SI_V3_17HB) # Scan for NaN values
BrO_SI_V3_17HB   = BrO_V3_17HB[V3_17_Y7maskHB] # Remove NaN values from BrO
SI_SI_V3_17HB    = SI_V3_17HB[V3_17_Y7maskHB] # Remove NaN values from SI
Sol_SI_V3_17HB   = Sol_V3_17HB[V3_17_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_17_Y8maskHB   = np.isfinite(RH_V3_17HB) # Scan for NaN values
BrO_RH_V3_17HB   = BrO_V3_17HB[V3_17_Y8maskHB] # Remove NaN values from BrO
RH_V3_17HB       = RH_V3_17HB[V3_17_Y8maskHB] # Remove NaN values from WS
Sol_RH_V3_17HB   = Sol_V3_17HB[V3_17_Y8maskHB] # Remove NaN values from Sol

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (BrO)
V1_18_Y1maskHB   = np.isfinite(BrO_V1_18HB) # Scan for NaN values
BrO_V1_18HB      = BrO_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from BrO
O3_V1_18HB       = O3_V1_18H[V1_18_Y1maskHB] # Remove NaN values from Sol
Sol_V1_18HB      = Sol_V1_18H[V1_18_Y1maskHB] # Remove NaN values from Sol
Temp_V1_18HB     = Temp_V1_18H[V1_18_Y1maskHB] # Remove NaN values from Sol
WD_vect_V1_18HB  = WD_vect_V1_18H[V1_18_Y1maskHB] # Remove NaN values from Sol
WS_V1_18HB       = WS_V1_18H[V1_18_Y1maskHB] # Remove NaN values from Sol
Hg0_V1_18HB      = Hg0_V1_18H[V1_18_Y1maskHB] # Remove NaN values from Sol
SI_V1_18HB       = SI_V1_18H[V1_18_Y1maskHB] # Remove NaN values from Sol
RH_V1_18HB       = RH_V1_18H[V1_18_Y1maskHB] # Remove NaN values from RH

# Pass 1 (Sol)
V1_18_Y1maskHB   = np.isfinite(Sol_V1_18HB) # Scan for NaN values
BrO_V1_18HB      = BrO_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from BrO
O3_V1_18HB       = O3_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from Sol
Sol_V1_18HB      = Sol_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from Sol
Temp_V1_18HB     = Temp_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from Sol
WD_vect_V1_18HB  = WD_vect_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from Sol
WS_V1_18HB       = WS_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from Sol
Hg0_V1_18HB      = Hg0_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from Sol
SI_V1_18HB       = SI_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from Sol
RH_V1_18HB       = RH_V1_18HB[V1_18_Y1maskHB] # Remove NaN values from RH

# Pass 2 (O3) 
V1_18_Y2maskHB   = np.isfinite(O3_V1_18HB) # Scan for NaN values
BrO_O3_V1_18HB   = BrO_V1_18HB[V1_18_Y2maskHB] # Remove NaN values from BrO
O3_V1_18HB       = O3_V1_18HB[V1_18_Y2maskHB] # Remove NaN values from Temp
Sol_O3_V1_18HB   = Sol_V1_18HB[V1_18_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_18_Y3maskHB   = np.isfinite(Temp_V1_18HB) # Scan for NaN values
BrO_Temp_V1_18HB = BrO_V1_18HB[V1_18_Y3maskHB] # Remove NaN values from BrO
Temp_V1_18HB     = Temp_V1_18HB[V1_18_Y3maskHB] # Remove NaN values from Temp
Sol_Temp_V1_18HB = Sol_V1_18HB[V1_18_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_18_Y4maskHB   = np.isfinite(WD_vect_V1_18HB) # Scan for NaN values
BrO_WD_V1_18HB   = BrO_V1_18HB[V1_18_Y4maskHB] # Remove NaN values from BrO
WD_vect_V1_18HB  = WD_vect_V1_18HB[V1_18_Y4maskHB] # Remove NaN values from WD_vect
Sol_WD_V1_18HB   = Sol_V1_18HB[V1_18_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_18_Y5maskHB   = np.isfinite(WS_V1_18HB) # Scan for NaN values
BrO_WS_V1_18HB   = BrO_V1_18HB[V1_18_Y5maskHB] # Remove NaN values from BrO
WS_V1_18HB       = WS_V1_18HB[V1_18_Y5maskHB] # Remove NaN values from WS
Sol_WS_V1_18HB   = Sol_V1_18HB[V1_18_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_18_Y6maskHB   = np.isfinite(Hg0_V1_18HB) # Scan for NaN values
BrO_Hg0_V1_18HB  = BrO_V1_18HB[V1_18_Y6maskHB] # Remove NaN values from BrO
Hg0_V1_18HB      = Hg0_V1_18HB[V1_18_Y6maskHB] # Remove NaN values from SI
Sol_Hg0_V1_18HB  = Sol_V1_18HB[V1_18_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_18_Y7maskHB   = np.isfinite(SI_V1_18HB) # Scan for NaN values
BrO_SI_V1_18HB   = BrO_V1_18HB[V1_18_Y7maskHB] # Remove NaN values from BrO
SI_SI_V1_18HB    = SI_V1_18HB[V1_18_Y7maskHB] # Remove NaN values from SI
Sol_SI_V1_18HB   = Sol_V1_18HB[V1_18_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_18_Y8maskHB   = np.isfinite(RH_V1_18HB) # Scan for NaN values
BrO_RH_V1_18HB   = BrO_V1_18HB[V1_18_Y8maskHB] # Remove NaN values from BrO
RH_V1_18HB       = RH_V1_18HB[V1_18_Y8maskHB] # Remove NaN values from WS
Sol_RH_V1_18HB   = Sol_V1_18HB[V1_18_Y8maskHB] # Remove NaN values from Sol

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (BrO) 
V2_18_Y1maskHB   = np.isfinite(BrO_V2_18HB) # Scan for NaN values
BrO_V2_18HB      = BrO_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from BrO
O3_V2_18HB       = O3_V2_18H[V2_18_Y1maskHB] # Remove NaN values from Sol
Sol_V2_18HB      = Sol_V2_18H[V2_18_Y1maskHB] # Remove NaN values from Sol
Temp_V2_18HB     = Temp_V2_18H[V2_18_Y1maskHB] # Remove NaN values from Sol
WD_vect_V2_18HB  = WD_vect_V2_18H[V2_18_Y1maskHB] # Remove NaN values from Sol
WS_V2_18HB       = WS_V2_18H[V2_18_Y1maskHB] # Remove NaN values from Sol
Hg0_V2_18HB      = Hg0_V2_18H[V2_18_Y1maskHB] # Remove NaN values from Sol
SI_V2_18HB       = SI_V2_18H[V2_18_Y1maskHB] # Remove NaN values from Sol
RH_V2_18HB       = RH_V2_18H[V2_18_Y1maskHB] # Remove NaN values from RH

# Pass 1 (Sol) 
V2_18_Y1maskHB   = np.isfinite(Sol_V2_18HB) # Scan for NaN values
BrO_V2_18HB      = BrO_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from BrO
O3_V2_18HB       = O3_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from Sol
Sol_V2_18HB      = Sol_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from Sol
Temp_V2_18HB     = Temp_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from Sol
WD_vect_V2_18HB  = WD_vect_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from Sol
WS_V2_18HB       = WS_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from Sol
Hg0_V2_18HB      = Hg0_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from Sol
SI_V2_18HB       = SI_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from Sol
RH_V2_18HB       = RH_V2_18HB[V2_18_Y1maskHB] # Remove NaN values from RH

# Pass 2 (O3) 
V2_18_Y2maskHB   = np.isfinite(O3_V2_18HB) # Scan for NaN values
BrO_O3_V2_18HB   = BrO_V2_18HB[V2_18_Y2maskHB] # Remove NaN values from BrO
O3_V2_18HB       = O3_V2_18HB[V2_18_Y2maskHB] # Remove NaN values from Temp
Sol_O3_V2_18HB   = Sol_V2_18HB[V2_18_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_18_Y3maskHB   = np.isfinite(Temp_V2_18HB) # Scan for NaN values
BrO_Temp_V2_18HB = BrO_V2_18HB[V2_18_Y3maskHB] # Remove NaN values from BrO
Temp_V2_18HB     = Temp_V2_18HB[V2_18_Y3maskHB] # Remove NaN values from Temp
Sol_Temp_V2_18HB = Sol_V2_18HB[V2_18_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_18_Y4maskHB   = np.isfinite(WD_vect_V2_18HB) # Scan for NaN values
BrO_WD_V2_18HB   = BrO_V2_18HB[V2_18_Y4maskHB] # Remove NaN values from BrO
WD_vect_V2_18HB  = WD_vect_V2_18HB[V2_18_Y4maskHB] # Remove NaN values from WD_vect
Sol_WD_V2_18HB   = Sol_V2_18HB[V2_18_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_18_Y5maskHB   = np.isfinite(WS_V2_18HB) # Scan for NaN values
BrO_WS_V2_18HB   = BrO_V2_18HB[V2_18_Y5maskHB] # Remove NaN values from BrO
WS_V2_18HB       = WS_V2_18HB[V2_18_Y5maskHB] # Remove NaN values from WS
Sol_WS_V2_18HB   = Sol_V2_18HB[V2_18_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_18_Y6maskHB   = np.isfinite(Hg0_V2_18HB) # Scan for NaN values
BrO_Hg0_V2_18HB  = BrO_V2_18HB[V2_18_Y6maskHB] # Remove NaN values from BrO
Hg0_V2_18HB      = Hg0_V2_18HB[V2_18_Y6maskHB] # Remove NaN values from SI
Sol_Hg0_V2_18HB  = Sol_V2_18HB[V2_18_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_18_Y7maskHB   = np.isfinite(SI_V2_18HB) # Scan for NaN values
BrO_SI_V2_18HB   = BrO_V2_18HB[V2_18_Y7maskHB] # Remove NaN values from BrO
SI_SI_V2_18HB    = SI_V2_18HB[V2_18_Y7maskHB] # Remove NaN values from SI
Sol_SI_V2_18HB   = Sol_V2_18HB[V2_18_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_18_Y8maskHB   = np.isfinite(RH_V2_18HB) # Scan for NaN values
BrO_RH_V2_18HB   = BrO_V2_18HB[V2_18_Y8maskHB] # Remove NaN values from BrO
RH_V2_18HB       = RH_V2_18HB[V2_18_Y8maskHB] # Remove NaN values from WS
Sol_RH_V2_18HB   = Sol_V2_18HB[V2_18_Y8maskHB] # Remove NaN values from Sol

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (BrO) 
V3_18_Y1maskHB   = np.isfinite(BrO_V3_18HB) # Scan for NaN values
BrO_V3_18HB      = BrO_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from BrO
O3_V3_18HB       = O3_V3_18H[V3_18_Y1maskHB] # Remove NaN values from Sol
Sol_V3_18HB      = Sol_V3_18H[V3_18_Y1maskHB] # Remove NaN values from Sol
Temp_V3_18HB     = Temp_V3_18H[V3_18_Y1maskHB] # Remove NaN values from Sol
WD_vect_V3_18HB  = WD_vect_V3_18H[V3_18_Y1maskHB] # Remove NaN values from Sol
WS_V3_18HB       = WS_V3_18H[V3_18_Y1maskHB] # Remove NaN values from Sol
Hg0_V3_18HB      = Hg0_V3_18H[V3_18_Y1maskHB] # Remove NaN values from Sol
SI_V3_18HB       = SI_V3_18H[V3_18_Y1maskHB] # Remove NaN values from Sol
RH_V3_18HB       = RH_V3_18H[V3_18_Y1maskHB] # Remove NaN values from RH

# Pass 1 (Sol) 
V3_18_Y1maskHB   = np.isfinite(Sol_V3_18HB) # Scan for NaN values
BrO_V3_18HB      = BrO_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from BrO
O3_V3_18HB       = O3_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from Sol
Sol_V3_18HB      = Sol_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from Sol
Temp_V3_18HB     = Temp_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from Sol
WD_vect_V3_18HB  = WD_vect_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from Sol
WS_V3_18HB       = WS_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from Sol
Hg0_V3_18HB      = Hg0_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from Sol
SI_V3_18HB       = SI_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from Sol
RH_V3_18HB       = RH_V3_18HB[V3_18_Y1maskHB] # Remove NaN values from RH

# Pass 2 (O3) 
V3_18_Y2maskHB   = np.isfinite(O3_V3_18HB) # Scan for NaN values
BrO_O3_V3_18HB   = BrO_V3_18HB[V3_18_Y2maskHB] # Remove NaN values from BrO
O3_V3_18HB       = O3_V3_18HB[V3_18_Y2maskHB] # Remove NaN values from Temp
Sol_O3_V3_18HB   = Sol_V3_18HB[V3_18_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_18_Y3maskHB   = np.isfinite(Temp_V3_18HB) # Scan for NaN values
BrO_Temp_V3_18HB = BrO_V3_18HB[V3_18_Y3maskHB] # Remove NaN values from BrO
Temp_V3_18HB     = Temp_V3_18HB[V3_18_Y3maskHB] # Remove NaN values from Temp
Sol_Temp_V3_18HB = Sol_V3_18HB[V3_18_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_18_Y4maskHB   = np.isfinite(WD_vect_V3_18HB) # Scan for NaN values
BrO_WD_V3_18HB   = BrO_V3_18HB[V3_18_Y4maskHB] # Remove NaN values from BrO
WD_vect_V3_18HB  = WD_vect_V3_18HB[V3_18_Y4maskHB] # Remove NaN values from WD_vect
Sol_WD_V3_18HB   = Sol_V3_18HB[V3_18_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_18_Y5maskHB   = np.isfinite(WS_V3_18HB) # Scan for NaN values
BrO_WS_V3_18HB   = BrO_V3_18HB[V3_18_Y5maskHB] # Remove NaN values from BrO
WS_V3_18HB       = WS_V3_18HB[V3_18_Y5maskHB] # Remove NaN values from WS
Sol_WS_V3_18HB   = Sol_V3_18HB[V3_18_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_18_Y6maskHB   = np.isfinite(Hg0_V3_18HB) # Scan for NaN values
BrO_Hg0_V3_18HB  = BrO_V3_18HB[V3_18_Y6maskHB] # Remove NaN values from BrO
Hg0_V3_18HB      = Hg0_V3_18HB[V3_18_Y6maskHB] # Remove NaN values from SI
Sol_Hg0_V3_18HB  = Sol_V3_18HB[V3_18_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_18_Y7maskHB   = np.isfinite(SI_V3_18HB) # Scan for NaN values
BrO_SI_V3_18HB   = BrO_V3_18HB[V3_18_Y7maskHB] # Remove NaN values from BrO
SI_SI_V3_18HB    = SI_V3_18HB[V3_18_Y7maskHB] # Remove NaN values from SI
Sol_SI_V3_18HB   = Sol_V3_18HB[V3_18_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_18_Y8maskHB   = np.isfinite(RH_V3_18HB) # Scan for NaN values
BrO_RH_V3_18HB   = BrO_V3_18HB[V3_18_Y8maskHB] # Remove NaN values from BrO
RH_V3_18HB       = RH_V3_18HB[V3_18_Y8maskHB] # Remove NaN values from WS
Sol_RH_V3_18HB   = Sol_V3_18HB[V3_18_Y8maskHB] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskHB   = np.isfinite(BrOHB) # Scan for NaN values
BrOHB          = BrOHB[ALL_Y1maskHB] # Remove NaN values from BrO
O3HB           = O3H[ALL_Y1maskHB] # Remove NaN values from Sol
SolHB          = SolH[ALL_Y1maskHB] # Remove NaN values from Sol
TempHB         = TempH[ALL_Y1maskHB] # Remove NaN values from Sol
WD_vectHB      = WD_vectH[ALL_Y1maskHB] # Remove NaN values from Sol
WSHB           = WSH[ALL_Y1maskHB] # Remove NaN values from Sol
Hg0HB          = Hg0H[ALL_Y1maskHB] # Remove NaN values from Sol
SIHB           = SIH[ALL_Y1maskHB] # Remove NaN values from Sol
RHHB           = RHH[ALL_Y1maskHB] # Remove NaN values from WS

# Pass 1 (Sol) 
ALL_Y1maskHB   = np.isfinite(SolHB) # Scan for NaN values
BrOHB          = BrOHB[ALL_Y1maskHB] # Remove NaN values from BrO
O3HB           = O3HB[ALL_Y1maskHB] # Remove NaN values from Sol
SolHB          = SolHB[ALL_Y1maskHB] # Remove NaN values from Sol
TempHB         = TempHB[ALL_Y1maskHB] # Remove NaN values from Sol
WD_vectHB      = WD_vectHB[ALL_Y1maskHB] # Remove NaN values from Sol
WSHB           = WSHB[ALL_Y1maskHB] # Remove NaN values from Sol
Hg0HB          = Hg0HB[ALL_Y1maskHB] # Remove NaN values from Sol
SIHB           = SIHB[ALL_Y1maskHB] # Remove NaN values from Sol
RHHB           = RHHB[ALL_Y1maskHB] # Remove NaN values from WS

# Pass 2 (O3) 
ALL_Y2maskHB   = np.isfinite(O3HB) # Scan for NaN values
BrO_O3HB       = BrOHB[ALL_Y2maskHB] # Remove NaN values from BrO
O3HB           = O3HB[ALL_Y2maskHB] # Remove NaN values from Temp
Sol_O3HB       = SolHB[ALL_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskHB   = np.isfinite(TempHB) # Scan for NaN values
BrO_TempHB     = BrOHB[ALL_Y3maskHB] # Remove NaN values from BrO
TempHB         = TempHB[ALL_Y3maskHB] # Remove NaN values from Temp
Sol_TempHB     = SolHB[ALL_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskHB   = np.isfinite(WD_vectHB) # Scan for NaN values
BrO_WDHB       = BrOHB[ALL_Y4maskHB] # Remove NaN values from BrO
WD_vectHB      = WD_vectHB[ALL_Y4maskHB] # Remove NaN values from WD_vect
Sol_WDHB       = SolHB[ALL_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskHB   = np.isfinite(WSHB) # Scan for NaN values
BrO_WSHB       = BrOHB[ALL_Y5maskHB] # Remove NaN values from BrO
WSHB           = WSHB[ALL_Y5maskHB] # Remove NaN values from WS
Sol_WSHB       = SolHB[ALL_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskHB   = np.isfinite(Hg0HB) # Scan for NaN values
BrO_Hg0HB      = BrOHB[ALL_Y6maskHB] # Remove NaN values from BrO
Hg0HB          = Hg0HB[ALL_Y6maskHB] # Remove NaN values from SI
Sol_Hg0HB      = SolHB[ALL_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskHB   = np.isfinite(SIHB) # Scan for NaN values
BrO_SIHB       = BrOHB[ALL_Y7maskHB] # Remove NaN values from BrO
SI_SIHB        = SIHB[ALL_Y7maskHB] # Remove NaN values from SI
Sol_SIHB       = SolHB[ALL_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskHB  = np.isfinite(RHHB) # Scan for NaN values
BrO_RHHB      = BrOHB[ALL_Y8maskHB] # Remove NaN values from BrO
RHHB          = RHHB[ALL_Y8maskHB] # Remove NaN values from WS
Sol_RHHB      = SolHB[ALL_Y8maskHB] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)
#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
##--------------------------------
## V1_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_17LS, p_valueD1_V1_17LS = stats.pearsonr(O3_V1_17LS,BrO_O3_V1_17LS)
#slopeD1_V1_17LS, interceptD1_V1_17LS, rD1_V1_17LS, pD1_V1_17LS, std_errD1_V1_17LS = stats.linregress(O3_V1_17LS,BrO_O3_V1_17LS)
#
## 2) Between Temp and BrO
#r_rowD2_V1_17LS, p_valueD2_V1_17LS = stats.pearsonr(Temp_V1_17LS,BrO_V1_17LS)
#slopeD2_V1_17LS, interceptD2_V1_17LS, rD2_V1_17LS, pD2_V1_17LS, std_errD2_V1_17LS = stats.linregress(Temp_V1_17LS,BrO_V1_17LS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_17LS, p_valueD3_V1_17LS = stats.pearsonr(WD_vect_V1_17LS,BrO_WD_V1_17LS)
#slopeD3_V1_17LS, interceptD3_V1_17LS, rD3_V1_17LS, pD3_V1_17LS, std_errD3_V1_17LS = stats.linregress(WD_vect_V1_17LS,BrO_WD_V1_17LS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_17LS, p_valueD4_V1_17LS = stats.pearsonr(WS_V1_17LS,BrO_WS_V1_17LS)
#slopeD4_V1_17LS, interceptD4_V1_17LS, rD4_V1_17LS, pD4_V1_17LS, std_errD4_V1_17LS = stats.linregress(WS_V1_17LS,BrO_WS_V1_17LS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_17LS, p_valueD5_V1_17LS = stats.pearsonr(Sol_V1_17LS,BrO_V1_17LS)
#slopeD5_V1_17LS, interceptD5_V1_17LS, rD5_V1_17LS, pD5_V1_17LS, std_errD5_V1_17LS = stats.linregress(Sol_V1_17LS,BrO_V1_17LS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_17LS, p_valueD6_V1_17LS = stats.pearsonr(Hg0_V1_17LS,BrO_Hg0_V1_17LS)
#slopeD6_V1_17LS, interceptD6_V1_17LS, rD6_V1_17LS, pD6_V1_17LS, std_errD6_V1_17LS = stats.linregress(Hg0_V1_17LS,BrO_Hg0_V1_17LS)
#
## 7) Between SI and BrO
#r_rowD7_V1_17LS, p_valueD7_V1_17LS = stats.pearsonr(SI_SI_V1_17LS,BrO_SI_V1_17LS)
#slopeD7_V1_17LS, interceptD7_V1_17LS, rD7_V1_17LS, pD7_V1_17LS, std_errD7_V1_17LS = stats.linregress(SI_SI_V1_17LS,BrO_SI_V1_17LS)
#
## 8) Between RH and BrO
#r_rowD8_V1_17LS, p_valueD8_V1_17LS = stats.pearsonr(RH_V1_17LS,BrO_RH_V1_17LS)
#slopeD8_V1_17LS, interceptD8_V1_17LS, rD8_V1_17LS, pD8_V1_17LS, std_errD8_V1_17LS = stats.linregress(RH_V1_17LS,BrO_RH_V1_17LS)
#
##--------------------------------
## V2_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V2_17LS, p_valueD1_V2_17LS = stats.pearsonr(O3_V2_17LS,BrO_O3_V2_17LS)
#slopeD1_V2_17LS, interceptD1_V2_17LS, rD1_V2_17LS, pD1_V2_17LS, std_errD1_V2_17LS = stats.linregress(O3_V2_17LS,BrO_O3_V2_17LS)
#
## 2) Between Temp and BrO
#r_rowD2_V2_17LS, p_valueD2_V2_17LS = stats.pearsonr(Temp_V2_17LS,BrO_V2_17LS)
#slopeD2_V2_17LS, interceptD2_V2_17LS, rD2_V2_17LS, pD2_V2_17LS, std_errD2_V2_17LS = stats.linregress(Temp_V2_17LS,BrO_V2_17LS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V2_17LS, p_valueD3_V2_17LS = stats.pearsonr(WD_vect_V2_17LS,BrO_WD_V2_17LS)
#slopeD3_V2_17LS, interceptD3_V2_17LS, rD3_V2_17LS, pD3_V2_17LS, std_errD3_V2_17LS = stats.linregress(WD_vect_V2_17LS,BrO_WD_V2_17LS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V2_17LS, p_valueD4_V2_17LS = stats.pearsonr(WS_V2_17LS,BrO_WS_V2_17LS)
#slopeD4_V2_17LS, interceptD4_V2_17LS, rD4_V2_17LS, pD4_V2_17LS, std_errD4_V2_17LS = stats.linregress(WS_V2_17LS,BrO_WS_V2_17LS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V2_17LS, p_valueD5_V2_17LS = stats.pearsonr(Sol_V2_17LS,BrO_V2_17LS)
#slopeD5_V2_17LS, interceptD5_V2_17LS, rD5_V2_17LS, pD5_V2_17LS, std_errD5_V2_17LS = stats.linregress(Sol_V2_17LS,BrO_V2_17LS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V2_17LS, p_valueD6_V2_17LS = stats.pearsonr(Hg0_V2_17LS,BrO_Hg0_V2_17LS)
#slopeD6_V2_17LS, interceptD6_V2_17LS, rD6_V2_17LS, pD6_V2_17LS, std_errD6_V2_17LS = stats.linregress(Hg0_V2_17LS,BrO_Hg0_V2_17LS)
#
## 7) Between SI and BrO
#r_rowD7_V2_17LS, p_valueD7_V2_17LS = stats.pearsonr(SI_SI_V2_17LS,BrO_SI_V2_17LS)
#slopeD7_V2_17LS, interceptD7_V2_17LS, rD7_V2_17LS, pD7_V2_17LS, std_errD7_V2_17LS = stats.linregress(SI_SI_V2_17LS,BrO_SI_V2_17LS)
#
## 8) Between RH and BrO
#r_rowD8_V2_17LS, p_valueD8_V2_17LS = stats.pearsonr(RH_V2_17LS,BrO_RH_V2_17LS)
#slopeD8_V2_17LS, interceptD8_V2_17LS, rD8_V2_17LS, pD8_V2_17LS, std_errD8_V2_17LS = stats.linregress(RH_V2_17LS,BrO_RH_V2_17LS)
#
##--------------------------------
## V3_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_17LS, p_valueD1_V3_17LS = stats.pearsonr(O3_V3_17LS,BrO_O3_V3_17LS)
#slopeD1_V3_17LS, interceptD1_V3_17LS, rD1_V3_17LS, pD1_V3_17LS, std_errD1_V3_17LS = stats.linregress(O3_V3_17LS,BrO_O3_V3_17LS)
#
## 2) Between Temp and BrO
#r_rowD2_V3_17LS, p_valueD2_V3_17LS = stats.pearsonr(Temp_V3_17LS,BrO_V3_17LS)
#slopeD2_V3_17LS, interceptD2_V3_17LS, rD2_V3_17LS, pD2_V3_17LS, std_errD2_V3_17LS = stats.linregress(Temp_V3_17LS,BrO_V3_17LS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_17LS, p_valueD3_V3_17LS = stats.pearsonr(WD_vect_V3_17LS,BrO_WD_V3_17LS)
#slopeD3_V3_17LS, interceptD3_V3_17LS, rD3_V3_17LS, pD3_V3_17LS, std_errD3_V3_17LS = stats.linregress(WD_vect_V3_17LS,BrO_WD_V3_17LS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_17LS, p_valueD4_V3_17LS = stats.pearsonr(WS_V3_17LS,BrO_WS_V3_17LS)
#slopeD4_V3_17LS, interceptD4_V3_17LS, rD4_V3_17LS, pD4_V3_17LS, std_errD4_V3_17LS = stats.linregress(WS_V3_17LS,BrO_WS_V3_17LS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_17LS, p_valueD5_V3_17LS = stats.pearsonr(Sol_V3_17LS,BrO_V3_17LS)
#slopeD5_V3_17LS, interceptD5_V3_17LS, rD5_V3_17LS, pD5_V3_17LS, std_errD5_V3_17LS = stats.linregress(Sol_V3_17LS,BrO_V3_17LS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_17LS, p_valueD6_V3_17LS = stats.pearsonr(Hg0_V3_17LS,BrO_Hg0_V3_17LS)
#slopeD6_V3_17LS, interceptD6_V3_17LS, rD6_V3_17LS, pD6_V3_17LS, std_errD6_V3_17LS = stats.linregress(Hg0_V3_17LS,BrO_Hg0_V3_17LS)
#
## 7) Between SI and BrO
#r_rowD7_V3_17LS, p_valueD7_V3_17LS = stats.pearsonr(SI_SI_V3_17LS,BrO_SI_V3_17LS)
#slopeD7_V3_17LS, interceptD7_V3_17LS, rD7_V3_17LS, pD7_V3_17LS, std_errD7_V3_17LS = stats.linregress(SI_SI_V3_17LS,BrO_SI_V3_17LS)
#
## 8) Between RH and BrO
#r_rowD8_V3_17LS, p_valueD8_V3_17LS = stats.pearsonr(RH_V3_17LS,BrO_RH_V3_17LS)
#slopeD8_V3_17LS, interceptD8_V3_17LS, rD8_V3_17LS, pD8_V3_17LS, std_errD8_V3_17LS = stats.linregress(RH_V3_17LS,BrO_RH_V3_17LS)
#
##--------------------------------
## V1_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_18LS, p_valueD1_V1_18LS = stats.pearsonr(O3_V1_18LS,BrO_O3_V1_18LS)
#slopeD1_V1_18LS, interceptD1_V1_18LS, rD1_V1_18LS, pD1_V1_18LS, std_errD1_V1_18LS = stats.linregress(O3_V1_18LS,BrO_O3_V1_18LS)
#
## 2) Between Temp and BrO
#r_rowD2_V1_18LS, p_valueD2_V1_18LS = stats.pearsonr(Temp_V1_18LS,BrO_V1_18LS)
#slopeD2_V1_18LS, interceptD2_V1_18LS, rD2_V1_18LS, pD2_V1_18LS, std_errD2_V1_18LS = stats.linregress(Temp_V1_18LS,BrO_V1_18LS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_18LS, p_valueD3_V1_18LS = stats.pearsonr(WD_vect_V1_18LS,BrO_WD_V1_18LS)
#slopeD3_V1_18LS, interceptD3_V1_18LS, rD3_V1_18LS, pD3_V1_18LS, std_errD3_V1_18LS = stats.linregress(WD_vect_V1_18LS,BrO_WD_V1_18LS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_18LS, p_valueD4_V1_18LS = stats.pearsonr(WS_V1_18LS,BrO_WS_V1_18LS)
#slopeD4_V1_18LS, interceptD4_V1_18LS, rD4_V1_18LS, pD4_V1_18LS, std_errD4_V1_18LS = stats.linregress(WS_V1_18LS,BrO_WS_V1_18LS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_18LS, p_valueD5_V1_18LS = stats.pearsonr(Sol_V1_18LS,BrO_V1_18LS)
#slopeD5_V1_18LS, interceptD5_V1_18LS, rD5_V1_18LS, pD5_V1_18LS, std_errD5_V1_18LS = stats.linregress(Sol_V1_18LS,BrO_V1_18LS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_18LS, p_valueD6_V1_18LS = stats.pearsonr(Hg0_V1_18LS,BrO_Hg0_V1_18LS)
#slopeD6_V1_18LS, interceptD6_V1_18LS, rD6_V1_18LS, pD6_V1_18LS, std_errD6_V1_18LS = stats.linregress(Hg0_V1_18LS,BrO_Hg0_V1_18LS)
#
## 7) Between SI and BrO
#r_rowD7_V1_18LS, p_valueD7_V1_18LS = stats.pearsonr(SI_SI_V1_18LS,BrO_SI_V1_18LS)
#slopeD7_V1_18LS, interceptD7_V1_18LS, rD7_V1_18LS, pD7_V1_18LS, std_errD7_V1_18LS = stats.linregress(SI_SI_V1_18LS,BrO_SI_V1_18LS)
#
## 8) Between RH and BrO
#r_rowD8_V1_18LS, p_valueD8_V1_18LS = stats.pearsonr(RH_V1_18LS,BrO_RH_V1_18LS)
#slopeD8_V1_18LS, interceptD8_V1_18LS, rD8_V1_18LS, pD8_V1_18LS, std_errD8_V1_18LS = stats.linregress(RH_V1_18LS,BrO_RH_V1_18LS)
#
##--------------------------------
## V2_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V2_18LS, p_valueD1_V2_18LS = stats.pearsonr(O3_V2_18LS,BrO_O3_V2_18LS)
#slopeD1_V2_18LS, interceptD1_V2_18LS, rD1_V2_18LS, pD1_V2_18LS, std_errD1_V2_18LS = stats.linregress(O3_V2_18LS,BrO_O3_V2_18LS)
#
## 2) Between Temp and BrO
#r_rowD2_V2_18LS, p_valueD2_V2_18LS = stats.pearsonr(Temp_V2_18LS,BrO_V2_18LS)
#slopeD2_V2_18LS, interceptD2_V2_18LS, rD2_V2_18LS, pD2_V2_18LS, std_errD2_V2_18LS = stats.linregress(Temp_V2_18LS,BrO_V2_18LS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V2_18LS, p_valueD3_V2_18LS = stats.pearsonr(WD_vect_V2_18LS,BrO_WD_V2_18LS)
#slopeD3_V2_18LS, interceptD3_V2_18LS, rD3_V2_18LS, pD3_V2_18LS, std_errD3_V2_18LS = stats.linregress(WD_vect_V2_18LS,BrO_WD_V2_18LS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V2_18LS, p_valueD4_V2_18LS = stats.pearsonr(WS_V2_18LS,BrO_WS_V2_18LS)
#slopeD4_V2_18LS, interceptD4_V2_18LS, rD4_V2_18LS, pD4_V2_18LS, std_errD4_V2_18LS = stats.linregress(WS_V2_18LS,BrO_WS_V2_18LS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V2_18LS, p_valueD5_V2_18LS = stats.pearsonr(Sol_V2_18LS,BrO_V2_18LS)
#slopeD5_V2_18LS, interceptD5_V2_18LS, rD5_V2_18LS, pD5_V2_18LS, std_errD5_V2_18LS = stats.linregress(Sol_V2_18LS,BrO_V2_18LS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V2_18LS, p_valueD6_V2_18LS = stats.pearsonr(Hg0_V2_18LS,BrO_Hg0_V2_18LS)
#slopeD6_V2_18LS, interceptD6_V2_18LS, rD6_V2_18LS, pD6_V2_18LS, std_errD6_V2_18LS = stats.linregress(Hg0_V2_18LS,BrO_Hg0_V2_18LS)
#
## 7) Between SI and BrO
#r_rowD7_V2_18LS, p_valueD7_V2_18LS = stats.pearsonr(SI_SI_V2_18LS,BrO_SI_V2_18LS)
#slopeD7_V2_18LS, interceptD7_V2_18LS, rD7_V2_18LS, pD7_V2_18LS, std_errD7_V2_18LS = stats.linregress(SI_SI_V2_18LS,BrO_SI_V2_18LS)
#
## 8) Between RH and BrO
#r_rowD8_V2_18LS, p_valueD8_V2_18LS = stats.pearsonr(RH_V2_18LS,BrO_RH_V2_18LS)
#slopeD8_V2_18LS, interceptD8_V2_18LS, rD8_V2_18LS, pD8_V2_18LS, std_errD8_V2_18LS = stats.linregress(RH_V2_18LS,BrO_RH_V2_18LS)
#
##--------------------------------
## V3_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_18LS, p_valueD1_V3_18LS = stats.pearsonr(O3_V3_18LS,BrO_O3_V3_18LS)
#slopeD1_V3_18LS, interceptD1_V3_18LS, rD1_V3_18LS, pD1_V3_18LS, std_errD1_V3_18LS = stats.linregress(O3_V3_18LS,BrO_O3_V3_18LS)
#
## 2) Between Temp and BrO
#r_rowD2_V3_18LS, p_valueD2_V3_18LS = stats.pearsonr(Temp_V1_18LS,BrO_V1_18LS)
#slopeD2_V3_18LS, interceptD2_V3_18LS, rD2_V3_18LS, pD2_V3_18LS, std_errD2_V3_18LS = stats.linregress(Temp_V3_18LS,BrO_V3_18LS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_18LS, p_valueD3_V3_18LS = stats.pearsonr(WD_vect_V3_18LS,BrO_WD_V3_18LS)
#slopeD3_V3_18LS, interceptD3_V3_18LS, rD3_V3_18LS, pD3_V3_18LS, std_errD3_V3_18LS = stats.linregress(WD_vect_V3_18LS,BrO_WD_V3_18LS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_18LS, p_valueD4_V3_18LS = stats.pearsonr(WS_V3_18LS,BrO_WS_V3_18LS)
#slopeD4_V3_18LS, interceptD4_V3_18LS, rD4_V3_18LS, pD4_V3_18LS, std_errD4_V3_18LS = stats.linregress(WS_V3_18LS,BrO_WS_V3_18LS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_18LS, p_valueD5_V3_18LS = stats.pearsonr(Sol_V3_18LS,BrO_V3_18LS)
#slopeD5_V3_18LS, interceptD5_V3_18LS, rD5_V3_18LS, pD5_V3_18LS, std_errD5_V3_18LS = stats.linregress(Sol_V3_18LS,BrO_V3_18LS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_18LS, p_valueD6_V3_18LS = stats.pearsonr(Hg0_V3_18LS,BrO_Hg0_V3_18LS)
#slopeD6_V3_18LS, interceptD6_V3_18LS, rD6_V3_18LS, pD6_V3_18LS, std_errD6_V3_18LS = stats.linregress(Hg0_V3_18LS,BrO_Hg0_V3_18LS)
#
## 7) Between SI and BrO
#r_rowD7_V3_18LS, p_valueD7_V3_18LS = stats.pearsonr(SI_SI_V3_18LS,BrO_SI_V3_18LS)
#slopeD7_V3_18LS, interceptD7_V3_18LS, rD7_V3_18LS, pD7_V3_18LS, std_errD7_V3_18LS = stats.linregress(SI_SI_V3_18LS,BrO_SI_V3_18LS)
#
## 8) Between RH and BrO
#r_rowD8_V3_18LS, p_valueD8_V3_18LS = stats.pearsonr(RH_V3_18LS,BrO_RH_V3_18LS)
#slopeD8_V3_18LS, interceptD8_V3_18LS, rD8_V3_18LS, pD8_V3_18LS, std_errD8_V3_18LS = stats.linregress(RH_V3_18LS,BrO_RH_V3_18LS)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1LS, p_valueD1LS = stats.pearsonr(O3LS,BrO_O3LS)
slopeD1LS, interceptD1LS, rD1LS, pD1LS, std_errD1LS = stats.linregress(O3LS,BrO_O3LS)

# 2) Between Temp and BrO
r_rowD2LS, p_valueD2LS = stats.pearsonr(TempLS,BrOLS)
slopeD2LS, interceptD2LS, rD2LS, pD2LS, std_errD2LS = stats.linregress(TempLS,BrOLS)

# 3) Between Wind Direction and BrO
r_rowD3LS, p_valueD3LS = stats.pearsonr(WD_vectLS,BrO_WDLS)
slopeD3LS, interceptD3LS, rD3LS, pD3LS, std_errD3LS = stats.linregress(WD_vectLS,BrO_WDLS)

# 4) Between Wind Speed and BrO
r_rowD4LS, p_valueD4LS = stats.pearsonr(WSLS,BrO_WSLS)
slopeD4LS, interceptD4LS, rD4LS, pD4LS, std_errD4LS = stats.linregress(WSLS,BrO_WSLS)

# 5) Between Solar Radiation and BrO
r_rowD5LS, p_valueD5LS = stats.pearsonr(SolLS,BrOLS)
slopeD5LS, interceptD5LS, rD5LS, pD5LS, std_errD5LS = stats.linregress(SolLS,BrOLS)

# 6) Between Hg0 and BrO
r_rowD6LS, p_valueD6LS = stats.pearsonr(Hg0LS,BrO_Hg0LS)
slopeD6LS, interceptD6LS, rD6LS, pD6LS, std_errD6LS = stats.linregress(Hg0LS,BrO_Hg0LS)

# 7) Between SI and BrO
r_rowD7LS, p_valueD7LS = stats.pearsonr(SI_SILS,BrO_SILS)
slopeD7LS, interceptD7LS, rD7LS, pD7LS, std_errD7LS = stats.linregress(SI_SILS,BrO_SILS)

# 8) Between SI and BrO
r_rowD8LS, p_valueD8LS = stats.pearsonr(RHLS,BrO_RHLS)
slopeD8LS, interceptD8LS, rD8LS, pD8LS, std_errD8LS = stats.linregress(RHLS,BrO_RHLS)

#------------------------------------------------------------------------------
#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
##--------------------------------
## V1_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_17HS, p_valueD1_V1_17HS = stats.pearsonr(O3_V1_17HS,BrO_O3_V1_17HS)
#slopeD1_V1_17HS, interceptD1_V1_17HS, rD1_V1_17HS, pD1_V1_17HS, std_errD1_V1_17HS = stats.linregress(O3_V1_17HS,BrO_O3_V1_17HS)
#
## 2) Between Temp and BrO
#r_rowD2_V1_17HS, p_valueD2_V1_17HS = stats.pearsonr(Temp_V1_17HS,BrO_V1_17HS)
#slopeD2_V1_17HS, interceptD2_V1_17HS, rD2_V1_17HS, pD2_V1_17HS, std_errD2_V1_17HS = stats.linregress(Temp_V1_17HS,BrO_V1_17HS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_17HS, p_valueD3_V1_17HS = stats.pearsonr(WD_vect_V1_17HS,BrO_WD_V1_17HS)
#slopeD3_V1_17HS, interceptD3_V1_17HS, rD3_V1_17HS, pD3_V1_17HS, std_errD3_V1_17HS = stats.linregress(WD_vect_V1_17HS,BrO_WD_V1_17HS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_17HS, p_valueD4_V1_17HS = stats.pearsonr(WS_V1_17HS,BrO_WS_V1_17HS)
#slopeD4_V1_17HS, interceptD4_V1_17HS, rD4_V1_17HS, pD4_V1_17HS, std_errD4_V1_17HS = stats.linregress(WS_V1_17HS,BrO_WS_V1_17HS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_17HS, p_valueD5_V1_17HS = stats.pearsonr(Sol_V1_17HS,BrO_V1_17HS)
#slopeD5_V1_17HS, interceptD5_V1_17HS, rD5_V1_17HS, pD5_V1_17HS, std_errD5_V1_17HS = stats.linregress(Sol_V1_17HS,BrO_V1_17HS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_17HS, p_valueD6_V1_17HS = stats.pearsonr(Hg0_V1_17HS,BrO_Hg0_V1_17HS)
#slopeD6_V1_17HS, interceptD6_V1_17HS, rD6_V1_17HS, pD6_V1_17HS, std_errD6_V1_17HS = stats.linregress(Hg0_V1_17HS,BrO_Hg0_V1_17HS)
#
## 7) Between SI and BrO
#r_rowD7_V1_17HS, p_valueD7_V1_17HS = stats.pearsonr(SI_SI_V1_17HS,BrO_SI_V1_17HS)
#slopeD7_V1_17HS, interceptD7_V1_17HS, rD7_V1_17HS, pD7_V1_17HS, std_errD7_V1_17HS = stats.linregress(SI_SI_V1_17HS,BrO_SI_V1_17HS)
#
## 8) Between RH and BrO
#r_rowD8_V1_17HS, p_valueD8_V1_17HS = stats.pearsonr(RH_V1_17HS,BrO_RH_V1_17HS)
#slopeD8_V1_17HS, interceptD8_V1_17HS, rD8_V1_17HS, pD8_V1_17HS, std_errD8_V1_17HS = stats.linregress(RH_V1_17HS,BrO_RH_V1_17HS)
#
###--------------------------------
### V2_17 (2017-18)
###--------------------------------
### 1) Between O3 and BrO
##r_rowD1_V2_17HS, p_valueD1_V2_17HS = stats.pearsonr(O3_V2_17HS,BrO_O3_V2_17HS)
##slopeD1_V2_17HS, interceptD1_V2_17HS, rD1_V2_17HS, pD1_V2_17HS, std_errD1_V2_17HS = stats.linregress(O3_V2_17HS,BrO_O3_V2_17HS)
##
### 2) Between Temp and BrO
##r_rowD2_V2_17HS, p_valueD2_V2_17HS = stats.pearsonr(Temp_V2_17HS,BrO_V2_17HS)
##slopeD2_V2_17HS, interceptD2_V2_17HS, rD2_V2_17HS, pD2_V2_17HS, std_errD2_V2_17HS = stats.linregress(Temp_V2_17HS,BrO_V2_17HS)
##
### 3) Between Wind Direction and BrO
##r_rowD3_V2_17HS, p_valueD3_V2_17HS = stats.pearsonr(WD_vect_V2_17HS,BrO_WD_V2_17HS)
##slopeD3_V2_17HS, interceptD3_V2_17HS, rD3_V2_17HS, pD3_V2_17HS, std_errD3_V2_17HS = stats.linregress(WD_vect_V2_17HS,BrO_WD_V2_17HS)
##
### 4) Between Wind Speed and BrO
##r_rowD4_V2_17HS, p_valueD4_V2_17HS = stats.pearsonr(WS_V2_17HS,BrO_WS_V2_17HS)
##slopeD4_V2_17HS, interceptD4_V2_17HS, rD4_V2_17HS, pD4_V2_17HS, std_errD4_V2_17HS = stats.linregress(WS_V2_17HS,BrO_WS_V2_17HS)
##
### 5) Between Solar Radiation and BrO
##r_rowD5_V2_17HS, p_valueD5_V2_17HS = stats.pearsonr(Sol_V2_17HS,BrO_V2_17HS)
##slopeD5_V2_17HS, interceptD5_V2_17HS, rD5_V2_17HS, pD5_V2_17HS, std_errD5_V2_17HS = stats.linregress(Sol_V2_17HS,BrO_V2_17HS)
##
### 6) Between Hg0 and BrO
##r_rowD6_V2_17HS, p_valueD6_V2_17HS = stats.pearsonr(Hg0_V2_17HS,BrO_Hg0_V2_17HS)
##slopeD6_V2_17HS, interceptD6_V2_17HS, rD6_V2_17HS, pD6_V2_17HS, std_errD6_V2_17HS = stats.linregress(Hg0_V2_17HS,BrO_Hg0_V2_17HS)
##
### 7) Between SI and BrO
##r_rowD7_V2_17HS, p_valueD7_V2_17HS = stats.pearsonr(SI_SI_V2_17HS,BrO_SI_V2_17HS)
##slopeD7_V2_17HS, interceptD7_V2_17HS, rD7_V2_17HS, pD7_V2_17HS, std_errD7_V2_17HS = stats.linregress(SI_SI_V2_17HS,BrO_SI_V2_17HS)
#
## 8) Between RH and BrO
##r_rowD8_V2_17HS, p_valueD8_V2_17HS = stats.pearsonr(RH_V2_17HS,BrO_RH_V2_17HS)
##slopeD8_V2_17HS, interceptD8_V2_17HS, rD8_V2_17HS, pD8_V2_17HS, std_errD8_V2_17HS = stats.linregress(RH_V2_17HS,BrO_RH_V2_17HS)
#
##--------------------------------
## V3_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_17HS, p_valueD1_V3_17HS = stats.pearsonr(O3_V3_17HS,BrO_O3_V3_17HS)
#slopeD1_V3_17HS, interceptD1_V3_17HS, rD1_V3_17HS, pD1_V3_17HS, std_errD1_V3_17HS = stats.linregress(O3_V3_17HS,BrO_O3_V3_17HS)
#
## 2) Between Temp and BrO
#r_rowD2_V3_17HS, p_valueD2_V3_17HS = stats.pearsonr(Temp_V3_17HS,BrO_V3_17HS)
#slopeD2_V3_17HS, interceptD2_V3_17HS, rD2_V3_17HS, pD2_V3_17HS, std_errD2_V3_17HS = stats.linregress(Temp_V3_17HS,BrO_V3_17HS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_17HS, p_valueD3_V3_17HS = stats.pearsonr(WD_vect_V3_17HS,BrO_WD_V3_17HS)
#slopeD3_V3_17HS, interceptD3_V3_17HS, rD3_V3_17HS, pD3_V3_17HS, std_errD3_V3_17HS = stats.linregress(WD_vect_V3_17HS,BrO_WD_V3_17HS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_17HS, p_valueD4_V3_17HS = stats.pearsonr(WS_V3_17HS,BrO_WS_V3_17HS)
#slopeD4_V3_17HS, interceptD4_V3_17HS, rD4_V3_17HS, pD4_V3_17HS, std_errD4_V3_17HS = stats.linregress(WS_V3_17HS,BrO_WS_V3_17HS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_17HS, p_valueD5_V3_17HS = stats.pearsonr(Sol_V3_17HS,BrO_V3_17HS)
#slopeD5_V3_17HS, interceptD5_V3_17HS, rD5_V3_17HS, pD5_V3_17HS, std_errD5_V3_17HS = stats.linregress(Sol_V3_17HS,BrO_V3_17HS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_17HS, p_valueD6_V3_17HS = stats.pearsonr(Hg0_V3_17HS,BrO_Hg0_V3_17HS)
#slopeD6_V3_17HS, interceptD6_V3_17HS, rD6_V3_17HS, pD6_V3_17HS, std_errD6_V3_17HS = stats.linregress(Hg0_V3_17HS,BrO_Hg0_V3_17HS)
#
## 7) Between SI and BrO
#r_rowD7_V3_17HS, p_valueD7_V3_17HS = stats.pearsonr(SI_SI_V3_17HS,BrO_SI_V3_17HS)
#slopeD7_V3_17HS, interceptD7_V3_17HS, rD7_V3_17HS, pD7_V3_17HS, std_errD7_V3_17HS = stats.linregress(SI_SI_V3_17HS,BrO_SI_V3_17HS)
#
## 8) Between RH and BrO
#r_rowD8_V3_17HS, p_valueD8_V3_17HS = stats.pearsonr(RH_V3_17HS,BrO_RH_V3_17HS)
#slopeD8_V3_17HS, interceptD8_V3_17HS, rD8_V3_17HS, pD8_V3_17HS, std_errD8_V3_17HS = stats.linregress(RH_V3_17HS,BrO_RH_V3_17HS)
#
##--------------------------------
## V1_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_18HS, p_valueD1_V1_18HS = stats.pearsonr(O3_V1_18HS,BrO_O3_V1_18HS)
#slopeD1_V1_18HS, interceptD1_V1_18HS, rD1_V1_18HS, pD1_V1_18HS, std_errD1_V1_18HS = stats.linregress(O3_V1_18HS,BrO_O3_V1_18HS)
#
## 2) Between Temp and BrO
#r_rowD2_V1_18HS, p_valueD2_V1_18HS = stats.pearsonr(Temp_V1_18HS,BrO_V1_18HS)
#slopeD2_V1_18HS, interceptD2_V1_18HS, rD2_V1_18HS, pD2_V1_18HS, std_errD2_V1_18HS = stats.linregress(Temp_V1_18HS,BrO_V1_18HS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_18HS, p_valueD3_V1_18HS = stats.pearsonr(WD_vect_V1_18HS,BrO_WD_V1_18HS)
#slopeD3_V1_18HS, interceptD3_V1_18HS, rD3_V1_18HS, pD3_V1_18HS, std_errD3_V1_18HS = stats.linregress(WD_vect_V1_18HS,BrO_WD_V1_18HS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_18HS, p_valueD4_V1_18HS = stats.pearsonr(WS_V1_18HS,BrO_WS_V1_18HS)
#slopeD4_V1_18HS, interceptD4_V1_18HS, rD4_V1_18HS, pD4_V1_18HS, std_errD4_V1_18HS = stats.linregress(WS_V1_18HS,BrO_WS_V1_18HS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_18HS, p_valueD5_V1_18HS = stats.pearsonr(Sol_V1_18HS,BrO_V1_18HS)
#slopeD5_V1_18HS, interceptD5_V1_18HS, rD5_V1_18HS, pD5_V1_18HS, std_errD5_V1_18HS = stats.linregress(Sol_V1_18HS,BrO_V1_18HS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_18HS, p_valueD6_V1_18HS = stats.pearsonr(Hg0_V1_18HS,BrO_Hg0_V1_18HS)
#slopeD6_V1_18HS, interceptD6_V1_18HS, rD6_V1_18HS, pD6_V1_18HS, std_errD6_V1_18HS = stats.linregress(Hg0_V1_18HS,BrO_Hg0_V1_18HS)
#
## 7) Between SI and BrO
#r_rowD7_V1_18HS, p_valueD7_V1_18HS = stats.pearsonr(SI_SI_V1_18HS,BrO_SI_V1_18HS)
#slopeD7_V1_18HS, interceptD7_V1_18HS, rD7_V1_18HS, pD7_V1_18HS, std_errD7_V1_18HS = stats.linregress(SI_SI_V1_18HS,BrO_SI_V1_18HS)
#
## 8) Between RH and BrO
#r_rowD8_V1_18HS, p_valueD8_V1_18HS = stats.pearsonr(RH_V1_18HS,BrO_RH_V1_18HS)
#slopeD8_V1_18HS, interceptD8_V1_18HS, rD8_V1_18HS, pD8_V1_18HS, std_errD8_V1_18HS = stats.linregress(RH_V1_18HS,BrO_RH_V1_18HS)
#
##--------------------------------
## V2_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V2_18HS, p_valueD1_V2_18HS = stats.pearsonr(O3_V2_18HS,BrO_O3_V2_18HS)
#slopeD1_V2_18HS, interceptD1_V2_18HS, rD1_V2_18HS, pD1_V2_18HS, std_errD1_V2_18HS = stats.linregress(O3_V2_18HS,BrO_O3_V2_18HS)
#
## 2) Between Temp and BrO
#r_rowD2_V2_18HS, p_valueD2_V2_18HS = stats.pearsonr(Temp_V2_18HS,BrO_V2_18HS)
#slopeD2_V2_18HS, interceptD2_V2_18HS, rD2_V2_18HS, pD2_V2_18HS, std_errD2_V2_18HS = stats.linregress(Temp_V2_18HS,BrO_V2_18HS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V2_18HS, p_valueD3_V2_18HS = stats.pearsonr(WD_vect_V2_18HS,BrO_WD_V2_18HS)
#slopeD3_V2_18HS, interceptD3_V2_18HS, rD3_V2_18HS, pD3_V2_18HS, std_errD3_V2_18HS = stats.linregress(WD_vect_V2_18HS,BrO_WD_V2_18HS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V2_18HS, p_valueD4_V2_18HS = stats.pearsonr(WS_V2_18HS,BrO_WS_V2_18HS)
#slopeD4_V2_18HS, interceptD4_V2_18HS, rD4_V2_18HS, pD4_V2_18HS, std_errD4_V2_18HS = stats.linregress(WS_V2_18HS,BrO_WS_V2_18HS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V2_18HS, p_valueD5_V2_18HS = stats.pearsonr(Sol_V2_18HS,BrO_V2_18HS)
#slopeD5_V2_18HS, interceptD5_V2_18HS, rD5_V2_18HS, pD5_V2_18HS, std_errD5_V2_18HS = stats.linregress(Sol_V2_18HS,BrO_V2_18HS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V2_18HS, p_valueD6_V2_18HS = stats.pearsonr(Hg0_V2_18HS,BrO_Hg0_V2_18HS)
#slopeD6_V2_18HS, interceptD6_V2_18HS, rD6_V2_18HS, pD6_V2_18HS, std_errD6_V2_18HS = stats.linregress(Hg0_V2_18HS,BrO_Hg0_V2_18HS)
#
## 7) Between SI and BrO
#r_rowD7_V2_18HS, p_valueD7_V2_18HS = stats.pearsonr(SI_SI_V2_18HS,BrO_SI_V2_18HS)
#slopeD7_V2_18HS, interceptD7_V2_18HS, rD7_V2_18HS, pD7_V2_18HS, std_errD7_V2_18HS = stats.linregress(SI_SI_V2_18HS,BrO_SI_V2_18HS)
#
## 8) Between RH and BrO
#r_rowD8_V2_18HS, p_valueD8_V2_18HS = stats.pearsonr(RH_V2_18HS,BrO_RH_V2_18HS)
#slopeD8_V2_18HS, interceptD8_V2_18HS, rD8_V2_18HS, pD8_V2_18HS, std_errD8_V2_18HS = stats.linregress(RH_V2_18HS,BrO_RH_V2_18HS)
#
##--------------------------------
## V3_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_18HS, p_valueD1_V3_18HS = stats.pearsonr(O3_V3_18HS,BrO_O3_V3_18HS)
#slopeD1_V3_18HS, interceptD1_V3_18HS, rD1_V3_18HS, pD1_V3_18HS, std_errD1_V3_18HS = stats.linregress(O3_V3_18HS,BrO_O3_V3_18HS)
#
## 2) Between Temp and BrO
#r_rowD2_V3_18HS, p_valueD2_V3_18HS = stats.pearsonr(Temp_V1_18HS,BrO_V1_18HS)
#slopeD2_V3_18HS, interceptD2_V3_18HS, rD2_V3_18HS, pD2_V3_18HS, std_errD2_V3_18HS = stats.linregress(Temp_V3_18HS,BrO_V3_18HS)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_18HS, p_valueD3_V3_18HS = stats.pearsonr(WD_vect_V3_18HS,BrO_WD_V3_18HS)
#slopeD3_V3_18HS, interceptD3_V3_18HS, rD3_V3_18HS, pD3_V3_18HS, std_errD3_V3_18HS = stats.linregress(WD_vect_V3_18HS,BrO_WD_V3_18HS)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_18HS, p_valueD4_V3_18HS = stats.pearsonr(WS_V3_18HS,BrO_WS_V3_18HS)
#slopeD4_V3_18HS, interceptD4_V3_18HS, rD4_V3_18HS, pD4_V3_18HS, std_errD4_V3_18HS = stats.linregress(WS_V3_18HS,BrO_WS_V3_18HS)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_18HS, p_valueD5_V3_18HS = stats.pearsonr(Sol_V3_18HS,BrO_V3_18HS)
#slopeD5_V3_18HS, interceptD5_V3_18HS, rD5_V3_18HS, pD5_V3_18HS, std_errD5_V3_18HS = stats.linregress(Sol_V3_18HS,BrO_V3_18HS)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_18HS, p_valueD6_V3_18HS = stats.pearsonr(Hg0_V3_18HS,BrO_Hg0_V3_18HS)
#slopeD6_V3_18HS, interceptD6_V3_18HS, rD6_V3_18HS, pD6_V3_18HS, std_errD6_V3_18HS = stats.linregress(Hg0_V3_18HS,BrO_Hg0_V3_18HS)
#
## 7) Between SI and BrO
#r_rowD7_V3_18HS, p_valueD7_V3_18HS = stats.pearsonr(SI_SI_V3_18HS,BrO_SI_V3_18HS)
#slopeD7_V3_18HS, interceptD7_V3_18HS, rD7_V3_18HS, pD7_V3_18HS, std_errD7_V3_18HS = stats.linregress(SI_SI_V3_18HS,BrO_SI_V3_18HS)
#
## 8) Between RH and BrO
#r_rowD8_V3_18HS, p_valueD8_V3_18HS = stats.pearsonr(RH_V3_18HS,BrO_RH_V3_18HS)
#slopeD8_V3_18HS, interceptD8_V3_18HS, rD8_V3_18HS, pD8_V3_18HS, std_errD8_V3_18HS = stats.linregress(RH_V3_18HS,BrO_RH_V3_18HS)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1HS, p_valueD1HS = stats.pearsonr(O3HS,BrO_O3HS)
slopeD1HS, interceptD1HS, rD1HS, pD1HS, std_errD1HS = stats.linregress(O3HS,BrO_O3HS)

# 2) Between Temp and BrO
r_rowD2HS, p_valueD2HS = stats.pearsonr(TempHS,BrOHS)
slopeD2HS, interceptD2HS, rD2HS, pD2HS, std_errD2HS = stats.linregress(TempHS,BrOHS)

# 3) Between Wind Direction and BrO
r_rowD3HS, p_valueD3HS = stats.pearsonr(WD_vectHS,BrO_WDHS)
slopeD3HS, interceptD3HS, rD3HS, pD3HS, std_errD3HS = stats.linregress(WD_vectHS,BrO_WDHS)

# 4) Between Wind Speed and BrO
r_rowD4HS, p_valueD4HS = stats.pearsonr(WSHS,BrO_WSHS)
slopeD4HS, interceptD4HS, rD4HS, pD4HS, std_errD4HS = stats.linregress(WSHS,BrO_WSHS)

# 5) Between Solar Radiation and BrO
r_rowD5HS, p_valueD5HS = stats.pearsonr(SolHS,BrOHS)
slopeD5HS, interceptD5HS, rD5HS, pD5HS, std_errD5HS = stats.linregress(SolHS,BrOHS)

# 6) Between Hg0 and BrO
r_rowD6HS, p_valueD6HS = stats.pearsonr(Hg0HS,BrO_Hg0HS)
slopeD6HS, interceptD6HS, rD6HS, pD6HS, std_errD6HS = stats.linregress(Hg0HS,BrO_Hg0HS)

# 7) Between SI and BrO
r_rowD7HS, p_valueD7HS = stats.pearsonr(SI_SIHS,BrO_SIHS)
slopeD7HS, interceptD7HS, rD7HS, pD7HS, std_errD7HS = stats.linregress(SI_SIHS,BrO_SIHS)

# 8) Between SI and BrO
r_rowD8HS, p_valueD8HS = stats.pearsonr(RHHS,BrO_RHHS)
slopeD8HS, interceptD8HS, rD8HS, pD8HS, std_errD8HS = stats.linregress(RHHS,BrO_RHHS)

##-----------------------------------
## Low Wind Speed (<=7 m/s) *BOUNDARY*
##-----------------------------------
##--------------------------------
## V1_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_17LB, p_valueD1_V1_17LB = stats.pearsonr(O3_V1_17LB,BrO_O3_V1_17LB)
#slopeD1_V1_17LB, interceptD1_V1_17LB, rD1_V1_17LB, pD1_V1_17LB, std_errD1_V1_17LB = stats.linregress(O3_V1_17LB,BrO_O3_V1_17LB)
#
## 2) Between Temp and BrO
#r_rowD2_V1_17LB, p_valueD2_V1_17LB = stats.pearsonr(Temp_V1_17LB,BrO_V1_17LB)
#slopeD2_V1_17LB, interceptD2_V1_17LB, rD2_V1_17LB, pD2_V1_17LB, std_errD2_V1_17LB = stats.linregress(Temp_V1_17LB,BrO_V1_17LB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_17LB, p_valueD3_V1_17LB = stats.pearsonr(WD_vect_V1_17LB,BrO_WD_V1_17LB)
#slopeD3_V1_17LB, interceptD3_V1_17LB, rD3_V1_17LB, pD3_V1_17LB, std_errD3_V1_17LB = stats.linregress(WD_vect_V1_17LB,BrO_WD_V1_17LB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_17LB, p_valueD4_V1_17LB = stats.pearsonr(WS_V1_17LB,BrO_WS_V1_17LB)
#slopeD4_V1_17LB, interceptD4_V1_17LB, rD4_V1_17LB, pD4_V1_17LB, std_errD4_V1_17LB = stats.linregress(WS_V1_17LB,BrO_WS_V1_17LB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_17LB, p_valueD5_V1_17LB = stats.pearsonr(Sol_V1_17LB,BrO_V1_17LB)
#slopeD5_V1_17LB, interceptD5_V1_17LB, rD5_V1_17LB, pD5_V1_17LB, std_errD5_V1_17LB = stats.linregress(Sol_V1_17LB,BrO_V1_17LB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_17LB, p_valueD6_V1_17LB = stats.pearsonr(Hg0_V1_17LB,BrO_Hg0_V1_17LB)
#slopeD6_V1_17LB, interceptD6_V1_17LB, rD6_V1_17LB, pD6_V1_17LB, std_errD6_V1_17LB = stats.linregress(Hg0_V1_17LB,BrO_Hg0_V1_17LB)
#
## 7) Between SI and BrO
#r_rowD7_V1_17LB, p_valueD7_V1_17LB = stats.pearsonr(SI_SI_V1_17LB,BrO_SI_V1_17LB)
#slopeD7_V1_17LB, interceptD7_V1_17LB, rD7_V1_17LB, pD7_V1_17LB, std_errD7_V1_17LB = stats.linregress(SI_SI_V1_17LB,BrO_SI_V1_17LB)
#
## 8) Between RH and BrO
#r_rowD8_V1_17LB, p_valueD8_V1_17LB = stats.pearsonr(RH_V1_17LB,BrO_RH_V1_17LB)
#slopeD8_V1_17LB, interceptD8_V1_17LB, rD8_V1_17LB, pD8_V1_17LB, std_errD8_V1_17LB = stats.linregress(RH_V1_17LB,BrO_RH_V1_17LB)
#
##--------------------------------
## V2_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V2_17LB, p_valueD1_V2_17LB = stats.pearsonr(O3_V2_17LB,BrO_O3_V2_17LB)
#slopeD1_V2_17LB, interceptD1_V2_17LB, rD1_V2_17LB, pD1_V2_17LB, std_errD1_V2_17LB = stats.linregress(O3_V2_17LB,BrO_O3_V2_17LB)
#
## 2) Between Temp and BrO
#r_rowD2_V2_17LB, p_valueD2_V2_17LB = stats.pearsonr(Temp_V2_17LB,BrO_V2_17LB)
#slopeD2_V2_17LB, interceptD2_V2_17LB, rD2_V2_17LB, pD2_V2_17LB, std_errD2_V2_17LB = stats.linregress(Temp_V2_17LB,BrO_V2_17LB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V2_17LB, p_valueD3_V2_17LB = stats.pearsonr(WD_vect_V2_17LB,BrO_WD_V2_17LB)
#slopeD3_V2_17LB, interceptD3_V2_17LB, rD3_V2_17LB, pD3_V2_17LB, std_errD3_V2_17LB = stats.linregress(WD_vect_V2_17LB,BrO_WD_V2_17LB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V2_17LB, p_valueD4_V2_17LB = stats.pearsonr(WS_V2_17LB,BrO_WS_V2_17LB)
#slopeD4_V2_17LB, interceptD4_V2_17LB, rD4_V2_17LB, pD4_V2_17LB, std_errD4_V2_17LB = stats.linregress(WS_V2_17LB,BrO_WS_V2_17LB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V2_17LB, p_valueD5_V2_17LB = stats.pearsonr(Sol_V2_17LB,BrO_V2_17LB)
#slopeD5_V2_17LB, interceptD5_V2_17LB, rD5_V2_17LB, pD5_V2_17LB, std_errD5_V2_17LB = stats.linregress(Sol_V2_17LB,BrO_V2_17LB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V2_17LB, p_valueD6_V2_17LB = stats.pearsonr(Hg0_V2_17LB,BrO_Hg0_V2_17LB)
#slopeD6_V2_17LB, interceptD6_V2_17LB, rD6_V2_17LB, pD6_V2_17LB, std_errD6_V2_17LB = stats.linregress(Hg0_V2_17LB,BrO_Hg0_V2_17LB)
#
## 7) Between SI and BrO
#r_rowD7_V2_17LB, p_valueD7_V2_17LB = stats.pearsonr(SI_SI_V2_17LB,BrO_SI_V2_17LB)
#slopeD7_V2_17LB, interceptD7_V2_17LB, rD7_V2_17LB, pD7_V2_17LB, std_errD7_V2_17LB = stats.linregress(SI_SI_V2_17LB,BrO_SI_V2_17LB)
#
## 8) Between RH and BrO
#r_rowD8_V2_17LB, p_valueD8_V2_17LB = stats.pearsonr(RH_V2_17LB,BrO_RH_V2_17LB)
#slopeD8_V2_17LB, interceptD8_V2_17LB, rD8_V2_17LB, pD8_V2_17LB, std_errD8_V2_17LB = stats.linregress(RH_V2_17LB,BrO_RH_V2_17LB)
#
##--------------------------------
## V3_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_17LB, p_valueD1_V3_17LB = stats.pearsonr(O3_V3_17LB,BrO_O3_V3_17LB)
#slopeD1_V3_17LB, interceptD1_V3_17LB, rD1_V3_17LB, pD1_V3_17LB, std_errD1_V3_17LB = stats.linregress(O3_V3_17LB,BrO_O3_V3_17LB)
#
## 2) Between Temp and BrO
#r_rowD2_V3_17LB, p_valueD2_V3_17LB = stats.pearsonr(Temp_V3_17LB,BrO_V3_17LB)
#slopeD2_V3_17LB, interceptD2_V3_17LB, rD2_V3_17LB, pD2_V3_17LB, std_errD2_V3_17LB = stats.linregress(Temp_V3_17LB,BrO_V3_17LB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_17LB, p_valueD3_V3_17LB = stats.pearsonr(WD_vect_V3_17LB,BrO_WD_V3_17LB)
#slopeD3_V3_17LB, interceptD3_V3_17LB, rD3_V3_17LB, pD3_V3_17LB, std_errD3_V3_17LB = stats.linregress(WD_vect_V3_17LB,BrO_WD_V3_17LB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_17LB, p_valueD4_V3_17LB = stats.pearsonr(WS_V3_17LB,BrO_WS_V3_17LB)
#slopeD4_V3_17LB, interceptD4_V3_17LB, rD4_V3_17LB, pD4_V3_17LB, std_errD4_V3_17LB = stats.linregress(WS_V3_17LB,BrO_WS_V3_17LB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_17LB, p_valueD5_V3_17LB = stats.pearsonr(Sol_V3_17LB,BrO_V3_17LB)
#slopeD5_V3_17LB, interceptD5_V3_17LB, rD5_V3_17LB, pD5_V3_17LB, std_errD5_V3_17LB = stats.linregress(Sol_V3_17LB,BrO_V3_17LB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_17LB, p_valueD6_V3_17LB = stats.pearsonr(Hg0_V3_17LB,BrO_Hg0_V3_17LB)
#slopeD6_V3_17LB, interceptD6_V3_17LB, rD6_V3_17LB, pD6_V3_17LB, std_errD6_V3_17LB = stats.linregress(Hg0_V3_17LB,BrO_Hg0_V3_17LB)
#
## 7) Between SI and BrO
#r_rowD7_V3_17LB, p_valueD7_V3_17LB = stats.pearsonr(SI_SI_V3_17LB,BrO_SI_V3_17LB)
#slopeD7_V3_17LB, interceptD7_V3_17LB, rD7_V3_17LB, pD7_V3_17LB, std_errD7_V3_17LB = stats.linregress(SI_SI_V3_17LB,BrO_SI_V3_17LB)
#
## 8) Between RH and BrO
#r_rowD8_V3_17LB, p_valueD8_V3_17LB = stats.pearsonr(RH_V3_17LB,BrO_RH_V3_17LB)
#slopeD8_V3_17LB, interceptD8_V3_17LB, rD8_V3_17LB, pD8_V3_17LB, std_errD8_V3_17LB = stats.linregress(RH_V3_17LB,BrO_RH_V3_17LB)
#
##--------------------------------
## V1_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_18LB, p_valueD1_V1_18LB = stats.pearsonr(O3_V1_18LB,BrO_O3_V1_18LB)
#slopeD1_V1_18LB, interceptD1_V1_18LB, rD1_V1_18LB, pD1_V1_18LB, std_errD1_V1_18LB = stats.linregress(O3_V1_18LB,BrO_O3_V1_18LB)
#
## 2) Between Temp and BrO
#r_rowD2_V1_18LB, p_valueD2_V1_18LB = stats.pearsonr(Temp_V1_18LB,BrO_V1_18LB)
#slopeD2_V1_18LB, interceptD2_V1_18LB, rD2_V1_18LB, pD2_V1_18LB, std_errD2_V1_18LB = stats.linregress(Temp_V1_18LB,BrO_V1_18LB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_18LB, p_valueD3_V1_18LB = stats.pearsonr(WD_vect_V1_18LB,BrO_WD_V1_18LB)
#slopeD3_V1_18LB, interceptD3_V1_18LB, rD3_V1_18LB, pD3_V1_18LB, std_errD3_V1_18LB = stats.linregress(WD_vect_V1_18LB,BrO_WD_V1_18LB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_18LB, p_valueD4_V1_18LB = stats.pearsonr(WS_V1_18LB,BrO_WS_V1_18LB)
#slopeD4_V1_18LB, interceptD4_V1_18LB, rD4_V1_18LB, pD4_V1_18LB, std_errD4_V1_18LB = stats.linregress(WS_V1_18LB,BrO_WS_V1_18LB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_18LB, p_valueD5_V1_18LB = stats.pearsonr(Sol_V1_18LB,BrO_V1_18LB)
#slopeD5_V1_18LB, interceptD5_V1_18LB, rD5_V1_18LB, pD5_V1_18LB, std_errD5_V1_18LB = stats.linregress(Sol_V1_18LB,BrO_V1_18LB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_18LB, p_valueD6_V1_18LB = stats.pearsonr(Hg0_V1_18LB,BrO_Hg0_V1_18LB)
#slopeD6_V1_18LB, interceptD6_V1_18LB, rD6_V1_18LB, pD6_V1_18LB, std_errD6_V1_18LB = stats.linregress(Hg0_V1_18LB,BrO_Hg0_V1_18LB)
#
## 7) Between SI and BrO
#r_rowD7_V1_18LB, p_valueD7_V1_18LB = stats.pearsonr(SI_SI_V1_18LB,BrO_SI_V1_18LB)
#slopeD7_V1_18LB, interceptD7_V1_18LB, rD7_V1_18LB, pD7_V1_18LB, std_errD7_V1_18LB = stats.linregress(SI_SI_V1_18LB,BrO_SI_V1_18LB)
#
## 8) Between RH and BrO
#r_rowD8_V1_18LB, p_valueD8_V1_18LB = stats.pearsonr(RH_V1_18LB,BrO_RH_V1_18LB)
#slopeD8_V1_18LB, interceptD8_V1_18LB, rD8_V1_18LB, pD8_V1_18LB, std_errD8_V1_18LB = stats.linregress(RH_V1_18LB,BrO_RH_V1_18LB)
#
##--------------------------------
## V2_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V2_18LB, p_valueD1_V2_18LB = stats.pearsonr(O3_V2_18LB,BrO_O3_V2_18LB)
#slopeD1_V2_18LB, interceptD1_V2_18LB, rD1_V2_18LB, pD1_V2_18LB, std_errD1_V2_18LB = stats.linregress(O3_V2_18LB,BrO_O3_V2_18LB)
#
## 2) Between Temp and BrO
#r_rowD2_V2_18LB, p_valueD2_V2_18LB = stats.pearsonr(Temp_V2_18LB,BrO_V2_18LB)
#slopeD2_V2_18LB, interceptD2_V2_18LB, rD2_V2_18LB, pD2_V2_18LB, std_errD2_V2_18LB = stats.linregress(Temp_V2_18LB,BrO_V2_18LB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V2_18LB, p_valueD3_V2_18LB = stats.pearsonr(WD_vect_V2_18LB,BrO_WD_V2_18LB)
#slopeD3_V2_18LB, interceptD3_V2_18LB, rD3_V2_18LB, pD3_V2_18LB, std_errD3_V2_18LB = stats.linregress(WD_vect_V2_18LB,BrO_WD_V2_18LB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V2_18LB, p_valueD4_V2_18LB = stats.pearsonr(WS_V2_18LB,BrO_WS_V2_18LB)
#slopeD4_V2_18LB, interceptD4_V2_18LB, rD4_V2_18LB, pD4_V2_18LB, std_errD4_V2_18LB = stats.linregress(WS_V2_18LB,BrO_WS_V2_18LB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V2_18LB, p_valueD5_V2_18LB = stats.pearsonr(Sol_V2_18LB,BrO_V2_18LB)
#slopeD5_V2_18LB, interceptD5_V2_18LB, rD5_V2_18LB, pD5_V2_18LB, std_errD5_V2_18LB = stats.linregress(Sol_V2_18LB,BrO_V2_18LB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V2_18LB, p_valueD6_V2_18LB = stats.pearsonr(Hg0_V2_18LB,BrO_Hg0_V2_18LB)
#slopeD6_V2_18LB, interceptD6_V2_18LB, rD6_V2_18LB, pD6_V2_18LB, std_errD6_V2_18LB = stats.linregress(Hg0_V2_18LB,BrO_Hg0_V2_18LB)
#
## 7) Between SI and BrO
#r_rowD7_V2_18LB, p_valueD7_V2_18LB = stats.pearsonr(SI_SI_V2_18LB,BrO_SI_V2_18LB)
#slopeD7_V2_18LB, interceptD7_V2_18LB, rD7_V2_18LB, pD7_V2_18LB, std_errD7_V2_18LB = stats.linregress(SI_SI_V2_18LB,BrO_SI_V2_18LB)
#
## 8) Between RH and BrO
#r_rowD8_V2_18LB, p_valueD8_V2_18LB = stats.pearsonr(RH_V2_18LB,BrO_RH_V2_18LB)
#slopeD8_V2_18LB, interceptD8_V2_18LB, rD8_V2_18LB, pD8_V2_18LB, std_errD8_V2_18LB = stats.linregress(RH_V2_18LB,BrO_RH_V2_18LB)
#
##--------------------------------
## V3_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_18LB, p_valueD1_V3_18LB = stats.pearsonr(O3_V3_18LB,BrO_O3_V3_18LB)
#slopeD1_V3_18LB, interceptD1_V3_18LB, rD1_V3_18LB, pD1_V3_18LB, std_errD1_V3_18LB = stats.linregress(O3_V3_18LB,BrO_O3_V3_18LB)
#
## 2) Between Temp and BrO
#r_rowD2_V3_18LB, p_valueD2_V3_18LB = stats.pearsonr(Temp_V1_18LB,BrO_V1_18LB)
#slopeD2_V3_18LB, interceptD2_V3_18LB, rD2_V3_18LB, pD2_V3_18LB, std_errD2_V3_18LB = stats.linregress(Temp_V3_18LB,BrO_V3_18LB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_18LB, p_valueD3_V3_18LB = stats.pearsonr(WD_vect_V3_18LB,BrO_WD_V3_18LB)
#slopeD3_V3_18LB, interceptD3_V3_18LB, rD3_V3_18LB, pD3_V3_18LB, std_errD3_V3_18LB = stats.linregress(WD_vect_V3_18LB,BrO_WD_V3_18LB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_18LB, p_valueD4_V3_18LB = stats.pearsonr(WS_V3_18LB,BrO_WS_V3_18LB)
#slopeD4_V3_18LB, interceptD4_V3_18LB, rD4_V3_18LB, pD4_V3_18LB, std_errD4_V3_18LB = stats.linregress(WS_V3_18LB,BrO_WS_V3_18LB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_18LB, p_valueD5_V3_18LB = stats.pearsonr(Sol_V3_18LB,BrO_V3_18LB)
#slopeD5_V3_18LB, interceptD5_V3_18LB, rD5_V3_18LB, pD5_V3_18LB, std_errD5_V3_18LB = stats.linregress(Sol_V3_18LB,BrO_V3_18LB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_18LB, p_valueD6_V3_18LB = stats.pearsonr(Hg0_V3_18LB,BrO_Hg0_V3_18LB)
#slopeD6_V3_18LB, interceptD6_V3_18LB, rD6_V3_18LB, pD6_V3_18LB, std_errD6_V3_18LB = stats.linregress(Hg0_V3_18LB,BrO_Hg0_V3_18LB)
#
## 7) Between SI and BrO
#r_rowD7_V3_18LB, p_valueD7_V3_18LB = stats.pearsonr(SI_SI_V3_18LB,BrO_SI_V3_18LB)
#slopeD7_V3_18LB, interceptD7_V3_18LB, rD7_V3_18LB, pD7_V3_18LB, std_errD7_V3_18LB = stats.linregress(SI_SI_V3_18LB,BrO_SI_V3_18LB)
#
## 8) Between RH and BrO
#r_rowD8_V3_18LB, p_valueD8_V3_18LB = stats.pearsonr(RH_V3_18LB,BrO_RH_V3_18LB)
#slopeD8_V3_18LB, interceptD8_V3_18LB, rD8_V3_18LB, pD8_V3_18LB, std_errD8_V3_18LB = stats.linregress(RH_V3_18LB,BrO_RH_V3_18LB)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1LB, p_valueD1LB = stats.pearsonr(O3LB,BrO_O3LB)
slopeD1LB, interceptD1LB, rD1LB, pD1LB, std_errD1LB = stats.linregress(O3LB,BrO_O3LB)

# 2) Between Temp and BrO
r_rowD2LB, p_valueD2LB = stats.pearsonr(TempLB,BrOLB)
slopeD2LB, interceptD2LB, rD2LB, pD2LB, std_errD2LB = stats.linregress(TempLB,BrOLB)

# 3) Between Wind Direction and BrO
r_rowD3LB, p_valueD3LB = stats.pearsonr(WD_vectLB,BrO_WDLB)
slopeD3LB, interceptD3LB, rD3LB, pD3LB, std_errD3LB = stats.linregress(WD_vectLB,BrO_WDLB)

# 4) Between Wind Speed and BrO
r_rowD4LB, p_valueD4LB = stats.pearsonr(WSLB,BrO_WSLB)
slopeD4LB, interceptD4LB, rD4LB, pD4LB, std_errD4LB = stats.linregress(WSLB,BrO_WSLB)

# 5) Between Solar Radiation and BrO
r_rowD5LB, p_valueD5LB = stats.pearsonr(SolLB,BrOLB)
slopeD5LB, interceptD5LB, rD5LB, pD5LB, std_errD5LB = stats.linregress(SolLB,BrOLB)

# 6) Between Hg0 and BrO
r_rowD6LB, p_valueD6LB = stats.pearsonr(Hg0LB,BrO_Hg0LB)
slopeD6LB, interceptD6LB, rD6LB, pD6LB, std_errD6LB = stats.linregress(Hg0LB,BrO_Hg0LB)

# 7) Between SI and BrO
r_rowD7LB, p_valueD7LB = stats.pearsonr(SI_SILB,BrO_SILB)
slopeD7LB, interceptD7LB, rD7LB, pD7LB, std_errD7LB = stats.linregress(SI_SILB,BrO_SILB)

# 8) Between SI and BrO
r_rowD8LB, p_valueD8LB = stats.pearsonr(RHLB,BrO_RHLB)
slopeD8LB, interceptD8LB, rD8LB, pD8LB, std_errD8LB = stats.linregress(RHLB,BrO_RHLB)

#------------------------------------------------------------------------------
##-----------------------------------
## High Wind Speed (>7 m/s) *BOUNDARY*
##-----------------------------------
##--------------------------------
## V1_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_17HB, p_valueD1_V1_17HB = stats.pearsonr(O3_V1_17HB,BrO_O3_V1_17HB)
#slopeD1_V1_17HB, interceptD1_V1_17HB, rD1_V1_17HB, pD1_V1_17HB, std_errD1_V1_17HB = stats.linregress(O3_V1_17HB,BrO_O3_V1_17HB)
#
## 2) Between Temp and BrO
#r_rowD2_V1_17HB, p_valueD2_V1_17HB = stats.pearsonr(Temp_V1_17HB,BrO_V1_17HB)
#slopeD2_V1_17HB, interceptD2_V1_17HB, rD2_V1_17HB, pD2_V1_17HB, std_errD2_V1_17HB = stats.linregress(Temp_V1_17HB,BrO_V1_17HB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_17HB, p_valueD3_V1_17HB = stats.pearsonr(WD_vect_V1_17HB,BrO_WD_V1_17HB)
#slopeD3_V1_17HB, interceptD3_V1_17HB, rD3_V1_17HB, pD3_V1_17HB, std_errD3_V1_17HB = stats.linregress(WD_vect_V1_17HB,BrO_WD_V1_17HB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_17HB, p_valueD4_V1_17HB = stats.pearsonr(WS_V1_17HB,BrO_WS_V1_17HB)
#slopeD4_V1_17HB, interceptD4_V1_17HB, rD4_V1_17HB, pD4_V1_17HB, std_errD4_V1_17HB = stats.linregress(WS_V1_17HB,BrO_WS_V1_17HB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_17HB, p_valueD5_V1_17HB = stats.pearsonr(Sol_V1_17HB,BrO_V1_17HB)
#slopeD5_V1_17HB, interceptD5_V1_17HB, rD5_V1_17HB, pD5_V1_17HB, std_errD5_V1_17HB = stats.linregress(Sol_V1_17HB,BrO_V1_17HB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_17HB, p_valueD6_V1_17HB = stats.pearsonr(Hg0_V1_17HB,BrO_Hg0_V1_17HB)
#slopeD6_V1_17HB, interceptD6_V1_17HB, rD6_V1_17HB, pD6_V1_17HB, std_errD6_V1_17HB = stats.linregress(Hg0_V1_17HB,BrO_Hg0_V1_17HB)
#
## 7) Between SI and BrO
#r_rowD7_V1_17HB, p_valueD7_V1_17HB = stats.pearsonr(SI_SI_V1_17HB,BrO_SI_V1_17HB)
#slopeD7_V1_17HB, interceptD7_V1_17HB, rD7_V1_17HB, pD7_V1_17HB, std_errD7_V1_17HB = stats.linregress(SI_SI_V1_17HB,BrO_SI_V1_17HB)
#
## 8) Between RH and BrO
#r_rowD8_V1_17HB, p_valueD8_V1_17HB = stats.pearsonr(RH_V1_17HB,BrO_RH_V1_17HB)
#slopeD8_V1_17HB, interceptD8_V1_17HB, rD8_V1_17HB, pD8_V1_17HB, std_errD8_V1_17HB = stats.linregress(RH_V1_17HB,BrO_RH_V1_17HB)
#
###--------------------------------
### V2_17 (2017-18)
###--------------------------------
### 1) Between O3 and BrO
##r_rowD1_V2_17HB, p_valueD1_V2_17HB = stats.pearsonr(O3_V2_17HB,BrO_O3_V2_17HB)
##slopeD1_V2_17HB, interceptD1_V2_17HB, rD1_V2_17HB, pD1_V2_17HB, std_errD1_V2_17HB = stats.linregress(O3_V2_17HB,BrO_O3_V2_17HB)
##
### 2) Between Temp and BrO
##r_rowD2_V2_17HB, p_valueD2_V2_17HB = stats.pearsonr(Temp_V2_17HB,BrO_V2_17HB)
##slopeD2_V2_17HB, interceptD2_V2_17HB, rD2_V2_17HB, pD2_V2_17HB, std_errD2_V2_17HB = stats.linregress(Temp_V2_17HB,BrO_V2_17HB)
##
### 3) Between Wind Direction and BrO
##r_rowD3_V2_17HB, p_valueD3_V2_17HB = stats.pearsonr(WD_vect_V2_17HB,BrO_WD_V2_17HB)
##slopeD3_V2_17HB, interceptD3_V2_17HB, rD3_V2_17HB, pD3_V2_17HB, std_errD3_V2_17HB = stats.linregress(WD_vect_V2_17HB,BrO_WD_V2_17HB)
##
### 4) Between Wind Speed and BrO
##r_rowD4_V2_17HB, p_valueD4_V2_17HB = stats.pearsonr(WS_V2_17HB,BrO_WS_V2_17HB)
##slopeD4_V2_17HB, interceptD4_V2_17HB, rD4_V2_17HB, pD4_V2_17HB, std_errD4_V2_17HB = stats.linregress(WS_V2_17HB,BrO_WS_V2_17HB)
##
### 5) Between Solar Radiation and BrO
##r_rowD5_V2_17HB, p_valueD5_V2_17HB = stats.pearsonr(Sol_V2_17HB,BrO_V2_17HB)
##slopeD5_V2_17HB, interceptD5_V2_17HB, rD5_V2_17HB, pD5_V2_17HB, std_errD5_V2_17HB = stats.linregress(Sol_V2_17HB,BrO_V2_17HB)
##
### 6) Between Hg0 and BrO
##r_rowD6_V2_17HB, p_valueD6_V2_17HB = stats.pearsonr(Hg0_V2_17HB,BrO_Hg0_V2_17HB)
##slopeD6_V2_17HB, interceptD6_V2_17HB, rD6_V2_17HB, pD6_V2_17HB, std_errD6_V2_17HB = stats.linregress(Hg0_V2_17HB,BrO_Hg0_V2_17HB)
##
### 7) Between SI and BrO
##r_rowD7_V2_17HB, p_valueD7_V2_17HB = stats.pearsonr(SI_SI_V2_17HB,BrO_SI_V2_17HB)
##slopeD7_V2_17HB, interceptD7_V2_17HB, rD7_V2_17HB, pD7_V2_17HB, std_errD7_V2_17HB = stats.linregress(SI_SI_V2_17HB,BrO_SI_V2_17HB)
#
## 8) Between RH and BrO
##r_rowD8_V2_17HB, p_valueD8_V2_17HB = stats.pearsonr(RH_V2_17HB,BrO_RH_V2_17HB)
##slopeD8_V2_17HB, interceptD8_V2_17HB, rD8_V2_17HB, pD8_V2_17HB, std_errD8_V2_17HB = stats.linregress(RH_V2_17HB,BrO_RH_V2_17HB)
#
##--------------------------------
## V3_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_17HB, p_valueD1_V3_17HB = stats.pearsonr(O3_V3_17HB,BrO_O3_V3_17HB)
#slopeD1_V3_17HB, interceptD1_V3_17HB, rD1_V3_17HB, pD1_V3_17HB, std_errD1_V3_17HB = stats.linregress(O3_V3_17HB,BrO_O3_V3_17HB)
#
## 2) Between Temp and BrO
#r_rowD2_V3_17HB, p_valueD2_V3_17HB = stats.pearsonr(Temp_V3_17HB,BrO_V3_17HB)
#slopeD2_V3_17HB, interceptD2_V3_17HB, rD2_V3_17HB, pD2_V3_17HB, std_errD2_V3_17HB = stats.linregress(Temp_V3_17HB,BrO_V3_17HB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_17HB, p_valueD3_V3_17HB = stats.pearsonr(WD_vect_V3_17HB,BrO_WD_V3_17HB)
#slopeD3_V3_17HB, interceptD3_V3_17HB, rD3_V3_17HB, pD3_V3_17HB, std_errD3_V3_17HB = stats.linregress(WD_vect_V3_17HB,BrO_WD_V3_17HB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_17HB, p_valueD4_V3_17HB = stats.pearsonr(WS_V3_17HB,BrO_WS_V3_17HB)
#slopeD4_V3_17HB, interceptD4_V3_17HB, rD4_V3_17HB, pD4_V3_17HB, std_errD4_V3_17HB = stats.linregress(WS_V3_17HB,BrO_WS_V3_17HB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_17HB, p_valueD5_V3_17HB = stats.pearsonr(Sol_V3_17HB,BrO_V3_17HB)
#slopeD5_V3_17HB, interceptD5_V3_17HB, rD5_V3_17HB, pD5_V3_17HB, std_errD5_V3_17HB = stats.linregress(Sol_V3_17HB,BrO_V3_17HB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_17HB, p_valueD6_V3_17HB = stats.pearsonr(Hg0_V3_17HB,BrO_Hg0_V3_17HB)
#slopeD6_V3_17HB, interceptD6_V3_17HB, rD6_V3_17HB, pD6_V3_17HB, std_errD6_V3_17HB = stats.linregress(Hg0_V3_17HB,BrO_Hg0_V3_17HB)
#
## 7) Between SI and BrO
#r_rowD7_V3_17HB, p_valueD7_V3_17HB = stats.pearsonr(SI_SI_V3_17HB,BrO_SI_V3_17HB)
#slopeD7_V3_17HB, interceptD7_V3_17HB, rD7_V3_17HB, pD7_V3_17HB, std_errD7_V3_17HB = stats.linregress(SI_SI_V3_17HB,BrO_SI_V3_17HB)
#
## 8) Between RH and BrO
#r_rowD8_V3_17HB, p_valueD8_V3_17HB = stats.pearsonr(RH_V3_17HB,BrO_RH_V3_17HB)
#slopeD8_V3_17HB, interceptD8_V3_17HB, rD8_V3_17HB, pD8_V3_17HB, std_errD8_V3_17HB = stats.linregress(RH_V3_17HB,BrO_RH_V3_17HB)
#
##--------------------------------
## V1_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V1_18HB, p_valueD1_V1_18HB = stats.pearsonr(O3_V1_18HB,BrO_O3_V1_18HB)
#slopeD1_V1_18HB, interceptD1_V1_18HB, rD1_V1_18HB, pD1_V1_18HB, std_errD1_V1_18HB = stats.linregress(O3_V1_18HB,BrO_O3_V1_18HB)
#
## 2) Between Temp and BrO
#r_rowD2_V1_18HB, p_valueD2_V1_18HB = stats.pearsonr(Temp_V1_18HB,BrO_V1_18HB)
#slopeD2_V1_18HB, interceptD2_V1_18HB, rD2_V1_18HB, pD2_V1_18HB, std_errD2_V1_18HB = stats.linregress(Temp_V1_18HB,BrO_V1_18HB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V1_18HB, p_valueD3_V1_18HB = stats.pearsonr(WD_vect_V1_18HB,BrO_WD_V1_18HB)
#slopeD3_V1_18HB, interceptD3_V1_18HB, rD3_V1_18HB, pD3_V1_18HB, std_errD3_V1_18HB = stats.linregress(WD_vect_V1_18HB,BrO_WD_V1_18HB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V1_18HB, p_valueD4_V1_18HB = stats.pearsonr(WS_V1_18HB,BrO_WS_V1_18HB)
#slopeD4_V1_18HB, interceptD4_V1_18HB, rD4_V1_18HB, pD4_V1_18HB, std_errD4_V1_18HB = stats.linregress(WS_V1_18HB,BrO_WS_V1_18HB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V1_18HB, p_valueD5_V1_18HB = stats.pearsonr(Sol_V1_18HB,BrO_V1_18HB)
#slopeD5_V1_18HB, interceptD5_V1_18HB, rD5_V1_18HB, pD5_V1_18HB, std_errD5_V1_18HB = stats.linregress(Sol_V1_18HB,BrO_V1_18HB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V1_18HB, p_valueD6_V1_18HB = stats.pearsonr(Hg0_V1_18HB,BrO_Hg0_V1_18HB)
#slopeD6_V1_18HB, interceptD6_V1_18HB, rD6_V1_18HB, pD6_V1_18HB, std_errD6_V1_18HB = stats.linregress(Hg0_V1_18HB,BrO_Hg0_V1_18HB)
#
## 7) Between SI and BrO
#r_rowD7_V1_18HB, p_valueD7_V1_18HB = stats.pearsonr(SI_SI_V1_18HB,BrO_SI_V1_18HB)
#slopeD7_V1_18HB, interceptD7_V1_18HB, rD7_V1_18HB, pD7_V1_18HB, std_errD7_V1_18HB = stats.linregress(SI_SI_V1_18HB,BrO_SI_V1_18HB)
#
## 8) Between RH and BrO
#r_rowD8_V1_18HB, p_valueD8_V1_18HB = stats.pearsonr(RH_V1_18HB,BrO_RH_V1_18HB)
#slopeD8_V1_18HB, interceptD8_V1_18HB, rD8_V1_18HB, pD8_V1_18HB, std_errD8_V1_18HB = stats.linregress(RH_V1_18HB,BrO_RH_V1_18HB)
#
##--------------------------------
## V2_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V2_18HB, p_valueD1_V2_18HB = stats.pearsonr(O3_V2_18HB,BrO_O3_V2_18HB)
#slopeD1_V2_18HB, interceptD1_V2_18HB, rD1_V2_18HB, pD1_V2_18HB, std_errD1_V2_18HB = stats.linregress(O3_V2_18HB,BrO_O3_V2_18HB)
#
## 2) Between Temp and BrO
#r_rowD2_V2_18HB, p_valueD2_V2_18HB = stats.pearsonr(Temp_V2_18HB,BrO_V2_18HB)
#slopeD2_V2_18HB, interceptD2_V2_18HB, rD2_V2_18HB, pD2_V2_18HB, std_errD2_V2_18HB = stats.linregress(Temp_V2_18HB,BrO_V2_18HB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V2_18HB, p_valueD3_V2_18HB = stats.pearsonr(WD_vect_V2_18HB,BrO_WD_V2_18HB)
#slopeD3_V2_18HB, interceptD3_V2_18HB, rD3_V2_18HB, pD3_V2_18HB, std_errD3_V2_18HB = stats.linregress(WD_vect_V2_18HB,BrO_WD_V2_18HB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V2_18HB, p_valueD4_V2_18HB = stats.pearsonr(WS_V2_18HB,BrO_WS_V2_18HB)
#slopeD4_V2_18HB, interceptD4_V2_18HB, rD4_V2_18HB, pD4_V2_18HB, std_errD4_V2_18HB = stats.linregress(WS_V2_18HB,BrO_WS_V2_18HB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V2_18HB, p_valueD5_V2_18HB = stats.pearsonr(Sol_V2_18HB,BrO_V2_18HB)
#slopeD5_V2_18HB, interceptD5_V2_18HB, rD5_V2_18HB, pD5_V2_18HB, std_errD5_V2_18HB = stats.linregress(Sol_V2_18HB,BrO_V2_18HB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V2_18HB, p_valueD6_V2_18HB = stats.pearsonr(Hg0_V2_18HB,BrO_Hg0_V2_18HB)
#slopeD6_V2_18HB, interceptD6_V2_18HB, rD6_V2_18HB, pD6_V2_18HB, std_errD6_V2_18HB = stats.linregress(Hg0_V2_18HB,BrO_Hg0_V2_18HB)
#
## 7) Between SI and BrO
#r_rowD7_V2_18HB, p_valueD7_V2_18HB = stats.pearsonr(SI_SI_V2_18HB,BrO_SI_V2_18HB)
#slopeD7_V2_18HB, interceptD7_V2_18HB, rD7_V2_18HB, pD7_V2_18HB, std_errD7_V2_18HB = stats.linregress(SI_SI_V2_18HB,BrO_SI_V2_18HB)
#
## 8) Between RH and BrO
#r_rowD8_V2_18HB, p_valueD8_V2_18HB = stats.pearsonr(RH_V2_18HB,BrO_RH_V2_18HB)
#slopeD8_V2_18HB, interceptD8_V2_18HB, rD8_V2_18HB, pD8_V2_18HB, std_errD8_V2_18HB = stats.linregress(RH_V2_18HB,BrO_RH_V2_18HB)
#
##--------------------------------
## V3_18 (2018-19)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V3_18HB, p_valueD1_V3_18HB = stats.pearsonr(O3_V3_18HB,BrO_O3_V3_18HB)
#slopeD1_V3_18HB, interceptD1_V3_18HB, rD1_V3_18HB, pD1_V3_18HB, std_errD1_V3_18HB = stats.linregress(O3_V3_18HB,BrO_O3_V3_18HB)
#
## 2) Between Temp and BrO
#r_rowD2_V3_18HB, p_valueD2_V3_18HB = stats.pearsonr(Temp_V1_18HB,BrO_V1_18HB)
#slopeD2_V3_18HB, interceptD2_V3_18HB, rD2_V3_18HB, pD2_V3_18HB, std_errD2_V3_18HB = stats.linregress(Temp_V3_18HB,BrO_V3_18HB)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V3_18HB, p_valueD3_V3_18HB = stats.pearsonr(WD_vect_V3_18HB,BrO_WD_V3_18HB)
#slopeD3_V3_18HB, interceptD3_V3_18HB, rD3_V3_18HB, pD3_V3_18HB, std_errD3_V3_18HB = stats.linregress(WD_vect_V3_18HB,BrO_WD_V3_18HB)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V3_18HB, p_valueD4_V3_18HB = stats.pearsonr(WS_V3_18HB,BrO_WS_V3_18HB)
#slopeD4_V3_18HB, interceptD4_V3_18HB, rD4_V3_18HB, pD4_V3_18HB, std_errD4_V3_18HB = stats.linregress(WS_V3_18HB,BrO_WS_V3_18HB)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V3_18HB, p_valueD5_V3_18HB = stats.pearsonr(Sol_V3_18HB,BrO_V3_18HB)
#slopeD5_V3_18HB, interceptD5_V3_18HB, rD5_V3_18HB, pD5_V3_18HB, std_errD5_V3_18HB = stats.linregress(Sol_V3_18HB,BrO_V3_18HB)
#
## 6) Between Hg0 and BrO
#r_rowD6_V3_18HB, p_valueD6_V3_18HB = stats.pearsonr(Hg0_V3_18HB,BrO_Hg0_V3_18HB)
#slopeD6_V3_18HB, interceptD6_V3_18HB, rD6_V3_18HB, pD6_V3_18HB, std_errD6_V3_18HB = stats.linregress(Hg0_V3_18HB,BrO_Hg0_V3_18HB)
#
## 7) Between SI and BrO
#r_rowD7_V3_18HB, p_valueD7_V3_18HB = stats.pearsonr(SI_SI_V3_18HB,BrO_SI_V3_18HB)
#slopeD7_V3_18HB, interceptD7_V3_18HB, rD7_V3_18HB, pD7_V3_18HB, std_errD7_V3_18HB = stats.linregress(SI_SI_V3_18HB,BrO_SI_V3_18HB)
#
## 8) Between RH and BrO
#r_rowD8_V3_18HB, p_valueD8_V3_18HB = stats.pearsonr(RH_V3_18HB,BrO_RH_V3_18HB)
#slopeD8_V3_18HB, interceptD8_V3_18HB, rD8_V3_18HB, pD8_V3_18HB, std_errD8_V3_18HB = stats.linregress(RH_V3_18HB,BrO_RH_V3_18HB)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1HB, p_valueD1HB = stats.pearsonr(O3HB,BrO_O3HB)
slopeD1HB, interceptD1HB, rD1HB, pD1HB, std_errD1HB = stats.linregress(O3HB,BrO_O3HB)

# 2) Between Temp and BrO
r_rowD2HB, p_valueD2HB = stats.pearsonr(TempHB,BrOHB)
slopeD2HB, interceptD2HB, rD2HB, pD2HB, std_errD2HB = stats.linregress(TempHB,BrOHB)

# 3) Between Wind Direction and BrO
r_rowD3HB, p_valueD3HB = stats.pearsonr(WD_vectHB,BrO_WDHB)
slopeD3HB, interceptD3HB, rD3HB, pD3HB, std_errD3HB = stats.linregress(WD_vectHB,BrO_WDHB)

# 4) Between Wind Speed and BrO
r_rowD4HB, p_valueD4HB = stats.pearsonr(WSHB,BrO_WSHB)
slopeD4HB, interceptD4HB, rD4HB, pD4HB, std_errD4HB = stats.linregress(WSHB,BrO_WSHB)

# 5) Between Solar Radiation and BrO
r_rowD5HB, p_valueD5HB = stats.pearsonr(SolHB,BrOHB)
slopeD5HB, interceptD5HB, rD5HB, pD5HB, std_errD5HB = stats.linregress(SolHB,BrOHB)

# 6) Between Hg0 and BrO
r_rowD6HB, p_valueD6HB = stats.pearsonr(Hg0HB,BrO_Hg0HB)
slopeD6HB, interceptD6HB, rD6HB, pD6HB, std_errD6HB = stats.linregress(Hg0HB,BrO_Hg0HB)

# 7) Between SI and BrO
r_rowD7HB, p_valueD7HB = stats.pearsonr(SI_SIHB,BrO_SIHB)
slopeD7HB, interceptD7HB, rD7HB, pD7HB, std_errD7HB = stats.linregress(SI_SIHB,BrO_SIHB)

# 8) Between SI and BrO
r_rowD8HB, p_valueD8HB = stats.pearsonr(RHHB,BrO_RHHB)
slopeD8HB, interceptD8HB, rD8HB, pD8HB, std_errD8HB = stats.linregress(RHHB,BrO_RHHB)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs O3)

fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 1
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_V1_17LS,   BrO_O3_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(O3_V2_17LS,   BrO_O3_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(O3_V3_17LS,   BrO_O3_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(O3_V1_18LS,   BrO_O3_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(O3_V2_18LS,   BrO_O3_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(O3_V3_18LS,   BrO_O3_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(O3LS, interceptD1LS + slopeD1LS * O3LS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1LS))+" $\pm$"+str("%7.4f"%(std_errD1LS))+" pptv, r: "+str("%7.4f"%(rD1LS))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 1
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_V1_17LB,   BrO_O3_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(O3_V2_17LB,   BrO_O3_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(O3_V3_17LB,   BrO_O3_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(O3_V1_18LB,   BrO_O3_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(O3_V2_18LB,   BrO_O3_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(O3_V3_18LB,   BrO_O3_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(O3LB, interceptD1LB + slopeD1LB * O3LB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1LB))+" $\pm$"+str("%7.4f"%(std_errD1LB))+" pptv, r: "+str("%7.4f"%(rD1LB))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 1
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_V1_17HS,   BrO_O3_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(O3_V2_17HS,   BrO_O3_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(O3_V3_17HS,   BrO_O3_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(O3_V1_18HS,   BrO_O3_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(O3_V2_18HS,   BrO_O3_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(O3_V3_18HS,   BrO_O3_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(O3HS, interceptD1HS + slopeD1HS * O3HS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1HS))+" $\pm$"+str("%7.4f"%(std_errD1HS))+" pptv, r: "+str("%7.4f"%(rD1HS))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 1
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_V1_17HB,   BrO_O3_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(O3_V2_17HB,   BrO_O3_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(O3_V3_17HB,   BrO_O3_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(O3_V1_18HB,   BrO_O3_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(O3_V2_18HB,   BrO_O3_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(O3_V3_18HB,   BrO_O3_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(O3HB, interceptD1HB + slopeD1HB * O3HB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1HB))+" $\pm$"+str("%7.4f"%(std_errD1HB))+" pptv, r: "+str("%7.4f"%(rD1HB))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Temperature)

fig2 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 2
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_V1_17LS,   BrO_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Temp_V2_17LS,   BrO_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Temp_V3_17LS,   BrO_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Temp_V1_18LS,   BrO_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Temp_V2_18LS,   BrO_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Temp_V3_18LS,   BrO_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(TempLS, interceptD2LS + slopeD2LS * TempLS, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2LS))+" $\pm$"+str("%7.4f"%(std_errD2LS))+" $^\circ$C, r: "+str("%7.4f"%(rD2LS))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 2
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_V1_17LB,   BrO_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Temp_V2_17LB,   BrO_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Temp_V3_17LB,   BrO_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Temp_V1_18LB,   BrO_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Temp_V2_18LB,   BrO_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Temp_V3_18LB,   BrO_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(TempLB, interceptD2LB + slopeD2LB * TempLB, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2LB))+" $\pm$"+str("%7.4f"%(std_errD2LB))+" $^\circ$C, r: "+str("%7.4f"%(rD2LB))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 2
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_V1_17HS,   BrO_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Temp_V2_17HS,   BrO_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Temp_V3_17HS,   BrO_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Temp_V1_18HS,   BrO_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Temp_V2_18HS,   BrO_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Temp_V3_18HS,   BrO_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(TempHS, interceptD2HS + slopeD2HS * TempHS, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2HS))+" $\pm$"+str("%7.4f"%(std_errD2HS))+" $^\circ$C, r: "+str("%7.4f"%(rD2HS))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 2
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_V1_17HB,   BrO_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Temp_V2_17HB,   BrO_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Temp_V3_17HB,   BrO_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Temp_V1_18HB,   BrO_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Temp_V2_18HB,   BrO_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Temp_V3_18HB,   BrO_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(TempHB, interceptD2HB + slopeD2HB * TempHB, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2HB))+" $\pm$"+str("%7.4f"%(std_errD2HB))+" $^\circ$C, r: "+str("%7.4f"%(rD2HB))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Direction)

fig3 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 3
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_V1_17LS,   BrO_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(WD_vect_V2_17LS,   BrO_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WD_vect_V3_17LS,   BrO_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WD_vect_V1_18LS,   BrO_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WD_vect_V2_18LS,   BrO_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WD_vect_V3_18LS,   BrO_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WD_vectLS, interceptD3LS + slopeD3LS * WD_vectLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3LS))+" $\pm$"+str("%7.4f"%(std_errD3LS))+" $^\circ$, r: "+str("%7.4f"%(rD3LS))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 3
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_V1_17LB,   BrO_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(WD_vect_V2_17LB,   BrO_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WD_vect_V3_17LB,   BrO_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WD_vect_V1_18LB,   BrO_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WD_vect_V2_18LB,   BrO_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WD_vect_V3_18LB,   BrO_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WD_vectLB, interceptD3LB + slopeD3LB * WD_vectLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3LB))+" $\pm$"+str("%7.4f"%(std_errD3LB))+" $^\circ$, r: "+str("%7.4f"%(rD3LB))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 3
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_V1_17HS,   BrO_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(WD_vect_V2_17HS,   BrO_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WD_vect_V3_17HS,   BrO_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WD_vect_V1_18HS,   BrO_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WD_vect_V2_18HS,   BrO_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WD_vect_V3_18HS,   BrO_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WD_vectHS, interceptD3HS + slopeD3HS * WD_vectHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3HS))+" $\pm$"+str("%7.4f"%(std_errD3HS))+" $^\circ$, r: "+str("%7.4f"%(rD3HS))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#-----------------------------------
# Graph 3
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_V1_17HB,   BrO_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(WD_vect_V2_17HB,   BrO_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WD_vect_V3_17HB,   BrO_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WD_vect_V1_18HB,   BrO_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WD_vect_V2_18HB,   BrO_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WD_vect_V3_18HB,   BrO_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WD_vectHB, interceptD3HB + slopeD3HB * WD_vectHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3HB))+" $\pm$"+str("%7.4f"%(std_errD3HB))+" $^\circ$, r: "+str("%7.4f"%(rD3HB))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Speed)

fig4 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 4
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_V1_17LS,   BrO_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(WS_V2_17LS,   BrO_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WS_V3_17LS,   BrO_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WS_V1_18LS,   BrO_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WS_V2_18LS,   BrO_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WS_V3_18LS,   BrO_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WSLS, interceptD4LS + slopeD4LS * WSLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4LS))+" $\pm$"+str("%7.4f"%(std_errD4LS))+" m/s, r: "+str("%7.4f"%(rD4LS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 4
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_V1_17LB,   BrO_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(WS_V2_17LB,   BrO_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WS_V3_17LB,   BrO_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WS_V1_18LB,   BrO_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WS_V2_18LB,   BrO_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WS_V3_18LB,   BrO_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WSLB, interceptD4LB + slopeD4LB * WSLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4LB))+" $\pm$"+str("%7.4f"%(std_errD4LB))+" m/s, r: "+str("%7.4f"%(rD4LB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 4
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_V1_17HS,   BrO_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(WS_V2_17HS,   BrO_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WS_V3_17HS,   BrO_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WS_V1_18HS,   BrO_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WS_V2_18HS,   BrO_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WS_V3_18HS,   BrO_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WSHS, interceptD4HS + slopeD4HS * WSHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4HS))+" $\pm$"+str("%7.4f"%(std_errD4HS))+" m/s, r: "+str("%7.4f"%(rD4HS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 4
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_V1_17HB,   BrO_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(WS_V2_17HB,   BrO_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WS_V3_17HB,   BrO_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WS_V1_18HB,   BrO_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WS_V2_18HB,   BrO_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WS_V3_18HB,   BrO_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(WSHB, interceptD4HB + slopeD4HB * WSHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4HB))+" $\pm$"+str("%7.4f"%(std_errD4HB))+" m/s, r: "+str("%7.4f"%(rD4HB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Solar Radiation)

fig5 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 5
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_V1_17LS,   BrO_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Sol_V2_17LS,   BrO_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Sol_V3_17LS,   BrO_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Sol_V1_18LS,   BrO_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Sol_V2_18LS,   BrO_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Sol_V3_18LS,   BrO_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(SolLS, interceptD5LS + slopeD5LS * SolLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5LS))+" $\pm$"+str("%7.4f"%(std_errD5LS))+" W/m$^2$, r: "+str("%7.4f"%(rD5LS))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 5
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_V1_17LB,   BrO_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Sol_V2_17LB,   BrO_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Sol_V3_17LB,   BrO_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Sol_V1_18LB,   BrO_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Sol_V2_18LB,   BrO_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Sol_V3_18LB,   BrO_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(SolLB, interceptD5LB + slopeD5LB * SolLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5LB))+" $\pm$"+str("%7.4f"%(std_errD5LB))+" W/m$^2$, r: "+str("%7.4f"%(rD5LB))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 5
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_V1_17HS,   BrO_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Sol_V2_17HS,   BrO_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Sol_V3_17HS,   BrO_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Sol_V1_18HS,   BrO_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Sol_V2_18HS,   BrO_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Sol_V3_18HS,   BrO_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(SolHS, interceptD5HS + slopeD5HS * SolHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5HS))+" $\pm$"+str("%7.4f"%(std_errD5HS))+" W/m$^2$, r: "+str("%7.4f"%(rD5HS))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 5
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_V1_17HB,   BrO_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Sol_V2_17HB,   BrO_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Sol_V3_17HB,   BrO_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Sol_V1_18HB,   BrO_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Sol_V2_18HB,   BrO_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Sol_V3_18HB,   BrO_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(SolHB, interceptD5HB + slopeD5HB * SolHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5HB))+" $\pm$"+str("%7.4f"%(std_errD5HB))+" W/m$^2$, r: "+str("%7.4f"%(rD5HB))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Hg0)

fig6 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 6
ax = plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_V1_17LS,   BrO_Hg0_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Hg0_V2_17LS,   BrO_Hg0_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Hg0_V3_17LS,   BrO_Hg0_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Hg0_V1_18LS,   BrO_Hg0_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Hg0_V2_18LS,   BrO_Hg0_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Hg0_V3_18LS,   BrO_Hg0_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(Hg0LS, interceptD6LS + slopeD6LS * Hg0LS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6LS))+" $\pm$ "+str("%7.4f"%(std_errD6LS))+" ng/m$^2$, r: "+str("%7.4f"%(rD6LS))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 6
ax = plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_V1_17LB,   BrO_Hg0_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Hg0_V2_17LB,   BrO_Hg0_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Hg0_V3_17LB,   BrO_Hg0_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Hg0_V1_18LB,   BrO_Hg0_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Hg0_V2_18LB,   BrO_Hg0_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Hg0_V3_18LB,   BrO_Hg0_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(Hg0LB, interceptD6LB + slopeD6LB * Hg0LB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6LB))+" $\pm$ "+str("%7.4f"%(std_errD6LB))+" ng/m$^2$, r: "+str("%7.4f"%(rD6LB))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 6
ax = plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_V1_17HS,   BrO_Hg0_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Hg0_V2_17HS,   BrO_Hg0_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Hg0_V3_17HS,   BrO_Hg0_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Hg0_V1_18HS,   BrO_Hg0_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Hg0_V2_18HS,   BrO_Hg0_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Hg0_V3_18HS,   BrO_Hg0_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(Hg0HS, interceptD6HS + slopeD6HS * Hg0HS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6HS))+" $\pm$ "+str("%7.4f"%(std_errD6HS))+" ng/m$^2$, r: "+str("%7.4f"%(rD6HS))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 6
ax = plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_V1_17HB,   BrO_Hg0_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Hg0_V2_17HB,   BrO_Hg0_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Hg0_V3_17HB,   BrO_Hg0_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Hg0_V1_18HB,   BrO_Hg0_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Hg0_V2_18HB,   BrO_Hg0_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Hg0_V3_18HB,   BrO_Hg0_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(Hg0HB, interceptD6HB + slopeD6HB * Hg0HB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6HB))+" $\pm$ "+str("%7.4f"%(std_errD6HB))+" ng/m$^2$, r: "+str("%7.4f"%(rD6HB))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Sea Ice)

fig7 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 7
ax = plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_V1_17LS,   BrO_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(SI_V2_17LS,   BrO_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(SI_V3_17LS,   BrO_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(SI_V1_18LS,   BrO_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(SI_V2_18LS,   BrO_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(SI_V3_18LS,   BrO_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(SILS, interceptD7LS + slopeD7LS * SILS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7LS))+" $\pm$"+str("%7.4f"%(std_errD7LS))+" %, r: "+str("%7.4f"%(rD7LS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 7
ax = plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_V1_17LB,   BrO_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(SI_V2_17LB,   BrO_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(SI_V3_17LB,   BrO_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(SI_V1_18LB,   BrO_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(SI_V2_18LB,   BrO_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(SI_V3_18LB,   BrO_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(SILB, interceptD7LB + slopeD7LB * SILB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7LB))+" $\pm$"+str("%7.4f"%(std_errD7LB))+" %, r: "+str("%7.4f"%(rD7LB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 7
ax = plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_V1_17HS,   BrO_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(SI_V2_17HS,   BrO_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(SI_V3_17HS,   BrO_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(SI_V1_18HS,   BrO_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(SI_V2_18HS,   BrO_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(SI_V3_18HS,   BrO_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(SIHS, interceptD7HS + slopeD7HS * SIHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7HS))+" $\pm$"+str("%7.4f"%(std_errD7HS))+" %, r: "+str("%7.4f"%(rD7HS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 7
ax = plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_V1_17HB,   BrO_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(SI_V2_17HB,   BrO_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(SI_V3_17HB,   BrO_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(SI_V1_18HB,   BrO_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(SI_V2_18HB,   BrO_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(SI_V3_18HB,   BrO_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(SIHB, interceptD7HB + slopeD7HB * SIHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7HB))+" $\pm$"+str("%7.4f"%(std_errD7HB))+" %, r: "+str("%7.4f"%(rD7HB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Relative Humidity)

fig8 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 8
ax = plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_V1_17LS,   BrO_RH_V1_17LS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(RH_V2_17LS,   BrO_RH_V2_17LS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(RH_V3_17LS,   BrO_RH_V3_17LS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(RH_V1_18LS,   BrO_RH_V1_18LS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(RH_V2_18LS,   BrO_RH_V2_18LS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(RH_V3_18LS,   BrO_RH_V3_18LS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(RHLS, interceptD8LS + slopeD8LS * RHLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8LS))+" $\pm$"+str("%7.4f"%(std_errD8LS))+" %, r: "+str("%7.4f"%(rD8LS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#-----------------------------------
# Graph 8
ax = plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_V1_17LB,   BrO_RH_V1_17LB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(RH_V2_17LB,   BrO_RH_V2_17LB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(RH_V3_17LB,   BrO_RH_V3_17LB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(RH_V1_18LB,   BrO_RH_V1_18LB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(RH_V2_18LB,   BrO_RH_V2_18LB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(RH_V3_18LB,   BrO_RH_V3_18LB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(RHLB, interceptD8LB + slopeD8LB * RHLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8LB))+" $\pm$"+str("%7.4f"%(std_errD8LB))+" %, r: "+str("%7.4f"%(rD8LB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 8
ax = plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_V1_17HS,   BrO_RH_V1_17HS,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(RH_V2_17HS,   BrO_RH_V2_17HS,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(RH_V3_17HS,   BrO_RH_V3_17HS,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(RH_V1_18HS,   BrO_RH_V1_18HS,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(RH_V2_18HS,   BrO_RH_V2_18HS,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(RH_V3_18HS,   BrO_RH_V3_18HS,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(RHHS, interceptD8HS + slopeD8HS * RHHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8HS))+" $\pm$"+str("%7.4f"%(std_errD8HS))+" %, r: "+str("%7.4f"%(rD8HS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)


#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 8
ax = plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_V1_17HB,   BrO_RH_V1_17HB,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(RH_V2_17HB,   BrO_RH_V2_17HB,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(RH_V3_17HB,   BrO_RH_V3_17HB,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(RH_V1_18HB,   BrO_RH_V1_18HB,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(RH_V2_18HB,   BrO_RH_V2_18HB,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(RH_V3_18HB,   BrO_RH_V3_18HB,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')

# Plot the regression line
line6, = plt.plot(RHHB, interceptD8HB + slopeD8HB * RHHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8HB))+" $\pm$"+str("%7.4f"%(std_errD8HB))+" %, r: "+str("%7.4f"%(rD8HB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)
