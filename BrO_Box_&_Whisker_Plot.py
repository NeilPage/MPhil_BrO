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
import statsmodels.api as sm 

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

#---------
# BrO
#---------
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv',index_col=0)       # BrO V1 (2017/18)
BrO_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv',index_col=0)       # BrO V2 (2017/18)
BrO_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv',index_col=0)       # BrO V3 (2017/18)

BrO_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv',index_col=0)       # BrO V1 (2018/19)
BrO_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv',index_col=0)       # BrO V2 (2018/19)
BrO_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv',index_col=0)       # BrO V3 (2018/19)

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
# Define the variables

#-----------------------------
# While at station (with ship exhaust)
#-----------------------------
# CAMMPCAN (2017-18)
BrO_V1_17_D = np.array(V1_17_BrO['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_V2_17_C = np.array(V2_17_BrO['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_V3_17_M = np.array(V3_17_BrOM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_V3_17_D = np.array(V3_17_BrOD['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

# CAMMPCAN (2018-19)
BrO_V1_18_D = np.array(V1_18_BrO['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_V2_18_C = np.array(V2_18_BrO['surf_vmr(ppmv)'])  * 1e6 # convert from ppmv to pptv
BrO_V3_18_M = np.array(V3_18_BrOM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_V3_18_D = np.array(V3_18_BrOD['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

# SIPEXII (2012)
BrO_SIPEXII_I = np.array(SIPEXII_BrO['surf_vmr(ppmv)'])* 1e6 # convert from ppmv to pptv

# Season
BrO_2017 = np.concatenate((BrO_V1_17_D, BrO_V2_17_C, BrO_V3_17_M, BrO_V3_17_D), axis = None)
BrO_2018 = np.concatenate((BrO_V1_18_D, BrO_V2_18_C, BrO_V3_18_M, BrO_V3_18_D), axis = None)

# Station
Davis_All  = np.concatenate((BrO_V1_17_D, BrO_V3_17_D, BrO_V1_18_D, BrO_V3_18_D), axis = None) 
Casey_All  = np.concatenate((BrO_V2_17_C, BrO_V2_18_C), axis = None)
Mawson_All = np.concatenate((BrO_V3_17_M, BrO_V3_18_M), axis = None)

# All
BrO_All     = np.concatenate((BrO_V1_17_D, BrO_V2_17_C, BrO_V3_17_M, BrO_V3_17_D, BrO_V1_18_D, BrO_V2_18_C, BrO_V3_18_M, BrO_V3_18_D), axis = None)
BrO_All_SIP = np.concatenate((BrO_V1_17_D, BrO_V2_17_C, BrO_V3_17_M, BrO_V3_17_D, BrO_V1_18_D, BrO_V2_18_C, BrO_V3_18_M, BrO_V3_18_D, BrO_SIPEXII_I), axis = None)

#------------------------------------------------------------------------------
# BrO VCD

# CAMMPCAN (2017-18)
VCD_V1_17_D = np.array(V1_17_BrO['BrO_VCD(molec/cm^2)'])
VCD_V2_17_C = np.array(V2_17_BrO['BrO_VCD(molec/cm^2)'])
VCD_V3_17_M = np.array(V3_17_BrOM['BrO_VCD(molec/cm^2)'])
VCD_V3_17_D = np.array(V3_17_BrOD['BrO_VCD(molec/cm^2)'])

# CAMMPCAN (2018-19)
VCD_V1_18_D = np.array(V1_18_BrO['BrO_VCD(molec/cm^2)'])
VCD_V2_18_C = np.array(V2_18_BrO['BrO_VCD(molec/cm^2)'])
VCD_V3_18_M = np.array(V3_18_BrOM['BrO_VCD(molec/cm^2)'])
VCD_V3_18_D = np.array(V3_18_BrOD['BrO_VCD(molec/cm^2)'])

# SIPEXII (2012)
VCD_SIPEXII_I = np.array(SIPEXII_BrO['BrO_VCD(molec/cm^2)'])

# All
BrO_VCD = np.concatenate((VCD_V1_17_D, VCD_V2_17_C, VCD_V3_17_M, VCD_V3_17_D, VCD_V1_18_D, VCD_V2_18_C, VCD_V3_18_M, VCD_V3_18_D), axis = None)

#------------------------------------------------------------------------------
# Build a dataframe for the BrO BoxPlot

# While at station
data2 = [BrO_V1_17_D, BrO_V1_18_D, BrO_V2_17_C, BrO_V2_18_C, BrO_V3_17_M, BrO_V3_18_M, BrO_SIPEXII_I]

# Graph 4 data set-up
example_data1 = [BrO_V1_17_D, BrO_V2_17_C, BrO_V3_17_M, BrO_V3_17_D]
example_data2 = [BrO_V1_18_D, BrO_V2_18_C, BrO_V3_18_M, BrO_V3_18_D]
example_data3 = [BrO_SIPEXII_I]

#------------------------------------------------------------------------------
# BrO while on station

#-----------------------------
# Calculate the mean
# 2017-18
Mean_V1_17  = np.mean(BrO_V1_17_D)
Mean_V2_17  = np.mean(BrO_V2_17_C)
Mean_V3_17M = np.mean(BrO_V3_17_M)
Mean_V3_17D = np.mean(BrO_V3_17_D)

# 2018-19
Mean_V1_18  = np.mean(BrO_V1_18_D)
Mean_V2_18  = np.mean(BrO_V2_18_C)
Mean_V3_18M = np.mean(BrO_V3_18_M)
Mean_V3_18D = np.mean(BrO_V3_18_D)

# 2012
Mean_SIPEXII = np.mean(BrO_SIPEXII_I)

# Mean for season
Mean_2017    = np.mean(BrO_2017)
Mean_2018    = np.mean(BrO_2018)
Mean_All     = np.mean(BrO_All)
Mean_All_SIP = np.mean(BrO_All_SIP)

#-----------------------------
# Calculate the VCD mean
# 2017-18
Mean_VCD_V1_17  = np.mean(VCD_V1_17_D)
Mean_VCD_V2_17  = np.mean(VCD_V2_17_C)
Mean_VCD_V3_17M = np.mean(VCD_V3_17_M)
Mean_VCD_V3_17D = np.mean(VCD_V3_17_D)

# 2018-19
Mean_VCD_V1_18  = np.mean(VCD_V1_18_D)
Mean_VCD_V2_18  = np.mean(VCD_V2_18_C)
Mean_VCD_V3_18M = np.mean(VCD_V3_18_M)
Mean_VCD_V3_18D = np.mean(VCD_V3_18_D)

# 2012
Mean_VCD_SIPEXII = np.mean(VCD_SIPEXII_I)

# All
Mean_VCD_All     = np.mean(BrO_VCD)

#-----------------------------
# Calculate the standard deviation
# 2017-18
StDev_V1_17  = np.std(BrO_V1_17_D)
StDev_V2_17  = np.std(BrO_V2_17_C)
StDev_V3_17M = np.std(BrO_V3_17_M)
StDev_V3_17D = np.std(BrO_V3_17_D)

# 2018-19
StDev_V1_18  = np.std(BrO_V1_18_D)
StDev_V2_18  = np.std(BrO_V2_18_C)
StDev_V3_18M = np.std(BrO_V3_18_M)
StDev_V3_18D = np.std(BrO_V3_18_D)

# 2012
StDev_SIPEXII = np.std(BrO_SIPEXII_I)

# StDev for season
StDev_2017    = np.std(BrO_2017)
StDev_2018    = np.std(BrO_2018)
StDev_All     = np.std(BrO_All)
StDev_All_SIP = np.std(BrO_All_SIP)

#-----------------------------
# Calculate the VCD standard deviation
# 2017-18
StDev_VCD_V1_17  = np.std(VCD_V1_17_D)
StDev_VCD_V2_17  = np.std(VCD_V2_17_C)
StDev_VCD_V3_17M = np.std(VCD_V3_17_M)
StDev_VCD_V3_17D = np.std(VCD_V3_17_D)

# 2018-19
StDev_VCD_V1_18  = np.std(VCD_V1_18_D)
StDev_VCD_V2_18  = np.std(VCD_V2_18_C)
StDev_VCD_V3_18M = np.std(VCD_V3_18_M)
StDev_VCD_V3_18D = np.std(VCD_V3_18_D)

# 2012
StDev_VCD_SIPEXII = np.std(VCD_SIPEXII_I)

# All
StDev_VCD_All     = np.std(BrO_VCD)

#-----------------------------
# Calculate the median
# 2017-18
Median_V1_17  = np.median(BrO_V1_17_D)
Median_V2_17  = np.median(BrO_V2_17_C)
Median_V3_17M = np.median(BrO_V3_17_M)
Median_V3_17D = np.median(BrO_V3_17_D)

# 2018-19
Median_V1_18  = np.median(BrO_V1_18_D)
Median_V2_18  = np.median(BrO_V2_18_C)
Median_V3_18M = np.median(BrO_V3_18_M)
Median_V3_18D = np.median(BrO_V3_18_D)

# 2012
Median_SIPEXII = np.median(BrO_SIPEXII_I)

# Median for season
Median_2017    = np.median(BrO_2017)
Median_2018    = np.median(BrO_2018)
Median_All     = np.median(BrO_All)
Median_All_SIP = np.median(BrO_All_SIP)

#-----------------------------
# Calculate the median absolute deviation
# 2017-18
Mad_V1_17  = stats.median_abs_deviation(BrO_V1_17_D)
Mad_V2_17  = stats.median_abs_deviation(BrO_V2_17_C)
Mad_V3_17M = stats.median_abs_deviation(BrO_V3_17_M)
Mad_V3_17D = stats.median_abs_deviation(BrO_V3_17_D)

# 2018-19
Mad_V1_18  = stats.median_abs_deviation(BrO_V1_18_D)
Mad_V2_18  = stats.median_abs_deviation(BrO_V2_18_C)
Mad_V3_18M = stats.median_abs_deviation(BrO_V3_18_M)
Mad_V3_18D = stats.median_abs_deviation(BrO_V3_18_D)

# 2012
Mad_SIPEXII = stats.median_abs_deviation(BrO_SIPEXII_I)

# Median for season
Mad_2017    = stats.median_abs_deviation(BrO_2017)
Mad_2018    = stats.median_abs_deviation(BrO_2018)
Mad_All     = stats.median_abs_deviation(BrO_All)
Mad_All_SIP = stats.median_abs_deviation(BrO_All_SIP)

#-----------------------------
# Calculate the minimum BrO concentration
# 2017-18
Min_V1_17  = np.min(BrO_V1_17_D)
Min_V2_17  = np.min(BrO_V2_17_C)
Min_V3_17M = np.min(BrO_V3_17_M)
Min_V3_17D = np.min(BrO_V3_17_D)

# 2018-19
Min_V1_18  = np.min(BrO_V1_18_D)
Min_V2_18  = np.min(BrO_V2_18_C)
Min_V3_18M = np.min(BrO_V3_18_M)
Min_V3_18D = np.min(BrO_V3_18_D)

# 2012
Min_SIPEXII = np.min(BrO_SIPEXII_I)

# Median for season
Min_2017    = np.min(BrO_2017)
Min_2018    = np.min(BrO_2018)
Min_All     = np.min(BrO_All)
Min_All_SIP = np.min(BrO_All_SIP)

#-----------------------------
# Calculate the maximum BrO concentration
# 2017-18
Max_V1_17  = np.max(BrO_V1_17_D)
Max_V2_17  = np.max(BrO_V2_17_C)
Max_V3_17M = np.max(BrO_V3_17_M)
Max_V3_17D = np.max(BrO_V3_17_D)

# 2018-19
Max_V1_18  = np.max(BrO_V1_18_D)
Max_V2_18  = np.max(BrO_V2_18_C)
Max_V3_18M = np.max(BrO_V3_18_M)
Max_V3_18D = np.max(BrO_V3_18_D)

# 2012
Max_SIPEXII = np.max(BrO_SIPEXII_I)

# Median for season
Max_2017    = np.max(BrO_2017)
Max_2018    = np.max(BrO_2018)
Max_All     = np.max(BrO_All)
Max_All_SIP = np.max(BrO_All_SIP)

#------------------------------------------------------------------------------
# Make a list of the number of values in each distribution

# text to include with label
j = 'n = '

# CAMMPCAN 2017-18
N_V1_17  = len(BrO_V1_17_D)
N_V2_17  = len(BrO_V2_17_C)
N_V3_17M = len(BrO_V3_17_M)
N_V3_17D = len(BrO_V3_17_D)

# CAMMPCAN 2018-19
N_V1_18  = len(BrO_V1_18_D)
N_V2_18  = len(BrO_V2_18_C)
N_V3_18M = len(BrO_V3_18_M)
N_V3_18D = len(BrO_V3_18_D)

# SIPPEX 2012
N_SIPEXII = len(BrO_SIPEXII_I)

# CAMMPCAN 2017-18
N_2017 = len(BrO_2017)

# CAMMPCAN 2018-19
N_2018 = len(BrO_2018)

# CAMMPCAN All (2017-18 & 2018-19)
N_All = len(BrO_All)

DF1 = [N_V1_17, N_V1_18, N_V2_17, N_V2_18, N_V3_17M, N_V3_18M, N_V3_17D, N_V3_18D, N_SIPEXII]

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE STATISTICAL RESULTS

# Build a pandas dataframe
dfBrO_Stats = {'No':[N_V1_17, N_V2_17, N_V3_17M, N_V3_17D,
                     N_2017,
                     N_V1_18, N_V2_18, N_V3_18M, N_V3_18D,
                     N_2018,
                     N_All,
                     N_SIPEXII],
               'Mean':[Mean_V1_17, Mean_V2_17, Mean_V3_17M, Mean_V3_17D,
                       Mean_2017,
                       Mean_V1_18, Mean_V2_18, Mean_V3_18M, Mean_V3_18D,
                       Mean_2018,
                       Mean_All,
                       Mean_SIPEXII],
               'StDev':[StDev_V1_17, StDev_V2_17, StDev_V3_17M, StDev_V3_17D,
                        StDev_2017,
                        StDev_V1_18, StDev_V2_18, StDev_V3_18M, StDev_V3_18D,
                        StDev_2018,
                        StDev_All,
                        StDev_SIPEXII],
               'Median':[Median_V1_17, Median_V2_17, Median_V3_17M, Median_V3_17D,
                         Median_2017,
                         Median_V1_18, Median_V2_18, Median_V3_18M, Median_V3_18D,
                         Median_2018,
                         Median_All,
                         Median_SIPEXII],
               'MAD':[Mad_V1_17, Mad_V2_17, Mad_V3_17M, Mad_V3_17D,
                      Mad_2017,
                      Mad_V1_18, Mad_V2_18, Mad_V3_18M, Mad_V3_18D,
                      Mad_2018,
                      Mad_All,
                      Mad_SIPEXII],
               'Min':[Min_V1_17, Min_V2_17, Min_V3_17M, Min_V3_17D,
                      Min_2017,
                      Min_V1_18, Min_V2_18, Min_V3_18M, Min_V3_18D,
                      Min_2018,
                      Min_All,
                      Min_SIPEXII],
               'Max':[Max_V1_17, Max_V2_17, Max_V3_17M, Max_V3_17D,
                      Max_2017,
                      Max_V1_18, Max_V2_18, Max_V3_18M, Max_V3_18D,
                      Max_2018,
                      Max_All,
                      Max_SIPEXII]}
dfBrO_Stats = pd.DataFrame(dfBrO_Stats, index = ['V1_17','V2_17','V3_17M','V3_17D','TOTAL_2017','V1_18','V2_18','V3_18M','V3_18D','TOTAL_2018','CAMMPCAN_All','SIPEXII'])

# Save the dataframe as .csv
#dfBrO_Stats.to_csv('/Users/ncp532/Documents/Data/BrO_Observations_Statistics.csv')
    
#------------------------------------------------------------------------------
# Welches T-Test on BrO 

# T-test for the means of 2 indpendent populations
# (Note: unequal sample sizes and/or variance, therefore Welches t-test)
# Interannual variability (2017-18 to 2018-19)
WT_stat_1,  WT_pval_1  = stats.ttest_ind(BrO_V1_17_D, BrO_V1_18_D, equal_var = False) # V1_17 & V1_18
WT_stat_2,  WT_pval_2  = stats.ttest_ind(BrO_V2_17_C, BrO_V2_18_C, equal_var = False) # V2_17 & V2_18
WT_stat_3,  WT_pval_3  = stats.ttest_ind(BrO_V3_17_M, BrO_V3_18_M, equal_var = False) # V3_17_M & V3_18_M
WT_stat_4,  WT_pval_4  = stats.ttest_ind(BrO_V3_17_D, BrO_V3_18_D, equal_var = False) # V3_17_D & V3_18_D

WT_stat_5,  WT_pval_5  = stats.ttest_ind(BrO_2017,    BrO_2018,    equal_var = False) # 2017-18 & 2018-19

# Variability (2017-18)
WT_stat_6,  WT_pval_6  = stats.ttest_ind(BrO_V1_17_D, BrO_V2_17_C, equal_var = False) # V1_17 & V2_17
WT_stat_7,  WT_pval_7  = stats.ttest_ind(BrO_V1_17_D, BrO_V3_17_M, equal_var = False) # V1_17 & M_17_M
WT_stat_8,  WT_pval_8  = stats.ttest_ind(BrO_V1_17_D, BrO_V3_17_D, equal_var = False) # V1_17 & V3_17_D
WT_stat_9,  WT_pval_9  = stats.ttest_ind(BrO_V2_17_C, BrO_V3_17_M, equal_var = False) # V2_17 & V3_17_M
WT_stat_10, WT_pval_10 = stats.ttest_ind(BrO_V2_17_C, BrO_V3_17_D, equal_var = False) # V2_17 & V3_17_D
WT_stat_11, WT_pval_11 = stats.ttest_ind(BrO_V3_17_M, BrO_V3_17_D, equal_var = False) # V3_17_M & V3_17_D

# Variability (2018-19)
WT_stat_12, WT_pval_12 = stats.ttest_ind(BrO_V1_18_D, BrO_V2_18_C, equal_var = False) # V1_18 & V2_18
WT_stat_13, WT_pval_13 = stats.ttest_ind(BrO_V1_18_D, BrO_V3_18_M, equal_var = False) # V1_18 & V3_18_M
WT_stat_14, WT_pval_14 = stats.ttest_ind(BrO_V1_18_D, BrO_V3_18_D, equal_var = False) # V1_18 & V3_18_D
WT_stat_15, WT_pval_15 = stats.ttest_ind(BrO_V2_18_C, BrO_V3_18_M, equal_var = False) # V2_18 & V3_18_M
WT_stat_16, WT_pval_16 = stats.ttest_ind(BrO_V2_18_C, BrO_V3_18_D, equal_var = False) # V2_18 & V3_18_D
WT_stat_17, WT_pval_17 = stats.ttest_ind(BrO_V3_17_M, BrO_V3_18_D, equal_var = False) # V3_18_M & V3_18_D

#------------------------------------------------------------------------------
# KS-Test on BrO (Kolmogorov-Smirnov Test)

# Interannual variability (2017-18 to 2018-19)
KS_stat_1,  KS_pval_1  = stats.ks_2samp(BrO_V1_17_D, BrO_V1_18_D, alternative='two-sided', mode='auto') # V1_17  & V1_18
KS_stat_2,  KS_pval_2  = stats.ks_2samp(BrO_V2_17_C, BrO_V2_18_C, alternative='two-sided', mode='auto') # V2_17  & V2_18
KS_stat_3,  KS_pval_3  = stats.ks_2samp(BrO_V3_17_M, BrO_V3_18_M, alternative='two-sided', mode='auto') # V3_17M & V3_18M
KS_stat_4,  KS_pval_4  = stats.ks_2samp(BrO_V3_17_D, BrO_V3_18_D, alternative='two-sided', mode='auto') # V1_17D & V3_18D

KS_stat_5,  KS_pval_5  = stats.ks_2samp(BrO_2017,    BrO_2018,    alternative='two-sided', mode='auto') # 2017-18 & 2018-19

# Variability (2017-18)
KS_stat_6,  KS_pval_6  = stats.ks_2samp(BrO_V1_17_D, BrO_V2_17_C, alternative='two-sided', mode='auto') # V1_17  & V2_17
KS_stat_7,  KS_pval_7  = stats.ks_2samp(BrO_V1_17_D, BrO_V3_17_M, alternative='two-sided', mode='auto') # V1_17  & V3_17M
KS_stat_8,  KS_pval_8  = stats.ks_2samp(BrO_V1_17_D, BrO_V3_17_D, alternative='two-sided', mode='auto') # V1_17  & V3_17D

KS_stat_9,  KS_pval_9  = stats.ks_2samp(BrO_V2_17_C, BrO_V3_17_M, alternative='two-sided', mode='auto') # V2_17  & V3_17M
KS_stat_10, KS_pval_10 = stats.ks_2samp(BrO_V2_17_C, BrO_V3_17_D, alternative='two-sided', mode='auto') # V2_17  & V3_17D

KS_stat_11, KS_pval_11 = stats.ks_2samp(BrO_V3_17_M, BrO_V3_17_D, alternative='two-sided', mode='auto') # V3_17M & V3_17D

# Variability (2018-19)
KS_stat_12, KS_pval_12 = stats.ks_2samp(BrO_V1_18_D, BrO_V2_18_C, alternative='two-sided', mode='auto') # V1_18  & V2_18
KS_stat_13, KS_pval_13 = stats.ks_2samp(BrO_V1_18_D, BrO_V3_18_M, alternative='two-sided', mode='auto') # V1_18  & V3_18M
KS_stat_14, KS_pval_14 = stats.ks_2samp(BrO_V1_18_D, BrO_V3_18_D, alternative='two-sided', mode='auto') # V1_18  & V3_18D

KS_stat_15, KS_pval_15 = stats.ks_2samp(BrO_V2_18_C, BrO_V3_18_M, alternative='two-sided', mode='auto') # V2_18  & V3_18M
KS_stat_16, KS_pval_16 = stats.ks_2samp(BrO_V2_18_C, BrO_V3_18_D, alternative='two-sided', mode='auto') # V2_18  & V3_18D

KS_stat_17, KS_pval_17 = stats.ks_2samp(BrO_V3_18_M, BrO_V3_18_D, alternative='two-sided', mode='auto') # V3_18M & V3_18D

#------------------------------------------------------------------------------
# MW (Mann-Whitney) U-Test on BrO

# Interannual variability (2017-18 to 2018-19)
MW_stat_1,  MW_pval_1  = stats.mannwhitneyu(BrO_V1_17_D, BrO_V1_18_D, alternative='two-sided') # V1_17  & V1_18
MW_stat_2,  MW_pval_2  = stats.mannwhitneyu(BrO_V2_17_C, BrO_V2_18_C, alternative='two-sided') # V2_17  & V2_18
MW_stat_3,  MW_pval_3  = stats.mannwhitneyu(BrO_V3_17_M, BrO_V3_18_M, alternative='two-sided') # V3_17M & V3_18M
MW_stat_4,  MW_pval_4  = stats.mannwhitneyu(BrO_V3_17_D, BrO_V3_18_D, alternative='two-sided') # V1_17D & V3_18D

MW_stat_5,  MW_pval_5  = stats.mannwhitneyu(BrO_2017,    BrO_2018,    alternative='two-sided') # 2017-18 & 2018-19

# Variability (2017-18)
MW_stat_6,  MW_pval_6  = stats.mannwhitneyu(BrO_V1_17_D, BrO_V2_17_C, alternative='two-sided') # V1_17  & V2_17
MW_stat_7,  MW_pval_7  = stats.mannwhitneyu(BrO_V1_17_D, BrO_V3_17_M, alternative='two-sided') # V1_17  & V3_17M
MW_stat_8,  MW_pval_8  = stats.mannwhitneyu(BrO_V1_17_D, BrO_V3_17_D, alternative='two-sided') # V1_17  & V3_17D

MW_stat_9,  MW_pval_9  = stats.mannwhitneyu(BrO_V2_17_C, BrO_V3_17_M, alternative='two-sided') # V2_17  & V3_17M
MW_stat_10, MW_pval_10 = stats.mannwhitneyu(BrO_V2_17_C, BrO_V3_17_D, alternative='two-sided') # V2_17  & V3_17D

MW_stat_11, MW_pval_11 = stats.mannwhitneyu(BrO_V3_17_M, BrO_V3_17_D, alternative='two-sided') # V3_17M & V3_17D

# Variability (2018-19)
MW_stat_12, MW_pval_12 = stats.mannwhitneyu(BrO_V1_18_D, BrO_V2_18_C, alternative='two-sided') # V1_18  & V2_18
MW_stat_13, MW_pval_13 = stats.mannwhitneyu(BrO_V1_18_D, BrO_V3_18_M, alternative='two-sided') # V1_18  & V3_18M
MW_stat_14, MW_pval_14 = stats.mannwhitneyu(BrO_V1_18_D, BrO_V3_18_D, alternative='two-sided') # V1_18  & V3_18D

MW_stat_15, MW_pval_15 = stats.mannwhitneyu(BrO_V2_18_C, BrO_V3_18_M, alternative='two-sided') # V2_18  & V3_18M
MW_stat_16, MW_pval_16 = stats.mannwhitneyu(BrO_V2_18_C, BrO_V3_18_D, alternative='two-sided') # V2_18  & V3_18D

MW_stat_17, MW_pval_17 = stats.mannwhitneyu(BrO_V3_18_M, BrO_V3_18_D, alternative='two-sided') # V3_18M & V3_18D

#------------------------------------------------------------------------------
# KW (Kruskal-Wallis) H-Test on BrO

# Interannual variability (2017-18 to 2018-19)
KW_stat_1,  KW_pval_1  = stats.kruskal(BrO_V1_17_D, BrO_V1_18_D) # V1_17  & V1_18
KW_stat_2,  KW_pval_2  = stats.kruskal(BrO_V2_17_C, BrO_V2_18_C) # V2_17  & V2_18
KW_stat_3,  KW_pval_3  = stats.kruskal(BrO_V3_17_M, BrO_V3_18_M) # V3_17M & V3_18M
KW_stat_4,  KW_pval_4  = stats.kruskal(BrO_V3_17_D, BrO_V3_18_D) # V1_17D & V3_18D

KW_stat_5,  KW_pval_5  = stats.kruskal(BrO_2017,    BrO_2018)    # 2017-18 & 2018-19

# Variability (2017-18)
KW_stat_6,  KW_pval_6  = stats.kruskal(BrO_V1_17_D, BrO_V2_17_C) # V1_17  & V2_17
KW_stat_7,  KW_pval_7  = stats.kruskal(BrO_V1_17_D, BrO_V3_17_M) # V1_17  & V3_17M
KW_stat_8,  KW_pval_8  = stats.kruskal(BrO_V1_17_D, BrO_V3_17_D) # V1_17  & V3_17D

KW_stat_9,  KW_pval_9  = stats.kruskal(BrO_V2_17_C, BrO_V3_17_M) # V2_17  & V3_17M
KW_stat_10, KW_pval_10 = stats.kruskal(BrO_V2_17_C, BrO_V3_17_D) # V2_17  & V3_17D

KW_stat_11, KW_pval_11 = stats.kruskal(BrO_V3_17_M, BrO_V3_17_D) # V3_17M & V3_17D

# Variability (2018-19)
KW_stat_12, KW_pval_12 = stats.kruskal(BrO_V1_18_D, BrO_V2_18_C) # V1_18  & V2_18
KW_stat_13, KW_pval_13 = stats.kruskal(BrO_V1_18_D, BrO_V3_18_M) # V1_18  & V3_18M
KW_stat_14, KW_pval_14 = stats.kruskal(BrO_V1_18_D, BrO_V3_18_D) # V1_18  & V3_18D

KW_stat_15, KW_pval_15 = stats.kruskal(BrO_V2_18_C, BrO_V3_18_M) # V2_18  & V3_18M
KW_stat_16, KW_pval_16 = stats.kruskal(BrO_V2_18_C, BrO_V3_18_D) # V2_18  & V3_18D

KW_stat_17, KW_pval_17 = stats.kruskal(BrO_V3_18_M, BrO_V3_18_D) # V3_18M & V3_18D

#------------------------------------------------------------------------------
#BUILD DATAFRAME FOR THE VARIABILITY RESULTS

# Build a pandas dataframe
dfBrO_Varia = {'Welches (stat)':[WT_stat_1,  WT_stat_2,  WT_stat_3, WT_stat_4,
                                 WT_stat_5,
                                 WT_stat_6,  WT_stat_7,  WT_stat_8,
                                 WT_stat_9,  WT_stat_10,
                                 WT_stat_11,
                                 WT_stat_12, WT_stat_13, WT_stat_14,
                                 WT_stat_15, WT_stat_16,
                                 WT_stat_17],
               'Welches (pval)':[WT_pval_1,  WT_pval_2,  WT_pval_3, WT_pval_4,
                                 WT_pval_5,
                                 WT_pval_6,  WT_pval_7,  WT_pval_8,
                                 WT_pval_9,  WT_pval_10,
                                 WT_pval_11,
                                 WT_pval_12, WT_pval_13, WT_pval_14,
                                 WT_pval_15, WT_pval_16,
                                 WT_pval_17],
               'KS-Test (stat)':[KS_stat_1,  KS_stat_2,  KS_stat_3, KS_stat_4,
                                 KS_stat_5,
                                 KS_stat_6,  KS_stat_7,  KS_stat_8,
                                 KS_stat_9,  KS_stat_10,
                                 KS_stat_11,
                                 KS_stat_12, KS_stat_13, KS_stat_14,
                                 KS_stat_15, KS_stat_16,
                                 KS_stat_17],
               'KS-Test (pval)':[KS_pval_1,  KS_pval_2,  KS_pval_3, KS_pval_4,
                                 KS_pval_5,
                                 KS_pval_6,  KS_pval_7,  KS_pval_8,
                                 KS_pval_9,  KS_pval_10,
                                 KS_pval_11,
                                 KS_pval_12, KS_pval_13, KS_pval_14,
                                 KS_pval_15, KS_pval_16,
                                 KS_pval_17],
               'MW U-Test (stat)':[MW_stat_1,  MW_stat_2,  MW_stat_3, MW_stat_4,
                                   MW_stat_5,
                                   MW_stat_6,  MW_stat_7,  MW_stat_8,
                                   MW_stat_9,  MW_stat_10,
                                   MW_stat_11,
                                   MW_stat_12, MW_stat_13, MW_stat_14,
                                   MW_stat_15, MW_stat_16,
                                   MW_stat_17],
               'MW U-Test (pval)':[MW_pval_1,  MW_pval_2,  MW_pval_3, MW_pval_4,
                                   MW_pval_5,
                                   MW_pval_6,  MW_pval_7,  MW_pval_8,
                                   MW_pval_9,  MW_pval_10,
                                   MW_pval_11,
                                   MW_pval_12, MW_pval_13, MW_pval_14,
                                   MW_pval_15, MW_pval_16,
                                   MW_pval_17],
               'KW H-Test (stat)':[KW_stat_1,  KW_stat_2,  KW_stat_3, KW_stat_4,
                                   KW_stat_5,
                                   KW_stat_6,  KW_stat_7,  KW_stat_8,
                                   KW_stat_9,  KW_stat_10,
                                   KW_stat_11,
                                   KW_stat_12, KW_stat_13, KW_stat_14,
                                   KW_stat_15, KW_stat_16,
                                   KW_stat_17],
               'KW H-Test (pval)':[KW_pval_1,  KW_pval_2,  KW_pval_3, KW_pval_4,
                                   KW_pval_5,
                                   KW_pval_6,  KW_pval_7,  KW_pval_8,
                                   KW_pval_9,  KW_pval_10,
                                   KW_pval_11,
                                   KW_pval_12, KW_pval_13, KW_pval_14,
                                   KW_pval_15, KW_pval_16,
                                   KW_pval_17]}
dfBrO_Varia = pd.DataFrame(dfBrO_Varia, index = ['V1_17 & V1_18','V2_17 & V2_18','V3_17M & V3_18M','V3_17D & V3_18D',
                                                 '2017_18 & 2018_19',
                                                 'V1_17 & V2_17','V1_17 & V3_17M','V1_17 & V3_17D',
                                                 'V2_17 & V3_17M','V2_17 & V3_17D',
                                                 'V3_17M & V3_17D',
                                                 'V1_18 & V2_18','V1_18 & V3_18M','V1_18 & V3_18D',
                                                 'V2_18 & V3_18M','V2_18 & V3_18D',
                                                 'V3_18M & V3_18D'])
dfBrO_Varia.to_csv('/Users/ncp532/Documents/Data/BrO_Variability.csv')

#------------------------------------------------------------------------------
# PLOT THE GRAPH

# Graph 1
fig1, ax1 = plt.subplots()

# option 1, specify props dictionaries
c1 = "black"
c2 = "blue"

box1 = ax1.boxplot(example_data1, positions=[1,2,3,4], bootstrap=None, notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25,0.25,0.25,0.25)
            )

# option 2, set all colors individually
c3 = "black"
c4 = "red"
box2 = ax1.boxplot(example_data2, positions=[1.5,2.5,3.5,4.5], bootstrap=None, notch=True, patch_artist=True,widths=(0.25,0.25,0.25,0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box2[item], color=c3)
plt.setp(box2["boxes"], facecolor=c4)
plt.setp(box2["fliers"], markeredgecolor=c3)

# option 2, set all colors individually
c5 = "black"
c6 = "green"
box3 = ax1.boxplot(example_data3, positions=[5], bootstrap=None, notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3[item], color=c5)
plt.setp(box3["boxes"], facecolor=c6)
plt.setp(box3["fliers"], markeredgecolor=c5)

for i, v in enumerate(DF1):
    ax1.text((i/2)+0.9 ,v/DF1[i]-0.7,j + str(DF1[i]),fontsize=12,color='black',fontweight='bold')
 
plt.xlim(0.5,5.5)
plt.ylim(0,8)
#plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
plt.xticks([1.25,2.25,3.25,4.25,5],['Davis (V1)','Casey (V2)','Mawson (V3)','Davis (V3)','SIPEXII'],fontsize=15)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
#ax1.set_title('BrO distributions for CAMMPCAN 2017-19 and SIPEXII',fontsize=20,y=1.02)
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
ax1.set_xlabel('Voyage', fontsize=20, labelpad=15)
lg = ax1.legend([box1["boxes"][0], box2["boxes"][0], box3["boxes"][0]], ['2017-18', '2018-19', '2012'], loc='upper left',bbox_to_anchor=(0.7, 0.98),title='Season',fontsize=15)
lg.get_title().set_fontsize(15)
plt.show()