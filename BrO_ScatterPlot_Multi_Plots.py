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
V1_17_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_17_Data.csv',header=0,encoding = 'unicode_escape')
V1_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv')
V1_17_SI  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv')
V1_17_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv')
V1_17_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv')

# V2_17 (2017-18)
V2_17_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_17_Data.csv',header=0,encoding = 'unicode_escape')
V2_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv')
V2_17_SI  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv')
V2_17_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V2_Hg0_QAQC_17-18.csv')
V2_17_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv')

# V3_17 (2017-18)
V3_17_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_17_Data.csv',header=0,encoding = 'unicode_escape')
V3_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv')
V3_17_SI  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv')
V3_17_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V3_Hg0_QAQC_17-18.csv')
V3_17_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv')

# V1_18 (2018-19)
V1_18_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_18_Data.csv',header=0,encoding = 'unicode_escape')
V1_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv')
V1_18_SI  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv')
V1_18_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V1_Hg0_QAQC_18-19.csv')
V1_18_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V1_O3_1min.csv')

# V2_18 (2018-19)
V2_18_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_18_Data.csv',header=0,encoding = 'unicode_escape')
V2_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv')
V2_18_SI  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv')
V2_18_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V2_Hg0_QAQC_18-19.csv')
V2_18_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V2_O3_1min.csv')

# V3_18 (2018-19)
V3_18_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_18_Data.csv',header=0,encoding = 'unicode_escape')
V3_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv')
V3_18_SI  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv')
V3_18_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/CAMMPCAN_V3_Hg0_QAQC_18-19.csv')
V3_18_O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V3_O3_1min.csv')

# SIPEXII 2012
SIPEXII_BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/SIPEXII_Data.csv',header=0,encoding = 'unicode_escape')
SIPEXII_Met = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_underway_60.csv') #SIPEXII_underway_60.csv') 
SIPEXII_SI  = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv')
SIPEXII_Hg  = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_QAQC_2012.csv')
SIPEXII_O3  = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv')

#------------------------------------------------------------------------------
# Set the date

# V1_17 (2017-18)
V1_17_BrO['DateTime'] = pd.to_datetime(V1_17_BrO['DateTime'], dayfirst=True)
V1_17_Met['DateTime'] = pd.to_datetime(V1_17_Met['DateTime'], dayfirst=True)
V1_17_SI['DateTime']  = pd.to_datetime(V1_17_SI['DateTime'],  dayfirst=True)
V1_17_Hg['DateTime']  = pd.to_datetime(V1_17_Hg['DateTime'],  dayfirst=True)
V1_17_O3['DateTime']  = pd.to_datetime(V1_17_O3['DateTime'],  dayfirst=True)

# V2_17 (2017-18)
V2_17_BrO['DateTime'] = pd.to_datetime(V2_17_BrO['DateTime'], dayfirst=True)
V2_17_Met['DateTime'] = pd.to_datetime(V2_17_Met['DateTime'], dayfirst=True)
V2_17_SI['DateTime']  = pd.to_datetime(V2_17_SI['DateTime'],  dayfirst=True)
V2_17_Hg['DateTime']  = pd.to_datetime(V2_17_Hg['DateTime'],  dayfirst=True)
V2_17_O3['DateTime']  = pd.to_datetime(V2_17_O3['DateTime'],  dayfirst=True)

# V3_17 (2017-18)
V3_17_BrO['DateTime'] = pd.to_datetime(V3_17_BrO['DateTime'], dayfirst=True)
V3_17_Met['DateTime'] = pd.to_datetime(V3_17_Met['DateTime'], dayfirst=True)
V3_17_SI['DateTime']  = pd.to_datetime(V3_17_SI['DateTime'],  dayfirst=True)
V3_17_Hg['DateTime']  = pd.to_datetime(V3_17_Hg['DateTime'],  dayfirst=True)
V3_17_O3['DateTime']  = pd.to_datetime(V3_17_O3['DateTime'],  dayfirst=True)

# V1_18 (2018-19)
V1_18_BrO['DateTime'] = pd.to_datetime(V1_18_BrO['DateTime'], dayfirst=True)
V1_18_Met['DateTime'] = pd.to_datetime(V1_18_Met['DateTime'], dayfirst=True)
V1_18_SI['DateTime']  = pd.to_datetime(V1_18_SI['DateTime'],  dayfirst=True)
V1_18_Hg['DateTime']  = pd.to_datetime(V1_18_Hg['DateTime'],  dayfirst=True)
V1_18_O3['DateTime']  = pd.to_datetime(V1_18_O3['DateTime'],  dayfirst=True)

# V2_18 (2018-19)
V2_18_BrO['DateTime'] = pd.to_datetime(V2_18_BrO['DateTime'], dayfirst=True)
V2_18_Met['DateTime'] = pd.to_datetime(V2_18_Met['DateTime'], dayfirst=True)
V2_18_SI['DateTime']  = pd.to_datetime(V2_18_SI['DateTime'],  dayfirst=True)
V2_18_Hg['DateTime']  = pd.to_datetime(V2_18_Hg['DateTime'],  dayfirst=True)
V2_18_O3['DateTime']  = pd.to_datetime(V2_18_O3['DateTime'],  dayfirst=True)

# V3_18 (2018-19)
V3_18_BrO['DateTime'] = pd.to_datetime(V3_18_BrO['DateTime'], dayfirst=True)
V3_18_Met['DateTime'] = pd.to_datetime(V3_18_Met['DateTime'], dayfirst=True)
V3_18_SI['DateTime']  = pd.to_datetime(V3_18_SI['DateTime'],  dayfirst=True)
V3_18_Hg['DateTime']  = pd.to_datetime(V3_18_Hg['DateTime'],  dayfirst=True)
V3_18_O3['DateTime']  = pd.to_datetime(V3_18_O3['DateTime'],  dayfirst=True)

# SIPEXII (2012)
SIPEXII_BrO['DateTime'] = pd.to_datetime(SIPEXII_BrO['DateTime'], dayfirst=True)
SIPEXII_Met['DateTime'] = pd.to_datetime(SIPEXII_Met['DateTime'], dayfirst=True)
SIPEXII_SI['DateTime']  = pd.to_datetime(SIPEXII_SI['DateTime'],  dayfirst=True)
SIPEXII_Hg['DateTime']  = pd.to_datetime(SIPEXII_Hg['DateTime'],  dayfirst=True)
SIPEXII_O3['DateTime']  = pd.to_datetime(SIPEXII_O3['DateTime'],  dayfirst=True)

#------------------------------------------------------------------------------
# set datetime as the index

# V1_17 (2017-18)
V1_17_BrO = V1_17_BrO.set_index('DateTime')
V1_17_Met = V1_17_Met.set_index('DateTime')
V1_17_SI  = V1_17_SI.set_index('DateTime')
V1_17_Hg  = V1_17_Hg.set_index('DateTime')
V1_17_O3  = V1_17_O3.set_index('DateTime')

# V2_17 (2017-18)
V2_17_BrO = V2_17_BrO.set_index('DateTime')
V2_17_Met = V2_17_Met.set_index('DateTime')
V2_17_SI  = V2_17_SI.set_index('DateTime')
V2_17_Hg  = V2_17_Hg.set_index('DateTime')
V2_17_O3  = V2_17_O3.set_index('DateTime')

# V3_17 (2017-18)
V3_17_BrO = V3_17_BrO.set_index('DateTime')
V3_17_Met = V3_17_Met.set_index('DateTime')
V3_17_SI  = V3_17_SI.set_index('DateTime')
V3_17_Hg  = V3_17_Hg.set_index('DateTime')
V3_17_O3  = V3_17_O3.set_index('DateTime')

# V1_18 (2018-19)
V1_18_BrO = V1_18_BrO.set_index('DateTime')
V1_18_Met = V1_18_Met.set_index('DateTime')
V1_18_SI  = V1_18_SI.set_index('DateTime')
V1_18_Hg  = V1_18_Hg.set_index('DateTime')
V1_18_O3  = V1_18_O3.set_index('DateTime')

# V2_18 (2018-19)
V2_18_BrO = V2_18_BrO.set_index('DateTime')
V2_18_Met = V2_18_Met.set_index('DateTime')
V2_18_SI  = V2_18_SI.set_index('DateTime')
V2_18_Hg  = V2_18_Hg.set_index('DateTime')
V2_18_O3  = V2_18_O3.set_index('DateTime')

# V3_18 (2018-19)
V3_18_BrO = V3_18_BrO.set_index('DateTime')
V3_18_Met = V3_18_Met.set_index('DateTime')
V3_18_SI  = V3_18_SI.set_index('DateTime')
V3_18_Hg  = V3_18_Hg.set_index('DateTime')
V3_18_O3  = V3_18_O3.set_index('DateTime')

# SIPEXII (2012)
SIPEXII_BrO = SIPEXII_BrO.set_index('DateTime')
SIPEXII_Met = SIPEXII_Met.set_index('DateTime')
SIPEXII_SI  = SIPEXII_SI.set_index('DateTime')
SIPEXII_Hg  = SIPEXII_Hg.set_index('DateTime')
SIPEXII_O3  = SIPEXII_O3.set_index('DateTime')

#------------------------------------------------------------------------------
# Resample all data to 20 min averages

# V1_17 (2017-18)
V1_17_Met = V1_17_Met.resample('20T').mean()
V1_17_SI  = V1_17_SI.resample('20T').mean()
V1_17_Hg  = V1_17_Hg.resample('20T').mean()
V1_17_O3  = V1_17_O3.resample('20T').mean()

# V2_17 (2017-18)
V2_17_Met = V2_17_Met.resample('20T').mean()
V2_17_SI  = V2_17_SI.resample('20T').mean()
V2_17_Hg  = V2_17_Hg.resample('20T').mean()
V2_17_O3  = V2_17_O3.resample('20T').mean()

# V3_17 (2017-18)
V3_17_Met = V3_17_Met.resample('20T').mean()
V3_17_SI  = V3_17_SI.resample('20T').mean()
V3_17_Hg  = V3_17_Hg.resample('20T').mean()
V3_17_O3  = V3_17_O3.resample('20T').mean()

# V1_18 (2018-19)
V1_18_Met = V1_18_Met.resample('20T').mean()
V1_18_SI  = V1_18_SI.resample('20T').mean()
V1_18_Hg  = V1_18_Hg.resample('20T').mean()
V1_18_O3  = V1_18_O3.resample('20T').mean()

# V2_18 (2018-19)
V2_18_Met = V2_18_Met.resample('20T').mean()
V2_18_SI  = V2_18_SI.resample('20T').mean()
V2_18_Hg  = V2_18_Hg.resample('20T').mean()
V2_18_O3  = V2_18_O3.resample('20T').mean()

# V3_18 (2018-19)
V3_18_Met = V3_18_Met.resample('20T').mean()
V3_18_SI  = V3_18_SI.resample('20T').mean()
V3_18_Hg  = V3_18_Hg.resample('20T').mean()
V3_18_O3  = V3_18_O3.resample('20T').mean()

# SIPEXII (2012)
SIPEXII_Met = SIPEXII_Met.resample('20T').mean()
SIPEXII_SI  = SIPEXII_SI.resample('20T').mean()
SIPEXII_Hg  = SIPEXII_Hg.resample('20T').mean()
SIPEXII_O3  = SIPEXII_O3.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

# V1_17 (2017-18)
V1_17_Met.index = V1_17_Met.index - pd.Timedelta(minutes=10)
V1_17_SI.index  = V1_17_SI.index - pd.Timedelta(minutes=10)
V1_17_Hg.index  = V1_17_Hg.index - pd.Timedelta(minutes=10)
V1_17_O3.index  = V1_17_O3.index - pd.Timedelta(minutes=10)

# V2_17 (2017-18)
V2_17_Met.index = V2_17_Met.index - pd.Timedelta(minutes=10)
V2_17_SI.index  = V2_17_SI.index - pd.Timedelta(minutes=10)
V2_17_Hg.index  = V2_17_Hg.index - pd.Timedelta(minutes=10)
V2_17_O3.index  = V2_17_O3.index - pd.Timedelta(minutes=10)

# V3_17 (2017-18)
V3_17_Met.index = V3_17_Met.index - pd.Timedelta(minutes=10)
V3_17_SI.index  = V3_17_SI.index - pd.Timedelta(minutes=10)
V3_17_Hg.index  = V3_17_Hg.index - pd.Timedelta(minutes=10)
V3_17_O3.index  = V3_17_O3.index - pd.Timedelta(minutes=10)

# V1_18 (2018-19)
V1_18_Met.index = V1_18_Met.index - pd.Timedelta(minutes=10)
V1_18_SI.index  = V1_18_SI.index - pd.Timedelta(minutes=10)
V1_18_Hg.index  = V1_18_Hg.index - pd.Timedelta(minutes=10)
V1_18_O3.index  = V1_18_O3.index - pd.Timedelta(minutes=10)

# V2_18 (2018-19)
V2_18_Met.index = V2_18_Met.index - pd.Timedelta(minutes=10)
V2_18_SI.index  = V2_18_SI.index - pd.Timedelta(minutes=10)
V2_18_Hg.index  = V2_18_Hg.index - pd.Timedelta(minutes=10)
V2_18_O3.index  = V2_18_O3.index - pd.Timedelta(minutes=10)

# V3_18 (2018-19)
V3_18_Met.index = V3_18_Met.index - pd.Timedelta(minutes=10)
V3_18_SI.index  = V3_18_SI.index - pd.Timedelta(minutes=10)
V3_18_Hg.index  = V3_18_Hg.index - pd.Timedelta(minutes=10)
V3_18_O3.index  = V3_18_O3.index - pd.Timedelta(minutes=10)

# SIPEXII (2012)
SIPEXII_Met.index = SIPEXII_Met.index - pd.Timedelta(minutes=10)
SIPEXII_SI.index  = SIPEXII_SI.index - pd.Timedelta(minutes=10)
SIPEXII_Hg.index  = SIPEXII_Hg.index - pd.Timedelta(minutes=10)
SIPEXII_O3.index  = SIPEXII_O3.index - pd.Timedelta(minutes=10)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

# V1_17 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V1_17_BrO['Time'] >= start_time) & (V1_17_BrO['Time'] < end_time)
V1_17_MM = V1_17_BrO[Midday]

# V2_17 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V2_17_BrO['Time'] >= start_time) & (V2_17_BrO['Time'] < end_time)
V2_17_MM = V2_17_BrO[Midday]

# V3_17 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V3_17_BrO['Time'] >= start_time) & (V3_17_BrO['Time'] < end_time)
V3_17_MM = V3_17_BrO[Midday]

# V1_18 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V1_18_BrO['Time'] >= start_time) & (V1_18_BrO['Time'] < end_time)
V1_18_MM = V1_18_BrO[Midday]

# V2_18 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V2_18_BrO['Time'] >= start_time) & (V2_18_BrO['Time'] < end_time)
V2_18_MM = V2_18_BrO[Midday]

# V3_18 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (V3_18_BrO['Time'] >= start_time) & (V3_18_BrO['Time'] < end_time)
V3_18_MM = V3_18_BrO[Midday]

# SIPEXII (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday = (SIPEXII_BrO['Time'] >= start_time) & (SIPEXII_BrO['Time'] < end_time)
SIPEXII_MM = SIPEXII_BrO[Midday]

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

# V1_17 (2017-18)
V1_17F = (V1_17_MM['Filter'] < 0.6)
V1_17T = V1_17_MM[V1_17F]

# V2_17 (2017-18)
V2_17F = (V2_17_MM['Filter'] < 0.6)
V2_17T = V2_17_MM[V2_17F]

# V3_17 (2017-18)
V3_17F = (V3_17_MM['Filter'] < 0.6)
V3_17T = V3_17_MM[V3_17F]

# V1_18 (2018-19)
V1_18F = (V1_18_MM['Filter'] < 0.6)
V1_18T = V1_18_MM[V1_18F]

# V2_18 (2018-19)
V2_18F = (V2_18_MM['Filter'] < 0.6)
V2_18T = V2_18_MM[V2_18F]

# V3_18 (2018-19)
V3_18F = (V3_18_MM['Filter'] < 0.6)
V3_18T = V3_18_MM[V3_18F]

# SIPEXII (2012)
SIPEXIIF = (SIPEXII_MM['Filter'] < 0.6)
SIPEXIIT = SIPEXII_MM[SIPEXIIF]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# V1_17 Davis (14-22 Nov 2017)
start_date = '2017-11-14'
end_date = '2017-11-23'
Davis = (V1_17T.index >= start_date) & (V1_17T.index < end_date)
V1_17T = V1_17T[Davis]

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

# V3_17 Mawson (1-17 Feb 2018)
start_date = '2018-02-01'
end_date = '2018-02-18'
Mawson = (V3_17T.index >= start_date) & (V3_17T.index < end_date)
V3_17T = V3_17T[Mawson]

# V1_18 Davis (7-15 Nov 2018)
start_date = '2018-11-07'
end_date = '2018-11-16'
Davis = (V1_18T.index >= start_date) & (V1_18T.index < end_date)
V1_18T = V1_18T[Davis]

# V2_18 Casey (15-30 Dec 2018)
start_date = '2018-12-15'
end_date = '2018-12-31'
Casey = (V2_18T.index >= start_date) & (V2_18T.index < end_date)
V2_18T = V2_18T[Casey]

# V3_18 Mawson (30 Jan - 9 Feb 2019)
start_date = '2019-01-30'
end_date = '2019-02-10'
Mawson = (V3_18T.index >= start_date) & (V3_18T.index < end_date)
V3_18T = V3_18T[Mawson]

# SIPEXII (23 Sep to 11 Nov 2012)
start_date = '2012-09-23'
end_date = '2012-11-11'
SIPEX = (SIPEXIIT.index >= start_date) & (SIPEXIIT.index < end_date)
SIPEXIIT = SIPEXIIT[SIPEX]

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

# V1_17 (2017-18)
D1_V1_17 = pd.merge(left=V1_17T,right=V1_17_Met, how='left', left_index=True, right_index=True)
D2_V1_17 = pd.merge(left=D1_V1_17,right=V1_17_SI, how='left', left_index=True, right_index=True)
D3_V1_17 = pd.merge(left=D2_V1_17,right=V1_17_Hg, how='left', left_index=True, right_index=True)
D4_V1_17 = pd.merge(left=D3_V1_17,right=V1_17_O3, how='left', left_index=True, right_index=True)

# V2_17 (2017-18)
D1_V2_17 = pd.merge(left=V2_17T,right=V2_17_Met, how='left', left_index=True, right_index=True)
D2_V2_17 = pd.merge(left=D1_V2_17,right=V2_17_SI, how='left', left_index=True, right_index=True)
D3_V2_17 = pd.merge(left=D2_V2_17,right=V2_17_Hg, how='left', left_index=True, right_index=True)
D4_V2_17 = pd.merge(left=D3_V2_17,right=V2_17_O3, how='left', left_index=True, right_index=True)

# V3_17 (2017-18)
D1_V3_17 = pd.merge(left=V3_17T,right=V3_17_Met, how='left', left_index=True, right_index=True)
D2_V3_17 = pd.merge(left=D1_V3_17,right=V3_17_SI, how='left', left_index=True, right_index=True)
D3_V3_17 = pd.merge(left=D2_V3_17,right=V3_17_Hg, how='left', left_index=True, right_index=True)
D4_V3_17 = pd.merge(left=D3_V3_17,right=V3_17_O3, how='left', left_index=True, right_index=True)

# V1_18 (2018-19)
D1_V1_18 = pd.merge(left=V1_18T,right=V1_18_Met, how='left', left_index=True, right_index=True)
D2_V1_18 = pd.merge(left=D1_V1_18,right=V1_18_SI, how='left', left_index=True, right_index=True)
D3_V1_18 = pd.merge(left=D2_V1_18,right=V1_18_Hg, how='left', left_index=True, right_index=True)
D4_V1_18 = pd.merge(left=D3_V1_18,right=V1_18_O3, how='left', left_index=True, right_index=True)

# V2_18 (2018-19)
D1_V2_18 = pd.merge(left=V2_18T,right=V2_18_Met, how='left', left_index=True, right_index=True)
D2_V2_18 = pd.merge(left=D1_V2_18,right=V2_18_SI, how='left', left_index=True, right_index=True)
D3_V2_18 = pd.merge(left=D2_V2_18,right=V2_18_Hg, how='left', left_index=True, right_index=True)
D4_V2_18 = pd.merge(left=D3_V2_18,right=V2_18_O3, how='left', left_index=True, right_index=True)

# V3_18 (2018-19)
D1_V3_18 = pd.merge(left=V3_18T,right=V3_18_Met, how='left', left_index=True, right_index=True)
D2_V3_18 = pd.merge(left=D1_V3_18,right=V3_18_SI, how='left', left_index=True, right_index=True)
D3_V3_18 = pd.merge(left=D2_V3_18,right=V3_18_Hg, how='left', left_index=True, right_index=True)
D4_V3_18 = pd.merge(left=D3_V3_18,right=V3_18_O3, how='left', left_index=True, right_index=True)

# SIPEXII (2012)
D1_SIPEXII = pd.merge(left=SIPEXIIT,right=SIPEXII_Met, how='left', left_index=True, right_index=True)
D2_SIPEXII = pd.merge(left=D1_SIPEXII,right=SIPEXII_SI, how='left', left_index=True, right_index=True)
D3_SIPEXII = pd.merge(left=D2_SIPEXII,right=SIPEXII_Hg, how='left', left_index=True, right_index=True)
D4_SIPEXII = pd.merge(left=D3_SIPEXII,right=SIPEXII_O3, how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Define the variables

#--------------------------------
# BrO surface volume mixing ratio (VMR)
BrO_V1_17   = np.array(D4_V1_17['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V2_17   = np.array(D4_V2_17['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V3_17   = np.array(D4_V3_17['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V1_18   = np.array(D4_V1_18['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V2_18   = np.array(D4_V2_18['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_V3_18   = np.array(D4_V3_18['surf_vmr(ppmv)'])   * 1e6 # convert from ppmv to ppbv
BrO_SIPEXII = np.array(D4_SIPEXII['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to ppbv

#--------------------------------
# O3 (ppb)
O3_V1_17   = np.array(D4_V1_17['O3_(ppb)_y']) # O3 (ppb)
O3_V2_17   = np.array(D4_V2_17['O3_(ppb)_y']) # O3 (ppb)
O3_V3_17   = np.array(D4_V3_17['O3_(ppb)_y']) # O3 (ppb)
O3_V1_18   = np.array(D4_V1_18['O3']) # O3 (ppb)
O3_V2_18   = np.array(D4_V2_18['O3']) # O3 (ppb)
O3_V3_18   = np.array(D4_V3_18['O3']) # O3 (ppb)
O3_SIPEXII = np.array(D4_SIPEXII['O3_(ppb)_y']) # O3 (ppb)

#--------------------------------
# Solar Radiation (W/m2)
Sol_s_V1_17 = np.array(D4_V1_17['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V1_17 = np.array(D4_V1_17['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V1_17['MeanSol'] = D4_V1_17[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_17 = np.array(D4_V1_17['MeanSol'])

Sol_s_V2_17 = np.array(D4_V2_17['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V2_17 = np.array(D4_V2_17['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V2_17['MeanSol'] = D4_V2_17[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_17 = np.array(D4_V2_17['MeanSol'])

Sol_s_V3_17 = np.array(D4_V3_17['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V3_17 = np.array(D4_V3_17['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V3_17['MeanSol'] = D4_V3_17[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_17 = np.array(D4_V3_17['MeanSol'])

Sol_s_V1_18 = np.array(D4_V1_18['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V1_18 = np.array(D4_V1_18['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V1_18['MeanSol'] = D4_V1_18[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V1_18 = np.array(D4_V1_18['MeanSol'])

Sol_s_V2_18 = np.array(D4_V2_18['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V2_18 = np.array(D4_V2_18['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V2_18['MeanSol'] = D4_V2_18[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V2_18 = np.array(D4_V2_18['MeanSol'])

Sol_s_V3_18 = np.array(D4_V3_18['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_V3_18 = np.array(D4_V3_18['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_V3_18['MeanSol'] = D4_V3_18[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_V3_18 = np.array(D4_V3_18['MeanSol'])

Sol_s_SIPEXII = np.array(D4_SIPEXII['RAD_SLR_STRBRD_WPERM2_y']) # starboard side solar radiation
Sol_p_SIPEXII = np.array(D4_SIPEXII['RAD_SLR_PORT_WPERM2_y']) # port side solar radiation
D4_SIPEXII['MeanSol'] = D4_SIPEXII[['RAD_SLR_STRBRD_WPERM2_y','RAD_SLR_PORT_WPERM2_y']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_SIPEXII = np.array(D4_SIPEXII['MeanSol'])

#--------------------------------
# Temperature (C)

Temp_s_V1_17 = np.array(D4_V1_17['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V1_17 = np.array(D4_V1_17['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V1_17['MeanTemp'] = D4_V1_17[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_17 = np.array(D4_V1_17['MeanTemp'])

Temp_s_V2_17 = np.array(D4_V2_17['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V2_17 = np.array(D4_V2_17['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V2_17['MeanTemp'] = D4_V2_17[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_17 = np.array(D4_V2_17['MeanTemp'])

Temp_s_V3_17 = np.array(D4_V3_17['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V3_17 = np.array(D4_V3_17['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V3_17['MeanTemp'] = D4_V3_17[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_17 = np.array(D4_V3_17['MeanTemp'])

Temp_s_V1_18 = np.array(D4_V1_18['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V1_18 = np.array(D4_V1_18['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V1_18['MeanTemp'] = D4_V1_18[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V1_18 = np.array(D4_V1_18['MeanTemp'])

Temp_s_V2_18 = np.array(D4_V2_18['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V2_18 = np.array(D4_V2_18['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V2_18['MeanTemp'] = D4_V2_18[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V2_18 = np.array(D4_V2_18['MeanTemp'])

Temp_s_V3_18 = np.array(D4_V3_18['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_V3_18 = np.array(D4_V3_18['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_V3_18['MeanTemp'] = D4_V3_18[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_V3_18 = np.array(D4_V3_18['MeanTemp'])

Temp_s_SIPEXII = np.array(D4_SIPEXII['TEMP_AIR_STRBRD_DEGC_y']) # starboard side temperature
Temp_p_SIPEXII = np.array(D4_SIPEXII['TEMP_AIR_PORT_DEGC_y']) # port side temperature
D4_SIPEXII['MeanTemp'] = D4_SIPEXII[['TEMP_AIR_STRBRD_DEGC_y','TEMP_AIR_PORT_DEGC_y']].mean(axis=1) # Average the temperature for port and starboard
Temp_SIPEXII = np.array(D4_SIPEXII['MeanTemp'])

#--------------------------------
# Wind Direction

WD_s_V1_17 = np.array(D4_V1_17['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V1_17 = np.array(D4_V1_17['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V2_17 = np.array(D4_V2_17['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V2_17 = np.array(D4_V2_17['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V3_17 = np.array(D4_V3_17['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V3_17 = np.array(D4_V3_17['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V1_18 = np.array(D4_V1_18['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V1_18 = np.array(D4_V1_18['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V2_18 = np.array(D4_V2_18['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V2_18 = np.array(D4_V2_18['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_V3_18 = np.array(D4_V3_18['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_V3_18 = np.array(D4_V3_18['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

WD_s_SIPEXII = np.array(D4_SIPEXII['WND_DIR_STRBD_CORR_DEG_y']) # starboard side wind direction (correlated)
WD_p_SIPEXII = np.array(D4_SIPEXII['WND_DIR_PORT_CORR_DEG_y']) # port side wind direction (correlated)

#--------------------------------
# Wind Speed

WS_s_V1_17 = np.array(D4_V1_17['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_17 = np.array(D4_V1_17['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V1_17 = (WS_s_V1_17 + WS_p_V1_17)/2 # Average the wind speed for port and starboard

WS_s_V2_17 = np.array(D4_V2_17['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_17 = np.array(D4_V2_17['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V2_17 = (WS_s_V2_17 + WS_p_V2_17)/2 # Average the wind speed for port and starboard

WS_s_V3_17 = np.array(D4_V3_17['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_17 = np.array(D4_V3_17['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V3_17 = (WS_s_V3_17 + WS_p_V3_17)/2 # Average the wind speed for port and starboard

WS_s_V1_18 = np.array(D4_V1_18['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V1_18 = np.array(D4_V1_18['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V1_18 = (WS_s_V1_18 + WS_p_V1_18)/2 # Average the wind speed for port and starboard

WS_s_V2_18 = np.array(D4_V2_18['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V2_18 = np.array(D4_V2_18['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V2_18 = (WS_s_V2_18 + WS_p_V2_18)/2 # Average the wind speed for port and starboard

WS_s_V3_18 = np.array(D4_V3_18['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_V3_18 = np.array(D4_V3_18['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_V3_18 = (WS_s_V3_18 + WS_p_V3_18)/2 # Average the wind speed for port and starboard

WS_s_SIPEXII = np.array(D4_SIPEXII['WND_SPD_STRBD_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXII = np.array(D4_SIPEXII['WND_SPD_PORT_CORR_KNOT_y']) * 0.514444444 # Convert from knots to m/s
WS_SIPEXII = (WS_s_SIPEXII + WS_p_SIPEXII)/2 # Average the wind speed for port and starboard

#--------------------------------
# Vector Mean Wind Direction

WD_vect_V1_17 = ((WD_s_V1_17 * WS_s_V1_17) / (WS_s_V1_17 + WS_p_V1_17)) + ((WD_p_V1_17 * WS_p_V1_17) / (WS_s_V1_17 + WS_p_V1_17)) # Calculate the vector mean wind direction
WD_vect_V2_17 = ((WD_s_V2_17 * WS_s_V2_17) / (WS_s_V2_17 + WS_p_V2_17)) + ((WD_p_V2_17 * WS_p_V2_17) / (WS_s_V2_17 + WS_p_V2_17)) # Calculate the vector mean wind direction
WD_vect_V3_17 = ((WD_s_V3_17 * WS_s_V3_17) / (WS_s_V3_17 + WS_p_V3_17)) + ((WD_p_V3_17 * WS_p_V3_17) / (WS_s_V3_17 + WS_p_V3_17)) # Calculate the vector mean wind direction
WD_vect_V1_18 = ((WD_s_V1_18 * WS_s_V1_18) / (WS_s_V1_18 + WS_p_V1_18)) + ((WD_p_V1_18 * WS_p_V1_18) / (WS_s_V1_18 + WS_p_V1_18)) # Calculate the vector mean wind direction
WD_vect_V2_18 = ((WD_s_V2_18 * WS_s_V2_18) / (WS_s_V2_18 + WS_p_V2_18)) + ((WD_p_V2_18 * WS_p_V2_18) / (WS_s_V2_18 + WS_p_V2_18)) # Calculate the vector mean wind direction
WD_vect_V3_18 = ((WD_s_V3_18 * WS_s_V3_18) / (WS_s_V3_18 + WS_p_V3_18)) + ((WD_p_V3_18 * WS_p_V3_18) / (WS_s_V3_18 + WS_p_V3_18)) # Calculate the vector mean wind direction
WD_vect_SIPEXII = ((WD_s_SIPEXII * WS_s_SIPEXII) / (WS_s_SIPEXII + WS_p_SIPEXII)) + ((WD_p_SIPEXII * WS_p_SIPEXII) / (WS_s_SIPEXII + WS_p_SIPEXII)) # Calculate the vector mean wind direction

#--------------------------------
# Hg0

Hg0_V1_17 = np.array(D4_V1_17['ng/m3_y']) # Hg0
Hg0_V2_17 = np.array(D4_V2_17['ng/m3_y']) # Hg0
Hg0_V3_17 = np.array(D4_V3_17['ng/m3_y']) # Hg0
Hg0_V1_18 = np.array(D4_V1_18['ng/m3_y']) # Hg0
Hg0_V2_18 = np.array(D4_V2_18['ng/m3_y']) # Hg0
Hg0_V3_18 = np.array(D4_V3_18['ng/m3_y']) # Hg0
Hg0_SIPEXII = np.array(D4_SIPEXII['ng/m3_y']) # Hg0

#--------------------------------
# Sea Ice Concentration

SI_V1_17 = np.array(D4_V1_17['Sea_Ice_Conc'])*100
SI_V2_17 = np.array(D4_V2_17['Sea_Ice_Conc'])*100
SI_V3_17 = np.array(D4_V3_17['Sea_Ice_Conc'])*100
SI_V1_18 = np.array(D4_V1_18['Sea_Ice_Conc'])*100
SI_V2_18 = np.array(D4_V2_18['Sea_Ice_Conc'])*100
SI_V3_18 = np.array(D4_V3_18['Sea_Ice_Conc'])*100
SI_SIPEXII = np.array(D4_SIPEXII['Sea_Ice_Conc'])*100

#--------------------------------
# Relative Humidity

RH_s_V1_17 = np.array(D4_V1_17['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V1_17 = np.array(D4_V1_17['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V1_17 = (RH_s_V1_17 + RH_p_V1_17)/2

RH_s_V2_17 = np.array(D4_V2_17['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V2_17 = np.array(D4_V2_17['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V2_17 = (RH_s_V2_17 + RH_p_V2_17)/2

RH_s_V3_17 = np.array(D4_V3_17['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V3_17 = np.array(D4_V3_17['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V3_17 = (RH_s_V3_17 + RH_p_V3_17)/2

RH_s_V1_18 = np.array(D4_V1_18['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V1_18 = np.array(D4_V1_18['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V1_18 = (RH_s_V1_18 + RH_p_V1_18)/2

RH_s_V2_18 = np.array(D4_V2_18['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V2_18 = np.array(D4_V2_18['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V2_18 = (RH_s_V2_18 + RH_p_V2_18)/2

RH_s_V3_18 = np.array(D4_V3_18['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_V3_18 = np.array(D4_V3_18['REL_HUMIDITY_PORT_PERCENT_y'])
RH_V3_18 = (RH_s_V3_18 + RH_p_V3_18)/2

RH_s_SIPEXII = np.array(D4_SIPEXII['REL_HUMIDITY_STRBRD_PERCENT_y'])
RH_p_SIPEXII = np.array(D4_SIPEXII['REL_HUMIDITY_PORT_PERCENT_y'])
RH_SIPEXII = (RH_s_SIPEXII + RH_p_SIPEXII)/2

#------------------------------------------------------------------------------
# Scan for NaN values

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V1_17_Y1mask  = np.isfinite(Sol_V1_17) # Scan for NaN values
BrO_V1_17     = BrO_V1_17[V1_17_Y1mask] # Remove NaN values from BrO
O3_V1_17      = O3_V1_17[V1_17_Y1mask] # Remove NaN values from Sol
Sol_V1_17     = Sol_V1_17[V1_17_Y1mask] # Remove NaN values from Sol
Temp_V1_17    = Temp_V1_17[V1_17_Y1mask] # Remove NaN values from Sol
WD_vect_V1_17 = WD_vect_V1_17[V1_17_Y1mask] # Remove NaN values from Sol
WS_V1_17      = WS_V1_17[V1_17_Y1mask] # Remove NaN values from Sol
Hg0_V1_17     = Hg0_V1_17[V1_17_Y1mask] # Remove NaN values from Sol
SI_V1_17      = SI_V1_17[V1_17_Y1mask] # Remove NaN values from Sol

# Pass 2 (O3) 
V1_17_Y2mask = np.isfinite(O3_V1_17) # Scan for NaN values
BrO_O3_V1_17 = BrO_V1_17[V1_17_Y2mask] # Remove NaN values from BrO
O3_V1_17     = O3_V1_17[V1_17_Y2mask] # Remove NaN values from Temp
Sol_O3_V1_17 = Sol_V1_17[V1_17_Y2mask] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_17_Y3mask   = np.isfinite(Temp_V1_17) # Scan for NaN values
BrO_Temp_V1_17 = BrO_V1_17[V1_17_Y3mask] # Remove NaN values from BrO
Temp_V1_17     = Temp_V1_17[V1_17_Y3mask] # Remove NaN values from Temp
Sol_Temp_V1_17 = Sol_V1_17[V1_17_Y3mask] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_17_Y4mask  = np.isfinite(WD_vect_V1_17) # Scan for NaN values
BrO_WD_V1_17  = BrO_V1_17[V1_17_Y4mask] # Remove NaN values from BrO
WD_vect_V1_17 = WD_vect_V1_17[V1_17_Y4mask] # Remove NaN values from WD_vect
Sol_WD_V1_17  = Sol_V1_17[V1_17_Y4mask] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_17_Y5mask = np.isfinite(WS_V1_17) # Scan for NaN values
BrO_WS_V1_17 = BrO_V1_17[V1_17_Y5mask] # Remove NaN values from BrO
WS_V1_17     = WS_V1_17[V1_17_Y5mask] # Remove NaN values from WS
Sol_WS_V1_17 = Sol_V1_17[V1_17_Y5mask] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_17_Y6mask  = np.isfinite(Hg0_V1_17) # Scan for NaN values
BrO_Hg0_V1_17 = BrO_V1_17[V1_17_Y6mask] # Remove NaN values from BrO
Hg0_V1_17     = Hg0_V1_17[V1_17_Y6mask] # Remove NaN values from SI
Sol_Hg0_V1_17 = Sol_V1_17[V1_17_Y6mask] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_17_Y7mask = np.isfinite(SI_V1_17) # Scan for NaN values
BrO_SI_V1_17 = BrO_V1_17[V1_17_Y7mask] # Remove NaN values from BrO
SI_SI_V1_17  = SI_V1_17[V1_17_Y7mask] # Remove NaN values from SI
Sol_SI_V1_17 = Sol_V1_17[V1_17_Y7mask] # Remove NaN values from Sol

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V2_17_Y1mask  = np.isfinite(Sol_V2_17) # Scan for NaN values
BrO_V2_17     = BrO_V2_17[V2_17_Y1mask] # Remove NaN values from BrO
O3_V2_17      = O3_V2_17[V2_17_Y1mask] # Remove NaN values from Sol
Sol_V2_17     = Sol_V2_17[V2_17_Y1mask] # Remove NaN values from Sol
Temp_V2_17    = Temp_V2_17[V2_17_Y1mask] # Remove NaN values from Sol
WD_vect_V2_17 = WD_vect_V2_17[V2_17_Y1mask] # Remove NaN values from Sol
WS_V2_17      = WS_V2_17[V2_17_Y1mask] # Remove NaN values from Sol
Hg0_V2_17     = Hg0_V2_17[V2_17_Y1mask] # Remove NaN values from Sol
SI_V2_17      = SI_V2_17[V2_17_Y1mask] # Remove NaN values from Sol

# Pass 2 (O3) 
V2_17_Y2mask = np.isfinite(O3_V2_17) # Scan for NaN values
BrO_O3_V2_17 = BrO_V2_17[V2_17_Y2mask] # Remove NaN values from BrO
O3_V2_17     = O3_V2_17[V2_17_Y2mask] # Remove NaN values from Temp
Sol_O3_V2_17 = Sol_V2_17[V2_17_Y2mask] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_17_Y3mask   = np.isfinite(Temp_V2_17) # Scan for NaN values
BrO_Temp_V2_17 = BrO_V2_17[V2_17_Y3mask] # Remove NaN values from BrO
Temp_V2_17     = Temp_V2_17[V2_17_Y3mask] # Remove NaN values from Temp
Sol_Temp_V2_17 = Sol_V2_17[V2_17_Y3mask] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_17_Y4mask  = np.isfinite(WD_vect_V2_17) # Scan for NaN values
BrO_WD_V2_17  = BrO_V2_17[V2_17_Y4mask] # Remove NaN values from BrO
WD_vect_V2_17 = WD_vect_V2_17[V2_17_Y4mask] # Remove NaN values from WD_vect
Sol_WD_V2_17  = Sol_V2_17[V2_17_Y4mask] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_17_Y5mask = np.isfinite(WS_V2_17) # Scan for NaN values
BrO_WS_V2_17 = BrO_V2_17[V2_17_Y5mask] # Remove NaN values from BrO
WS_V2_17     = WS_V2_17[V2_17_Y5mask] # Remove NaN values from WS
Sol_WS_V2_17 = Sol_V2_17[V2_17_Y5mask] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_17_Y6mask  = np.isfinite(Hg0_V2_17) # Scan for NaN values
BrO_Hg0_V2_17 = BrO_V2_17[V2_17_Y6mask] # Remove NaN values from BrO
Hg0_V2_17     = Hg0_V2_17[V2_17_Y6mask] # Remove NaN values from SI
Sol_Hg0_V2_17 = Sol_V2_17[V2_17_Y6mask] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_17_Y7mask = np.isfinite(SI_V2_17) # Scan for NaN values
BrO_SI_V2_17 = BrO_V2_17[V2_17_Y7mask] # Remove NaN values from BrO
SI_SI_V2_17  = SI_V2_17[V2_17_Y7mask] # Remove NaN values from SI
Sol_SI_V2_17 = Sol_V2_17[V2_17_Y7mask] # Remove NaN values from Sol

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# Pass 1 (Sol) 
V3_17_Y1mask  = np.isfinite(Sol_V3_17) # Scan for NaN values
BrO_V3_17     = BrO_V3_17[V3_17_Y1mask] # Remove NaN values from BrO
O3_V3_17      = O3_V3_17[V3_17_Y1mask] # Remove NaN values from Sol
Sol_V3_17     = Sol_V3_17[V3_17_Y1mask] # Remove NaN values from Sol
Temp_V3_17    = Temp_V3_17[V3_17_Y1mask] # Remove NaN values from Sol
WD_vect_V3_17 = WD_vect_V3_17[V3_17_Y1mask] # Remove NaN values from Sol
WS_V3_17      = WS_V3_17[V3_17_Y1mask] # Remove NaN values from Sol
Hg0_V3_17     = Hg0_V3_17[V3_17_Y1mask] # Remove NaN values from Sol
SI_V3_17      = SI_V3_17[V3_17_Y1mask] # Remove NaN values from Sol

# Pass 2 (O3) 
V3_17_Y2mask = np.isfinite(O3_V3_17) # Scan for NaN values
BrO_O3_V3_17 = BrO_V3_17[V3_17_Y2mask] # Remove NaN values from BrO
O3_V3_17     = O3_V3_17[V3_17_Y2mask] # Remove NaN values from Temp
Sol_O3_V3_17 = Sol_V3_17[V3_17_Y2mask] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_17_Y3mask   = np.isfinite(Temp_V3_17) # Scan for NaN values
BrO_Temp_V3_17 = BrO_V3_17[V3_17_Y3mask] # Remove NaN values from BrO
Temp_V3_17     = Temp_V3_17[V3_17_Y3mask] # Remove NaN values from Temp
Sol_Temp_V3_17 = Sol_V3_17[V3_17_Y3mask] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_17_Y4mask  = np.isfinite(WD_vect_V3_17) # Scan for NaN values
BrO_WD_V3_17  = BrO_V3_17[V3_17_Y4mask] # Remove NaN values from BrO
WD_vect_V3_17 = WD_vect_V3_17[V3_17_Y4mask] # Remove NaN values from WD_vect
Sol_WD_V3_17  = Sol_V3_17[V3_17_Y4mask] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_17_Y5mask = np.isfinite(WS_V3_17) # Scan for NaN values
BrO_WS_V3_17 = BrO_V3_17[V3_17_Y5mask] # Remove NaN values from BrO
WS_V3_17     = WS_V3_17[V3_17_Y5mask] # Remove NaN values from WS
Sol_WS_V3_17 = Sol_V3_17[V3_17_Y5mask] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_17_Y6mask  = np.isfinite(Hg0_V3_17) # Scan for NaN values
BrO_Hg0_V3_17 = BrO_V3_17[V3_17_Y6mask] # Remove NaN values from BrO
Hg0_V3_17     = Hg0_V3_17[V3_17_Y6mask] # Remove NaN values from SI
Sol_Hg0_V3_17 = Sol_V3_17[V3_17_Y6mask] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_17_Y7mask = np.isfinite(SI_V3_17) # Scan for NaN values
BrO_SI_V3_17 = BrO_V3_17[V3_17_Y7mask] # Remove NaN values from BrO
SI_SI_V3_17  = SI_V3_17[V3_17_Y7mask] # Remove NaN values from SI
Sol_SI_V3_17 = Sol_V3_17[V3_17_Y7mask] # Remove NaN values from Sol

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V1_18_Y1mask  = np.isfinite(Sol_V1_18) # Scan for NaN values
BrO_V1_18     = BrO_V1_18[V1_18_Y1mask] # Remove NaN values from BrO
O3_V1_18      = O3_V1_18[V1_18_Y1mask] # Remove NaN values from Sol
Sol_V1_18     = Sol_V1_18[V1_18_Y1mask] # Remove NaN values from Sol
Temp_V1_18    = Temp_V1_18[V1_18_Y1mask] # Remove NaN values from Sol
WD_vect_V1_18 = WD_vect_V1_18[V1_18_Y1mask] # Remove NaN values from Sol
WS_V1_18      = WS_V1_18[V1_18_Y1mask] # Remove NaN values from Sol
Hg0_V1_18     = Hg0_V1_18[V1_18_Y1mask] # Remove NaN values from Sol
SI_V1_18      = SI_V1_18[V1_18_Y1mask] # Remove NaN values from Sol

# Pass 2 (O3) 
V1_18_Y2mask = np.isfinite(O3_V1_18) # Scan for NaN values
BrO_O3_V1_18 = BrO_V1_18[V1_18_Y2mask] # Remove NaN values from BrO
O3_V1_18     = O3_V1_18[V1_18_Y2mask] # Remove NaN values from Temp
Sol_O3_V1_18 = Sol_V1_18[V1_18_Y2mask] # Remove NaN values from Sol

# Pass 3 (Temp) 
V1_18_Y3mask   = np.isfinite(Temp_V1_18) # Scan for NaN values
BrO_Temp_V1_18 = BrO_V1_18[V1_18_Y3mask] # Remove NaN values from BrO
Temp_V1_18     = Temp_V1_18[V1_18_Y3mask] # Remove NaN values from Temp
Sol_Temp_V1_18 = Sol_V1_18[V1_18_Y3mask] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V1_18_Y4mask  = np.isfinite(WD_vect_V1_18) # Scan for NaN values
BrO_WD_V1_18  = BrO_V1_18[V1_18_Y4mask] # Remove NaN values from BrO
WD_vect_V1_18 = WD_vect_V1_18[V1_18_Y4mask] # Remove NaN values from WD_vect
Sol_WD_V1_18  = Sol_V1_18[V1_18_Y4mask] # Remove NaN values from Sol

# Pass 5 (WS) 
V1_18_Y5mask = np.isfinite(WS_V1_18) # Scan for NaN values
BrO_WS_V1_18 = BrO_V1_18[V1_18_Y5mask] # Remove NaN values from BrO
WS_V1_18     = WS_V1_18[V1_18_Y5mask] # Remove NaN values from WS
Sol_WS_V1_18 = Sol_V1_18[V1_18_Y5mask] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V1_18_Y6mask  = np.isfinite(Hg0_V1_18) # Scan for NaN values
BrO_Hg0_V1_18 = BrO_V1_18[V1_18_Y6mask] # Remove NaN values from BrO
Hg0_V1_18     = Hg0_V1_18[V1_18_Y6mask] # Remove NaN values from SI
Sol_Hg0_V1_18 = Sol_V1_18[V1_18_Y6mask] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V1_18_Y7mask = np.isfinite(SI_V1_18) # Scan for NaN values
BrO_SI_V1_18 = BrO_V1_18[V1_18_Y7mask] # Remove NaN values from BrO
SI_SI_V1_18  = SI_V1_18[V1_18_Y7mask] # Remove NaN values from SI
Sol_SI_V1_18 = Sol_V1_18[V1_18_Y7mask] # Remove NaN values from Sol

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V2_18_Y1mask  = np.isfinite(Sol_V2_18) # Scan for NaN values
BrO_V2_18     = BrO_V2_18[V2_18_Y1mask] # Remove NaN values from BrO
O3_V2_18      = O3_V2_18[V2_18_Y1mask] # Remove NaN values from Sol
Sol_V2_18     = Sol_V2_18[V2_18_Y1mask] # Remove NaN values from Sol
Temp_V2_18    = Temp_V2_18[V2_18_Y1mask] # Remove NaN values from Sol
WD_vect_V2_18 = WD_vect_V2_18[V2_18_Y1mask] # Remove NaN values from Sol
WS_V2_18      = WS_V2_18[V2_18_Y1mask] # Remove NaN values from Sol
Hg0_V2_18     = Hg0_V2_18[V2_18_Y1mask] # Remove NaN values from Sol
SI_V2_18      = SI_V2_18[V2_18_Y1mask] # Remove NaN values from Sol

# Pass 2 (O3) 
V2_18_Y2mask = np.isfinite(O3_V2_18) # Scan for NaN values
BrO_O3_V2_18 = BrO_V2_18[V2_18_Y2mask] # Remove NaN values from BrO
O3_V2_18     = O3_V2_18[V2_18_Y2mask] # Remove NaN values from Temp
Sol_O3_V2_18 = Sol_V2_18[V2_18_Y2mask] # Remove NaN values from Sol

# Pass 3 (Temp) 
V2_18_Y3mask   = np.isfinite(Temp_V2_18) # Scan for NaN values
BrO_Temp_V2_18 = BrO_V2_18[V2_18_Y3mask] # Remove NaN values from BrO
Temp_V2_18     = Temp_V2_18[V2_18_Y3mask] # Remove NaN values from Temp
Sol_Temp_V2_18 = Sol_V2_18[V2_18_Y3mask] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V2_18_Y4mask  = np.isfinite(WD_vect_V2_18) # Scan for NaN values
BrO_WD_V2_18  = BrO_V2_18[V2_18_Y4mask] # Remove NaN values from BrO
WD_vect_V2_18 = WD_vect_V2_18[V2_18_Y4mask] # Remove NaN values from WD_vect
Sol_WD_V2_18  = Sol_V2_18[V2_18_Y4mask] # Remove NaN values from Sol

# Pass 5 (WS) 
V2_18_Y5mask = np.isfinite(WS_V2_18) # Scan for NaN values
BrO_WS_V2_18 = BrO_V2_18[V2_18_Y5mask] # Remove NaN values from BrO
WS_V2_18     = WS_V2_18[V2_18_Y5mask] # Remove NaN values from WS
Sol_WS_V2_18 = Sol_V2_18[V2_18_Y5mask] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V2_18_Y6mask  = np.isfinite(Hg0_V2_18) # Scan for NaN values
BrO_Hg0_V2_18 = BrO_V2_18[V2_18_Y6mask] # Remove NaN values from BrO
Hg0_V2_18     = Hg0_V2_18[V2_18_Y6mask] # Remove NaN values from SI
Sol_Hg0_V2_18 = Sol_V2_18[V2_18_Y6mask] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V2_18_Y7mask = np.isfinite(SI_V2_18) # Scan for NaN values
BrO_SI_V2_18 = BrO_V2_18[V2_18_Y7mask] # Remove NaN values from BrO
SI_SI_V2_18  = SI_V2_18[V2_18_Y7mask] # Remove NaN values from SI
Sol_SI_V2_18 = Sol_V2_18[V2_18_Y7mask] # Remove NaN values from Sol

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# Pass 1 (Sol) 
V3_18_Y1mask  = np.isfinite(Sol_V3_18) # Scan for NaN values
BrO_V3_18     = BrO_V3_18[V3_18_Y1mask] # Remove NaN values from BrO
O3_V3_18      = O3_V3_18[V3_18_Y1mask] # Remove NaN values from Sol
Sol_V3_18     = Sol_V3_18[V3_18_Y1mask] # Remove NaN values from Sol
Temp_V3_18    = Temp_V3_18[V3_18_Y1mask] # Remove NaN values from Sol
WD_vect_V3_18 = WD_vect_V3_18[V3_18_Y1mask] # Remove NaN values from Sol
WS_V3_18      = WS_V3_18[V3_18_Y1mask] # Remove NaN values from Sol
Hg0_V3_18     = Hg0_V3_18[V3_18_Y1mask] # Remove NaN values from Sol
SI_V3_18      = SI_V3_18[V3_18_Y1mask] # Remove NaN values from Sol

# Pass 2 (O3) 
V3_18_Y2mask = np.isfinite(O3_V3_18) # Scan for NaN values
BrO_O3_V3_18 = BrO_V3_18[V3_18_Y2mask] # Remove NaN values from BrO
O3_V3_18     = O3_V3_18[V3_18_Y2mask] # Remove NaN values from Temp
Sol_O3_V3_18 = Sol_V3_18[V3_18_Y2mask] # Remove NaN values from Sol

# Pass 3 (Temp) 
V3_18_Y3mask   = np.isfinite(Temp_V3_18) # Scan for NaN values
BrO_Temp_V3_18 = BrO_V3_18[V3_18_Y3mask] # Remove NaN values from BrO
Temp_V3_18     = Temp_V3_18[V3_18_Y3mask] # Remove NaN values from Temp
Sol_Temp_V3_18 = Sol_V3_18[V3_18_Y3mask] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
V3_18_Y4mask  = np.isfinite(WD_vect_V3_18) # Scan for NaN values
BrO_WD_V3_18  = BrO_V3_18[V3_18_Y4mask] # Remove NaN values from BrO
WD_vect_V3_18 = WD_vect_V3_18[V3_18_Y4mask] # Remove NaN values from WD_vect
Sol_WD_V3_18  = Sol_V3_18[V3_18_Y4mask] # Remove NaN values from Sol

# Pass 5 (WS) 
V3_18_Y5mask = np.isfinite(WS_V3_18) # Scan for NaN values
BrO_WS_V3_18 = BrO_V3_18[V3_18_Y5mask] # Remove NaN values from BrO
WS_V3_18     = WS_V3_18[V3_18_Y5mask] # Remove NaN values from WS
Sol_WS_V3_18 = Sol_V3_18[V3_18_Y5mask] # Remove NaN values from Sol

# Pass 6 (Hg0) 
V3_18_Y6mask  = np.isfinite(Hg0_V3_18) # Scan for NaN values
BrO_Hg0_V3_18 = BrO_V3_18[V3_18_Y6mask] # Remove NaN values from BrO
Hg0_V3_18     = Hg0_V3_18[V3_18_Y6mask] # Remove NaN values from SI
Sol_Hg0_V3_18 = Sol_V3_18[V3_18_Y6mask] # Remove NaN values from Sol

# Pass 7 (SI Field) 
V3_18_Y7mask = np.isfinite(SI_V3_18) # Scan for NaN values
BrO_SI_V3_18 = BrO_V3_18[V3_18_Y7mask] # Remove NaN values from BrO
SI_SI_V3_18  = SI_V3_18[V3_18_Y7mask] # Remove NaN values from SI
Sol_SI_V3_18 = Sol_V3_18[V3_18_Y7mask] # Remove NaN values from Sol

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (Sol) 
SIPEXII_Y1mask  = np.isfinite(Sol_SIPEXII) # Scan for NaN values
BrO_SIPEXII     = BrO_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from BrO
O3_SIPEXII      = O3_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from Sol
Sol_SIPEXII     = Sol_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from Sol
Temp_SIPEXII    = Temp_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from Sol
WD_vect_SIPEXII = WD_vect_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from Sol
WS_SIPEXII      = WS_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from Sol
Hg0_SIPEXII     = Hg0_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from Sol
SI_SIPEXII      = SI_SIPEXII[SIPEXII_Y1mask] # Remove NaN values from Sol

# Pass 2 (Temp) 
SIPEXII_Y2mask   = np.isfinite(Temp_SIPEXII) # Scan for NaN values
BrO_Temp_SIPEXII = BrO_SIPEXII[SIPEXII_Y2mask] # Remove NaN values from BrO
Temp_SIPEXII     = Temp_SIPEXII[SIPEXII_Y2mask] # Remove NaN values from Temp
Sol_Temp_SIPEXII = Sol_SIPEXII[SIPEXII_Y2mask] # Remove NaN values from Sol

# Pass 3 (WD_vect) 
SIPEXII_Y3mask  = np.isfinite(WD_vect_SIPEXII) # Scan for NaN values
BrO_WD_SIPEXII  = BrO_SIPEXII[SIPEXII_Y3mask] # Remove NaN values from BrO
WD_vect_SIPEXII = WD_vect_SIPEXII[SIPEXII_Y3mask] # Remove NaN values from WD_vect
Sol_WD_SIPEXII  = Sol_SIPEXII[SIPEXII_Y3mask] # Remove NaN values from Sol

# Pass 4 (WS) 
SIPEXII_Y4mask = np.isfinite(WS_SIPEXII) # Scan for NaN values
BrO_WS_SIPEXII = BrO_SIPEXII[SIPEXII_Y4mask] # Remove NaN values from BrO
WS_SIPEXII     = WS_SIPEXII[SIPEXII_Y4mask] # Remove NaN values from WS
Sol_WS_SIPEXII = Sol_SIPEXII[SIPEXII_Y4mask] # Remove NaN values from Sol

# Pass 5 (Hg0) 
SIPEXII_Y5mask  = np.isfinite(Hg0_SIPEXII) # Scan for NaN values
BrO_Hg0_SIPEXII = BrO_SIPEXII[SIPEXII_Y5mask] # Remove NaN values from BrO
Hg0_SIPEXII     = Hg0_SIPEXII[SIPEXII_Y5mask] # Remove NaN values from SI
Sol_Hg0_SIPEXII = Sol_SIPEXII[SIPEXII_Y5mask] # Remove NaN values from Sol

# Pass 6 (SI Field) 
SIPEXII_Y6mask = np.isfinite(SI_SIPEXII) # Scan for NaN values
BrO_SI_SIPEXII = BrO_SIPEXII[SIPEXII_Y6mask] # Remove NaN values from BrO
SI_SI_SIPEXII  = SI_SIPEXII[SIPEXII_Y6mask] # Remove NaN values from SI
Sol_SI_SIPEXII = Sol_SIPEXII[SIPEXII_Y6mask] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)

#--------------------------------
# V1_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V1_17, p_valueD1_V1_17 = stats.pearsonr(O3_V1_17,BrO_O3_V1_17)
slopeD1_V1_17, interceptD1_V1_17, rD1_V1_17, pD1_V1_17, std_errD1_V1_17 = stats.linregress(O3_V1_17,BrO_O3_V1_17)

# 2) Between Temp and BrO
r_rowD2_V1_17, p_valueD2_V1_17 = stats.pearsonr(Temp_V1_17,BrO_V1_17)
slopeD2_V1_17, interceptD2_V1_17, rD2_V1_17, pD2_V1_17, std_errD2_V1_17 = stats.linregress(Temp_V1_17,BrO_V1_17)

# 3) Between Wind Direction and BrO
r_rowD3_V1_17, p_valueD3_V1_17 = stats.pearsonr(WD_vect_V1_17,BrO_WD_V1_17)
slopeD3_V1_17, interceptD3_V1_17, rD3_V1_17, pD3_V1_17, std_errD3_V1_17 = stats.linregress(WD_vect_V1_17,BrO_WD_V1_17)

# 4) Between Wind Speed and BrO
r_rowD4_V1_17, p_valueD4_V1_17 = stats.pearsonr(WS_V1_17,BrO_WS_V1_17)
slopeD4_V1_17, interceptD4_V1_17, rD4_V1_17, pD4_V1_17, std_errD4_V1_17 = stats.linregress(WS_V1_17,BrO_WS_V1_17)

# 5) Between Solar Radiation and BrO
r_rowD5_V1_17, p_valueD5_V1_17 = stats.pearsonr(Sol_V1_17,BrO_V1_17)
slopeD5_V1_17, interceptD5_V1_17, rD5_V1_17, pD5_V1_17, std_errD5_V1_17 = stats.linregress(Sol_V1_17,BrO_V1_17)

# 6) Between Hg0 and BrO
r_rowD6_V1_17, p_valueD6_V1_17 = stats.pearsonr(Hg0_V1_17,BrO_Hg0_V1_17)
slopeD6_V1_17, interceptD6_V1_17, rD6_V1_17, pD6_V1_17, std_errD6_V1_17 = stats.linregress(Hg0_V1_17,BrO_Hg0_V1_17)

# 7) Between SI and BrO
r_rowD7_V1_17, p_valueD7_V1_17 = stats.pearsonr(SI_SI_V1_17,BrO_SI_V1_17)
slopeD7_V1_17, interceptD7_V1_17, rD7_V1_17, pD7_V1_17, std_errD7_V1_17 = stats.linregress(SI_SI_V1_17,BrO_SI_V1_17)

#--------------------------------
# V2_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V2_17, p_valueD1_V2_17 = stats.pearsonr(O3_V2_17,BrO_O3_V2_17)
slopeD1_V2_17, interceptD1_V2_17, rD1_V2_17, pD1_V2_17, std_errD1_V2_17 = stats.linregress(O3_V2_17,BrO_O3_V2_17)

# 2) Between Temp and BrO
r_rowD2_V2_17, p_valueD2_V2_17 = stats.pearsonr(Temp_V2_17,BrO_V2_17)
slopeD2_V2_17, interceptD2_V2_17, rD2_V2_17, pD2_V2_17, std_errD2_V2_17 = stats.linregress(Temp_V2_17,BrO_V2_17)

# 3) Between Wind Direction and BrO
r_rowD3_V2_17, p_valueD3_V2_17 = stats.pearsonr(WD_vect_V2_17,BrO_WD_V2_17)
slopeD3_V2_17, interceptD3_V2_17, rD3_V2_17, pD3_V2_17, std_errD3_V2_17 = stats.linregress(WD_vect_V2_17,BrO_WD_V2_17)

# 4) Between Wind Speed and BrO
r_rowD4_V2_17, p_valueD4_V2_17 = stats.pearsonr(WS_V2_17,BrO_WS_V2_17)
slopeD4_V2_17, interceptD4_V2_17, rD4_V2_17, pD4_V2_17, std_errD4_V2_17 = stats.linregress(WS_V2_17,BrO_WS_V2_17)

# 5) Between Solar Radiation and BrO
r_rowD5_V2_17, p_valueD5_V2_17 = stats.pearsonr(Sol_V2_17,BrO_V2_17)
slopeD5_V2_17, interceptD5_V2_17, rD5_V2_17, pD5_V2_17, std_errD5_V2_17 = stats.linregress(Sol_V2_17,BrO_V2_17)

# 6) Between Hg0 and BrO
r_rowD6_V2_17, p_valueD6_V2_17 = stats.pearsonr(Hg0_V2_17,BrO_Hg0_V2_17)
slopeD6_V2_17, interceptD6_V2_17, rD6_V2_17, pD6_V2_17, std_errD6_V2_17 = stats.linregress(Hg0_V2_17,BrO_Hg0_V2_17)

# 7) Between SI and BrO
r_rowD7_V2_17, p_valueD7_V2_17 = stats.pearsonr(SI_SI_V2_17,BrO_SI_V2_17)
slopeD7_V2_17, interceptD7_V2_17, rD7_V2_17, pD7_V2_17, std_errD7_V2_17 = stats.linregress(SI_SI_V2_17,BrO_SI_V2_17)

#--------------------------------
# V3_17 (2017-18)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V3_17, p_valueD1_V3_17 = stats.pearsonr(O3_V3_17,BrO_O3_V3_17)
slopeD1_V3_17, interceptD1_V3_17, rD1_V3_17, pD1_V3_17, std_errD1_V3_17 = stats.linregress(O3_V3_17,BrO_O3_V3_17)

# 2) Between Temp and BrO
r_rowD2_V3_17, p_valueD2_V3_17 = stats.pearsonr(Temp_V1_17,BrO_V1_17)
slopeD2_V3_17, interceptD2_V3_17, rD2_V3_17, pD2_V3_17, std_errD2_V3_17 = stats.linregress(Temp_V3_17,BrO_V3_17)

# 3) Between Wind Direction and BrO
r_rowD3_V3_17, p_valueD3_V3_17 = stats.pearsonr(WD_vect_V3_17,BrO_WD_V3_17)
slopeD3_V3_17, interceptD3_V3_17, rD3_V3_17, pD3_V3_17, std_errD3_V3_17 = stats.linregress(WD_vect_V3_17,BrO_WD_V3_17)

# 4) Between Wind Speed and BrO
r_rowD4_V3_17, p_valueD4_V3_17 = stats.pearsonr(WS_V3_17,BrO_WS_V3_17)
slopeD4_V3_17, interceptD4_V3_17, rD4_V3_17, pD4_V3_17, std_errD4_V3_17 = stats.linregress(WS_V3_17,BrO_WS_V3_17)

# 5) Between Solar Radiation and BrO
r_rowD5_V3_17, p_valueD5_V3_17 = stats.pearsonr(Sol_V3_17,BrO_V3_17)
slopeD5_V3_17, interceptD5_V3_17, rD5_V3_17, pD5_V3_17, std_errD5_V3_17 = stats.linregress(Sol_V3_17,BrO_V3_17)

# 6) Between Hg0 and BrO
r_rowD6_V3_17, p_valueD6_V3_17 = stats.pearsonr(Hg0_V3_17,BrO_Hg0_V3_17)
slopeD6_V3_17, interceptD6_V3_17, rD6_V3_17, pD6_V3_17, std_errD6_V3_17 = stats.linregress(Hg0_V3_17,BrO_Hg0_V3_17)

# 7) Between SI and BrO
r_rowD7_V3_17, p_valueD7_V3_17 = stats.pearsonr(SI_SI_V3_17,BrO_SI_V3_17)
slopeD7_V3_17, interceptD7_V3_17, rD7_V3_17, pD7_V3_17, std_errD7_V3_17 = stats.linregress(SI_SI_V3_17,BrO_SI_V3_17)

#--------------------------------
# V1_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V1_18, p_valueD1_V1_18 = stats.pearsonr(O3_V1_18,BrO_O3_V1_18)
slopeD1_V1_18, interceptD1_V1_18, rD1_V1_18, pD1_V1_18, std_errD1_V1_18 = stats.linregress(O3_V1_18,BrO_O3_V1_18)

# 2) Between Temp and BrO
r_rowD2_V1_18, p_valueD2_V1_18 = stats.pearsonr(Temp_V1_18,BrO_V1_18)
slopeD2_V1_18, interceptD2_V1_18, rD2_V1_18, pD2_V1_18, std_errD2_V1_18 = stats.linregress(Temp_V1_18,BrO_V1_18)

# 3) Between Wind Direction and BrO
r_rowD3_V1_18, p_valueD3_V1_18 = stats.pearsonr(WD_vect_V1_18,BrO_WD_V1_18)
slopeD3_V1_18, interceptD3_V1_18, rD3_V1_18, pD3_V1_18, std_errD3_V1_18 = stats.linregress(WD_vect_V1_18,BrO_WD_V1_18)

# 4) Between Wind Speed and BrO
r_rowD4_V1_18, p_valueD4_V1_18 = stats.pearsonr(WS_V1_18,BrO_WS_V1_18)
slopeD4_V1_18, interceptD4_V1_18, rD4_V1_18, pD4_V1_18, std_errD4_V1_18 = stats.linregress(WS_V1_18,BrO_WS_V1_18)

# 5) Between Solar Radiation and BrO
r_rowD5_V1_18, p_valueD5_V1_18 = stats.pearsonr(Sol_V1_18,BrO_V1_18)
slopeD5_V1_18, interceptD5_V1_18, rD5_V1_18, pD5_V1_18, std_errD5_V1_18 = stats.linregress(Sol_V1_18,BrO_V1_18)

# 6) Between Hg0 and BrO
r_rowD6_V1_18, p_valueD6_V1_18 = stats.pearsonr(Hg0_V1_18,BrO_Hg0_V1_18)
slopeD6_V1_18, interceptD6_V1_18, rD6_V1_18, pD6_V1_18, std_errD6_V1_18 = stats.linregress(Hg0_V1_18,BrO_Hg0_V1_18)

# 7) Between SI and BrO
r_rowD7_V1_18, p_valueD7_V1_18 = stats.pearsonr(SI_SI_V1_18,BrO_SI_V1_18)
slopeD7_V1_18, interceptD7_V1_18, rD7_V1_18, pD7_V1_18, std_errD7_V1_18 = stats.linregress(SI_SI_V1_18,BrO_SI_V1_18)

#--------------------------------
# V2_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V2_18, p_valueD1_V2_18 = stats.pearsonr(O3_V2_18,BrO_O3_V2_18)
slopeD1_V2_18, interceptD1_V2_18, rD1_V2_18, pD1_V2_18, std_errD1_V2_18 = stats.linregress(O3_V2_18,BrO_O3_V2_18)

# 2) Between Temp and BrO
r_rowD2_V2_18, p_valueD2_V2_18 = stats.pearsonr(Temp_V2_18,BrO_V2_18)
slopeD2_V2_18, interceptD2_V2_18, rD2_V2_18, pD2_V2_18, std_errD2_V2_18 = stats.linregress(Temp_V2_18,BrO_V2_18)

# 3) Between Wind Direction and BrO
r_rowD3_V2_18, p_valueD3_V2_18 = stats.pearsonr(WD_vect_V2_18,BrO_WD_V2_18)
slopeD3_V2_18, interceptD3_V2_18, rD3_V2_18, pD3_V2_18, std_errD3_V2_18 = stats.linregress(WD_vect_V2_18,BrO_WD_V2_18)

# 4) Between Wind Speed and BrO
r_rowD4_V2_18, p_valueD4_V2_18 = stats.pearsonr(WS_V2_18,BrO_WS_V2_18)
slopeD4_V2_18, interceptD4_V2_18, rD4_V2_18, pD4_V2_18, std_errD4_V2_18 = stats.linregress(WS_V2_18,BrO_WS_V2_18)

# 5) Between Solar Radiation and BrO
r_rowD5_V2_18, p_valueD5_V2_18 = stats.pearsonr(Sol_V2_18,BrO_V2_18)
slopeD5_V2_18, interceptD5_V2_18, rD5_V2_18, pD5_V2_18, std_errD5_V2_18 = stats.linregress(Sol_V2_18,BrO_V2_18)

# 6) Between Hg0 and BrO
r_rowD6_V2_18, p_valueD6_V2_18 = stats.pearsonr(Hg0_V2_18,BrO_Hg0_V2_18)
slopeD6_V2_18, interceptD6_V2_18, rD6_V2_18, pD6_V2_18, std_errD6_V2_18 = stats.linregress(Hg0_V2_18,BrO_Hg0_V2_18)

# 7) Between SI and BrO
r_rowD7_V2_18, p_valueD7_V2_18 = stats.pearsonr(SI_SI_V2_18,BrO_SI_V2_18)
slopeD7_V2_18, interceptD7_V2_18, rD7_V2_18, pD7_V2_18, std_errD7_V2_18 = stats.linregress(SI_SI_V2_18,BrO_SI_V2_18)

#--------------------------------
# V3_18 (2018-19)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_V3_18, p_valueD1_V3_18 = stats.pearsonr(O3_V3_18,BrO_O3_V3_18)
slopeD1_V3_18, interceptD1_V3_18, rD1_V3_18, pD1_V3_18, std_errD1_V3_18 = stats.linregress(O3_V3_18,BrO_O3_V3_18)

# 2) Between Temp and BrO
r_rowD2_V3_18, p_valueD2_V3_18 = stats.pearsonr(Temp_V1_18,BrO_V1_18)
slopeD2_V3_18, interceptD2_V3_18, rD2_V3_18, pD2_V3_18, std_errD2_V3_18 = stats.linregress(Temp_V3_18,BrO_V3_18)

# 3) Between Wind Direction and BrO
r_rowD3_V3_18, p_valueD3_V3_18 = stats.pearsonr(WD_vect_V3_18,BrO_WD_V3_18)
slopeD3_V3_18, interceptD3_V3_18, rD3_V3_18, pD3_V3_18, std_errD3_V3_18 = stats.linregress(WD_vect_V3_18,BrO_WD_V3_18)

# 4) Between Wind Speed and BrO
r_rowD4_V3_18, p_valueD4_V3_18 = stats.pearsonr(WS_V3_18,BrO_WS_V3_18)
slopeD4_V3_18, interceptD4_V3_18, rD4_V3_18, pD4_V3_18, std_errD4_V3_18 = stats.linregress(WS_V3_18,BrO_WS_V3_18)

# 5) Between Solar Radiation and BrO
r_rowD5_V3_18, p_valueD5_V3_18 = stats.pearsonr(Sol_V3_18,BrO_V3_18)
slopeD5_V3_18, interceptD5_V3_18, rD5_V3_18, pD5_V3_18, std_errD5_V3_18 = stats.linregress(Sol_V3_18,BrO_V3_18)

# 6) Between Hg0 and BrO
r_rowD6_V3_18, p_valueD6_V3_18 = stats.pearsonr(Hg0_V3_18,BrO_Hg0_V3_18)
slopeD6_V3_18, interceptD6_V3_18, rD6_V3_18, pD6_V3_18, std_errD6_V3_18 = stats.linregress(Hg0_V3_18,BrO_Hg0_V3_18)

# 7) Between SI and BrO
r_rowD7_V3_18, p_valueD7_V3_18 = stats.pearsonr(SI_SI_V3_18,BrO_SI_V3_18)
slopeD7_V3_18, interceptD7_V3_18, rD7_V3_18, pD7_V3_18, std_errD7_V3_18 = stats.linregress(SI_SI_V3_18,BrO_SI_V3_18)

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_SIPEXII, p_valueD1_SIPEXII = stats.pearsonr(O3_SIPEXII,BrO_SIPEXII)
slopeD1_SIPEXII, interceptD1_SIPEXII, rD1_SIPEXII, pD1_SIPEXII, std_errD1_SIPEXII = stats.linregress(O3_SIPEXII,BrO_SIPEXII)

# 2) Between Temp and BrO
r_rowD2_SIPEXII, p_valueD2_SIPEXII = stats.pearsonr(Temp_SIPEXII,BrO_SIPEXII)
slopeD2_SIPEXII, interceptD2_SIPEXII, rD2_SIPEXII, pD2_SIPEXII, std_errD2_SIPEXII = stats.linregress(Temp_SIPEXII,BrO_SIPEXII)

# 3) Between Wind Direction and BrO
r_rowD3_SIPEXII, p_valueD3_SIPEXII = stats.pearsonr(WD_vect_SIPEXII,BrO_WD_SIPEXII)
slopeD3_SIPEXII, interceptD3_SIPEXII, rD3_SIPEXII, pD3_SIPEXII, std_errD3_SIPEXII = stats.linregress(WD_vect_SIPEXII,BrO_WD_SIPEXII)

# 4) Between Wind Speed and BrO
r_rowD4_SIPEXII, p_valueD4_SIPEXII = stats.pearsonr(WS_SIPEXII,BrO_WS_SIPEXII)
slopeD4_SIPEXII, interceptD4_SIPEXII, rD4_SIPEXII, pD4_SIPEXII, std_errD4_SIPEXII = stats.linregress(WS_SIPEXII,BrO_WS_SIPEXII)

# 5) Between Solar Radiation and BrO
r_rowD5_SIPEXII, p_valueD5_SIPEXII = stats.pearsonr(Sol_SIPEXII,BrO_SIPEXII)
slopeD5_SIPEXII, interceptD5_SIPEXII, rD5_SIPEXII, pD5_SIPEXII, std_errD5_SIPEXII = stats.linregress(Sol_SIPEXII,BrO_SIPEXII)

# 6) Between Hg0 and BrO
r_rowD6_SIPEXII, p_valueD6_SIPEXII = stats.pearsonr(Hg0_SIPEXII,BrO_Hg0_SIPEXII)
slopeD6_SIPEXII, interceptD6_SIPEXII, rD6_SIPEXII, pD6_SIPEXII, std_errD6_SIPEXII = stats.linregress(Hg0_SIPEXII,BrO_Hg0_SIPEXII)

# 7) Between SI and BrO
r_rowD7_SIPEXII, p_valueD7_SIPEXII = stats.pearsonr(SI_SI_SIPEXII,BrO_SI_SIPEXII)
slopeD7_SIPEXII, interceptD7_SIPEXII, rD7_SIPEXII, pD7_SIPEXII, std_errD7_SIPEXII = stats.linregress(SI_SI_SIPEXII,BrO_SI_SIPEXII)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs O3)

fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3_V1_17, BrO_O3_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_O3_V1_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3_V1_17, interceptD1_V1_17 + slopeD1_V1_17*O3_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V1_17))+" $\pm$"+str("%7.4f"%(std_errD1_V1_17))+" pptv, r: "+str("%7.4f"%(rD1_V1_17))+")", xy=(1.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 2 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3_V2_17, BrO_O3_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_O3_V2_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3_V2_17, interceptD1_V2_17 + slopeD1_V2_17*O3_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V2_17))+" $\pm$"+str("%7.4f"%(std_errD1_V2_17))+" pptv, r: "+str("%7.4f"%(rD1_V2_17))+")", xy=(1.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 3 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3_V3_17, BrO_O3_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_O3_V3_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3_V3_17, interceptD1_V3_17 + slopeD1_V3_17*O3_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V3_17))+" $\pm$"+str("%7.4f"%(std_errD1_V3_17))+" pptv, r: "+str("%7.4f"%(rD1_V3_17))+")", xy=(1.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 4 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3_V1_18, BrO_O3_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_O3_V1_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3_V1_18, interceptD1_V1_18 + slopeD1_V1_18*O3_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V1_18))+" $\pm$"+str("%7.4f"%(std_errD1_V1_18))+" pptv, r: "+str("%7.4f"%(rD1_V1_18))+")", xy=(1.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 5 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3_V2_18, BrO_O3_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_O3_V2_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3_V2_18, interceptD1_V2_18 + slopeD1_V2_18*O3_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V2_18))+" $\pm$"+str("%7.4f"%(std_errD1_V2_18))+" pptv, r: "+str("%7.4f"%(rD1_V2_18))+")", xy=(1.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 6 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3_V3_18, BrO_O3_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_O3_V3_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3_V3_18, interceptD1_V3_18 + slopeD1_V3_18*O3_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_V3_18))+" $\pm$"+str("%7.4f"%(std_errD1_V3_18))+" pptv, r: "+str("%7.4f"%(rD1_V3_18))+")", xy=(1.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 7 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(O3_SIPEXII, BrO_SIPEXII, edgecolors='none', marker='o', norm=norm, c=Sol_SIPEXII, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line1, = plt.plot(O3_SIPEXII, interceptD1_SIPEXII + slopeD1_SIPEXII*O3_SIPEXII, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=10)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=15)
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1_SIPEXII))+" $\pm$"+str("%7.4f"%(std_errD1_SIPEXII))+" pptv, r: "+str("%7.4f"%(rD1_SIPEXII))+")", xy=(1.0,17.0), color='black', fontweight='bold')

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Temperature)

fig2 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp_V1_17, BrO_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_V1_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp_V1_17, interceptD2_V1_17 + slopeD2_V1_17*Temp_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V1_17))+" $\pm$"+str("%7.4f"%(std_errD2_V1_17))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V1_17))+")", xy=(-20.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp_V2_17, BrO_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_V2_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp_V2_17, interceptD2_V2_17 + slopeD2_V2_17*Temp_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V2_17))+" $\pm$"+str("%7.4f"%(std_errD2_V2_17))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V2_17))+")", xy=(-20.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp_V3_17, BrO_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_V3_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp_V3_17, interceptD2_V3_17 + slopeD2_V3_17*Temp_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V3_17))+" $\pm$"+str("%7.4f"%(std_errD2_V3_17))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V3_17))+")", xy=(-20.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp_V1_18, BrO_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_V1_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp_V1_18, interceptD2_V1_18 + slopeD2_V1_18*Temp_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V1_18))+" $\pm$"+str("%7.4f"%(std_errD2_V1_18))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V1_18))+")", xy=(-20.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp_V2_18, BrO_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_V2_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp_V2_18, interceptD2_V2_18 + slopeD2_V2_18*Temp_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V2_18))+" $\pm$"+str("%7.4f"%(std_errD2_V2_18))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V2_18))+")", xy=(-20.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp_V3_18, BrO_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_V3_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp_V3_18, interceptD2_V3_18 + slopeD2_V3_18*Temp_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_V3_18))+" $\pm$"+str("%7.4f"%(std_errD2_V3_18))+" $^\circ$C, r: "+str("%7.4f"%(rD2_V3_18))+")", xy=(-20.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Temp_SIPEXII, BrO_SIPEXII, edgecolors='none', marker='o', norm=norm, c=Sol_SIPEXII, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line2, = plt.plot(Temp_SIPEXII, interceptD2_SIPEXII + slopeD2_SIPEXII*Temp_SIPEXII, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=10)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=15)
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2_SIPEXII))+" $\pm$"+str("%7.4f"%(std_errD2_SIPEXII))+" $^\circ$C, r: "+str("%7.4f"%(rD2_SIPEXII))+")", xy=(-20.0,18.0), color='black', fontweight='bold')

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Direction)

fig3 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect_V1_17, BrO_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_V1_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect_V1_17, interceptD3_V1_17 + slopeD3_V1_17*WD_vect_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V1_17))+" $\pm$"+str("%7.4f"%(std_errD3_V1_17))+" $^\circ$, r: "+str("%7.4f"%(rD3_V1_17))+")", xy=(10.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect_V2_17, BrO_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_V2_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect_V2_17, interceptD3_V2_17 + slopeD3_V2_17*WD_vect_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V2_17))+" $\pm$"+str("%7.4f"%(std_errD3_V2_17))+" $^\circ$, r: "+str("%7.4f"%(rD3_V2_17))+")", xy=(10.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect_V3_17, BrO_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_V3_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect_V3_17, interceptD3_V3_17 + slopeD3_V3_17*WD_vect_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V3_17))+" $\pm$"+str("%7.4f"%(std_errD3_V3_17))+" $^\circ$, r: "+str("%7.4f"%(rD3_V3_17))+")", xy=(10.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect_V1_18, BrO_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_V1_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect_V1_18, interceptD3_V1_18 + slopeD3_V1_18*WD_vect_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V1_18))+" $\pm$"+str("%7.4f"%(std_errD3_V1_18))+" $^\circ$, r: "+str("%7.4f"%(rD3_V1_18))+")", xy=(10.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect_V2_18, BrO_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_V2_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect_V2_18, interceptD3_V2_18 + slopeD3_V2_18*WD_vect_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V2_18))+" $\pm$"+str("%7.4f"%(std_errD3_V2_18))+" $^\circ$, r: "+str("%7.4f"%(rD3_V2_18))+")", xy=(10.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect_V3_18, BrO_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_V3_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect_V3_18, interceptD3_V3_18 + slopeD3_V3_18*WD_vect_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_V3_18))+" $\pm$"+str("%7.4f"%(std_errD3_V3_18))+" $^\circ$, r: "+str("%7.4f"%(rD3_V3_18))+")", xy=(10.0,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WD_vect_SIPEXII, BrO_SIPEXII, edgecolors='none', marker='o', norm=norm, c=Sol_SIPEXII, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line3, = plt.plot(WD_vect_SIPEXII, interceptD3_SIPEXII + slopeD3_SIPEXII*WD_vect_SIPEXII, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=10)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=15)
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3_SIPEXII))+" $\pm$"+str("%7.4f"%(std_errD3_SIPEXII))+" $^\circ$, r: "+str("%7.4f"%(rD3_SIPEXII))+")", xy=(10.0,18.0), color='black', fontweight='bold')

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Speed)

fig4 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS_V1_17, BrO_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_V1_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS_V1_17, interceptD4_V1_17 + slopeD4_V1_17*WS_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 21.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind speed (m/s)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4_V1_17))+" $\pm$"+str("%7.4f"%(std_errD4_V1_17))+" m/s, r: "+str("%7.4f"%(rD4_V1_17))+")", xy=(0.5,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS_V2_17, BrO_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_V2_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS_V2_17, interceptD4_V2_17 + slopeD4_V2_17*WS_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 21.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind speed (m/s)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4_V2_17))+" $\pm$"+str("%7.4f"%(std_errD4_V2_17))+" m/s, r: "+str("%7.4f"%(rD4_V2_17))+")", xy=(0.5,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS_V3_17, BrO_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_V3_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS_V3_17, interceptD4_V3_17 + slopeD4_V3_17*WS_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 21.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind speed (m/s)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4_V3_17))+" $\pm$"+str("%7.4f"%(std_errD4_V3_17))+" m/s, r: "+str("%7.4f"%(rD4_V3_17))+")", xy=(0.5,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS_V1_18, BrO_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_V1_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS_V1_18, interceptD4_V1_18 + slopeD4_V1_18*WS_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 21.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind speed (m/s)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4_V1_18))+" $\pm$"+str("%7.4f"%(std_errD4_V1_18))+" m/s, r: "+str("%7.4f"%(rD4_V1_18))+")", xy=(0.5,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS_V2_18, BrO_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_V2_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS_V2_18, interceptD4_V2_18 + slopeD4_V2_18*WS_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 21.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind speed (m/s)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4_V2_18))+" $\pm$"+str("%7.4f"%(std_errD4_V2_18))+" m/s, r: "+str("%7.4f"%(rD4_V2_18))+")", xy=(0.5,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS_V3_18, BrO_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_V3_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS_V3_18, interceptD4_V3_18 + slopeD4_V3_18*WS_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 21.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind speed (m/s)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4_V3_18))+" $\pm$"+str("%7.4f"%(std_errD4_V3_18))+" m/s, r: "+str("%7.4f"%(rD4_V3_18))+")", xy=(0.5,18.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(WS_SIPEXII, BrO_SIPEXII, edgecolors='none', marker='o', norm=norm, c=Sol_SIPEXII, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line4, = plt.plot(WS_SIPEXII, interceptD4_SIPEXII + slopeD4_SIPEXII*WS_SIPEXII, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 21.9)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Wind speed (m/s)', fontsize=10)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=15)
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4_SIPEXII))+" $\pm$"+str("%7.4f"%(std_errD4_SIPEXII))+" m/s, r: "+str("%7.4f"%(rD4_SIPEXII))+")", xy=(0.5,18.0), color='black', fontweight='bold')

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Solar Radiation)

fig5 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol_V1_17, BrO_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_V1_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol_V1_17, interceptD5_V1_17 + slopeD5_V1_17*Sol_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5_V1_17))+" $\pm$"+str("%7.4f"%(std_errD5_V1_17))+" W/m$^2$, r: "+str("%7.4f"%(rD5_V1_17))+")", xy=(15.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol_V2_17, BrO_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_V2_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol_V2_17, interceptD5_V2_17 + slopeD5_V2_17*Sol_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5_V2_17))+" $\pm$"+str("%7.4f"%(std_errD5_V2_17))+" W/m$^2$, r: "+str("%7.4f"%(rD5_V2_17))+")", xy=(15.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol_V3_17, BrO_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_V3_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol_V3_17, interceptD5_V3_17 + slopeD5_V3_17*Sol_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5_V3_17))+" $\pm$"+str("%7.4f"%(std_errD5_V3_17))+" W/m$^2$, r: "+str("%7.4f"%(rD5_V3_17))+")", xy=(15.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol_V1_18, BrO_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_V1_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol_V1_18, interceptD5_V1_18 + slopeD5_V1_18*Sol_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5_V1_18))+" $\pm$"+str("%7.4f"%(std_errD5_V1_18))+" W/m$^2$, r: "+str("%7.4f"%(rD5_V1_18))+")", xy=(15.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol_V2_18, BrO_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_V2_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol_V2_18, interceptD5_V2_18 + slopeD5_V2_18*Sol_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5_V2_18))+" $\pm$"+str("%7.4f"%(std_errD5_V2_18))+" W/m$^2$, r: "+str("%7.4f"%(rD5_V2_18))+")", xy=(15.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol_V3_18, BrO_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_V3_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol_V3_18, interceptD5_V3_18 + slopeD5_V3_18*Sol_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5_V3_18))+" $\pm$"+str("%7.4f"%(std_errD5_V3_18))+" W/m$^2$, r: "+str("%7.4f"%(rD5_V3_18))+")", xy=(15.0,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Sol_SIPEXII, BrO_SIPEXII, edgecolors='none', marker='o', norm=norm, c=Sol_SIPEXII, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line5, = plt.plot(Sol_SIPEXII, interceptD5_SIPEXII + slopeD5_SIPEXII*Sol_SIPEXII, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=15)
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5_SIPEXII))+" $\pm$"+str("%7.4f"%(std_errD5_SIPEXII))+" W/m$^2$, r: "+str("%7.4f"%(rD5_SIPEXII))+")", xy=(15.0,17.0), color='black', fontweight='bold')

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Hg0)

fig6 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Hg0_V1_17, BrO_Hg0_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_Hg0_V1_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(Hg0_V1_17, interceptD6_V1_17 + slopeD6_V1_17*Hg0_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0, 1.45)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=15)
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6_V1_17))+" $\pm$ "+str("%7.4f"%(std_errD6_V1_17))+" ng/m$^2$, r: "+str("%7.4f"%(rD6_V1_17))+")", xy=(0.015,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Hg0_V2_17, BrO_Hg0_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_Hg0_V2_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(Hg0_V2_17, interceptD6_V2_17 + slopeD6_V2_17*Hg0_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0, 1.45)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=15)
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6_V2_17))+" $\pm$ "+str("%7.4f"%(std_errD6_V2_17))+" ng/m$^2$, r: "+str("%7.4f"%(rD6_V2_17))+")", xy=(0.015,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Hg0_V3_17, BrO_Hg0_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_Hg0_V3_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(Hg0_V3_17, interceptD6_V3_17 + slopeD6_V3_17*Hg0_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0, 1.45)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=15)
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6_V3_17))+" $\pm$ "+str("%7.4f"%(std_errD6_V3_17))+" ng/m$^2$, r: "+str("%7.4f"%(rD6_V3_17))+")", xy=(0.015,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Hg0_V1_18, BrO_Hg0_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_Hg0_V1_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(Hg0_V1_18, interceptD6_V1_18 + slopeD6_V1_18*Hg0_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0, 1.45)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=15)
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6_V1_18))+" $\pm$ "+str("%7.4f"%(std_errD6_V1_18))+" ng/m$^2$, r: "+str("%7.4f"%(rD6_V1_18))+")", xy=(0.015,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Hg0_V2_18, BrO_Hg0_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_Hg0_V2_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(Hg0_V2_18, interceptD6_V2_18 + slopeD6_V2_18*Hg0_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0, 1.45)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=15)
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6_V2_18))+" $\pm$ "+str("%7.4f"%(std_errD6_V2_18))+" ng/m$^2$, r: "+str("%7.4f"%(rD6_V2_18))+")", xy=(0.015,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Hg0_V3_18, BrO_Hg0_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_Hg0_V3_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(Hg0_V3_18, interceptD6_V3_18 + slopeD6_V3_18*Hg0_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0, 1.45)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=15)
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6_V3_18))+" $\pm$ "+str("%7.4f"%(std_errD6_V3_18))+" ng/m$^2$, r: "+str("%7.4f"%(rD6_V3_18))+")", xy=(0.015,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(Hg0_SIPEXII, BrO_Hg0_SIPEXII, edgecolors='none', marker='o', norm=norm, c=Sol_Hg0_SIPEXII, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(Hg0_SIPEXII, interceptD6_SIPEXII + slopeD6_SIPEXII*Hg0_SIPEXII, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0, 1.45)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=10)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=15)
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6_SIPEXII))+" $\pm$ "+str("%7.4f"%(std_errD6_SIPEXII))+" ng/m$^2$, r: "+str("%7.4f"%(rD6_SIPEXII))+")", xy=(0.015,17.0), color='black', fontweight='bold')

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Sea Ice)

fig7 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI_V1_17, BrO_V1_17, edgecolors='none', marker='o', norm=norm, c=Sol_V1_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI_V1_17, interceptD7_V1_17 + slopeD7_V1_17*SI_V1_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1, 101.0)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2017-18)', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7_V1_17))+" $\pm$"+str("%7.4f"%(std_errD7_V1_17))+" %, r: "+str("%7.4f"%(rD7_V1_17))+")", xy=(0.5,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI_V2_17, BrO_V2_17, edgecolors='none', marker='o', norm=norm, c=Sol_V2_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI_V2_17, interceptD7_V2_17 + slopeD7_V2_17*SI_V2_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1, 101.0)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2017-18)', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7_V2_17))+" $\pm$"+str("%7.4f"%(std_errD7_V2_17))+" %, r: "+str("%7.4f"%(rD7_V2_17))+")", xy=(0.5,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI_V3_17, BrO_V3_17, edgecolors='none', marker='o', norm=norm, c=Sol_V3_17, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI_V3_17, interceptD7_V3_17 + slopeD7_V3_17*SI_V3_17, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1, 101.0)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2017-18)', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7_V3_17))+" $\pm$"+str("%7.4f"%(std_errD7_V3_17))+" %, r: "+str("%7.4f"%(rD7_V3_17))+")", xy=(0.5,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI_V1_18, BrO_V1_18, edgecolors='none', marker='o', norm=norm, c=Sol_V1_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI_V1_18, interceptD7_V1_18 + slopeD7_V1_18*SI_V1_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1, 101.0)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V1 (2018-19)', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7_V1_18))+" $\pm$"+str("%7.4f"%(std_errD7_V1_18))+" %, r: "+str("%7.4f"%(rD7_V1_18))+")", xy=(0.5,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI_V2_18, BrO_V2_18, edgecolors='none', marker='o', norm=norm, c=Sol_V2_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI_V2_18, interceptD7_V2_18 + slopeD7_V2_18*SI_V2_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1, 101.0)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V2 (2018-19)', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7_V2_18))+" $\pm$"+str("%7.4f"%(std_errD7_V2_18))+" %, r: "+str("%7.4f"%(rD7_V2_18))+")", xy=(0.5,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI_V3_18, BrO_V3_18, edgecolors='none', marker='o', norm=norm, c=Sol_V3_18, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI_V3_18, interceptD7_V3_18 + slopeD7_V3_18*SI_V3_18, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1, 101.0)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('V3 (2018-19)', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7_V3_18))+" $\pm$"+str("%7.4f"%(std_errD7_V3_18))+" %, r: "+str("%7.4f"%(rD7_V3_18))+")", xy=(0.5,17.0), color='black', fontweight='bold')

#--------------------------------
# Graph 7
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)

# BrO VMR
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,1600,200), cmap.N)
plt.scatter(SI_SIPEXII, BrO_SIPEXII, edgecolors='none', marker='o', norm=norm, c=Sol_SIPEXII, cmap=cmap)
plt.colorbar(label='Solar radiation (W/m$^2$)')

# Plot the regression line
line6, = plt.plot(SI_SIPEXII, interceptD7_SIPEXII + slopeD7_SIPEXII*SI_SIPEXII, color='black') #, label="O3 and BrO:\n (slope: "+str("%7.4f"%(p_valueD1))+"$\pm$ "+str("%7.4f"%(std_errD1))+"%, r: "+str("%7.4f"%(r_rowD1))+")")

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1, 101.0)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 21.5)

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=10)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=15)
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7_SIPEXII))+" $\pm$"+str("%7.4f"%(std_errD7_SIPEXII))+" %, r: "+str("%7.4f"%(rD7_SIPEXII))+")", xy=(0.5,17.0), color='black', fontweight='bold')
