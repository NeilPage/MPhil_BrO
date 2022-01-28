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

# Date and Time handling package
import datetime as dt
from datetime import datetime,time, timedelta		# functions to handle date and time
from matplotlib.colors import BoundaryNorm

#------------------------------------------------------------------------------
# DEFINE THE DATASET

# BrO
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv',index_col=0)       # BrO V1 (2017/18)
BrO_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv',index_col=0)       # BrO V2 (2017/18)
BrO_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv',index_col=0)       # BrO V3 (2017/18)

BrO_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv',index_col=0)       # BrO V1 (2018/19)
BrO_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv',index_col=0)       # BrO V2 (2018/19)
BrO_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv',index_col=0)       # BrO V3 (2018/19)

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv',index_col=0) # BrO SIPEXII (2012)

# AEC
AEC_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_Aerosol/V1_17_AeroExt_338.csv',index_col=0) # AEC at 338nm V1 (2017/18)
AEC_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_Aerosol/V2_17_AeroExt_338.csv',index_col=0) # AEC at 338nm V2 (2017/18)
AEC_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_Aerosol/V3_17_AeroExt_338.csv',index_col=0) # AEC at 338nm V3 (2017/18)

AEC_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_Aerosol/V1_18_AeroExt_338.csv',index_col=0) # AEC at 338nm V1 (2018/19)
AEC_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_Aerosol/V2_18_AeroExt_338.csv',index_col=0) # AEC at 338nm V2 (2018/19)
AEC_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_Aerosol/V3_18_AeroExt_338.csv',index_col=0) # AEC at 338nm V3 (2018/19)

AEC_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_Aerosol/SIPEXII_AeroExt_338.csv',index_col=0) # AEC at 338nm SIPEXII (2012)

# AOD
AOD_V1_17   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_AOD/V1_17_AOD_338.csv',index_col=0) # AOD at 338nm V1 (2017/18)
AOD_V2_17   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_AOD/V2_17_AOD_338.csv',index_col=0) # AOD at 338nm V2 (2017/18)
AOD_V3_17   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_AOD/V3_17_AOD_338.csv',index_col=0) # AOD at 338nm V3 (2017/18)

AOD_V1_18   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_AOD/V1_18_AOD_338.csv',index_col=0) # AOD at 338nm V1 (2018/19)
AOD_V2_18   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_AOD/V2_18_AOD_338.csv',index_col=0) # AOD at 338nm V2 (2018/19)
AOD_V3_18   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_AOD/V3_18_AOD_338.csv',index_col=0) # AOD at 338nm V3 (2018/19)

AOD_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_AOD/SIPEXII_AOD_338.csv',index_col=0) # AOD at 338nm SIPEXII (2012)

# Met
Met_V1_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V1_17_underway_60.csv', index_col=0)
Met_V2_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V2_17_underway_60.csv', index_col=0)
Met_V3_17M = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V3_17_underway_60.csv', index_col=0)
Met_V3_17D = Met_V3_17M

Met_V1_18  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V1_18_underway_60.csv', index_col=0) 
Met_V2_18  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V2_18_underway_60.csv', index_col=0)
Met_V3_18M = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/ShipTrack/V3_18_underway_60.csv', index_col=0) 
Met_V3_18D = Met_V3_18M

Met_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/ShipTrack/SIPEXII_underway_60.csv', index_col=0) 

#------------------------------------------------------------------------------
# FILTER THE BrO DATA FOR RELATIVE ERROR 

# Calculate the Relative Error (>=0.6)
Filter1 = BrO_V1_17['err_surf_vmr'] / BrO_V1_17['surf_vmr(ppmv)']
Filter2 = BrO_V2_17['err_surf_vmr'] / BrO_V2_17['surf_vmr(ppmv)']
Filter3 = BrO_V3_17['err_surf_vmr'] / BrO_V3_17['surf_vmr(ppmv)']

Filter4 = BrO_V1_18['err_surf_vmr'] / BrO_V1_18['surf_vmr(ppmv)']
Filter5 = BrO_V2_18['err_surf_vmr'] / BrO_V2_18['surf_vmr(ppmv)']
Filter6 = BrO_V3_18['err_surf_vmr'] / BrO_V3_18['surf_vmr(ppmv)']

Filter7 = BrO_SIPEXII['err_surf_vmr'] / BrO_SIPEXII['surf_vmr(ppmv)']

# Apply the filter
V1_17F       = Filter1 < 0.6
BrO_V1_17T   = BrO_V1_17[V1_17F]

V2_17F       = Filter2 < 0.6
BrO_V2_17T   = BrO_V2_17[V2_17F]

V3_17F       = Filter3 < 0.6
BrO_V3_17T   = BrO_V3_17[V3_17F]

V1_18F       = Filter4 < 0.6
BrO_V1_18T   = BrO_V1_18[V1_18F]

V2_18F       = Filter5 < 0.6
BrO_V2_18T   = BrO_V2_18[V2_18F]

V3_18F       = Filter6 < 0.6
BrO_V3_18T   = BrO_V3_18[V3_18F]

SIPEXIIF     = Filter7 < 0.6
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

# AEC
AEC_V1_17   = AEC_V1_17.T
AEC_V2_17   = AEC_V2_17.T
AEC_V3_17M  = AEC_V3_17.T
AEC_V3_17D  = AEC_V3_17.T

AEC_V1_18   = AEC_V1_18.T
AEC_V2_18   = AEC_V2_18.T
AEC_V3_18M  = AEC_V3_18.T
AEC_V3_18D  = AEC_V3_18.T

AEC_SIPEXII = AEC_SIPEXII.T

# AOD
AOD_V1_17   = AOD_V1_17
AOD_V2_17   = AOD_V2_17
AOD_V3_17M  = AOD_V3_17
AOD_V3_17D  = AOD_V3_17

AOD_V1_18   = AOD_V1_18
AOD_V2_18   = AOD_V2_18
AOD_V3_18M  = AOD_V3_18
AOD_V3_18D  = AOD_V3_18

AOD_SIPEXII = AOD_SIPEXII

#------------------------------------------------------------------------------
# SET THE DATE

# BrO
BrO_V1_17T.index   = (pd.to_datetime(BrO_V1_17T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_17T.index   = (pd.to_datetime(BrO_V2_17T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_17MT.index  = (pd.to_datetime(BrO_V3_17MT.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_17DT.index  = (pd.to_datetime(BrO_V3_17DT.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_V1_18T.index   = (pd.to_datetime(BrO_V1_18T.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
BrO_V2_18T.index   = (pd.to_datetime(BrO_V2_18T.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
BrO_V3_18MT.index  = (pd.to_datetime(BrO_V3_18MT.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
BrO_V3_18DT.index  = (pd.to_datetime(BrO_V3_18DT.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

BrO_SIPEXIIT.index = (pd.to_datetime(BrO_SIPEXIIT.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

# AEC
AEC_V1_17.index   = (pd.to_datetime(AEC_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
AEC_V2_17.index   = (pd.to_datetime(AEC_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
AEC_V3_17M.index  = (pd.to_datetime(AEC_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
AEC_V3_17D.index  = (pd.to_datetime(AEC_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

AEC_V1_18.index   = (pd.to_datetime(AEC_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
AEC_V2_18.index   = (pd.to_datetime(AEC_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
AEC_V3_18M.index  = (pd.to_datetime(AEC_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
AEC_V3_18D.index  = (pd.to_datetime(AEC_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

AEC_SIPEXII.index = (pd.to_datetime(AEC_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

# AEC
AOD_V1_17.index   = (pd.to_datetime(AOD_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
AOD_V2_17.index   = (pd.to_datetime(AOD_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
AOD_V3_17M.index  = (pd.to_datetime(AOD_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
AOD_V3_17D.index  = (pd.to_datetime(AOD_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

AOD_V1_18.index   = (pd.to_datetime(AOD_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
AOD_V2_18.index   = (pd.to_datetime(AOD_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
AOD_V3_18M.index  = (pd.to_datetime(AOD_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
AOD_V3_18D.index  = (pd.to_datetime(AOD_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

AOD_SIPEXII.index = (pd.to_datetime(AOD_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

# Met
Met_V1_17.index   = (pd.to_datetime(Met_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
Met_V2_17.index   = (pd.to_datetime(Met_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
Met_V3_17M.index  = (pd.to_datetime(Met_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
Met_V3_17D.index  = (pd.to_datetime(Met_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

Met_V1_18.index   = (pd.to_datetime(Met_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
Met_V2_18.index   = (pd.to_datetime(Met_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
Met_V3_18M.index  = (pd.to_datetime(Met_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
Met_V3_18D.index  = (pd.to_datetime(Met_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

Met_SIPEXII.index = (pd.to_datetime(Met_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8

#------------------------------------------------------------------------------
# RESAMPLE MET TO 20 MIN AVERAGES

Met_V1_17   = Met_V1_17.resample('20T').mean()
Met_V2_17   = Met_V2_17.resample('20T').mean()
Met_V3_17M  = Met_V3_17M.resample('20T').mean()
Met_V3_17D  = Met_V3_17D.resample('20T').mean()

Met_V1_18   = Met_V1_18.resample('20T').mean()
Met_V2_18   = Met_V2_18.resample('20T').mean()
Met_V3_18M  = Met_V3_18M.resample('20T').mean()
Met_V3_18D  = Met_V3_18D.resample('20T').mean()

Met_SIPEXII = Met_SIPEXII.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

Met_V1_17.index   = Met_V1_17.index   - pd.Timedelta(minutes=10)
Met_V2_17.index   = Met_V2_17.index   - pd.Timedelta(minutes=10)
Met_V3_17M.index  = Met_V3_17M.index  - pd.Timedelta(minutes=10)
Met_V3_17D.index  = Met_V3_17D.index  - pd.Timedelta(minutes=10)

Met_V1_18.index   = Met_V1_18.index   - pd.Timedelta(minutes=10)
Met_V2_18.index   = Met_V2_18.index   - pd.Timedelta(minutes=10)
Met_V3_18M.index  = Met_V3_18M.index  - pd.Timedelta(minutes=10)
Met_V3_18D.index  = Met_V3_18D.index  - pd.Timedelta(minutes=10)

Met_SIPEXII.index = Met_SIPEXII.index - pd.Timedelta(minutes=10)

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

# AEC
AEC_V1_17   = AEC_V1_17.replace(-9999.000000, np.nan)
AEC_V2_17   = AEC_V2_17.replace(-9999.000000, np.nan)
AEC_V3_17M  = AEC_V3_17M.replace(-9999.000000, np.nan)
AEC_V3_17D  = AEC_V3_17D.replace(-9999.000000, np.nan)

AEC_V1_18   = AEC_V1_18.replace(-9999.000000, np.nan)
AEC_V2_18   = AEC_V2_18.replace(-9999.000000, np.nan)
AEC_V3_18M  = AEC_V3_18M.replace(-9999.000000, np.nan)
AEC_V3_18D  = AEC_V3_18D.replace(-9999.000000, np.nan)

AEC_SIPEXII = AEC_SIPEXII.replace(-9999.000000, np.nan)

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
# AEC
Davis        = (AEC_V1_17.index >= start_date) & (AEC_V1_17.index < end_date)
V1_17_AEC    = AEC_V1_17[Davis]
# AOD
Davis        = (AOD_V1_17.index >= start_date) & (AOD_V1_17.index < end_date)
V1_17_AOD    = AOD_V1_17[Davis]
# Met
Davis        = (Met_V1_17.index >= start_date) & (Met_V1_17.index < end_date)
V1_17_Met    = Met_V1_17[Davis]

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
# AEC
Casey1       = (AEC_V2_17.index >= start_date1) & (AEC_V2_17.index < end_date1)
Casey2       = (AEC_V2_17.index >= start_date2) & (AEC_V2_17.index < end_date2)
V2_17_AEC1   = AEC_V2_17[Casey1]
V2_17_AEC2   = AEC_V2_17[Casey2]
V2_17_AEC    = pd.concat([V2_17_AEC1,V2_17_AEC2], axis =0)
# AOD
Casey1       = (AOD_V2_17.index >= start_date1) & (AOD_V2_17.index < end_date1)
Casey2       = (AOD_V2_17.index >= start_date2) & (AOD_V2_17.index < end_date2)
V2_17_AOD1   = AOD_V2_17[Casey1]
V2_17_AOD2   = AOD_V2_17[Casey2]
V2_17_AOD    = pd.concat([V2_17_AOD1,V2_17_AOD2], axis =0)
# Met
Casey1       = (Met_V2_17.index >= start_date1) & (Met_V2_17.index < end_date1)
Casey2       = (Met_V2_17.index >= start_date2) & (Met_V2_17.index < end_date2)
V2_17_Met1   = Met_V2_17[Casey1]
V2_17_Met2   = Met_V2_17[Casey2]
V2_17_Met    = pd.concat([V2_17_Met1,V2_17_Met2], axis =0)

#-----------------------------
# V3_17 Mawson (1-17 Feb 2018)
#-----------------------------
start_date    = '2018-02-01'
end_date      = '2018-02-18'
# BrO
Mawson        = (BrO_V3_17MT.index >= start_date) & (BrO_V3_17MT.index < end_date)
V3_17_BrOM    = BrO_V3_17MT[Mawson]
# AEC
Mawson        = (AEC_V3_17M.index >= start_date) & (AEC_V3_17M.index < end_date)
V3_17_AECM    = AEC_V3_17M[Mawson]
# AOD
Mawson        = (AOD_V3_17M.index >= start_date) & (AOD_V3_17M.index < end_date)
V3_17_AODM    = AOD_V3_17M[Mawson]
# Met
Mawson        = (Met_V3_17M.index >= start_date) & (Met_V3_17M.index < end_date)
V3_17_MetM    = Met_V3_17M[Mawson]

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
# AEC
Davis1        = (AEC_V3_17D.index >= start_date1) & (AEC_V3_17D.index < end_date1)
Davis2        = (AEC_V3_17D.index >= start_date2) & (AEC_V3_17D.index < end_date2)
V3_17_AEC1    = AEC_V3_17D[Davis1]
V3_17_AEC2    = AEC_V3_17D[Davis2]
V3_17_AECD    = pd.concat([V3_17_AEC1,V3_17_AEC2], axis =0)
# AOD
Davis1        = (AOD_V3_17D.index >= start_date1) & (AOD_V3_17D.index < end_date1)
Davis2        = (AOD_V3_17D.index >= start_date2) & (AOD_V3_17D.index < end_date2)
V3_17_AOD1    = AOD_V3_17D[Davis1]
V3_17_AOD2    = AOD_V3_17D[Davis2]
V3_17_AODD    = pd.concat([V3_17_AOD1,V3_17_AOD2], axis =0)
# Met
Davis1        = (Met_V3_17D.index >= start_date1) & (Met_V3_17D.index < end_date1)
Davis2        = (Met_V3_17D.index >= start_date2) & (Met_V3_17D.index < end_date2)
V3_17_Met1    = Met_V3_17D[Davis1]
V3_17_Met2    = Met_V3_17D[Davis2]
V3_17_MetD    = pd.concat([V3_17_Met1,V3_17_Met2], axis =0)

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# BrO
Davis        = (BrO_V1_18T.index >= start_date) & (BrO_V1_18T.index < end_date)
V1_18_BrO    = BrO_V1_18T[Davis]
# AEC
Davis        = (AEC_V1_18.index >= start_date) & (AEC_V1_18.index < end_date)
V1_18_AEC    = AEC_V1_18[Davis]
# AOD
Davis        = (AOD_V1_18.index >= start_date) & (AOD_V1_18.index < end_date)
V1_18_AOD    = AOD_V1_18[Davis]
# Met
Davis        = (Met_V1_18.index >= start_date) & (Met_V1_18.index < end_date)
V1_18_Met    = Met_V1_18[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# BrO
Casey        = (BrO_V2_18T.index >= start_date) & (BrO_V2_18T.index < end_date)
V2_18_BrO    = BrO_V2_18T[Casey]
# AEC
Casey        = (AEC_V2_18.index >= start_date) & (AEC_V2_18.index < end_date)
V2_18_AEC    = AEC_V2_18[Casey]
# AOD
Casey        = (AOD_V2_18.index >= start_date) & (AOD_V2_18.index < end_date)
V2_18_AOD    = AOD_V2_18[Casey]
# Met
Casey        = (Met_V2_18.index >= start_date) & (Met_V2_18.index < end_date)
V2_18_Met    = Met_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# BrO
Mawson        = (BrO_V3_18MT.index >= start_date) & (BrO_V3_18MT.index < end_date)
V3_18_BrOM    = BrO_V3_18MT[Mawson]
# AEC
Mawson        = (AEC_V3_18M.index >= start_date) & (AEC_V3_18M.index < end_date)
V3_18_AECM    = AEC_V3_18M[Mawson]
# AOD
Mawson        = (AOD_V3_18M.index >= start_date) & (AOD_V3_18M.index < end_date)
V3_18_AODM    = AOD_V3_18M[Mawson]
# Met
Mawson        = (Met_V3_18M.index >= start_date) & (Met_V3_18M.index < end_date)
V3_18_MetM    = Met_V3_18M[Mawson]

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
# AEC
Davis1        = (AEC_V3_18D.index >= start_date1) & (AEC_V3_18D.index < end_date1)
Davis2        = (AEC_V3_18D.index >= start_date2) & (AEC_V3_18D.index < end_date2)
V3_18_AEC1    = AEC_V3_18D[Davis1]
V3_18_AEC2    = AEC_V3_18D[Davis2]
V3_18_AECD    = pd.concat([V3_18_AEC1,V3_18_AEC2], axis =0)
# AOD
Davis1        = (AOD_V3_18D.index >= start_date1) & (AOD_V3_18D.index < end_date1)
Davis2        = (AOD_V3_18D.index >= start_date2) & (AOD_V3_18D.index < end_date2)
V3_18_AOD1    = AOD_V3_18D[Davis1]
V3_18_AOD2    = AOD_V3_18D[Davis2]
V3_18_AODD    = pd.concat([V3_18_AOD1,V3_18_AOD2], axis =0)
# Met
Davis1        = (Met_V3_18D.index >= start_date1) & (Met_V3_18D.index < end_date1)
Davis2        = (Met_V3_18D.index >= start_date2) & (Met_V3_18D.index < end_date2)
V3_18_Met1    = Met_V3_18D[Davis1]
V3_18_Met2    = Met_V3_18D[Davis2]
V3_18_MetD    = pd.concat([V3_18_Met1,V3_18_Met2], axis =0)

#-----------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
#-----------------------------
start_date     = '2012-09-23'
end_date       = '2012-11-12'
# BrO
SIPEX          = (BrO_SIPEXIIT.index >= start_date) & (BrO_SIPEXIIT.index < end_date)
SIPEXII_BrO    = BrO_SIPEXIIT[SIPEX]
# AEC
SIPEX          = (AEC_SIPEXII.index >= start_date) & (AEC_SIPEXII.index < end_date)
SIPEXII_AEC    = AEC_SIPEXII[SIPEX]
# AOD
SIPEX          = (AOD_SIPEXII.index >= start_date) & (AOD_SIPEXII.index < end_date)
SIPEXII_AOD    = AOD_SIPEXII[SIPEX]
# Met
SIPEX          = (Met_SIPEXII.index >= start_date) & (Met_SIPEXII.index < end_date)
SIPEXII_Met    = Met_SIPEXII[SIPEX]

#------------------------------------------------------------------------------
# RENAME THE AEC COLUMN FOR SURFACE LEVEL

V1_17_AEC.rename(columns={ V1_17_AEC.columns[0]: 'AEC' }, inplace = True)
V2_17_AEC.rename(columns={ V2_17_AEC.columns[0]: 'AEC' }, inplace = True)
V3_17_AECM.rename(columns={ V3_17_AECM.columns[0]: 'AEC' }, inplace = True)
V3_17_AECD.rename(columns={ V3_17_AECD.columns[0]: 'AEC' }, inplace = True)

V1_18_AEC.rename(columns={ V1_18_AEC.columns[0]: 'AEC' }, inplace = True)
V2_18_AEC.rename(columns={ V2_18_AEC.columns[0]: 'AEC' }, inplace = True)
V3_18_AECM.rename(columns={ V3_18_AECM.columns[0]: 'AEC' }, inplace = True)
V3_18_AECD.rename(columns={ V3_18_AECD.columns[0]: 'AEC' }, inplace = True)

SIPEXII_AEC.rename(columns={ SIPEXII_AEC.columns[0]: 'AEC' }, inplace = True)

#------------------------------------------------------------------------------
# FILTER THE DATAFRAMES TO ONLY INCLUDE THE SAME DATES

# Find periods when BrO and Met are collocated
V1_17_BrO   = pd.merge(left=V1_17_BrO,   right=V1_17_Met,   how='left', left_index=True, right_index=True)
V2_17_BrO   = pd.merge(left=V2_17_BrO,   right=V2_17_Met,   how='left', left_index=True, right_index=True)
V3_17_BrOM  = pd.merge(left=V3_17_BrOM,  right=V3_17_MetM,  how='left', left_index=True, right_index=True)
V3_17_BrOD  = pd.merge(left=V3_17_BrOD,  right=V3_17_MetD,  how='left', left_index=True, right_index=True)

V1_18_BrO   = pd.merge(left=V1_18_BrO,   right=V1_18_Met,   how='left', left_index=True, right_index=True)
V2_18_BrO   = pd.merge(left=V2_18_BrO,   right=V2_18_Met,   how='left', left_index=True, right_index=True)
V3_18_BrOM  = pd.merge(left=V3_18_BrOM,  right=V3_18_MetM,  how='left', left_index=True, right_index=True)
V3_18_BrOD  = pd.merge(left=V3_18_BrOD,  right=V3_18_MetD,  how='left', left_index=True, right_index=True)

SIPEXII_BrO = pd.merge(left=SIPEXII_BrO, right=SIPEXII_Met, how='left', left_index=True, right_index=True)

# Find periods when BrO and AEC are collocated
V1_17_BrO   = pd.merge(left=V1_17_BrO,   right=V1_17_AEC,   how='left', left_index=True, right_index=True)
V2_17_BrO   = pd.merge(left=V2_17_BrO,   right=V2_17_AEC,   how='left', left_index=True, right_index=True)
V3_17_BrOM  = pd.merge(left=V3_17_BrOM,  right=V3_17_AECM,  how='left', left_index=True, right_index=True)
V3_17_BrOD  = pd.merge(left=V3_17_BrOD,  right=V3_17_AECD,  how='left', left_index=True, right_index=True)

V1_18_BrO   = pd.merge(left=V1_18_BrO,   right=V1_18_AEC,   how='left', left_index=True, right_index=True)
V2_18_BrO   = pd.merge(left=V2_18_BrO,   right=V2_18_AEC,   how='left', left_index=True, right_index=True)
V3_18_BrOM  = pd.merge(left=V3_18_BrOM,  right=V3_18_AECM,  how='left', left_index=True, right_index=True)
V3_18_BrOD  = pd.merge(left=V3_18_BrOD,  right=V3_18_AECD,  how='left', left_index=True, right_index=True)

SIPEXII_BrO = pd.merge(left=SIPEXII_BrO, right=SIPEXII_AEC, how='left', left_index=True, right_index=True)

# Find periods when BrO and AOD are collocated
V1_17_BrO   = pd.merge(left=V1_17_BrO,   right=V1_17_AOD,   how='left', left_index=True, right_index=True)
V2_17_BrO   = pd.merge(left=V2_17_BrO,   right=V2_17_AOD,   how='left', left_index=True, right_index=True)
V3_17_BrOM  = pd.merge(left=V3_17_BrOM,  right=V3_17_AODM,  how='left', left_index=True, right_index=True)
V3_17_BrOD  = pd.merge(left=V3_17_BrOD,  right=V3_17_AODD,  how='left', left_index=True, right_index=True)

V1_18_BrO   = pd.merge(left=V1_18_BrO,   right=V1_18_AOD,   how='left', left_index=True, right_index=True)
V2_18_BrO   = pd.merge(left=V2_18_BrO,   right=V2_18_AOD,   how='left', left_index=True, right_index=True)
V3_18_BrOM  = pd.merge(left=V3_18_BrOM,  right=V3_18_AODM,  how='left', left_index=True, right_index=True)
V3_18_BrOD  = pd.merge(left=V3_18_BrOD,  right=V3_18_AODD,  how='left', left_index=True, right_index=True)

SIPEXII_BrO = pd.merge(left=SIPEXII_BrO, right=SIPEXII_AOD, how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# SET THE VARIABLES

# Surface BrO
BrO_Surf_V1_17   = (V1_17_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V2_17   = (V2_17_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V3_17M  = (V3_17_BrOM['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2
BrO_Surf_V3_17D  = (V3_17_BrOD['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2

BrO_Surf_V1_18   = (V1_18_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V2_18   = (V2_18_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13  # Convert to molec/cm2
BrO_Surf_V3_18M  = (V3_18_BrOM['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2
BrO_Surf_V3_18D  = (V3_18_BrOD['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2

BrO_Surf_SIPEXII = (SIPEXII_BrO['surf_num_dens(molec/cm^3)']*20000)/1e13 # Convert to molec/cm2

# LtCol BrO
BrO_LtCol_V1_17   = V1_17_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V2_17   = V2_17_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V3_17M  = V3_17_BrOM['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD
BrO_LtCol_V3_17D  = V3_17_BrOD['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD

BrO_LtCol_V1_18   = V1_18_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V2_18   = V2_18_BrO['BrO_VCD(molec/cm^2)']/1e13  # BrO VCD
BrO_LtCol_V3_18M  = V3_18_BrOM['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD
BrO_LtCol_V3_18D  = V3_18_BrOD['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD

BrO_LtCol_SIPEXII = SIPEXII_BrO['BrO_VCD(molec/cm^2)']/1e13 # BrO VCD


# All BrO
BrO_Surf_All = pd.concat([BrO_Surf_V1_17, BrO_Surf_V2_17, BrO_Surf_V3_17M, BrO_Surf_V3_17D,
                          BrO_Surf_V1_18, BrO_Surf_V2_18, BrO_Surf_V3_18M, BrO_Surf_V3_18D],axis=0)#,
#                          BrO_Surf_SIPEXII],axis=0)
BrO_LtCol_All = pd.concat([BrO_LtCol_V1_17, BrO_LtCol_V2_17, BrO_LtCol_V3_17M, BrO_LtCol_V3_17D,
                          BrO_LtCol_V1_18, BrO_LtCol_V2_18, BrO_LtCol_V3_18M, BrO_LtCol_V3_18D],axis=0)#,
#                          BrO_LtCol_SIPEXII],axis=0)

# AEC
AEC_V1_17   = V1_17_BrO['AEC']  # Aerosol extinction coefficient (km-1)
AEC_V2_17   = V2_17_BrO['AEC']   # Aerosol extinction coefficient (km-1)
AEC_V3_17M  = V3_17_BrOM['AEC']  # Aerosol extinction coefficient (km-1)
AEC_V3_17D  = V3_17_BrOD['AEC']  # Aerosol extinction coefficient (km-1)

AEC_V1_18   = V1_18_BrO['AEC']   # Aerosol extinction coefficient (km-1)
AEC_V2_18   = V2_18_BrO['AEC']   # Aerosol extinction coefficient (km-1)
AEC_V3_18M  = V3_18_BrOM['AEC']  # Aerosol extinction coefficient (km-1)
AEC_V3_18D  = V3_18_BrOD['AEC']  # Aerosol extinction coefficient (km-1)

AEC_SIPEXII = SIPEXII_BrO['AEC'] # Aerosol extinction coefficient (km-1)

# AOD
AOD_V1_17   = V1_17_BrO['AOD'] # AOD at 338nm
AOD_V2_17   = V2_17_BrO['AOD'] # AOD at 338nm
AOD_V3_17M  = V3_17_BrOM['AOD'] # AOD at 338nm
AOD_V3_17D  = V3_17_BrOD['AOD'] # AOD at 338nm

AOD_V1_18   = V1_18_BrO['AOD'] # AOD at 338nm
AOD_V2_18   = V2_18_BrO['AOD'] # AOD at 338nm
AOD_V3_18M  = V3_18_BrOM['AOD'] # AOD at 338nm
AOD_V3_18D  = V3_18_BrOD['AOD'] # AOD at 338nm

AOD_SIPEXII = SIPEXII_BrO['AOD'] # AOD at 338nm

# All AEC
AEC_All = pd.concat([AEC_V1_17, AEC_V2_17, AEC_V3_17M, AEC_V3_17D,
                     AEC_V1_18, AEC_V2_18, AEC_V3_18M, AEC_V3_18D],axis=0)#,
 #                    AEC_SIPEXII],axis=0)

# All AOD
AOD_All = pd.concat([AOD_V1_17, AOD_V2_17, AOD_V3_17M, AOD_V3_17D,
                     AOD_V1_18, AOD_V2_18, AOD_V3_18M, AOD_V3_18D],axis=0)#,
#                     AOD_SIPEXII],axis=0)

# Wind speed (port side)
WSP_V1_17   = V1_17_BrO['wnd_spd_port_corr_knot']* 0.514444444   # Convert wind speed port side from knots to m/s
WSP_V2_17   = V2_17_BrO['wnd_spd_port_corr_knot']* 0.514444444   # Convert wind speed port side from knots to m/s
WSP_V3_17M  = V3_17_BrOM['wnd_spd_port_corr_knot']* 0.514444444  # Convert wind speed port side from knots to m/s
WSP_V3_17D  = V3_17_BrOD['wnd_spd_port_corr_knot']* 0.514444444  # Convert wind speed port side from knots to m/s

WSP_V1_18   = V1_18_BrO['wnd_spd_port_corr_knot']* 0.514444444   # Convert wind speed port side from knots to m/s
WSP_V2_18   = V2_18_BrO['wnd_spd_port_corr_knot']* 0.514444444   # Convert wind speed port side from knots to m/s
WSP_V3_18M  = V3_18_BrOM['wnd_spd_port_corr_knot']* 0.514444444  # Convert wind speed port side from knots to m/s
WSP_V3_18D  = V3_18_BrOD['wnd_spd_port_corr_knot']* 0.514444444  # Convert wind speed port side from knots to m/s

WSP_SIPEXII = SIPEXII_BrO['wnd_spd_port_corr_knot']* 0.514444444 # Convert wind speed port side from knots to m/s

# Wind speed (strbrd side)
WSS_V1_17   = V1_17_BrO['wnd_spd_strbrd_corr_knot']* 0.514444444   # Convert wind speed strbrd side from knots to m/s
WSS_V2_17   = V2_17_BrO['wnd_spd_strbrd_corr_knot']* 0.514444444   # Convert wind speed strbrd side from knots to m/s
WSS_V3_17M  = V3_17_BrOM['wnd_spd_strbrd_corr_knot']* 0.514444444  # Convert wind speed strbrd side from knots to m/s
WSS_V3_17D  = V3_17_BrOD['wnd_spd_strbrd_corr_knot']* 0.514444444  # Convert wind speed strbrd side from knots to m/s

WSS_V1_18   = V1_18_BrO['wnd_spd_strbrd_corr_knot']* 0.514444444   # Convert wind speed strbrd side from knots to m/s
WSS_V2_18   = V2_18_BrO['wnd_spd_strbrd_corr_knot']* 0.514444444   # Convert wind speed strbrd side from knots to m/s
WSS_V3_18M  = V3_18_BrOM['wnd_spd_strbrd_corr_knot']* 0.514444444  # Convert wind speed strbrd side from knots to m/s
WSS_V3_18D  = V3_18_BrOD['wnd_spd_strbrd_corr_knot']* 0.514444444  # Convert wind speed strbrd side from knots to m/s

WSS_SIPEXII = SIPEXII_BrO['wnd_spd_strbrd_corr_knot']* 0.514444444 # Convert wind speed strbrd side from knots to m/s

# Wind speed (average of port & strbrd sides)
WS_V1_17   = (WSP_V1_17   + WSS_V1_17)/2
WS_V2_17   = (WSP_V2_17   + WSS_V2_17)/2
WS_V3_17M  = (WSP_V3_17M  + WSS_V3_17M)/2
WS_V3_17D  = (WSP_V3_17D  + WSS_V3_17D)/2

WS_V1_18   = (WSP_V1_18   + WSS_V1_18)/2
WS_V2_18   = (WSP_V2_18   + WSS_V2_18)/2
WS_V3_18M  = (WSP_V3_18M  + WSS_V3_18M)/2
WS_V3_18D  = (WSP_V3_18D  + WSS_V3_18D)/2

WS_SIPEXII = (WSP_SIPEXII + WSS_SIPEXII)/2

# All wind speed
WS_All = pd.concat([WS_V1_17, WS_V2_17, WS_V3_17M, WS_V3_17D,
                    WS_V1_18, WS_V2_18, WS_V3_18M, WS_V3_18D],axis=0)#,
#                    WS_SIPEXII],axis=0)

#------------------------------------------------------------------------------
# CALCULATE THE PERCENTAGE OF BrO IN SURFACE LAYER

Perc_V1_17   = (BrO_Surf_V1_17   / BrO_LtCol_V1_17)*100
Perc_V2_17   = (BrO_Surf_V2_17   / BrO_LtCol_V2_17)*100
Perc_V3_17M  = (BrO_Surf_V3_17M  / BrO_LtCol_V3_17M)*100
Perc_V3_17D  = (BrO_Surf_V3_17D  / BrO_LtCol_V3_17D)*100

Perc_V1_18   = (BrO_Surf_V1_18   / BrO_LtCol_V1_18)*100
Perc_V2_18   = (BrO_Surf_V2_18   / BrO_LtCol_V2_18)*100
Perc_V3_18M  = (BrO_Surf_V3_18M  / BrO_LtCol_V3_18M)*100
Perc_V3_18D  = (BrO_Surf_V3_18D  / BrO_LtCol_V3_18D)*100

Perc_SIPEXII = (BrO_Surf_SIPEXII / BrO_LtCol_SIPEXII)*100

Perc_All     = (BrO_Surf_All     / BrO_LtCol_All)*100

#------------------------------------------------------------------------------
# CALCULATE THE MEAN PERCENTAGE OF BrO IN SURFACE LAYER

Mean_Perc_V1_17  = np.mean(Perc_V1_17)
Mean_Perc_V2_17  = np.mean(Perc_V2_17)
Mean_Perc_V3_17M = np.mean(Perc_V3_17M)
Mean_Perc_V3_17D = np.mean(Perc_V3_17D)

Mean_Perc_V1_18  = np.mean(Perc_V1_18)
Mean_Perc_V2_18  = np.mean(Perc_V2_18)
Mean_Perc_V3_18M = np.mean(Perc_V3_18M)
Mean_Perc_V3_18D = np.mean(Perc_V3_18D)

Mean_Perc_SIPEXII = np.mean(Perc_SIPEXII)

Mean_Perc_All     = np. mean(Perc_All)

#------------------------------------------------------------------------------
# CREATE A DATAFRAME

dfBrO = np.column_stack((BrO_Surf_All,BrO_LtCol_All,Perc_All,AEC_All,AOD_All,WS_All))
dfBrO = pd.DataFrame(dfBrO, columns = ['BrO_Surf_All','BrO_LtCol_All','Perc_All','AEC_All','AOD_All','WS_All'], index = BrO_Surf_All.index)
dfBrO = dfBrO.dropna()

#------------------------------------------------------------------------------
# FILTER THE BrO DATA 

# Apply the filter (AEC)
F1a = dfBrO['AEC_All'] < 10**-8 
BrO_All_1a = dfBrO[F1a]

F2a = (dfBrO['AEC_All'] >= 10**-8) & (dfBrO['AEC_All'] < 10**-7) 
BrO_All_2a = dfBrO[F2a]

F3a = (dfBrO['AEC_All'] >= 10**-7) & (dfBrO['AEC_All'] < 10**-6) 
BrO_All_3a = dfBrO[F3a]

F4a = (dfBrO['AEC_All'] >= 10**-6) & (dfBrO['AEC_All'] < 10**-5) 
BrO_All_4a = dfBrO[F4a]

F5a = (dfBrO['AEC_All'] >= 10**-5) & (dfBrO['AEC_All'] < 10**-4) 
BrO_All_5a = dfBrO[F5a]

F6a = (dfBrO['AEC_All'] >= 10**-4) & (dfBrO['AEC_All'] < 10**-3) 
BrO_All_6a = dfBrO[F6a]

F7a = (dfBrO['AEC_All'] >= 10**-3) & (dfBrO['AEC_All'] < 10**-2) 
BrO_All_7a = dfBrO[F7a]

F8a = (dfBrO['AEC_All'] >= 10**-2) & (dfBrO['AEC_All'] < 10**-1) 
BrO_All_8a = dfBrO[F8a]

F9a = (dfBrO['AEC_All'] >= 10**-1) & (dfBrO['AEC_All'] < 10**0) 
BrO_All_9a = dfBrO[F9a]

F10a = (dfBrO['AEC_All'] >= 10**0) & (dfBrO['AEC_All'] < 10**1) 
BrO_All_10a = dfBrO[F10a]

F11a = (dfBrO['AEC_All'] >= 10**1) & (dfBrO['AEC_All'] < 10**2) 
BrO_All_11a = dfBrO[F11a]

# Apply the filter (AOD)
F1b = dfBrO['AOD_All'] < 10**-2 
BrO_All_1b = dfBrO[F1b]

F2b = (dfBrO['AOD_All'] >= 10**-2) & (dfBrO['AOD_All'] < 10**-1) 
BrO_All_2b = dfBrO[F2b]

F3b = (dfBrO['AOD_All'] >= 10**-1) & (dfBrO['AOD_All'] < 10**0) 
BrO_All_3b = dfBrO[F3b]

F4b = (dfBrO['AOD_All'] >= 10**0) & (dfBrO['AOD_All'] < 10**1) 
BrO_All_4b = dfBrO[F4b]

F5b = (dfBrO['AOD_All'] >= 10**1) & (dfBrO['AOD_All'] < 10**2) 
BrO_All_5b = dfBrO[F5b]

#F6b = (dfBrO['AOD_All'] >= 10**) & (dfBrO['AOD_All'] < 0.3) 
#BrO_All_6b = dfBrO[F6b]
#
#F7b = (dfBrO['AOD_All'] >= 0.3) & (dfBrO['AOD_All'] < 0.35) 
#BrO_All_7b = dfBrO[F7b]
#
#F8b = (dfBrO['AOD_All'] >= 0.35) & (dfBrO['AOD_All'] < 0.4) 
#BrO_All_8b = dfBrO[F8b]
#
#F9b = (dfBrO['AOD_All'] >= 0.4) & (dfBrO['AOD_All'] < 0.45) 
#BrO_All_9b = dfBrO[F9b]
#
#F10b = (dfBrO['AOD_All'] >= 0.45) & (dfBrO['AOD_All'] < 0.5) 
#BrO_All_10b = dfBrO[F10b]

#------------------------------------------------------------------------------
# CALCULATE THE MEAN FOR EACH RANGE

# AEC
Mean1a  = np.mean(BrO_All_1a)
Mean2a  = np.mean(BrO_All_2a)
Mean3a  = np.mean(BrO_All_3a)
Mean4a  = np.mean(BrO_All_4a)
Mean5a  = np.mean(BrO_All_5a)
Mean6a  = np.mean(BrO_All_6a)
Mean7a  = np.mean(BrO_All_7a)
Mean8a  = np.mean(BrO_All_8a)
Mean9a  = np.mean(BrO_All_9a)
Mean10a = np.mean(BrO_All_10a)

Mean_Alla = pd.concat([Mean1a,Mean2a,Mean3a,Mean4a,Mean5a,Mean6a,Mean7a,Mean8a,Mean9a,Mean10a], axis =1)
Mean_Alla = Mean_Alla.T

# AOD
Mean1b  = np.mean(BrO_All_1b)
Mean2b  = np.mean(BrO_All_2b)
Mean3b  = np.mean(BrO_All_3b)
Mean4b  = np.mean(BrO_All_4b)
Mean5b  = np.mean(BrO_All_5b)
#Mean6b  = np.mean(BrO_All_6b)
#Mean7b  = np.mean(BrO_All_7b)
#Mean8b  = np.mean(BrO_All_8b)
#Mean9b  = np.mean(BrO_All_9b)
#Mean10b = np.mean(BrO_All_10b)

Mean_Allb = pd.concat([Mean1b,Mean2b,Mean3b,Mean4b,Mean5b], axis =1)#,Mean6b,Mean7b,Mean8b,Mean9b,Mean10b], axis =1)
Mean_Allb = Mean_Allb.T

#------------------------------------------------------------------------------
# CALCULATE THE StDev FOR EACH RANGE

# AEC
StDev1a  = np.std(BrO_All_1a)
StDev2a  = np.std(BrO_All_2a)
StDev3a  = np.std(BrO_All_3a)
StDev4a  = np.std(BrO_All_4a)
StDev5a  = np.std(BrO_All_5a)
StDev6a  = np.std(BrO_All_6a)
StDev7a  = np.std(BrO_All_7a)
StDev8a  = np.std(BrO_All_8a)
StDev9a  = np.std(BrO_All_9a)
StDev10a = np.std(BrO_All_10a)

StDev_Alla = pd.concat([StDev1a,StDev2a,StDev3a,StDev4a,StDev5a,StDev6a,StDev7a,StDev8a,StDev9a,StDev10a], axis =1)
StDev_Alla = StDev_Alla.T

# AOD
StDev1b  = np.std(BrO_All_1b)
StDev2b  = np.std(BrO_All_2b)
StDev3b  = np.std(BrO_All_3b)
StDev4b  = np.std(BrO_All_4b)
StDev5b  = np.std(BrO_All_5b)
#StDev6b  = np.std(BrO_All_6b)
#StDev7b  = np.std(BrO_All_7b)
#StDev8b  = np.std(BrO_All_8b)
#StDev9b  = np.std(BrO_All_9b)
#StDev10b = np.std(BrO_All_10b)

StDev_Allb = pd.concat([StDev1b,StDev2b,StDev3b,StDev4b,StDev5b], axis =1)#,StDev6b,StDev7b,StDev8b,StDev9b,StDev10b], axis =1)
StDev_Allb = StDev_Allb.T

#------------------------------------------------------------------------------
# PLOT THE GRAPH (CAMMPCAN)
fig = plt.figure()

plt.subplots_adjust(wspace=0.1)

#-------------------------------
# Graph 1
ax=plt.subplot(121) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,24,2), cmap.N)
plt.scatter(AEC_All,BrO_Surf_All, edgecolors='none', marker='o', norm=norm, c=WS_All, cmap=cmap)

# Add a colorbar
#cbar = plt.colorbar(label='Wind speed (m/s)',ticks=[0,2,4,6,8,10,12,14,16,18,20,22,24])

# Plot the mean
ax.plot(Mean_Alla['AEC_All'], Mean_Alla['BrO_Surf_All'],  marker='o', linewidth=3, markersize = 0.5, c='r', linestyle='-', label='Mean')  # Surf BrO

# Plot the lower and upper limits
UL = Mean_Alla['BrO_Surf_All'] + StDev_Alla['BrO_Surf_All'] # find the upper limit
LL = Mean_Alla['BrO_Surf_All'] - StDev_Alla['BrO_Surf_All'] # find the lower limit
ax.plot(Mean_Alla['AEC_All'], UL, 'r-', linewidth=1.5, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(Mean_Alla['AEC_All'], LL, 'r-', linewidth=1.5, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(Mean_Alla['AEC_All'], UL, LL, facecolor='r', alpha=0.3) # fill the distribution

# Format x-axis
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(10**-9,10**1)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,1.2)

# Plot the axis labels
ax.set_ylabel('BrO$_s$$_u$$_r$$_f$ (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
ax.set_xlabel('AEC (km$^-$$^1$)', fontsize=10)

#Plot the legend and title
plt.title('Relationshp between BrO and aerosol particles', fontsize=15, y=1.03, x=1.12)

#-------------------------------
# Graph 2
ax=plt.subplot(122) # options graph 1 (vertical no, horizontal no, graph no)

# ScatterPlot the values
cmap=plt.cm.rainbow
norm = BoundaryNorm(np.arange(0,24,2), cmap.N)
plt.scatter(AOD_All, BrO_LtCol_All, edgecolors='none', marker='o', norm=norm, c=WS_All, cmap=cmap)

# Add a colorbar
cbar = plt.colorbar(label='Wind speed (m/s)',ticks=[0,2,4,6,8,10,12,14,16,18,20,22,24])

# Plot the mean
ax.plot(Mean_Allb['AOD_All'], Mean_Allb['BrO_LtCol_All'],  marker='o', linewidth=3, markersize = 0.5, c='r', linestyle='-', label='Mean')  # Surf BrO

# Plot the lower and upper limits
UL = Mean_Allb['BrO_LtCol_All'] + StDev_Allb['BrO_LtCol_All'] # find the upper limit
LL = Mean_Allb['BrO_LtCol_All'] - StDev_Allb['BrO_LtCol_All'] # find the lower limit
ax.plot(Mean_Allb['AOD_All'], UL, 'r-', linewidth=1.5, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(Mean_Allb['AOD_All'], LL, 'r-', linewidth=1.5, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(Mean_Allb['AOD_All'], UL, LL, facecolor='r', alpha=0.3) # fill the distribution

# Format x-axis
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(10**-3,10**2)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.set_ylim(0,8)

# Plot the axis labels
ax.set_ylabel('BrO$_L$$_T$$_c$$_o$$_l$ (10$^1$$^3$ molec/cm$^2$)', fontsize=10)
ax.set_xlabel('AOD', fontsize=10)
