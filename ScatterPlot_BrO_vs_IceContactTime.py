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
import netCDF4 as nc
import xarray as xr
from netCDF4 import Dataset

# Date and Time handling package
import datetime as dt
from datetime import datetime,time, timedelta		# functions to handle date and time
from matplotlib.colors import BoundaryNorm

#------------------------------------------------------------------------------
# DEFINE THE DATASET

#--------------
# BrO
#--------------
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv',index_col=0)       # BrO V1 (2017/18)
BrO_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv',index_col=0)       # BrO V2 (2017/18)
BrO_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv',index_col=0)       # BrO V3 (2017/18)

BrO_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv',index_col=0)       # BrO V1 (2018/19)
BrO_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv',index_col=0)       # BrO V2 (2018/19)
BrO_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv',index_col=0)       # BrO V3 (2018/19)

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv',index_col=0) # BrO SIPEXII (2012)

#--------------
# SZA
#--------------
SZA_V1_17  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_SZA/V1_17_SZA.csv',index_col=0) # SZA V1 (2017/18)
SZA_V2_17  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_SZA/V2_17_SZA.csv',index_col=0) # SZA V2 (2017/18)
SZA_V3_17M = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_SZA/V3_17_SZA.csv',index_col=0) # SZA V3 (2017/18)
SZA_V3_17D = SZA_V3_17M

SZA_V1_18  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_SZA/V1_18_SZA.csv',index_col=0) # SZA V1 (2018/19)
SZA_V2_18  = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_SZA/V2_18_SZA.csv',index_col=0) # SZA V2 (2018/19)
SZA_V3_18M = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_SZA/V3_18_SZA.csv',index_col=0) # SZA V3 (2018/19)
SZA_V3_18D = SZA_V3_18M

SZA_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_SZA/SIPEXII_SZA.csv',index_col=0) # SZA SIPEXII (2012)
                         
#--------------
# SEA ICE CONTACT TIME
#--------------
SI_100m_V1_18  = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/IceContactTime_100m.csv', index_col=0)
SI_100m_V2_18  = SI_100m_V1_18
SI_100m_V3_18M = SI_100m_V1_18
SI_100m_V3_18D = SI_100m_V1_18
                  
#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR RELATIVE ERROR 

#----------------
# BrO (Retrieval)
#----------------
# Calculate the Relative Error (>=0.6)
Filter1_BrO = BrO_V1_17['err_surf_vmr'] / BrO_V1_17['surf_vmr(ppmv)']
Filter2_BrO = BrO_V2_17['err_surf_vmr'] / BrO_V2_17['surf_vmr(ppmv)']
Filter3_BrO = BrO_V3_17['err_surf_vmr'] / BrO_V3_17['surf_vmr(ppmv)']

Filter4_BrO = BrO_V1_18['err_surf_vmr'] / BrO_V1_18['surf_vmr(ppmv)']
Filter5_BrO = BrO_V2_18['err_surf_vmr'] / BrO_V2_18['surf_vmr(ppmv)']
Filter6_BrO = BrO_V3_18['err_surf_vmr'] / BrO_V3_18['surf_vmr(ppmv)']

Filter7_BrO = BrO_SIPEXII['err_surf_vmr'] / BrO_SIPEXII['surf_vmr(ppmv)']

# Apply the filter
V1_17F       = Filter1_BrO < 0.6
BrO_V1_17T   = BrO_V1_17[V1_17F]

V2_17F       = Filter2_BrO < 0.6
BrO_V2_17T   = BrO_V2_17[V2_17F]

V3_17F       = Filter3_BrO < 0.6
BrO_V3_17T   = BrO_V3_17[V3_17F]

V1_18F       = Filter4_BrO < 0.6
BrO_V1_18T   = BrO_V1_18[V1_18F]

V2_18F       = Filter5_BrO < 0.6
BrO_V2_18T   = BrO_V2_18[V2_18F]

V3_18F       = Filter6_BrO < 0.6
BrO_V3_18T   = BrO_V3_18[V3_18F]

SIPEXIIF     = Filter7_BrO < 0.6
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

#--------------
# BrO
#--------------
BrO_V1_17T.index   = (pd.to_datetime(BrO_V1_17T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_17T.index   = (pd.to_datetime(BrO_V2_17T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_17MT.index  = (pd.to_datetime(BrO_V3_17MT.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_17DT.index  = (pd.to_datetime(BrO_V3_17DT.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_V1_18T.index   = (pd.to_datetime(BrO_V1_18T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_18T.index   = (pd.to_datetime(BrO_V2_18T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_18MT.index  = (pd.to_datetime(BrO_V3_18MT.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_18DT.index  = (pd.to_datetime(BrO_V3_18DT.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_SIPEXIIT.index = (pd.to_datetime(BrO_SIPEXIIT.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#--------------
# SZA
#--------------
SZA_V1_17.index   = (pd.to_datetime(SZA_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SZA_V2_17.index   = (pd.to_datetime(SZA_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SZA_V3_17M.index  = (pd.to_datetime(SZA_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
SZA_V3_17D.index  = (pd.to_datetime(SZA_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

SZA_V1_18.index   = (pd.to_datetime(SZA_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SZA_V2_18.index   = (pd.to_datetime(SZA_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SZA_V3_18M.index  = (pd.to_datetime(SZA_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
SZA_V3_18D.index  = (pd.to_datetime(SZA_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

SZA_SIPEXII.index = (pd.to_datetime(SZA_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#--------------
# SEA ICE CONTACT TIME
#--------------

# SI_100m_V1_17.index   = (pd.to_datetime(SI_100m_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
# SI_100m_V2_17.index   = (pd.to_datetime(SI_100m_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
# SI_100m_V3_17M.index  = (pd.to_datetime(SI_100m_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
# SI_100m_V3_17D.index  = (pd.to_datetime(SI_100m_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

SI_100m_V1_18.index   = (pd.to_datetime(SI_100m_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SI_100m_V2_18.index   = (pd.to_datetime(SI_100m_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SI_100m_V3_18M.index  = (pd.to_datetime(SI_100m_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
SI_100m_V3_18D.index  = (pd.to_datetime(SI_100m_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#SI_100m_SIPEXII.index = (pd.to_datetime(SI_100m_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# Filter the SZA for outliers

# Define the filter
def hampel(vals_orig, k=11, t0=3):
    '''
    vals: pandas series of values from which to remove outliers
    k: size of window (including the sample; 7 is equal to 3 on either side of value)
    '''
    #Make copy so original not edited
    vals=vals_orig.copy()    
    #Hampel Filter
    L= 1.4826
    rolling_median=vals.rolling(k).median()
    difference=np.abs(rolling_median-vals)
    median_abs_deviation=difference.rolling(k).median()
    threshold= t0 *L * median_abs_deviation
    outlier_idx=difference>threshold
    vals[outlier_idx]=np.nan
    return(vals)

# Apply the filter
SZA_1 = hampel(SZA_V1_17['SZA'])
SZA_2 = hampel(SZA_V2_17['SZA'])
SZA_3 = hampel(SZA_V3_17M['SZA'])
SZA_4 = hampel(SZA_V3_17D['SZA'])

SZA_5 = hampel(SZA_V1_18['SZA'])
SZA_6 = hampel(SZA_V2_18['SZA'])
SZA_7 = hampel(SZA_V3_18M['SZA'])
SZA_8 = hampel(SZA_V3_18D['SZA'])

SZA_9 = hampel(SZA_SIPEXII['SZA'])

#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR SZA (less than 75 degrees)

# Apply the filter
SZA_V1_17F   = SZA_1 < 75
SZA_V1_17T   = SZA_1[SZA_V1_17F]

SZA_V2_17F   = SZA_2 < 75
SZA_V2_17T   = SZA_2[SZA_V2_17F]

SZA_V3_17MF  = SZA_3 < 75
SZA_V3_17MT  = SZA_3[SZA_V3_17MF]

SZA_V3_17DF  = SZA_4 < 75
SZA_V3_17DT  = SZA_4[SZA_V3_17DF]


SZA_V1_18F   = SZA_5 < 75
SZA_V1_18T   = SZA_5[SZA_V1_18F]

SZA_V2_18F   = SZA_6 < 75
SZA_V2_18T   = SZA_6[SZA_V2_18F]

SZA_V3_18MF  = SZA_7 < 75
SZA_V3_18MT  = SZA_7[SZA_V3_18MF]

SZA_V3_18DF  = SZA_8 < 75
SZA_V3_18DT  = SZA_8[SZA_V3_18DF]


SZA_SIPEXIIF = SZA_9 < 75
SZA_SIPEXIIT = SZA_9[SZA_SIPEXIIF]

#------------------------------------------------------------------------------
# RESAMPLE THE SZA DATASETS TO 20-MINUTE TIME RESOLUTION

SZA_V1_17T   = SZA_V1_17T.resample('20T',   offset='10T').mean()
SZA_V2_17T   = SZA_V2_17T.resample('20T',   offset='10T').mean()
SZA_V3_17MT  = SZA_V3_17MT.resample('20T',  offset='10T').mean()
SZA_V3_17DT  = SZA_V3_17DT.resample('20T',  offset='10T').mean()

SZA_V1_18T   = SZA_V1_18T.resample('20T',   offset='10T').mean()
SZA_V2_18T   = SZA_V2_18T.resample('20T',   offset='10T').mean()
SZA_V3_18MT  = SZA_V3_18MT.resample('20T',  offset='10T').mean()
SZA_V3_18DT  = SZA_V3_18DT.resample('20T',  offset='10T').mean()

SZA_SIPEXIIT = SZA_SIPEXIIT.resample('20T', offset='10T').mean()

#------------------------------------------------------------------------------
# COMBINE THE SZA DATAFRAMES

# BrO (Retrieval)
BrO_V1_17T   = pd.concat([BrO_V1_17T,   SZA_V1_17T],   axis=1, join='inner')
BrO_V2_17T   = pd.concat([BrO_V2_17T,   SZA_V2_17T],   axis=1, join='inner')
BrO_V3_17MT  = pd.concat([BrO_V3_17MT,  SZA_V3_17MT],  axis=1, join='inner')
BrO_V3_17DT  = pd.concat([BrO_V3_17DT,  SZA_V3_17DT],  axis=1, join='inner')

BrO_V1_18T   = pd.concat([BrO_V1_18T,   SZA_V1_18T],   axis=1, join='inner')
BrO_V2_18T   = pd.concat([BrO_V2_18T,   SZA_V2_18T],   axis=1, join='inner')
BrO_V3_18MT  = pd.concat([BrO_V3_18MT,  SZA_V3_18MT],  axis=1, join='inner')
BrO_V3_18DT  = pd.concat([BrO_V3_18DT,  SZA_V3_18DT],  axis=1, join='inner')

BrO_SIPEXIIT = pd.concat([BrO_SIPEXIIT, SZA_SIPEXIIT], axis=1, join='inner')

# Drop nan values
BrO_V1_17T   = BrO_V1_17T.dropna()
BrO_V2_17T   = BrO_V2_17T.dropna()
BrO_V3_17MT  = BrO_V3_17MT.dropna()
BrO_V3_17DT  = BrO_V3_17DT.dropna()

BrO_V1_18T   = BrO_V1_18T.dropna()
BrO_V2_18T   = BrO_V2_18T.dropna()
BrO_V3_18MT  = BrO_V3_18MT.dropna()
BrO_V3_18DT  = BrO_V3_18DT.dropna()

BrO_SIPEXIIT = BrO_SIPEXIIT.dropna()

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
# RESAMPLE BrO TO 60 MIN AVERAGES

#--------------
# BrO
#--------------
BrO_V1_17T   = BrO_V1_17T.resample('60T').mean()
BrO_V2_17T   = BrO_V2_17T.resample('60T').mean()
BrO_V3_17MT  = BrO_V3_17MT.resample('60T').mean()
BrO_V3_17DT  = BrO_V3_17DT.resample('60T').mean()

BrO_V1_18T   = BrO_V1_18T.resample('60T').mean()
BrO_V2_18T   = BrO_V2_18T.resample('60T').mean()
BrO_V3_18MT  = BrO_V3_18MT.resample('60T').mean()
BrO_V3_18DT  = BrO_V3_18DT.resample('60T').mean()

BrO_SIPEXIIT = BrO_SIPEXIIT.resample('60T').mean()

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
# FILTER THE DATAFRAMES TO ONLY INCLUDE THE SAME DATES

# # Find periods when BrO and Met are collocated
# V1_17_BrO_100m   = pd.merge(left=V1_17_BrO,   right=SI_100m_V1_17,   how='left', left_index=True, right_index=True)
# V2_17_BrO_100m   = pd.merge(left=V2_17_BrO,   right=SI_100m_V2_17,   how='left', left_index=True, right_index=True)
# V3_17_BrOM_100m  = pd.merge(left=V3_17_BrOM,  right=SI_100m_V3_17M,  how='left', left_index=True, right_index=True)
# V3_17_BrOD_100m  = pd.merge(left=V3_17_BrOD,  right=SI_100m_V3_17D,  how='left', left_index=True, right_index=True)

V1_18_BrO_100m   = pd.merge(left=V1_18_BrO,   right=SI_100m_V1_18,   how='left', left_index=True, right_index=True)
V2_18_BrO_100m   = pd.merge(left=V2_18_BrO,   right=SI_100m_V2_18,   how='left', left_index=True, right_index=True)
V3_18_BrOM_100m  = pd.merge(left=V3_18_BrOM,  right=SI_100m_V3_18M,  how='left', left_index=True, right_index=True)
V3_18_BrOD_100m  = pd.merge(left=V3_18_BrOD,  right=SI_100m_V3_18D,  how='left', left_index=True, right_index=True)

#SIPEXII_BrO_100m = pd.merge(left=SIPEXII_BrO, right=SI_100m_SIPEXII, how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# CREATE A DATAFRAME

BrO_All_100m = pd.concat([V1_18_BrO_100m, V2_18_BrO_100m, V3_18_BrOM_100m, V3_18_BrOD_100m],axis=0) # Without SIPEXII

# Fix the units for BrO_LTcol and BrO_surf
BrO_All_100m["BrO_VCD(molec/cm^2)"]       = BrO_All_100m["BrO_VCD(molec/cm^2)"]/1e13
BrO_All_100m['surf_num_dens(molec/cm^3)'] = BrO_All_100m['surf_num_dens(molec/cm^3)']*20000/1e13

# Drop nan values
BrO_All_100m.dropna(subset = ["BrO_VCD(molec/cm^2)"], inplace=True)

#------------------------------------------------------------------------------
# DEFINE THE VARIABLES

# BrO
BrO_LTcol = BrO_All_100m['BrO_VCD(molec/cm^2)']
BrO_surf  = BrO_All_100m['surf_num_dens(molec/cm^3)']

# Ice contact time
Ice_MLH   = BrO_All_100m['Ice_MLH']
Ice_100m  = BrO_All_100m['Ice_100m']
SIC_MLH   = BrO_All_100m['SIC_MLH']
SIC_100m  = BrO_All_100m['SIC_100m']

#------------------------------------------------------------------------------
# CALCULATE THE CORRELATION COEFFICIENT (R)

# BrO & Ice_MLH
slope_LTcol_IceMLH,  intercept_LTcol_IceMLH,  r_LTcol_IceMLH,  p_LTcol_IceMLH,  stderr_LTcol_IceMLH  = stats.linregress(BrO_LTcol, Ice_MLH)
slope_surf_IceMLH,   intercept_surf_IceMLH,   r_surf_IceMLH,   p_surf_IceMLH,   stderr_surf_IceMLH   = stats.linregress(BrO_surf,  Ice_MLH)

# BrO & Ice_100m
slope_LTcol_Ice100m, intercept_LTcol_Ice100m, r_LTcol_Ice100m, p_LTcol_Ice100m, stderr_LTcol_Ice100m = stats.linregress(BrO_LTcol, Ice_100m)
slope_surf_Ice100m,  intercept_surf_Ice100m,  r_surf_Ice100m,  p_surf_Ice100m,  stderr_surf_Ice100m  = stats.linregress(BrO_surf,  Ice_100m)

# BrO & SIC_MLH
slope_LTcol_SICMLH,  intercept_LTcol_SICMLH,  r_LTcol_SICMLH,  p_LTcol_SICMLH,  stderr_LTcol_SICMLH  = stats.linregress(BrO_LTcol, SIC_MLH)
slope_surf_SICMLH,   intercept_surf_SICMLH,   r_surf_SICMLH,   p_surf_SICMLH,   stderr_surf_SICMLH   = stats.linregress(BrO_surf,  SIC_MLH)

# BrO & SIC_100m
slope_LTcol_SIC100m, intercept_LTcol_SIC100m, r_LTcol_SIC100m, p_LTcol_SIC100m, stderr_LTcol_SIC100m = stats.linregress(BrO_LTcol, SIC_100m)
slope_surf_SIC100m,  intercept_surf_SIC100m,  r_surf_SIC100m,  p_surf_SIC100m,  stderr_surf_SIC100m  = stats.linregress(BrO_surf,  SIC_100m)

#------------------------------------------------------------------------------
# PLOT FIGURE 1 (Ice_MLH)
fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(Ice_MLH, BrO_LTcol, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line1, = plt.plot(Ice_MLH, intercept_LTcol_IceMLH + slope_LTcol_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(Ice_MLH, BrO_LTcol, 1)
plt.plot(Ice_MLH, m*Ice_MLH + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_LTcol_IceMLH))+"\nr$^2$: "+str("%7.4f"%(r_LTcol_IceMLH * r_LTcol_IceMLH)), xy=(115.0,1.6), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_L$$_T$$_c$$_o$$_l$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_L$$_T$$_c$$_o$$_l$ and sea ice', fontsize=15, y=1.03)

#--------------------------------
# Graph 2
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(Ice_MLH, BrO_surf, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line2, = plt.plot(Ice_MLH, intercept_surf_IceMLH + slope_surf_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(Ice_MLH, BrO_surf, 1)
plt.plot(Ice_MLH, m*Ice_MLH + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_surf_IceMLH))+"\nr$^2$: "+str("%7.4f"%(r_surf_IceMLH * r_surf_IceMLH)), xy=(115.0,0.4), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_ylim(0,0.5)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_s$$_u$$_r$$_f$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_s$$_u$$_r$$_f$ and sea ice', fontsize=15, y=1.03)

#------------------------------------------------------------------------------
# PLOT FIGURE 2 (Ice_100m)
fig2 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(Ice_100m, BrO_LTcol, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line1, = plt.plot(Ice_MLH, intercept_LTcol_IceMLH + slope_LTcol_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(Ice_100m, BrO_LTcol, 1)
plt.plot(Ice_100m, m*Ice_100m + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_LTcol_Ice100m))+"\nr$^2$: "+str("%7.4f"%(r_LTcol_Ice100m * r_LTcol_Ice100m)), xy=(115.0,1.6), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_L$$_T$$_c$$_o$$_l$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_L$$_T$$_c$$_o$$_l$ and sea ice', fontsize=15, y=1.03)

#--------------------------------
# Graph 2
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(Ice_100m, BrO_surf, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line2, = plt.plot(Ice_MLH, intercept_surf_IceMLH + slope_surf_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(Ice_100m, BrO_surf, 1)
plt.plot(Ice_100m, m*Ice_100m + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_surf_Ice100m))+"\nr$^2$: "+str("%7.4f"%(r_surf_Ice100m * r_surf_Ice100m)), xy=(115.0,0.4), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_ylim(0,0.5)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_s$$_u$$_r$$_f$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_s$$_u$$_r$$_f$ and sea ice', fontsize=15, y=1.03)

#------------------------------------------------------------------------------
# PLOT FIGURE 3 (SIC_MLH)
fig3 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(SIC_MLH, BrO_LTcol, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line1, = plt.plot(Ice_MLH, intercept_LTcol_IceMLH + slope_LTcol_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(SIC_MLH, BrO_LTcol, 1)
plt.plot(SIC_MLH, m*SIC_MLH + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_LTcol_SICMLH))+"\nr$^2$: "+str("%7.4f"%(r_LTcol_SICMLH * r_LTcol_SICMLH)), xy=(115.0,1.6), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_L$$_T$$_c$$_o$$_l$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_L$$_T$$_c$$_o$$_l$ and sea ice', fontsize=15, y=1.03)

#--------------------------------
# Graph 2
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(SIC_MLH, BrO_surf, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line2, = plt.plot(Ice_MLH, intercept_surf_IceMLH + slope_surf_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(SIC_MLH, BrO_surf, 1)
plt.plot(SIC_MLH, m*SIC_MLH + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_surf_SICMLH))+"\nr$^2$: "+str("%7.4f"%(r_surf_SICMLH * r_surf_SICMLH)), xy=(115.0,0.4), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_ylim(0,0.5)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_s$$_u$$_r$$_f$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_s$$_u$$_r$$_f$ and sea ice', fontsize=15, y=1.03)

#------------------------------------------------------------------------------
# PLOT FIGURE 4 (SIC_100m)
fig4 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#--------------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(SIC_100m, BrO_LTcol, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line1, = plt.plot(Ice_MLH, intercept_LTcol_IceMLH + slope_LTcol_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(SIC_100m, BrO_LTcol, 1)
plt.plot(SIC_100m, m*SIC_100m + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_LTcol_SIC100m))+"\nr$^2$: "+str("%7.4f"%(r_LTcol_SIC100m * r_LTcol_SIC100m)), xy=(115.0,1.6), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,2)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_L$$_T$$_c$$_o$$_l$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_L$$_T$$_c$$_o$$_l$ and sea ice', fontsize=15, y=1.03)

#--------------------------------
# Graph 2
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
plt.scatter(SIC_100m, BrO_surf, edgecolors='none', marker='o', c='b', s = 5)

# Plot the regression line
#line2, = plt.plot(Ice_MLH, intercept_surf_IceMLH + slope_surf_IceMLH * Ice_MLH, color='black') 
m, b = np.polyfit(SIC_100m, BrO_surf, 1)
plt.plot(SIC_100m, m*SIC_100m + b, color='black')

# Plot the label for the regression line
plt.annotate("r:  "+str("%7.4f"%(r_surf_SIC100m))+"\nr$^2$: "+str("%7.4f"%(r_surf_SIC100m * r_surf_SIC100m)), xy=(105.0,0.4), color='black', fontweight='bold', fontsize=12)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_xlim(-5,125)

# Format y-axis 1
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_ylim(0,0.5)

# Plot the axis labels
ax.set_xlabel('Sea ice contact time (hours)', fontsize=15)
ax.set_ylabel('BrO$_s$$_u$$_r$$_f$ (10$^1$$^3$ molec/cm$^2$)', fontsize=15)

#Plot the legend and title
plt.title('Relationshp between BrO$_s$$_u$$_r$$_f$ and sea ice', fontsize=15, y=1.03)

