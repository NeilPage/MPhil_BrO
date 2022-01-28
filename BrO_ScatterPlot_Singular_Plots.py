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
V1_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv')
V1_17_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv')
V1_17_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv')
V1_17_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv')

# V2_17 (2017-18)
V2_17_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_17_Data.csv',header=0,encoding = 'unicode_escape')
V2_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv')
V2_17_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv')
V2_17_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv')
V2_17_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv')

# V3_17 (2017-18)
V3_17_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_17_Data.csv',header=0,encoding = 'unicode_escape')
V3_17_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv')
V3_17_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv')
V3_17_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv')
V3_17_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv')

# V1_18 (2018-19)
V1_18_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_18_Data.csv',header=0,encoding = 'unicode_escape')
V1_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv')
V1_18_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv')
V1_18_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv')
V1_18_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V1_O3_1min.csv')

# V2_18 (2018-19)
V2_18_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_18_Data.csv',header=0,encoding = 'unicode_escape')
V2_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv')
V2_18_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv')
V2_18_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv')
V2_18_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V2_O3_1min.csv')

# V3_18 (2018-19)
V3_18_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_18_Data.csv',header=0,encoding = 'unicode_escape')
V3_18_Met   = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv')
V3_18_SI    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv')
V3_18_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv')
V3_18_O3    = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V3_O3_1min.csv')

# SIPEXII 2012
SIPEXII_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/SIPEXII_Data.csv',header=0,encoding = 'unicode_escape')
SIPEXII_Met = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_underway_60.csv') #SIPEXII_underway_60.csv') 
SIPEXII_SI  = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv')
SIPEXII_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_QAQC_2012.csv')
SIPEXII_O3  = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv')

#------------------------------------------------------------------------------
# Set the date

# V1_17 (2017-18)
V1_17_BrO['DateTime']   = pd.to_datetime(V1_17_BrO['DateTime'], dayfirst=True)
V1_17_Met['DateTime']   = pd.to_datetime(V1_17_Met['DateTime'], dayfirst=True)
V1_17_SI['DateTime']    = pd.to_datetime(V1_17_SI['DateTime'],  dayfirst=True)
V1_17_Hg['DateTime']    = pd.to_datetime(V1_17_Hg['DateTime'],  dayfirst=True)
V1_17_O3['DateTime']    = pd.to_datetime(V1_17_O3['DateTime'],  dayfirst=True)

# V2_17 (2017-18)
V2_17_BrO['DateTime']   = pd.to_datetime(V2_17_BrO['DateTime'], dayfirst=True)
V2_17_Met['DateTime']   = pd.to_datetime(V2_17_Met['DateTime'], dayfirst=True)
V2_17_SI['DateTime']    = pd.to_datetime(V2_17_SI['DateTime'],  dayfirst=True)
V2_17_Hg['DateTime']    = pd.to_datetime(V2_17_Hg['DateTime'],  dayfirst=True)
V2_17_O3['DateTime']    = pd.to_datetime(V2_17_O3['DateTime'],  dayfirst=True)

# V3_17 (2017-18)
V3_17_BrO['DateTime']   = pd.to_datetime(V3_17_BrO['DateTime'], dayfirst=True)
V3_17_Met['DateTime']   = pd.to_datetime(V3_17_Met['DateTime'], dayfirst=True)
V3_17_SI['DateTime']    = pd.to_datetime(V3_17_SI['DateTime'],  dayfirst=True)
V3_17_Hg['DateTime']    = pd.to_datetime(V3_17_Hg['DateTime'],  dayfirst=True)
V3_17_O3['DateTime']    = pd.to_datetime(V3_17_O3['DateTime'],  dayfirst=True)

# V1_18 (2018-19)
V1_18_BrO['DateTime']   = pd.to_datetime(V1_18_BrO['DateTime'], dayfirst=True)
V1_18_Met['DateTime']   = pd.to_datetime(V1_18_Met['DateTime'], dayfirst=True)
V1_18_SI['DateTime']    = pd.to_datetime(V1_18_SI['DateTime'],  dayfirst=True)
V1_18_Hg['DateTime']    = pd.to_datetime(V1_18_Hg['DateTime'],  dayfirst=True)
V1_18_O3['DateTime']    = pd.to_datetime(V1_18_O3['DateTime'],  dayfirst=True)

# V2_18 (2018-19)
V2_18_BrO['DateTime']   = pd.to_datetime(V2_18_BrO['DateTime'], dayfirst=True)
V2_18_Met['DateTime']   = pd.to_datetime(V2_18_Met['DateTime'], dayfirst=True)
V2_18_SI['DateTime']    = pd.to_datetime(V2_18_SI['DateTime'],  dayfirst=True)
V2_18_Hg['DateTime']    = pd.to_datetime(V2_18_Hg['DateTime'],  dayfirst=True)
V2_18_O3['DateTime']    = pd.to_datetime(V2_18_O3['DateTime'],  dayfirst=True)

# V3_18 (2018-19)
V3_18_BrO['DateTime']   = pd.to_datetime(V3_18_BrO['DateTime'], dayfirst=True)
V3_18_Met['DateTime']   = pd.to_datetime(V3_18_Met['DateTime'], dayfirst=True)
V3_18_SI['DateTime']    = pd.to_datetime(V3_18_SI['DateTime'],  dayfirst=True)
V3_18_Hg['DateTime']    = pd.to_datetime(V3_18_Hg['DateTime'],  dayfirst=True)
V3_18_O3['DateTime']    = pd.to_datetime(V3_18_O3['DateTime'],  dayfirst=True)

# SIPEXII (2012)
SIPEXII_BrO['DateTime'] = pd.to_datetime(SIPEXII_BrO['DateTime'], dayfirst=True)
SIPEXII_Met['DateTime'] = pd.to_datetime(SIPEXII_Met['DateTime'], dayfirst=True)
SIPEXII_SI['DateTime']  = pd.to_datetime(SIPEXII_SI['DateTime'],  dayfirst=True)
SIPEXII_Hg['DateTime']  = pd.to_datetime(SIPEXII_Hg['DateTime'],  dayfirst=True)
SIPEXII_O3['DateTime']  = pd.to_datetime(SIPEXII_O3['DateTime'],  dayfirst=True)

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

# SIPEXII (2012)
SIPEXII_BrO = SIPEXII_BrO.set_index('DateTime')
SIPEXII_Met = SIPEXII_Met.set_index('DateTime')
SIPEXII_SI  = SIPEXII_SI.set_index('DateTime')
SIPEXII_Hg  = SIPEXII_Hg.set_index('DateTime')
SIPEXII_O3  = SIPEXII_O3.set_index('DateTime')

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

# SIPEXII (2012)
SIPEXII_Met = SIPEXII_Met.resample('20T').mean()
SIPEXII_SI  = SIPEXII_SI.resample('20T').mean()
SIPEXII_Hg  = SIPEXII_Hg.resample('20T').mean()
SIPEXII_O3  = SIPEXII_O3.resample('20T').mean()

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

# SIPEXII (2012)
SIPEXII_Met.index = SIPEXII_Met.index - pd.Timedelta(minutes=10)
SIPEXII_SI.index  = SIPEXII_SI.index  - pd.Timedelta(minutes=10)
SIPEXII_Hg.index  = SIPEXII_Hg.index  - pd.Timedelta(minutes=10)
SIPEXII_O3.index  = SIPEXII_O3.index  - pd.Timedelta(minutes=10)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

# V1_17 (07:00 to 18:00)
start_time = '07:00:00'
end_time   = '18:00:00'
Midday     = (V1_17_BrO['Time'] >= start_time) & (V1_17_BrO['Time'] < end_time)
V1_17_MM   = V1_17_BrO[Midday]

# V2_17 (07:00 to 18:00)
start_time = '07:00:00'
end_time   = '18:00:00'
Midday     = (V2_17_BrO['Time'] >= start_time) & (V2_17_BrO['Time'] < end_time)
V2_17_MM   = V2_17_BrO[Midday]

# V3_17 (07:00 to 18:00)
start_time = '07:00:00'
end_time   = '18:00:00'
Midday     = (V3_17_BrO['Time'] >= start_time) & (V3_17_BrO['Time'] < end_time)
V3_17_MM   = V3_17_BrO[Midday]

# V1_18 (07:00 to 18:00)
start_time = '07:00:00'
end_time   = '18:00:00'
Midday     = (V1_18_BrO['Time'] >= start_time) & (V1_18_BrO['Time'] < end_time)
V1_18_MM   = V1_18_BrO[Midday]

# V2_18 (07:00 to 18:00)
start_time = '07:00:00'
end_time   = '18:00:00'
Midday     = (V2_18_BrO['Time'] >= start_time) & (V2_18_BrO['Time'] < end_time)
V2_18_MM   = V2_18_BrO[Midday]

# V3_18 (07:00 to 18:00)
start_time = '07:00:00'
end_time   = '18:00:00'
Midday     = (V3_18_BrO['Time'] >= start_time) & (V3_18_BrO['Time'] < end_time)
V3_18_MM   = V3_18_BrO[Midday]

# SIPEXII (07:00 to 18:00)
start_time = '07:00:00'
end_time   = '18:00:00'
Midday     = (SIPEXII_BrO['Time'] >= start_time) & (SIPEXII_BrO['Time'] < end_time)
SIPEXII_MM = SIPEXII_BrO[Midday]

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

# SIPEXII (2012)
SIPEXIIF = (SIPEXII_MM['Filter'] < 0.6)
SIPEXIIT = SIPEXII_MM[SIPEXIIF]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# V1_17 Davis (14-22 Nov 2017)
start_date   = '2017-11-14'
end_date     = '2017-11-23'
Davis        = (V1_17T.index >= start_date) & (V1_17T.index < end_date)
V1_17T       = V1_17T[Davis]

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1  = '2017-12-21'
end_date1    = '2017-12-23'
start_date2  = '2017-12-26'
end_date2    = '2018-01-6'
Casey1       = (V2_17T.index >= start_date1) & (V2_17T.index < end_date1)
Casey2       = (V2_17T.index >= start_date2) & (V2_17T.index < end_date2)
V2_17_Casey1 = V2_17T[Casey1]
V2_17_Casey2 = V2_17T[Casey2]
V2_17T       = pd.concat([V2_17_Casey1,V2_17_Casey2], axis =0)

# V3_17 Mawson (1-17 Feb 2018)
start_date   = '2018-02-01'
end_date     = '2018-02-18'
Mawson       = (V3_17T.index >= start_date) & (V3_17T.index < end_date)
V3_17T       = V3_17T[Mawson]

# V1_18 Davis (7-15 Nov 2018)
start_date   = '2018-11-07'
end_date     = '2018-11-16'
Davis        = (V1_18T.index >= start_date) & (V1_18T.index < end_date)
V1_18T       = V1_18T[Davis]

# V2_18 Casey (15-30 Dec 2018)
start_date   = '2018-12-15'
end_date     = '2018-12-31'
Casey        = (V2_18T.index >= start_date) & (V2_18T.index < end_date)
V2_18T       = V2_18T[Casey]

# V3_18 Mawson (30 Jan - 9 Feb 2019)
start_date   = '2019-01-30'
end_date     = '2019-02-10'
Mawson       = (V3_18T.index >= start_date) & (V3_18T.index < end_date)
V3_18T       = V3_18T[Mawson]

# SIPEXII (23 Sep to 11 Nov 2012)
start_date   = '2012-09-23'
end_date     = '2012-11-11'
SIPEX        = (SIPEXIIT.index >= start_date) & (SIPEXIIT.index < end_date)
SIPEXIIT     = SIPEXIIT[SIPEX]

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

# V1_17 (2017-18)
D1_V1_17   = pd.merge(left=V1_17T,    right=V1_17_Met,    how='left', left_index=True, right_index=True)
D2_V1_17   = pd.merge(left=D1_V1_17,   right=V1_17_SI,    how='left', left_index=True, right_index=True)
D3_V1_17   = pd.merge(left=D2_V1_17,   right=V1_17_Hg,    how='left', left_index=True, right_index=True)
D4_V1_17   = pd.merge(left=D3_V1_17,   right=V1_17_O3,    how='left', left_index=True, right_index=True)

# V2_17 (2017-18)
D1_V2_17   = pd.merge(left=V2_17T,     right=V2_17_Met,   how='left', left_index=True, right_index=True)
D2_V2_17   = pd.merge(left=D1_V2_17,   right=V2_17_SI,    how='left', left_index=True, right_index=True)
D3_V2_17   = pd.merge(left=D2_V2_17,   right=V2_17_Hg,    how='left', left_index=True, right_index=True)
D4_V2_17   = pd.merge(left=D3_V2_17,   right=V2_17_O3,    how='left', left_index=True, right_index=True)

# V3_17 (2017-18)
D1_V3_17   = pd.merge(left=V3_17T,     right=V3_17_Met,   how='left', left_index=True, right_index=True)
D2_V3_17   = pd.merge(left=D1_V3_17,   right=V3_17_SI,    how='left', left_index=True, right_index=True)
D3_V3_17   = pd.merge(left=D2_V3_17,   right=V3_17_Hg,    how='left', left_index=True, right_index=True)
D4_V3_17   = pd.merge(left=D3_V3_17,   right=V3_17_O3,    how='left', left_index=True, right_index=True)

# V1_18 (2018-19)
D1_V1_18   = pd.merge(left=V1_18T,     right=V1_18_Met,   how='left', left_index=True, right_index=True)
D2_V1_18   = pd.merge(left=D1_V1_18,   right=V1_18_SI,    how='left', left_index=True, right_index=True)
D3_V1_18   = pd.merge(left=D2_V1_18,   right=V1_18_Hg,    how='left', left_index=True, right_index=True)
D4_V1_18   = pd.merge(left=D3_V1_18,   right=V1_18_O3,    how='left', left_index=True, right_index=True)

# V2_18 (2018-19)
D1_V2_18   = pd.merge(left=V2_18T,     right=V2_18_Met,   how='left', left_index=True, right_index=True)
D2_V2_18   = pd.merge(left=D1_V2_18,   right=V2_18_SI,    how='left', left_index=True, right_index=True)
D3_V2_18   = pd.merge(left=D2_V2_18,   right=V2_18_Hg,    how='left', left_index=True, right_index=True)
D4_V2_18   = pd.merge(left=D3_V2_18,   right=V2_18_O3,    how='left', left_index=True, right_index=True)

# V3_18 (2018-19)
D1_V3_18   = pd.merge(left=V3_18T,     right=V3_18_Met,   how='left', left_index=True, right_index=True)
D2_V3_18   = pd.merge(left=D1_V3_18,   right=V3_18_SI,    how='left', left_index=True, right_index=True)
D3_V3_18   = pd.merge(left=D2_V3_18,   right=V3_18_Hg,    how='left', left_index=True, right_index=True)
D4_V3_18   = pd.merge(left=D3_V3_18,   right=V3_18_O3,    how='left', left_index=True, right_index=True)

# SIPEXII (2012)
D1_SIPEXII = pd.merge(left=SIPEXIIT,   right=SIPEXII_Met, how='left', left_index=True, right_index=True)
D2_SIPEXII = pd.merge(left=D1_SIPEXII, right=SIPEXII_SI,  how='left', left_index=True, right_index=True)
D3_SIPEXII = pd.merge(left=D2_SIPEXII, right=SIPEXII_Hg,  how='left', left_index=True, right_index=True)
D4_SIPEXII = pd.merge(left=D3_SIPEXII, right=SIPEXII_O3,  how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Calculate the Wind Speed average

WS_s_V1_17           = np.array(D4_V1_17['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17           = np.array(D4_V1_17['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
D4_V1_17['WS_Avg']   = (WS_s_V1_17 + WS_p_V1_17)/2 # Average the wind speed for port and starboard

WS_s_V2_17           = np.array(D4_V2_17['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17           = np.array(D4_V2_17['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
D4_V2_17['WS_Avg']   = (WS_s_V2_17 + WS_p_V2_17)/2 # Average the wind speed for port and starboard

WS_s_V3_17           = np.array(D4_V3_17['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17           = np.array(D4_V3_17['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
D4_V3_17['WS_Avg']   = (WS_s_V3_17 + WS_p_V3_17)/2 # Average the wind speed for port and starboard

WS_s_V1_18           = np.array(D4_V1_18['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18           = np.array(D4_V1_18['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
D4_V1_18['WS_Avg']   = (WS_s_V1_18 + WS_p_V1_18)/2 # Average the wind speed for port and starboard

WS_s_V2_18           = np.array(D4_V2_18['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18           = np.array(D4_V2_18['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
D4_V2_18['WS_Avg']   = (WS_s_V2_18 + WS_p_V2_18)/2 # Average the wind speed for port and starboard

WS_s_V3_18           = np.array(D4_V3_18['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18           = np.array(D4_V3_18['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
D4_V3_18['WS_Avg']   = (WS_s_V3_18 + WS_p_V3_18)/2 # Average the wind speed for port and starboard

WS_s_SIPEXII         = np.array(D4_SIPEXII['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXII         = np.array(D4_SIPEXII['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
D4_SIPEXII['WS_Avg'] = (WS_s_SIPEXII + WS_p_SIPEXII)/2 # Average the wind speed for port and starboard

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

SIPEXII_LWS = (D4_SIPEXII['WS_Avg'] <= 7)
D4_SIPEXIIL = D4_SIPEXII[SIPEXII_LWS]

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

SIPEXII_HWS = (D4_SIPEXII['WS_Avg'] > 7)
D4_SIPEXIIH = D4_SIPEXII[SIPEXII_HWS]

#------------------------------------------------------------------------------
# Define the variables
#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrO_V1_17L   = np.array(D4_V1_17L['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17L   = np.array(D4_V2_17L['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17L   = np.array(D4_V3_17L['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18L   = np.array(D4_V1_18L['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18L   = np.array(D4_V2_18L['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18L   = np.array(D4_V3_18L['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_SIPEXIIL = np.array(D4_SIPEXIIL['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv

#--------------------------------
# O3 (ppb)
O3_V1_17L   = np.array(D4_V1_17L['O3_(ppb)_y']) # O3 (ppb)
O3_V2_17L   = np.array(D4_V2_17L['O3_(ppb)_y']) # O3 (ppb)
O3_V3_17L   = np.array(D4_V3_17L['O3_(ppb)_y']) # O3 (ppb)
O3_V1_18L   = np.array(D4_V1_18L['O3']) # O3 (ppb)
O3_V2_18L   = np.array(D4_V2_18L['O3']) # O3 (ppb)
O3_V3_18L   = np.array(D4_V3_18L['O3']) # O3 (ppb)
O3_SIPEXIIL = np.array(D4_SIPEXIIL['O3_(ppb)_y']) # O3 (ppb)

#--------------------------------
# Solar Radiation (W/m2)
Sol_s_V1_17L           = np.array(D4_V1_17L['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V1_17L           = np.array(D4_V1_17L['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V1_17L['MeanSol']   = D4_V1_17L[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_17L             = np.array(D4_V1_17L['MeanSol'])

Sol_s_V2_17L           = np.array(D4_V2_17L['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V2_17L           = np.array(D4_V2_17L['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V2_17L['MeanSol']   = D4_V2_17L[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_17L             = np.array(D4_V2_17L['MeanSol'])

Sol_s_V3_17L           = np.array(D4_V3_17L['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V3_17L           = np.array(D4_V3_17L['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V3_17L['MeanSol']   = D4_V3_17L[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_17L             = np.array(D4_V3_17L['MeanSol'])

Sol_s_V1_18L           = np.array(D4_V1_18L['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V1_18L           = np.array(D4_V1_18L['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V1_18L['MeanSol']   = D4_V1_18L[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_18L             = np.array(D4_V1_18L['MeanSol'])

Sol_s_V2_18L           = np.array(D4_V2_18L['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V2_18L           = np.array(D4_V2_18L['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V2_18L['MeanSol']   = D4_V2_18L[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_18L             = np.array(D4_V2_18L['MeanSol'])

Sol_s_V3_18L           = np.array(D4_V3_18L['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V3_18L           = np.array(D4_V3_18L['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V3_18L['MeanSol']   = D4_V3_18L[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_18L             = np.array(D4_V3_18L['MeanSol'])

Sol_s_SIPEXIIL         = np.array(D4_SIPEXIIL['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_SIPEXIIL         = np.array(D4_SIPEXIIL['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_SIPEXIIL['MeanSol'] = D4_SIPEXIIL[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_SIPEXIIL           = np.array(D4_SIPEXIIL['MeanSol'])

#--------------------------------
# Temperature (C)

Temp_s_V1_17L           = np.array(D4_V1_17L['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V1_17L           = np.array(D4_V1_17L['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V1_17L['MeanTemp']   = D4_V1_17L[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_17L             = np.array(D4_V1_17L['MeanTemp'])

Temp_s_V2_17L           = np.array(D4_V2_17L['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V2_17L           = np.array(D4_V2_17L['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V2_17L['MeanTemp']   = D4_V2_17L[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_17L             = np.array(D4_V2_17L['MeanTemp'])

Temp_s_V3_17L           = np.array(D4_V3_17L['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V3_17L           = np.array(D4_V3_17L['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V3_17L['MeanTemp']   = D4_V3_17L[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_17L             = np.array(D4_V3_17L['MeanTemp'])

Temp_s_V1_18L           = np.array(D4_V1_18L['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V1_18L           = np.array(D4_V1_18L['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V1_18L['MeanTemp']   = D4_V1_18L[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_18L             = np.array(D4_V1_18L['MeanTemp'])

Temp_s_V2_18L           = np.array(D4_V2_18L['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V2_18L           = np.array(D4_V2_18L['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V2_18L['MeanTemp']   = D4_V2_18L[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_18L             = np.array(D4_V2_18L['MeanTemp'])

Temp_s_V3_18L           = np.array(D4_V3_18L['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V3_18L           = np.array(D4_V3_18L['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V3_18L['MeanTemp']   = D4_V3_18L[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_18L             = np.array(D4_V3_18L['MeanTemp'])

Temp_s_SIPEXIIL         = np.array(D4_SIPEXIIL['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_SIPEXIIL         = np.array(D4_SIPEXIIL['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_SIPEXIIL['MeanTemp'] = D4_SIPEXIIL[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_SIPEXIIL           = np.array(D4_SIPEXIIL['MeanTemp'])

#--------------------------------
# Wind Direction

WD_s_V1_17L   = np.array(D4_V1_17L['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V1_17L   = np.array(D4_V1_17L['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V2_17L   = np.array(D4_V2_17L['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V2_17L   = np.array(D4_V2_17L['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V3_17L   = np.array(D4_V3_17L['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V3_17L   = np.array(D4_V3_17L['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V1_18L   = np.array(D4_V1_18L['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V1_18L   = np.array(D4_V1_18L['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V2_18L   = np.array(D4_V2_18L['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V2_18L   = np.array(D4_V2_18L['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V3_18L   = np.array(D4_V3_18L['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V3_18L   = np.array(D4_V3_18L['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_SIPEXIIL = np.array(D4_SIPEXIIL['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_SIPEXIIL = np.array(D4_SIPEXIIL['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

#--------------------------------
# Wind Speed

WS_s_V1_17L   = np.array(D4_V1_17L['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17L   = np.array(D4_V1_17L['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
WS_V1_17L     = (WS_s_V1_17L + WS_p_V1_17L)/2 # Average the wind speed for port and starboard

WS_s_V2_17L   = np.array(D4_V2_17L['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17L   = np.array(D4_V2_17L['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
WS_V2_17L     = (WS_s_V2_17L + WS_p_V2_17L)/2 # Average the wind speed for port and starboard

WS_s_V3_17L   = np.array(D4_V3_17L['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17L   = np.array(D4_V3_17L['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
WS_V3_17L     = (WS_s_V3_17L + WS_p_V3_17L)/2 # Average the wind speed for port and starboard

WS_s_V1_18L   = np.array(D4_V1_18L['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18L   = np.array(D4_V1_18L['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
WS_V1_18L     = (WS_s_V1_18L + WS_p_V1_18L)/2 # Average the wind speed for port and starboard

WS_s_V2_18L   = np.array(D4_V2_18L['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18L   = np.array(D4_V2_18L['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
WS_V2_18L     = (WS_s_V2_18L + WS_p_V2_18L)/2 # Average the wind speed for port and starboard

WS_s_V3_18L   = np.array(D4_V3_18L['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18L   = np.array(D4_V3_18L['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
WS_V3_18L     = (WS_s_V3_18L + WS_p_V3_18L)/2 # Average the wind speed for port and starboard

WS_s_SIPEXIIL = np.array(D4_SIPEXIIL['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXIIL = np.array(D4_SIPEXIIL['WND_SPD_PORT_CORR_KNOT_y'])  * 0.514444444 # Convert from knots to m/s
WS_SIPEXIIL   = (WS_s_SIPEXIIL + WS_p_SIPEXIIL)/2 # Average the wind speed for port and starboard

#--------------------------------
# Vector Mean Wind Direction

WD_vect_V1_17L   = ((WD_s_V1_17L   * WS_s_V1_17L)   / (WS_s_V1_17L   + WS_p_V1_17L))   + ((WD_p_V1_17L   * WS_p_V1_17L)   / (WS_s_V1_17L   + WS_p_V1_17L)) # Calculate the vector mean wind direction
WD_vect_V2_17L   = ((WD_s_V2_17L   * WS_s_V2_17L)   / (WS_s_V2_17L   + WS_p_V2_17L))   + ((WD_p_V2_17L   * WS_p_V2_17L)   / (WS_s_V2_17L   + WS_p_V2_17L)) # Calculate the vector mean wind direction
WD_vect_V3_17L   = ((WD_s_V3_17L   * WS_s_V3_17L)   / (WS_s_V3_17L   + WS_p_V3_17L))   + ((WD_p_V3_17L   * WS_p_V3_17L)   / (WS_s_V3_17L   + WS_p_V3_17L)) # Calculate the vector mean wind direction
WD_vect_V1_18L   = ((WD_s_V1_18L   * WS_s_V1_18L)   / (WS_s_V1_18L   + WS_p_V1_18L))   + ((WD_p_V1_18L   * WS_p_V1_18L)   / (WS_s_V1_18L   + WS_p_V1_18L)) # Calculate the vector mean wind direction
WD_vect_V2_18L   = ((WD_s_V2_18L   * WS_s_V2_18L)   / (WS_s_V2_18L   + WS_p_V2_18L))   + ((WD_p_V2_18L   * WS_p_V2_18L)   / (WS_s_V2_18L   + WS_p_V2_18L)) # Calculate the vector mean wind direction
WD_vect_V3_18L   = ((WD_s_V3_18L   * WS_s_V3_18L)   / (WS_s_V3_18L   + WS_p_V3_18L))   + ((WD_p_V3_18L   * WS_p_V3_18L)   / (WS_s_V3_18L   + WS_p_V3_18L)) # Calculate the vector mean wind direction
WD_vect_SIPEXIIL = ((WD_s_SIPEXIIL * WS_s_SIPEXIIL) / (WS_s_SIPEXIIL + WS_p_SIPEXIIL)) + ((WD_p_SIPEXIIL * WS_p_SIPEXIIL) / (WS_s_SIPEXIIL + WS_p_SIPEXIIL)) # Calculate the vector mean wind direction

#--------------------------------
# Hg0

Hg0_V1_17L   = np.array(D4_V1_17L['ng/m3_y']) # Hg0
Hg0_V2_17L   = np.array(D4_V2_17L['ng/m3_y']) # Hg0
Hg0_V3_17L   = np.array(D4_V3_17L['ng/m3_y']) # Hg0
Hg0_V1_18L   = np.array(D4_V1_18L['ng/m3_y']) # Hg0
Hg0_V2_18L   = np.array(D4_V2_18L['ng/m3_y']) # Hg0
Hg0_V3_18L   = np.array(D4_V3_18L['ng/m3_y']) # Hg0
Hg0_SIPEXIIL = np.array(D4_SIPEXIIL['ng/m3_y']) # Hg0

#--------------------------------
# Sea Ice Concentration

SI_V1_17L   = np.array(D4_V1_17L['Sea_Ice_Conc'])*100
SI_V2_17L   = np.array(D4_V2_17L['Sea_Ice_Conc'])*100
SI_V3_17L   = np.array(D4_V3_17L['Sea_Ice_Conc'])*100
SI_V1_18L   = np.array(D4_V1_18L['Sea_Ice_Conc'])*100
SI_V2_18L   = np.array(D4_V2_18L['Sea_Ice_Conc'])*100
SI_V3_18L   = np.array(D4_V3_18L['Sea_Ice_Conc'])*100
SI_SIPEXIIL = np.array(D4_SIPEXIIL['Sea_Ice_Conc'])*100

#--------------------------------
# Relative Humidity

RH_s_V1_17L   = np.array(D4_V1_17L['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V1_17L   = np.array(D4_V1_17L['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V1_17L     = (RH_s_V1_17L + RH_p_V1_17L)/2

RH_s_V2_17L   = np.array(D4_V2_17L['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V2_17L   = np.array(D4_V2_17L['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V2_17L     = (RH_s_V2_17L + RH_p_V2_17L)/2

RH_s_V3_17L   = np.array(D4_V3_17L['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V3_17L   = np.array(D4_V3_17L['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V3_17L     = (RH_s_V3_17L + RH_p_V3_17L)/2

RH_s_V1_18L   = np.array(D4_V1_18L['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V1_18L   = np.array(D4_V1_18L['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V1_18L     = (RH_s_V1_18L + RH_p_V1_18L)/2

RH_s_V2_18L   = np.array(D4_V2_18L['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V2_18L   = np.array(D4_V2_18L['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V2_18L     = (RH_s_V2_18L + RH_p_V2_18L)/2

RH_s_V3_18L   = np.array(D4_V3_18L['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V3_18L   = np.array(D4_V3_18L['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V3_18L     = (RH_s_V3_18L + RH_p_V3_18L)/2

RH_s_SIPEXIIL = np.array(D4_SIPEXIIL['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_SIPEXIIL = np.array(D4_SIPEXIIL['REL_HUMIDITY_PORT_PERCENT_y'])
RH_SIPEXIIL   = (RH_s_SIPEXIIL + RH_p_SIPEXIIL)/2

#------------------------------------------------------------------------------
# Define the variables
#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrO_V1_17H   = np.array(D4_V1_17H['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17H   = np.array(D4_V2_17H['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17H   = np.array(D4_V3_17H['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18H   = np.array(D4_V1_18H['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18H   = np.array(D4_V2_18H['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18H   = np.array(D4_V3_18H['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_SIPEXIIH = np.array(D4_SIPEXIIH['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv

#--------------------------------
# O3 (ppb)
O3_V1_17H   = np.array(D4_V1_17H['O3_(ppb)_y']) # O3 (ppb)
O3_V2_17H   = np.array(D4_V2_17H['O3_(ppb)_y']) # O3 (ppb)
O3_V3_17H   = np.array(D4_V3_17H['O3_(ppb)_y']) # O3 (ppb)
O3_V1_18H   = np.array(D4_V1_18H['O3']) # O3 (ppb)
O3_V2_18H   = np.array(D4_V2_18H['O3']) # O3 (ppb)
O3_V3_18H   = np.array(D4_V3_18H['O3']) # O3 (ppb)
O3_SIPEXIIH = np.array(D4_SIPEXIIH['O3_(ppb)_y']) # O3 (ppb)

#--------------------------------
# Solar Radiation (W/m2)
Sol_s_V1_17H           = np.array(D4_V1_17H['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V1_17H           = np.array(D4_V1_17H['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V1_17H['MeanSol']   = D4_V1_17H[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_17H             = np.array(D4_V1_17H['MeanSol'])

Sol_s_V2_17H           = np.array(D4_V2_17H['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V2_17H           = np.array(D4_V2_17H['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V2_17H['MeanSol']   = D4_V2_17H[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_17H             = np.array(D4_V2_17H['MeanSol'])

Sol_s_V3_17H           = np.array(D4_V3_17H['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V3_17H           = np.array(D4_V3_17H['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V3_17H['MeanSol']   = D4_V3_17H[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_17H             = np.array(D4_V3_17H['MeanSol'])

Sol_s_V1_18H           = np.array(D4_V1_18H['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V1_18H           = np.array(D4_V1_18H['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V1_18H['MeanSol']   = D4_V1_18H[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_18H             = np.array(D4_V1_18H['MeanSol'])

Sol_s_V2_18H           = np.array(D4_V2_18H['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V2_18H           = np.array(D4_V2_18H['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V2_18H['MeanSol']   = D4_V2_18H[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_18H             = np.array(D4_V2_18H['MeanSol'])

Sol_s_V3_18H           = np.array(D4_V3_18H['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V3_18H           = np.array(D4_V3_18H['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V3_18H['MeanSol']   = D4_V3_18H[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_18H             = np.array(D4_V3_18H['MeanSol'])

Sol_s_SIPEXIIH         = np.array(D4_SIPEXIIH['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_SIPEXIIH         = np.array(D4_SIPEXIIH['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_SIPEXIIH['MeanSol'] = D4_SIPEXIIH[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_SIPEXIIH           = np.array(D4_SIPEXIIH['MeanSol'])

#--------------------------------
# Temperature (C)

Temp_s_V1_17H           = np.array(D4_V1_17H['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V1_17H           = np.array(D4_V1_17H['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V1_17H['MeanTemp']   = D4_V1_17H[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_17H             = np.array(D4_V1_17H['MeanTemp'])

Temp_s_V2_17H           = np.array(D4_V2_17H['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V2_17H           = np.array(D4_V2_17H['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V2_17H['MeanTemp']   = D4_V2_17H[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_17H             = np.array(D4_V2_17H['MeanTemp'])

Temp_s_V3_17H           = np.array(D4_V3_17H['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V3_17H           = np.array(D4_V3_17H['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V3_17H['MeanTemp']   = D4_V3_17H[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_17H             = np.array(D4_V3_17H['MeanTemp'])

Temp_s_V1_18H           = np.array(D4_V1_18H['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V1_18H           = np.array(D4_V1_18H['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V1_18H['MeanTemp']   = D4_V1_18H[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_18H             = np.array(D4_V1_18H['MeanTemp'])

Temp_s_V2_18H           = np.array(D4_V2_18H['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V2_18H           = np.array(D4_V2_18H['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V2_18H['MeanTemp']   = D4_V2_18H[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_18H             = np.array(D4_V2_18H['MeanTemp'])

Temp_s_V3_18H           = np.array(D4_V3_18H['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V3_18H           = np.array(D4_V3_18H['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V3_18H['MeanTemp']   = D4_V3_18H[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_18H             = np.array(D4_V3_18H['MeanTemp'])

Temp_s_SIPEXIIH         = np.array(D4_SIPEXIIH['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_SIPEXIIH         = np.array(D4_SIPEXIIH['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_SIPEXIIH['MeanTemp'] = D4_SIPEXIIH[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_SIPEXIIH           = np.array(D4_SIPEXIIH['MeanTemp'])

#--------------------------------
# Wind Direction

WD_s_V1_17H   = np.array(D4_V1_17H['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V1_17H   = np.array(D4_V1_17H['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V2_17H   = np.array(D4_V2_17H['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V2_17H   = np.array(D4_V2_17H['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V3_17H   = np.array(D4_V3_17H['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V3_17H   = np.array(D4_V3_17H['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V1_18H   = np.array(D4_V1_18H['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V1_18H   = np.array(D4_V1_18H['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V2_18H   = np.array(D4_V2_18H['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V2_18H   = np.array(D4_V2_18H['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V3_18H   = np.array(D4_V3_18H['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V3_18H   = np.array(D4_V3_18H['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_SIPEXIIH = np.array(D4_SIPEXIIH['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_SIPEXIIH = np.array(D4_SIPEXIIH['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

#--------------------------------
# Wind Speed

WS_s_V1_17H   = np.array(D4_V1_17H['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17H   = np.array(D4_V1_17H['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V1_17H     = (WS_s_V1_17H + WS_p_V1_17H)/2 # Average the wind speed for port and starboard

WS_s_V2_17H   = np.array(D4_V2_17H['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17H   = np.array(D4_V2_17H['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V2_17H     = (WS_s_V2_17H + WS_p_V2_17H)/2 # Average the wind speed for port and starboard

WS_s_V3_17H   = np.array(D4_V3_17H['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17H   = np.array(D4_V3_17H['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V3_17H     = (WS_s_V3_17H + WS_p_V3_17H)/2 # Average the wind speed for port and starboard

WS_s_V1_18H   = np.array(D4_V1_18H['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18H   = np.array(D4_V1_18H['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V1_18H     = (WS_s_V1_18H + WS_p_V1_18H)/2 # Average the wind speed for port and starboard

WS_s_V2_18H   = np.array(D4_V2_18H['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18H   = np.array(D4_V2_18H['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V2_18H     = (WS_s_V2_18H + WS_p_V2_18H)/2 # Average the wind speed for port and starboard

WS_s_V3_18H   = np.array(D4_V3_18H['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18H   = np.array(D4_V3_18H['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V3_18H     = (WS_s_V3_18H + WS_p_V3_18H)/2 # Average the wind speed for port and starboard

WS_s_SIPEXIIH = np.array(D4_SIPEXIIH['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXIIH = np.array(D4_SIPEXIIH['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_SIPEXIIH   = (WS_s_SIPEXIIH + WS_p_SIPEXIIH)/2 # Average the wind speed for port and starboard

#--------------------------------
# Vector Mean Wind Direction

WD_vect_V1_17H   = ((WD_s_V1_17H   * WS_s_V1_17H)   / (WS_s_V1_17H   + WS_p_V1_17H))   + ((WD_p_V1_17H   * WS_p_V1_17H)   / (WS_s_V1_17H   + WS_p_V1_17H)) # Calculate the vector mean wind direction
WD_vect_V2_17H   = ((WD_s_V2_17H   * WS_s_V2_17H)   / (WS_s_V2_17H   + WS_p_V2_17H))   + ((WD_p_V2_17H   * WS_p_V2_17H)   / (WS_s_V2_17H   + WS_p_V2_17H)) # Calculate the vector mean wind direction
WD_vect_V3_17H   = ((WD_s_V3_17H   * WS_s_V3_17H)   / (WS_s_V3_17H   + WS_p_V3_17H))   + ((WD_p_V3_17H   * WS_p_V3_17H)   / (WS_s_V3_17H   + WS_p_V3_17H)) # Calculate the vector mean wind direction
WD_vect_V1_18H   = ((WD_s_V1_18H   * WS_s_V1_18H)   / (WS_s_V1_18H   + WS_p_V1_18H))   + ((WD_p_V1_18H   * WS_p_V1_18H)   / (WS_s_V1_18H   + WS_p_V1_18H)) # Calculate the vector mean wind direction
WD_vect_V2_18H   = ((WD_s_V2_18H   * WS_s_V2_18H)   / (WS_s_V2_18H   + WS_p_V2_18H))   + ((WD_p_V2_18H   * WS_p_V2_18H)   / (WS_s_V2_18H   + WS_p_V2_18H)) # Calculate the vector mean wind direction
WD_vect_V3_18H   = ((WD_s_V3_18H   * WS_s_V3_18H)   / (WS_s_V3_18H   + WS_p_V3_18H))   + ((WD_p_V3_18H   * WS_p_V3_18H)   / (WS_s_V3_18H   + WS_p_V3_18H)) # Calculate the vector mean wind direction
WD_vect_SIPEXIIH = ((WD_s_SIPEXIIH * WS_s_SIPEXIIH) / (WS_s_SIPEXIIH + WS_p_SIPEXIIH)) + ((WD_p_SIPEXIIH * WS_p_SIPEXIIH) / (WS_s_SIPEXIIH + WS_p_SIPEXIIH)) # Calculate the vector mean wind direction

#--------------------------------
# Hg0

Hg0_V1_17H   = np.array(D4_V1_17H['ng/m3_y']) # Hg0
Hg0_V2_17H   = np.array(D4_V2_17H['ng/m3_y']) # Hg0
Hg0_V3_17H   = np.array(D4_V3_17H['ng/m3_y']) # Hg0
Hg0_V1_18H   = np.array(D4_V1_18H['ng/m3_y']) # Hg0
Hg0_V2_18H   = np.array(D4_V2_18H['ng/m3_y']) # Hg0
Hg0_V3_18H   = np.array(D4_V3_18H['ng/m3_y']) # Hg0
Hg0_SIPEXIIH = np.array(D4_SIPEXIIH['ng/m3_y']) # Hg0

#--------------------------------
# Sea Ice Concentration

SI_V1_17H   = np.array(D4_V1_17H['Sea_Ice_Conc'])   * 100
SI_V2_17H   = np.array(D4_V2_17H['Sea_Ice_Conc'])   * 100
SI_V3_17H   = np.array(D4_V3_17H['Sea_Ice_Conc'])   * 100
SI_V1_18H   = np.array(D4_V1_18H['Sea_Ice_Conc'])   * 100
SI_V2_18H   = np.array(D4_V2_18H['Sea_Ice_Conc'])   * 100
SI_V3_18H   = np.array(D4_V3_18H['Sea_Ice_Conc'])   * 100
SI_SIPEXIIH = np.array(D4_SIPEXIIH['Sea_Ice_Conc']) * 100

#--------------------------------
# Relative Humidity

RH_s_V1_17H   = np.array(D4_V1_17H['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V1_17H   = np.array(D4_V1_17H['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V1_17H     = (RH_s_V1_17H + RH_p_V1_17H)/2

RH_s_V2_17H   = np.array(D4_V2_17H['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V2_17H   = np.array(D4_V2_17H['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V2_17H     = (RH_s_V2_17H + RH_p_V2_17H)/2

RH_s_V3_17H   = np.array(D4_V3_17H['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V3_17H   = np.array(D4_V3_17H['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V3_17H     = (RH_s_V3_17H + RH_p_V3_17H)/2

RH_s_V1_18H   = np.array(D4_V1_18H['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V1_18H   = np.array(D4_V1_18H['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V1_18H     = (RH_s_V1_18H + RH_p_V1_18H)/2

RH_s_V2_18H   = np.array(D4_V2_18H['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V2_18H   = np.array(D4_V2_18H['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V2_18H     = (RH_s_V2_18H + RH_p_V2_18H)/2

RH_s_V3_18H   = np.array(D4_V3_18H['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V3_18H   = np.array(D4_V3_18H['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V3_18H     = (RH_s_V3_18H + RH_p_V3_18H)/2

RH_s_SIPEXIIH = np.array(D4_SIPEXIIH['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_SIPEXIIH = np.array(D4_SIPEXIIH['REL_HUMIDITY_PORT_PERCENT_y'])
RH_SIPEXIIH   = (RH_s_SIPEXIIH + RH_p_SIPEXIIH)/2

#------------------------------------------------------------------------------
# Concate the variables from each voyage

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOL = np.concatenate((BrO_V1_17L, BrO_V2_17L, BrO_V3_17L, BrO_V1_18L, BrO_V2_18L, BrO_V3_18L, BrO_SIPEXIIL), axis=0)

# O3 (ppb)
O3L = np.concatenate((O3_V1_17L, O3_V2_17L, O3_V3_17L, O3_V1_18L, O3_V2_18L, O3_V3_18L, O3_SIPEXIIL), axis=0)

# Solar Radiation (W/m2)
SolL = np.concatenate((Sol_V1_17L, Sol_V2_17L, Sol_V3_17L, Sol_V1_18L, Sol_V2_18L, Sol_V3_18L, Sol_SIPEXIIL), axis=0)

# Temperature (C)
TempL = np.concatenate((Temp_V1_17L, Temp_V2_17L, Temp_V3_17L, Temp_V1_18L, Temp_V2_18L, Temp_V3_18L, Temp_SIPEXIIL), axis=0)

# Wind Speed
WSL = np.concatenate((WS_V1_17L, WS_V2_17L, WS_V3_17L, WS_V1_18L, WS_V2_18L, WS_V3_18L, WS_SIPEXIIL), axis=0)

# Vector Mean Wind Direction
WD_vectL = np.concatenate((WD_vect_V1_17L, WD_vect_V2_17L, WD_vect_V3_17L, WD_vect_V1_18L, WD_vect_V2_18L, WD_vect_V3_18L, WD_vect_SIPEXIIL), axis=0)

# Hg0
Hg0L = np.concatenate((Hg0_V1_17L, Hg0_V2_17L, Hg0_V3_17L, Hg0_V1_18L, Hg0_V2_18L, Hg0_V3_18L, Hg0_SIPEXIIL), axis=0)

# Sea Ice Concentration
SIL = np.concatenate((SI_V1_17L, SI_V2_17L, SI_V3_17L, SI_V1_18L, SI_V2_18L, SI_V3_18L, SI_SIPEXIIL), axis=0)

# Relative Humidity
RHL = np.concatenate((RH_V1_17L, RH_V2_17L, RH_V3_17L, RH_V1_18L, RH_V2_18L, RH_V3_18L, RH_SIPEXIIL), axis=0)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOH = np.concatenate((BrO_V1_17H, BrO_V2_17H, BrO_V3_17H, BrO_V1_18H, BrO_V2_18H, BrO_V3_18H, BrO_SIPEXIIH), axis=0)

# O3 (ppb)
O3H = np.concatenate((O3_V1_17H, O3_V2_17H, O3_V3_17H, O3_V1_18H, O3_V2_18H, O3_V3_18H, O3_SIPEXIIH), axis=0)

# Solar Radiation (W/m2)
SolH = np.concatenate((Sol_V1_17H, Sol_V2_17H, Sol_V3_17H, Sol_V1_18H, Sol_V2_18H, Sol_V3_18H, Sol_SIPEXIIH), axis=0)

# Temperature (C)
TempH = np.concatenate((Temp_V1_17H, Temp_V2_17H, Temp_V3_17H, Temp_V1_18H, Temp_V2_18H, Temp_V3_18H, Temp_SIPEXIIH), axis=0)

# Wind Speed
WSH = np.concatenate((WS_V1_17H, WS_V2_17H, WS_V3_17H, WS_V1_18H, WS_V2_18H, WS_V3_18H, WS_SIPEXIIH), axis=0)

# Vector Mean Wind Direction
WD_vectH = np.concatenate((WD_vect_V1_17H, WD_vect_V2_17H, WD_vect_V3_17H, WD_vect_V1_18H, WD_vect_V2_18H, WD_vect_V3_18H, WD_vect_SIPEXIIH), axis=0)

# Hg0
Hg0H = np.concatenate((Hg0_V1_17H, Hg0_V2_17H, Hg0_V3_17H, Hg0_V1_18H, Hg0_V2_18H, Hg0_V3_18H, Hg0_SIPEXIIH), axis=0)

# Sea Ice Concentration
SIH = np.concatenate((SI_V1_17H, SI_V2_17H, SI_V3_17H, SI_V1_18H, SI_V2_18H, SI_V3_18H, SI_SIPEXIIH), axis=0)

# Relative Humidity
RHH = np.concatenate((RH_V1_17H, RH_V2_17H, RH_V3_17H, RH_V1_18H, RH_V2_18H, RH_V3_18H, RH_SIPEXIIH), axis=0)

#------------------------------------------------------------------------------
# Scan for NaN values
#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V1_17_Y1maskL   = np.isfinite(Sol_V1_17L) # Scan for NaN values
BrO_V1_17L      = BrO_V1_17L[V1_17_Y1maskL] # Remove NaN values from BrO
O3_V1_17L       = O3_V1_17L[V1_17_Y1maskL] # Remove NaN values from Sol
Sol_V1_17L      = Sol_V1_17L[V1_17_Y1maskL] # Remove NaN values from Sol
Temp_V1_17L     = Temp_V1_17L[V1_17_Y1maskL] # Remove NaN values from Sol
WD_vect_V1_17L  = WD_vect_V1_17L[V1_17_Y1maskL] # Remove NaN values from Sol
WS_V1_17L       = WS_V1_17L[V1_17_Y1maskL] # Remove NaN values from Sol
Hg0_V1_17L      = Hg0_V1_17L[V1_17_Y1maskL] # Remove NaN values from Sol
SI_V1_17L       = SI_V1_17L[V1_17_Y1maskL] # Remove NaN values from Sol

# Pass 2 (O3) 
V1_17_Y2maskL   = np.isfinite(O3_V1_17L) # Scan for NaN values
BrO_O3_V1_17L   = BrO_V1_17L[V1_17_Y2maskL] # Remove NaN values from BrO
O3_V1_17L       = O3_V1_17L[V1_17_Y2maskL] # Remove NaN values from Temp
Sol_O3_V1_17L   = Sol_V1_17L[V1_17_Y2maskL] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_17_Y3maskL   = np.isfinite(Temp_V1_17L) # Scan for NaN values
BrO_Temp_V1_17L = BrO_V1_17L[V1_17_Y3maskL] # Remove NaN values from BrO
Temp_V1_17L     = Temp_V1_17L[V1_17_Y3maskL] # Remove NaN values from Temp
Sol_Temp_V1_17L = Sol_V1_17L[V1_17_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_17_Y4maskL   = np.isfinite(WD_vect_V1_17L) # Scan for NaN values
BrO_WD_V1_17L   = BrO_V1_17L[V1_17_Y4maskL] # Remove NaN values from BrO
WD_vect_V1_17L  = WD_vect_V1_17L[V1_17_Y4maskL] # Remove NaN values from WD_vect
Sol_WD_V1_17L   = Sol_V1_17L[V1_17_Y4maskL] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_17_Y5maskL   = np.isfinite(WS_V1_17L) # Scan for NaN values
BrO_WS_V1_17L   = BrO_V1_17L[V1_17_Y5maskL] # Remove NaN values from BrO
WS_V1_17L       = WS_V1_17L[V1_17_Y5maskL] # Remove NaN values from WS
Sol_WS_V1_17L   = Sol_V1_17L[V1_17_Y5maskL] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_17_Y6maskL   = np.isfinite(Hg0_V1_17L) # Scan for NaN values
BrO_Hg0_V1_17L  = BrO_V1_17L[V1_17_Y6maskL] # Remove NaN values from BrO
Hg0_V1_17L      = Hg0_V1_17L[V1_17_Y6maskL] # Remove NaN values from SI
Sol_Hg0_V1_17L  = Sol_V1_17L[V1_17_Y6maskL] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_17_Y7maskL   = np.isfinite(SI_V1_17L) # Scan for NaN values
BrO_SI_V1_17L   = BrO_V1_17L[V1_17_Y7maskL] # Remove NaN values from BrO
SI_SI_V1_17L    = SI_V1_17L[V1_17_Y7maskL] # Remove NaN values from SI
Sol_SI_V1_17L   = Sol_V1_17L[V1_17_Y7maskL] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_17_Y8maskL   = np.isfinite(RH_V1_17L) # Scan for NaN values
BrO_RH_V1_17L   = BrO_V1_17L[V1_17_Y8maskL] # Remove NaN values from BrO
RH_V1_17L       = RH_V1_17L[V1_17_Y8maskL] # Remove NaN values from WS
Sol_RH_V1_17L   = Sol_V1_17L[V1_17_Y8maskL] # Remove NaN values from Sol

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V2_17_Y1maskL   = np.isfinite(Sol_V2_17L) # Scan for NaN values
BrO_V2_17L      = BrO_V2_17L[V2_17_Y1maskL] # Remove NaN values from BrO
O3_V2_17L       = O3_V2_17L[V2_17_Y1maskL] # Remove NaN values from Sol
Sol_V2_17L      = Sol_V2_17L[V2_17_Y1maskL] # Remove NaN values from Sol
Temp_V2_17L     = Temp_V2_17L[V2_17_Y1maskL] # Remove NaN values from Sol
WD_vect_V2_17L  = WD_vect_V2_17L[V2_17_Y1maskL] # Remove NaN values from Sol
WS_V2_17L       = WS_V2_17L[V2_17_Y1maskL] # Remove NaN values from Sol
Hg0_V2_17L      = Hg0_V2_17L[V2_17_Y1maskL] # Remove NaN values from Sol
SI_V2_17L       = SI_V2_17L[V2_17_Y1maskL] # Remove NaN values from Sol

# Pass 2 (O3) 
V2_17_Y2maskL   = np.isfinite(O3_V2_17L) # Scan for NaN values
BrO_O3_V2_17L   = BrO_V2_17L[V2_17_Y2maskL] # Remove NaN values from BrO
O3_V2_17L       = O3_V2_17L[V2_17_Y2maskL] # Remove NaN values from Temp
Sol_O3_V2_17L   = Sol_V2_17L[V2_17_Y2maskL] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_17_Y3maskL   = np.isfinite(Temp_V2_17L) # Scan for NaN values
BrO_Temp_V2_17L = BrO_V2_17L[V2_17_Y3maskL] # Remove NaN values from BrO
Temp_V2_17L     = Temp_V2_17L[V2_17_Y3maskL] # Remove NaN values from Temp
Sol_Temp_V2_17L = Sol_V2_17L[V2_17_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_17_Y4maskL   = np.isfinite(WD_vect_V2_17L) # Scan for NaN values
BrO_WD_V2_17L   = BrO_V2_17L[V2_17_Y4maskL] # Remove NaN values from BrO
WD_vect_V2_17L  = WD_vect_V2_17L[V2_17_Y4maskL] # Remove NaN values from WD_vect
Sol_WD_V2_17L   = Sol_V2_17L[V2_17_Y4maskL] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_17_Y5maskL   = np.isfinite(WS_V2_17L) # Scan for NaN values
BrO_WS_V2_17L   = BrO_V2_17L[V2_17_Y5maskL] # Remove NaN values from BrO
WS_V2_17L       = WS_V2_17L[V2_17_Y5maskL] # Remove NaN values from WS
Sol_WS_V2_17L   = Sol_V2_17L[V2_17_Y5maskL] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_17_Y6maskL   = np.isfinite(Hg0_V2_17L) # Scan for NaN values
BrO_Hg0_V2_17L  = BrO_V2_17L[V2_17_Y6maskL] # Remove NaN values from BrO
Hg0_V2_17L      = Hg0_V2_17L[V2_17_Y6maskL] # Remove NaN values from SI
Sol_Hg0_V2_17L  = Sol_V2_17L[V2_17_Y6maskL] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_17_Y7maskL   = np.isfinite(SI_V2_17L) # Scan for NaN values
BrO_SI_V2_17L   = BrO_V2_17L[V2_17_Y7maskL] # Remove NaN values from BrO
SI_SI_V2_17L    = SI_V2_17L[V2_17_Y7maskL] # Remove NaN values from SI
Sol_SI_V2_17L   = Sol_V2_17L[V2_17_Y7maskL] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_17_Y8maskL   = np.isfinite(RH_V2_17L) # Scan for NaN values
BrO_RH_V2_17L   = BrO_V2_17L[V2_17_Y8maskL] # Remove NaN values from BrO
RH_V2_17L       = RH_V2_17L[V2_17_Y8maskL] # Remove NaN values from WS
Sol_RH_V2_17L   = Sol_V2_17L[V2_17_Y8maskL] # Remove NaN values from Sol

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V3_17_Y1maskL   = np.isfinite(Sol_V3_17L) # Scan for NaN values
BrO_V3_17L      = BrO_V3_17L[V3_17_Y1maskL] # Remove NaN values from BrO
O3_V3_17L       = O3_V3_17L[V3_17_Y1maskL] # Remove NaN values from Sol
Sol_V3_17L      = Sol_V3_17L[V3_17_Y1maskL] # Remove NaN values from Sol
Temp_V3_17L     = Temp_V3_17L[V3_17_Y1maskL] # Remove NaN values from Sol
WD_vect_V3_17L  = WD_vect_V3_17L[V3_17_Y1maskL] # Remove NaN values from Sol
WS_V3_17L       = WS_V3_17L[V3_17_Y1maskL] # Remove NaN values from Sol
Hg0_V3_17L      = Hg0_V3_17L[V3_17_Y1maskL] # Remove NaN values from Sol
SI_V3_17L       = SI_V3_17L[V3_17_Y1maskL] # Remove NaN values from Sol

# Pass 2 (O3) 
V3_17_Y2maskL   = np.isfinite(O3_V3_17L) # Scan for NaN values
BrO_O3_V3_17L   = BrO_V3_17L[V3_17_Y2maskL] # Remove NaN values from BrO
O3_V3_17L       = O3_V3_17L[V3_17_Y2maskL] # Remove NaN values from Temp
Sol_O3_V3_17L   = Sol_V3_17L[V3_17_Y2maskL] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_17_Y3maskL   = np.isfinite(Temp_V3_17L) # Scan for NaN values
BrO_Temp_V3_17L = BrO_V3_17L[V3_17_Y3maskL] # Remove NaN values from BrO
Temp_V3_17L     = Temp_V3_17L[V3_17_Y3maskL] # Remove NaN values from Temp
Sol_Temp_V3_17L = Sol_V3_17L[V3_17_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_17_Y4maskL   = np.isfinite(WD_vect_V3_17L) # Scan for NaN values
BrO_WD_V3_17L   = BrO_V3_17L[V3_17_Y4maskL] # Remove NaN values from BrO
WD_vect_V3_17L  = WD_vect_V3_17L[V3_17_Y4maskL] # Remove NaN values from WD_vect
Sol_WD_V3_17L   = Sol_V3_17L[V3_17_Y4maskL] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_17_Y5maskL   = np.isfinite(WS_V3_17L) # Scan for NaN values
BrO_WS_V3_17L   = BrO_V3_17L[V3_17_Y5maskL] # Remove NaN values from BrO
WS_V3_17L       = WS_V3_17L[V3_17_Y5maskL] # Remove NaN values from WS
Sol_WS_V3_17L   = Sol_V3_17L[V3_17_Y5maskL] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_17_Y6maskL   = np.isfinite(Hg0_V3_17L) # Scan for NaN values
BrO_Hg0_V3_17L  = BrO_V3_17L[V3_17_Y6maskL] # Remove NaN values from BrO
Hg0_V3_17L      = Hg0_V3_17L[V3_17_Y6maskL] # Remove NaN values from SI
Sol_Hg0_V3_17L  = Sol_V3_17L[V3_17_Y6maskL] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_17_Y7maskL   = np.isfinite(SI_V3_17L) # Scan for NaN values
BrO_SI_V3_17L   = BrO_V3_17L[V3_17_Y7maskL] # Remove NaN values from BrO
SI_SI_V3_17L    = SI_V3_17L[V3_17_Y7maskL] # Remove NaN values from SI
Sol_SI_V3_17L   = Sol_V3_17L[V3_17_Y7maskL] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_17_Y8maskL   = np.isfinite(RH_V3_17L) # Scan for NaN values
BrO_RH_V3_17L   = BrO_V3_17L[V3_17_Y8maskL] # Remove NaN values from BrO
RH_V3_17L       = RH_V3_17L[V3_17_Y8maskL] # Remove NaN values from WS
Sol_RH_V3_17L   = Sol_V3_17L[V3_17_Y8maskL] # Remove NaN values from Sol

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V1_18_Y1maskL   = np.isfinite(Sol_V1_18L) # Scan for NaN values
BrO_V1_18L      = BrO_V1_18L[V1_18_Y1maskL] # Remove NaN values from BrO
O3_V1_18L       = O3_V1_18L[V1_18_Y1maskL] # Remove NaN values from Sol
Sol_V1_18L      = Sol_V1_18L[V1_18_Y1maskL] # Remove NaN values from Sol
Temp_V1_18L     = Temp_V1_18L[V1_18_Y1maskL] # Remove NaN values from Sol
WD_vect_V1_18L  = WD_vect_V1_18L[V1_18_Y1maskL] # Remove NaN values from Sol
WS_V1_18L       = WS_V1_18L[V1_18_Y1maskL] # Remove NaN values from Sol
Hg0_V1_18L      = Hg0_V1_18L[V1_18_Y1maskL] # Remove NaN values from Sol
SI_V1_18L       = SI_V1_18L[V1_18_Y1maskL] # Remove NaN values from Sol

# Pass 2 (O3) 
V1_18_Y2maskL   = np.isfinite(O3_V1_18L) # Scan for NaN values
BrO_O3_V1_18L   = BrO_V1_18L[V1_18_Y2maskL] # Remove NaN values from BrO
O3_V1_18L       = O3_V1_18L[V1_18_Y2maskL] # Remove NaN values from Temp
Sol_O3_V1_18L   = Sol_V1_18L[V1_18_Y2maskL] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_18_Y3maskL   = np.isfinite(Temp_V1_18L) # Scan for NaN values
BrO_Temp_V1_18L = BrO_V1_18L[V1_18_Y3maskL] # Remove NaN values from BrO
Temp_V1_18L     = Temp_V1_18L[V1_18_Y3maskL] # Remove NaN values from Temp
Sol_Temp_V1_18L = Sol_V1_18L[V1_18_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_18_Y4maskL   = np.isfinite(WD_vect_V1_18L) # Scan for NaN values
BrO_WD_V1_18L   = BrO_V1_18L[V1_18_Y4maskL] # Remove NaN values from BrO
WD_vect_V1_18L  = WD_vect_V1_18L[V1_18_Y4maskL] # Remove NaN values from WD_vect
Sol_WD_V1_18L   = Sol_V1_18L[V1_18_Y4maskL] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_18_Y5maskL   = np.isfinite(WS_V1_18L) # Scan for NaN values
BrO_WS_V1_18L   = BrO_V1_18L[V1_18_Y5maskL] # Remove NaN values from BrO
WS_V1_18L       = WS_V1_18L[V1_18_Y5maskL] # Remove NaN values from WS
Sol_WS_V1_18L   = Sol_V1_18L[V1_18_Y5maskL] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_18_Y6maskL   = np.isfinite(Hg0_V1_18L) # Scan for NaN values
BrO_Hg0_V1_18L  = BrO_V1_18L[V1_18_Y6maskL] # Remove NaN values from BrO
Hg0_V1_18L      = Hg0_V1_18L[V1_18_Y6maskL] # Remove NaN values from SI
Sol_Hg0_V1_18L  = Sol_V1_18L[V1_18_Y6maskL] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_18_Y7maskL   = np.isfinite(SI_V1_18L) # Scan for NaN values
BrO_SI_V1_18L   = BrO_V1_18L[V1_18_Y7maskL] # Remove NaN values from BrO
SI_SI_V1_18L    = SI_V1_18L[V1_18_Y7maskL] # Remove NaN values from SI
Sol_SI_V1_18L   = Sol_V1_18L[V1_18_Y7maskL] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_18_Y8maskL   = np.isfinite(RH_V1_18L) # Scan for NaN values
BrO_RH_V1_18L   = BrO_V1_18L[V1_18_Y8maskL] # Remove NaN values from BrO
RH_V1_18L       = RH_V1_18L[V1_18_Y8maskL] # Remove NaN values from WS
Sol_RH_V1_18L   = Sol_V1_18L[V1_18_Y8maskL] # Remove NaN values from Sol

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V2_18_Y1maskL   = np.isfinite(Sol_V2_18L) # Scan for NaN values
BrO_V2_18L      = BrO_V2_18L[V2_18_Y1maskL] # Remove NaN values from BrO
O3_V2_18L       = O3_V2_18L[V2_18_Y1maskL] # Remove NaN values from Sol
Sol_V2_18L      = Sol_V2_18L[V2_18_Y1maskL] # Remove NaN values from Sol
Temp_V2_18L     = Temp_V2_18L[V2_18_Y1maskL] # Remove NaN values from Sol
WD_vect_V2_18L  = WD_vect_V2_18L[V2_18_Y1maskL] # Remove NaN values from Sol
WS_V2_18L       = WS_V2_18L[V2_18_Y1maskL] # Remove NaN values from Sol
Hg0_V2_18L      = Hg0_V2_18L[V2_18_Y1maskL] # Remove NaN values from Sol
SI_V2_18L       = SI_V2_18L[V2_18_Y1maskL] # Remove NaN values from Sol

# Pass 2 (O3) 
V2_18_Y2maskL   = np.isfinite(O3_V2_18L) # Scan for NaN values
BrO_O3_V2_18L   = BrO_V2_18L[V2_18_Y2maskL] # Remove NaN values from BrO
O3_V2_18L       = O3_V2_18L[V2_18_Y2maskL] # Remove NaN values from Temp
Sol_O3_V2_18L   = Sol_V2_18L[V2_18_Y2maskL] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_18_Y3maskL   = np.isfinite(Temp_V2_18L) # Scan for NaN values
BrO_Temp_V2_18L = BrO_V2_18L[V2_18_Y3maskL] # Remove NaN values from BrO
Temp_V2_18L     = Temp_V2_18L[V2_18_Y3maskL] # Remove NaN values from Temp
Sol_Temp_V2_18L = Sol_V2_18L[V2_18_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_18_Y4maskL   = np.isfinite(WD_vect_V2_18L) # Scan for NaN values
BrO_WD_V2_18L   = BrO_V2_18L[V2_18_Y4maskL] # Remove NaN values from BrO
WD_vect_V2_18L  = WD_vect_V2_18L[V2_18_Y4maskL] # Remove NaN values from WD_vect
Sol_WD_V2_18L   = Sol_V2_18L[V2_18_Y4maskL] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_18_Y5maskL   = np.isfinite(WS_V2_18L) # Scan for NaN values
BrO_WS_V2_18L   = BrO_V2_18L[V2_18_Y5maskL] # Remove NaN values from BrO
WS_V2_18L       = WS_V2_18L[V2_18_Y5maskL] # Remove NaN values from WS
Sol_WS_V2_18L   = Sol_V2_18L[V2_18_Y5maskL] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_18_Y6maskL   = np.isfinite(Hg0_V2_18L) # Scan for NaN values
BrO_Hg0_V2_18L  = BrO_V2_18L[V2_18_Y6maskL] # Remove NaN values from BrO
Hg0_V2_18L      = Hg0_V2_18L[V2_18_Y6maskL] # Remove NaN values from SI
Sol_Hg0_V2_18L  = Sol_V2_18L[V2_18_Y6maskL] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_18_Y7maskL   = np.isfinite(SI_V2_18L) # Scan for NaN values
BrO_SI_V2_18L   = BrO_V2_18L[V2_18_Y7maskL] # Remove NaN values from BrO
SI_SI_V2_18L    = SI_V2_18L[V2_18_Y7maskL] # Remove NaN values from SI
Sol_SI_V2_18L   = Sol_V2_18L[V2_18_Y7maskL] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_18_Y8maskL   = np.isfinite(RH_V2_18L) # Scan for NaN values
BrO_RH_V2_18L   = BrO_V2_18L[V2_18_Y8maskL] # Remove NaN values from BrO
RH_V2_18L       = RH_V2_18L[V2_18_Y8maskL] # Remove NaN values from WS
Sol_RH_V2_18L   = Sol_V2_18L[V2_18_Y8maskL] # Remove NaN values from Sol

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V3_18_Y1maskL   = np.isfinite(Sol_V3_18L) # Scan for NaN values
BrO_V3_18L      = BrO_V3_18L[V3_18_Y1maskL] # Remove NaN values from BrO
O3_V3_18L       = O3_V3_18L[V3_18_Y1maskL] # Remove NaN values from Sol
Sol_V3_18L      = Sol_V3_18L[V3_18_Y1maskL] # Remove NaN values from Sol
Temp_V3_18L     = Temp_V3_18L[V3_18_Y1maskL] # Remove NaN values from Sol
WD_vect_V3_18L  = WD_vect_V3_18L[V3_18_Y1maskL] # Remove NaN values from Sol
WS_V3_18L       = WS_V3_18L[V3_18_Y1maskL] # Remove NaN values from Sol
Hg0_V3_18L      = Hg0_V3_18L[V3_18_Y1maskL] # Remove NaN values from Sol
SI_V3_18L       = SI_V3_18L[V3_18_Y1maskL] # Remove NaN values from Sol

# Pass 2 (O3) 
V3_18_Y2maskL   = np.isfinite(O3_V3_18L) # Scan for NaN values
BrO_O3_V3_18L   = BrO_V3_18L[V3_18_Y2maskL] # Remove NaN values from BrO
O3_V3_18L       = O3_V3_18L[V3_18_Y2maskL] # Remove NaN values from Temp
Sol_O3_V3_18L   = Sol_V3_18L[V3_18_Y2maskL] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_18_Y3maskL   = np.isfinite(Temp_V3_18L) # Scan for NaN values
BrO_Temp_V3_18L = BrO_V3_18L[V3_18_Y3maskL] # Remove NaN values from BrO
Temp_V3_18L     = Temp_V3_18L[V3_18_Y3maskL] # Remove NaN values from Temp
Sol_Temp_V3_18L = Sol_V3_18L[V3_18_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_18_Y4maskL   = np.isfinite(WD_vect_V3_18L) # Scan for NaN values
BrO_WD_V3_18L   = BrO_V3_18L[V3_18_Y4maskL] # Remove NaN values from BrO
WD_vect_V3_18L  = WD_vect_V3_18L[V3_18_Y4maskL] # Remove NaN values from WD_vect
Sol_WD_V3_18L   = Sol_V3_18L[V3_18_Y4maskL] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_18_Y5maskL   = np.isfinite(WS_V3_18L) # Scan for NaN values
BrO_WS_V3_18L   = BrO_V3_18L[V3_18_Y5maskL] # Remove NaN values from BrO
WS_V3_18L       = WS_V3_18L[V3_18_Y5maskL] # Remove NaN values from WS
Sol_WS_V3_18L   = Sol_V3_18L[V3_18_Y5maskL] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_18_Y6maskL   = np.isfinite(Hg0_V3_18L) # Scan for NaN values
BrO_Hg0_V3_18L  = BrO_V3_18L[V3_18_Y6maskL] # Remove NaN values from BrO
Hg0_V3_18L      = Hg0_V3_18L[V3_18_Y6maskL] # Remove NaN values from SI
Sol_Hg0_V3_18L  = Sol_V3_18L[V3_18_Y6maskL] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_18_Y7maskL   = np.isfinite(SI_V3_18L) # Scan for NaN values
BrO_SI_V3_18L   = BrO_V3_18L[V3_18_Y7maskL] # Remove NaN values from BrO
SI_SI_V3_18L    = SI_V3_18L[V3_18_Y7maskL] # Remove NaN values from SI
Sol_SI_V3_18L   = Sol_V3_18L[V3_18_Y7maskL] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_18_Y8maskL   = np.isfinite(RH_V3_18L) # Scan for NaN values
BrO_RH_V3_18L   = BrO_V3_18L[V3_18_Y8maskL] # Remove NaN values from BrO
RH_V3_18L       = RH_V3_18L[V3_18_Y8maskL] # Remove NaN values from WS
Sol_RH_V3_18L   = Sol_V3_18L[V3_18_Y8maskL] # Remove NaN values from Sol

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (Sol) 
SIPEXII_Y1maskL   = np.isfinite(Sol_SIPEXIIL) # Scan for NaN values
BrO_SIPEXIIL      = BrO_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from BrO
O3_SIPEXIIL       = O3_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from Sol
Sol_SIPEXIIL      = Sol_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from Sol
Temp_SIPEXIIL     = Temp_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from Sol
WD_vect_SIPEXIIL  = WD_vect_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from Sol
WS_SIPEXIIL       = WS_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from Sol
Hg0_SIPEXIIL      = Hg0_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from Sol
SI_SIPEXIIL       = SI_SIPEXIIL[SIPEXII_Y1maskL] # Remove NaN values from Sol

# Pass 2 (Temp) 
SIPEXII_Y2maskL   = np.isfinite(Temp_SIPEXIIL) # Scan for NaN values
BrO_Temp_SIPEXIIL = BrO_SIPEXIIL[SIPEXII_Y2maskL] # Remove NaN values from BrO
Temp_SIPEXIIL     = Temp_SIPEXIIL[SIPEXII_Y2maskL] # Remove NaN values from Temp
Sol_Temp_SIPEXIIL = Sol_SIPEXIIL[SIPEXII_Y2maskL] # Remove NaN values from Sol

# Pass 3 (WD_vect) 
SIPEXII_Y3maskL   = np.isfinite(WD_vect_SIPEXIIL) # Scan for NaN values
BrO_WD_SIPEXIIL   = BrO_SIPEXIIL[SIPEXII_Y3maskL] # Remove NaN values from BrO
WD_vect_SIPEXIIL  = WD_vect_SIPEXIIL[SIPEXII_Y3maskL] # Remove NaN values from WD_vect
Sol_WD_SIPEXIIL   = Sol_SIPEXIIL[SIPEXII_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WS) 
SIPEXII_Y4maskL   = np.isfinite(WS_SIPEXIIL) # Scan for NaN values
BrO_WS_SIPEXIIL   = BrO_SIPEXIIL[SIPEXII_Y4maskL] # Remove NaN values from BrO
WS_SIPEXIIL       = WS_SIPEXIIL[SIPEXII_Y4maskL] # Remove NaN values from WS
Sol_WS_SIPEXIIL   = Sol_SIPEXIIL[SIPEXII_Y4maskL] # Remove NaN values from Sol

# Pass 5 (Hg0) 
SIPEXII_Y5maskL   = np.isfinite(Hg0_SIPEXIIL) # Scan for NaN values
BrO_Hg0_SIPEXIIL  = BrO_SIPEXIIL[SIPEXII_Y5maskL] # Remove NaN values from BrO
Hg0_SIPEXIIL      = Hg0_SIPEXIIL[SIPEXII_Y5maskL] # Remove NaN values from SI
Sol_Hg0_SIPEXIIL  = Sol_SIPEXIIL[SIPEXII_Y5maskL] # Remove NaN values from Sol

# Pass 6 (SI Field) 
SIPEXII_Y6maskL   = np.isfinite(SI_SIPEXIIL) # Scan for NaN values
BrO_SI_SIPEXIIL   = BrO_SIPEXIIL[SIPEXII_Y6maskL] # Remove NaN values from BrO
SI_SI_SIPEXIIL    = SI_SIPEXIIL[SIPEXII_Y6maskL] # Remove NaN values from SI
Sol_SI_SIPEXIIL   = Sol_SIPEXIIL[SIPEXII_Y6maskL] # Remove NaN values from Sol

# Pass 7 (RH) 
SIPEXII_Y7maskL   = np.isfinite(RH_SIPEXIIL) # Scan for NaN values
BrO_RH_SIPEXIIL   = BrO_SIPEXIIL[SIPEXII_Y7maskL] # Remove NaN values from BrO
RH_SIPEXIIL       = RH_SIPEXIIL[SIPEXII_Y7maskL] # Remove NaN values from WS
Sol_RH_SIPEXIIL   = Sol_SIPEXIIL[SIPEXII_Y7maskL] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (Sol) 
ALL_Y1maskL  = np.isfinite(SolL) # Scan for NaN values
BrOL         = BrOL[ALL_Y1maskL] # Remove NaN values from BrO
O3L          = O3L[ALL_Y1maskL] # Remove NaN values from Sol
SolL         = SolL[ALL_Y1maskL] # Remove NaN values from Sol
TempL        = TempL[ALL_Y1maskL] # Remove NaN values from Sol
WD_vectL     = WD_vectL[ALL_Y1maskL] # Remove NaN values from Sol
WSL          = WSL[ALL_Y1maskL] # Remove NaN values from Sol
Hg0L         = Hg0L[ALL_Y1maskL] # Remove NaN values from Sol
SIL          = SIL[ALL_Y1maskL] # Remove NaN values from Sol

# Pass 2 (O3) 
ALL_Y2maskL  = np.isfinite(O3L) # Scan for NaN values
BrO_O3L      = BrOL[ALL_Y2maskL] # Remove NaN values from BrO
O3L          = O3L[ALL_Y2maskL] # Remove NaN values from Temp
Sol_O3L      = SolL[ALL_Y2maskL] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskL  = np.isfinite(TempL) # Scan for NaN values
BrO_TempL    = BrOL[ALL_Y3maskL] # Remove NaN values from BrO
TempL        = TempL[ALL_Y3maskL] # Remove NaN values from Temp
Sol_TempL    = SolL[ALL_Y3maskL] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskL  = np.isfinite(WD_vectL) # Scan for NaN values
BrO_WDL      = BrOL[ALL_Y4maskL] # Remove NaN values from BrO
WD_vectL     = WD_vectL[ALL_Y4maskL] # Remove NaN values from WD_vect
Sol_WDL      = SolL[ALL_Y4maskL] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskL  = np.isfinite(WSL) # Scan for NaN values
BrO_WSL      = BrOL[ALL_Y5maskL] # Remove NaN values from BrO
WSL          = WSL[ALL_Y5maskL] # Remove NaN values from WS
Sol_WSL      = SolL[ALL_Y5maskL] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskL  = np.isfinite(Hg0L) # Scan for NaN values
BrO_Hg0L     = BrOL[ALL_Y6maskL] # Remove NaN values from BrO
Hg0L         = Hg0L[ALL_Y6maskL] # Remove NaN values from SI
Sol_Hg0L     = SolL[ALL_Y6maskL] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskL  = np.isfinite(SIL) # Scan for NaN values
BrO_SIL      = BrOL[ALL_Y7maskL] # Remove NaN values from BrO
SI_SIL       = SIL[ALL_Y7maskL] # Remove NaN values from SI
Sol_SIL      = SolL[ALL_Y7maskL] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskL  = np.isfinite(RHL) # Scan for NaN values
BrO_RHL      = BrOL[ALL_Y8maskL] # Remove NaN values from BrO
RHL          = RHL[ALL_Y8maskL] # Remove NaN values from WS
Sol_RHL      = SolL[ALL_Y8maskL] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Scan for NaN values
#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V1_17_Y1maskH   = np.isfinite(Sol_V1_17H) # Scan for NaN values
BrO_V1_17H      = BrO_V1_17H[V1_17_Y1maskH] # Remove NaN values from BrO
O3_V1_17H       = O3_V1_17H[V1_17_Y1maskH] # Remove NaN values from Sol
Sol_V1_17H      = Sol_V1_17H[V1_17_Y1maskH] # Remove NaN values from Sol
Temp_V1_17H     = Temp_V1_17H[V1_17_Y1maskH] # Remove NaN values from Sol
WD_vect_V1_17H  = WD_vect_V1_17H[V1_17_Y1maskH] # Remove NaN values from Sol
WS_V1_17H       = WS_V1_17H[V1_17_Y1maskH] # Remove NaN values from Sol
Hg0_V1_17H      = Hg0_V1_17H[V1_17_Y1maskH] # Remove NaN values from Sol
SI_V1_17H       = SI_V1_17H[V1_17_Y1maskH] # Remove NaN values from Sol

# Pass 2 (O3) 
V1_17_Y2maskH   = np.isfinite(O3_V1_17H) # Scan for NaN values
BrO_O3_V1_17H   = BrO_V1_17H[V1_17_Y2maskH] # Remove NaN values from BrO
O3_V1_17H       = O3_V1_17H[V1_17_Y2maskH] # Remove NaN values from Temp
Sol_O3_V1_17    = Sol_V1_17H[V1_17_Y2maskH] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_17_Y3maskH   = np.isfinite(Temp_V1_17H) # Scan for NaN values
BrO_Temp_V1_17H = BrO_V1_17H[V1_17_Y3maskH] # Remove NaN values from BrO
Temp_V1_17H     = Temp_V1_17H[V1_17_Y3maskH] # Remove NaN values from Temp
Sol_Temp_V1_17H = Sol_V1_17H[V1_17_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_17_Y4maskH   = np.isfinite(WD_vect_V1_17H) # Scan for NaN values
BrO_WD_V1_17H   = BrO_V1_17H[V1_17_Y4maskH] # Remove NaN values from BrO
WD_vect_V1_17H  = WD_vect_V1_17H[V1_17_Y4maskH] # Remove NaN values from WD_vect
Sol_WD_V1_17H   = Sol_V1_17H[V1_17_Y4maskH] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_17_Y5maskH   = np.isfinite(WS_V1_17H) # Scan for NaN values
BrO_WS_V1_17H   = BrO_V1_17H[V1_17_Y5maskH] # Remove NaN values from BrO
WS_V1_17H       = WS_V1_17H[V1_17_Y5maskH] # Remove NaN values from WS
Sol_WS_V1_17H   = Sol_V1_17H[V1_17_Y5maskH] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_17_Y6maskH   = np.isfinite(Hg0_V1_17H) # Scan for NaN values
BrO_Hg0_V1_17H  = BrO_V1_17H[V1_17_Y6maskH] # Remove NaN values from BrO
Hg0_V1_17H      = Hg0_V1_17H[V1_17_Y6maskH] # Remove NaN values from SI
Sol_Hg0_V1_17H  = Sol_V1_17H[V1_17_Y6maskH] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_17_Y7maskH   = np.isfinite(SI_V1_17H) # Scan for NaN values
BrO_SI_V1_17H   = BrO_V1_17H[V1_17_Y7maskH] # Remove NaN values from BrO
SI_SI_V1_17H    = SI_V1_17H[V1_17_Y7maskH] # Remove NaN values from SI
Sol_SI_V1_17H   = Sol_V1_17H[V1_17_Y7maskH] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_17_Y8maskH   = np.isfinite(RH_V1_17H) # Scan for NaN values
BrO_RH_V1_17H   = BrO_V1_17H[V1_17_Y8maskH] # Remove NaN values from BrO
RH_V1_17H       = RH_V1_17H[V1_17_Y8maskH] # Remove NaN values from WS
Sol_RH_V1_17H   = Sol_V1_17H[V1_17_Y8maskH] # Remove NaN values from Sol

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V2_17_Y1maskH   = np.isfinite(Sol_V2_17H) # Scan for NaN values
BrO_V2_17H      = BrO_V2_17H[V2_17_Y1maskH] # Remove NaN values from BrO
O3_V2_17H       = O3_V2_17H[V2_17_Y1maskH] # Remove NaN values from Sol
Sol_V2_17H      = Sol_V2_17H[V2_17_Y1maskH] # Remove NaN values from Sol
Temp_V2_17H     = Temp_V2_17H[V2_17_Y1maskH] # Remove NaN values from Sol
WD_vect_V2_17H  = WD_vect_V2_17H[V2_17_Y1maskH] # Remove NaN values from Sol
WS_V2_17H       = WS_V2_17H[V2_17_Y1maskH] # Remove NaN values from Sol
Hg0_V2_17H      = Hg0_V2_17H[V2_17_Y1maskH] # Remove NaN values from Sol
SI_V2_17H       = SI_V2_17H[V2_17_Y1maskH] # Remove NaN values from Sol

# Pass 2 (O3) 
V2_17_Y2maskH   = np.isfinite(O3_V2_17H) # Scan for NaN values
BrO_O3_V2_17H   = BrO_V2_17H[V2_17_Y2maskH] # Remove NaN values from BrO
O3_V2_17H       = O3_V2_17H[V2_17_Y2maskH] # Remove NaN values from Temp
Sol_O3_V2_17H   = Sol_V2_17H[V2_17_Y2maskH] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_17_Y3maskH   = np.isfinite(Temp_V2_17H) # Scan for NaN values
BrO_Temp_V2_17H = BrO_V2_17H[V2_17_Y3maskH] # Remove NaN values from BrO
Temp_V2_17H     = Temp_V2_17H[V2_17_Y3maskH] # Remove NaN values from Temp
Sol_Temp_V2_17H = Sol_V2_17H[V2_17_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_17_Y4maskH   = np.isfinite(WD_vect_V2_17H) # Scan for NaN values
BrO_WD_V2_17H   = BrO_V2_17H[V2_17_Y4maskH] # Remove NaN values from BrO
WD_vect_V2_17H  = WD_vect_V2_17H[V2_17_Y4maskH] # Remove NaN values from WD_vect
Sol_WD_V2_17H   = Sol_V2_17H[V2_17_Y4maskH] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_17_Y5maskH   = np.isfinite(WS_V2_17H) # Scan for NaN values
BrO_WS_V2_17H   = BrO_V2_17H[V2_17_Y5maskH] # Remove NaN values from BrO
WS_V2_17H       = WS_V2_17H[V2_17_Y5maskH] # Remove NaN values from WS
Sol_WS_V2_17H   = Sol_V2_17H[V2_17_Y5maskH] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_17_Y6maskH   = np.isfinite(Hg0_V2_17H) # Scan for NaN values
BrO_Hg0_V2_17H  = BrO_V2_17H[V2_17_Y6maskH] # Remove NaN values from BrO
Hg0_V2_17H      = Hg0_V2_17H[V2_17_Y6maskH] # Remove NaN values from SI
Sol_Hg0_V2_17H  = Sol_V2_17H[V2_17_Y6maskH] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_17_Y7maskH   = np.isfinite(SI_V2_17H) # Scan for NaN values
BrO_SI_V2_17H   = BrO_V2_17H[V2_17_Y7maskH] # Remove NaN values from BrO
SI_SI_V2_17H    = SI_V2_17H[V2_17_Y7maskH] # Remove NaN values from SI
Sol_SI_V2_17H   = Sol_V2_17H[V2_17_Y7maskH] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_17_Y8maskH   = np.isfinite(RH_V2_17H) # Scan for NaN values
BrO_RH_V2_17H   = BrO_V2_17H[V2_17_Y8maskH] # Remove NaN values from BrO
RH_V2_17H       = RH_V2_17H[V2_17_Y8maskH] # Remove NaN values from WS
Sol_RH_V2_17H   = Sol_V2_17H[V2_17_Y8maskH] # Remove NaN values from Sol

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V3_17_Y1maskH   = np.isfinite(Sol_V3_17H) # Scan for NaN values
BrO_V3_17H      = BrO_V3_17H[V3_17_Y1maskH] # Remove NaN values from BrO
O3_V3_17H       = O3_V3_17H[V3_17_Y1maskH] # Remove NaN values from Sol
Sol_V3_17H      = Sol_V3_17H[V3_17_Y1maskH] # Remove NaN values from Sol
Temp_V3_17H     = Temp_V3_17H[V3_17_Y1maskH] # Remove NaN values from Sol
WD_vect_V3_17H  = WD_vect_V3_17H[V3_17_Y1maskH] # Remove NaN values from Sol
WS_V3_17H       = WS_V3_17H[V3_17_Y1maskH] # Remove NaN values from Sol
Hg0_V3_17H      = Hg0_V3_17H[V3_17_Y1maskH] # Remove NaN values from Sol
SI_V3_17H       = SI_V3_17H[V3_17_Y1maskH] # Remove NaN values from Sol

# Pass 2 (O3) 
V3_17_Y2maskH   = np.isfinite(O3_V3_17H) # Scan for NaN values
BrO_O3_V3_17H   = BrO_V3_17H[V3_17_Y2maskH] # Remove NaN values from BrO
O3_V3_17H       = O3_V3_17H[V3_17_Y2maskH] # Remove NaN values from Temp
Sol_O3_V3_17H   = Sol_V3_17H[V3_17_Y2maskH] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_17_Y3maskH   = np.isfinite(Temp_V3_17H) # Scan for NaN values
BrO_Temp_V3_17H = BrO_V3_17H[V3_17_Y3maskH] # Remove NaN values from BrO
Temp_V3_17H     = Temp_V3_17H[V3_17_Y3maskH] # Remove NaN values from Temp
Sol_Temp_V3_17H = Sol_V3_17H[V3_17_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_17_Y4maskH   = np.isfinite(WD_vect_V3_17H) # Scan for NaN values
BrO_WD_V3_17H   = BrO_V3_17H[V3_17_Y4maskH] # Remove NaN values from BrO
WD_vect_V3_17H  = WD_vect_V3_17H[V3_17_Y4maskH] # Remove NaN values from WD_vect
Sol_WD_V3_17H   = Sol_V3_17H[V3_17_Y4maskH] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_17_Y5maskH   = np.isfinite(WS_V3_17H) # Scan for NaN values
BrO_WS_V3_17H   = BrO_V3_17H[V3_17_Y5maskH] # Remove NaN values from BrO
WS_V3_17H       = WS_V3_17H[V3_17_Y5maskH] # Remove NaN values from WS
Sol_WS_V3_17H   = Sol_V3_17H[V3_17_Y5maskH] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_17_Y6maskH   = np.isfinite(Hg0_V3_17H) # Scan for NaN values
BrO_Hg0_V3_17H  = BrO_V3_17H[V3_17_Y6maskH] # Remove NaN values from BrO
Hg0_V3_17H      = Hg0_V3_17H[V3_17_Y6maskH] # Remove NaN values from SI
Sol_Hg0_V3_17H  = Sol_V3_17H[V3_17_Y6maskH] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_17_Y7maskH   = np.isfinite(SI_V3_17H) # Scan for NaN values
BrO_SI_V3_17H   = BrO_V3_17H[V3_17_Y7maskH] # Remove NaN values from BrO
SI_SI_V3_17H    = SI_V3_17H[V3_17_Y7maskH] # Remove NaN values from SI
Sol_SI_V3_17H   = Sol_V3_17H[V3_17_Y7maskH] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_17_Y8maskH   = np.isfinite(RH_V3_17H) # Scan for NaN values
BrO_RH_V3_17H   = BrO_V3_17H[V3_17_Y8maskH] # Remove NaN values from BrO
RH_V3_17H       = RH_V3_17H[V3_17_Y8maskH] # Remove NaN values from WS
Sol_RH_V3_17H   = Sol_V3_17H[V3_17_Y8maskH] # Remove NaN values from Sol

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (Sol)
V1_18_Y1maskH   = np.isfinite(Sol_V1_18H) # Scan for NaN values
BrO_V1_18H      = BrO_V1_18H[V1_18_Y1maskH] # Remove NaN values from BrO
O3_V1_18H       = O3_V1_18H[V1_18_Y1maskH] # Remove NaN values from Sol
Sol_V1_18H      = Sol_V1_18H[V1_18_Y1maskH] # Remove NaN values from Sol
Temp_V1_18H     = Temp_V1_18H[V1_18_Y1maskH] # Remove NaN values from Sol
WD_vect_V1_18H  = WD_vect_V1_18H[V1_18_Y1maskH] # Remove NaN values from Sol
WS_V1_18H       = WS_V1_18H[V1_18_Y1maskH] # Remove NaN values from Sol
Hg0_V1_18H      = Hg0_V1_18H[V1_18_Y1maskH] # Remove NaN values from Sol
SI_V1_18H       = SI_V1_18H[V1_18_Y1maskH] # Remove NaN values from Sol

# Pass 2 (O3) 
V1_18_Y2maskH   = np.isfinite(O3_V1_18H) # Scan for NaN values
BrO_O3_V1_18H   = BrO_V1_18H[V1_18_Y2maskH] # Remove NaN values from BrO
O3_V1_18H       = O3_V1_18H[V1_18_Y2maskH] # Remove NaN values from Temp
Sol_O3_V1_18H   = Sol_V1_18H[V1_18_Y2maskH] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_18_Y3maskH   = np.isfinite(Temp_V1_18H) # Scan for NaN values
BrO_Temp_V1_18H = BrO_V1_18H[V1_18_Y3maskH] # Remove NaN values from BrO
Temp_V1_18H     = Temp_V1_18H[V1_18_Y3maskH] # Remove NaN values from Temp
Sol_Temp_V1_18H = Sol_V1_18H[V1_18_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_18_Y4maskH   = np.isfinite(WD_vect_V1_18H) # Scan for NaN values
BrO_WD_V1_18H   = BrO_V1_18H[V1_18_Y4maskH] # Remove NaN values from BrO
WD_vect_V1_18H  = WD_vect_V1_18H[V1_18_Y4maskH] # Remove NaN values from WD_vect
Sol_WD_V1_18H   = Sol_V1_18H[V1_18_Y4maskH] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_18_Y5maskH   = np.isfinite(WS_V1_18H) # Scan for NaN values
BrO_WS_V1_18H   = BrO_V1_18H[V1_18_Y5maskH] # Remove NaN values from BrO
WS_V1_18H       = WS_V1_18H[V1_18_Y5maskH] # Remove NaN values from WS
Sol_WS_V1_18H   = Sol_V1_18H[V1_18_Y5maskH] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_18_Y6maskH   = np.isfinite(Hg0_V1_18H) # Scan for NaN values
BrO_Hg0_V1_18H  = BrO_V1_18H[V1_18_Y6maskH] # Remove NaN values from BrO
Hg0_V1_18H      = Hg0_V1_18H[V1_18_Y6maskH] # Remove NaN values from SI
Sol_Hg0_V1_18H  = Sol_V1_18H[V1_18_Y6maskH] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_18_Y7maskH   = np.isfinite(SI_V1_18H) # Scan for NaN values
BrO_SI_V1_18H   = BrO_V1_18H[V1_18_Y7maskH] # Remove NaN values from BrO
SI_SI_V1_18H    = SI_V1_18H[V1_18_Y7maskH] # Remove NaN values from SI
Sol_SI_V1_18H   = Sol_V1_18H[V1_18_Y7maskH] # Remove NaN values from Sol

# Pass 8 (RH) 
V1_18_Y8maskH   = np.isfinite(RH_V1_18H) # Scan for NaN values
BrO_RH_V1_18H   = BrO_V1_18H[V1_18_Y8maskH] # Remove NaN values from BrO
RH_V1_18H       = RH_V1_18H[V1_18_Y8maskH] # Remove NaN values from WS
Sol_RH_V1_18H   = Sol_V1_18H[V1_18_Y8maskH] # Remove NaN values from Sol

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V2_18_Y1maskH   = np.isfinite(Sol_V2_18H) # Scan for NaN values
BrO_V2_18H      = BrO_V2_18H[V2_18_Y1maskH] # Remove NaN values from BrO
O3_V2_18H       = O3_V2_18H[V2_18_Y1maskH] # Remove NaN values from Sol
Sol_V2_18H      = Sol_V2_18H[V2_18_Y1maskH] # Remove NaN values from Sol
Temp_V2_18H     = Temp_V2_18H[V2_18_Y1maskH] # Remove NaN values from Sol
WD_vect_V2_18H  = WD_vect_V2_18H[V2_18_Y1maskH] # Remove NaN values from Sol
WS_V2_18H       = WS_V2_18H[V2_18_Y1maskH] # Remove NaN values from Sol
Hg0_V2_18H      = Hg0_V2_18H[V2_18_Y1maskH] # Remove NaN values from Sol
SI_V2_18H       = SI_V2_18H[V2_18_Y1maskH] # Remove NaN values from Sol

# Pass 2 (O3) 
V2_18_Y2maskH   = np.isfinite(O3_V2_18H) # Scan for NaN values
BrO_O3_V2_18H   = BrO_V2_18H[V2_18_Y2maskH] # Remove NaN values from BrO
O3_V2_18H       = O3_V2_18H[V2_18_Y2maskH] # Remove NaN values from Temp
Sol_O3_V2_18H   = Sol_V2_18H[V2_18_Y2maskH] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_18_Y3maskH   = np.isfinite(Temp_V2_18H) # Scan for NaN values
BrO_Temp_V2_18H = BrO_V2_18H[V2_18_Y3maskH] # Remove NaN values from BrO
Temp_V2_18H     = Temp_V2_18H[V2_18_Y3maskH] # Remove NaN values from Temp
Sol_Temp_V2_18H = Sol_V2_18H[V2_18_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_18_Y4maskH   = np.isfinite(WD_vect_V2_18H) # Scan for NaN values
BrO_WD_V2_18H   = BrO_V2_18H[V2_18_Y4maskH] # Remove NaN values from BrO
WD_vect_V2_18H  = WD_vect_V2_18H[V2_18_Y4maskH] # Remove NaN values from WD_vect
Sol_WD_V2_18H   = Sol_V2_18H[V2_18_Y4maskH] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_18_Y5maskH   = np.isfinite(WS_V2_18H) # Scan for NaN values
BrO_WS_V2_18H   = BrO_V2_18H[V2_18_Y5maskH] # Remove NaN values from BrO
WS_V2_18H       = WS_V2_18H[V2_18_Y5maskH] # Remove NaN values from WS
Sol_WS_V2_18H   = Sol_V2_18H[V2_18_Y5maskH] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_18_Y6maskH   = np.isfinite(Hg0_V2_18H) # Scan for NaN values
BrO_Hg0_V2_18H  = BrO_V2_18H[V2_18_Y6maskH] # Remove NaN values from BrO
Hg0_V2_18H      = Hg0_V2_18H[V2_18_Y6maskH] # Remove NaN values from SI
Sol_Hg0_V2_18H  = Sol_V2_18H[V2_18_Y6maskH] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_18_Y7maskH   = np.isfinite(SI_V2_18H) # Scan for NaN values
BrO_SI_V2_18H   = BrO_V2_18H[V2_18_Y7maskH] # Remove NaN values from BrO
SI_SI_V2_18H    = SI_V2_18H[V2_18_Y7maskH] # Remove NaN values from SI
Sol_SI_V2_18H   = Sol_V2_18H[V2_18_Y7maskH] # Remove NaN values from Sol

# Pass 8 (RH) 
V2_18_Y8maskH   = np.isfinite(RH_V2_18H) # Scan for NaN values
BrO_RH_V2_18H   = BrO_V2_18H[V2_18_Y8maskH] # Remove NaN values from BrO
RH_V2_18H       = RH_V2_18H[V2_18_Y8maskH] # Remove NaN values from WS
Sol_RH_V2_18H   = Sol_V2_18H[V2_18_Y8maskH] # Remove NaN values from Sol

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V3_18_Y1maskH   = np.isfinite(Sol_V3_18H) # Scan for NaN values
BrO_V3_18H      = BrO_V3_18H[V3_18_Y1maskH] # Remove NaN values from BrO
O3_V3_18H       = O3_V3_18H[V3_18_Y1maskH] # Remove NaN values from Sol
Sol_V3_18H      = Sol_V3_18H[V3_18_Y1maskH] # Remove NaN values from Sol
Temp_V3_18H     = Temp_V3_18H[V3_18_Y1maskH] # Remove NaN values from Sol
WD_vect_V3_18H  = WD_vect_V3_18H[V3_18_Y1maskH] # Remove NaN values from Sol
WS_V3_18H       = WS_V3_18H[V3_18_Y1maskH] # Remove NaN values from Sol
Hg0_V3_18H      = Hg0_V3_18H[V3_18_Y1maskH] # Remove NaN values from Sol
SI_V3_18H       = SI_V3_18H[V3_18_Y1maskH] # Remove NaN values from Sol

# Pass 2 (O3) 
V3_18_Y2maskH   = np.isfinite(O3_V3_18H) # Scan for NaN values
BrO_O3_V3_18H   = BrO_V3_18H[V3_18_Y2maskH] # Remove NaN values from BrO
O3_V3_18H       = O3_V3_18H[V3_18_Y2maskH] # Remove NaN values from Temp
Sol_O3_V3_18H   = Sol_V3_18H[V3_18_Y2maskH] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_18_Y3maskH   = np.isfinite(Temp_V3_18H) # Scan for NaN values
BrO_Temp_V3_18H = BrO_V3_18H[V3_18_Y3maskH] # Remove NaN values from BrO
Temp_V3_18H     = Temp_V3_18H[V3_18_Y3maskH] # Remove NaN values from Temp
Sol_Temp_V3_18H = Sol_V3_18H[V3_18_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_18_Y4maskH   = np.isfinite(WD_vect_V3_18H) # Scan for NaN values
BrO_WD_V3_18H   = BrO_V3_18H[V3_18_Y4maskH] # Remove NaN values from BrO
WD_vect_V3_18H  = WD_vect_V3_18H[V3_18_Y4maskH] # Remove NaN values from WD_vect
Sol_WD_V3_18H   = Sol_V3_18H[V3_18_Y4maskH] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_18_Y5maskH   = np.isfinite(WS_V3_18H) # Scan for NaN values
BrO_WS_V3_18H   = BrO_V3_18H[V3_18_Y5maskH] # Remove NaN values from BrO
WS_V3_18H       = WS_V3_18H[V3_18_Y5maskH] # Remove NaN values from WS
Sol_WS_V3_18H   = Sol_V3_18H[V3_18_Y5maskH] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_18_Y6maskH   = np.isfinite(Hg0_V3_18H) # Scan for NaN values
BrO_Hg0_V3_18H  = BrO_V3_18H[V3_18_Y6maskH] # Remove NaN values from BrO
Hg0_V3_18H      = Hg0_V3_18H[V3_18_Y6maskH] # Remove NaN values from SI
Sol_Hg0_V3_18H  = Sol_V3_18H[V3_18_Y6maskH] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_18_Y7maskH   = np.isfinite(SI_V3_18H) # Scan for NaN values
BrO_SI_V3_18H   = BrO_V3_18H[V3_18_Y7maskH] # Remove NaN values from BrO
SI_SI_V3_18H    = SI_V3_18H[V3_18_Y7maskH] # Remove NaN values from SI
Sol_SI_V3_18H   = Sol_V3_18H[V3_18_Y7maskH] # Remove NaN values from Sol

# Pass 8 (RH) 
V3_18_Y8maskH   = np.isfinite(RH_V3_18H) # Scan for NaN values
BrO_RH_V3_18H   = BrO_V3_18H[V3_18_Y8maskH] # Remove NaN values from BrO
RH_V3_18H       = RH_V3_18H[V3_18_Y8maskH] # Remove NaN values from WS
Sol_RH_V3_18H   = Sol_V3_18H[V3_18_Y8maskH] # Remove NaN values from Sol

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (Sol) 
SIPEXII_Y1maskH   = np.isfinite(Sol_SIPEXIIH) # Scan for NaN values
BrO_SIPEXIIH      = BrO_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from BrO
O3_SIPEXIIH       = O3_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from Sol
Sol_SIPEXIIH      = Sol_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from Sol
Temp_SIPEXIIH     = Temp_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from Sol
WD_vect_SIPEXIIH  = WD_vect_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from Sol
WS_SIPEXIIH       = WS_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from Sol
Hg0_SIPEXIIH      = Hg0_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from Sol
SI_SIPEXIIH       = SI_SIPEXIIH[SIPEXII_Y1maskH] # Remove NaN values from Sol

# Pass 2 (Temp) 
SIPEXII_Y2maskH   = np.isfinite(Temp_SIPEXIIH) # Scan for NaN values
BrO_Temp_SIPEXIIH = BrO_SIPEXIIH[SIPEXII_Y2maskH] # Remove NaN values from BrO
Temp_SIPEXIIH     = Temp_SIPEXIIH[SIPEXII_Y2maskH] # Remove NaN values from Temp
Sol_Temp_SIPEXIIH = Sol_SIPEXIIH[SIPEXII_Y2maskH] # Remove NaN values from Sol

# Pass 3 (WD_vect) 
SIPEXII_Y3maskH   = np.isfinite(WD_vect_SIPEXIIH) # Scan for NaN values
BrO_WD_SIPEXIIH   = BrO_SIPEXIIH[SIPEXII_Y3maskH] # Remove NaN values from BrO
WD_vect_SIPEXIIH  = WD_vect_SIPEXIIH[SIPEXII_Y3maskH] # Remove NaN values from WD_vect
Sol_WD_SIPEXIIH   = Sol_SIPEXIIH[SIPEXII_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WS) 
SIPEXII_Y4maskH   = np.isfinite(WS_SIPEXIIH) # Scan for NaN values
BrO_WS_SIPEXIIH   = BrO_SIPEXIIH[SIPEXII_Y4maskH] # Remove NaN values from BrO
WS_SIPEXIIH       = WS_SIPEXIIH[SIPEXII_Y4maskH] # Remove NaN values from WS
Sol_WS_SIPEXIIH   = Sol_SIPEXIIH[SIPEXII_Y4maskH] # Remove NaN values from Sol

# Pass 5 (Hg0) 
SIPEXII_Y5maskH   = np.isfinite(Hg0_SIPEXIIH) # Scan for NaN values
BrO_Hg0_SIPEXIIH  = BrO_SIPEXIIH[SIPEXII_Y5maskH] # Remove NaN values from BrO
Hg0_SIPEXIIH      = Hg0_SIPEXIIH[SIPEXII_Y5maskH] # Remove NaN values from SI
Sol_Hg0_SIPEXIIH  = Sol_SIPEXIIH[SIPEXII_Y5maskH] # Remove NaN values from Sol

# Pass 6 (SI Field) 
SIPEXII_Y6maskH   = np.isfinite(SI_SIPEXIIH) # Scan for NaN values
BrO_SI_SIPEXIIH   = BrO_SIPEXIIH[SIPEXII_Y6maskH] # Remove NaN values from BrO
SI_SI_SIPEXIIH    = SI_SIPEXIIH[SIPEXII_Y6maskH] # Remove NaN values from SI
Sol_SI_SIPEXIIH   = Sol_SIPEXIIH[SIPEXII_Y6maskH] # Remove NaN values from Sol

# Pass 7 (RH) 
SIPEXII_Y7maskH   = np.isfinite(RH_SIPEXIIH) # Scan for NaN values
BrO_RH_SIPEXIIH   = BrO_SIPEXIIH[SIPEXII_Y7maskH] # Remove NaN values from BrO
RH_SIPEXIIH       = RH_SIPEXIIH[SIPEXII_Y7maskH] # Remove NaN values from WS
Sol_RH_SIPEXIIH   = Sol_SIPEXIIH[SIPEXII_Y7maskH] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (Sol) 
ALL_Y1maskH   = np.isfinite(SolH) # Scan for NaN values
BrOH          = BrOH[ALL_Y1maskH] # Remove NaN values from BrO
O3H           = O3H[ALL_Y1maskH] # Remove NaN values from Sol
SolH          = SolH[ALL_Y1maskH] # Remove NaN values from Sol
TempH         = TempH[ALL_Y1maskH] # Remove NaN values from Sol
WD_vectH      = WD_vectH[ALL_Y1maskH] # Remove NaN values from Sol
WSH           = WSH[ALL_Y1maskH] # Remove NaN values from Sol
Hg0H          = Hg0H[ALL_Y1maskH] # Remove NaN values from Sol
SIH           = SIH[ALL_Y1maskH] # Remove NaN values from Sol

# Pass 2 (O3) 
ALL_Y2maskH   = np.isfinite(O3H) # Scan for NaN values
BrO_O3H       = BrOH[ALL_Y2maskH] # Remove NaN values from BrO
O3H           = O3H[ALL_Y2maskH] # Remove NaN values from Temp
Sol_O3H       = SolH[ALL_Y2maskH] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskH   = np.isfinite(TempH) # Scan for NaN values
BrO_TempH     = BrOH[ALL_Y3maskH] # Remove NaN values from BrO
TempH         = TempH[ALL_Y3maskH] # Remove NaN values from Temp
Sol_Temp      = SolH[ALL_Y3maskH] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskH   = np.isfinite(WD_vectH) # Scan for NaN values
BrO_WDH       = BrOH[ALL_Y4maskH] # Remove NaN values from BrO
WD_vectH      = WD_vectH[ALL_Y4maskH] # Remove NaN values from WD_vect
Sol_WDH       = SolH[ALL_Y4maskH] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskH   = np.isfinite(WSH) # Scan for NaN values
BrO_WSH       = BrOH[ALL_Y5maskH] # Remove NaN values from BrO
WSH           = WSH[ALL_Y5maskH] # Remove NaN values from WS
Sol_WSH       = SolH[ALL_Y5maskH] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskH   = np.isfinite(Hg0H) # Scan for NaN values
BrO_Hg0H      = BrOH[ALL_Y6maskH] # Remove NaN values from BrO
Hg0H          = Hg0H[ALL_Y6maskH] # Remove NaN values from SI
Sol_Hg0H      = SolH[ALL_Y6maskH] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskH   = np.isfinite(SIH) # Scan for NaN values
BrO_SIH       = BrOH[ALL_Y7maskH] # Remove NaN values from BrO
SI_SIH        = SIH[ALL_Y7maskH] # Remove NaN values from SI
Sol_SIH       = SolH[ALL_Y7maskH] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskH  = np.isfinite(RHH) # Scan for NaN values
BrO_RHH      = BrOH[ALL_Y8maskH] # Remove NaN values from BrO
RHH          = RHH[ALL_Y8maskH] # Remove NaN values from WS
Sol_RHH      = SolH[ALL_Y8maskH] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)
#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V1_17L, p_valueD1_V1_17L = stats.pearsonr(O3_V1_17L,BrO_O3_V1_17L)
slopeD1_V1_17L, interceptD1_V1_17L, rD1_V1_17L, pD1_V1_17L, std_errD1_V1_17L = stats.linregress(O3_V1_17L,BrO_O3_V1_17L)

# 2) Between Temp and BrO
r_rowD2_V1_17L, p_valueD2_V1_17L = stats.pearsonr(Temp_V1_17L,BrO_V1_17L)
slopeD2_V1_17L, interceptD2_V1_17L, rD2_V1_17L, pD2_V1_17L, std_errD2_V1_17L = stats.linregress(Temp_V1_17L,BrO_V1_17L)

# 3) Between Wind Direction and BrO
r_rowD3_V1_17L, p_valueD3_V1_17L = stats.pearsonr(WD_vect_V1_17L,BrO_WD_V1_17L)
slopeD3_V1_17L, interceptD3_V1_17L, rD3_V1_17L, pD3_V1_17L, std_errD3_V1_17L = stats.linregress(WD_vect_V1_17L,BrO_WD_V1_17L)

# 4) Between Wind Speed and BrO
r_rowD4_V1_17L, p_valueD4_V1_17L = stats.pearsonr(WS_V1_17L,BrO_WS_V1_17L)
slopeD4_V1_17L, interceptD4_V1_17L, rD4_V1_17L, pD4_V1_17L, std_errD4_V1_17L = stats.linregress(WS_V1_17L,BrO_WS_V1_17L)

# 5) Between Solar Radiation and BrO
r_rowD5_V1_17L, p_valueD5_V1_17L = stats.pearsonr(Sol_V1_17L,BrO_V1_17L)
slopeD5_V1_17L, interceptD5_V1_17L, rD5_V1_17L, pD5_V1_17L, std_errD5_V1_17L = stats.linregress(Sol_V1_17L,BrO_V1_17L)

# 6) Between Hg0 and BrO
r_rowD6_V1_17L, p_valueD6_V1_17L = stats.pearsonr(Hg0_V1_17L,BrO_Hg0_V1_17L)
slopeD6_V1_17L, interceptD6_V1_17L, rD6_V1_17L, pD6_V1_17L, std_errD6_V1_17L = stats.linregress(Hg0_V1_17L,BrO_Hg0_V1_17L)

# 7) Between SI and BrO
r_rowD7_V1_17L, p_valueD7_V1_17L = stats.pearsonr(SI_SI_V1_17L,BrO_SI_V1_17L)
slopeD7_V1_17L, interceptD7_V1_17L, rD7_V1_17L, pD7_V1_17L, std_errD7_V1_17L = stats.linregress(SI_SI_V1_17L,BrO_SI_V1_17L)

# 8) Between RH and BrO
r_rowD8_V1_17L, p_valueD8_V1_17L = stats.pearsonr(RH_V1_17L,BrO_RH_V1_17L)
slopeD8_V1_17L, interceptD8_V1_17L, rD8_V1_17L, pD8_V1_17L, std_errD8_V1_17L = stats.linregress(RH_V1_17L,BrO_RH_V1_17L)

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V2_17L, p_valueD1_V2_17L = stats.pearsonr(O3_V2_17L,BrO_O3_V2_17L)
slopeD1_V2_17L, interceptD1_V2_17L, rD1_V2_17L, pD1_V2_17L, std_errD1_V2_17L = stats.linregress(O3_V2_17L,BrO_O3_V2_17L)

# 2) Between Temp and BrO
r_rowD2_V2_17L, p_valueD2_V2_17L = stats.pearsonr(Temp_V2_17L,BrO_V2_17L)
slopeD2_V2_17L, interceptD2_V2_17L, rD2_V2_17L, pD2_V2_17L, std_errD2_V2_17L = stats.linregress(Temp_V2_17L,BrO_V2_17L)

# 3) Between Wind Direction and BrO
r_rowD3_V2_17L, p_valueD3_V2_17L = stats.pearsonr(WD_vect_V2_17L,BrO_WD_V2_17L)
slopeD3_V2_17L, interceptD3_V2_17L, rD3_V2_17L, pD3_V2_17L, std_errD3_V2_17L = stats.linregress(WD_vect_V2_17L,BrO_WD_V2_17L)

# 4) Between Wind Speed and BrO
r_rowD4_V2_17L, p_valueD4_V2_17L = stats.pearsonr(WS_V2_17L,BrO_WS_V2_17L)
slopeD4_V2_17L, interceptD4_V2_17L, rD4_V2_17L, pD4_V2_17L, std_errD4_V2_17L = stats.linregress(WS_V2_17L,BrO_WS_V2_17L)

# 5) Between Solar Radiation and BrO
r_rowD5_V2_17L, p_valueD5_V2_17L = stats.pearsonr(Sol_V2_17L,BrO_V2_17L)
slopeD5_V2_17L, interceptD5_V2_17L, rD5_V2_17L, pD5_V2_17L, std_errD5_V2_17L = stats.linregress(Sol_V2_17L,BrO_V2_17L)

# 6) Between Hg0 and BrO
r_rowD6_V2_17L, p_valueD6_V2_17L = stats.pearsonr(Hg0_V2_17L,BrO_Hg0_V2_17L)
slopeD6_V2_17L, interceptD6_V2_17L, rD6_V2_17L, pD6_V2_17L, std_errD6_V2_17L = stats.linregress(Hg0_V2_17L,BrO_Hg0_V2_17L)

# 7) Between SI and BrO
r_rowD7_V2_17L, p_valueD7_V2_17L = stats.pearsonr(SI_SI_V2_17L,BrO_SI_V2_17L)
slopeD7_V2_17L, interceptD7_V2_17L, rD7_V2_17L, pD7_V2_17L, std_errD7_V2_17L = stats.linregress(SI_SI_V2_17L,BrO_SI_V2_17L)

# 8) Between RH and BrO
r_rowD8_V2_17L, p_valueD8_V2_17L = stats.pearsonr(RH_V2_17L,BrO_RH_V2_17L)
slopeD8_V2_17L, interceptD8_V2_17L, rD8_V2_17L, pD8_V2_17L, std_errD8_V2_17L = stats.linregress(RH_V2_17L,BrO_RH_V2_17L)

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V3_17L, p_valueD1_V3_17L = stats.pearsonr(O3_V3_17L,BrO_O3_V3_17L)
slopeD1_V3_17L, interceptD1_V3_17L, rD1_V3_17L, pD1_V3_17L, std_errD1_V3_17L = stats.linregress(O3_V3_17L,BrO_O3_V3_17L)

# 2) Between Temp and BrO
r_rowD2_V3_17L, p_valueD2_V3_17L = stats.pearsonr(Temp_V3_17L,BrO_V3_17L)
slopeD2_V3_17L, interceptD2_V3_17L, rD2_V3_17L, pD2_V3_17L, std_errD2_V3_17L = stats.linregress(Temp_V3_17L,BrO_V3_17L)

# 3) Between Wind Direction and BrO
r_rowD3_V3_17L, p_valueD3_V3_17L = stats.pearsonr(WD_vect_V3_17L,BrO_WD_V3_17L)
slopeD3_V3_17L, interceptD3_V3_17L, rD3_V3_17L, pD3_V3_17L, std_errD3_V3_17L = stats.linregress(WD_vect_V3_17L,BrO_WD_V3_17L)

# 4) Between Wind Speed and BrO
r_rowD4_V3_17L, p_valueD4_V3_17L = stats.pearsonr(WS_V3_17L,BrO_WS_V3_17L)
slopeD4_V3_17L, interceptD4_V3_17L, rD4_V3_17L, pD4_V3_17L, std_errD4_V3_17L = stats.linregress(WS_V3_17L,BrO_WS_V3_17L)

# 5) Between Solar Radiation and BrO
r_rowD5_V3_17L, p_valueD5_V3_17L = stats.pearsonr(Sol_V3_17L,BrO_V3_17L)
slopeD5_V3_17L, interceptD5_V3_17L, rD5_V3_17L, pD5_V3_17L, std_errD5_V3_17L = stats.linregress(Sol_V3_17L,BrO_V3_17L)

# 6) Between Hg0 and BrO
r_rowD6_V3_17L, p_valueD6_V3_17L = stats.pearsonr(Hg0_V3_17L,BrO_Hg0_V3_17L)
slopeD6_V3_17L, interceptD6_V3_17L, rD6_V3_17L, pD6_V3_17L, std_errD6_V3_17L = stats.linregress(Hg0_V3_17L,BrO_Hg0_V3_17L)

# 7) Between SI and BrO
r_rowD7_V3_17L, p_valueD7_V3_17L = stats.pearsonr(SI_SI_V3_17L,BrO_SI_V3_17L)
slopeD7_V3_17L, interceptD7_V3_17L, rD7_V3_17L, pD7_V3_17L, std_errD7_V3_17L = stats.linregress(SI_SI_V3_17L,BrO_SI_V3_17L)

# 8) Between RH and BrO
r_rowD8_V3_17L, p_valueD8_V3_17L = stats.pearsonr(RH_V3_17L,BrO_RH_V3_17L)
slopeD8_V3_17L, interceptD8_V3_17L, rD8_V3_17L, pD8_V3_17L, std_errD8_V3_17L = stats.linregress(RH_V3_17L,BrO_RH_V3_17L)

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V1_18L, p_valueD1_V1_18L = stats.pearsonr(O3_V1_18L,BrO_O3_V1_18L)
slopeD1_V1_18L, interceptD1_V1_18L, rD1_V1_18L, pD1_V1_18L, std_errD1_V1_18L = stats.linregress(O3_V1_18L,BrO_O3_V1_18L)

# 2) Between Temp and BrO
r_rowD2_V1_18L, p_valueD2_V1_18L = stats.pearsonr(Temp_V1_18L,BrO_V1_18L)
slopeD2_V1_18L, interceptD2_V1_18L, rD2_V1_18L, pD2_V1_18L, std_errD2_V1_18L = stats.linregress(Temp_V1_18L,BrO_V1_18L)

# 3) Between Wind Direction and BrO
r_rowD3_V1_18L, p_valueD3_V1_18L = stats.pearsonr(WD_vect_V1_18L,BrO_WD_V1_18L)
slopeD3_V1_18L, interceptD3_V1_18L, rD3_V1_18L, pD3_V1_18L, std_errD3_V1_18L = stats.linregress(WD_vect_V1_18L,BrO_WD_V1_18L)

# 4) Between Wind Speed and BrO
r_rowD4_V1_18L, p_valueD4_V1_18L = stats.pearsonr(WS_V1_18L,BrO_WS_V1_18L)
slopeD4_V1_18L, interceptD4_V1_18L, rD4_V1_18L, pD4_V1_18L, std_errD4_V1_18L = stats.linregress(WS_V1_18L,BrO_WS_V1_18L)

# 5) Between Solar Radiation and BrO
r_rowD5_V1_18L, p_valueD5_V1_18L = stats.pearsonr(Sol_V1_18L,BrO_V1_18L)
slopeD5_V1_18L, interceptD5_V1_18L, rD5_V1_18L, pD5_V1_18L, std_errD5_V1_18L = stats.linregress(Sol_V1_18L,BrO_V1_18L)

# 6) Between Hg0 and BrO
r_rowD6_V1_18L, p_valueD6_V1_18L = stats.pearsonr(Hg0_V1_18L,BrO_Hg0_V1_18L)
slopeD6_V1_18L, interceptD6_V1_18L, rD6_V1_18L, pD6_V1_18L, std_errD6_V1_18L = stats.linregress(Hg0_V1_18L,BrO_Hg0_V1_18L)

# 7) Between SI and BrO
r_rowD7_V1_18L, p_valueD7_V1_18L = stats.pearsonr(SI_SI_V1_18L,BrO_SI_V1_18L)
slopeD7_V1_18L, interceptD7_V1_18L, rD7_V1_18L, pD7_V1_18L, std_errD7_V1_18L = stats.linregress(SI_SI_V1_18L,BrO_SI_V1_18L)

# 8) Between RH and BrO
r_rowD8_V1_18L, p_valueD8_V1_18L = stats.pearsonr(RH_V1_18L,BrO_RH_V1_18L)
slopeD8_V1_18L, interceptD8_V1_18L, rD8_V1_18L, pD8_V1_18L, std_errD8_V1_18L = stats.linregress(RH_V1_18L,BrO_RH_V1_18L)

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V2_18L, p_valueD1_V2_18L = stats.pearsonr(O3_V2_18L,BrO_O3_V2_18L)
slopeD1_V2_18L, interceptD1_V2_18L, rD1_V2_18L, pD1_V2_18L, std_errD1_V2_18L = stats.linregress(O3_V2_18L,BrO_O3_V2_18L)

# 2) Between Temp and BrO
r_rowD2_V2_18L, p_valueD2_V2_18L = stats.pearsonr(Temp_V2_18L,BrO_V2_18L)
slopeD2_V2_18L, interceptD2_V2_18L, rD2_V2_18L, pD2_V2_18L, std_errD2_V2_18L = stats.linregress(Temp_V2_18L,BrO_V2_18L)

# 3) Between Wind Direction and BrO
r_rowD3_V2_18L, p_valueD3_V2_18L = stats.pearsonr(WD_vect_V2_18L,BrO_WD_V2_18L)
slopeD3_V2_18L, interceptD3_V2_18L, rD3_V2_18L, pD3_V2_18L, std_errD3_V2_18L = stats.linregress(WD_vect_V2_18L,BrO_WD_V2_18L)

# 4) Between Wind Speed and BrO
r_rowD4_V2_18L, p_valueD4_V2_18L = stats.pearsonr(WS_V2_18L,BrO_WS_V2_18L)
slopeD4_V2_18L, interceptD4_V2_18L, rD4_V2_18L, pD4_V2_18L, std_errD4_V2_18L = stats.linregress(WS_V2_18L,BrO_WS_V2_18L)

# 5) Between Solar Radiation and BrO
r_rowD5_V2_18L, p_valueD5_V2_18L = stats.pearsonr(Sol_V2_18L,BrO_V2_18L)
slopeD5_V2_18L, interceptD5_V2_18L, rD5_V2_18L, pD5_V2_18L, std_errD5_V2_18L = stats.linregress(Sol_V2_18L,BrO_V2_18L)

# 6) Between Hg0 and BrO
r_rowD6_V2_18L, p_valueD6_V2_18L = stats.pearsonr(Hg0_V2_18L,BrO_Hg0_V2_18L)
slopeD6_V2_18L, interceptD6_V2_18L, rD6_V2_18L, pD6_V2_18L, std_errD6_V2_18L = stats.linregress(Hg0_V2_18L,BrO_Hg0_V2_18L)

# 7) Between SI and BrO
r_rowD7_V2_18L, p_valueD7_V2_18L = stats.pearsonr(SI_SI_V2_18L,BrO_SI_V2_18L)
slopeD7_V2_18L, interceptD7_V2_18L, rD7_V2_18L, pD7_V2_18L, std_errD7_V2_18L = stats.linregress(SI_SI_V2_18L,BrO_SI_V2_18L)

# 8) Between RH and BrO
r_rowD8_V2_18L, p_valueD8_V2_18L = stats.pearsonr(RH_V2_18L,BrO_RH_V2_18L)
slopeD8_V2_18L, interceptD8_V2_18L, rD8_V2_18L, pD8_V2_18L, std_errD8_V2_18L = stats.linregress(RH_V2_18L,BrO_RH_V2_18L)

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V3_18L, p_valueD1_V3_18L = stats.pearsonr(O3_V3_18L,BrO_O3_V3_18L)
slopeD1_V3_18L, interceptD1_V3_18L, rD1_V3_18L, pD1_V3_18L, std_errD1_V3_18L = stats.linregress(O3_V3_18L,BrO_O3_V3_18L)

# 2) Between Temp and BrO
r_rowD2_V3_18L, p_valueD2_V3_18L = stats.pearsonr(Temp_V1_18L,BrO_V1_18L)
slopeD2_V3_18L, interceptD2_V3_18L, rD2_V3_18L, pD2_V3_18L, std_errD2_V3_18L = stats.linregress(Temp_V3_18L,BrO_V3_18L)

# 3) Between Wind Direction and BrO
r_rowD3_V3_18L, p_valueD3_V3_18L = stats.pearsonr(WD_vect_V3_18L,BrO_WD_V3_18L)
slopeD3_V3_18L, interceptD3_V3_18L, rD3_V3_18L, pD3_V3_18L, std_errD3_V3_18L = stats.linregress(WD_vect_V3_18L,BrO_WD_V3_18L)

# 4) Between Wind Speed and BrO
r_rowD4_V3_18L, p_valueD4_V3_18L = stats.pearsonr(WS_V3_18L,BrO_WS_V3_18L)
slopeD4_V3_18L, interceptD4_V3_18L, rD4_V3_18L, pD4_V3_18L, std_errD4_V3_18L = stats.linregress(WS_V3_18L,BrO_WS_V3_18L)

# 5) Between Solar Radiation and BrO
r_rowD5_V3_18L, p_valueD5_V3_18L = stats.pearsonr(Sol_V3_18L,BrO_V3_18L)
slopeD5_V3_18L, interceptD5_V3_18L, rD5_V3_18L, pD5_V3_18L, std_errD5_V3_18L = stats.linregress(Sol_V3_18L,BrO_V3_18L)

# 6) Between Hg0 and BrO
r_rowD6_V3_18L, p_valueD6_V3_18L = stats.pearsonr(Hg0_V3_18L,BrO_Hg0_V3_18L)
slopeD6_V3_18L, interceptD6_V3_18L, rD6_V3_18L, pD6_V3_18L, std_errD6_V3_18L = stats.linregress(Hg0_V3_18L,BrO_Hg0_V3_18L)

# 7) Between SI and BrO
r_rowD7_V3_18L, p_valueD7_V3_18L = stats.pearsonr(SI_SI_V3_18L,BrO_SI_V3_18L)
slopeD7_V3_18L, interceptD7_V3_18L, rD7_V3_18L, pD7_V3_18L, std_errD7_V3_18L = stats.linregress(SI_SI_V3_18L,BrO_SI_V3_18L)

# 8) Between RH and BrO
r_rowD8_V3_18L, p_valueD8_V3_18L = stats.pearsonr(RH_V3_18L,BrO_RH_V3_18L)
slopeD8_V3_18L, interceptD8_V3_18L, rD8_V3_18L, pD8_V3_18L, std_errD8_V3_18L = stats.linregress(RH_V3_18L,BrO_RH_V3_18L)

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_SIPEXIIL, p_valueD1_SIPEXIIL = stats.pearsonr(O3_SIPEXIIL,BrO_SIPEXIIL)
slopeD1_SIPEXIIL, interceptD1_SIPEXIIL, rD1_SIPEXIIL, pD1_SIPEXIIL, std_errD1_SIPEXIIL = stats.linregress(O3_SIPEXIIL,BrO_SIPEXIIL)

# 2) Between Temp and BrO
r_rowD2_SIPEXIIL, p_valueD2_SIPEXIIL = stats.pearsonr(Temp_SIPEXIIL,BrO_SIPEXIIL)
slopeD2_SIPEXIIL, interceptD2_SIPEXIIL, rD2_SIPEXIIL, pD2_SIPEXIIL, std_errD2_SIPEXIIL = stats.linregress(Temp_SIPEXIIL,BrO_SIPEXIIL)

# 3) Between Wind Direction and BrO
r_rowD3_SIPEXIIL, p_valueD3_SIPEXIIL = stats.pearsonr(WD_vect_SIPEXIIL,BrO_WD_SIPEXIIL)
slopeD3_SIPEXIIL, interceptD3_SIPEXIIL, rD3_SIPEXIIL, pD3_SIPEXIIL, std_errD3_SIPEXIIL = stats.linregress(WD_vect_SIPEXIIL,BrO_WD_SIPEXIIL)

# 4) Between Wind Speed and BrO
r_rowD4_SIPEXIIL, p_valueD4_SIPEXIIL = stats.pearsonr(WS_SIPEXIIL,BrO_WS_SIPEXIIL)
slopeD4_SIPEXIIL, interceptD4_SIPEXIIL, rD4_SIPEXIIL, pD4_SIPEXIIL, std_errD4_SIPEXIIL = stats.linregress(WS_SIPEXIIL,BrO_WS_SIPEXIIL)

# 5) Between Solar Radiation and BrO
r_rowD5_SIPEXIIL, p_valueD5_SIPEXIIL = stats.pearsonr(Sol_SIPEXIIL,BrO_SIPEXIIL)
slopeD5_SIPEXIIL, interceptD5_SIPEXIIL, rD5_SIPEXIIL, pD5_SIPEXIIL, std_errD5_SIPEXIIL = stats.linregress(Sol_SIPEXIIL,BrO_SIPEXIIL)

# 6) Between Hg0 and BrO
r_rowD6_SIPEXIIL, p_valueD6_SIPEXIIL = stats.pearsonr(Hg0_SIPEXIIL,BrO_Hg0_SIPEXIIL)
slopeD6_SIPEXIIL, interceptD6_SIPEXIIL, rD6_SIPEXIIL, pD6_SIPEXIIL, std_errD6_SIPEXIIL = stats.linregress(Hg0_SIPEXIIL,BrO_Hg0_SIPEXIIL)

# 7) Between SI and BrO
r_rowD7_SIPEXIIL, p_valueD7_SIPEXIIL = stats.pearsonr(SI_SI_SIPEXIIL,BrO_SI_SIPEXIIL)
slopeD7_SIPEXIIL, interceptD7_SIPEXIIL, rD7_SIPEXIIL, pD7_SIPEXIIL, std_errD7_SIPEXIIL = stats.linregress(SI_SI_SIPEXIIL,BrO_SI_SIPEXIIL)

# 8) Between RH and BrO
r_rowD8_SIPEXIIL, p_valueD8_SIPEXIIL = stats.pearsonr(RH_SIPEXIIL,BrO_RH_SIPEXIIL)
slopeD8_SIPEXIIL, interceptD8_SIPEXIIL, rD8_SIPEXIIL, pD8_SIPEXIIL, std_errD8_SIPEXIIL = stats.linregress(RH_SIPEXIIL,BrO_RH_SIPEXIIL)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1L, p_valueD1L = stats.pearsonr(O3L,BrO_O3L)
slopeD1L, interceptD1L, rD1L, pD1L, std_errD1L = stats.linregress(O3L,BrO_O3L)

# 2) Between Temp and BrO
r_rowD2L, p_valueD2L = stats.pearsonr(TempL,BrOL)
slopeD2L, interceptD2L, rD2L, pD2L, std_errD2L = stats.linregress(TempL,BrOL)

# 3) Between Wind Direction and BrO
r_rowD3L, p_valueD3L = stats.pearsonr(WD_vectL,BrO_WDL)
slopeD3L, interceptD3L, rD3L, pD3L, std_errD3L = stats.linregress(WD_vectL,BrO_WDL)

# 4) Between Wind Speed and BrO
r_rowD4L, p_valueD4L = stats.pearsonr(WSL,BrO_WSL)
slopeD4L, interceptD4L, rD4L, pD4L, std_errD4L = stats.linregress(WSL,BrO_WSL)

# 5) Between Solar Radiation and BrO
r_rowD5L, p_valueD5L = stats.pearsonr(SolL,BrOL)
slopeD5L, interceptD5L, rD5L, pD5L, std_errD5L = stats.linregress(SolL,BrOL)

# 6) Between Hg0 and BrO
r_rowD6L, p_valueD6L = stats.pearsonr(Hg0L,BrO_Hg0L)
slopeD6L, interceptD6L, rD6L, pD6L, std_errD6L = stats.linregress(Hg0L,BrO_Hg0L)

# 7) Between SI and BrO
r_rowD7L, p_valueD7L = stats.pearsonr(SI_SIL,BrO_SIL)
slopeD7L, interceptD7L, rD7L, pD7L, std_errD7L = stats.linregress(SI_SIL,BrO_SIL)

# 8) Between SI and BrO
r_rowD8L, p_valueD8L = stats.pearsonr(RHL,BrO_RHL)
slopeD8L, interceptD8L, rD8L, pD8L, std_errD8L = stats.linregress(RHL,BrO_RHL)

#------------------------------------------------------------------------------
#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V1_17H, p_valueD1_V1_17H = stats.pearsonr(O3_V1_17H,BrO_O3_V1_17H)
slopeD1_V1_17H, interceptD1_V1_17H, rD1_V1_17H, pD1_V1_17H, std_errD1_V1_17H = stats.linregress(O3_V1_17H,BrO_O3_V1_17H)

# 2) Between Temp and BrO
r_rowD2_V1_17H, p_valueD2_V1_17H = stats.pearsonr(Temp_V1_17H,BrO_V1_17H)
slopeD2_V1_17H, interceptD2_V1_17H, rD2_V1_17H, pD2_V1_17H, std_errD2_V1_17H = stats.linregress(Temp_V1_17H,BrO_V1_17H)

# 3) Between Wind Direction and BrO
r_rowD3_V1_17H, p_valueD3_V1_17H = stats.pearsonr(WD_vect_V1_17H,BrO_WD_V1_17H)
slopeD3_V1_17H, interceptD3_V1_17H, rD3_V1_17H, pD3_V1_17H, std_errD3_V1_17H = stats.linregress(WD_vect_V1_17H,BrO_WD_V1_17H)

# 4) Between Wind Speed and BrO
r_rowD4_V1_17H, p_valueD4_V1_17H = stats.pearsonr(WS_V1_17H,BrO_WS_V1_17H)
slopeD4_V1_17H, interceptD4_V1_17H, rD4_V1_17H, pD4_V1_17H, std_errD4_V1_17H = stats.linregress(WS_V1_17H,BrO_WS_V1_17H)

# 5) Between Solar Radiation and BrO
r_rowD5_V1_17H, p_valueD5_V1_17H = stats.pearsonr(Sol_V1_17H,BrO_V1_17H)
slopeD5_V1_17H, interceptD5_V1_17H, rD5_V1_17H, pD5_V1_17H, std_errD5_V1_17H = stats.linregress(Sol_V1_17H,BrO_V1_17H)

# 6) Between Hg0 and BrO
r_rowD6_V1_17H, p_valueD6_V1_17H = stats.pearsonr(Hg0_V1_17H,BrO_Hg0_V1_17H)
slopeD6_V1_17H, interceptD6_V1_17H, rD6_V1_17H, pD6_V1_17H, std_errD6_V1_17H = stats.linregress(Hg0_V1_17H,BrO_Hg0_V1_17H)

# 7) Between SI and BrO
r_rowD7_V1_17H, p_valueD7_V1_17H = stats.pearsonr(SI_SI_V1_17H,BrO_SI_V1_17H)
slopeD7_V1_17H, interceptD7_V1_17H, rD7_V1_17H, pD7_V1_17H, std_errD7_V1_17H = stats.linregress(SI_SI_V1_17H,BrO_SI_V1_17H)

# 8) Between RH and BrO
r_rowD8_V1_17H, p_valueD8_V1_17H = stats.pearsonr(RH_V1_17H,BrO_RH_V1_17H)
slopeD8_V1_17H, interceptD8_V1_17H, rD8_V1_17H, pD8_V1_17H, std_errD8_V1_17H = stats.linregress(RH_V1_17H,BrO_RH_V1_17H)

##--------------------------------
## V2_17 (2017-18)
##--------------------------------
## 1) Between O3 and BrO
#r_rowD1_V2_17H, p_valueD1_V2_17H = stats.pearsonr(O3_V2_17H,BrO_O3_V2_17H)
#slopeD1_V2_17H, interceptD1_V2_17H, rD1_V2_17H, pD1_V2_17H, std_errD1_V2_17H = stats.linregress(O3_V2_17H,BrO_O3_V2_17H)
#
## 2) Between Temp and BrO
#r_rowD2_V2_17H, p_valueD2_V2_17H = stats.pearsonr(Temp_V2_17H,BrO_V2_17H)
#slopeD2_V2_17H, interceptD2_V2_17H, rD2_V2_17H, pD2_V2_17H, std_errD2_V2_17H = stats.linregress(Temp_V2_17H,BrO_V2_17H)
#
## 3) Between Wind Direction and BrO
#r_rowD3_V2_17H, p_valueD3_V2_17H = stats.pearsonr(WD_vect_V2_17H,BrO_WD_V2_17H)
#slopeD3_V2_17H, interceptD3_V2_17H, rD3_V2_17H, pD3_V2_17H, std_errD3_V2_17H = stats.linregress(WD_vect_V2_17H,BrO_WD_V2_17H)
#
## 4) Between Wind Speed and BrO
#r_rowD4_V2_17H, p_valueD4_V2_17H = stats.pearsonr(WS_V2_17H,BrO_WS_V2_17H)
#slopeD4_V2_17H, interceptD4_V2_17H, rD4_V2_17H, pD4_V2_17H, std_errD4_V2_17H = stats.linregress(WS_V2_17H,BrO_WS_V2_17H)
#
## 5) Between Solar Radiation and BrO
#r_rowD5_V2_17H, p_valueD5_V2_17H = stats.pearsonr(Sol_V2_17H,BrO_V2_17H)
#slopeD5_V2_17H, interceptD5_V2_17H, rD5_V2_17H, pD5_V2_17H, std_errD5_V2_17H = stats.linregress(Sol_V2_17H,BrO_V2_17H)
#
## 6) Between Hg0 and BrO
#r_rowD6_V2_17H, p_valueD6_V2_17H = stats.pearsonr(Hg0_V2_17H,BrO_Hg0_V2_17H)
#slopeD6_V2_17H, interceptD6_V2_17H, rD6_V2_17H, pD6_V2_17H, std_errD6_V2_17H = stats.linregress(Hg0_V2_17H,BrO_Hg0_V2_17H)
#
## 7) Between SI and BrO
#r_rowD7_V2_17H, p_valueD7_V2_17H = stats.pearsonr(SI_SI_V2_17H,BrO_SI_V2_17H)
#slopeD7_V2_17H, interceptD7_V2_17H, rD7_V2_17H, pD7_V2_17H, std_errD7_V2_17H = stats.linregress(SI_SI_V2_17H,BrO_SI_V2_17H)

# 8) Between RH and BrO
#r_rowD8_V2_17H, p_valueD8_V2_17H = stats.pearsonr(RH_V2_17H,BrO_RH_V2_17H)
#slopeD8_V2_17H, interceptD8_V2_17H, rD8_V2_17H, pD8_V2_17H, std_errD8_V2_17H = stats.linregress(RH_V2_17H,BrO_RH_V2_17H)

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V3_17H, p_valueD1_V3_17H = stats.pearsonr(O3_V3_17H,BrO_O3_V3_17H)
slopeD1_V3_17H, interceptD1_V3_17H, rD1_V3_17H, pD1_V3_17H, std_errD1_V3_17H = stats.linregress(O3_V3_17H,BrO_O3_V3_17H)

# 2) Between Temp and BrO
r_rowD2_V3_17H, p_valueD2_V3_17H = stats.pearsonr(Temp_V3_17H,BrO_V3_17H)
slopeD2_V3_17H, interceptD2_V3_17H, rD2_V3_17H, pD2_V3_17H, std_errD2_V3_17H = stats.linregress(Temp_V3_17H,BrO_V3_17H)

# 3) Between Wind Direction and BrO
r_rowD3_V3_17H, p_valueD3_V3_17H = stats.pearsonr(WD_vect_V3_17H,BrO_WD_V3_17H)
slopeD3_V3_17H, interceptD3_V3_17H, rD3_V3_17H, pD3_V3_17H, std_errD3_V3_17H = stats.linregress(WD_vect_V3_17H,BrO_WD_V3_17H)

# 4) Between Wind Speed and BrO
r_rowD4_V3_17H, p_valueD4_V3_17H = stats.pearsonr(WS_V3_17H,BrO_WS_V3_17H)
slopeD4_V3_17H, interceptD4_V3_17H, rD4_V3_17H, pD4_V3_17H, std_errD4_V3_17H = stats.linregress(WS_V3_17H,BrO_WS_V3_17H)

# 5) Between Solar Radiation and BrO
r_rowD5_V3_17H, p_valueD5_V3_17H = stats.pearsonr(Sol_V3_17H,BrO_V3_17H)
slopeD5_V3_17H, interceptD5_V3_17H, rD5_V3_17H, pD5_V3_17H, std_errD5_V3_17H = stats.linregress(Sol_V3_17H,BrO_V3_17H)

# 6) Between Hg0 and BrO
r_rowD6_V3_17H, p_valueD6_V3_17H = stats.pearsonr(Hg0_V3_17H,BrO_Hg0_V3_17H)
slopeD6_V3_17H, interceptD6_V3_17H, rD6_V3_17H, pD6_V3_17H, std_errD6_V3_17H = stats.linregress(Hg0_V3_17H,BrO_Hg0_V3_17H)

# 7) Between SI and BrO
r_rowD7_V3_17H, p_valueD7_V3_17H = stats.pearsonr(SI_SI_V3_17H,BrO_SI_V3_17H)
slopeD7_V3_17H, interceptD7_V3_17H, rD7_V3_17H, pD7_V3_17H, std_errD7_V3_17H = stats.linregress(SI_SI_V3_17H,BrO_SI_V3_17H)

# 8) Between RH and BrO
r_rowD8_V3_17H, p_valueD8_V3_17H = stats.pearsonr(RH_V3_17H,BrO_RH_V3_17H)
slopeD8_V3_17H, interceptD8_V3_17H, rD8_V3_17H, pD8_V3_17H, std_errD8_V3_17H = stats.linregress(RH_V3_17H,BrO_RH_V3_17H)

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V1_18H, p_valueD1_V1_18H = stats.pearsonr(O3_V1_18H,BrO_O3_V1_18H)
slopeD1_V1_18H, interceptD1_V1_18H, rD1_V1_18H, pD1_V1_18H, std_errD1_V1_18H = stats.linregress(O3_V1_18H,BrO_O3_V1_18H)

# 2) Between Temp and BrO
r_rowD2_V1_18H, p_valueD2_V1_18H = stats.pearsonr(Temp_V1_18H,BrO_V1_18H)
slopeD2_V1_18H, interceptD2_V1_18H, rD2_V1_18H, pD2_V1_18H, std_errD2_V1_18H = stats.linregress(Temp_V1_18H,BrO_V1_18H)

# 3) Between Wind Direction and BrO
r_rowD3_V1_18H, p_valueD3_V1_18H = stats.pearsonr(WD_vect_V1_18H,BrO_WD_V1_18H)
slopeD3_V1_18H, interceptD3_V1_18H, rD3_V1_18H, pD3_V1_18H, std_errD3_V1_18H = stats.linregress(WD_vect_V1_18H,BrO_WD_V1_18H)

# 4) Between Wind Speed and BrO
r_rowD4_V1_18H, p_valueD4_V1_18H = stats.pearsonr(WS_V1_18H,BrO_WS_V1_18H)
slopeD4_V1_18H, interceptD4_V1_18H, rD4_V1_18H, pD4_V1_18H, std_errD4_V1_18H = stats.linregress(WS_V1_18H,BrO_WS_V1_18H)

# 5) Between Solar Radiation and BrO
r_rowD5_V1_18H, p_valueD5_V1_18H = stats.pearsonr(Sol_V1_18H,BrO_V1_18H)
slopeD5_V1_18H, interceptD5_V1_18H, rD5_V1_18H, pD5_V1_18H, std_errD5_V1_18H = stats.linregress(Sol_V1_18H,BrO_V1_18H)

# 6) Between Hg0 and BrO
r_rowD6_V1_18H, p_valueD6_V1_18H = stats.pearsonr(Hg0_V1_18H,BrO_Hg0_V1_18H)
slopeD6_V1_18H, interceptD6_V1_18H, rD6_V1_18H, pD6_V1_18H, std_errD6_V1_18H = stats.linregress(Hg0_V1_18H,BrO_Hg0_V1_18H)

# 7) Between SI and BrO
r_rowD7_V1_18H, p_valueD7_V1_18H = stats.pearsonr(SI_SI_V1_18H,BrO_SI_V1_18H)
slopeD7_V1_18H, interceptD7_V1_18H, rD7_V1_18H, pD7_V1_18H, std_errD7_V1_18H = stats.linregress(SI_SI_V1_18H,BrO_SI_V1_18H)

# 8) Between RH and BrO
r_rowD8_V1_18H, p_valueD8_V1_18H = stats.pearsonr(RH_V1_18H,BrO_RH_V1_18H)
slopeD8_V1_18H, interceptD8_V1_18H, rD8_V1_18H, pD8_V1_18H, std_errD8_V1_18H = stats.linregress(RH_V1_18H,BrO_RH_V1_18H)

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V2_18H, p_valueD1_V2_18H = stats.pearsonr(O3_V2_18H,BrO_O3_V2_18H)
slopeD1_V2_18H, interceptD1_V2_18H, rD1_V2_18H, pD1_V2_18H, std_errD1_V2_18H = stats.linregress(O3_V2_18H,BrO_O3_V2_18H)

# 2) Between Temp and BrO
r_rowD2_V2_18H, p_valueD2_V2_18H = stats.pearsonr(Temp_V2_18H,BrO_V2_18H)
slopeD2_V2_18H, interceptD2_V2_18H, rD2_V2_18H, pD2_V2_18H, std_errD2_V2_18H = stats.linregress(Temp_V2_18H,BrO_V2_18H)

# 3) Between Wind Direction and BrO
r_rowD3_V2_18H, p_valueD3_V2_18H = stats.pearsonr(WD_vect_V2_18H,BrO_WD_V2_18H)
slopeD3_V2_18H, interceptD3_V2_18H, rD3_V2_18H, pD3_V2_18H, std_errD3_V2_18H = stats.linregress(WD_vect_V2_18H,BrO_WD_V2_18H)

# 4) Between Wind Speed and BrO
r_rowD4_V2_18H, p_valueD4_V2_18H = stats.pearsonr(WS_V2_18H,BrO_WS_V2_18H)
slopeD4_V2_18H, interceptD4_V2_18H, rD4_V2_18H, pD4_V2_18H, std_errD4_V2_18H = stats.linregress(WS_V2_18H,BrO_WS_V2_18H)

# 5) Between Solar Radiation and BrO
r_rowD5_V2_18H, p_valueD5_V2_18H = stats.pearsonr(Sol_V2_18H,BrO_V2_18H)
slopeD5_V2_18H, interceptD5_V2_18H, rD5_V2_18H, pD5_V2_18H, std_errD5_V2_18H = stats.linregress(Sol_V2_18H,BrO_V2_18H)

# 6) Between Hg0 and BrO
r_rowD6_V2_18H, p_valueD6_V2_18H = stats.pearsonr(Hg0_V2_18H,BrO_Hg0_V2_18H)
slopeD6_V2_18H, interceptD6_V2_18H, rD6_V2_18H, pD6_V2_18H, std_errD6_V2_18H = stats.linregress(Hg0_V2_18H,BrO_Hg0_V2_18H)

# 7) Between SI and BrO
r_rowD7_V2_18H, p_valueD7_V2_18H = stats.pearsonr(SI_SI_V2_18H,BrO_SI_V2_18H)
slopeD7_V2_18H, interceptD7_V2_18H, rD7_V2_18H, pD7_V2_18H, std_errD7_V2_18H = stats.linregress(SI_SI_V2_18H,BrO_SI_V2_18H)

# 8) Between RH and BrO
r_rowD8_V2_18H, p_valueD8_V2_18H = stats.pearsonr(RH_V2_18H,BrO_RH_V2_18H)
slopeD8_V2_18H, interceptD8_V2_18H, rD8_V2_18H, pD8_V2_18H, std_errD8_V2_18H = stats.linregress(RH_V2_18H,BrO_RH_V2_18H)

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V3_18H, p_valueD1_V3_18H = stats.pearsonr(O3_V3_18H,BrO_O3_V3_18H)
slopeD1_V3_18H, interceptD1_V3_18H, rD1_V3_18H, pD1_V3_18H, std_errD1_V3_18H = stats.linregress(O3_V3_18H,BrO_O3_V3_18H)

# 2) Between Temp and BrO
r_rowD2_V3_18H, p_valueD2_V3_18H = stats.pearsonr(Temp_V1_18H,BrO_V1_18H)
slopeD2_V3_18H, interceptD2_V3_18H, rD2_V3_18H, pD2_V3_18H, std_errD2_V3_18H = stats.linregress(Temp_V3_18H,BrO_V3_18H)

# 3) Between Wind Direction and BrO
r_rowD3_V3_18H, p_valueD3_V3_18H = stats.pearsonr(WD_vect_V3_18H,BrO_WD_V3_18H)
slopeD3_V3_18H, interceptD3_V3_18H, rD3_V3_18H, pD3_V3_18H, std_errD3_V3_18H = stats.linregress(WD_vect_V3_18H,BrO_WD_V3_18H)

# 4) Between Wind Speed and BrO
r_rowD4_V3_18H, p_valueD4_V3_18H = stats.pearsonr(WS_V3_18H,BrO_WS_V3_18H)
slopeD4_V3_18H, interceptD4_V3_18H, rD4_V3_18H, pD4_V3_18H, std_errD4_V3_18H = stats.linregress(WS_V3_18H,BrO_WS_V3_18H)

# 5) Between Solar Radiation and BrO
r_rowD5_V3_18H, p_valueD5_V3_18H = stats.pearsonr(Sol_V3_18H,BrO_V3_18H)
slopeD5_V3_18H, interceptD5_V3_18H, rD5_V3_18H, pD5_V3_18H, std_errD5_V3_18H = stats.linregress(Sol_V3_18H,BrO_V3_18H)

# 6) Between Hg0 and BrO
r_rowD6_V3_18H, p_valueD6_V3_18H = stats.pearsonr(Hg0_V3_18H,BrO_Hg0_V3_18H)
slopeD6_V3_18H, interceptD6_V3_18H, rD6_V3_18H, pD6_V3_18H, std_errD6_V3_18H = stats.linregress(Hg0_V3_18H,BrO_Hg0_V3_18H)

# 7) Between SI and BrO
r_rowD7_V3_18H, p_valueD7_V3_18H = stats.pearsonr(SI_SI_V3_18H,BrO_SI_V3_18H)
slopeD7_V3_18H, interceptD7_V3_18H, rD7_V3_18H, pD7_V3_18H, std_errD7_V3_18H = stats.linregress(SI_SI_V3_18H,BrO_SI_V3_18H)

# 8) Between RH and BrO
r_rowD8_V3_18H, p_valueD8_V3_18H = stats.pearsonr(RH_V3_18H,BrO_RH_V3_18H)
slopeD8_V3_18H, interceptD8_V3_18H, rD8_V3_18H, pD8_V3_18H, std_errD8_V3_18H = stats.linregress(RH_V3_18H,BrO_RH_V3_18H)

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_SIPEXIIH, p_valueD1_SIPEXIIH = stats.pearsonr(O3_SIPEXIIH,BrO_SIPEXIIH)
slopeD1_SIPEXIIH, interceptD1_SIPEXIIH, rD1_SIPEXIIH, pD1_SIPEXIIH, std_errD1_SIPEXIIH = stats.linregress(O3_SIPEXIIH,BrO_SIPEXIIH)

# 2) Between Temp and BrO
r_rowD2_SIPEXIIH, p_valueD2_SIPEXIIH = stats.pearsonr(Temp_SIPEXIIH,BrO_SIPEXIIH)
slopeD2_SIPEXIIH, interceptD2_SIPEXIIH, rD2_SIPEXIIH, pD2_SIPEXIIH, std_errD2_SIPEXIIH = stats.linregress(Temp_SIPEXIIH,BrO_SIPEXIIH)

# 3) Between Wind Direction and BrO
r_rowD3_SIPEXIIH, p_valueD3_SIPEXIIH = stats.pearsonr(WD_vect_SIPEXIIH,BrO_WD_SIPEXIIH)
slopeD3_SIPEXIIH, interceptD3_SIPEXIIH, rD3_SIPEXIIH, pD3_SIPEXIIH, std_errD3_SIPEXIIH = stats.linregress(WD_vect_SIPEXIIH,BrO_WD_SIPEXIIH)

# 4) Between Wind Speed and BrO
r_rowD4_SIPEXIIH, p_valueD4_SIPEXIIH = stats.pearsonr(WS_SIPEXIIH,BrO_WS_SIPEXIIH)
slopeD4_SIPEXIIH, interceptD4_SIPEXIIH, rD4_SIPEXIIH, pD4_SIPEXIIH, std_errD4_SIPEXIIH = stats.linregress(WS_SIPEXIIH,BrO_WS_SIPEXIIH)

# 5) Between Solar Radiation and BrO
r_rowD5_SIPEXIIH, p_valueD5_SIPEXIIH = stats.pearsonr(Sol_SIPEXIIH,BrO_SIPEXIIH)
slopeD5_SIPEXIIH, interceptD5_SIPEXIIH, rD5_SIPEXIIH, pD5_SIPEXIIH, std_errD5_SIPEXIIH = stats.linregress(Sol_SIPEXIIH,BrO_SIPEXIIH)

# 6) Between Hg0 and BrO
r_rowD6_SIPEXIIH, p_valueD6_SIPEXIIH = stats.pearsonr(Hg0_SIPEXIIH,BrO_Hg0_SIPEXIIH)
slopeD6_SIPEXIIH, interceptD6_SIPEXIIH, rD6_SIPEXIIH, pD6_SIPEXIIH, std_errD6_SIPEXIIH = stats.linregress(Hg0_SIPEXIIH,BrO_Hg0_SIPEXIIH)

# 7) Between SI and BrO
r_rowD7_SIPEXIIH, p_valueD7_SIPEXIIH = stats.pearsonr(SI_SI_SIPEXIIH,BrO_SI_SIPEXIIH)
slopeD7_SIPEXIIH, interceptD7_SIPEXIIH, rD7_SIPEXIIH, pD7_SIPEXIIH, std_errD7_SIPEXIIH = stats.linregress(SI_SI_SIPEXIIH,BrO_SI_SIPEXIIH)

# 8) Between RH and BrO
r_rowD8_SIPEXIIH, p_valueD8_SIPEXIIH = stats.pearsonr(RH_SIPEXIIH,BrO_RH_SIPEXIIH)
slopeD8_SIPEXIIH, interceptD8_SIPEXIIH, rD8_SIPEXIIH, pD8_SIPEXIIH, std_errD8_SIPEXIIH = stats.linregress(RH_SIPEXIIH,BrO_RH_SIPEXIIH)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1H, p_valueD1H = stats.pearsonr(O3H,BrO_O3H)
slopeD1H, interceptD1H, rD1H, pD1H, std_errD1H = stats.linregress(O3H,BrO_O3H)

# 2) Between Temp and BrO
r_rowD2H, p_valueD2H = stats.pearsonr(TempH,BrOH)
slopeD2H, interceptD2H, rD2H, pD2H, std_errD2H = stats.linregress(TempH,BrOH)

# 3) Between Wind Direction and BrO
r_rowD3H, p_valueD3H = stats.pearsonr(WD_vectH,BrO_WDH)
slopeD3H, interceptD3H, rD3H, pD3H, std_errD3H = stats.linregress(WD_vectH,BrO_WDH)

# 4) Between Wind Speed and BrO
r_rowD4H, p_valueD4H = stats.pearsonr(WSH,BrO_WSH)
slopeD4H, interceptD4H, rD4H, pD4H, std_errD4H = stats.linregress(WSH,BrO_WSH)

# 5) Between Solar Radiation and BrO
r_rowD5H, p_valueD5H = stats.pearsonr(SolH,BrOH)
slopeD5H, interceptD5H, rD5H, pD5H, std_errD5H = stats.linregress(SolH,BrOH)

# 6) Between Hg0 and BrO
r_rowD6H, p_valueD6H = stats.pearsonr(Hg0H,BrO_Hg0H)
slopeD6H, interceptD6H, rD6H, pD6H, std_errD6H = stats.linregress(Hg0H,BrO_Hg0H)

# 7) Between SI and BrO
r_rowD7H, p_valueD7H = stats.pearsonr(SI_SIH,BrO_SIH)
slopeD7H, interceptD7H, rD7H, pD7H, std_errD7H = stats.linregress(SI_SIH,BrO_SIH)

# 8) Between SI and BrO
r_rowD8H, p_valueD8H = stats.pearsonr(RHH,BrO_RHH)
slopeD8H, interceptD8H, rD8H, pD8H, std_errD8H = stats.linregress(RHH,BrO_RHH)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs O3)

fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_V1_17L,   BrO_O3_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(O3_V2_17L,   BrO_O3_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(O3_V3_17L,   BrO_O3_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(O3_V1_18L,   BrO_O3_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(O3_V2_18L,   BrO_O3_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(O3_V3_18L,   BrO_O3_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(O3_SIPEXIIL, BrO_SIPEXIIL,    edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(O3L, interceptD1L + slopeD1L * O3L, color='black')

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V1_17L))+" $\pm$"+str("%7.4f"%(std_errD1_V1_17L))+" pptv, r: "+str("%7.4f"%(rD1_V1_17L))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 1
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_V1_17H,   BrO_O3_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(O3_V2_17H,   BrO_O3_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(O3_V3_17H,   BrO_O3_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(O3_V1_18H,   BrO_O3_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(O3_V2_18H,   BrO_O3_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(O3_V3_18H,   BrO_O3_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(O3_SIPEXIIH, BrO_SIPEXIIH,    edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(O3H, interceptD1H + slopeD1H * O3H, color='black')

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V1_17H))+" $\pm$"+str("%7.4f"%(std_errD1_V1_17H))+" pptv, r: "+str("%7.4f"%(rD1_V1_17H))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Temperature)

fig2 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 2
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_V1_17L,   BrO_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Temp_V2_17L,   BrO_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Temp_V3_17L,   BrO_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Temp_V1_18L,   BrO_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Temp_V2_18L,   BrO_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Temp_V3_18L,   BrO_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(Temp_SIPEXIIL, BrO_SIPEXIIL, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(TempL, interceptD2L + slopeD2L * TempL, color='black') 

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V1_17L))+" $\pm$"+str("%7.4f"%(std_errD2_V1_17L))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V1_17L))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 2
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_V1_17H,   BrO_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Temp_V2_17H,   BrO_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Temp_V3_17H,   BrO_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Temp_V1_18H,   BrO_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Temp_V2_18H,   BrO_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Temp_V3_18H,   BrO_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(Temp_SIPEXIIH, BrO_SIPEXIIH, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(TempH, interceptD2H + slopeD2H * TempH, color='black') 

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V1_17H))+" $\pm$"+str("%7.4f"%(std_errD2_V1_17H))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V1_17H))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Direction)

fig3 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 3
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_V1_17L,   BrO_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(WD_vect_V2_17L,   BrO_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WD_vect_V3_17L,   BrO_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WD_vect_V1_18L,   BrO_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WD_vect_V2_18L,   BrO_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WD_vect_V3_18L,   BrO_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(WD_vect_SIPEXIIL, BrO_SIPEXIIL, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WD_vectL, interceptD3L + slopeD3L * WD_vectL, color='black')

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V1_17L))+" $\pm$"+str("%7.4f"%(std_errD3_V1_17L))+" $^\circ$, r: "+str("%7.4f"%(rD3_V1_17L))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 3
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_V1_17H,   BrO_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(WD_vect_V2_17H,   BrO_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WD_vect_V3_17H,   BrO_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WD_vect_V1_18H,   BrO_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WD_vect_V2_18H,   BrO_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WD_vect_V3_18H,   BrO_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(WD_vect_SIPEXIIH, BrO_SIPEXIIH, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WD_vectH, interceptD3H + slopeD3H * WD_vectH, color='black')

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V1_17H))+" $\pm$"+str("%7.4f"%(std_errD3_V1_17H))+" $^\circ$, r: "+str("%7.4f"%(rD3_V1_17H))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Speed)

fig4 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 4
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_V1_17L,   BrO_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(WS_V2_17L,   BrO_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WS_V3_17L,   BrO_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WS_V1_18L,   BrO_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WS_V2_18L,   BrO_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WS_V3_18L,   BrO_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(WS_SIPEXIIL, BrO_SIPEXIIL, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WSL, interceptD4L + slopeD4L * WSL, color='black')

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4L))+" $\pm$"+str("%7.4f"%(std_errD4L))+" m/s, r: "+str("%7.4f"%(rD4L))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 4
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_V1_17H,   BrO_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(WS_V2_17H,   BrO_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(WS_V3_17H,   BrO_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(WS_V1_18H,   BrO_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(WS_V2_18H,   BrO_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(WS_V3_18H,   BrO_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(WS_SIPEXIIH, BrO_SIPEXIIH, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WSH, interceptD4H + slopeD4H * WSH, color='black')

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4H))+" $\pm$"+str("%7.4f"%(std_errD4H))+" m/s, r: "+str("%7.4f"%(rD4H))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Solar Radiation)

fig5 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 5
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_V1_17L,   BrO_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Sol_V2_17L,   BrO_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Sol_V3_17L,   BrO_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Sol_V1_18L,   BrO_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Sol_V2_18L,   BrO_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Sol_V3_18L,   BrO_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(Sol_SIPEXIIL, BrO_SIPEXIIL, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(SolL, interceptD5L + slopeD5L * SolL, color='black')

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5L))+" $\pm$"+str("%7.4f"%(std_errD5L))+" W/m$^2$, r: "+str("%7.4f"%(rD5L))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 5
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_V1_17H,   BrO_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Sol_V2_17H,   BrO_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Sol_V3_17H,   BrO_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Sol_V1_18H,   BrO_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Sol_V2_18H,   BrO_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Sol_V3_18H,   BrO_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(Sol_SIPEXIIH, BrO_SIPEXIIH, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(SolH, interceptD5H + slopeD5H * SolH, color='black')

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5H))+" $\pm$"+str("%7.4f"%(std_errD5H))+" W/m$^2$, r: "+str("%7.4f"%(rD5H))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Hg0)

fig6 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 6
ax = plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_V1_17L,   BrO_Hg0_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(Hg0_V2_17L,   BrO_Hg0_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Hg0_V3_17L,   BrO_Hg0_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Hg0_V1_18L,   BrO_Hg0_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Hg0_V2_18L,   BrO_Hg0_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Hg0_V3_18L,   BrO_Hg0_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(Hg0_SIPEXIIL, BrO_Hg0_SIPEXIIL, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(Hg0L, interceptD6L + slopeD6L * Hg0L, color='black')

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6L))+" $\pm$ "+str("%7.4f"%(std_errD6L))+" ng/m$^2$, r: "+str("%7.4f"%(rD6L))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 6
ax = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_V1_17H,   BrO_Hg0_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(Hg0_V2_17H,   BrO_Hg0_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(Hg0_V3_17H,   BrO_Hg0_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(Hg0_V1_18H,   BrO_Hg0_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(Hg0_V2_18H,   BrO_Hg0_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(Hg0_V3_18H,   BrO_Hg0_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(Hg0_SIPEXIIH, BrO_Hg0_SIPEXIIH, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(Hg0H, interceptD6H + slopeD6H * Hg0H, color='black')

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=15)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6H))+" $\pm$ "+str("%7.4f"%(std_errD6H))+" ng/m$^2$, r: "+str("%7.4f"%(rD6H))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Sea Ice)

fig7 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 7
ax = plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_V1_17L,   BrO_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(SI_V2_17L,   BrO_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(SI_V3_17L,   BrO_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(SI_V1_18L,   BrO_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(SI_V2_18L,   BrO_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(SI_V3_18L,   BrO_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(SI_SIPEXIIL, BrO_SIPEXIIL, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SIL, interceptD7L + slopeD7L * SIL, color='black')

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=13)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7L))+" $\pm$"+str("%7.4f"%(std_errD7L))+" %, r: "+str("%7.4f"%(rD7L))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 7
ax = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_V1_17H,   BrO_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(SI_V2_17H,   BrO_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(SI_V3_17H,   BrO_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(SI_V1_18H,   BrO_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(SI_V2_18H,   BrO_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(SI_V3_18H,   BrO_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(SI_SIPEXIIH, BrO_SIPEXIIH, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SIH, interceptD7H + slopeD7H * SIH, color='black')

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=13)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7H))+" $\pm$"+str("%7.4f"%(std_errD7H))+" %, r: "+str("%7.4f"%(rD7H))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Sea Ice)

fig8 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
# Graph 8
ax = plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_V1_17L,   BrO_RH_V1_17L,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
ax.scatter(RH_V2_17L,   BrO_RH_V2_17L,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(RH_V3_17L,   BrO_RH_V3_17L,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(RH_V1_18L,   BrO_RH_V1_18L,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(RH_V2_18L,   BrO_RH_V2_18L,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(RH_V3_18L,   BrO_RH_V3_18L,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(RH_SIPEXIIL, BrO_RH_SIPEXIIL, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SIL, interceptD7L + slopeD7L * SIL, color='black')

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
plt.title('Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=13)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8L))+" $\pm$"+str("%7.4f"%(std_errD8L))+" %, r: "+str("%7.4f"%(rD8L))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
# Graph 8
ax = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_V1_17H,   BrO_RH_V1_17H,   edgecolors='none', marker='o', c='black',  label='V1 (2017-18)')
#ax.scatter(RH_V2_17H,   BrO_RH_V2_17H,   edgecolors='none', marker='o', c='red',    label='V2 (2017-18)')
ax.scatter(RH_V3_17H,   BrO_RH_V3_17H,   edgecolors='none', marker='o', c='blue',   label='V3 (2017-18)')
ax.scatter(RH_V1_18H,   BrO_RH_V1_18H,   edgecolors='none', marker='o', c='green',  label='V1 (2018-19)')
ax.scatter(RH_V2_18H,   BrO_RH_V2_18H,   edgecolors='none', marker='o', c='yellow', label='V2 (2018-19)')
ax.scatter(RH_V3_18H,   BrO_RH_V3_18H,   edgecolors='none', marker='o', c='purple', label='V3 (2018-19)')
ax.scatter(RH_SIPEXIIH, BrO_RH_SIPEXIIH, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SIH, interceptD7H + slopeD7H * SIH, color='black')

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
plt.title('High Wind Speed (>7 m/s)', fontsize=25, pad=10)

# Plot the legend
#legend = ax.legend(loc='upper right', fontsize=13)
legend = ax.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize=13)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8H))+" $\pm$"+str("%7.4f"%(std_errD8H))+" %, r: "+str("%7.4f"%(rD8H))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)
