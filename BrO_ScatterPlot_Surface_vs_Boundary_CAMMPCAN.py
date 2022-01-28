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
V1_17_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2017/18)
V1_17_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/BrO_error/V1_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2017/18)
V1_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv')

# V2_17 (2017-18)
V2_17_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V2 (2017/18)
V2_17_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/BrO_error/V2_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V2 (2017/18)
V2_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv')

# V3_17 (2017-18)
V3_17_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V3 (2017/18)
V3_17_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/BrO_error/V3_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V3 (2017/18)
V3_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv')

# V1_18 (2018-19)
V1_18_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)
V1_18_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/BrO_error/V1_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2018/19)
V1_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv')

# V2_18 (2018-19)
V2_18_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V2 (2018/19)
V2_18_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/BrO_error/V2_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V2 (2018/19)
V2_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv')

# V3_18 (2018-19)
V3_18_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V3 (2018/19)
V3_18_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/BrO_error/V3_18_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V3 (2018/19)
V3_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv')

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
V1_17_VMR.columns       = (pd.to_datetime(V1_17_VMR.columns, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
V1_17_Met['DateTime']   = pd.to_datetime(V1_17_Met['DateTime'], dayfirst=True)

# V2_17 (2017-18)
V2_17_VMR.columns       = (pd.to_datetime(V2_17_VMR.columns, dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
V2_17_Met['DateTime']   = pd.to_datetime(V2_17_Met['DateTime'], dayfirst=True)

# V3_17 (2017-18)
V3_17_VMR.columns       = (pd.to_datetime(V3_17_VMR.columns, dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
V3_17_Met['DateTime']   = pd.to_datetime(V3_17_Met['DateTime'], dayfirst=True)

# V1_18 (2018-19)
V1_18_VMR.columns       = (pd.to_datetime(V1_18_VMR.columns, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
V1_18_Met['DateTime']   = pd.to_datetime(V1_18_Met['DateTime'], dayfirst=True)

# V2_18 (2018-19)
V2_18_VMR.columns       = (pd.to_datetime(V2_18_VMR.columns, dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
V2_18_Met['DateTime']   = pd.to_datetime(V2_18_Met['DateTime'], dayfirst=True)

# V3_18 (2018-19)
V3_18_VMR.columns       = (pd.to_datetime(V3_18_VMR.columns, dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
V3_18_Met['DateTime']   = pd.to_datetime(V3_18_Met['DateTime'], dayfirst=True)

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

V1_17_Met   = V1_17_Met.set_index('DateTime')
V2_17_Met   = V2_17_Met.set_index('DateTime')
V3_17_Met   = V3_17_Met.set_index('DateTime')
V1_18_Met   = V1_18_Met.set_index('DateTime')
V2_18_Met   = V2_18_Met.set_index('DateTime')
V3_18_Met   = V3_18_Met.set_index('DateTime')

#------------------------------------------------------------------------------
# Resample all data to 20 min averages

V1_17_Met   = V1_17_Met.resample('20T').mean()
V2_17_Met   = V2_17_Met.resample('20T').mean()
V3_17_Met   = V3_17_Met.resample('20T').mean()
V1_18_Met   = V1_18_Met.resample('20T').mean()
V2_18_Met   = V2_18_Met.resample('20T').mean()
V3_18_Met   = V3_18_Met.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

V1_17_Met.index   = V1_17_Met.index   - pd.Timedelta(minutes=10)
V2_17_Met.index   = V2_17_Met.index   - pd.Timedelta(minutes=10)
V3_17_Met.index   = V3_17_Met.index   - pd.Timedelta(minutes=10)
V1_18_Met.index   = V1_18_Met.index   - pd.Timedelta(minutes=10)
V2_18_Met.index   = V2_18_Met.index   - pd.Timedelta(minutes=10)
V3_18_Met.index   = V3_18_Met.index   - pd.Timedelta(minutes=10)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

#-----------------------
# V1_17 (07:00 to 18:00)
#-----------------------

start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V1_17TT['Time'] >= start_time) & (V1_17TT['Time'] < end_time)
V1_17M     = V1_17TT[Midday_VMR]

#-----------------------
# V2_17 (07:00 to 18:00)
#-----------------------

start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V2_17TT['Time'] >= start_time) & (V2_17TT['Time'] < end_time)
V2_17M     = V2_17TT[Midday_VMR]

#-----------------------
# V3_17 (07:00 to 18:00)
#-----------------------

start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V3_17TT['Time'] >= start_time) & (V3_17TT['Time'] < end_time)
V3_17M     = V3_17TT[Midday_VMR]

#-----------------------
# V1_18 (07:00 to 18:00)
#-----------------------

start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V1_18TT['Time'] >= start_time) & (V1_18TT['Time'] < end_time)
V1_18M     = V1_18TT[Midday_VMR]

#-----------------------
# V2_18 (07:00 to 18:00)
#-----------------------

start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V2_18TT['Time'] >= start_time) & (V2_18TT['Time'] < end_time)
V2_18M     = V2_18TT[Midday_VMR]

#-----------------------
# V3_18 (07:00 to 18:00)
#-----------------------

start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V3_18TT['Time'] >= start_time) & (V3_18TT['Time'] < end_time)
V3_18M     = V3_18TT[Midday_VMR]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# V1_17 Davis (14-22 Nov 2017)
start_date   = '2017-11-14'
end_date     = '2017-11-23'

Davis_VMR    = (V1_17M.index >= start_date) & (V1_17M.index < end_date)
V1_17M       = V1_17M[Davis_VMR]

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1  = '2017-12-21'
end_date1    = '2017-12-23'
start_date2  = '2017-12-26'
end_date2    = '2018-01-6'

Casey1_VMR       = (V2_17M.index >= start_date1) & (V2_17M.index < end_date1)
Casey2_VMR       = (V2_17M.index >= start_date2) & (V2_17M.index < end_date2)
V2_17_Casey1_VMR = V2_17M[Casey1_VMR]
V2_17_Casey2_VMR = V2_17M[Casey2_VMR]
V2_17M           = pd.concat([V2_17_Casey1_VMR,V2_17_Casey2_VMR], axis =0)

# V3_17 Mawson (1-17 Feb 2018)
start_date   = '2018-02-01'
end_date     = '2018-02-18'

Mawson_VMR   = (V3_17M.index >= start_date) & (V3_17M.index < end_date)
V3_17M       = V3_17M[Mawson_VMR]

# V1_18 Davis (7-15 Nov 2018)
start_date   = '2018-11-07'
end_date     = '2018-11-16'

Davis_VMR    = (V1_18M.index >= start_date) & (V1_18M.index < end_date)
V1_18M       = V1_18M[Davis_VMR]

# V2_18 Casey (15-30 Dec 2018)
start_date   = '2018-12-15'
end_date     = '2018-12-31'

Casey_VMR    = (V2_18M.index >= start_date) & (V2_18M.index < end_date)
V2_18M       = V2_18M[Casey_VMR]

# V3_18 Mawson (30 Jan - 9 Feb 2019)
start_date   = '2019-01-30'
end_date     = '2019-02-10'

Mawson_VMR   = (V3_18M.index >= start_date) & (V3_18M.index < end_date)
V3_18M       = V3_18M[Mawson_VMR]

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

# V1_17 (2017-18)
D1_V1_17   = pd.merge(left=V1_17M,    right=V1_17_Met,    how='left', left_index=True, right_index=True)

# V2_17 (2017-18)
D1_V2_17   = pd.merge(left=V2_17M,     right=V2_17_Met,   how='left', left_index=True, right_index=True)

# V3_17 (2017-18)
D1_V3_17   = pd.merge(left=V3_17M,     right=V3_17_Met,   how='left', left_index=True, right_index=True)

# V1_18 (2018-19)
D1_V1_18   = pd.merge(left=V1_18M,     right=V1_18_Met,   how='left', left_index=True, right_index=True)

# V2_18 (2018-19)
D1_V2_18   = pd.merge(left=V2_18M,     right=V2_18_Met,   how='left', left_index=True, right_index=True)

# V3_18 (2018-19)
D1_V3_18   = pd.merge(left=V3_18M,     right=V3_18_Met,   how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Calculate the Wind Speed average

WS_s_V1_17           = np.array(D1_V1_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17           = np.array(D1_V1_17['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D1_V1_17['WS_Avg']   = (WS_s_V1_17 + WS_p_V1_17)/2 # Average the wind speed for port and starboard

WS_s_V2_17           = np.array(D1_V2_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17           = np.array(D1_V2_17['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D1_V2_17['WS_Avg']   = (WS_s_V2_17 + WS_p_V2_17)/2 # Average the wind speed for port and starboard

WS_s_V3_17           = np.array(D1_V3_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17           = np.array(D1_V3_17['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D1_V3_17['WS_Avg']   = (WS_s_V3_17 + WS_p_V3_17)/2 # Average the wind speed for port and starboard

WS_s_V1_18           = np.array(D1_V1_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18           = np.array(D1_V1_18['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D1_V1_18['WS_Avg']   = (WS_s_V1_18 + WS_p_V1_18)/2 # Average the wind speed for port and starboard

WS_s_V2_18           = np.array(D1_V2_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18           = np.array(D1_V2_18['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D1_V2_18['WS_Avg']   = (WS_s_V2_18 + WS_p_V2_18)/2 # Average the wind speed for port and starboard

WS_s_V3_18           = np.array(D1_V3_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18           = np.array(D1_V3_18['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D1_V3_18['WS_Avg']   = (WS_s_V3_18 + WS_p_V3_18)/2 # Average the wind speed for port and starboard

#------------------------------------------------------------------------------
# Seperate the data into low (<=7 m/s) and high (>7 m/s) wind speeds

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
V1_17_LWS   = (D1_V1_17['WS_Avg'] <= 7)
D1_V1_17L   = D1_V1_17[V1_17_LWS]

V2_17_LWS   = (D1_V2_17['WS_Avg'] <= 7)
D1_V2_17L   = D1_V2_17[V2_17_LWS]

V3_17_LWS   = (D1_V3_17['WS_Avg'] <= 7)
D1_V3_17L   = D1_V3_17[V3_17_LWS]

V1_18_LWS   = (D1_V1_18['WS_Avg'] <= 7)
D1_V1_18L   = D1_V1_18[V1_18_LWS]

V2_18_LWS   = (D1_V2_18['WS_Avg'] <= 7)
D1_V2_18L   = D1_V2_18[V2_18_LWS]

V3_18_LWS   = (D1_V3_18['WS_Avg'] <= 7)
D1_V3_18L   = D1_V3_18[V3_18_LWS]

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
V1_17_HWS   = (D1_V1_17['WS_Avg'] > 7)
D1_V1_17H   = D1_V1_17[V1_17_HWS]

V2_17_HWS   = (D1_V2_17['WS_Avg'] > 7)
D1_V2_17H   = D1_V2_17[V2_17_HWS]

V3_17_HWS   = (D1_V3_17['WS_Avg'] > 7)
D1_V3_17H   = D1_V3_17[V3_17_HWS]

V1_18_HWS   = (D1_V1_18['WS_Avg'] > 7)
D1_V1_18H   = D1_V1_18[V1_18_HWS]

V2_18_HWS   = (D1_V2_18['WS_Avg'] > 7)
D1_V2_18H   = D1_V2_18[V2_18_HWS]

V3_18_HWS   = (D1_V3_18['WS_Avg'] > 7)
D1_V3_18H   = D1_V3_18[V3_18_HWS]

#------------------------------------------------------------------------------
# Define the variables

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# Surface Layer
BrO_V1_17LS   = np.array(D1_V1_17L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17LS   = np.array(D1_V2_17L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17LS   = np.array(D1_V3_17L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18LS   = np.array(D1_V1_18L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18LS   = np.array(D1_V2_18L[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18LS   = np.array(D1_V3_18L[0.1])   * 1e6 # convert from ppmv to ppbv

# Boundary Layer
BrO_V1_17LB   = np.array(D1_V1_17L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17LB   = np.array(D1_V2_17L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17LB   = np.array(D1_V3_17L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18LB   = np.array(D1_V1_18L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18LB   = np.array(D1_V2_18L[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18LB   = np.array(D1_V3_18L[0.3])   * 1e6 # convert from ppmv to ppbv

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# Surface Layer 
BrO_V1_17HS   = np.array(D1_V1_17H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17HS   = np.array(D1_V2_17H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17HS   = np.array(D1_V3_17H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18HS   = np.array(D1_V1_18H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18HS   = np.array(D1_V2_18H[0.1])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18HS   = np.array(D1_V3_18H[0.1])   * 1e6 # convert from ppmv to ppbv

# Boundary Layer 
BrO_V1_17HB   = np.array(D1_V1_17H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17HB   = np.array(D1_V2_17H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17HB   = np.array(D1_V3_17H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18HB   = np.array(D1_V1_18H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18HB   = np.array(D1_V2_18H[0.3])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18HB   = np.array(D1_V3_18H[0.3])   * 1e6 # convert from ppmv to ppbv

#------------------------------------------------------------------------------
# Concate the variables from each voyage

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOLS = np.concatenate((BrO_V1_17LS, BrO_V2_17LS, BrO_V3_17LS, BrO_V1_18LS, BrO_V2_18LS, BrO_V3_18LS), axis=0)

# BrO boundary volume mixing ratio (VMR)
BrOLB = np.concatenate((BrO_V1_17LB, BrO_V2_17LB, BrO_V3_17LB, BrO_V1_18LB, BrO_V2_18LB, BrO_V3_18LB), axis=0)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOHS = np.concatenate((BrO_V1_17HS, BrO_V2_17HS, BrO_V3_17HS, BrO_V1_18HS, BrO_V2_18HS, BrO_V3_18HS), axis=0)

# BrO boundary volume mixing ratio (VMR)
BrOHB = np.concatenate((BrO_V1_17HB, BrO_V2_17HB, BrO_V3_17HB, BrO_V1_18HB, BrO_V2_18HB, BrO_V3_18HB), axis=0)

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# Low Wind Speed (<=7 m/s)
#------------------------------------
#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (BrO Surface) 
V1_17_Y1maskLS = np.isfinite(BrO_V1_17LS) # Scan for NaN values
BrO_V1_17LS    = BrO_V1_17LS[V1_17_Y1maskLS] # BrO HWS Surface
BrO_V1_17LB    = BrO_V1_17LB[V1_17_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V1_17_Y1maskLB = np.isfinite(BrO_V1_17LB) # Scan for NaN values
BrO_V1_17LS    = BrO_V1_17LS[V1_17_Y1maskLB] # BrO HWS Surface
BrO_V1_17LB    = BrO_V1_17LB[V1_17_Y1maskLB] # BrO HWS Boundary

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (BrO Surface) 
V2_17_Y1maskLS = np.isfinite(BrO_V2_17LS) # Scan for NaN values
BrO_V2_17LS    = BrO_V2_17LS[V2_17_Y1maskLS] # BrO HWS Surface
BrO_V2_17LB    = BrO_V2_17LB[V2_17_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V2_17_Y1maskLB = np.isfinite(BrO_V2_17LB) # Scan for NaN values
BrO_V2_17LS    = BrO_V2_17LS[V2_17_Y1maskLB] # BrO HWS Surface
BrO_V2_17LB    = BrO_V2_17LB[V2_17_Y1maskLB] # BrO HWS Boundary

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (BrO Surface) 
V3_17_Y1maskLS = np.isfinite(BrO_V3_17LS) # Scan for NaN values
BrO_V3_17LS    = BrO_V3_17LS[V3_17_Y1maskLS] # BrO HWS Surface
BrO_V3_17LB    = BrO_V3_17LB[V3_17_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V3_17_Y1maskLB = np.isfinite(BrO_V3_17LB) # Scan for NaN values
BrO_V3_17LS    = BrO_V3_17LS[V3_17_Y1maskLB] # BrO HWS Surface
BrO_V3_17LB    = BrO_V3_17LB[V3_17_Y1maskLB] # BrO HWS Boundary

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (BrO Surface)
V1_18_Y1maskLS = np.isfinite(BrO_V1_18LS) # Scan for NaN values
BrO_V1_18LS    = BrO_V1_18LS[V1_18_Y1maskLS] # BrO HWS Surface
BrO_V1_18LB    = BrO_V1_18LB[V1_18_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary)
V1_18_Y1maskLB = np.isfinite(BrO_V1_18LB) # Scan for NaN values
BrO_V1_18LS    = BrO_V1_18LS[V1_18_Y1maskLB] # BrO HWS Surface
BrO_V1_18LB    = BrO_V1_18LB[V1_18_Y1maskLB] # BrO HWS Boundary

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (BrO Surface) 
V2_18_Y1maskLS = np.isfinite(BrO_V2_18LS) # Scan for NaN values
BrO_V2_18LS    = BrO_V2_18LS[V2_18_Y1maskLS] # BrO HWS Surface
BrO_V2_18LB    = BrO_V2_18LB[V2_18_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V2_18_Y1maskLB = np.isfinite(BrO_V2_18LB) # Scan for NaN values
BrO_V2_18LS    = BrO_V2_18LS[V2_18_Y1maskLB] # BrO HWS Surface
BrO_V2_18LB    = BrO_V2_18LB[V2_18_Y1maskLB] # BrO HWS Boundary

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (BrO Surface) 
V3_18_Y1maskLS = np.isfinite(BrO_V3_18LS) # Scan for NaN values
BrO_V3_18LS    = BrO_V3_18LS[V3_18_Y1maskLS] # BrO HWS Surface
BrO_V3_18LB    = BrO_V3_18LB[V3_18_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V3_18_Y1maskLB = np.isfinite(BrO_V3_18LB) # Scan for NaN values
BrO_V3_18LS    = BrO_V3_18LS[V3_18_Y1maskLB] # BrO HWS Surface
BrO_V3_18LB    = BrO_V3_18LB[V3_18_Y1maskLB] # BrO HWS Boundary

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO Surface) 
ALL_Y1maskLS   = np.isfinite(BrOLS) # Scan for NaN values
BrOLS          = BrOLS[ALL_Y1maskLS] # BrO HWS Surface
BrOLB          = BrOLB[ALL_Y1maskLS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
ALL_Y1maskLB   = np.isfinite(BrOLB) # Scan for NaN values
BrOLS          = BrOLS[ALL_Y1maskLB] # BrO HWS Surface
BrOLB          = BrOLB[ALL_Y1maskLB] # BrO HWS Boundary

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# High Wind Speed (>7 m/s)
#------------------------------------
#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (BrO Surface) 
V1_17_Y1maskHS = np.isfinite(BrO_V1_17HS) # Scan for NaN values
BrO_V1_17HS    = BrO_V1_17HS[V1_17_Y1maskHS] # BrO HWS Surface
BrO_V1_17HB    = BrO_V1_17HB[V1_17_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V1_17_Y1maskHB = np.isfinite(BrO_V1_17HB) # Scan for NaN values
BrO_V1_17HS    = BrO_V1_17HS[V1_17_Y1maskHB] # BrO HWS Surface
BrO_V1_17HB    = BrO_V1_17HB[V1_17_Y1maskHB] # BrO HWS Boundary

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (BrO Surface) 
V2_17_Y1maskHS = np.isfinite(BrO_V2_17HS) # Scan for NaN values
BrO_V2_17HS    = BrO_V2_17HS[V2_17_Y1maskHS] # BrO HWS Surface
BrO_V2_17HB    = BrO_V2_17HB[V2_17_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V2_17_Y1maskHB = np.isfinite(BrO_V2_17HB) # Scan for NaN values
BrO_V2_17HS    = BrO_V2_17HS[V2_17_Y1maskHB] # BrO HWS Surface
BrO_V2_17HB    = BrO_V2_17HB[V2_17_Y1maskHB] # BrO HWS Boundary

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (BrO Surface) 
V3_17_Y1maskHS = np.isfinite(BrO_V3_17HS) # Scan for NaN values
BrO_V3_17HS    = BrO_V3_17HS[V3_17_Y1maskHS] # BrO HWS Surface
BrO_V3_17HB    = BrO_V3_17HB[V3_17_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V3_17_Y1maskHB = np.isfinite(BrO_V3_17HB) # Scan for NaN values
BrO_V3_17HS    = BrO_V3_17HS[V3_17_Y1maskHB] # BrO HWS Surface
BrO_V3_17HB    = BrO_V3_17HB[V3_17_Y1maskHB] # BrO HWS Boundary

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (BrO Surface)
V1_18_Y1maskHS = np.isfinite(BrO_V1_18HS) # Scan for NaN values
BrO_V1_18HS    = BrO_V1_18HS[V1_18_Y1maskHS] # BrO HWS Surface
BrO_V1_18HB    = BrO_V1_18HB[V1_18_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary)
V1_18_Y1maskHB = np.isfinite(BrO_V1_18HB) # Scan for NaN values
BrO_V1_18HS    = BrO_V1_18HS[V1_18_Y1maskHB] # BrO HWS Surface
BrO_V1_18HB    = BrO_V1_18HB[V1_18_Y1maskHB] # BrO HWS Boundary

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (BrO Surface) 
V2_18_Y1maskHS = np.isfinite(BrO_V2_18HS) # Scan for NaN values
BrO_V2_18HS    = BrO_V2_18HS[V2_18_Y1maskHS] # BrO HWS Surface
BrO_V2_18HB    = BrO_V2_18HB[V2_18_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V2_18_Y1maskHB = np.isfinite(BrO_V2_18HB) # Scan for NaN values
BrO_V2_18HS    = BrO_V2_18HS[V2_18_Y1maskHB] # BrO HWS Surface
BrO_V2_18HB    = BrO_V2_18HB[V2_18_Y1maskHB] # BrO HWS Boundary

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (BrO Surface) 
V3_18_Y1maskHS = np.isfinite(BrO_V3_18HS) # Scan for NaN values
BrO_V3_18HS    = BrO_V3_18HS[V3_18_Y1maskHS] # BrO HWS Surface
BrO_V3_18HB    = BrO_V3_18HB[V3_18_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
V3_18_Y1maskHB = np.isfinite(BrO_V3_18HB) # Scan for NaN values
BrO_V3_18HS    = BrO_V3_18HS[V3_18_Y1maskHB] # BrO HWS Surface
BrO_V3_18HB    = BrO_V3_18HB[V3_18_Y1maskHB] # BrO HWS Boundary

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO Surface) 
ALL_Y1maskHS   = np.isfinite(BrOHS) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHS] # BrO HWS Surface
BrOHB          = BrOHB[ALL_Y1maskHS] # BrO HWS Boundary

# Pass 2 (BrO Boundary) 
ALL_Y1maskHB   = np.isfinite(BrOHB) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHB] # BrO HWS Surface
BrOHB          = BrOHB[ALL_Y1maskHB] # BrO HWS Boundary

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)
#-----------------------------------
# Between BrO Surface (0-100m) and BrO Boundary (100-300m)
#-----------------------------------

#-----------------------------------
# Low Wind Speed (<=7 m/s) 
#-----------------------------------
#--------------------------------
# V1_17 (2017-18)
#--------------------------------
r_rowD_V1_17L, p_valueD_V1_17L = stats.pearsonr(BrO_V1_17LS,BrO_V1_17LB)
slopeD_V1_17L, interceptD_V1_17L, rD_V1_17L, pD_V1_17L, std_errD_V1_17L = stats.linregress(BrO_V1_17LS,BrO_V1_17LB)

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
r_rowD_V2_17L, p_valueD_V2_17L = stats.pearsonr(BrO_V2_17LS,BrO_V2_17LB)
slopeD_V2_17L, interceptD_V2_17L, rD_V2_17L, pD_V2_17L, std_errD_V2_17L = stats.linregress(BrO_V2_17LS,BrO_V2_17LB)

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
r_rowD_V3_17L, p_valueD_V3_17L = stats.pearsonr(BrO_V3_17LS,BrO_V3_17LB)
slopeD_V3_17L, interceptD_V3_17L, rD_V3_17L, pD_V3_17L, std_errD_V3_17L = stats.linregress(BrO_V3_17LS,BrO_V3_17LB)

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
r_rowD_V1_18L, p_valueD_V1_18L = stats.pearsonr(BrO_V1_18LS,BrO_V1_18LB)
slopeD_V1_18L, interceptD_V1_18L, rD_V1_18L, pD_V1_18L, std_errD_V1_18L = stats.linregress(BrO_V1_18LS,BrO_V1_18LB)

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
r_rowD_V2_18L, p_valueD_V2_18L = stats.pearsonr(BrO_V2_18LS,BrO_V2_18LB)
slopeD_V2_18L, interceptD_V2_18L, rD_V2_18L, pD_V2_18L, std_errD_V2_18L = stats.linregress(BrO_V2_18LS,BrO_V2_18LB)

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
r_rowD_V3_18L, p_valueD_V3_18L = stats.pearsonr(BrO_V3_18LS,BrO_V3_18LB)
slopeD_V3_18L, interceptD_V3_18L, rD_V3_18L, pD_V3_18L, std_errD_V3_18L = stats.linregress(BrO_V3_18LS,BrO_V3_18LB)

#--------------------------------
# COMBINED
#--------------------------------
r_rowDL, p_valueDL = stats.pearsonr(BrOLS,BrOLB)
slopeDL, interceptDL, rDL, pDL, std_errDL = stats.linregress(BrOLS,BrOLB)

#------------------------------------------------------------------------------
#-----------------------------------
# High Wind Speed (>7 m/s) 
#-----------------------------------
#--------------------------------
# V1_17 (2017-18)
#--------------------------------
r_rowD_V1_17H, p_valueD_V1_17H = stats.pearsonr(BrO_V1_17HS,BrO_V1_17HB)
slopeD_V1_17H, interceptD_V1_17H, rD_V1_17H, pD_V1_17H, std_errD_V1_17H = stats.linregress(BrO_V1_17HS,BrO_V1_17HB)

##--------------------------------
## V2_17 (2017-18)
##--------------------------------
#r_rowD_V2_17H, p_valueD_V2_17HB = stats.pearsonr(BrO_V2_17HS,BrO_V2_17HB)
#slopeD_V2_17H, interceptD_V2_17HB, rD_V2_17H, pD_V2_17H, std_errD_V2_17H = stats.linregress(BrO_V2_17HS,BrO_V2_17HB)

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
r_rowD_V3_17H, p_valueD_V3_17H = stats.pearsonr(BrO_V3_17HS,BrO_V3_17HB)
slopeD_V3_17H, interceptD_V3_17H, rD_V3_17H, pD_V3_17H, std_errD_V3_17H = stats.linregress(BrO_V3_17HS,BrO_V3_17HB)

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
r_rowD_V1_18H, p_valueD_V1_18H = stats.pearsonr(BrO_V1_18HS,BrO_V1_18HB)
slopeD_V1_18H, interceptD_V1_18H, rD_V1_18H, pD_V1_18H, std_errD_V1_18H = stats.linregress(BrO_V1_18HS,BrO_V1_18HB)

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
r_rowD_V2_18H, p_valueD_V2_18H = stats.pearsonr(BrO_V2_18HS,BrO_V2_18HB)
slopeD_V2_18H, interceptD_V2_18H, rD_V2_18H, pD_V2_18H, std_errD_V2_18H = stats.linregress(BrO_V2_18HS,BrO_V2_18HB)

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
r_rowD_V3_18H, p_valueD_V3_18H = stats.pearsonr(BrO_V3_18HS,BrO_V3_18HB)
slopeD_V3_18H, interceptD_V3_18H, rD_V3_18H, pD_V3_18H, std_errD_V3_18H = stats.linregress(BrO_V3_18HS,BrO_V3_18HB)

#--------------------------------
# COMBINED
#--------------------------------
r_rowDH, p_valueDH = stats.pearsonr(BrOHS,BrOHB)
slopeDH, interceptDH, rDH, pDH, std_errDH = stats.linregress(BrOHS,BrOHB)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs O3)

fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) 
#-----------------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO Surface (0-100m) vs BrO Boundary (100-300m)
ax.scatter(BrO_V1_17LS,   BrO_V1_17LB,   edgecolors='none', marker='x', c='black',  label='V1 (2017-18)')
ax.scatter(BrO_V2_17LS,   BrO_V2_17LB,   edgecolors='none', marker='x', c='red',    label='V2 (2017-18)')
ax.scatter(BrO_V3_17LS,   BrO_V3_17LB,   edgecolors='none', marker='x', c='blue',   label='V3 (2017-18)')
ax.scatter(BrO_V1_18LS,   BrO_V1_18LB,   edgecolors='none', marker='x', c='green',  label='V1 (2018-19)')
ax.scatter(BrO_V2_18LS,   BrO_V2_18LB,   edgecolors='none', marker='x', c='yellow', label='V2 (2018-19)')
ax.scatter(BrO_V3_18LS,   BrO_V3_18LB,   edgecolors='none', marker='x', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(BrOLS, interceptDL + slopeDL * BrOLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 25.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0, 25.0)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)\n[100-300m ASL]', fontsize=20)
ax.set_xlabel('BrO (pptv)\n[0-100m ASL]', fontsize=20)

# Plot the title
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax.legend(bbox_to_anchor=(0.865, 0.95), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("BrO (0-100m) and BrO (100-300m):\n (slope: "+str("%7.4f"%(slopeDL))+" $\pm$"+str("%7.4f"%(std_errDL))+" pptv, r: "+str("%7.4f"%(rDL))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s)
#-----------------------------------
# Graph 1
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO Surface (0-100m) vs BrO Boundary (100-300m)
ax.scatter(BrO_V1_17HS,   BrO_V1_17HB,   edgecolors='none', marker='x', c='black',  label='V1 (2017-18)')
#ax.scatter(BrO_V2_17HS,   BrO_V2_17HB,   edgecolors='none', marker='x', c='red',    label='V2 (2017-18)')
ax.scatter(BrO_V3_17HS,   BrO_V3_17HB,   edgecolors='none', marker='x', c='blue',   label='V3 (2017-18)')
ax.scatter(BrO_V1_18HS,   BrO_V1_18HB,   edgecolors='none', marker='x', c='green',  label='V1 (2018-19)')
ax.scatter(BrO_V2_18HS,   BrO_V2_18HB,   edgecolors='none', marker='x', c='yellow', label='V2 (2018-19)')
ax.scatter(BrO_V3_18HS,   BrO_V3_18HB,   edgecolors='none', marker='x', c='purple', label='V3 (2018-19)')

# Plot the regression line
line1, = plt.plot(BrOHS, interceptDH + slopeDH * BrOHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 25.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0, 25.0)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)\n[100-300m ASL]', fontsize=20)
ax.set_xlabel('BrO (pptv)\n[0-100m ASL ]', fontsize=20)

# Plot the title
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("BrO (0-100m) and BrO (100-300m):\n (slope: "+str("%7.4f"%(slopeDH))+" $\pm$"+str("%7.4f"%(std_errDH))+" pptv, r: "+str("%7.4f"%(rDH))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)
