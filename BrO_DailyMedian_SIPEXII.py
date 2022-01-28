#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:26:31 2019

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
from matplotlib.lines import Line2D

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

#---------
# BrO
#---------
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv',index_col=0) # BrO V1 (2017/18)
BrO_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv',index_col=0) # BrO V2 (2017/18)
BrO_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv',index_col=0) # BrO V3 (2017/18)

BrO_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv',index_col=0) # BrO V1 (2018/19)
BrO_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv',index_col=0) # BrO V2 (2018/19)
BrO_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv',index_col=0) # BrO V3 (2018/19)

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv',index_col=0) # BrO SIPEXII (2012)

#---------
# SZA
#---------
SZA_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_SZA/V1_17_SZA.csv',index_col=0) # SZA V1 (2017/18)
SZA_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_SZA/V2_17_SZA.csv',index_col=0) # SZA V2 (2017/18)
SZA_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_SZA/V3_17_SZA.csv',index_col=0) # SZA V3 (2017/18)

SZA_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_SZA/V1_18_SZA.csv',index_col=0) # SZA V1 (2018/19)
SZA_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_SZA/V2_18_SZA.csv',index_col=0) # SZA V2 (2018/19)
SZA_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_SZA/V3_18_SZA.csv',index_col=0) # SZA V3 (2018/19)

SZA_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_SZA/SIPEXII_SZA.csv',index_col=0) # SZA SIPEXII (2012)

#--------------
# Met
#--------------
Met_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V1_17_underway_60.csv', index_col=0)
Met_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V2_17_underway_60.csv', index_col=0)
Met_V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V3_17_underway_60.csv', index_col=0)

Met_V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V1_18_underway_60.csv', index_col=0) 
Met_V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V2_18_underway_60.csv', index_col=0)
Met_V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V3_18_underway_60.csv', index_col=0) 

Met_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/ShipTrack/SIPEXII_underway_60.csv', index_col=0) 

#--------------
# Sea Ice
#--------------
SI_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv', index_col=0)

#SI_V1_17  = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_17_BrO.csv',  index_col=0)
#SI_V2_17  = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_17_BrO.csv',  index_col=0)
SI_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv', index_col=0)
SI_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv', index_col=0)
SI_V3_17  = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_17M_BrO.csv', index_col=0)

#SI_V1_18  = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V1_18_BrO.csv',  index_col=0)
#SI_V2_18  = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V2_18_BrO.csv',  index_col=0)
SI_V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv', index_col=0)
SI_V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv', index_col=0)
SI_V3_18  = pd.read_csv('/Users/ncp532/Documents/Data/SeaIce_Trajectories/Traj_V3_18M_BrO.csv', index_col=0)

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
# Set the date

#---------
# BrO
#---------
BrO_V1_17T.index  = (pd.to_datetime(BrO_V1_17T.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_17T.index  = (pd.to_datetime(BrO_V2_17T.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_17T.index  = (pd.to_datetime(BrO_V3_17T.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

BrO_V1_18T.index  = (pd.to_datetime(BrO_V1_18T.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_18T.index  = (pd.to_datetime(BrO_V2_18T.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_18T.index  = (pd.to_datetime(BrO_V3_18T.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

BrO_SIPEXIIT.index = (pd.to_datetime(BrO_SIPEXIIT.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#---------
# SZA
#---------
SZA_V1_17.index  = (pd.to_datetime(SZA_V1_17.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SZA_V2_17.index  = (pd.to_datetime(SZA_V2_17.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SZA_V3_17.index  = (pd.to_datetime(SZA_V3_17.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

SZA_V1_18.index  = (pd.to_datetime(SZA_V1_18.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SZA_V2_18.index  = (pd.to_datetime(SZA_V2_18.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SZA_V3_18.index  = (pd.to_datetime(SZA_V3_18.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

SZA_SIPEXII.index = (pd.to_datetime(SZA_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#--------------
# Met
#--------------
Met_V1_17.index  = (pd.to_datetime(Met_V1_17.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
Met_V2_17.index  = (pd.to_datetime(Met_V2_17.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
Met_V3_17.index  = (pd.to_datetime(Met_V3_17.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

Met_V1_18.index  = (pd.to_datetime(Met_V1_18.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
Met_V2_18.index  = (pd.to_datetime(Met_V2_18.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
Met_V3_18.index  = (pd.to_datetime(Met_V3_18.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

Met_SIPEXII.index = (pd.to_datetime(Met_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#--------------
# Sea Ice
#--------------
SI_V1_17.index  = (pd.to_datetime(SI_V1_17.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SI_V2_17.index  = (pd.to_datetime(SI_V2_17.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SI_V3_17.index  = pd.to_datetime(SI_V3_17.index,  dayfirst=True)

SI_V1_18.index  = (pd.to_datetime(SI_V1_18.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SI_V2_18.index  = (pd.to_datetime(SI_V2_18.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SI_V3_18.index  = pd.to_datetime(SI_V3_18.index,  dayfirst=True)

SI_SIPEXII.index = (pd.to_datetime(SI_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

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
SZA_3 = hampel(SZA_V3_17['SZA'])

SZA_4 = hampel(SZA_V1_18['SZA'])
SZA_5 = hampel(SZA_V2_18['SZA'])
SZA_6 = hampel(SZA_V3_18['SZA'])

SZA_7 = hampel(SZA_SIPEXII['SZA'])

#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR SZA (less than 75 degrees)

# Apply the filter
SZA_V1_17F   = SZA_1 < 75
SZA_V1_17T   = SZA_1[SZA_V1_17F]

SZA_V2_17F   = SZA_2 < 75
SZA_V2_17T   = SZA_2[SZA_V2_17F]

SZA_V3_17F   = SZA_3 < 75
SZA_V3_17T   = SZA_3[SZA_V3_17F]

SZA_V1_18F   = SZA_4 < 75
SZA_V1_18T   = SZA_4[SZA_V1_18F]

SZA_V2_18F   = SZA_5 < 75
SZA_V2_18T   = SZA_5[SZA_V2_18F]

SZA_V3_18F   = SZA_6 < 75
SZA_V3_18T   = SZA_6[SZA_V3_18F]

SZA_SIPEXIIF = SZA_7 < 75
SZA_SIPEXIIT = SZA_7[SZA_SIPEXIIF]

#------------------------------------------------------------------------------
# CONVERT THE SZA DATASETS TO 20-MINUTE TIME RESOLUTION

SZA_V1_17T   = SZA_V1_17T.resample('20T',   offset='10T').mean()
SZA_V2_17T   = SZA_V2_17T.resample('20T',   offset='10T').mean()
SZA_V3_17T   = SZA_V3_17T.resample('20T',   offset='10T').mean()

SZA_V1_18T   = SZA_V1_18T.resample('20T',   offset='10T').mean()
SZA_V2_18T   = SZA_V2_18T.resample('20T',   offset='10T').mean()
SZA_V3_18T   = SZA_V3_18T.resample('20T',   offset='10T').mean()

SZA_SIPEXIIT = SZA_SIPEXIIT.resample('20T', offset='10T').mean()

#------------------------------------------------------------------------------
# COMBINE THE BrO and SZA DATAFRAMES

# BrO (Retrieval)
BrO_SZA_V1_17 = pd.concat([BrO_V1_17T,SZA_V1_17T],axis=1,join='inner')
BrO_SZA_V2_17 = pd.concat([BrO_V2_17T,SZA_V2_17T],axis=1,join='inner')
BrO_SZA_V3_17 = pd.concat([BrO_V3_17T,SZA_V3_17T],axis=1,join='inner')

BrO_SZA_V1_18 = pd.concat([BrO_V1_18T,SZA_V1_18T],axis=1,join='inner')
BrO_SZA_V2_18 = pd.concat([BrO_V2_18T,SZA_V2_18T],axis=1,join='inner')
BrO_SZA_V3_18 = pd.concat([BrO_V3_18T,SZA_V3_18T],axis=1,join='inner')

BrO_SZA_SIPEXII = pd.concat([BrO_SIPEXIIT,SZA_SIPEXIIT],axis=1,join='inner')

# Drop nan values
BrO_SZA_V1_17 = BrO_SZA_V1_17.dropna()
BrO_SZA_V2_17 = BrO_SZA_V2_17.dropna()
BrO_SZA_V3_17 = BrO_SZA_V3_17.dropna()

BrO_SZA_V1_18 = BrO_SZA_V1_18.dropna()
BrO_SZA_V2_18 = BrO_SZA_V2_18.dropna()
BrO_SZA_V3_18 = BrO_SZA_V3_18.dropna()

BrO_SZA_SIPEXII = BrO_SZA_SIPEXII.dropna()

#------------------------------------------------------------------------------
# CALCULATE THE BrO DAILY MEAN

# BrO Daily Means
BrO_V1_17_DM = BrO_SZA_V1_17.resample('D').mean()
BrO_V2_17_DM = BrO_SZA_V2_17.resample('D').mean()
BrO_V3_17_DM = BrO_SZA_V3_17.resample('D').mean()

BrO_V1_18_DM = BrO_SZA_V1_18.resample('D').mean()
BrO_V2_18_DM = BrO_SZA_V2_18.resample('D').mean()
BrO_V3_18_DM = BrO_SZA_V3_18.resample('D').mean()

BrO_SIPEXII_DM = BrO_SZA_SIPEXII.resample('D').mean()

# Met Daily Means
Met_V1_17_DM = Met_V1_17.resample('D').mean()
Met_V2_17_DM = Met_V2_17.resample('D').mean()
Met_V3_17_DM = Met_V3_17.resample('D').mean()

Met_V1_18_DM = Met_V1_18.resample('D').mean()
Met_V2_18_DM = Met_V2_18.resample('D').mean()
Met_V3_18_DM = Met_V3_18.resample('D').mean()

Met_SIPEXII_DM = Met_SIPEXII.resample('D').mean()

# SeaIce Daily Means
SI_V1_17_DM = SI_V1_17.resample('D').mean()
SI_V2_17_DM = SI_V2_17.resample('D').mean()
SI_V3_17_DM = SI_V3_17.resample('D').mean()

SI_V1_18_DM = SI_V1_18.resample('D').mean()
SI_V2_18_DM = SI_V2_18.resample('D').mean()
SI_V3_18_DM = SI_V3_18.resample('D').mean()

SI_SIPEXII_DM = SI_SIPEXII.resample('D').mean()

#------------------------------------------------------------------------------
# CALCULATE THE BrO DAILY STANDARD DEVIATION

# BrO Standard Deviations
BrO_V1_17_STD = BrO_SZA_V1_17.resample('D').std()
BrO_V2_17_STD = BrO_SZA_V2_17.resample('D').std()
BrO_V3_17_STD = BrO_SZA_V3_17.resample('D').std()

BrO_V1_18_STD = BrO_SZA_V1_18.resample('D').std()
BrO_V2_18_STD = BrO_SZA_V2_18.resample('D').std()
BrO_V3_18_STD = BrO_SZA_V3_18.resample('D').std()

BrO_SIPEXII_STD = BrO_SZA_SIPEXII.resample('D').std()

#------------------------------------------------------------------------------
# CALCULATE THE BrO DAILY MEDIAN

# BrO medians
BrO_V1_17_DMed = BrO_SZA_V1_17.resample('D').median()
BrO_V2_17_DMed = BrO_SZA_V2_17.resample('D').median()
BrO_V3_17_DMed = BrO_SZA_V3_17.resample('D').median()

BrO_V1_18_DMed = BrO_SZA_V1_18.resample('D').median()
BrO_V2_18_DMed = BrO_SZA_V2_18.resample('D').median()
BrO_V3_18_DMed = BrO_SZA_V3_18.resample('D').median()

BrO_SIPEXII_DMed = BrO_SZA_SIPEXII.resample('D').median()

#------------------------------------------------------------------------------
# Filter the datasets based on the date

#-----------------------------
# V1_17 Davis (14-22 Nov 2017)
#-----------------------------
start_date   = '2017-11-14'
end_date     = '2017-11-23'
# BrO (Retrieval)
Davis        = (BrO_SZA_V1_17.index >= start_date) & (BrO_SZA_V1_17.index < end_date)
V1_17_BrO    = BrO_SZA_V1_17[Davis]

#-----------------------------
# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
#-----------------------------
start_date1 = '2017-12-21'
end_date1 = '2017-12-23'
start_date2 = '2017-12-26'
end_date2 = '2018-01-6'
# BrO (Retrieval)
Casey1       = (BrO_SZA_V2_17.index >= start_date1) & (BrO_SZA_V2_17.index < end_date1)
Casey2       = (BrO_SZA_V2_17.index >= start_date2) & (BrO_SZA_V2_17.index < end_date2)
V2_17_BrO1   = BrO_SZA_V2_17[Casey1]
V2_17_BrO2   = BrO_SZA_V2_17[Casey2]
V2_17_BrO    = pd.concat([V2_17_BrO1,V2_17_BrO2], axis =0)

#-----------------------------
# V3_17 Mawson (1-17 Feb 2018)
#-----------------------------
start_date    = '2018-02-01'
end_date      = '2018-02-18'
# BrO (Retrieval)
Mawson        = (BrO_SZA_V3_17.index >= start_date) & (BrO_SZA_V3_17.index < end_date)
V3_17_BrOM    = BrO_SZA_V3_17[Mawson]

#-----------------------------
# V3_17 Davis (27-30 Jan 2018 and 19-21 Feb 2018)
#-----------------------------
start_date1   = '2018-01-27'
end_date1     = '2018-01-31'
start_date2   = '2018-02-19'
end_date2     = '2018-02-22'
# BrO (Retrieval)
Davis1        = (BrO_SZA_V3_17.index >= start_date1) & (BrO_SZA_V3_17.index < end_date1)
Davis2        = (BrO_SZA_V3_17.index >= start_date2) & (BrO_SZA_V3_17.index < end_date2)
V3_17_BrO1    = BrO_SZA_V3_17[Davis1]
V3_17_BrO2    = BrO_SZA_V3_17[Davis2]
V3_17_BrOD    = pd.concat([V3_17_BrO1,V3_17_BrO2], axis =0)

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# BrO (Retrieval)
Davis        = (BrO_SZA_V1_18.index >= start_date) & (BrO_SZA_V1_18.index < end_date)
V1_18_BrO    = BrO_SZA_V1_18[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# BrO (Retrieval)
Casey        = (BrO_SZA_V2_18.index >= start_date) & (BrO_SZA_V2_18.index < end_date)
V2_18_BrO    = BrO_SZA_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# BrO (Retrieval)
Mawson        = (BrO_SZA_V3_18.index >= start_date) & (BrO_SZA_V3_18.index < end_date)
V3_18_BrOM    = BrO_SZA_V3_18[Mawson]

#-----------------------------
# V3_18 Davis (26-28 Jan 2019 and 19-20 Feb 2019)
#-----------------------------
start_date1   = '2019-01-26'
end_date1     = '2019-01-29'
start_date2   = '2019-02-19'
end_date2     = '2019-02-21'
# BrO (Retrieval)
Davis1        = (BrO_SZA_V3_18.index >= start_date1) & (BrO_SZA_V3_18.index < end_date1)
Davis2        = (BrO_SZA_V3_18.index >= start_date2) & (BrO_SZA_V3_18.index < end_date2)
V3_18_BrO1    = BrO_SZA_V3_18[Davis1]
V3_18_BrO2    = BrO_SZA_V3_18[Davis2]
V3_18_BrOD    = pd.concat([V3_18_BrO1,V3_18_BrO2], axis =0)

#-----------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#-----------------------------
start_date     = '2012-09-23'
end_date       = '2012-11-12'
# BrO (Retrieval)
SIPEX          = (BrO_SZA_SIPEXII.index >= start_date) & (BrO_SZA_SIPEXII.index < end_date)
SIPEXII_BrO    = BrO_SZA_SIPEXII[SIPEX]

#------------------------------------------------------------------------------
# BrO while on station

# CAMMPCAN (2017-18)
BrO_17_D = np.array(V1_17_BrO['surf_vmr(ppmv)'])* 1e6
BrO_17_C = np.array(V2_17_BrO['surf_vmr(ppmv)'])* 1e6
BrO_17_M = np.array(V3_17_BrOM['surf_vmr(ppmv)'])* 1e6
BrO_17_D2= np.array(V3_17_BrOD['surf_vmr(ppmv)'])* 1e6

# CAMMPCAN (2018-19)
BrO_18_D = np.array(V1_18_BrO['surf_vmr(ppmv)'])* 1e6
BrO_18_C = np.array(V2_18_BrO['surf_vmr(ppmv)'])* 1e6
BrO_18_M = np.array(V3_18_BrOM['surf_vmr(ppmv)'])* 1e6
BrO_18_D2= np.array(V3_18_BrOD['surf_vmr(ppmv)'])* 1e6

# SIPEXII (2012)
BrO_SIPEXII_I = np.array(SIPEXII_BrO['surf_vmr(ppmv)'])* 1e6

# Season
season2017 = np.concatenate((BrO_17_D, BrO_17_C, BrO_17_M, BrO_17_D2), axis = None)
season2018 = np.concatenate((BrO_18_D, BrO_18_C, BrO_18_M, BrO_18_D2), axis = None)

# Station
Davis_All  = np.concatenate((BrO_17_D, BrO_17_D2, BrO_18_D, BrO_18_D2), axis = None) 
Casey_All  = np.concatenate((BrO_17_C, BrO_18_C), axis = None)
Mawson_All = np.concatenate((BrO_17_M, BrO_18_M), axis = None)

# All
All = np.concatenate((BrO_17_D, BrO_17_C, BrO_17_M, BrO_17_D2, BrO_18_D, BrO_18_C, BrO_18_M, BrO_18_D2), axis = None)
All_SIP = np.concatenate((BrO_17_D, BrO_17_C, BrO_17_M, BrO_17_D2, BrO_18_D, BrO_18_C, BrO_18_M, BrO_18_D2, BrO_SIPEXII_I), axis = None)

#-----------------------------
# Calculate the standard deviation
# 2017-18
std1 = np.std(BrO_17_D)
std2 = np.std(BrO_17_C)
std3 = np.std(BrO_17_M)
std8 = np.std(BrO_17_D2)
# 2018-19
std4 = np.std(BrO_18_D)
std5 = np.std(BrO_18_C)
std6 = np.std(BrO_18_M)
std9 = np.std(BrO_18_D2)
# 2012
std7 = np.std(BrO_SIPEXII_I)

# std for season
std2017 = np.std(season2017)
std2018 = np.std(season2018)

# std for station
std_Davis  = np.std(Davis_All)
std_Casey  = np.std(Casey_All)
std_Mawson = np.std(Mawson_All)

# std for all
std_All     = np.std(All) # CAMMPCAN only 
std_All_SIP = np.std(All_SIP) # CAMMPCAN + SIPEXII

#-----------------------------
# Calculate the mean
# 2017-18
mean1 = np.mean(BrO_17_D)
mean2 = np.mean(BrO_17_C)
mean3 = np.mean(BrO_17_M)
mean8 = np.mean(BrO_17_D2)
# 2018-19
mean4 = np.mean(BrO_18_D)
mean5 = np.mean(BrO_18_C)
mean6 = np.mean(BrO_18_M)
mean9 = np.mean(BrO_18_D2)
# 2012
mean7 = np.mean(BrO_SIPEXII_I)

# Mean for season
mean2017 = np.mean(season2017)
mean2018 = np.mean(season2018)

# Mean for station
mean_Davis  = np.mean(Davis_All)
mean_Casey  = np.mean(Casey_All)
mean_Mawson = np.mean(Mawson_All)

# mean for all
mean_All     = np.mean(All) # CAMMPCAN only
mean_All_SIP = np.mean(All_SIP) # CAMMPCAN + SIPEXII

#-----------------------------
# Calculate the median
# 2017-18
median1 = np.median(BrO_17_D)
median2 = np.median(BrO_17_C)
median3 = np.median(BrO_17_M)
median8 = np.median(BrO_17_D2)
# 2018-19
median4 = np.median(BrO_18_D)
median5 = np.median(BrO_18_C)
median6 = np.median(BrO_18_M)
median9 = np.median(BrO_18_D2)
# 2012
median7 = np.median(BrO_SIPEXII_I)

# Median for season
median2017 = np.median(season2017)
median2018 = np.median(season2018)

# Median for station
median_Davis  = np.median(Davis_All)
median_Casey  = np.median(Casey_All)
median_Mawson = np.median(Mawson_All)

# median for all
median_All     = np.median(All) # CAMMPCAN only
median_All_SIP = np.median(All_SIP) # CAMMPCAN + SIPEXII

#-----------------------------
# Calculate the median absolute deviation
# 2017-18
mad1 = stats.median_absolute_deviation(BrO_17_D)
mad2 = stats.median_absolute_deviation(BrO_17_C)
mad3 = stats.median_absolute_deviation(BrO_17_M)
mad8 = stats.median_absolute_deviation(BrO_17_D2)
# 2018-19
mad4 = stats.median_absolute_deviation(BrO_18_D)
mad5 = stats.median_absolute_deviation(BrO_18_C)
mad6 = stats.median_absolute_deviation(BrO_18_M)
mad9 = stats.median_absolute_deviation(BrO_18_D2)
# 2012
mad7 = stats.median_absolute_deviation(BrO_SIPEXII_I)

# MAD for season
mad2017 = stats.median_absolute_deviation(season2017)
mad2018 = stats.median_absolute_deviation(season2018)

# MAD for station
mad_Davis  = stats.median_absolute_deviation(Davis_All)
mad_Casey  = stats.median_absolute_deviation(Casey_All)
mad_Mawson = stats.median_absolute_deviation(Mawson_All)

# MAD for all
mad_All     = stats.median_absolute_deviation(All) # CAMMPCAN only
mad_All_SIP = stats.median_absolute_deviation(All_SIP) # CAMMPCAN + SIPEXII

#-----------------------------
# Calculate the max
# 2017-18
max1 = np.max(BrO_17_D)
max2 = np.max(BrO_17_C)
max3 = np.max(BrO_17_M)
max8 = np.max(BrO_17_D2)
# 2018-19
max4 = np.max(BrO_18_D)
max5 = np.max(BrO_18_C)
max6 = np.max(BrO_18_M)
max9 = np.max(BrO_18_D2)
# 2012
max7 = np.max(BrO_SIPEXII_I)

# max for station
max_Davis  = np.max(Davis_All)
max_Casey  = np.max(Casey_All)
max_Mawson = np.max(Mawson_All)

#-----------------------------
# Calculate the min
# 2017-18
min1 = np.min(BrO_17_D)
min2 = np.min(BrO_17_C)
min3 = np.min(BrO_17_M)
min8 = np.min(BrO_17_D2)
# 2018-19
min4 = np.min(BrO_18_D)
min5 = np.min(BrO_18_C)
min6 = np.min(BrO_18_M)
min9 = np.min(BrO_18_D2)
# 2012
min7 = np.min(BrO_SIPEXII_I)

# max for station
min_Davis  = np.min(Davis_All)
min_Casey  = np.min(Casey_All)
min_Mawson = np.min(Mawson_All)

#-----------------------------
# Calculate the 95 percentile
# 2017-18
p95_1 = np.percentile(BrO_17_D, 95)
p95_2 = np.percentile(BrO_17_C, 95)
p95_3 = np.percentile(BrO_17_M, 95)
p95_8 = np.percentile(BrO_17_D2, 95)
# 2018-19
p95_4 = np.percentile(BrO_18_D, 95)
p95_5 = np.percentile(BrO_18_C, 95)
p95_6 = np.percentile(BrO_18_M, 95)
p95_9 = np.percentile(BrO_18_D2, 95)
# 2012
p95_7 = np.percentile(BrO_SIPEXII_I, 95)

# MAD for season
p95_2017 = np.percentile(season2017, 95)
p95_2018 = np.percentile(season2018, 95)

# MAD for station
p95_Davis  = np.percentile(Davis_All, 95)
p95_Casey  = np.percentile(Casey_All, 95)
p95_Mawson = np.percentile(Mawson_All, 95)

# MAD for all
p95_All     = np.percentile(All, 95)
p95_All_SIP = np.percentile(All_SIP, 95)

#-----------------------------
# Calculate the 3-sigma (mean + 3*StDev)
# 2017-18
sigma3_1 = mean1 + 3*std1
sigma3_2 = mean2 + 3*std2
sigma3_3 = mean3 + 3*std3
sigma3_8 = mean8 + 3*std8
# 2018-19
sigma3_4 = mean4 + 3*std4
sigma3_5 = mean5 + 3*std5
sigma3_6 = mean6 + 3*std6
sigma3_9 = mean9 + 3*std9
# 2012
sigma3_7 = mean7 + 3*std7

# MAD for season
sigma3_2017 = mean2017 + 3*std2017
sigma3_2018 = mean2018 + 3*std2018

# MAD for station
sigma3_Davis  = mean_Davis + 3*std_Davis
sigma3_Casey  = mean_Casey + 3*std_Casey
sigma3_Mawson = mean_Mawson + 3*std_Mawson

# MAD for all
sigma3_All     = mean_All + 3*std_All
sigma3_All_SIP = mean_All_SIP + 3*std_All_SIP

#-----------------------------
# Calculate the median + 3*MAD
# 2017-18
sigMAD_1 = median1 + 3*mad1
sigMAD_2 = median2 + 3*mad2
sigMAD_3 = median3 + 3*mad3
sigMAD_8 = median8 + 3*mad8
# 2018-19
sigMAD_4 = median4 + 3*mad4
sigMAD_5 = median5 + 3*mad5
sigMAD_6 = median6 + 3*mad6
sigMAD_9 = median9 + 3*mad9
# 2012
sigMAD_7 = median7 + 3*mad7

# MAD for season
sigMAD_2017 = median2017 + 3*mad2017
sigMAD_2018 = median2018 + 3*mad2018

# MAD for station
sigMAD_Davis  = median_Davis + 3*mad_Davis
sigMAD_Casey  = median_Casey + 3*mad_Casey
sigMAD_Mawson = median_Mawson + 3*mad_Mawson

# MAD for all
sigMAD_All     = median_All + 3*mad_All
sigMAD_All_SIP = median_All_SIP + 3*mad_All_SIP

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.2)

#------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))
ax3.spines["left"].set_color('blue')

# Shade time on station
arrive1 = datetime(2017,11,14) # Arrive Davis (V1 17)
depart1 = datetime(2017,11,21) # Depart Davis (V1 17)
ax.axvspan(arrive1, depart1, color='lawngreen', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax.text(arrive1 + (depart1 - arrive1)/2, 13, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax.plot(BrO_V1_17_DMed.index, BrO_V1_17_DMed['surf_vmr(ppmv)']*1e6, marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2017-18)\n median:'+str("%5.1f"%(median1))+" $\pm$ "+str("%5.1f"%(mad1))+" pptv")
ax2.plot(Met_V1_17_DM.index, Met_V1_17_DM['latitude'], ls='--', c='black', label ='Latitude')
ax3.plot(SI_V1_17.index, SI_V1_17['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the error shading (BrO)
UL1 = BrO_V1_17_DMed['surf_vmr(ppmv)']*1e6 + BrO_V1_17_STD['surf_vmr(ppmv)']*1e6 # find the upper limit
LL1 = BrO_V1_17_DMed['surf_vmr(ppmv)']*1e6 - BrO_V1_17_STD['surf_vmr(ppmv)']*1e6 # find the lower limit
ax.plot(BrO_V1_17_DMed.index, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(BrO_V1_17_DMed.index, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(BrO_V1_17_DMed.index, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,15)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)

# Plot the legend and title
plt.title("V1 (Davis)", y=1.1, fontsize=15)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# Label for CAMMPCAN (2017-18)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, " CAMMPCAN (2017-18) ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))

# Shade time on station
arrive1 = datetime(2017,12,21) # Arrive Casey (V2 17)
depart1 = datetime(2017,12,22) # Depart Casey (V2 17)
arrive2 = datetime(2017,12,24) # Arrive Casey (V2 17)
depart2 = datetime(2018,1,6)   # Depart Casey (V2 17)
ax.axvspan(arrive1, depart1, color='pink', alpha=0.4, lw=0) # dark shade
ax.axvspan(arrive2, depart2, color='pink', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax.text(arrive1 + (depart1 - arrive1)/2, 14, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax.text(arrive2 + (depart2 - arrive2)/3, 14, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax.plot(BrO_V2_17_DMed.index, BrO_V2_17_DMed['surf_vmr(ppmv)']*1e6, marker='o', c='blue', markersize = 3.0, ls='-', label ='V2 (2017-18)\n median:'+str("%5.1f"%(median2))+" $\pm$ "+str("%5.1f"%(mad2))+" pptv")
ax2.plot(Met_V2_17_DM.index, Met_V2_17_DM['latitude'], ls='--', c='black', label ='Latitude')
ax3.plot(SI_V2_17_DM.index, SI_V2_17_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the error shading (BrO)
UL2 = BrO_V2_17_DMed['surf_vmr(ppmv)']*1e6 + BrO_V2_17_STD['surf_vmr(ppmv)']*1e6 # find the upper limit
LL2 = BrO_V2_17_DMed['surf_vmr(ppmv)']*1e6 - BrO_V2_17_STD['surf_vmr(ppmv)']*1e6 # find the lower limit
ax.plot(BrO_V2_17_DMed.index, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(BrO_V2_17_DMed.index, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(BrO_V2_17_DMed.index, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,15)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)

# Plot the legend and title
plt.title("V2 (Casey)", y=1.1, fontsize=15)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax3.spines["right"].set_color('grey')

# Shade time on station
arrive1 = datetime(2018,2,1)  # Arrive Mawson (V3 17)
depart1 = datetime(2018,2,18) # Depart Mawson (V3 17)
arrive2 = datetime(2018,1,27) # Arrive Davis (V3 17)
depart2 = datetime(2018,1,30) # Depart Davis (V3 17)
arrive3 = datetime(2018,2,19) # Arrive Davis (V3 17)
depart3 = datetime(2018,2,20) # Depart Davis (V3 17)
ax.axvspan(arrive1, depart1, color='orange',    alpha=0.4, lw=0) # dark shade
ax.axvspan(arrive2, depart2, color='lawngreen', alpha=0.4, lw=0)  # dark shade
ax.axvspan(arrive3, depart3, color='lawngreen', alpha=0.4, lw=0)  # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax.text(arrive1 + (depart1 - arrive1)/2, 13.5, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax.text(arrive2 + (depart2 - arrive2)/2, 13.5, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax.text(arrive3 + (depart3 - arrive3)/2, 13.5, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax.plot(BrO_V3_17_DMed.index, BrO_V3_17_DMed['surf_vmr(ppmv)']*1e6, marker='o', c='blue', markersize = 3.0, ls='-', label ='V3 (2017-18)\n median (Mawson):'+str("%5.1f"%(median3))+" $\pm$ "+str("%5.1f"%(mad3))+' pptv\n median (Davis):    '+str("%5.1f"%(median8))+" $\pm$ "+str("%5.1f"%(mad8))+" pptv")
ax2.plot(Met_V3_17_DM.index, Met_V3_17_DM['latitude'], ls='--', c='black', label ='Latitude')
ax3.plot(SI_V3_17_DM.index, SI_V3_17_DM['Sea Ice Conc (0-1)']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the error shading (BrO)
UL3 = BrO_V3_17_DMed['surf_vmr(ppmv)']*1e6 + BrO_V3_17_STD['surf_vmr(ppmv)']*1e6 # find the upper limit
LL3 = BrO_V3_17_DMed['surf_vmr(ppmv)']*1e6 - BrO_V3_17_STD['surf_vmr(ppmv)']*1e6 # find the lower limit
ax.plot(BrO_V3_17_DMed.index, UL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(BrO_V3_17_DMed.index, LL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(BrO_V3_17_DMed.index, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,15)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)

# Plot the axis labels
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)

#Plot the legend and title
plt.title("V3 (Mawson & Davis)", y=1.1, fontsize=15)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))
ax3.spines["left"].set_color('red')

# Shade time on station
arrive1 = datetime(2018,11,7)  # Arrive Davis (V1 18)
depart1 = datetime(2018,11,15) # Depart Davis (V1 18)
ax.axvspan(arrive1, depart1, color='lawngreen', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax.text(arrive1 + (depart1 - arrive1)/2, 13, "Davis", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax.plot(BrO_V1_18_DMed.index, BrO_V1_18_DMed['surf_vmr(ppmv)']*1e6, marker='o', c='red', markersize = 3.0, ls='-', label ='V1 (2018-19)\n median:'+str("%5.1f"%(median4))+" $\pm$ "+str("%5.1f"%(mad4))+" pptv")
ax2.plot(Met_V1_18_DM.index, Met_V1_18_DM['latitude'], ls='--', c='black', label ='Latitude')
ax3.plot(SI_V1_18_DM.index, SI_V1_18_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the error shading (BrO)
UL4 = BrO_V1_18_DMed['surf_vmr(ppmv)']*1e6 + BrO_V1_18_STD['surf_vmr(ppmv)']*1e6 # find the upper limit
LL4 = BrO_V1_18_DMed['surf_vmr(ppmv)']*1e6 - BrO_V1_18_STD['surf_vmr(ppmv)']*1e6 # find the lower limit
ax.plot(BrO_V1_18_DMed.index, UL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(BrO_V1_18_DMed.index, LL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(BrO_V1_18_DMed.index, UL4, LL4, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,15)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)

#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# Label for CAMMPCAN (2018-19)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, " CAMMPCAN (2018-19) ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

#------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
#ax3.spines["right"].set_position(("axes", 1.15))

# Shade time on station
arrive1 = datetime(2018,12,14) # Arrive Casey (V2 18)
depart1 = datetime(2018,12,28) # Depart Casey (V2 18)
ax.axvspan(arrive1, depart1, color='pink', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax.text(arrive1 + (depart1 - arrive1)/2, 14, "Casey", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax.plot(BrO_V2_18_DMed.index, BrO_V2_18_DMed['surf_vmr(ppmv)']*1e6, marker='o', c='red', markersize = 3.0, ls='-', label ='V2 (2018-19)\n median:'+str("%5.1f"%(median5))+" $\pm$ "+str("%5.1f"%(mad5))+" pptv")
ax2.plot(Met_V2_18_DM.index, Met_V2_18_DM['latitude'], ls='--', c='black', label ='Latitude')
ax3.plot(SI_V2_18_DM.index, SI_V2_18_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the error shading (BrO)
UL5 = BrO_V2_18_DMed['surf_vmr(ppmv)']*1e6 + BrO_V2_18_STD['surf_vmr(ppmv)']*1e6 # find the upper limit
LL5 = BrO_V2_18_DMed['surf_vmr(ppmv)']*1e6 - BrO_V2_18_STD['surf_vmr(ppmv)']*1e6 # find the lower limit
ax.plot(BrO_V2_18_DMed.index, UL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(BrO_V2_18_DMed.index, LL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(BrO_V2_18_DMed.index, UL5, LL5, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,15)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)
ax2.axes.get_yaxis().set_visible(False)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)
ax3.axes.get_yaxis().set_visible(False)

# Plot the axis labels
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
#ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)

#Plot the legend and title
#plt.title('BrO Daily Average (V2 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax3.spines["right"].set_color('grey')

# Shade time on station
arrive1 = datetime(2019,1,29) # Arrive Mawson (V3 18)
depart1 = datetime(2019,2,9) # Depart Mawson (V3 18)
arrive2 = datetime(2019,1,25) # Arrive Davis (V3 18)
depart2 = datetime(2019,1,27) # Depart Davis (V3 18)
arrive3 = datetime(2019,2,17) # Arrive Davis (V3 18)
depart3 = datetime(2019,2,19) # Depart Davis (V3 18)
ax.axvspan(arrive1, depart1, color='orange',    alpha=0.4, lw=0) # dark shade
ax.axvspan(arrive2, depart2, color='lawngreen', alpha=0.4, lw=0) # dark shade
ax.axvspan(arrive3, depart3, color='lawngreen', alpha=0.4, lw=0) # dark shade

# Text box for Station name
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax.text(arrive1 + (depart1 - arrive1)/2, 13.5, "Mawson", color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax.text(arrive2 + (depart2 - arrive2)/2, 13.5, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax.text(arrive3 + (depart3 - arrive3)/2, 13.5, "Davis",  color='black', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Plot the variables
ax.plot(BrO_V3_18_DMed.index, BrO_V3_18_DMed['surf_vmr(ppmv)']*1e6, marker='o', c='red', markersize = 3.0, ls='-', label ='V3 (2018-19)\n median (Mawson):'+str("%5.1f"%(median6))+" $\pm$ "+str("%5.1f"%(mad6))+' pptv\n median (Davis):    '+str("%5.1f"%(median9))+" $\pm$ "+str("%5.1f"%(mad9))+" pptv")
ax2.plot(Met_V3_18_DM.index, Met_V3_18_DM['latitude'], ls='--', c='black', label ='Latitude')
ax3.plot(SI_V3_18_DM.index, SI_V3_18_DM['Sea Ice Conc (0-1)']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the error shading (BrO)
UL6 = BrO_V3_18_DMed['surf_vmr(ppmv)']*1e6 + BrO_V3_18_STD['surf_vmr(ppmv)']*1e6 # find the upper limit
LL6 = BrO_V3_18_DMed['surf_vmr(ppmv)']*1e6 - BrO_V3_18_STD['surf_vmr(ppmv)']*1e6 # find the lower limit
ax.plot(BrO_V3_18_DMed.index, UL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(BrO_V3_18_DMed.index, LL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(BrO_V3_18_DMed.index, UL6, LL6, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,15)
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)

# Plot the axis labels
#ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)

#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

#------------------------------
# Graph 7
ax=plt.subplot(337) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax3.spines["right"].set_color('grey')
ax3.spines["left"].set_color('green')

# Plot the variables
ax.plot(BrO_SIPEXII_DMed.index, BrO_SIPEXII_DMed['surf_vmr(ppmv)']*1e6, marker='o', c='green', markersize = 3.0, ls='-', label ='SIPEXII (2012)\n median:'+str("%5.1f"%(median7))+" $\pm$"+str("%5.1f"%(mad7))+" pptv")
ax2.plot(Met_SIPEXII_DM.index, Met_SIPEXII_DM['latitude'], ls='--', c='black', label ='Latitude')
ax3.plot(SI_SIPEXII_DM.index, SI_SIPEXII_DM['Sea_Ice_Conc']*100, ls='--', c='grey', label ='Sea Ice Concentration')

# Plot the error shading (BrO)
UL7 = BrO_SIPEXII_DMed['surf_vmr(ppmv)']*1e6 + BrO_SIPEXII_STD['surf_vmr(ppmv)']*1e6 # find the upper limit
LL7 = BrO_SIPEXII_DMed['surf_vmr(ppmv)']*1e6 - BrO_SIPEXII_STD['surf_vmr(ppmv)']*1e6 # find the lower limit
ax.plot(BrO_SIPEXII_DMed.index, UL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(BrO_SIPEXII_DMed.index, LL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(BrO_SIPEXII_DMed.index, UL7, LL7, facecolor='green', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=10)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('green')
ax.tick_params(axis='y', which='both', colors='green')
ax.set_ylim(0,15)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.label.set_color('black')
ax2.tick_params(axis='y', which='both', colors='black')
ax2.set_ylim(-69,-42)

# Format y-axis 3
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.yaxis.label.set_color('grey')
ax3.tick_params(axis='y', which='both', colors='grey')
ax3.set_ylim(0,100)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
ax3.set_ylabel('Sea Ice Concentration (%)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)

#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# legend = ax.legend(loc='upper left')
# legend.get_frame().set_facecolor('#00FFCC')
# legend.get_frame().set_alpha(0.99)

# Label for SIPEXII (2012)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(-0.35, 0.5, "       SIPEXII (2012)       ", transform=ax.transAxes, fontsize=14, verticalalignment='center', bbox=props, rotation=90)

# Custom Legend
custom_lines = [Line2D([0], [0], color='blue',  lw=4),
                Line2D([0], [0], color='red',   lw=4),
                Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='black', lw=4),
                Line2D([0], [0], color='grey',  lw=4)]
fig.legend(custom_lines, ['BrO (CAMMPCAN 2017-18)', 'BrO (CAMMPCAN 2018-19)', 'BrO (SIPEXII)', 'Latitude ($^\circ$S)','Sea Ice Concentration (%)'], loc='upper left', bbox_to_anchor=(0.725, 0.25))
