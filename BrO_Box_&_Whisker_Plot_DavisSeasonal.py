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

#------------------------------------------------------------------------------
# Build a dataframe for the BrO BoxPlot

# Whole voyage
#data = [BrO_V1_17, BrO_V2_17, BrO_V3_17, BrO_V1_18, BrO_V2_18, BrO_V3_18, BrO_SIPEXII]

# While at station
data2 = [BrO_V1_17_D, BrO_V1_18_D, BrO_V2_17_C, BrO_V2_18_C, BrO_V3_17_M, BrO_V3_18_M, BrO_SIPEXII_I]

# Graph 3 data set-up
#example_data1 = [BrO_V1_17_Davis, BrO_V2_17_Casey, BrO_V3_17_Mawson]
#example_data2 = [BrO_V1_18_Davis, BrO_V2_18_Casey, BrO_V3_18_Mawson]
#example_data3 = [BrO_SIPEXII_Ice]

# Graph 4 data set-up
example_data1 = [BrO_V1_17_D, BrO_V1_18_D]
example_data2 = [BrO_V3_17_D, BrO_V3_18_D]

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

# # Mean for season
# Mean_2017    = np.mean(BrO_2017)
# Mean_2018    = np.mean(BrO_2018)
# Mean_All     = np.mean(BrO_All)
# Mean_All_SIP = np.mean(BrO_All_SIP)

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

# # StDev for season
# StDev_2017    = np.std(BrO_2017)
# StDev_2018    = np.std(BrO_2018)
# StDev_All     = np.std(BrO_All)
# StDev_All_SIP = np.std(BrO_All_SIP)

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

# # Median for season
# Median_2017    = np.median(BrO_2017)
# Median_2018    = np.median(BrO_2018)
# Median_All     = np.median(BrO_All)
# Median_All_SIP = np.median(BrO_All_SIP)

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

# # Median for season
# Mad_2017    = stats.median_abs_deviation(BrO_2017)
# Mad_2018    = stats.median_abs_deviation(BrO_2018)
# Mad_All     = stats.median_abs_deviation(BrO_All)
# Mad_All_SIP = stats.median_abs_deviation(BrO_All_SIP)

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

# # Median for season
# Min_2017    = np.min(BrO_2017)
# Min_2018    = np.min(BrO_2018)
# Min_All     = np.min(BrO_All)
# Min_All_SIP = np.min(BrO_All_SIP)

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

# # Median for season
# Max_2017    = np.max(BrO_2017)
# Max_2018    = np.max(BrO_2018)
# Max_All     = np.max(BrO_All)
# Max_All_SIP = np.max(BrO_All_SIP)

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

# # CAMMPCAN 2017-18
# N_2017 = len(BrO_2017)

# # CAMMPCAN 2018-19
# N_2018 = len(BrO_2018)

# # CAMMPCAN All (2017-18 & 2018-19)
# N_All = len(BrO_All)

DF1 = [N_V1_17, N_V1_18, N_V2_17, N_V2_18, N_V3_17M, N_V3_18M, N_V3_17D, N_V3_18D, N_SIPEXII]

#------------------------------------------------------------------------------
# PLOT THE GRAPH
#fig = plt.figure()
#plt.subplots_adjust(hspace=0.5)

# Graph 1
fig1, ax1 = plt.subplots()

# option 1, specify props dictionaries
c1 = "black"
c2 = "magenta"

box1 = ax1.boxplot(example_data1, positions=[1,3.5], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.75,0.75)
            )

# option 2, set all colors individually
c3 = "black"
c4 = "lawngreen"
box2 = ax1.boxplot(example_data2, positions=[2,4.5], notch=True, patch_artist=True,widths=(0.75,0.75))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box2[item], color=c3)
plt.setp(box2["boxes"], facecolor=c4)
plt.setp(box2["fliers"], markeredgecolor=c3)

plt.xlim(0.5,5)
plt.ylim(0,10)
#plt.xticks([1,1.5,2,2.5,3,3.5],['Davis V1\n(2017-18)','Davis V1\n(2018-19)','Casey V2\n(2017-18)','Casey V2\n(2018-19)','Mawson V3\n(2017-18)','Mawson V3\n(2018-19)'])
plt.xticks([1.5,4],['Davis (2017-18)','Davis (2018-19)'],fontsize=15)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
#ax1.set_title('BrO distributions for CAMMPCAN 2017-19 and SIPEXII',fontsize=20,y=1.02)
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
ax1.set_xlabel('Voyage', fontsize=20, labelpad=15)
lg = ax1.legend([box1["boxes"][0], box2["boxes"][0]], ['Spring', 'Summer'], loc='upper left',bbox_to_anchor=(0.13, 0.98),title='Season',fontsize=15)
lg.get_title().set_fontsize(15)
plt.show()