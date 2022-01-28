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

# BrO
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_retrieval.csv',index_col=0)       # BrO V1 (2017/18)
BrO_V2_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_BrO/V2_17_BrO_retrieval.csv',index_col=0)       # BrO V2 (2017/18)
BrO_V3_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_BrO/V3_17_BrO_retrieval.csv',index_col=0)       # BrO V3 (2017/18)

BrO_V1_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_BrO/V1_18_BrO_retrieval.csv',index_col=0)       # BrO V1 (2018/19)
BrO_V2_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_BrO/V2_18_BrO_retrieval.csv',index_col=0)       # BrO V2 (2018/19)
BrO_V3_18 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_BrO/V3_18_BrO_retrieval.csv',index_col=0)       # BrO V3 (2018/19)

BrO_SIPEXII = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv',index_col=0) # BrO SIPEXII (2012)

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

# MERRA-2 (.CSV)
MERRA2_V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V1_17_MERRA2.csv',   index_col=0)
MERRA2_V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V2_17_MERRA2.csv',   index_col=0)
MERRA2_V3_17M  = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V3_17M_MERRA2.csv',  index_col=0)
MERRA2_V3_17D  = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V3_17D_MERRA2.csv',  index_col=0)

MERRA2_V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V1_18_MERRA2.csv',   index_col=0) 
MERRA2_V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V2_18_MERRA2.csv',   index_col=0)
MERRA2_V3_18M  = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V3_18M_MERRA2.csv',  index_col=0) 
MERRA2_V3_18D  = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/V3_18D_MERRA2.csv',  index_col=0)

MERRA2_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/SIPEXII_MERRA2.csv', index_col=0) 

# Radiosonde
RS_2017 = Dataset('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/Radiosonde/test.nc')
                  
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

# MERRA-2
MERRA2_V1_17.index   = (pd.to_datetime(MERRA2_V1_17.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
MERRA2_V2_17.index   = (pd.to_datetime(MERRA2_V2_17.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
MERRA2_V3_17M.index  = (pd.to_datetime(MERRA2_V3_17M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
MERRA2_V3_17D.index  = (pd.to_datetime(MERRA2_V3_17D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

MERRA2_V1_18.index   = (pd.to_datetime(MERRA2_V1_18.index,   dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7
MERRA2_V2_18.index   = (pd.to_datetime(MERRA2_V2_18.index,   dayfirst=True) + timedelta(hours=8)) # Casey timezone is UT+8
MERRA2_V3_18M.index  = (pd.to_datetime(MERRA2_V3_18M.index,  dayfirst=True) + timedelta(hours=5)) # Mawson timezone is UT+5
MERRA2_V3_18D.index  = (pd.to_datetime(MERRA2_V3_18D.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

MERRA2_SIPEXII.index = (pd.to_datetime(MERRA2_SIPEXII.index, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+88

#------------------------------------------------------------------------------
# RESAMPLE BrO & MET TO 60 MIN AVERAGES

# BrO
BrO_V1_17T   = BrO_V1_17T.resample('60T').mean()
BrO_V2_17T   = BrO_V2_17T.resample('60T').mean()
BrO_V3_17MT  = BrO_V3_17MT.resample('60T').mean()
BrO_V3_17DT  = BrO_V3_17DT.resample('60T').mean()

BrO_V1_18T   = BrO_V1_18T.resample('60T').mean()
BrO_V2_18T   = BrO_V2_18T.resample('60T').mean()
BrO_V3_18MT  = BrO_V3_18MT.resample('60T').mean()
BrO_V3_18DT  = BrO_V3_18DT.resample('60T').mean()

BrO_SIPEXIIT = BrO_SIPEXIIT.resample('60T').mean()

# Met
Met_V1_17   = Met_V1_17.resample('60T').mean()
Met_V2_17   = Met_V2_17.resample('60T').mean()
Met_V3_17M  = Met_V3_17M.resample('60T').mean()
Met_V3_17D  = Met_V3_17D.resample('60T').mean()

Met_V1_18   = Met_V1_18.resample('60T').mean()
Met_V2_18   = Met_V2_18.resample('60T').mean()
Met_V3_18M  = Met_V3_18M.resample('60T').mean()
Met_V3_18D  = Met_V3_18D.resample('60T').mean()

Met_SIPEXII = Met_SIPEXII.resample('60T').mean()

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
#  CALCULATE THE POTENTIAL TEMPERATURE DIFFERENTIAL IN LOWEST 100m (k)

# Potential temperature differential in lowest 100m (K)
MERRA2_V1_17['PTDif100m']   = MERRA2_V1_17['VPT100m']   - MERRA2_V1_17['VPT2m']
MERRA2_V2_17['PTDif100m']   = MERRA2_V2_17['VPT100m']   - MERRA2_V2_17['VPT2m']
MERRA2_V3_17M['PTDif100m']  = MERRA2_V3_17M['VPT100m']  - MERRA2_V3_17M['VPT2m']
MERRA2_V3_17D['PTDif100m']  = MERRA2_V3_17D['VPT100m']  - MERRA2_V3_17D['VPT2m']

MERRA2_V1_18['PTDif100m']   = MERRA2_V1_18['VPT100m']   - MERRA2_V1_18['VPT2m']
MERRA2_V2_18['PTDif100m']   = MERRA2_V2_18['VPT100m']   - MERRA2_V2_18['VPT2m']
MERRA2_V3_18M['PTDif100m']  = MERRA2_V3_18M['VPT100m']  - MERRA2_V3_18M['VPT2m']
MERRA2_V3_18D['PTDif100m']  = MERRA2_V3_18D['VPT100m']  - MERRA2_V3_18D['VPT2m']

MERRA2_SIPEXII['PTDif100m'] = MERRA2_SIPEXII['VPT100m'] - MERRA2_SIPEXII['VPT2m']

#------------------------------------------------------------------------------
#  CALCULATE THE POTENTIAL TEMPERATURE DIFFERENTIAL IN LOWEST 1000m (k)

# Potential temperature differential in lowest 1000m (K)
MERRA2_V1_17['PTDif1000m']   = MERRA2_V1_17['VPT1000m']   - MERRA2_V1_17['VPT2m']
MERRA2_V2_17['PTDif1000m']   = MERRA2_V2_17['VPT1000m']   - MERRA2_V2_17['VPT2m']
MERRA2_V3_17M['PTDif1000m']  = MERRA2_V3_17M['VPT1000m']  - MERRA2_V3_17M['VPT2m']
MERRA2_V3_17D['PTDif1000m']  = MERRA2_V3_17D['VPT1000m']  - MERRA2_V3_17D['VPT2m']

MERRA2_V1_18['PTDif1000m']   = MERRA2_V1_18['VPT1000m']   - MERRA2_V1_18['VPT2m']
MERRA2_V2_18['PTDif1000m']   = MERRA2_V2_18['VPT1000m']   - MERRA2_V2_18['VPT2m']
MERRA2_V3_18M['PTDif1000m']  = MERRA2_V3_18M['VPT1000m']  - MERRA2_V3_18M['VPT2m']
MERRA2_V3_18D['PTDif1000m']  = MERRA2_V3_18D['VPT1000m']  - MERRA2_V3_18D['VPT2m']

MERRA2_SIPEXII['PTDif1000m'] = MERRA2_SIPEXII['VPT1000m'] - MERRA2_SIPEXII['VPT2m']

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
# Met
Davis        = (Met_V1_17.index >= start_date) & (Met_V1_17.index < end_date)
V1_17_Met    = Met_V1_17[Davis]
# MERRA2
Davis        = (MERRA2_V1_17.index >= start_date) & (MERRA2_V1_17.index < end_date)
V1_17_MERRA2 = MERRA2_V1_17[Davis]

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
# Met
Casey1       = (Met_V2_17.index >= start_date1) & (Met_V2_17.index < end_date1)
Casey2       = (Met_V2_17.index >= start_date2) & (Met_V2_17.index < end_date2)
V2_17_Met1   = Met_V2_17[Casey1]
V2_17_Met2   = Met_V2_17[Casey2]
V2_17_Met    = pd.concat([V2_17_Met1,V2_17_Met2], axis =0)
# MERRA2
Casey1       = (MERRA2_V2_17.index >= start_date1) & (MERRA2_V2_17.index < end_date1)
Casey2       = (MERRA2_V2_17.index >= start_date2) & (MERRA2_V2_17.index < end_date2)
V2_17_MERRA21= MERRA2_V2_17[Casey1]
V2_17_MERRA22= MERRA2_V2_17[Casey2]
V2_17_MERRA2 = pd.concat([V2_17_MERRA21,V2_17_MERRA22], axis =0)

#-----------------------------
# V3_17 Mawson (1-17 Feb 2018)
#-----------------------------
start_date    = '2018-02-01'
end_date      = '2018-02-18'
# BrO
Mawson        = (BrO_V3_17MT.index >= start_date) & (BrO_V3_17MT.index < end_date)
V3_17_BrOM    = BrO_V3_17MT[Mawson]
# Met
Mawson        = (Met_V3_17M.index >= start_date) & (Met_V3_17M.index < end_date)
V3_17_MetM    = Met_V3_17M[Mawson]
# MERRA2
Mawson        = (MERRA2_V3_17M.index >= start_date) & (MERRA2_V3_17M.index < end_date)
V3_17_MERRA2M = MERRA2_V3_17M[Mawson]

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
# Met
Davis1        = (Met_V3_17D.index >= start_date1) & (Met_V3_17D.index < end_date1)
Davis2        = (Met_V3_17D.index >= start_date2) & (Met_V3_17D.index < end_date2)
V3_17_Met1    = Met_V3_17D[Davis1]
V3_17_Met2    = Met_V3_17D[Davis2]
V3_17_MetD    = pd.concat([V3_17_Met1,V3_17_Met2], axis =0)
# MERRA2
Davis1        = (MERRA2_V3_17D.index >= start_date1) & (MERRA2_V3_17D.index < end_date1)
Davis2        = (MERRA2_V3_17D.index >= start_date2) & (MERRA2_V3_17D.index < end_date2)
V3_17_MERRA21 = MERRA2_V3_17D[Davis1]
V3_17_MERRA22 = MERRA2_V3_17D[Davis2]
V3_17_MERRA2D = pd.concat([V3_17_MERRA21,V3_17_MERRA22], axis =0)

#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
#-----------------------------
start_date   = '2018-11-07'
end_date     = '2018-11-16'
# BrO
Davis        = (BrO_V1_18T.index >= start_date) & (BrO_V1_18T.index < end_date)
V1_18_BrO    = BrO_V1_18T[Davis]
# Met
Davis        = (Met_V1_18.index >= start_date) & (Met_V1_18.index < end_date)
V1_18_Met    = Met_V1_18[Davis]
# MERRA2
Davis        = (MERRA2_V1_18.index >= start_date) & (MERRA2_V1_18.index < end_date)
V1_18_MERRA2 = MERRA2_V1_18[Davis]

#-----------------------------
# V2_18 Casey (15-30 Dec 2018)
#-----------------------------
start_date   = '2018-12-15'
end_date     = '2018-12-31'
# BrO
Casey        = (BrO_V2_18T.index >= start_date) & (BrO_V2_18T.index < end_date)
V2_18_BrO    = BrO_V2_18T[Casey]
# Met
Casey        = (Met_V2_18.index >= start_date) & (Met_V2_18.index < end_date)
V2_18_Met    = Met_V2_18[Casey]
# MERRA2
Casey        = (MERRA2_V2_18.index >= start_date) & (MERRA2_V2_18.index < end_date)
V2_18_MERRA2 = MERRA2_V2_18[Casey]

#-----------------------------
# V3_18 Mawson (30 Jan - 9 Feb 2019)
#-----------------------------
start_date    = '2019-01-30'
end_date      = '2019-02-10'
# BrO
Mawson        = (BrO_V3_18MT.index >= start_date) & (BrO_V3_18MT.index < end_date)
V3_18_BrOM    = BrO_V3_18MT[Mawson]
# Met
Mawson        = (Met_V3_18M.index >= start_date) & (Met_V3_18M.index < end_date)
V3_18_MetM    = Met_V3_18M[Mawson]
# MERRA2
Mawson        = (MERRA2_V3_18M.index >= start_date) & (MERRA2_V3_18M.index < end_date)
V3_18_MERRA2M = MERRA2_V3_18M[Mawson]

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
# Met
SIPEX          = (Met_SIPEXII.index >= start_date) & (Met_SIPEXII.index < end_date)
SIPEXII_Met    = Met_SIPEXII[SIPEX]
# MERRA2
Davis1        = (MERRA2_V3_18D.index >= start_date1) & (MERRA2_V3_18D.index < end_date1)
Davis2        = (MERRA2_V3_18D.index >= start_date2) & (MERRA2_V3_18D.index < end_date2)
V3_18_MERRA21 = MERRA2_V3_18D[Davis1]
V3_18_MERRA22 = MERRA2_V3_18D[Davis2]
V3_18_MERRA2D = pd.concat([V3_18_MERRA21,V3_18_MERRA22], axis =0)
# MERRA2
SIPEX          = (MERRA2_SIPEXII.index >= start_date) & (MERRA2_SIPEXII.index < end_date)
SIPEXII_MERRA2 = MERRA2_SIPEXII[SIPEX]

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

# Find periods when BrO and MERRA2 are collocated
V1_17_BrO   = pd.merge(left=V1_17_BrO,   right=V1_17_MERRA2,   how='left', left_index=True, right_index=True)
V2_17_BrO   = pd.merge(left=V2_17_BrO,   right=V2_17_MERRA2,   how='left', left_index=True, right_index=True)
V3_17_BrOM  = pd.merge(left=V3_17_BrOM,  right=V3_17_MERRA2M,  how='left', left_index=True, right_index=True)
V3_17_BrOD  = pd.merge(left=V3_17_BrOD,  right=V3_17_MERRA2D,  how='left', left_index=True, right_index=True)

V1_18_BrO   = pd.merge(left=V1_18_BrO,   right=V1_18_MERRA2,   how='left', left_index=True, right_index=True)
V2_18_BrO   = pd.merge(left=V2_18_BrO,   right=V2_18_MERRA2,   how='left', left_index=True, right_index=True)
V3_18_BrOM  = pd.merge(left=V3_18_BrOM,  right=V3_18_MERRA2M,  how='left', left_index=True, right_index=True)
V3_18_BrOD  = pd.merge(left=V3_18_BrOD,  right=V3_18_MERRA2D,  how='left', left_index=True, right_index=True)

SIPEXII_BrO = pd.merge(left=SIPEXII_BrO, right=SIPEXII_MERRA2, how='left', left_index=True, right_index=True)

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

# Temp (port side)
TempP_V1_17   = (V1_17_BrO['temp_air_port_degc'])   # Met temperature port side (C)
TempP_V2_17   = (V2_17_BrO['temp_air_port_degc'])   # Met temperature port side (C)
TempP_V3_17M  = (V3_17_BrOM['temp_air_port_degc'])  # Met temperature port side (C)
TempP_V3_17D  = (V3_17_BrOD['temp_air_port_degc'])  # Met temperature port side (C)

TempP_V1_18   = (V1_18_BrO['temp_air_port_degc'])   # Met temperature port side (C)
TempP_V2_18   = (V2_18_BrO['temp_air_port_degc'])   # Met temperature port side (C)
TempP_V3_18M  = (V3_18_BrOM['temp_air_port_degc'])  # Met temperature port side (C)
TempP_V3_18D  = (V3_18_BrOD['temp_air_port_degc'])  # Met temperature port side (C)

TempP_SIPEXII = (SIPEXII_BrO['temp_air_port_degc']) # Met temperature port side (C)

# Temp (strbrd side)
TempS_V1_17   = (V1_17_BrO['temp_air_strbrd_degc'])   # Met temperature strbrd side (C)
TempS_V2_17   = (V2_17_BrO['temp_air_strbrd_degc'])   # Met temperature strbrd side (C)
TempS_V3_17M  = (V3_17_BrOM['temp_air_strbrd_degc'])  # Met temperature strbrd side (C)
TempS_V3_17D  = (V3_17_BrOD['temp_air_strbrd_degc'])  # Met temperature strbrd side (C)

TempS_V1_18   = (V1_18_BrO['temp_air_strbrd_degc'])   # Met temperature strbrd side (C)
TempS_V2_18   = (V2_18_BrO['temp_air_strbrd_degc'])   # Met temperature strbrd side (C)
TempS_V3_18M  = (V3_18_BrOM['temp_air_strbrd_degc'])  # Met temperature strbrd side (C)
TempS_V3_18D  = (V3_18_BrOD['temp_air_strbrd_degc'])  # Met temperature strbrd side (C)

TempS_SIPEXII = (SIPEXII_BrO['temp_air_strbrd_degc']) # Met temperature strbrd side (C)

# Temp (average of port & strbrd sides)
Temp_V1_17   = (TempP_V1_17   + TempS_V1_17)/2
Temp_V2_17   = (TempP_V2_17   + TempS_V2_17)/2
Temp_V3_17M  = (TempP_V3_17M  + TempS_V3_17M)/2
Temp_V3_17D  = (TempP_V3_17D  + TempS_V3_17D)/2

Temp_V1_18   = (TempP_V1_18   + TempS_V1_18)/2
Temp_V2_18   = (TempP_V2_18   + TempS_V2_18)/2
Temp_V3_18M  = (TempP_V3_18M  + TempS_V3_18M)/2
Temp_V3_18D  = (TempP_V3_18D  + TempS_V3_18D)/2

Temp_SIPEXII = (TempP_SIPEXII + TempS_SIPEXII)/2

# All Temp
Temp_All = pd.concat([Temp_V1_17, Temp_V2_17, Temp_V3_17M, Temp_V3_17D,
                      Temp_V1_18, Temp_V2_18, Temp_V3_18M, Temp_V3_18D],axis=0)#,
#                      Temp_SIPEXII],axis=0)


# Potential temperature differential in lowest 100m (K)
PTDif100m_V1_17   = V1_17_BrO['PTDif100m']
PTDif100m_V2_17   = V2_17_BrO['PTDif100m']
PTDif100m_V3_17M  = V3_17_BrOM['PTDif100m']
PTDif100m_V3_17D  = V3_17_BrOD['PTDif100m']

PTDif100m_V1_18   = V1_18_BrO['PTDif100m']
PTDif100m_V2_18   = V2_18_BrO['PTDif100m']
PTDif100m_V3_18M  = V3_18_BrOM['PTDif100m']
PTDif100m_V3_18D  = V3_18_BrOD['PTDif100m']

PTDif100m_SIPEXII = SIPEXII_BrO['PTDif100m']

# All PTDif100m
PTDif100m_All = pd.concat([PTDif100m_V1_17, PTDif100m_V2_17, PTDif100m_V3_17M, PTDif100m_V3_17D,
                           PTDif100m_V1_18, PTDif100m_V2_18, PTDif100m_V3_18M, PTDif100m_V3_18D],axis=0)#,
#                          PTDif100m_SIPEXII],axis=0)

# Potential temperature differential in lowest 1000m (K)
PTDif1000m_V1_17   = V1_17_BrO['PTDif1000m']
PTDif1000m_V2_17   = V2_17_BrO['PTDif1000m']
PTDif1000m_V3_17M  = V3_17_BrOM['PTDif1000m']
PTDif1000m_V3_17D  = V3_17_BrOD['PTDif1000m']

PTDif1000m_V1_18   = V1_18_BrO['PTDif1000m']
PTDif1000m_V2_18   = V2_18_BrO['PTDif1000m']
PTDif1000m_V3_18M  = V3_18_BrOM['PTDif1000m']
PTDif1000m_V3_18D  = V3_18_BrOD['PTDif1000m']

PTDif1000m_SIPEXII = SIPEXII_BrO['PTDif1000m']

# All PTDif100m
PTDif1000m_All = pd.concat([PTDif1000m_V1_17, PTDif1000m_V2_17, PTDif1000m_V3_17M, PTDif1000m_V3_17D,
                            PTDif1000m_V1_18, PTDif1000m_V2_18, PTDif1000m_V3_18M, PTDif1000m_V3_18D],axis=0)#,
#                           PTDif1000m_SIPEXII],axis=0)


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

Mean_Perc_V1_17   = np.mean(Perc_V1_17)
Mean_Perc_V2_17   = np.mean(Perc_V2_17)
Mean_Perc_V3_17M  = np.mean(Perc_V3_17M)
Mean_Perc_V3_17D  = np.mean(Perc_V3_17D)

Mean_Perc_V1_18   = np.mean(Perc_V1_18)
Mean_Perc_V2_18   = np.mean(Perc_V2_18)
Mean_Perc_V3_18M  = np.mean(Perc_V3_18M)
Mean_Perc_V3_18D  = np.mean(Perc_V3_18D)

Mean_Perc_SIPEXII = np.mean(Perc_SIPEXII)

Mean_Perc_All     = np. mean(Perc_All)

#------------------------------------------------------------------------------
# CREATE A DATAFRAME

dfBrO = np.column_stack((BrO_Surf_All,BrO_LtCol_All,Perc_All,Temp_All,PTDif100m_All,PTDif1000m_All))
dfBrO = pd.DataFrame(dfBrO, columns = ['BrO_Surf_All','BrO_LtCol_All','Perc_All','Temp_All','PTDif100m_All','PTDif1000m_All'], index = BrO_Surf_All.index)
dfBrO = dfBrO.dropna()

#------------------------------------------------------------------------------
# FILTER THE BrO DATA 

# PTDif100m
F1a = dfBrO['PTDif100m_All'] < 0 
BrO_All_1a = dfBrO[F1a]

F2a = (dfBrO['PTDif100m_All'] >= 0)
BrO_All_2a = dfBrO[F2a]

# PTDif1000m
F1b = dfBrO['PTDif1000m_All'] < 0 
BrO_All_1b = dfBrO[F1b]

F2b = (dfBrO['PTDif1000m_All'] >= 0)
BrO_All_2b = dfBrO[F2b]

#------------------------------------------------------------------------------
# CALCULATE THE MEAN FOR EACH RANGE

# PTDif100m
Mean1a  = np.mean(BrO_All_1a)
Mean2a  = np.mean(BrO_All_2a)

Mean_Alla = pd.concat([Mean1a,Mean2a], axis =1)
Mean_Alla = Mean_Alla.T

# PTDif1000m
Mean1b  = np.mean(BrO_All_1b)
Mean2b  = np.mean(BrO_All_2b)

Mean_Allb = pd.concat([Mean1b,Mean2b], axis =1)
Mean_Allb = Mean_Allb.T

#------------------------------------------------------------------------------
# CALCULATE THE StDev FOR EACH RANGE

# PTDif100m
StDev1a  = np.std(BrO_All_1a)
StDev2a  = np.std(BrO_All_2a)

StDev_Alla = pd.concat([StDev1a,StDev2a], axis =1)
StDev_Alla = StDev_Alla.T

# PTDif1000m
StDev1b  = np.std(BrO_All_1b)
StDev2b  = np.std(BrO_All_2b)

StDev_Allb = pd.concat([StDev1b,StDev2b], axis =1)
StDev_Allb = StDev_Allb.T

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig1, ax1 = plt.subplots()

# specify colours
c1 = "blue"
c2 = "red"
c3 = "black"
c4 = "white"

# BoxPlot 1 (<0)
box1 = ax1.boxplot(BrO_All_1a['Perc_All'], positions=[1], notch=True, patch_artist=True,
            boxprops=dict(color=c1,linewidth=2),
            capprops=dict(color=c3,linewidth=2),
            whiskerprops=dict(color=c3,linewidth=2,linestyle='--'),
            flierprops=dict(color=c2, markeredgecolor=c2),
            medianprops=dict(color=c2,linewidth=2),widths=(0.75)
            )
plt.setp(box1["boxes"], facecolor=c4)

# BoxPlot 2 (>0)
box2 = ax1.boxplot(BrO_All_2a['Perc_All'], positions=[2], notch=True, patch_artist=True,
            boxprops=dict(color=c1,linewidth=2),
            capprops=dict(color=c3,linewidth=2),
            whiskerprops=dict(color=c3,linewidth=2,linestyle='--'),
            flierprops=dict(color=c2, markeredgecolor=c2),
            medianprops=dict(color=c2,linewidth=2),widths=(0.75)
            )
plt.setp(box2["boxes"], facecolor=c4)

# Format y-axis
plt.ylim(10,30)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.yticks(fontsize=15)

# Format x-axis
plt.xticks([1,2],['<0 (Neutral)','>0 (Inverted)'],fontsize=15)

# Plot the axis labels and title
#ax1.set_title('BrO distributions for CAMMPCAN 2017-19 and SIPEXII',fontsize=20,y=1.02)
ax1.set_ylabel('BrO <200m (%)', fontsize=20, labelpad=15)
ax1.set_xlabel('Temperature gradient (K/100m)', fontsize=20, labelpad=15)
plt.show()
