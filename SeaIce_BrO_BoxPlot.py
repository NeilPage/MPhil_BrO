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
SI_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv', index_col=0)
SI_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv', index_col=0)
SI_V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv', index_col=0)

SI_V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv', index_col=0)
SI_V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv', index_col=0)
SI_V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv', index_col=0)
SI_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv', index_col=0)

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
SI_V3_17.index  = (pd.to_datetime(SI_V3_17.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

SI_V1_18.index  = (pd.to_datetime(SI_V1_18.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
SI_V2_18.index  = (pd.to_datetime(SI_V2_18.index,  dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
SI_V3_18.index  = (pd.to_datetime(SI_V3_18.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5

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
# CONVERT THE DATASETS TO 20-MINUTE TIME RESOLUTION

# SZA
SZA_V1_17T   = SZA_V1_17T.resample('20T',   offset='10T').mean()
SZA_V2_17T   = SZA_V2_17T.resample('20T',   offset='10T').mean()
SZA_V3_17T   = SZA_V3_17T.resample('20T',   offset='10T').mean()

SZA_V1_18T   = SZA_V1_18T.resample('20T',   offset='10T').mean()
SZA_V2_18T   = SZA_V2_18T.resample('20T',   offset='10T').mean()
SZA_V3_18T   = SZA_V3_18T.resample('20T',   offset='10T').mean()

SZA_SIPEXIIT = SZA_SIPEXIIT.resample('20T', offset='10T').mean()

# Sea Ice
SI_V1_17     = SI_V1_17.resample('20T',    offset='10T').mean()
SI_V2_17     = SI_V2_17.resample('20T',    offset='10T').mean()
SI_V3_17     = SI_V3_17.resample('20T',    offset='10T').mean()
SI_V1_18     = SI_V1_18.resample('20T',    offset='10T').mean()
SI_V2_18     = SI_V2_18.resample('20T',    offset='10T').mean()
SI_V3_18     = SI_V3_18.resample('20T',    offset='10T').mean()
SI_SIPEXII   = SI_SIPEXII.resample('20T',  offset='10T').mean()

# Met
Met_V1_17    = Met_V1_17.resample('20T',   offset='10T').mean()
Met_V2_17    = Met_V2_17.resample('20T',   offset='10T').mean()
Met_V3_17    = Met_V3_17.resample('20T',   offset='10T').mean()
Met_V1_18    = Met_V1_18.resample('20T',   offset='10T').mean()
Met_V2_18    = Met_V2_18.resample('20T',   offset='10T').mean()
Met_V3_18    = Met_V3_18.resample('20T',   offset='10T').mean()
Met_SIPEXII  = Met_SIPEXII.resample('20T', offset='10T').mean()

#------------------------------------------------------------------------------
# COMBINE DATAFRAMES

# BrO & SZA
BrO_SZA_V1_17   = pd.concat([BrO_V1_17T,   SZA_V1_17T],   axis=1, join='inner')
BrO_SZA_V2_17   = pd.concat([BrO_V2_17T,   SZA_V2_17T],   axis=1, join='inner')
BrO_SZA_V3_17   = pd.concat([BrO_V3_17T,   SZA_V3_17T],   axis=1, join='inner')

BrO_SZA_V1_18   = pd.concat([BrO_V1_18T,   SZA_V1_18T],   axis=1, join='inner')
BrO_SZA_V2_18   = pd.concat([BrO_V2_18T,   SZA_V2_18T],   axis=1, join='inner')
BrO_SZA_V3_18   = pd.concat([BrO_V3_18T,   SZA_V3_18T],   axis=1, join='inner')

BrO_SZA_SIPEXII = pd.concat([BrO_SIPEXIIT, SZA_SIPEXIIT], axis=1, join='inner')

# BrO & SeaIce
BrO_SZA_V1_17   = pd.concat([BrO_SZA_V1_17,   SI_V1_17],   axis=1, join='inner')
BrO_SZA_V2_17   = pd.concat([BrO_SZA_V2_17,   SI_V2_17],   axis=1, join='inner')
BrO_SZA_V3_17   = pd.concat([BrO_SZA_V3_17,   SI_V3_17],   axis=1, join='inner')

BrO_SZA_V1_18   = pd.concat([BrO_SZA_V1_18,   SI_V1_18],   axis=1, join='inner')
BrO_SZA_V2_18   = pd.concat([BrO_SZA_V2_18,   SI_V2_18],   axis=1, join='inner')
BrO_SZA_V3_18   = pd.concat([BrO_SZA_V3_18,   SI_V3_18],   axis=1, join='inner')

BrO_SZA_SIPEXII = pd.concat([BrO_SZA_SIPEXII, SI_SIPEXII], axis=1, join='inner')

# BrO & Met
BrO_SZA_V1_17   = pd.concat([BrO_SZA_V1_17,   Met_V1_17],   axis=1, join='inner')
BrO_SZA_V2_17   = pd.concat([BrO_SZA_V2_17,   Met_V2_17],   axis=1, join='inner')
BrO_SZA_V3_17   = pd.concat([BrO_SZA_V3_17,   Met_V3_17],   axis=1, join='inner')

BrO_SZA_V1_18   = pd.concat([BrO_SZA_V1_18,   Met_V1_18],   axis=1, join='inner')
BrO_SZA_V2_18   = pd.concat([BrO_SZA_V2_18,   Met_V2_18],   axis=1, join='inner')
BrO_SZA_V3_18   = pd.concat([BrO_SZA_V3_18,   Met_V3_18],   axis=1, join='inner')

BrO_SZA_SIPEXII = pd.concat([BrO_SZA_SIPEXII, Met_SIPEXII], axis=1, join='inner')

# # Drop nan values
# BrO_SZA_V1_17 = BrO_SZA_V1_17.dropna()
# BrO_SZA_V2_17 = BrO_SZA_V2_17.dropna()
# BrO_SZA_V3_17 = BrO_SZA_V3_17.dropna()

# BrO_SZA_V1_18 = BrO_SZA_V1_18.dropna()
# BrO_SZA_V2_18 = BrO_SZA_V2_18.dropna()
# BrO_SZA_V3_18 = BrO_SZA_V3_18.dropna()

# BrO_SZA_SIPEXII = BrO_SZA_SIPEXII.dropna()

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
# Calculate the Wind Speed average

WS_s_V1_17  = np.array(V1_17_BrO['wnd_spd_strbrd_corr_knot'])    * 0.514444444 # Convert from knots to m/s
WS_p_V1_17  = np.array(V1_17_BrO['wnd_spd_port_corr_knot'])      * 0.514444444 # Convert from knots to m/s
V1_17_BrO['WS_Avg'] = (WS_s_V1_17 + WS_p_V1_17)/2 # Average the wind speed for port and starboard

WS_s_V2_17  = np.array(V2_17_BrO['wnd_spd_strbrd_corr_knot'])    * 0.514444444 # Convert from knots to m/s
WS_p_V2_17  = np.array(V2_17_BrO['wnd_spd_port_corr_knot'])      * 0.514444444 # Convert from knots to m/s
V2_17_BrO['WS_Avg'] = (WS_s_V2_17 + WS_p_V2_17)/2 # Average the wind speed for port and starboard

WS_s_V3_17M = np.array(V3_17_BrOM['wnd_spd_strbrd_corr_knot'])   * 0.514444444 # Convert from knots to m/s
WS_p_V3_17M = np.array(V3_17_BrOM['wnd_spd_port_corr_knot'])     * 0.514444444 # Convert from knots to m/s
V3_17_BrOM['WS_Avg'] = (WS_s_V3_17M + WS_p_V3_17M)/2 # Average the wind speed for port and starboard

WS_s_V3_17D = np.array(V3_17_BrOD['wnd_spd_strbrd_corr_knot'])   * 0.514444444 # Convert from knots to m/s
WS_p_V3_17D = np.array(V3_17_BrOD['wnd_spd_port_corr_knot'])     * 0.514444444 # Convert from knots to m/s
V3_17_BrOD['WS_Avg'] = (WS_s_V3_17D + WS_p_V3_17D)/2 # Average the wind speed for port and starboard

WS_s_V1_18  = np.array(V1_18_BrO['wnd_spd_strbrd_corr_knot'])    * 0.514444444 # Convert from knots to m/s
WS_p_V1_18  = np.array(V1_18_BrO['wnd_spd_port_corr_knot'])      * 0.514444444 # Convert from knots to m/s
V1_18_BrO['WS_Avg'] = (WS_s_V1_18 + WS_p_V1_18)/2 # Average the wind speed for port and starboard

WS_s_V2_18  = np.array(V2_18_BrO['wnd_spd_strbrd_corr_knot'])    * 0.514444444 # Convert from knots to m/s
WS_p_V2_18  = np.array(V2_18_BrO['wnd_spd_port_corr_knot'])      * 0.514444444 # Convert from knots to m/s
V2_18_BrO['WS_Avg'] = (WS_s_V2_18 + WS_p_V2_18)/2 # Average the wind speed for port and starboard

WS_s_V3_18M = np.array(V3_18_BrOM['wnd_spd_strbrd_corr_knot'])   * 0.514444444 # Convert from knots to m/s
WS_p_V3_18M = np.array(V3_18_BrOM['wnd_spd_port_corr_knot'])     * 0.514444444 # Convert from knots to m/s
V3_18_BrOM['WS_Avg'] = (WS_s_V3_18M + WS_p_V3_18M)/2 # Average the wind speed for port and starboard

WS_s_V3_18D = np.array(V3_18_BrOD['wnd_spd_strbrd_corr_knot'])   * 0.514444444 # Convert from knots to m/s
WS_p_V3_18D = np.array(V3_18_BrOD['wnd_spd_port_corr_knot'])     * 0.514444444 # Convert from knots to m/s
V3_18_BrOD['WS_Avg'] = (WS_s_V3_18D + WS_p_V3_18D)/2 # Average the wind speed for port and starboard


WS_s_SIPEXII = np.array(SIPEXII_BrO['wnd_spd_strbrd_corr_knot']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXII = np.array(SIPEXII_BrO['wnd_spd_port_corr_knot'])   * 0.514444444 # Convert from knots to m/s
SIPEXII_BrO['WS_Avg'] = (WS_s_SIPEXII + WS_p_SIPEXII)/2 # Average the wind speed for port and starboard

#------------------------------------------------------------------------------
# Seperate the data into low (<=7 m/s) and high (>7 m/s) wind speeds

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------
V1_17_LWS   = (V1_17_BrO['WS_Avg']   <= 7)
D1_V1_17L   = V1_17_BrO[V1_17_LWS]

V2_17_LWS   = (V2_17_BrO['WS_Avg']   <= 7)
D1_V2_17L   = V2_17_BrO[V2_17_LWS]

V3_17M_LWS  = (V3_17_BrOM['WS_Avg']  <= 7)
D1_V3_17ML  = V3_17_BrOM[V3_17M_LWS]

V3_17D_LWS  = (V3_17_BrOD['WS_Avg']  <= 7)
D1_V3_17DL  = V3_17_BrOD[V3_17D_LWS]

V1_18_LWS   = (V1_18_BrO['WS_Avg']   <= 7)
D1_V1_18L   = V1_18_BrO[V1_18_LWS]

V2_18_LWS   = (V2_18_BrO['WS_Avg']   <= 7)
D1_V2_18L   = V2_18_BrO[V2_18_LWS]

V3_18M_LWS  = (V3_18_BrOM['WS_Avg']  <= 7)
D1_V3_18ML  = V3_18_BrOM[V3_18M_LWS]

V3_18D_LWS  = (V3_18_BrOD['WS_Avg']  <= 7)
D1_V3_18DL  = V3_18_BrOD[V3_18D_LWS]

SIPEXII_LWS = (SIPEXII_BrO['WS_Avg'] <= 7)
D1_SIPEXIIL = SIPEXII_BrO[SIPEXII_LWS]

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------
V1_17_HWS   = (V1_17_BrO['WS_Avg']   > 7)
D1_V1_17H   = V1_17_BrO[V1_17_HWS]

V2_17_HWS   = (V2_17_BrO['WS_Avg']   > 7)
D1_V2_17H   = V2_17_BrO[V2_17_HWS]

V3_17M_HWS  = (V3_17_BrOM['WS_Avg']  > 7)
D1_V3_17MH  = V3_17_BrOM[V3_17M_HWS]

V3_17D_HWS  = (V3_17_BrOD['WS_Avg']  > 7)
D1_V3_17DH  = V3_17_BrOD[V3_17D_HWS]

V1_18_HWS   = (V1_18_BrO['WS_Avg']   > 7)
D1_V1_18H   = V1_18_BrO[V1_18_HWS]

V2_18_HWS   = (V2_18_BrO['WS_Avg']   > 7)
D1_V2_18H   = V2_18_BrO[V2_18_HWS]

V3_18M_HWS  = (V3_18_BrOM['WS_Avg']  > 7)
D1_V3_18MH  = V3_18_BrOM[V3_18M_HWS]

V3_18D_HWS  = (V3_18_BrOD['WS_Avg']  > 7)
D1_V3_18DH  = V3_18_BrOD[V3_18D_HWS]

SIPEXII_HWS = (SIPEXII_BrO['WS_Avg'] > 7)
D1_SIPEXIIH = SIPEXII_BrO[SIPEXII_HWS]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover is 0%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17_F1L   = (D1_V1_17L['Sea_Ice_Conc']   == 0)
V1_17_ZL    = D1_V1_17L[V1_17_F1L]

V2_17_F1L   = (D1_V2_17L['Sea_Ice_Conc']   == 0)
V2_17_ZL    = D1_V2_17L[V2_17_F1L]

V3_17M_F1L  = (D1_V3_17ML['Sea_Ice_Conc']  == 0)
V3_17M_ZL   = D1_V3_17ML[V3_17M_F1L]

V3_17D_F1L  = (D1_V3_17DL['Sea_Ice_Conc']  == 0)
V3_17D_ZL   = D1_V3_17DL[V3_17D_F1L]

V1_18_F1L   = (D1_V1_18L['Sea_Ice_Conc']   == 0)
V1_18_ZL    = D1_V1_18L[V1_18_F1L]

V2_18_F1L   = (D1_V2_18L['Sea_Ice_Conc']   == 0)
V2_18_ZL    = D1_V2_18L[V2_18_F1L]

V3_18M_F1L  = (D1_V3_18ML['Sea_Ice_Conc']  == 0)
V3_18M_ZL   = D1_V3_18ML[V3_18M_F1L]

V3_18D_F1L  = (D1_V3_18DL['Sea_Ice_Conc']  == 0)
V3_18D_ZL   = D1_V3_18DL[V3_18D_F1L]

SIPEXII_F1L = (D1_SIPEXIIL['Sea_Ice_Conc'] == 0)
SIPEXII_ZL  = D1_SIPEXIIL[SIPEXII_F1L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17_F1H   = (D1_V1_17H['Sea_Ice_Conc']   == 0)
V1_17_ZH    = D1_V1_17H[V1_17_F1H]

V2_17_F1H   = (D1_V2_17H['Sea_Ice_Conc']   == 0)
V2_17_ZH    = D1_V2_17H[V2_17_F1H]

V3_17M_F1H  = (D1_V3_17MH['Sea_Ice_Conc']  == 0)
V3_17M_ZH   = D1_V3_17MH[V3_17M_F1H]

V3_17D_F1H  = (D1_V3_17DH['Sea_Ice_Conc']  == 0)
V3_17D_ZH   = D1_V3_17DH[V3_17D_F1H]

V1_18_F1H   = (D1_V1_18H['Sea_Ice_Conc']   == 0)
V1_18_ZH    = D1_V1_18H[V1_18_F1H]

V2_18_F1H   = (D1_V2_18H['Sea_Ice_Conc']   == 0)
V2_18_ZH    = D1_V2_18H[V2_18_F1H]

V3_18M_F1H  = (D1_V3_18MH['Sea_Ice_Conc']  == 0)
V3_18M_ZH   = D1_V3_18MH[V3_18M_F1H]

V3_18D_F1H  = (D1_V3_18DH['Sea_Ice_Conc']  == 0)
V3_18D_ZH   = D1_V3_18DH[V3_18D_F1H]

SIPEXII_F1H = (D1_SIPEXIIH['Sea_Ice_Conc'] == 0)
SIPEXII_ZH  = D1_SIPEXIIH[SIPEXII_F1H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover is 100%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17_F2L   = (D1_V1_17L['Sea_Ice_Conc'] >= 0.9)   & (D1_V1_17L['Sea_Ice_Conc']   <= 1.0)
V1_17_AL    = D1_V1_17L[V1_17_F2L]

V2_17_F2L   = (D1_V2_17L['Sea_Ice_Conc'] >= 0.9)   & (D1_V2_17L['Sea_Ice_Conc']   <= 1.0)
V2_17_AL    = D1_V2_17L[V2_17_F2L]

V3_17M_F2L  = (D1_V3_17ML['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_17ML['Sea_Ice_Conc']  <= 1.0)
V3_17M_AL   = D1_V3_17ML[V3_17M_F2L]

V3_17D_F2L  = (D1_V3_17DL['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_17DL['Sea_Ice_Conc']  <= 1.0)
V3_17D_AL   = D1_V3_17DL[V3_17D_F2L]

V1_18_F2L   = (D1_V1_18L['Sea_Ice_Conc'] >= 0.9)   & (D1_V1_18L['Sea_Ice_Conc']   <= 1.0)
V1_18_AL    = D1_V1_18L[V1_18_F2L]

V2_18_F2L   = (D1_V2_18L['Sea_Ice_Conc'] >= 0.9)   & (D1_V2_18L['Sea_Ice_Conc']   <= 1.0)
V2_18_AL    = D1_V2_18L[V2_18_F2L]

V3_18M_F2L  = (D1_V3_18ML['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_18ML['Sea_Ice_Conc']  <= 1.0)
V3_18M_AL   = D1_V3_18ML[V3_18M_F2L]

V3_18D_F2L  = (D1_V3_18DL['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_18DL['Sea_Ice_Conc']  <= 1.0)
V3_18D_AL   = D1_V3_18DL[V3_18D_F2L]

SIPEXII_F2L = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.9) & (D1_SIPEXIIL['Sea_Ice_Conc'] <= 1.0)
SIPEXII_AL  = D1_SIPEXIIL[SIPEXII_F2L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17_F2H   = (D1_V1_17H['Sea_Ice_Conc'] >= 0.9)   & (D1_V1_17H['Sea_Ice_Conc']   <= 1.0)
V1_17_AH    = D1_V1_17H[V1_17_F2H]

V2_17_F2H   = (D1_V2_17H['Sea_Ice_Conc'] >= 0.9)   & (D1_V2_17H['Sea_Ice_Conc']   <= 1.0)
V2_17_AH    = D1_V2_17H[V2_17_F2H]

V3_17M_F2H  = (D1_V3_17MH['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_17MH['Sea_Ice_Conc']  <= 1.0)
V3_17M_AH   = D1_V3_17MH[V3_17M_F2H]

V3_17D_F2H  = (D1_V3_17DH['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_17DH['Sea_Ice_Conc']  <= 1.0)
V3_17D_AH   = D1_V3_17DH[V3_17D_F2H]

V1_18_F2H   = (D1_V1_18H['Sea_Ice_Conc'] >= 0.9)   & (D1_V1_18H['Sea_Ice_Conc']   <= 1.0)
V1_18_AH    = D1_V1_18H[V1_18_F2H]

V2_18_F2H   = (D1_V2_18H['Sea_Ice_Conc'] >= 0.9)   & (D1_V2_18H['Sea_Ice_Conc']   <= 1.0)
V2_18_AH    = D1_V2_18H[V2_18_F2H]

V3_18M_F2H  = (D1_V3_18MH['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_18MH['Sea_Ice_Conc']  <= 1.0)
V3_18M_AH   = D1_V3_18MH[V3_18M_F2H]

V3_18D_F2H  = (D1_V3_18DH['Sea_Ice_Conc'] >= 0.9)  & (D1_V3_18DH['Sea_Ice_Conc']  <= 1.0)
V3_18D_AH   = D1_V3_18DH[V3_18D_F2H]

SIPEXII_F2H = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.9) & (D1_SIPEXIIH['Sea_Ice_Conc'] <= 1.0)
SIPEXII_AH  = D1_SIPEXIIH[SIPEXII_F2H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover is between 1-30%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17_F3L   = (D1_V1_17L['Sea_Ice_Conc'] >= 0.01)   & (D1_V1_17L['Sea_Ice_Conc']   < 0.3)
V1_17_P1L   = D1_V1_17L[V1_17_F3L]

V2_17_F3L   = (D1_V2_17L['Sea_Ice_Conc'] >= 0.01)   & (D1_V2_17L['Sea_Ice_Conc']   < 0.3)
V2_17_P1L   = D1_V2_17L[V2_17_F3L]

V3_17M_F3L  = (D1_V3_17ML['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_17ML['Sea_Ice_Conc']  < 0.3)
V3_17M_P1L  = D1_V3_17ML[V3_17M_F3L]

V3_17D_F3L  = (D1_V3_17DL['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_17DL['Sea_Ice_Conc']  < 0.3)
V3_17D_P1L  = D1_V3_17DL[V3_17D_F3L]

V1_18_F3L   = (D1_V1_18L['Sea_Ice_Conc'] >= 0.01)   & (D1_V1_18L['Sea_Ice_Conc']   < 0.3)
V1_18_P1L   = D1_V1_18L[V1_18_F3L]

V2_18_F3L   = (D1_V2_18L['Sea_Ice_Conc'] >= 0.01)   & (D1_V2_18L['Sea_Ice_Conc']   < 0.3)
V2_18_P1L   = D1_V2_18L[V2_18_F3L]

V3_18M_F3L  = (D1_V3_18ML['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_18ML['Sea_Ice_Conc']  < 0.3)
V3_18M_P1L  = D1_V3_18ML[V3_18M_F3L]

V3_18D_F3L  = (D1_V3_18DL['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_18DL['Sea_Ice_Conc']  < 0.3)
V3_18D_P1L  = D1_V3_18DL[V3_18D_F3L]

SIPEXII_F3L = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.01) & (D1_SIPEXIIL['Sea_Ice_Conc'] < 0.3)
SIPEXII_P1L = D1_SIPEXIIL[SIPEXII_F3L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17_F3H   = (D1_V1_17H['Sea_Ice_Conc'] >= 0.01)   & (D1_V1_17H['Sea_Ice_Conc']   < 0.3)
V1_17_P1H   = D1_V1_17H[V1_17_F3H]

V2_17_F3H   = (D1_V2_17H['Sea_Ice_Conc'] >= 0.01)   & (D1_V2_17H['Sea_Ice_Conc']   < 0.3)
V2_17_P1H   = D1_V2_17H[V2_17_F3H]

V3_17M_F3H  = (D1_V3_17MH['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_17MH['Sea_Ice_Conc']  < 0.3)
V3_17M_P1H  = D1_V3_17MH[V3_17M_F3H]

V3_17D_F3H  = (D1_V3_17DH['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_17DH['Sea_Ice_Conc']  < 0.3)
V3_17D_P1H  = D1_V3_17DH[V3_17D_F3H]

V1_18_F3H   = (D1_V1_18H['Sea_Ice_Conc'] >= 0.01)   & (D1_V1_18H['Sea_Ice_Conc']   < 0.3)
V1_18_P1H   = D1_V1_18H[V1_18_F3H]

V2_18_F3H   = (D1_V2_18H['Sea_Ice_Conc'] >= 0.01)   & (D1_V2_18H['Sea_Ice_Conc']   < 0.3)
V2_18_P1H   = D1_V2_18H[V2_18_F3H]

V3_18M_F3H  = (D1_V3_18MH['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_18MH['Sea_Ice_Conc']  < 0.3)
V3_18M_P1H  = D1_V3_18MH[V3_18M_F3H]

V3_18D_F3H  = (D1_V3_18DH['Sea_Ice_Conc'] >= 0.01)  & (D1_V3_18DH['Sea_Ice_Conc']  < 0.3)
V3_18D_P1H  = D1_V3_18DH[V3_18D_F3H]

SIPEXII_F3H = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.01) & (D1_SIPEXIIH['Sea_Ice_Conc'] < 0.3)
SIPEXII_P1H = D1_SIPEXIIH[SIPEXII_F3H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover between 30-60%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17_F4L   = (D1_V1_17L['Sea_Ice_Conc'] >= 0.3)   & (D1_V1_17L['Sea_Ice_Conc']   < 0.6)
V1_17_P2L   = D1_V1_17L[V1_17_F4L]

V2_17_F4L   = (D1_V2_17L['Sea_Ice_Conc'] >= 0.3)   & (D1_V2_17L['Sea_Ice_Conc']   < 0.6)
V2_17_P2L   = D1_V2_17L[V2_17_F4L]

V3_17M_F4L  = (D1_V3_17ML['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_17ML['Sea_Ice_Conc']  < 0.6)
V3_17M_P2L  = D1_V3_17ML[V3_17M_F4L]

V3_17D_F4L  = (D1_V3_17DL['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_17DL['Sea_Ice_Conc']  < 0.6)
V3_17D_P2L  = D1_V3_17DL[V3_17D_F4L]

V1_18_F4L   = (D1_V1_18L['Sea_Ice_Conc'] >= 0.3)   & (D1_V1_18L['Sea_Ice_Conc']   < 0.6)
V1_18_P2L   = D1_V1_18L[V1_18_F4L]

V2_18_F4L   = (D1_V2_18L['Sea_Ice_Conc'] >= 0.3)   & (D1_V2_18L['Sea_Ice_Conc']   < 0.6)
V2_18_P2L   = D1_V2_18L[V2_18_F4L]

V3_18M_F4L  = (D1_V3_18ML['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_18ML['Sea_Ice_Conc']  < 0.6)
V3_18M_P2L  = D1_V3_18ML[V3_18M_F4L]

V3_18D_F4L  = (D1_V3_18DL['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_18DL['Sea_Ice_Conc']  < 0.6)
V3_18D_P2L  = D1_V3_18DL[V3_18D_F4L]

SIPEXII_F4L = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.3) & (D1_SIPEXIIL['Sea_Ice_Conc'] < 0.6)
SIPEXII_P2L = D1_SIPEXIIL[SIPEXII_F4L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17_F4H   = (D1_V1_17H['Sea_Ice_Conc'] >= 0.3)   & (D1_V1_17H['Sea_Ice_Conc']   < 0.6)
V1_17_P2H   = D1_V1_17H[V1_17_F4H]

V2_17_F4H   = (D1_V2_17H['Sea_Ice_Conc'] >= 0.3)   & (D1_V2_17H['Sea_Ice_Conc']   < 0.6)
V2_17_P2H   = D1_V2_17H[V2_17_F4H]

V3_17M_F4H  = (D1_V3_17MH['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_17MH['Sea_Ice_Conc']  < 0.6)
V3_17M_P2H  = D1_V3_17MH[V3_17M_F4H]

V3_17D_F4H  = (D1_V3_17DH['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_17DH['Sea_Ice_Conc']  < 0.6)
V3_17D_P2H  = D1_V3_17DH[V3_17D_F4H]

V1_18_F4H   = (D1_V1_18H['Sea_Ice_Conc'] >= 0.3)   & (D1_V1_18H['Sea_Ice_Conc']   < 0.6)
V1_18_P2H   = D1_V1_18H[V1_18_F4H]

V2_18_F4H   = (D1_V2_18H['Sea_Ice_Conc'] >= 0.3)   & (D1_V2_18H['Sea_Ice_Conc']   < 0.6)
V2_18_P2H   = D1_V2_18H[V2_18_F4H]

V3_18M_F4H  = (D1_V3_18MH['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_18MH['Sea_Ice_Conc']  < 0.6)
V3_18M_P2H  = D1_V3_18MH[V3_18M_F4H]

V3_18D_F4H  = (D1_V3_18DH['Sea_Ice_Conc'] >= 0.3)  & (D1_V3_18DH['Sea_Ice_Conc']  < 0.6)
V3_18D_P2H  = D1_V3_18DH[V3_18D_F4H]

SIPEXII_F4H = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.3) & (D1_SIPEXIIH['Sea_Ice_Conc'] < 0.6)
SIPEXII_P2H = D1_SIPEXIIH[SIPEXII_F4H]

#------------------------------------------------------------------------------
# Filter dataframe for when sea ice cover between 60-90%

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
V1_17_F5L   = (D1_V1_17L['Sea_Ice_Conc'] >= 0.6)   & (D1_V1_17L['Sea_Ice_Conc']   < 0.9)
V1_17_P3L   = D1_V1_17L[V1_17_F5L]

V2_17_F5L   = (D1_V2_17L['Sea_Ice_Conc'] >= 0.6)   & (D1_V2_17L['Sea_Ice_Conc']   < 0.9)
V2_17_P3L   = D1_V2_17L[V2_17_F5L]

V3_17M_F5L  = (D1_V3_17ML['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_17ML['Sea_Ice_Conc']  < 0.9)
V3_17M_P3L  = D1_V3_17ML[V3_17M_F5L]

V3_17D_F5L  = (D1_V3_17DL['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_17DL['Sea_Ice_Conc']  < 0.9)
V3_17D_P3L  = D1_V3_17DL[V3_17D_F5L]

V1_18_F5L   = (D1_V1_18L['Sea_Ice_Conc'] >= 0.6)   & (D1_V1_18L['Sea_Ice_Conc']   < 0.9)
V1_18_P3L   = D1_V1_18L[V1_18_F5L]

V2_18_F5L   = (D1_V2_18L['Sea_Ice_Conc'] >= 0.6)   & (D1_V2_18L['Sea_Ice_Conc']   < 0.9)
V2_18_P3L   = D1_V2_18L[V2_18_F5L]

V3_18M_F5L  = (D1_V3_18ML['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_18ML['Sea_Ice_Conc']  < 0.9)
V3_18M_P3L  = D1_V3_18ML[V3_18M_F5L]

V3_18D_F5L  = (D1_V3_18DL['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_18DL['Sea_Ice_Conc']  < 0.9)
V3_18D_P3L  = D1_V3_18DL[V3_18D_F5L]

SIPEXII_F5L = (D1_SIPEXIIL['Sea_Ice_Conc'] >= 0.6) & (D1_SIPEXIIL['Sea_Ice_Conc'] < 0.9)
SIPEXII_P3L = D1_SIPEXIIL[SIPEXII_F5L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
V1_17_F5H   = (D1_V1_17H['Sea_Ice_Conc'] >= 0.6)   & (D1_V1_17H['Sea_Ice_Conc']   < 0.9)
V1_17_P3H   = D1_V1_17H[V1_17_F5H]

V2_17_F5H   = (D1_V2_17H['Sea_Ice_Conc'] >= 0.6)   & (D1_V2_17H['Sea_Ice_Conc']   < 0.9)
V2_17_P3H   = D1_V2_17H[V2_17_F5H]

V3_17M_F5H  = (D1_V3_17MH['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_17MH['Sea_Ice_Conc']  < 0.9)
V3_17M_P3H  = D1_V3_17MH[V3_17M_F5H]

V3_17D_F5H  = (D1_V3_17DH['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_17DH['Sea_Ice_Conc']  < 0.9)
V3_17D_P3H  = D1_V3_17DH[V3_17D_F5H]

V1_18_F5H   = (D1_V1_18H['Sea_Ice_Conc'] >= 0.6)   & (D1_V1_18H['Sea_Ice_Conc']   < 0.9)
V1_18_P3H   = D1_V1_18H[V1_18_F5H]

V2_18_F5H   = (D1_V2_18H['Sea_Ice_Conc'] >= 0.6)   & (D1_V2_18H['Sea_Ice_Conc']   < 0.9)
V2_18_P3H   = D1_V2_18H[V2_18_F5H]

V3_18M_F5H  = (D1_V3_18MH['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_18MH['Sea_Ice_Conc']  < 0.9)
V3_18M_P3H  = D1_V3_18MH[V3_18M_F5H]

V3_18D_F5H  = (D1_V3_18DH['Sea_Ice_Conc'] >= 0.6)  & (D1_V3_18DH['Sea_Ice_Conc']  < 0.9)
V3_18D_P3H  = D1_V3_18DH[V3_18D_F5H]

SIPEXII_F5H = (D1_SIPEXIIH['Sea_Ice_Conc'] >= 0.6) & (D1_SIPEXIIH['Sea_Ice_Conc'] < 0.9)
SIPEXII_P3H = D1_SIPEXIIH[SIPEXII_F5H]

#------------------------------------------------------------------------------
# Concate the filtered dataframes

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
# Sea ice cover is 0%
zeroL     = pd.concat([V1_17_ZL,  V2_17_ZL,  V3_17M_ZL,  V3_17D_ZL,  V1_18_ZL,  V2_18_ZL,  V3_18M_ZL,  V3_18D_ZL])#,   SIPEXII_ZL])

# Sea ice cover is between 1-30%
partial1L = pd.concat([V1_17_P1L, V2_17_P1L, V3_17M_P1L, V3_17D_P1L, V1_18_P1L, V2_18_P1L, V3_18M_P1L, V3_18D_P1L,])#, SIPEXII_P1L])

# Sea ice cover is between 30-60%
partial2L = pd.concat([V1_17_P2L, V2_17_P2L, V3_17M_P2L, V3_17D_P2L, V1_18_P2L, V2_18_P2L, V3_18M_P2L, V3_18D_P2L,])#, SIPEXII_P2L])

# Sea ice cover is between 60-90%
partial3L = pd.concat([V1_17_P3L, V2_17_P3L, V3_17M_P3L, V3_17D_P3L, V1_18_P3L, V2_18_P3L, V3_18M_P3L, V3_18D_P3L,])#, SIPEXII_P3L])

# Sea ice cover is 100%
fullL     = pd.concat([V1_17_AL,  V2_17_AL,  V3_17M_AL,  V3_17D_AL,  V1_18_AL,  V2_18_AL,  V3_18M_AL,  V3_18D_AL])#,   SIPEXIIVAL])

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
# Sea ice cover is 0%
zeroH     = pd.concat([V1_17_ZH,  V2_17_ZH,  V3_17M_ZH,  V3_17D_ZH,  V1_18_ZH,  V2_18_ZH,  V3_18M_ZH,  V3_18D_ZH])#,  SIPEXIIZH])

# Sea ice cover is between 1-30%
partial1H = pd.concat([V1_17_P1H, V2_17_P1H, V3_17M_P1H, V3_17D_P1H, V1_18_P1H, V2_18_P1H, V3_18M_P1H, V3_18D_P1H])#, SIPEXIIP1H])

# Sea ice cover is between 30-60%
partial2H = pd.concat([V1_17_P2H, V2_17_P2H, V3_17M_P2H, V3_17D_P2H, V1_18_P2H, V2_18_P2H, V3_18M_P2H, V3_18D_P2H])#, SIPEXIIP2H])

# Sea ice cover is between 60-90%
partial3H = pd.concat([V1_17_P3H, V2_17_P3H, V3_17M_P3H, V3_17D_P3H, V1_18_P3H, V2_18_P3H, V3_18M_P3H, V3_18D_P3H])#, SIPEXIIP3H])

# Sea ice cover is 100%
fullH     = pd.concat([V1_17_AH,  V2_17_AH,  V3_17M_AH,  V3_17D_AH,  V1_18_AH,  V2_18_AH,  V3_18M_AH,  V3_18D_AH])#,  SIPEXIIAH])

#------------------------------------------------------------------------------
# Calculate the Mean

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
meanZL  = np.mean((zeroL['surf_vmr(ppmv)'])     * 1e6)
meanP1L = np.mean((partial1L['surf_vmr(ppmv)']) * 1e6)
meanP2L = np.mean((partial2L['surf_vmr(ppmv)']) * 1e6)
meanP3L = np.mean((partial3L['surf_vmr(ppmv)']) * 1e6)
meanAL  = np.mean((fullL['surf_vmr(ppmv)'])     * 1e6)

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
meanZH  = np.mean((zeroH['surf_vmr(ppmv)'])     * 1e6)
meanP1H = np.mean((partial1H['surf_vmr(ppmv)']) * 1e6)
meanP2H = np.mean((partial2H['surf_vmr(ppmv)']) * 1e6)
meanP3H = np.mean((partial3H['surf_vmr(ppmv)']) * 1e6)
meanAH  = np.mean((fullH['surf_vmr(ppmv)'])     * 1e6)

#------------------------------------------------------------------------------
# Calculate the Standard deviation

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
stdevZL  = np.std((zeroL['surf_vmr(ppmv)'])     * 1e6)
stdevP1L = np.std((partial1L['surf_vmr(ppmv)']) * 1e6)
stdevP2L = np.std((partial2L['surf_vmr(ppmv)']) * 1e6)
stdevP3L = np.std((partial3L['surf_vmr(ppmv)']) * 1e6)
stdevAL  = np.std((fullL['surf_vmr(ppmv)'])     * 1e6)

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
stdevZH  = np.std((zeroH['surf_vmr(ppmv)'])     * 1e6)
stdevP1H = np.std((partial1H['surf_vmr(ppmv)']) * 1e6)
stdevP2H = np.std((partial2H['surf_vmr(ppmv)']) * 1e6)
stdevP3H = np.std((partial3H['surf_vmr(ppmv)']) * 1e6)
stdevAH  = np.std((fullH['surf_vmr(ppmv)'])     * 1e6)

#------------------------------------------------------------------------------
# Calculate the Median

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
medianZL  = np.median((zeroL['surf_vmr(ppmv)'])     * 1e6)
medianP1L = np.median((partial1L['surf_vmr(ppmv)']) * 1e6)
medianP2L = np.median((partial2L['surf_vmr(ppmv)']) * 1e6)
medianP3L = np.median((partial3L['surf_vmr(ppmv)']) * 1e6)
medianAL  = np.median((fullL['surf_vmr(ppmv)'])     * 1e6)

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
medianZH  = np.median((zeroH['surf_vmr(ppmv)'])     * 1e6)
medianP1H = np.median((partial1H['surf_vmr(ppmv)']) * 1e6)
medianP2H = np.median((partial2H['surf_vmr(ppmv)']) * 1e6)
medianP3H = np.median((partial3H['surf_vmr(ppmv)']) * 1e6)
medianAH  = np.median((fullH['surf_vmr(ppmv)'])     * 1e6)

#------------------------------------------------------------------------------
# Calculate the Median absolute deviation

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
madZL  = stats.median_absolute_deviation((zeroL['surf_vmr(ppmv)'])     * 1e6)
madP1L = stats.median_absolute_deviation((partial1L['surf_vmr(ppmv)']) * 1e6)
madP2L = stats.median_absolute_deviation((partial2L['surf_vmr(ppmv)']) * 1e6)
madP3L = stats.median_absolute_deviation((partial3L['surf_vmr(ppmv)']) * 1e6)
madAL  = stats.median_absolute_deviation((fullL['surf_vmr(ppmv)'])     * 1e6)

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
madZH  = stats.median_absolute_deviation((zeroH['surf_vmr(ppmv)'])     * 1e6)
madP1H = stats.median_absolute_deviation((partial1H['surf_vmr(ppmv)']) * 1e6)
madP2H = stats.median_absolute_deviation((partial2H['surf_vmr(ppmv)']) * 1e6)
madP3H = stats.median_absolute_deviation((partial3H['surf_vmr(ppmv)']) * 1e6)
madAH  = stats.median_absolute_deviation((fullH['surf_vmr(ppmv)'])     * 1e6)

#------------------------------------------------------------------------------
# Welches T-Test on BrO 
# T-test for the means of 2 indpendent populations
# (Note: unequal sample sizes and/or variance, therefore Welches t-test)

# LWS
WT_stat_1,  WT_pval_1  = stats.ttest_ind(zeroL['surf_vmr(ppmv)'],     partial1L['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 0% vs 1-30%
WT_stat_2,  WT_pval_2  = stats.ttest_ind(zeroL['surf_vmr(ppmv)'],     partial2L['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 0% vs 30-60%
WT_stat_3,  WT_pval_3  = stats.ttest_ind(zeroL['surf_vmr(ppmv)'],     partial3L['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 0% vs 60-90%
WT_stat_4,  WT_pval_4  = stats.ttest_ind(zeroL['surf_vmr(ppmv)'],     fullL['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 0% vs 90-100%

WT_stat_5,  WT_pval_5  = stats.ttest_ind(partial1L['surf_vmr(ppmv)'], partial2L['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 1-30% vs 30-60%
WT_stat_6,  WT_pval_6  = stats.ttest_ind(partial1L['surf_vmr(ppmv)'], partial3L['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 1-30% vs 60-90%
WT_stat_7,  WT_pval_7  = stats.ttest_ind(partial1L['surf_vmr(ppmv)'], fullL['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 1-30% vs 90-100%

WT_stat_8,  WT_pval_8  = stats.ttest_ind(partial2L['surf_vmr(ppmv)'], partial3L['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 30-60% vs 60-90%
WT_stat_9,  WT_pval_9  = stats.ttest_ind(partial2L['surf_vmr(ppmv)'], fullL['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 30-60% vs 90-100%

WT_stat_10, WT_pval_10 = stats.ttest_ind(partial3L['surf_vmr(ppmv)'], fullL['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 60-90% vs 90-100%

# HWS
WT_stat_11, WT_pval_11 = stats.ttest_ind(zeroH['surf_vmr(ppmv)'],     partial1H['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 0% vs 1-30%
WT_stat_12, WT_pval_12 = stats.ttest_ind(zeroH['surf_vmr(ppmv)'],     partial2H['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 0% vs 30-60%
WT_stat_13, WT_pval_13 = stats.ttest_ind(zeroH['surf_vmr(ppmv)'],     partial3H['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 0% vs 60-90%
WT_stat_14, WT_pval_14 = stats.ttest_ind(zeroH['surf_vmr(ppmv)'],     fullH['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 0% vs 90-100%

WT_stat_15, WT_pval_15 = stats.ttest_ind(partial1H['surf_vmr(ppmv)'], partial2H['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 1-30% vs 30-60%
WT_stat_16, WT_pval_16 = stats.ttest_ind(partial1H['surf_vmr(ppmv)'], partial3H['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 1-30% vs 60-90%
WT_stat_17, WT_pval_17 = stats.ttest_ind(partial1H['surf_vmr(ppmv)'], fullH['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 1-30% vs 90-100%

WT_stat_18, WT_pval_18 = stats.ttest_ind(partial2H['surf_vmr(ppmv)'], partial3H['surf_vmr(ppmv)'], equal_var = False) # Sea Ice 30-60% vs 60-90%
WT_stat_19, WT_pval_19 = stats.ttest_ind(partial2H['surf_vmr(ppmv)'], fullH['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 30-60% vs 90-100%

WT_stat_20, WT_pval_20 = stats.ttest_ind(partial3H['surf_vmr(ppmv)'], fullH['surf_vmr(ppmv)'],     equal_var = False) # Sea Ice 60-90% vs 90-100%

#------------------------------------------------------------------------------
# KS-Test on BrO (Kolmogorov-Smirnov Test)

# LWS
KS_stat_1,  KS_pval_1  = stats.ks_2samp(zeroL['surf_vmr(ppmv)'],     partial1L['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 0% vs 1-30%
KS_stat_2,  KS_pval_2  = stats.ks_2samp(zeroL['surf_vmr(ppmv)'],     partial2L['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 0% vs 30-60%
KS_stat_3,  KS_pval_3  = stats.ks_2samp(zeroL['surf_vmr(ppmv)'],     partial3L['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 0% vs 60-90%
KS_stat_4,  KS_pval_4  = stats.ks_2samp(zeroL['surf_vmr(ppmv)'],     fullL['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 0% vs 90-100%

KS_stat_5,  KS_pval_5  = stats.ks_2samp(partial1L['surf_vmr(ppmv)'], partial2L['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 1-30% vs 30-60%
KS_stat_6,  KS_pval_6  = stats.ks_2samp(partial1L['surf_vmr(ppmv)'], partial3L['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 1-30% vs 60-90%
KS_stat_7,  KS_pval_7  = stats.ks_2samp(partial1L['surf_vmr(ppmv)'], fullL['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 1-30% vs 90-100%

KS_stat_8,  KS_pval_8  = stats.ks_2samp(partial2L['surf_vmr(ppmv)'], partial3L['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 30-60% vs 60-90%
KS_stat_9,  KS_pval_9  = stats.ks_2samp(partial2L['surf_vmr(ppmv)'], fullL['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 30-60% vs 90-100%

KS_stat_10, KS_pval_10 = stats.ks_2samp(partial3L['surf_vmr(ppmv)'], fullL['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 60-90% vs 90-100%

# HWS
KS_stat_11, KS_pval_11 = stats.ks_2samp(zeroH['surf_vmr(ppmv)'],     partial1H['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 0% vs 1-30%
KS_stat_12, KS_pval_12 = stats.ks_2samp(zeroH['surf_vmr(ppmv)'],     partial2H['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 0% vs 30-60%
KS_stat_13, KS_pval_13 = stats.ks_2samp(zeroH['surf_vmr(ppmv)'],     partial3H['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 0% vs 60-90%
KS_stat_14, KS_pval_14 = stats.ks_2samp(zeroH['surf_vmr(ppmv)'],     fullH['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 0% vs 90-100%

KS_stat_15, KS_pval_15 = stats.ks_2samp(partial1H['surf_vmr(ppmv)'], partial2H['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 1-30% vs 30-60%
KS_stat_16, KS_pval_16 = stats.ks_2samp(partial1H['surf_vmr(ppmv)'], partial3H['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 1-30% vs 60-90%
KS_stat_17, KS_pval_17 = stats.ks_2samp(partial1H['surf_vmr(ppmv)'], fullH['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 1-30% vs 90-100%

KS_stat_18, KS_pval_18 = stats.ks_2samp(partial2H['surf_vmr(ppmv)'], partial3H['surf_vmr(ppmv)'], alternative='two-sided', mode='auto') # Sea Ice 30-60% vs 60-90%
KS_stat_19, KS_pval_19 = stats.ks_2samp(partial2H['surf_vmr(ppmv)'], fullH['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 30-60% vs 90-100%

KS_stat_20, KS_pval_20 = stats.ks_2samp(partial3H['surf_vmr(ppmv)'], fullH['surf_vmr(ppmv)'],     alternative='two-sided', mode='auto') # Sea Ice 60-90% vs 90-100%


# Build a pandas dataframe
dfBrO_Varia = {'Welches (stat)':[WT_stat_1,  WT_stat_2,  WT_stat_3,  WT_stat_4,
                                 WT_stat_5,  WT_stat_6,  WT_stat_7,
                                 WT_stat_8,  WT_stat_9,
                                 WT_stat_10,
                                 WT_stat_11, WT_stat_12, WT_stat_13, WT_stat_14,
                                 WT_stat_15, WT_stat_16, WT_stat_17,
                                 WT_stat_18, WT_stat_19,
                                 WT_stat_20],
               'Welches (pval)':[WT_pval_1,  WT_pval_2,  WT_pval_3,  WT_pval_4,
                                 WT_pval_5,  WT_pval_6,  WT_pval_7,
                                 WT_pval_8,  WT_pval_9,
                                 WT_pval_10,
                                 WT_pval_11, WT_pval_12, WT_pval_13, WT_pval_14,
                                 WT_pval_15, WT_pval_16, WT_pval_17,
                                 WT_pval_18, WT_pval_19,
                                 WT_pval_20],
               'KS-Test (stat)':[KS_stat_1,  KS_stat_2,  KS_stat_3,  KS_stat_4,
                                 KS_stat_5,  KS_stat_6,  KS_stat_7,
                                 KS_stat_8,  KS_stat_9,
                                 KS_stat_10,
                                 KS_stat_11, KS_stat_12, KS_stat_13, KS_stat_14,
                                 KS_stat_15, KS_stat_16, KS_stat_17,
                                 KS_stat_18, KS_stat_19,
                                 KS_stat_20],
               'KS-Test (pval)':[KS_pval_1,  KS_pval_2,  KS_pval_3,  KS_pval_4,
                                 KS_pval_5,  KS_pval_6,  KS_pval_7,
                                 KS_pval_8,  KS_pval_9,
                                 KS_pval_10,
                                 KS_pval_11, KS_pval_12, KS_pval_13, KS_pval_14,
                                 KS_pval_15, KS_pval_16, KS_pval_17,
                                 KS_pval_18, KS_pval_19,
                                 KS_pval_20]}
dfBrO_Varia = pd.DataFrame(dfBrO_Varia, index = ['LWS_0%_vs_1-30%',      'LWS_0%_vs_30-60%',    'LWS_0%_vs_60-90%','LWS_0%_vs_100%',
                                                 'LWS_1-30%_vs_30-60%',  'LWS_1-30%_vs_60-90%', 'LWS_1-30%_vs_100%',
                                                 'LWS_30-60%_vs_60-90%', 'LWS_30-60%_vs_100%',
                                                 'LWS_60-90%_vs_100%',
                                                 'HWS_0%_vs_1-30%',      'HWS_0%_vs_30-60%',    'HWS_0%_vs_60-90%','HWS_0%_vs_100%',
                                                 'HWS_1-30%_vs_30-60%',  'HWS_1-30%_vs_60-90%', 'HWS_1-30%_vs_100%',
                                                 'HWS_30-60%_vs_60-90%', 'HWS_30-60%_vs_100%',
                                                 'HWS_60-90%_vs_100%'])
dfBrO_Varia.to_csv('/Users/ncp532/Documents/Data/STATS_BrO_SI.csv')

#------------------------------------------------------------------------------
# Build a dataframe for the BrO BoxPlot

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
example_data1 = [((zeroL['surf_vmr(ppmv)']) * 1e6), ((partial1L['surf_vmr(ppmv)']) * 1e6), ((partial2L['surf_vmr(ppmv)']) * 1e6), ((partial3L['surf_vmr(ppmv)']) * 1e6), ((fullL['surf_vmr(ppmv)']) * 1e6)]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
example_data2 = [((zeroH['surf_vmr(ppmv)']) * 1e6), ((partial1H['surf_vmr(ppmv)']) * 1e6), ((partial2H['surf_vmr(ppmv)']) * 1e6), ((partial3H['surf_vmr(ppmv)']) * 1e6), ((fullH['surf_vmr(ppmv)']) * 1e6)]

#------------------------------------------------------------------------------
# Make a list of the number of values in each distribution

# text to include with label
j1  = 'n = ' 
j1L = '(LWS)\nn = '
j1H = '(HWS)\nn = '

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
aL = len(zeroL)
#bL = len(partial1L)
cL = len(partial2L)
dL = len(partial3L)
eL = len(fullL)

DF1L = [aL,cL,dL,eL]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
aH = len(zeroH)
#bH = len(partial1H)
cH = len(partial2H)
dH = len(partial3H)
eH = len(fullH)

DF1H = [aH,cH,dH,eH]

#------------------------------------------------------------------------------
# Make a list of the mean +/- std dev for each distribution

# text to include with label
j2 = 'mean = '

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
mean1L = str("%4.1f"%(meanZL))  + u" \u00B1 " + str("%4.1f"%(stdevZL))
#mean2L = str("%4.1f"%(meanP1L)) + u" \u00B1 " + str("%4.1f"%(stdevP1L))
mean3L = str("%4.1f"%(meanP2L)) + u" \u00B1 " + str("%4.1f"%(stdevP2L))
mean4L = str("%4.1f"%(meanP3L)) + u" \u00B1 " + str("%4.1f"%(stdevP3L))
mean5L = str("%4.1f"%(meanAL))  + u" \u00B1 " + str("%4.1f"%(stdevAL))

DF2L = [mean1L, mean3L, mean4L, mean5L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
mean1H = str("%4.1f"%(meanZH))  + u" \u00B1 " + str("%4.1f"%(stdevZH))
#mean2H = str("%4.1f"%(meanP1H)) + u" \u00B1 " + str("%4.1f"%(stdevP1H))
mean3H = str("%4.1f"%(meanP2H)) + u" \u00B1 " + str("%4.1f"%(stdevP2H))
mean4H = str("%4.1f"%(meanP3H)) + u" \u00B1 " + str("%4.1f"%(stdevP3H))
mean5H = str("%4.1f"%(meanAH))  + u" \u00B1 " + str("%4.1f"%(stdevAH))

DF2H = [mean1H, mean3H, mean4H, mean5H]

#------------------------------------------------------------------------------
# Make a list of the mean +/- std dev for each distribution

# text to include with label
j3 = 'Median = '
j4 = 'Median \u00B1 MAD\n'

#-----------------------------
# Low Wind Speed (<7 m/s)
#-----------------------------
median1L = str("%4.1f"%(medianZL))  + u" \u00B1 " + str("%4.1f"%(madZL))
#median2L = str("%4.1f"%(medianP1L)) + u" \u00B1 " + str("%4.1f"%(madP1L))
median3L = str("%4.1f"%(medianP2L)) + u" \u00B1 " + str("%4.1f"%(madP2L))
median4L = str("%4.1f"%(medianP3L)) + u" \u00B1 " + str("%4.1f"%(madP3L))
median5L = str("%4.1f"%(medianAL))  + u" \u00B1 " + str("%4.1f"%(madAL))

MedianL  = [medianZL, medianP2L, medianP3L, medianAL]
MADL     = [madZL,    madP2L,    madP3L,    madAL]
DF3L     = [median1L, median3L,  median4L,  median5L]

#-----------------------------
# High Wind Speed (>=7 m/s)
#-----------------------------
median1H = str("%4.1f"%(medianZH))  + u" \u00B1 " + str("%4.1f"%(madZH))
#median2H = str("%4.1f"%(medianP1H)) + u" \u00B1 " + str("%4.1f"%(madP1H))
median3H = str("%4.1f"%(medianP2H)) + u" \u00B1 " + str("%4.1f"%(madP2H))
median4H = str("%4.1f"%(medianP3H)) + u" \u00B1 " + str("%4.1f"%(madP3H))
median5H = str("%4.1f"%(medianAH))  + u" \u00B1 " + str("%4.1f"%(madAH))

MedianH  = [medianZH, medianP2H, medianP3H, medianAH]
MADH     = [madZH,    madP2H,    madP3H,    madAH]
DF3H     = [median1H, median3H,  median4H,  median5H]

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

box1L = ax1.boxplot(((zeroL['surf_vmr(ppmv)']) * 1e6), positions=[0.8], notch=True, patch_artist=True,
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
box3L = ax1.boxplot(((partial2L['surf_vmr(ppmv)']) * 1e6), positions=[1.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3L[item], color=c5)
plt.setp(box3L["boxes"], facecolor=c6)
plt.setp(box3L["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (Low Wind Speed)
c7 = "black"
c8 = "green"
box4L = ax1.boxplot(((partial3L['surf_vmr(ppmv)']) * 1e6), positions=[2.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4L[item], color=c7)
plt.setp(box4L["boxes"], facecolor=c8)
plt.setp(box4L["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (Low Wind Speed)
c9 = "black"
c10 = "purple"
box5L = ax1.boxplot(((fullL['surf_vmr(ppmv)']) * 1e6), positions=[3.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5L[item], color=c9)
plt.setp(box5L["boxes"], facecolor=c10)
plt.setp(box5L["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph
for i, v in enumerate(DF1L):
    t = ax1.text((i)+0.8 ,v/DF1L[i]-0.75,j1L + str(DF1L[i]),fontsize=12,color='black',fontweight='bold',horizontalalignment='center')
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
lg = ax1.legend([box1L["boxes"][0],box3L["boxes"][0],box4L["boxes"][0],box5L["boxes"][0]],[DF3L[0],DF3L[1],DF3L[2],DF3L[3]], loc='upper left',bbox_to_anchor=(0.85, 0.98),title='Median \u00B1 MAD',fontsize=15)
lg.get_title().set_fontsize(15)
lg.get_title().set_fontweight('bold')

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 1
ax1 = plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

#-----------------------------
# BOX PLOT 1 (High Wind Speed)
c1 = "black"
c2 = "blue"

box1H = ax1.boxplot(((zeroH['surf_vmr(ppmv)']) * 1e6), positions=[1.2], notch=True, patch_artist=True,
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
box3H = ax1.boxplot(((partial2H['surf_vmr(ppmv)']) * 1e6), positions=[2.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3H[item], color=c5)
plt.setp(box3H["boxes"], facecolor=c6)
plt.setp(box3H["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (High Wind Speed)
c7 = "black"
c8 = "green"
box4H = ax1.boxplot(((partial3H['surf_vmr(ppmv)']) * 1e6), positions=[3.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4H[item], color=c7)
plt.setp(box4H["boxes"], facecolor=c8)
plt.setp(box4H["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (High Wind Speed)
c9 = "black"
c10 = "purple"
box5H = ax1.boxplot(((fullH['surf_vmr(ppmv)']) * 1e6), positions=[4.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5H[item], color=c9)
plt.setp(box5H["boxes"], facecolor=c10)
plt.setp(box5H["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph
for i, v in enumerate(DF1H):
    t= ax1.text((i)+1.2 ,v/DF1H[i]-0.75,j1H + str(DF1H[i]),fontsize=12,color='black',fontweight='bold',horizontalalignment='center')
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
lg = ax1.legend([box1H["boxes"][0],box3H["boxes"][0],box4H["boxes"][0],box5H["boxes"][0]], [DF3H[0],DF3H[1],DF3H[2],DF3H[3]], loc='upper left',bbox_to_anchor=(0.85, 0.98),title='Median \u00B1 MAD',fontsize=15)
lg.get_title().set_fontsize(15)
lg.get_title().set_fontweight('bold')

#------------------------------------------------------------------------------
# PLOT GRAPH 2

fig2, ax1 = plt.subplots()

#-----------------------------
# BOX PLOT 1 (Low Wind Speed)
c1 = "black"
c2 = "blue"

box1L = ax1.boxplot(((zeroL['surf_vmr(ppmv)']) * 1e6), positions=[0.8], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

# BOX PLOT 1 (High Wind Speed)
c1 = "black"
c2 = "red"

box1H = ax1.boxplot(((zeroH['surf_vmr(ppmv)']) * 1e6), positions=[1.2], notch=True, patch_artist=True,
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
box3L = ax1.boxplot(((partial2L['surf_vmr(ppmv)']) * 1e6), positions=[1.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3L[item], color=c5)
plt.setp(box3L["boxes"], facecolor=c6)
plt.setp(box3L["fliers"], markeredgecolor=c5)

# BOX PLOT 3 (High Wind Speed)
c5 = "black"
c6 = "red"
box3H = ax1.boxplot(((partial2H['surf_vmr(ppmv)']) * 1e6), positions=[2.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3H[item], color=c5)
plt.setp(box3H["boxes"], facecolor=c6)
plt.setp(box3H["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (Low Wind Speed)
c7 = "black"
c8 = "blue"
box4L = ax1.boxplot(((partial3L['surf_vmr(ppmv)']) * 1e6), positions=[2.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4L[item], color=c7)
plt.setp(box4L["boxes"], facecolor=c8)
plt.setp(box4L["fliers"], markeredgecolor=c7)

# BOX PLOT 4 (High Wind Speed)
c7 = "black"
c8 = "red"
box4H = ax1.boxplot(((partial3H['surf_vmr(ppmv)']) * 1e6), positions=[3.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4H[item], color=c7)
plt.setp(box4H["boxes"], facecolor=c8)
plt.setp(box4H["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (Low Wind Speed)
c9 = "black"
c10 = "blue"
box5L = ax1.boxplot(((fullL['surf_vmr(ppmv)']) * 1e6), positions=[3.8], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5L[item], color=c9)
plt.setp(box5L["boxes"], facecolor=c10)
plt.setp(box5L["fliers"], markeredgecolor=c9)

# BOX PLOT 5 (High Wind Speed)
c9 = "black"
c10 = "red"
box5H = ax1.boxplot(((fullH['surf_vmr(ppmv)']) * 1e6), positions=[4.2], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5H[item], color=c9)
plt.setp(box5H["boxes"], facecolor=c10)
plt.setp(box5H["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph (no of variables)

# Low wind speed
for i, v in enumerate(DF1L):
    t = ax1.text((i)+0.8 ,v/DF1L[i]-1.05,j1 + str(DF1L[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

# High wind speed
for i, v in enumerate(DF1H):
    t= ax1.text((i)+1.2 ,v/DF1H[i]-1.05,j1 + str(DF1H[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

#-----------------------------
# Add values to the graph (median and mad)

# Low wind speed
for i, v in enumerate(MedianL):
    t = ax1.text((i)+0.8 ,v/MedianL[i]-0.75,j4 + str("%4.2f"%(MedianL[i])) + u" \u00B1 " + str("%4.2f"%(MADH[i])),fontsize=11,color='blue',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

# High wind speed
for i, v in enumerate(MedianH):
    t = ax1.text((i)+1.2 ,v/MedianH[i]-0.75,j4 + str("%4.2f"%(MedianH[i])) + u" \u00B1 " + str("%4.2f"%(MADH[i])),fontsize=11,color='red',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
  
# Format the y-axis
plt.ylim(-0.4,10)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# Format the x-axis
plt.xlim(0.4,4.6)
plt.xticks([1.0,2.0,3.0,4.0],['None\n(0%)','Partial\n(30-60%)','Partial\n(60-90%)','Full\n(90-100%)'],fontsize=15)

# Add axis labels
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
ax1.set_xlabel('Sea Ice Cover', fontsize=20, labelpad=15)

# Add a legend
lg = ax1.legend([box1L["boxes"][0],box1H["boxes"][0]], ["Low (<7 m/s)","High (>7 m/s)"], loc='upper left',bbox_to_anchor=(0.82, 0.96),title='Wind speed',fontsize=15)
lg.get_title().set_fontsize(15)
lg.get_title().set_fontweight('bold')
plt.show()

#------------------------------------------------------------------------------
# PLOT GRAPH 3

fig3, ax1 = plt.subplots()

#-----------------------------
# BOX PLOT 1 (Low Wind Speed)
c1 = "black"
c2 = "blue"

box1L = ax1.boxplot(((zeroL['surf_vmr(ppmv)']) * 1e6), positions=[0.8], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c2, color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color=c1),widths=(0.25)
            )

# BOX PLOT 1 (High Wind Speed)
c1 = "black"
c2 = "red"

box1H = ax1.boxplot(((zeroH['surf_vmr(ppmv)']) * 1e6), positions=[1.3], notch=True, patch_artist=True,
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
box3L = ax1.boxplot(((partial2L['surf_vmr(ppmv)']) * 1e6), positions=[1.9], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3L[item], color=c5)
plt.setp(box3L["boxes"], facecolor=c6)
plt.setp(box3L["fliers"], markeredgecolor=c5)

# BOX PLOT 3 (High Wind Speed)
c5 = "black"
c6 = "red"
box3H = ax1.boxplot(((partial2H['surf_vmr(ppmv)']) * 1e6), positions=[3.5], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box3H[item], color=c5)
plt.setp(box3H["boxes"], facecolor=c6)
plt.setp(box3H["fliers"], markeredgecolor=c5)

#-----------------------------
# BOX PLOT 4 (Low Wind Speed)
c7 = "black"
c8 = "blue"
box4L = ax1.boxplot(((partial3L['surf_vmr(ppmv)']) * 1e6), positions=[2.4], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4L[item], color=c7)
plt.setp(box4L["boxes"], facecolor=c8)
plt.setp(box4L["fliers"], markeredgecolor=c7)

# BOX PLOT 4 (High Wind Speed)
c7 = "black"
c8 = "red"
box4H = ax1.boxplot(((partial3H['surf_vmr(ppmv)']) * 1e6), positions=[4.0], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box4H[item], color=c7)
plt.setp(box4H["boxes"], facecolor=c8)
plt.setp(box4H["fliers"], markeredgecolor=c7)

#-----------------------------
# BOX PLOT 5 (Low Wind Speed)
c9 = "black"
c10 = "blue"
box5L = ax1.boxplot(((fullL['surf_vmr(ppmv)']) * 1e6), positions=[2.9], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5L[item], color=c9)
plt.setp(box5L["boxes"], facecolor=c10)
plt.setp(box5L["fliers"], markeredgecolor=c9)

# BOX PLOT 5 (High Wind Speed)
c9 = "black"
c10 = "red"
box5H = ax1.boxplot(((fullH['surf_vmr(ppmv)']) * 1e6), positions=[4.5], notch=True, patch_artist=True,widths=(0.25))
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box5H[item], color=c9)
plt.setp(box5H["boxes"], facecolor=c10)
plt.setp(box5H["fliers"], markeredgecolor=c9)

#-----------------------------
# Add values to the graph (no of variables)

# Low wind speed
t = ax1.text(0.8, -0.050000000000000044, j1 + str(DF1L[0]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

ADF1L = DF1L[1:4]
z = 1.9
for i, v in enumerate(ADF1L):
    t = ax1.text(z ,v/ADF1L[i]-1.05,j1 + str(ADF1L[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
    z = z + 0.5
   
# High wind speed
t = ax1.text(1.3, -0.050000000000000044, j1 + str(DF1H[0]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

ADF1H = DF1H[1:4]
z = 3.5
# High wind speed
for i, v in enumerate(ADF1H):
    t= ax1.text(z ,v/ADF1H[i]-1.05,j1 + str(ADF1H[i]),fontsize=11,color='black',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
    z = z + 0.5

#-----------------------------
# Add values to the graph (median and mad)

# Low wind speed
t = ax1.text(0.8, 0.25, j4 + str("%4.1f"%(MedianL[0])) + u" \u00B1 " + str("%4.1f"%(MADL[0])),fontsize=11,color='blue',fontweight='bold',horizontalalignment='center')
t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

AMedianL = MedianL[1:4]
AMADL    = MADL[1:4]
z = 1.9
for i, v in enumerate(AMedianL):
    t = ax1.text(z, v/AMedianL[i]-0.75, j4 + str("%4.1f"%(AMedianL[i])) + u" \u00B1 " + str("%4.1f"%(AMADL[i])),fontsize=11,color='blue',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
    z = z + 0.5

# High wind speed
t = ax1.text(1.3, 0.25, j4 + str("%4.1f"%(MedianH[0])) + u" \u00B1 " + str("%4.1f"%(MADH[0])),fontsize=11,color='red',fontweight='bold',horizontalalignment='center')
t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))

AMedianH = MedianH[1:4]
AMADH    = MADH[1:4]
z = 3.5
for i, v in enumerate(AMedianH):
    t = ax1.text(z, v/AMedianH[i]-0.75, j4 + str("%4.1f"%(AMedianH[i])) + u" \u00B1 " + str("%4.1f"%(AMADH[i])),fontsize=11,color='red',fontweight='bold',horizontalalignment='center')
    t.set_bbox(dict(facecolor='white', alpha=1.0, edgecolor='white'))
    z = z + 0.5
    
# Format the y-axis
plt.ylim(-0.4,8)
plt.yticks(fontsize=15)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

# Format the x-axis
plt.xlim(0.4,4.9)
plt.xticks([0.8,1.3,1.9,2.4,2.9,3.5,4.0,4.5],['None\n(0%)','None\n(0%)','Partial\n(30-60%)','Partial\n(60-90%)','Full\n(90-100%)','Partial\n(30-60%)','Partial\n(60-90%)','Full\n(90-100%)'],fontsize=15)

# Add axis labels
ax1.set_ylabel('BrO VMR (pptv)', fontsize=20, labelpad=15)
ax1.set_xlabel('Sea Ice Cover', fontsize=20, labelpad=15)

# Add a vertical line to seperate sea ice and no sea ice periods
plt.axvline(1.6,color='black')

# Add a legend
lg = ax1.legend([box1L["boxes"][0],box1H["boxes"][0]], ["Low (<7 m/s)","High (>7 m/s)"], loc='upper left',bbox_to_anchor=(0.62, 0.96),title='Wind speed',fontsize=15)
lg.get_title().set_fontsize(15)
lg.get_title().set_fontweight('bold')
plt.show()