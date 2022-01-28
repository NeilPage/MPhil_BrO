#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:10:29 2020

@author: ncp532
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:14:04 2019

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

# BrO
V1_17_BrO     = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_F.csv')
V2_17_BrO     = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V2_17_F.csv')
V3_17_BrO     = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V3_17_F.csv')
V1_18_BrO     = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_18_F.csv')
V2_18_BrO     = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V2_18_F.csv')
V3_18_BrO     = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V3_18_F.csv')
SIPEXII_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII_F.csv')

# BrO VMR
V1_17_VMR     = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_VMR.csv',     index_col=0) # BrO VMR for CAMPCANN V1 (2017/18)
V2_17_VMR     = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_VMR.csv',     index_col=0) # BrO VMR for CAMPCANN V2 (2017/18)
V3_17_VMR     = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_VMR.csv',     index_col=0) # BrO VMR for CAMPCANN V3 (2017/18)
V1_18_VMR     = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_VMR.csv',     index_col=0) # BrO VMR for CAMPCANN V1 (2018/19)
V2_18_VMR     = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_VMR.csv',     index_col=0) # BrO VMR for CAMPCANN V2 (2018/19)
V3_18_VMR     = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_VMR.csv',     index_col=0) # BrO VMR for CAMPCANN V3 (2018/19)
SIPEXII_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_VMR.csv', index_col=0) # BrO VMR for SIPEXII (2012)

# BrO VMR error
V1_17_Error   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/BrO_error/V1_17_BrO_error.csv',     index_col=0) # BrO VMR error for CAMPCANN V1 (2017/18)
V2_17_Error   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/BrO_error/V2_17_BrO_error.csv',     index_col=0) # BrO VMR error for CAMPCANN V2 (2017/18)
V3_17_Error   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/BrO_error/V3_17_BrO_error.csv',     index_col=0) # BrO VMR error for CAMPCANN V3 (2017/18)
V1_18_Error   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/BrO_error/V1_18_BrO_error.csv',     index_col=0) # BrO VMR error for CAMPCANN V1 (2018/19)
V2_18_Error   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/BrO_error/V2_18_BrO_error.csv',     index_col=0) # BrO VMR error for CAMPCANN V2 (2018/19)
V3_18_Error   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/BrO_error/V3_18_BrO_error.csv',     index_col=0) # BrO VMR error for CAMPCANN V3 (2018/19)
SIPEXII_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/BrO_error/SIPEXII_BrO_error.csv', index_col=0) # BrO VMR error for SIPEXII (2012)
# Sea Ice
V1_17_SI      = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv')
V2_17_SI      = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv')
V3_17_SI      = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv')
V1_18_SI      = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv')
V2_18_SI      = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv')
V3_18_SI      = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv')
SIPEXII_SI    = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv')

# Met
V1_17_Met     = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv')
V2_17_Met     = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv')
V3_17_Met     = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv')
V1_18_Met     = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv')
V2_18_Met     = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv')
V3_18_Met     = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv')
SIPEXII_Met   = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_underway_60.csv')

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

# BrO
V1_17_BrO['DateTime']   = pd.to_datetime(V1_17_BrO['DateTime'],   dayfirst=True)
V2_17_BrO['DateTime']   = pd.to_datetime(V2_17_BrO['DateTime'],   dayfirst=True)
V3_17_BrO['DateTime']   = pd.to_datetime(V3_17_BrO['DateTime'],   dayfirst=True)
V1_18_BrO['DateTime']   = pd.to_datetime(V1_18_BrO['DateTime'],   dayfirst=True)
V2_18_BrO['DateTime']   = pd.to_datetime(V2_18_BrO['DateTime'],   dayfirst=True)
V3_18_BrO['DateTime']   = pd.to_datetime(V3_18_BrO['DateTime'],   dayfirst=True)
SIPEXII_BrO['DateTime'] = pd.to_datetime(SIPEXII_BrO['DateTime'], dayfirst=True)

# BrO VMR
V1_17_VMR.columns       = (pd.to_datetime(V1_17_VMR.columns,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
V2_17_VMR.columns       = (pd.to_datetime(V2_17_VMR.columns,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
V3_17_VMR.columns       = (pd.to_datetime(V3_17_VMR.columns,   dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
V1_18_VMR.columns       = (pd.to_datetime(V1_18_VMR.columns,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
V2_18_VMR.columns       = (pd.to_datetime(V2_18_VMR.columns,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
V3_18_VMR.columns       = (pd.to_datetime(V3_18_VMR.columns,   dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
SIPEXII_VMR.columns     = (pd.to_datetime(SIPEXII_VMR.columns, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

# Sea Ice
V1_17_SI['DateTime']    = pd.to_datetime(V1_17_SI['DateTime'],   dayfirst=True)
V2_17_SI['DateTime']    = pd.to_datetime(V2_17_SI['DateTime'],   dayfirst=True)
V3_17_SI['DateTime']    = pd.to_datetime(V3_17_SI['DateTime'],   dayfirst=True)
V1_18_SI['DateTime']    = pd.to_datetime(V1_18_SI['DateTime'],   dayfirst=True)
V2_18_SI['DateTime']    = pd.to_datetime(V2_18_SI['DateTime'],   dayfirst=True)
V3_18_SI['DateTime']    = pd.to_datetime(V3_18_SI['DateTime'],   dayfirst=True)
SIPEXII_SI['DateTime']  = pd.to_datetime(SIPEXII_SI['DateTime'], dayfirst=True)

# Met
V1_17_Met['DateTime']   = pd.to_datetime(V1_17_Met['DateTime'],   dayfirst=True)
V2_17_Met['DateTime']   = pd.to_datetime(V2_17_Met['DateTime'],   dayfirst=True)
V3_17_Met['DateTime']   = pd.to_datetime(V3_17_Met['DateTime'],   dayfirst=True)
V1_18_Met['DateTime']   = pd.to_datetime(V1_18_Met['DateTime'],   dayfirst=True)
V2_18_Met['DateTime']   = pd.to_datetime(V2_18_Met['DateTime'],   dayfirst=True)
V3_18_Met['DateTime']   = pd.to_datetime(V3_18_Met['DateTime'],   dayfirst=True)
SIPEXII_Met['DateTime'] = pd.to_datetime(SIPEXII_Met['DateTime'], dayfirst=True)

#------------------------------------------------------------------------------
# Transpose the VMR dataframes

V1_17TT   = V1_17_VMR.T
V2_17TT   = V2_17_VMR.T
V3_17TT   = V3_17_VMR.T
V1_18TT   = V1_18_VMR.T
V2_18TT   = V2_18_VMR.T
V3_18TT   = V3_18_VMR.T
SIPEXIITT = SIPEXII_VMR.T

#------------------------------------------------------------------------------
# Add columns for DateTime, Date and Time

# DateTime
V1_17TT['DateTime']   = V1_17TT.index
V2_17TT['DateTime']   = V2_17TT.index
V3_17TT['DateTime']   = V3_17TT.index
V1_18TT['DateTime']   = V1_18TT.index
V2_18TT['DateTime']   = V2_18TT.index
V3_18TT['DateTime']   = V3_18TT.index
SIPEXIITT['DateTime'] = SIPEXIITT.index

# Date
V1_17TT['Date']       = V1_17TT['DateTime'].dt.date
V2_17TT['Date']       = V2_17TT['DateTime'].dt.date
V3_17TT['Date']       = V3_17TT['DateTime'].dt.date
V1_18TT['Date']       = V1_18TT['DateTime'].dt.date
V2_18TT['Date']       = V2_18TT['DateTime'].dt.date
V3_18TT['Date']       = V3_18TT['DateTime'].dt.date
SIPEXIITT['Date']     = SIPEXIITT['DateTime'].dt.date

# Time
V1_17TT['Time']       = V1_17TT['DateTime'].dt.time
V2_17TT['Time']       = V2_17TT['DateTime'].dt.time
V3_17TT['Time']       = V3_17TT['DateTime'].dt.time
V1_18TT['Time']       = V1_18TT['DateTime'].dt.time
V2_18TT['Time']       = V2_18TT['DateTime'].dt.time
V3_18TT['Time']       = V3_18TT['DateTime'].dt.time
SIPEXIITT['Time']     = SIPEXIITT['DateTime'].dt.time

#------------------------------------------------------------------------------
# set datetime as the index

# BrO
V1_17_BrO   = V1_17_BrO.set_index('DateTime')
V2_17_BrO   = V2_17_BrO.set_index('DateTime')
V3_17_BrO   = V3_17_BrO.set_index('DateTime')
V1_18_BrO   = V1_18_BrO.set_index('DateTime')
V2_18_BrO   = V2_18_BrO.set_index('DateTime')
V3_18_BrO   = V3_18_BrO.set_index('DateTime')
SIPEXII_BrO = SIPEXII_BrO.set_index('DateTime')

# Sea Ice
V1_17_SI    = V1_17_SI.set_index('DateTime')
V2_17_SI    = V2_17_SI.set_index('DateTime')
V3_17_SI    = V3_17_SI.set_index('DateTime')
V1_18_SI    = V1_18_SI.set_index('DateTime')
V2_18_SI    = V2_18_SI.set_index('DateTime')
V3_18_SI    = V3_18_SI.set_index('DateTime')
SIPEXII_SI  = SIPEXII_SI.set_index('DateTime')

# Met
V1_17_Met   = V1_17_Met.set_index('DateTime')
V2_17_Met   = V2_17_Met.set_index('DateTime')
V3_17_Met   = V3_17_Met.set_index('DateTime')
V1_18_Met   = V1_18_Met.set_index('DateTime')
V2_18_Met   = V2_18_Met.set_index('DateTime')
V3_18_Met   = V3_18_Met.set_index('DateTime')
SIPEXII_Met = SIPEXII_Met.set_index('DateTime')

#------------------------------------------------------------------------------
# Resample all data to 20 min averages

# Sea Ice
V1_17_SI    = V1_17_SI.resample('20T').mean()
V2_17_SI    = V2_17_SI.resample('20T').mean()
V3_17_SI    = V3_17_SI.resample('20T').mean()
V1_18_SI    = V1_18_SI.resample('20T').mean()
V2_18_SI    = V2_18_SI.resample('20T').mean()
V3_18_SI    = V3_18_SI.resample('20T').mean()
SIPEXII_SI  = SIPEXII_SI.resample('20T').mean()

# Met
V1_17_Met    = V1_17_Met.resample('20T').mean()
V2_17_Met    = V2_17_Met.resample('20T').mean()
V3_17_Met    = V3_17_Met.resample('20T').mean()
V1_18_Met    = V1_18_Met.resample('20T').mean()
V2_18_Met    = V2_18_Met.resample('20T').mean()
V3_18_Met    = V3_18_Met.resample('20T').mean()
SIPEXII_Met  = SIPEXII_Met.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

# Sea Ice
V1_17_SI.index    = V1_17_SI.index - pd.Timedelta(minutes=10)
V2_17_SI.index    = V2_17_SI.index - pd.Timedelta(minutes=10)
V3_17_SI.index    = V3_17_SI.index - pd.Timedelta(minutes=10)
V1_18_SI.index    = V1_18_SI.index - pd.Timedelta(minutes=10)
V2_18_SI.index    = V2_18_SI.index - pd.Timedelta(minutes=10)
V3_18_SI.index    = V3_18_SI.index - pd.Timedelta(minutes=10)
SIPEXII_SI.index  = SIPEXII_SI.index - pd.Timedelta(minutes=10)

# Met
V1_17_Met.index    = V1_17_Met.index - pd.Timedelta(minutes=10)
V2_17_Met.index    = V2_17_Met.index - pd.Timedelta(minutes=10)
V3_17_Met.index    = V3_17_Met.index - pd.Timedelta(minutes=10)
V1_18_Met.index    = V1_18_Met.index - pd.Timedelta(minutes=10)
V2_18_Met.index    = V2_18_Met.index - pd.Timedelta(minutes=10)
V3_18_Met.index    = V3_18_Met.index - pd.Timedelta(minutes=10)
SIPEXII_Met.index  = SIPEXII_Met.index - pd.Timedelta(minutes=10)

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
# V2_17 (08:00 to 16:00)
#-----------------------
start_time = '08:00:00'
end_time   = '16:00:00'
# BrO
Midday     = (V2_17_BrO['Time'] >= start_time) & (V2_17_BrO['Time'] < end_time)
V2_17_MM   = V2_17_BrO[Midday]
# VMR
start_time = pd.to_datetime('08:00:00').time()
end_time   = pd.to_datetime('16:00:00').time()
Midday_VMR = (V2_17TT['Time'] >= start_time) & (V2_17TT['Time'] < end_time)
V2_17M     = V2_17TT[Midday_VMR]

#-----------------------
# V3_17 (08:00 to 18:00)
#-----------------------
start_time = '08:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (V3_17_BrO['Time'] >= start_time) & (V3_17_BrO['Time'] < end_time)
V3_17_MM   = V3_17_BrO[Midday]
# VMR
start_time = pd.to_datetime('08:00:00').time()
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
# V2_18 (08:00 to 16:00)
#-----------------------
start_time = '08:00:00'
end_time   = '16:00:00'
# BrO
Midday     = (V2_18_BrO['Time'] >= start_time) & (V2_18_BrO['Time'] < end_time)
V2_18_MM   = V2_18_BrO[Midday]
# VMR
start_time = pd.to_datetime('08:00:00').time()
end_time   = pd.to_datetime('16:00:00').time()
Midday_VMR = (V2_18TT['Time'] >= start_time) & (V2_18TT['Time'] < end_time)
V2_18M     = V2_18TT[Midday_VMR]

#-----------------------
# V3_18 (08:00 to 18:00)
#-----------------------
start_time = '08:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (V3_18_BrO['Time'] >= start_time) & (V3_18_BrO['Time'] < end_time)
V3_18_MM   = V3_18_BrO[Midday]
# VMR
start_time = pd.to_datetime('08:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (V3_18TT['Time'] >= start_time) & (V3_18TT['Time'] < end_time)
V3_18M     = V3_18TT[Midday_VMR]

#-----------------------
# SIPEXII (07:00 to 18:00)
#-----------------------
start_time = '07:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (SIPEXII_BrO['Time'] >= start_time) & (SIPEXII_BrO['Time'] < end_time)
SIPEXII_MM = SIPEXII_BrO[Midday]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (SIPEXIITT['Time'] >= start_time) & (SIPEXIITT['Time'] < end_time)
SIPEXIIM   = SIPEXIITT[Midday_VMR]

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

# SIPEXII (23 Sep to 11 Nov 2012)
start_date   = '2012-09-23'
end_date     = '2012-11-11'
# BrO
SIPEX_BrO    = (SIPEXIIT.index >= start_date) & (SIPEXIIT.index < end_date)
SIPEXIIT     = SIPEXIIT[SIPEX_BrO]
# VMR
SIPEX_VMR    = (SIPEXIIM.index >= start_date) & (SIPEXIIM.index < end_date)
SIPEXIIM     = SIPEXIIM[SIPEX_VMR]

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

# Pass 1
D1_V1_17   = pd.merge(left=V1_17M,     right=V1_17_SI,   how='left', left_index=True, right_index=True)
D1_V2_17   = pd.merge(left=V2_17M,     right=V2_17_SI,   how='left', left_index=True, right_index=True)
D1_V3_17   = pd.merge(left=V3_17M,     right=V3_17_SI,   how='left', left_index=True, right_index=True)
D1_V1_18   = pd.merge(left=V1_18M,     right=V1_18_SI,   how='left', left_index=True, right_index=True)
D1_V2_18   = pd.merge(left=V2_18M,     right=V2_18_SI,   how='left', left_index=True, right_index=True)
D1_V3_18   = pd.merge(left=V3_18M,     right=V3_18_SI,   how='left', left_index=True, right_index=True)
D1_SIPEXII = pd.merge(left=SIPEXIIM,   right=SIPEXII_SI, how='left', left_index=True, right_index=True)

# Pass 2
D1_V1_17   = pd.merge(left=D1_V1_17,   right=V1_17_Met,   how='left', left_index=True, right_index=True)
D1_V2_17   = pd.merge(left=D1_V2_17,   right=V2_17_Met,   how='left', left_index=True, right_index=True)
D1_V3_17   = pd.merge(left=D1_V3_17,   right=V3_17_Met,   how='left', left_index=True, right_index=True)
D1_V1_18   = pd.merge(left=D1_V1_18,   right=V1_18_Met,   how='left', left_index=True, right_index=True)
D1_V2_18   = pd.merge(left=D1_V2_18,   right=V2_18_Met,   how='left', left_index=True, right_index=True)
D1_V3_18   = pd.merge(left=D1_V3_18,   right=V3_18_Met,   how='left', left_index=True, right_index=True)
D1_SIPEXII = pd.merge(left=D1_SIPEXII, right=SIPEXII_Met, how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Calculate the Wind Speed average

WS_s_V1_17           = np.array(D1_V1_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17           = np.array(D1_V1_17['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
D1_V1_17['WS_Avg']   = (WS_s_V1_17 + WS_p_V1_17)/2 # Average the wind speed for port and starboard

WS_s_V2_17           = np.array(D1_V2_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17           = np.array(D1_V2_17['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
D1_V2_17['WS_Avg']   = (WS_s_V2_17 + WS_p_V2_17)/2 # Average the wind speed for port and starboard

WS_s_V3_17           = np.array(D1_V3_17['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17           = np.array(D1_V3_17['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
D1_V3_17['WS_Avg']   = (WS_s_V3_17 + WS_p_V3_17)/2 # Average the wind speed for port and starboard

WS_s_V1_18           = np.array(D1_V1_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18           = np.array(D1_V1_18['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
D1_V1_18['WS_Avg']   = (WS_s_V1_18 + WS_p_V1_18)/2 # Average the wind speed for port and starboard

WS_s_V2_18           = np.array(D1_V2_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18           = np.array(D1_V2_18['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
D1_V2_18['WS_Avg']   = (WS_s_V2_18 + WS_p_V2_18)/2 # Average the wind speed for port and starboard

WS_s_V3_18           = np.array(D1_V3_18['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18           = np.array(D1_V3_18['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
D1_V3_18['WS_Avg']   = (WS_s_V3_18 + WS_p_V3_18)/2 # Average the wind speed for port and starboard

WS_s_SIPEXII         = np.array(D1_SIPEXII['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXII         = np.array(D1_SIPEXII['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
D1_SIPEXII['WS_Avg'] = (WS_s_SIPEXII + WS_p_SIPEXII)/2 # Average the wind speed for port and starboard

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

SIPEXII_LWS = (D1_SIPEXII['WS_Avg'] <= 7)
D1_SIPEXIIL = D1_SIPEXII[SIPEXII_LWS]

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

SIPEXII_HWS = (D1_SIPEXII['WS_Avg'] > 7)
D1_SIPEXIIH = D1_SIPEXII[SIPEXII_HWS]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover is 0%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17F1L   = (D1_V1_17L['Sea_Ice_Conc'] == 0)
V1_17ZL    = D1_V1_17L[V1_17F1L]

V2_17F1L   = (D1_V2_17L['Sea_Ice_Conc'] == 0)
V2_17ZL    = D1_V2_17L[V2_17F1L]

V3_17F1L   = (D1_V3_17L['Sea_Ice_Conc'] == 0)
V3_17ZL    = D1_V3_17L[V3_17F1L]

V1_18F1L   = (D1_V1_18L['Sea_Ice_Conc'] == 0)
V1_18ZL    = D1_V1_18L[V1_18F1L]

V2_18F1L   = (D1_V2_18L['Sea_Ice_Conc'] == 0)
V2_18ZL    = D1_V2_18L[V2_18F1L]

V3_18F1L   = (D1_V3_18L['Sea_Ice_Conc'] == 0)
V3_18ZL    = D1_V3_18L[V3_18F1L]

SIPEXIIF1L = (D1_SIPEXIIL['Sea_Ice_Conc'] == 0)
SIPEXIIZL  = D1_SIPEXIIL[SIPEXIIF1L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17F1H   = (D1_V1_17H['Sea_Ice_Conc'] == 0)
V1_17ZH    = D1_V1_17H[V1_17F1H]

V2_17F1H   = (D1_V2_17H['Sea_Ice_Conc'] == 0)
V2_17ZH    = D1_V2_17H[V2_17F1H]

V3_17F1H   = (D1_V3_17H['Sea_Ice_Conc'] == 0)
V3_17ZH    = D1_V3_17H[V3_17F1H]

V1_18F1H   = (D1_V1_18H['Sea_Ice_Conc'] == 0)
V1_18ZH    = D1_V1_18H[V1_18F1H]

V2_18F1H   = (D1_V2_18H['Sea_Ice_Conc'] == 0)
V2_18ZH    = D1_V2_18H[V2_18F1H]

V3_18F1H   = (D1_V3_18H['Sea_Ice_Conc'] == 0)
V3_18ZH    = D1_V3_18H[V3_18F1H]

SIPEXIIF1H = (D1_SIPEXIIH['Sea_Ice_Conc'] == 0)
SIPEXIIZH  = D1_SIPEXIIH[SIPEXIIF1H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover is 100%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17F2L     = (D1_V1_17L['Sea_Ice_Conc'] >= 0.9) & (D1_V1_17L['Sea_Ice_Conc'] <= 1.0)
V1_17AL      = D1_V1_17L[V1_17F2L]

V2_17F2L     = (D1_V2_17L['Sea_Ice_Conc'] >= 0.9) & (D1_V2_17L['Sea_Ice_Conc'] <= 1.0)
V2_17AL      = D1_V2_17L[V2_17F2L]

V3_17F2L     = (D1_V3_17L['Sea_Ice_Conc'] >= 0.9) & (D1_V3_17L['Sea_Ice_Conc'] <= 1.0)
V3_17AL      = D1_V3_17L[V3_17F2L]

V1_18F2L     = (D1_V1_18L['Sea_Ice_Conc'] >= 0.9) & (D1_V1_18L['Sea_Ice_Conc'] <= 1.0)
V1_18AL      = D1_V1_18L[V1_18F2L]

V2_18F2L     = (D1_V2_18L['Sea_Ice_Conc'] >= 0.9) & (D1_V2_18L['Sea_Ice_Conc'] <= 1.0)
V2_18AL      = D1_V2_18L[V2_18F2L]

V3_18F2L     = (D1_V3_18L['Sea_Ice_Conc'] >= 0.9) & (D1_V3_18L['Sea_Ice_Conc'] <= 1.0)
V3_18AL      = D1_V3_18L[V3_18F2L]

SIPEXIIF2L   = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.9) & (D1_SIPEXIIL['Sea_Ice_Conc'] <= 1.0)
SIPEXIIAL    = D1_SIPEXIIL[SIPEXIIF2L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17F2H     = (D1_V1_17H['Sea_Ice_Conc'] >= 0.9) & (D1_V1_17H['Sea_Ice_Conc'] <= 1.0)
V1_17AH      = D1_V1_17H[V1_17F2H]

V2_17F2H     = (D1_V2_17H['Sea_Ice_Conc'] >= 0.9) & (D1_V2_17H['Sea_Ice_Conc'] <= 1.0)
V2_17AH      = D1_V2_17H[V2_17F2H]

V3_17F2H     = (D1_V3_17H['Sea_Ice_Conc'] >= 0.9) & (D1_V3_17H['Sea_Ice_Conc'] <= 1.0)
V3_17AH      = D1_V3_17H[V3_17F2H]

V1_18F2H     = (D1_V1_18H['Sea_Ice_Conc'] >= 0.9) & (D1_V1_18H['Sea_Ice_Conc'] <= 1.0)
V1_18AH      = D1_V1_18H[V1_18F2H]

V2_18F2H     = (D1_V2_18H['Sea_Ice_Conc'] >= 0.9) & (D1_V2_18H['Sea_Ice_Conc'] <= 1.0)
V2_18AH      = D1_V2_18H[V2_18F2H]

V3_18F2H     = (D1_V3_18H['Sea_Ice_Conc'] >= 0.9) & (D1_V3_18H['Sea_Ice_Conc'] <= 1.0)
V3_18AH      = D1_V3_18H[V3_18F2H]

SIPEXIIF2H   = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.9) & (D1_SIPEXIIH['Sea_Ice_Conc'] <= 1.0)
SIPEXIIAH    = D1_SIPEXIIH[SIPEXIIF2H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover is between 1-30%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17F3L     = (D1_V1_17L['Sea_Ice_Conc'] >= 0.01) & (D1_V1_17L['Sea_Ice_Conc'] < 0.3)
V1_17P1L     = D1_V1_17L[V1_17F3L]

V2_17F3L     = (D1_V2_17L['Sea_Ice_Conc'] >= 0.01) & (D1_V2_17L['Sea_Ice_Conc'] < 0.3)
V2_17P1L     = D1_V2_17L[V2_17F3L]

V3_17F3L     = (D1_V3_17L['Sea_Ice_Conc'] >= 0.01) & (D1_V3_17L['Sea_Ice_Conc'] < 0.3)
V3_17P1L     = D1_V3_17L[V3_17F3L]

V1_18F3L     = (D1_V1_18L['Sea_Ice_Conc'] >= 0.01) & (D1_V1_18L['Sea_Ice_Conc'] < 0.3)
V1_18P1L     = D1_V1_18L[V1_18F3L]

V2_18F3L     = (D1_V2_18L['Sea_Ice_Conc'] >= 0.01) & (D1_V2_18L['Sea_Ice_Conc'] < 0.3)
V2_18P1L     = D1_V2_18L[V2_18F3L]

V3_18F3L     = (D1_V3_18L['Sea_Ice_Conc'] >= 0.01) & (D1_V3_18L['Sea_Ice_Conc'] < 0.3)
V3_18P1L     = D1_V3_18L[V3_18F3L]

SIPEXIIF3L   = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.01) & (D1_SIPEXIIL['Sea_Ice_Conc'] < 0.3)
SIPEXIIP1L   = D1_SIPEXIIL[SIPEXIIF3L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17F3H     = (D1_V1_17H['Sea_Ice_Conc'] >= 0.01) & (D1_V1_17H['Sea_Ice_Conc'] < 0.3)
V1_17P1H     = D1_V1_17H[V1_17F3H]

V2_17F3H     = (D1_V2_17H['Sea_Ice_Conc'] >= 0.01) & (D1_V2_17H['Sea_Ice_Conc'] < 0.3)
V2_17P1H     = D1_V2_17H[V2_17F3H]

V3_17F3H     = (D1_V3_17H['Sea_Ice_Conc'] >= 0.01) & (D1_V3_17H['Sea_Ice_Conc'] < 0.3)
V3_17P1H     = D1_V3_17H[V3_17F3H]

V1_18F3H     = (D1_V1_18H['Sea_Ice_Conc'] >= 0.01) & (D1_V1_18H['Sea_Ice_Conc'] < 0.3)
V1_18P1H     = D1_V1_18H[V1_18F3H]

V2_18F3H     = (D1_V2_18H['Sea_Ice_Conc'] >= 0.01) & (D1_V2_18H['Sea_Ice_Conc'] < 0.3)
V2_18P1H     = D1_V2_18H[V2_18F3H]

V3_18F3H     = (D1_V3_18H['Sea_Ice_Conc'] >= 0.01) & (D1_V3_18H['Sea_Ice_Conc'] < 0.3)
V3_18P1H     = D1_V3_18H[V3_18F3H]

SIPEXIIF3H   = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.01) & (D1_SIPEXIIH['Sea_Ice_Conc'] < 0.3)
SIPEXIIP1H   = D1_SIPEXIIH[SIPEXIIF3H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover between 30-60%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17F4L     = (D1_V1_17L['Sea_Ice_Conc'] >= 0.3) & (D1_V1_17L['Sea_Ice_Conc'] < 0.6)
V1_17P2L     = D1_V1_17L[V1_17F4L]

V2_17F4L     = (D1_V2_17L['Sea_Ice_Conc'] >= 0.3) & (D1_V2_17L['Sea_Ice_Conc'] < 0.6)
V2_17P2L     = D1_V2_17L[V2_17F4L]

V3_17F4L     = (D1_V3_17L['Sea_Ice_Conc'] >= 0.3) & (D1_V3_17L['Sea_Ice_Conc'] < 0.6)
V3_17P2L     = D1_V3_17L[V3_17F4L]

V1_18F4L     = (D1_V1_18L['Sea_Ice_Conc'] >= 0.3) & (D1_V1_18L['Sea_Ice_Conc'] < 0.6)
V1_18P2L     = D1_V1_18L[V1_18F4L]

V2_18F4L     = (D1_V2_18L['Sea_Ice_Conc'] >= 0.3) & (D1_V2_18L['Sea_Ice_Conc'] < 0.6)
V2_18P2L     = D1_V2_18L[V2_18F4L]

V3_18F4L     = (D1_V3_18L['Sea_Ice_Conc'] >= 0.3) & (D1_V3_18L['Sea_Ice_Conc'] < 0.6)
V3_18P2L     = D1_V3_18L[V3_18F4L]

SIPEXIIF4L   = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.3) & (D1_SIPEXIIL['Sea_Ice_Conc'] < 0.6)
SIPEXIIP2L   = D1_SIPEXIIL[SIPEXIIF4L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17F4H     = (D1_V1_17H['Sea_Ice_Conc'] >= 0.3) & (D1_V1_17H['Sea_Ice_Conc'] < 0.6)
V1_17P2H     = D1_V1_17H[V1_17F4H]

V2_17F4H     = (D1_V2_17H['Sea_Ice_Conc'] >= 0.3) & (D1_V2_17H['Sea_Ice_Conc'] < 0.6)
V2_17P2H     = D1_V2_17H[V2_17F4H]

V3_17F4H     = (D1_V3_17H['Sea_Ice_Conc'] >= 0.3) & (D1_V3_17H['Sea_Ice_Conc'] < 0.6)
V3_17P2H     = D1_V3_17H[V3_17F4H]

V1_18F4H     = (D1_V1_18H['Sea_Ice_Conc'] >= 0.3) & (D1_V1_18H['Sea_Ice_Conc'] < 0.6)
V1_18P2H     = D1_V1_18H[V1_18F4H]

V2_18F4H     = (D1_V2_18H['Sea_Ice_Conc'] >= 0.3) & (D1_V2_18H['Sea_Ice_Conc'] < 0.6)
V2_18P2H     = D1_V2_18H[V2_18F4H]

V3_18F4H     = (D1_V3_18H['Sea_Ice_Conc'] >= 0.3) & (D1_V3_18H['Sea_Ice_Conc'] < 0.6)
V3_18P2H     = D1_V3_18H[V3_18F4H]

SIPEXIIF4H   = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.3) & (D1_SIPEXIIH['Sea_Ice_Conc'] < 0.6)
SIPEXIIP2H   = D1_SIPEXIIH[SIPEXIIF4H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover between 60-90%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17F5L     = (D1_V1_17L['Sea_Ice_Conc'] >= 0.6) & (D1_V1_17L['Sea_Ice_Conc'] < 0.9)
V1_17P3L      = D1_V1_17L[V1_17F5L]

V2_17F5L     = (D1_V2_17L['Sea_Ice_Conc'] >= 0.6) & (D1_V2_17L['Sea_Ice_Conc'] < 0.9)
V2_17P3L      = D1_V2_17L[V2_17F5L]

V3_17F5L     = (D1_V3_17L['Sea_Ice_Conc'] >= 0.6) & (D1_V3_17L['Sea_Ice_Conc'] < 0.9)
V3_17P3L      = D1_V3_17L[V3_17F5L]

V1_18F5L     = (D1_V1_18L['Sea_Ice_Conc'] >= 0.6) & (D1_V1_18L['Sea_Ice_Conc'] < 0.9)
V1_18P3L      = D1_V1_18L[V1_18F5L]

V2_18F5L     = (D1_V2_18L['Sea_Ice_Conc'] >= 0.6) & (D1_V2_18L['Sea_Ice_Conc'] < 0.9)
V2_18P3L     = D1_V2_18L[V2_18F5L]

V3_18F5L     = (D1_V3_18L['Sea_Ice_Conc'] >= 0.6) & (D1_V3_18L['Sea_Ice_Conc'] < 0.9)
V3_18P3L     = D1_V3_18L[V3_18F5L]

SIPEXIIF5L   = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.6) & (D1_SIPEXIIL['Sea_Ice_Conc'] < 0.9)
SIPEXIIP3L   = D1_SIPEXIIL[SIPEXIIF5L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17F5H     = (D1_V1_17H['Sea_Ice_Conc'] >= 0.6) & (D1_V1_17H['Sea_Ice_Conc'] < 0.9)
V1_17P3H      = D1_V1_17H[V1_17F5H]

V2_17F5H     = (D1_V2_17H['Sea_Ice_Conc'] >= 0.6) & (D1_V2_17H['Sea_Ice_Conc'] < 0.9)
V2_17P3H      = D1_V2_17H[V2_17F5H]

V3_17F5H     = (D1_V3_17H['Sea_Ice_Conc'] >= 0.6) & (D1_V3_17H['Sea_Ice_Conc'] < 0.9)
V3_17P3H      = D1_V3_17H[V3_17F5H]

V1_18F5H     = (D1_V1_18H['Sea_Ice_Conc'] >= 0.6) & (D1_V1_18H['Sea_Ice_Conc'] < 0.9)
V1_18P3H      = D1_V1_18H[V1_18F5H]

V2_18F5H     = (D1_V2_18H['Sea_Ice_Conc'] >= 0.6) & (D1_V2_18H['Sea_Ice_Conc'] < 0.9)
V2_18P3H     = D1_V2_18H[V2_18F5H]

V3_18F5H     = (D1_V3_18H['Sea_Ice_Conc'] >= 0.6) & (D1_V3_18H['Sea_Ice_Conc'] < 0.9)
V3_18P3H     = D1_V3_18H[V3_18F5H]

SIPEXIIF5H   = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.6) & (D1_SIPEXIIH['Sea_Ice_Conc'] < 0.9)
SIPEXIIP3H   = D1_SIPEXIIH[SIPEXIIF5H]

#------------------------------------------------------------------------------
# Concate the filtered dataframes

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
# Sea ice cover is 0%
zeroL = pd.concat([V1_17ZL, V2_17ZL, V3_17ZL, V1_18ZL, V2_18ZL, V3_18ZL])#, SIPEXIIZL])

# Sea ice cover is between 1-30%
partial1L = pd.concat([V1_17P1L, V2_17P1L, V3_17P1L, V1_18P1L, V2_18P1L, V3_18P1L])#, SIPEXIIP1L])

# Sea ice cover is between 30-60%
partial2L = pd.concat([V1_17P2L, V2_17P2L, V3_17P2L, V1_18P2L, V2_18P2L, V3_18P2L])#, SIPEXIIP2L])

# Sea ice cover is between 60-90%
partial3L = pd.concat([V1_17P3L, V2_17P3L, V3_17P3L, V1_18P3L, V2_18P3L, V3_18P3L])#, SIPEXIIP3L])

# Sea ice cover is 100%
fullL = pd.concat([V1_17AL, V2_17AL, V3_17AL, V1_18AL, V2_18AL, V3_18AL])#, SIPEXIIAL])

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
# Sea ice cover is 0%
zeroH = pd.concat([V1_17ZH, V2_17ZH, V3_17ZH, V1_18ZH, V2_18ZH, V3_18ZH])#, SIPEXIIZH])

# Sea ice cover is between 1-30%
partial1H = pd.concat([V1_17P1H, V2_17P1H, V3_17P1H, V1_18P1H, V2_18P1H, V3_18P1H])#, SIPEXIIP1H])

# Sea ice cover is between 30-60%
partial2H = pd.concat([V1_17P2H, V2_17P2H, V3_17P2H, V1_18P2H, V2_18P2H, V3_18P2H])#, SIPEXIIP2H])

# Sea ice cover is between 60-90%
partial3H = pd.concat([V1_17P3H, V2_17P3H, V3_17P3H, V1_18P3H, V2_18P3H, V3_18P3H])#, SIPEXIIP3H])

# Sea ice cover is 100%
fullH = pd.concat([V1_17AH, V2_17AH, V3_17AH, V1_18AH, V2_18AH, V3_18AH])#, SIPEXIIAH])

#------------------------------------------------------------------------------
# Calculate the Mean (BrO)

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
SmeanZL  = np.nanmean((zeroL[0.1])     * 1e6)
SmeanP1L = np.nanmean((partial1L[0.1]) * 1e6)
SmeanP2L = np.nanmean((partial2L[0.1]) * 1e6)
SmeanP3L = np.nanmean((partial3L[0.1]) * 1e6)
SmeanAL  = np.nanmean((fullL[0.1])     * 1e6)

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
SmeanZH  = np.nanmean((zeroH[0.1])     * 1e6)
SmeanP1H = np.nanmean((partial1H[0.1]) * 1e6)
SmeanP2H = np.nanmean((partial2H[0.1]) * 1e6)
SmeanP3H = np.nanmean((partial3H[0.1]) * 1e6)
SmeanAH  = np.nanmean((fullH[0.1])     * 1e6)

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
BmeanZL  = np.nanmean((zeroL[0.3])     * 1e6)
BmeanP1L = np.nanmean((partial1L[0.3]) * 1e6)
BmeanP2L = np.nanmean((partial2L[0.3]) * 1e6)
BmeanP3L = np.nanmean((partial3L[0.3]) * 1e6)
BmeanAL  = np.nanmean((fullL[0.3])     * 1e6)

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
BmeanZH  = np.nanmean((zeroH[0.3])     * 1e6)
BmeanP1H = np.nanmean((partial1H[0.3]) * 1e6)
BmeanP2H = np.nanmean((partial2H[0.3]) * 1e6)
BmeanP3H = np.nanmean((partial3H[0.3]) * 1e6)
BmeanAH  = np.nanmean((fullH[0.3])     * 1e6)

#------------------------------------------------------------------------------
# Calculate the Standard deviation (BrO)

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
SstdevZL  = np.nanstd((zeroL[0.1])     * 1e6)
SstdevP1L = np.nanstd((partial1L[0.1]) * 1e6)
SstdevP2L = np.nanstd((partial2L[0.1]) * 1e6)
SstdevP3L = np.nanstd((partial3L[0.1]) * 1e6)
SstdevAL  = np.nanstd((fullL[0.1])     * 1e6)

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
SstdevZH  = np.nanstd((zeroH[0.1])     * 1e6)
SstdevP1H = np.nanstd((partial1H[0.1]) * 1e6)
SstdevP2H = np.nanstd((partial2H[0.1]) * 1e6)
SstdevP3H = np.nanstd((partial3H[0.1]) * 1e6)
SstdevAH  = np.nanstd((fullH[0.1])     * 1e6)

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
BstdevZL  = np.nanstd((zeroL[0.3])     * 1e6)
BstdevP1L = np.nanstd((partial1L[0.3]) * 1e6)
BstdevP2L = np.nanstd((partial2L[0.3]) * 1e6)
BstdevP3L = np.nanstd((partial3L[0.3]) * 1e6)
BstdevAL  = np.nanstd((fullL[0.3])     * 1e6)

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
BstdevZH  = np.nanstd((zeroH[0.3])     * 1e6)
BstdevP1H = np.nanstd((partial1H[0.3]) * 1e6)
BstdevP2H = np.nanstd((partial2H[0.3]) * 1e6)
BstdevP3H = np.nanstd((partial3H[0.3]) * 1e6)
BstdevAH  = np.nanstd((fullH[0.3])     * 1e6)

#------------------------------------------------------------------------------
# Calculate the Median (BrO)

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
SmedianZL  = np.nanmedian((zeroL[0.1])     * 1e6)
SmedianP1L = np.nanmedian((partial1L[0.1]) * 1e6)
SmedianP2L = np.nanmedian((partial2L[0.1]) * 1e6)
SmedianP3L = np.nanmedian((partial3L[0.1]) * 1e6)
SmedianAL  = np.nanmedian((fullL[0.1])     * 1e6)

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
SmedianZH  = np.nanmedian((zeroH[0.1])     * 1e6)
SmedianP1H = np.nanmedian((partial1H[0.1]) * 1e6)
SmedianP2H = np.nanmedian((partial2H[0.1]) * 1e6)
SmedianP3H = np.nanmedian((partial3H[0.1]) * 1e6)
SmedianAH  = np.nanmedian((fullH[0.1])     * 1e6)

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
BmedianZL  = np.nanmedian((zeroL[0.3])     * 1e6)
BmedianP1L = np.nanmedian((partial1L[0.3]) * 1e6)
BmedianP2L = np.nanmedian((partial2L[0.3]) * 1e6)
BmedianP3L = np.nanmedian((partial3L[0.3]) * 1e6)
BmedianAL  = np.nanmedian((fullL[0.3])     * 1e6)

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
BmedianZH  = np.nanmedian((zeroH[0.3])     * 1e6)
BmedianP1H = np.nanmedian((partial1H[0.3]) * 1e6)
BmedianP2H = np.nanmedian((partial2H[0.3]) * 1e6)
BmedianP3H = np.nanmedian((partial3H[0.3]) * 1e6)
BmedianAH  = np.nanmedian((fullH[0.3])     * 1e6)

#------------------------------------------------------------------------------
# Calculate the Median absolute deviation (BrO)

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
SmadZL  = stats.median_absolute_deviation(zeroL[0.1],     nan_policy = 'omit') * 1e6
SmadP1L = stats.median_absolute_deviation(partial1L[0.1], nan_policy = 'omit') * 1e6
SmadP2L = stats.median_absolute_deviation(partial2L[0.1], nan_policy = 'omit') * 1e6
SmadP3L = stats.median_absolute_deviation(partial3L[0.1], nan_policy = 'omit') * 1e6
SmadAL  = stats.median_absolute_deviation(fullL[0.1],     nan_policy = 'omit') * 1e6

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
SmadZH  = stats.median_absolute_deviation(zeroH[0.1],     nan_policy = 'omit') * 1e6
SmadP1H = stats.median_absolute_deviation(partial1H[0.1], nan_policy = 'omit') * 1e6
SmadP2H = stats.median_absolute_deviation(partial2H[0.1], nan_policy = 'omit') * 1e6
SmadP3H = stats.median_absolute_deviation(partial3H[0.1], nan_policy = 'omit') * 1e6
SmadAH  = stats.median_absolute_deviation(fullH[0.1],     nan_policy = 'omit') * 1e6

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
BmadZL  = stats.median_absolute_deviation(zeroL[0.1],     nan_policy = 'omit') * 1e6
BmadP1L = stats.median_absolute_deviation(partial1L[0.1], nan_policy = 'omit') * 1e6
BmadP2L = stats.median_absolute_deviation(partial2L[0.1], nan_policy = 'omit') * 1e6
BmadP3L = stats.median_absolute_deviation(partial3L[0.1], nan_policy = 'omit') * 1e6
BmadAL  = stats.median_absolute_deviation(fullL[0.1],     nan_policy = 'omit') * 1e6

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
BmadZH  = stats.median_absolute_deviation(zeroH[0.1],     nan_policy = 'omit') * 1e6
BmadP1H = stats.median_absolute_deviation(partial1H[0.1], nan_policy = 'omit') * 1e6
BmadP2H = stats.median_absolute_deviation(partial2H[0.1], nan_policy = 'omit') * 1e6
BmadP3H = stats.median_absolute_deviation(partial3H[0.1], nan_policy = 'omit') * 1e6
BmadAH  = stats.median_absolute_deviation(fullH[0.1],     nan_policy = 'omit') * 1e6

#------------------------------------------------------------------------------
# Build a dataframe for the BrO BoxPlot

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
example_data1 = [((zeroL[0.1]) * 1e6), ((partial1L[0.1]) * 1e6), ((partial2L[0.1]) * 1e6), ((partial3L[0.1]) * 1e6), ((fullL[0.1]) * 1e6)]

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
example_data2 = [((zeroH[0.1]) * 1e6), ((partial1H[0.1]) * 1e6), ((partial2H[0.1]) * 1e6), ((partial3H[0.1]) * 1e6), ((fullH[0.1]) * 1e6)]

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
example_data3 = [((zeroL[0.3]) * 1e6), ((partial1L[0.3]) * 1e6), ((partial2L[0.3]) * 1e6), ((partial3L[0.3]) * 1e6), ((fullL[0.3]) * 1e6)]

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
example_data4 = [((zeroH[0.3]) * 1e6), ((partial1H[0.3]) * 1e6), ((partial2H[0.3]) * 1e6), ((partial3H[0.3]) * 1e6), ((fullH[0.3]) * 1e6)]

#------------------------------------------------------------------------------
# Build a dataframe for the SeaIce ScatterPlot

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
#example_data5 = pd.concat([partial1L, partial2L, partial3L, fullL])
example_data5 = pd.concat([partial2L, partial3L, fullL])

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
#example_data6 = pd.concat([partial1H, partial2H, partial3H, fullH])
example_data6 = pd.concat([partial2H, partial3H, fullH])

#------------------------------------------------------------------------------
# Define the variables

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------

BrO_LWS = np.array(example_data5[0.1]) * 1e6 # convert from ppmv to pptv
SI_LWS  = np.array(example_data5['Sea_Ice_Conc']) * 100

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------

BrO_HWS = np.array(example_data6[0.1]) * 1e6 # convert from ppmv to pptv
SI_HWS  = np.array(example_data6['Sea_Ice_Conc']) * 100

#------------------------------------------------------------------------------
# Scan for NaN values

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------

# Pass 1 (BrO) 
BrO_maskLWS = np.isfinite(BrO_LWS) # Scan for NaN values
BrO_LWS     = BrO_LWS[BrO_maskLWS] # Remove NaN values from BrO
SI_LWS      = SI_LWS[BrO_maskLWS] # Remove NaN values from Sol

# Pass 2 (SeaIce) 
SI_maskLWS = np.isfinite(SI_LWS) # Scan for NaN values
BrO_LWS     = BrO_LWS[SI_maskLWS] # Remove NaN values from BrO
SI_LWS      = SI_LWS[SI_maskLWS] # Remove NaN values from Sol

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------

# Pass 1 (BrO) 
BrO_maskHWS = np.isfinite(BrO_HWS) # Scan for NaN values
BrO_HWS     = BrO_HWS[BrO_maskHWS] # Remove NaN values from BrO
SI_HWS      = SI_HWS[BrO_maskHWS] # Remove NaN values from Sol

# Pass 2 (SeaIce) 
SI_maskHWS = np.isfinite(SI_HWS) # Scan for NaN values
BrO_HWS     = BrO_HWS[SI_maskHWS] # Remove NaN values from BrO
SI_HWS      = SI_HWS[SI_maskHWS] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------

r_rowD_LWS, p_valueD_LWS = stats.pearsonr(SI_LWS,BrO_LWS)
slopeD_LWS, interceptD_LWS, rD_LWS, pD_LWS, std_errD_LWS = stats.linregress(SI_LWS,BrO_LWS)

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------

r_rowD_HWS, p_valueD_HWS = stats.pearsonr(SI_HWS,BrO_HWS)
slopeD_HWS, interceptD_HWS, rD_HWS, pD_HWS, std_errD_HWS = stats.linregress(SI_HWS,BrO_HWS)

#------------------------------------------------------------------------------
# Make a list of the mean +/- std dev for each distribution

# text to include with label
j2 = 'mean = '

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
Smean1L = str("%4.2f"%(SmeanZL))  + u" \u00B1 " + str("%4.2f"%(SstdevZL))
#Smean2L = str("%4.2f"%(SmeanP1L)) + u" \u00B1 " + str("%4.2f"%(SstdevP1L))
Smean3L = str("%4.2f"%(SmeanP2L)) + u" \u00B1 " + str("%4.2f"%(SstdevP2L))
Smean4L = str("%4.2f"%(SmeanP3L)) + u" \u00B1 " + str("%4.2f"%(SstdevP3L))
Smean5L = str("%4.2f"%(SmeanAL))  + u" \u00B1 " + str("%4.2f"%(SstdevAL))

SDF2L = [Smean1L, Smean3L, Smean4L, Smean5L]

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
Smean1H = str("%4.2f"%(SmeanZH))  + u" \u00B1 " + str("%4.2f"%(SstdevZH))
#Smean2H = str("%4.2f"%(SmeanP1H)) + u" \u00B1 " + str("%4.2f"%(SstdevP1H))
Smean3H = str("%4.2f"%(SmeanP2H)) + u" \u00B1 " + str("%4.2f"%(SstdevP2H))
Smean4H = str("%4.2f"%(SmeanP3H)) + u" \u00B1 " + str("%4.2f"%(SstdevP3H))
Smean5H = str("%4.2f"%(SmeanAH))  + u" \u00B1 " + str("%4.2f"%(SstdevAH))

SDF2H = [Smean1H, Smean3H, Smean4H, Smean5H]

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
Bmean1L = str("%4.2f"%(BmeanZL))  + u" \u00B1 " + str("%4.2f"%(BstdevZL))
#Bmean2L = str("%4.2f"%(BmeanP1L)) + u" \u00B1 " + str("%4.2f"%(BstdevP1L))
Bmean3L = str("%4.2f"%(BmeanP2L)) + u" \u00B1 " + str("%4.2f"%(BstdevP2L))
Bmean4L = str("%4.2f"%(BmeanP3L)) + u" \u00B1 " + str("%4.2f"%(BstdevP3L))
Bmean5L = str("%4.2f"%(BmeanAL))  + u" \u00B1 " + str("%4.2f"%(BstdevAL))

BDF2L = [Bmean1L, Bmean3L, Bmean4L, Bmean5L]

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
Bmean1H = str("%4.2f"%(BmeanZH))  + u" \u00B1 " + str("%4.2f"%(BstdevZH))
#Bmean2H = str("%4.2f"%(BmeanP1H)) + u" \u00B1 " + str("%4.2f"%(BstdevP1H))
Bmean3H = str("%4.2f"%(BmeanP2H)) + u" \u00B1 " + str("%4.2f"%(BstdevP2H))
Bmean4H = str("%4.2f"%(BmeanP3H)) + u" \u00B1 " + str("%4.2f"%(BstdevP3H))
Bmean5H = str("%4.2f"%(BmeanAH))  + u" \u00B1 " + str("%4.2f"%(BstdevAH))

BDF2H = [Bmean1H, Bmean3H, Bmean4H, Bmean5H]

#------------------------------------------------------------------------------
# Make a list of the mean +/- std dev for each distribution

# text to include with label
j3 = 'median = '
j4 = 'median\n'

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
Smedian1L = str("%4.2f"%(SmedianZL))  + u" \u00B1 " + str("%4.2f"%(SmadZL))
#Smedian2L = str("%4.2f"%(SmedianP1L)) + u" \u00B1 " + str("%4.2f"%(SmadP1L))
Smedian3L = str("%4.2f"%(SmedianP2L)) + u" \u00B1 " + str("%4.2f"%(SmadP2L))
Smedian4L = str("%4.2f"%(SmedianP3L)) + u" \u00B1 " + str("%4.2f"%(SmadP3L))
Smedian5L = str("%4.2f"%(SmedianAL))  + u" \u00B1 " + str("%4.2f"%(SmadAL))

SMedianL  = [SmedianZL, SmedianP2L, SmedianP3L, SmedianAL]
SMADL     = [SmadZL, SmadP2L, SmadP3L, SmadAL]
SDF3L     = [Smedian1L, Smedian3L, Smedian4L, Smedian5L]

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
Smedian1H = str("%4.2f"%(SmedianZH))  + u" \u00B1 " + str("%4.2f"%(SmadZH))
#Smedian2H = str("%4.2f"%(SmedianP1H)) + u" \u00B1 " + str("%4.2f"%(SmadP1H))
Smedian3H = str("%4.2f"%(SmedianP2H)) + u" \u00B1 " + str("%4.2f"%(SmadP2H))
Smedian4H = str("%4.2f"%(SmedianP3H)) + u" \u00B1 " + str("%4.2f"%(SmadP3H))
Smedian5H = str("%4.2f"%(SmedianAH))  + u" \u00B1 " + str("%4.2f"%(SmadAH))

SMedianH  = [SmedianZH, SmedianP2H, SmedianP3H, SmedianAH]
SMADH     = [SmadZH, SmadP2H, SmadP3H, SmadAH]
SDF3H     = [Smedian1H, Smedian3H, Smedian4H, Smedian5H]

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
Bmedian1L = str("%4.2f"%(BmedianZL))  + u" \u00B1 " + str("%4.2f"%(BmadZL))
#Bmedian2L = str("%4.2f"%(BmedianP1L)) + u" \u00B1 " + str("%4.2f"%(BmadP1L))
Bmedian3L = str("%4.2f"%(BmedianP2L)) + u" \u00B1 " + str("%4.2f"%(BmadP2L))
Bmedian4L = str("%4.2f"%(BmedianP3L)) + u" \u00B1 " + str("%4.2f"%(BmadP3L))
Bmedian5L = str("%4.2f"%(BmedianAL))  + u" \u00B1 " + str("%4.2f"%(BmadAL))

BMedianL  = [BmedianZL, BmedianP2L, BmedianP3L, BmedianAL]
BMADL     = [BmadZL, BmadP2L, BmadP3L, BmadAL]
BDF3L     = [Bmedian1L, Bmedian3L, Bmedian4L, Bmedian5L]

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
Bmedian1H = str("%4.2f"%(BmedianZH))  + u" \u00B1 " + str("%4.2f"%(BmadZH))
#Bmedian2H = str("%4.2f"%(BmedianP1H)) + u" \u00B1 " + str("%4.2f"%(BmadP1H))
Bmedian3H = str("%4.2f"%(BmedianP2H)) + u" \u00B1 " + str("%4.2f"%(BmadP2H))
Bmedian4H = str("%4.2f"%(BmedianP3H)) + u" \u00B1 " + str("%4.2f"%(BmadP3H))
Bmedian5H = str("%4.2f"%(BmedianAH))  + u" \u00B1 " + str("%4.2f"%(BmadAH))

BMedianH  = [BmedianZH, BmedianP2H, BmedianP3H, BmedianAH]
BMADH     = [BmadZH, BmadP2H, BmadP3H, BmadAH]
BDF3H     = [Bmedian1H, Bmedian3H, Bmedian4H, Bmedian5H]

#------------------------------------------------------------------------------
# Scan for NaN values

#-----------------------------------
# SURFACE Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
Smask_zeroL     = np.isfinite(zeroL[0.1])         # Scan for NaN values
SzL             = zeroL[0.1][Smask_zeroL]          # Remove NaN values from BrO

Smask_partial1L = np.isfinite(partial1L[0.1])     # Scan for NaN values
Sp1L            = partial1L[0.1][Smask_partial1L]  # Remove NaN values from BrO

Smask_partial2L = np.isfinite(partial2L[0.1])     # Scan for NaN values
Sp2L            = partial2L[0.1][Smask_partial2L]  # Remove NaN values from BrO

Smask_partial3L = np.isfinite(partial3L[0.1])     # Scan for NaN values
Sp3L            = partial3L[0.1][Smask_partial3L]  # Remove NaN values from BrO

Smask_fullL     = np.isfinite(fullL[0.1])         # Scan for NaN values
SfL             = fullL[0.1][Smask_fullL]          # Remove NaN values from BrO

#-----------------------------------
# SURFACE High Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
Smask_zeroH     = np.isfinite(zeroH[0.1])         # Scan for NaN values
SzH             = zeroH[0.1][Smask_zeroH]          # Remove NaN values from BrO

Smask_partial1H = np.isfinite(partial1H[0.1])     # Scan for NaN values
Sp1H            = partial1H[0.1][Smask_partial1H]  # Remove NaN values from BrO

Smask_partial2H = np.isfinite(partial2H[0.1])     # Scan for NaN values
Sp2H            = partial2H[0.1][Smask_partial2H]  # Remove NaN values from BrO

Smask_partial3H = np.isfinite(partial3H[0.1])     # Scan for NaN values
Sp3H            = partial3H[0.1][Smask_partial3H]  # Remove NaN values from BrO

Smask_fullH     = np.isfinite(fullH[0.1])         # Scan for NaN values
SfH             = fullH[0.1][Smask_fullH]          # Remove NaN values from BrO

#-----------------------------------
# BOUNDARY Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
Bmask_zeroL     = np.isfinite(zeroL[0.3])         # Scan for NaN values
BzL             = zeroL[0.3][Bmask_zeroL]          # Remove NaN values from BrO

Bmask_partial1L = np.isfinite(partial1L[0.3])     # Scan for NaN values
Bp1L            = partial1L[0.3][Bmask_partial1L]  # Remove NaN values from BrO

Bmask_partial2L = np.isfinite(partial2L[0.3])     # Scan for NaN values
Bp2L            = partial2L[0.3][Bmask_partial2L]  # Remove NaN values from BrO

Bmask_partial3L = np.isfinite(partial3L[0.3])     # Scan for NaN values
Bp3L            = partial3L[0.3][Bmask_partial3L]  # Remove NaN values from BrO

Bmask_fullL     = np.isfinite(fullL[0.3])         # Scan for NaN values
BfL             = fullL[0.3][Bmask_fullL]          # Remove NaN values from BrO

#-----------------------------------
# BOUNDARY High Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
Bmask_zeroH     = np.isfinite(zeroH[0.3])         # Scan for NaN values
BzH             = zeroH[0.3][Bmask_zeroH]          # Remove NaN values from BrO

Bmask_partial1H = np.isfinite(partial1H[0.3])     # Scan for NaN values
Bp1H            = partial1H[0.3][Bmask_partial1H]  # Remove NaN values from BrO

Bmask_partial2H = np.isfinite(partial2H[0.3])     # Scan for NaN values
Bp2H            = partial2H[0.3][Bmask_partial2H]  # Remove NaN values from BrO

Bmask_partial3H = np.isfinite(partial3H[0.3])     # Scan for NaN values
Bp3H            = partial3H[0.3][Bmask_partial3H]  # Remove NaN values from BrO

Bmask_fullH     = np.isfinite(fullH[0.3])         # Scan for NaN values
BfH             = fullH[0.3][Bmask_fullH]          # Remove NaN values from BrO

#------------------------------------------------------------------------------
# Make a list of the number of values in each distribution

# text to include with label
j1  = 'n = ' 
j1L = '(LWS)\nn = '
j1H = '(HWS)\nn = '

#-----------------------------
# SURFACE Low Wind Speed (<7 m/s)
#-----------------------------
SaL = len(SzL)
#SbL = len(Sp1L)
ScL = len(Sp2L)
SdL = len(Sp3L)
SeL = len(SfL)

SDF1L = [SaL,ScL,SdL,SeL]

#-----------------------------
# SURFACE High Wind Speed (>=7 m/s)
#-----------------------------
SaH = len(SzH)
#SbH = len(Sp1H)
ScH = len(Sp2H)
SdH = len(Sp3H)
SeH = len(SfH)

SDF1H = [SaH,ScH,SdH,SeH]

#-----------------------------
# BOUNDARY Low Wind Speed (<7 m/s)
#-----------------------------
BaL = len(BzL)
#BbL = len(Bp1L)
BcL = len(Bp2L)
BdL = len(Bp3L)
BeL = len(BfL)

BDF1L = [BaL,BcL,BdL,BeL]

#-----------------------------
# BOUNDARY High Wind Speed (>=7 m/s)
#-----------------------------
BaH = len(BzH)
#BbH = len(Bp1H)
BcH = len(Bp2H)
BdH = len(Bp3H)
BeH = len(BfH)

BDF1H = [BaH,BcH,BdH,BeH]

#------------------------------------------------------------------------------
# PLOT GRAPH 1

fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 1
ax1 = plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

#-----------------------------
# BOX PLOT 1 (Low Wind Speed)
c1 = "black"
c2 = "blue"

box1L = ax1.boxplot((SzL * 1e6), positions=[0.8], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

#-----------------------------
# BOX PLOT 3 (Low Wind Speed)
c5 = "black"
c6 = "red"
box3L = ax1.boxplot((Sp2L * 1e6), positions=[1.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3L[item], color=c5)
plt.setp(box3L["boxes"], facecolor=c6)
plt.setp(box3L["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (Low Wind Speed)
c7 = "black"
c8 = "green"
box4L = ax1.boxplot((Sp3L * 1e6), positions=[2.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4L[item], color=c7)
plt.setp(box4L["boxes"], facecolor=c8)
plt.setp(box4L["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (Low Wind Speed)
c9 = "black"
c10 = "purple"
box5L = ax1.boxplot((SfL * 1e6), positions=[3.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5L[item], color=c9)
plt.setp(box5L["boxes"], facecolor=c10)
plt.setp(box5L["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph
for i, v in enumerate(SDF1L):
    t = ax1.text((i)+0.8 ,v/SDF1L[i]-0.75,j1L + str(SDF1L[i]),fontsize=12,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
    
# Format the y-axis
plt.ylim(0,10)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# Format the x-axis
plt.xlim(0,5.5)
plt.xticks([1.0,2.0,3.0,4.0],['None\n(0%)','Partial\n(30-60%)','Partial\n(60-90%)','Full\n(90-100%)'],fontsize=15)

# Add axis labels
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
ax1.set_xlabel('Sea Ice Cover', fontsize=20, labelpad=15)

# Add a legend
lg = ax1.legend([box1L["boxes"][0],box3L["boxes"][0],box4L["boxes"][0],box5L["boxes"][0]],[SDF3L[0],SDF3L[1],SDF3L[2],SDF3L[3]], loc='upper left',bbox_to_anchor=(0.85, 0.98),title='Median \u00B1 MAD',fontsize=15)
lg.get_title().set_fontsize(15)
lg.get_title().set_fontweight('bold')

#-----------------------------------
# High Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 1
ax1 = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

#-----------------------------
# BOX PLOT 1 (High Wind Speed)
c1 = "black"
c2 = "blue"

box1H = ax1.boxplot((SzH * 1e6), positions=[1.2], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

#-----------------------------
# BOX PLOT 3 (High Wind Speed)
c5 = "black"
c6 = "red"
box3H = ax1.boxplot((Sp2H * 1e6), positions=[2.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3H[item], color=c5)
plt.setp(box3H["boxes"], facecolor=c6)
plt.setp(box3H["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (High Wind Speed)
c7 = "black"
c8 = "green"
box4H = ax1.boxplot((Sp3H * 1e6), positions=[3.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4H[item], color=c7)
plt.setp(box4H["boxes"], facecolor=c8)
plt.setp(box4H["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (High Wind Speed)
c9 = "black"
c10 = "purple"
box5H = ax1.boxplot((SfH * 1e6), positions=[4.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5H[item], color=c9)
plt.setp(box5H["boxes"], facecolor=c10)
plt.setp(box5H["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph
for i, v in enumerate(SDF1H):
    t= ax1.text((i)+1.2 ,v/SDF1H[i]-0.75,j1H + str(SDF1H[i]),fontsize=12,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

# Format the y-axis
plt.ylim(0,10)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# Format the x-axis
plt.xlim(0,5.5)
plt.xticks([1.0,2.0,3.0,4.0],['None\n(0%)','Partial\n(30-60%)','Partial\n(60-90%)','Full\n(90-100%)'],fontsize=15)

# Add axis labels
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
ax1.set_xlabel('Sea Ice Cover', fontsize=20, labelpad=15)

## Add a legend
#lg = ax1.legend([box1H["boxes"][0],box3H["boxes"][0],box4H["boxes"][0],box5H["boxes"][0]], [SDF3H[0],SDF3H[1],SDF3H[2],SDF3H[3]], loc='upper left',bbox_to_anchor=(0.85, 0.98),title='Median \u00B1 MAD',fontsize=15)
#lg.get_title().set_fontsize(15)
#lg.get_title().set_fontweight('bold')

#------------------------------------------------------------------------------
# PLOT GRAPH 2

fig2 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# SubPlot 1 (SURFACE LAYER)
#-----------------------------------
ax1 = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

#-----------------------------
# BOX PLOT 1 (Low Wind Speed)
c1 = "black"
c2 = "blue"

box1L = ax1.boxplot((SzL * 1e6), positions=[0.8], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

# BOX PLOT 1 (High Wind Speed)
c1 = "black"
c2 = "red"

box1H = ax1.boxplot((SzH * 1e6), positions=[1.2], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

#-----------------------------
# BOX PLOT 3 (Low Wind Speed)
c5 = "black"
c6 = "blue"
box3L = ax1.boxplot((Sp2L * 1e6), positions=[1.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3L[item], color=c5)
plt.setp(box3L["boxes"], facecolor=c6)
plt.setp(box3L["fliers"], markeredgecolor=c5)

# BOX PLOT 3 (High Wind Speed)
c5 = "black"
c6 = "red"
box3H = ax1.boxplot((Sp2H * 1e6), positions=[2.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3H[item], color=c5)
plt.setp(box3H["boxes"], facecolor=c6)
plt.setp(box3H["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (Low Wind Speed)
c7 = "black"
c8 = "blue"
box4L = ax1.boxplot((Sp3L * 1e6), positions=[2.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4L[item], color=c7)
plt.setp(box4L["boxes"], facecolor=c8)
plt.setp(box4L["fliers"], markeredgecolor=c7)

# BOX PLOT 4 (High Wind Speed)
c7 = "black"
c8 = "red"
box4H = ax1.boxplot((Sp3H * 1e6), positions=[3.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4H[item], color=c7)
plt.setp(box4H["boxes"], facecolor=c8)
plt.setp(box4H["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (Low Wind Speed)
c9 = "black"
c10 = "blue"
box5L = ax1.boxplot((SfL * 1e6), positions=[3.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5L[item], color=c9)
plt.setp(box5L["boxes"], facecolor=c10)
plt.setp(box5L["fliers"], markeredgecolor=c9)

# BOX PLOT 5 (High Wind Speed)
c9 = "black"
c10 = "red"
box5H = ax1.boxplot((SfH * 1e6), positions=[4.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5H[item], color=c9)
plt.setp(box5H["boxes"], facecolor=c10)
plt.setp(box5H["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph (no of variables)

# Low wind speed
for i, v in enumerate(SDF1L):
    t = ax1.text((i)+0.8 ,v/SDF1L[i]-2.5,j1 + str(SDF1L[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

# High wind speed
for i, v in enumerate(SDF1H):
    t= ax1.text((i)+1.2 ,v/SDF1H[i]-2.5,j1 + str(SDF1H[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

#-----------------------------
# Add values to the graph (median and mad)

# Low wind speed
for i, v in enumerate(SMedianL):
    t = ax1.text((i)+0.8 ,v/SMedianL[i]-1.65,j4 + str("%4.2f"%(SMedianL[i])) + u" \u00B1 " + str("%4.2f"%(SMADH[i])),fontsize=11,color='blue',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

# High wind speed
for i, v in enumerate(SMedianH):
    t = ax1.text((i)+1.2 ,v/SMedianH[i]-1.65,j4 + str("%4.2f"%(SMedianH[i])) + u" \u00B1 " + str("%4.2f"%(SMADH[i])),fontsize=11,color='red',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
  
# Format the y-axis
plt.ylim(-1.9,10)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# Format the x-axis
plt.xlim(0.4,4.6)
plt.xticks([1.0,2.0,3.0,4.0],['None\n(0%)','Partial\n(30-60%)','Partial\n(60-90%)','Full\n(90-100%)'],fontsize=15)

# Add axis labels
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
ax1.set_xlabel('Sea Ice Cover', fontsize=20, labelpad=15)

# Plot the title
plt.title('[0-100m ASL]', fontsize=25, pad=10)

## Add a legend
#lg = ax1.legend([box1L["boxes"][0],box1H["boxes"][0]], ["Low (<7 m/s)","High (>7 m/s)"], loc='upper left',bbox_to_anchor=(0.82, 1.36),title='Wind speed',fontsize=15)
#lg.get_title().set_fontsize(15)
#lg.get_title().set_fontweight('bold')

#-----------------------------------
# SubPlot 1 (BOUNDARY LAYER)
#-----------------------------------
ax1 = plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

#-----------------------------
# BOX PLOT 1 (Low Wind Speed)
c1 = "black"
c2 = "blue"

box1L = ax1.boxplot((BzL * 1e6), positions=[0.8], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

# BOX PLOT 1 (High Wind Speed)
c1 = "black"
c2 = "red"

box1H = ax1.boxplot((BzH * 1e6), positions=[1.2], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

#-----------------------------
# BOX PLOT 3 (Low Wind Speed)
c5 = "black"
c6 = "blue"
box3L = ax1.boxplot((Bp2L * 1e6), positions=[1.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3L[item], color=c5)
plt.setp(box3L["boxes"], facecolor=c6)
plt.setp(box3L["fliers"], markeredgecolor=c5)

# BOX PLOT 3 (High Wind Speed)
c5 = "black"
c6 = "red"
box3H = ax1.boxplot((Bp2H * 1e6), positions=[2.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3H[item], color=c5)
plt.setp(box3H["boxes"], facecolor=c6)
plt.setp(box3H["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (Low Wind Speed)
c7 = "black"
c8 = "blue"
box4L = ax1.boxplot((Bp3L * 1e6), positions=[2.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4L[item], color=c7)
plt.setp(box4L["boxes"], facecolor=c8)
plt.setp(box4L["fliers"], markeredgecolor=c7)

# BOX PLOT 4 (High Wind Speed)
c7 = "black"
c8 = "red"
box4H = ax1.boxplot((Bp3H * 1e6), positions=[3.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4H[item], color=c7)
plt.setp(box4H["boxes"], facecolor=c8)
plt.setp(box4H["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (Low Wind Speed)
c9 = "black"
c10 = "blue"
box5L = ax1.boxplot((BfL * 1e6), positions=[3.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5L[item], color=c9)
plt.setp(box5L["boxes"], facecolor=c10)
plt.setp(box5L["fliers"], markeredgecolor=c9)

# BOX PLOT 5 (High Wind Speed)
c9 = "black"
c10 = "red"
box5H = ax1.boxplot((BfH * 1e6), positions=[4.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5H[item], color=c9)
plt.setp(box5H["boxes"], facecolor=c10)
plt.setp(box5H["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph (no of variables)

# Low wind speed
for i, v in enumerate(BDF1L):
    t = ax1.text((i)+0.8 ,v/BDF1L[i]-2.5,j1 + str(BDF1L[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

# High wind speed
for i, v in enumerate(BDF1H):
    t= ax1.text((i)+1.2 ,v/BDF1H[i]-2.5,j1 + str(BDF1H[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

#-----------------------------
# Add values to the graph (median and mad)

# Low wind speed
for i, v in enumerate(BMedianL):
    t = ax1.text((i)+0.8 ,v/BMedianL[i]-1.65,j4 + str("%4.2f"%(BMedianL[i])) + u" \u00B1 " + str("%4.2f"%(BMADH[i])),fontsize=11,color='blue',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

# High wind speed
for i, v in enumerate(BMedianH):
    t = ax1.text((i)+1.2 ,v/BMedianH[i]-1.65,j4 + str("%4.2f"%(BMedianH[i])) + u" \u00B1 " + str("%4.2f"%(BMADH[i])),fontsize=11,color='red',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
  
# Format the y-axis
plt.ylim(-1.9,10)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# Format the x-axis
plt.xlim(0.4,4.6)
#plt.xticks([1.0,2.0,3.0,4.0],['None\n(0%)','Partial\n(30-60%)','Partial\n(60-90%)','Full\n(90-100%)'],fontsize=15)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

# Add axis labels
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
#ax1.set_xlabel('Sea Ice Cover', fontsize=20, labelpad=15)

# Plot the title
plt.title('[100-300m ASL]', fontsize=25, pad=10)

# Add a legend
lg = ax1.legend([box1L["boxes"][0],box1H["boxes"][0]], ["Low (<7 m/s)","High (>7 m/s)"], loc='upper left',bbox_to_anchor=(0.82, 1.36),title='Wind speed',fontsize=15)
lg.get_title().set_fontsize(15)
lg.get_title().set_fontweight('bold')

#------------------------------------------------------------------------------
# PLOT GRAPH 3

fig3 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# SubPlot 1 (LWS)
#-----------------------------------
ax1 = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax1.scatter(SI_LWS, BrO_LWS, edgecolors='none', marker='o', c='blue', label='LWS')
#ax1.scatter(SI_HWS, BrO_HWS, edgecolors='none', marker='o', c='red',  label='HWS')

# Plot the regression line
line1, = plt.plot(SI_LWS, interceptD_LWS + slopeD_LWS * SI_LWS, color='blue')
#line2, = plt.plot(SI_HWS, interceptD_HWS + slopeD_HWS * SI_HWS, color='red')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_xlim(-1, 101.0)
ax1.xaxis.labelpad = 10

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0.1, 22.5)
ax1.yaxis.labelpad = 10

# Plot the axis labels
ax1.set_ylabel('BrO (pptv)', fontsize=20)
ax1.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax1.legend(bbox_to_anchor=(0.86, 0.95), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax1.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD_LWS))+" $\pm$"+str("%7.4f"%(std_errD_LWS))+" %, r: "+str("%7.4f"%(rD_LWS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# SubPlot 2 (HWS)
#-----------------------------------
ax1 = plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
#ax1.scatter(SI_LWS, BrO_LWS, edgecolors='none', marker='o', c='blue', label='LWS')
ax1.scatter(SI_HWS, BrO_HWS, edgecolors='none', marker='o', c='red',  label='HWS')

# Plot the regression line
#line1, = plt.plot(SI_LWS, interceptD_LWS + slopeD_LWS * SI_LWS, color='blue')
line2, = plt.plot(SI_HWS, interceptD_HWS + slopeD_HWS * SI_HWS, color='red')

# Format x-axis
ax1.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_xlim(-1, 101.0)
ax1.xaxis.labelpad = 10

# Format y-axis 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax1.set_ylim(0.1, 22.5)
ax1.yaxis.labelpad = 10

# Plot the axis labels
ax1.set_ylabel('BrO (pptv)', fontsize=20)
ax1.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
legend = ax1.legend(bbox_to_anchor=(0.86, 0.95), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax1.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD_HWS))+" $\pm$"+str("%7.4f"%(std_errD_HWS))+" %, r: "+str("%7.4f"%(rD_HWS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)
