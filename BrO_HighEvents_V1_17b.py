#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:23:17 2018

@author: ncp532
"""

# File system packages
from netCDF4 import Dataset, MFDataset
import xarray as xr

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator, AutoMinorLocator
from matplotlib import gridspec
import cmocean
import matplotlib.image as mpimg
from matplotlib import cm                   # imports the colormap function from matplotlib
import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import signal, stats
import os
import glob

# Date and Time handling package
import datetime as dt
from datetime import datetime,time, timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# OBSERVATIONS

#---------
# BrO
#---------
# BrO VMR
BrO_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_BrO/V1_17_BrO_VMR.csv', index_col=0) # BrO data for CAMPCANN V1 (2018/19)

# BrO Error
Err_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/BrO_error/V1_17_BrO_error.csv', index_col=0) # BrO error data for CAMPCANN V1 (2018/19)

# Calculate the Relative Error (>=0.6)
Filter    = Err_V1_17 / BrO_V1_17

# Apply the filter
V1_17F    = Filter < 0.6
BrO_V1_17 = BrO_V1_17[V1_17F]

#---------
# Aerosol extinction at 338 nm (BrO)
#---------
AEC_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_Aerosol/V1_17_AeroExt_338.csv',index_col=0) # Aerosol extinction data at 338 nm for CAMPCANN V1 (2017/18)

#---------
# AOD
#---------
AOD_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_AOD/V1_17_AOD_338.csv',index_col=0) # AOD data for CAMMPCAN V1 (2018/19)

#---------
# SZA
#---------
SZA_V1_17 = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_SZA/V1_17_SZA.csv',index_col=0) # SZA data for CAMPCANN V1 (2018/19)

#---------
# MET
#---------
Met_V1_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ShipTrack/V1_17_underway_60.csv', index_col=0)

#---------
# O3
#---------
O3_V1_17  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv', index_col=0)

#---------
# Hg0
#---------
Hg0_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/CAMMPCAN_V1_Hg0_QAQC_17-18.csv', index_col=0)

#-------------
# Sea Ice
#-------------

# XARRAY
cubes_E1_2a = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/Hamburg_ICDC/20171114_median5day.nc', decode_cf=False, engine='netcdf4')
cubes_E3_4a = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/Hamburg_ICDC/20171115_median5day.nc', decode_cf=False, engine='netcdf4')
cubes_E5a   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/Hamburg_ICDC/20171116_median5day.nc', decode_cf=False, engine='netcdf4')
cubes_E6_7a = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/Hamburg_ICDC/20171120_median5day.nc', decode_cf=False, engine='netcdf4')
cubes_E8a   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/Hamburg_ICDC/20171121_median5day.nc', decode_cf=False, engine='netcdf4')

cubes_E1_2b = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/NSIDC/2017-18/seaice_conc_daily_sh_f17_20171114_v03r01.nc', decode_cf=False, engine='netcdf4')
cubes_E3_4b = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/NSIDC/2017-18/seaice_conc_daily_sh_f17_20171115_v03r01.nc', decode_cf=False, engine='netcdf4')
cubes_E5b   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/NSIDC/2017-18/seaice_conc_daily_sh_f17_20171116_v03r01.nc', decode_cf=False, engine='netcdf4')
cubes_E6_7b = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/NSIDC/2017-18/seaice_conc_daily_sh_f17_20171120_v03r01.nc', decode_cf=False, engine='netcdf4')
cubes_E8b   = xr.open_dataset('/Users/ncp532/Documents/Data/Sea_Ice_Cover/NSIDC/2017-18/seaice_conc_daily_sh_f17_20171121_v03r01.nc', decode_cf=False, engine='netcdf4')

#-------------
# Back Trajectories (EVENT 1)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'

dateStart   = '2017111413'
dateEnd     = '2017111417'
start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E1 = pd.concat(Traj)

#-------------
# Back Trajectories (EVENT2)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'

dateStart   = '2017111422'
dateEnd     = '2017111505'
start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E2 = pd.concat(Traj)

#-------------
# Back Trajectories (EVENT 3)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'

dateStart   = '2017111514'
dateEnd     = '2017111517'
start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E3 = pd.concat(Traj)

#-------------
# Back Trajectories (EVENT 4)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'

dateStart   = '2017111522'
dateEnd     = '2017111605'
start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E4 = pd.concat(Traj)

#-------------
# Back Trajectories (EVENT 5)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'

dateStart   = '2017111611'
dateEnd     = '2017111617'
start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E5 = pd.concat(Traj)

#-------------
# Back Trajectories (EVENT 6)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'


dateStart   = '2017112013'
dateEnd     = '2017112016'
start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E6 = pd.concat(Traj)

#-------------
# Back Trajectories (EVENT 7)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'


dateStart   = '2017112023'
dateEnd     = '2017112106'
start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E7 = pd.concat(Traj)

#-------------
# Back Trajectories (EVENT 8)
#-------------
# Set the location for the working directory
os.chdir("/Users/ncp532/Documents/Data/SeaIce_Trajectories/100m/")

# Set the start and end date
DATE_FORMAT = '%Y%m%d%H'

dateStart   = '2017112111'
dateEnd     = '2017112116'

start_date     = datetime.strptime(dateStart, DATE_FORMAT)
end_date       = datetime.strptime(dateEnd,   DATE_FORMAT)
delta_one_hour = timedelta(hours=1)

# Save a list of all the file names to the variable all_filenames 
all_filenames = []
date = start_date
while date <= end_date:
    dateA = date.strftime('%Y%m%d%H')
    filename = 'gdas1nov0100spring' + dateA + '.csv'
    date += delta_one_hour
    all_filenames.append(filename)

# Set an empty array
Traj = []

# Loop over the files in the folder
for f in all_filenames:
    # Set the file name
    file = pd.read_csv(f)
    # Sum the ice contact column below 100m
    file['IceContact_100m'] = np.sum(file['Traj over Sea Ice and height < 100 m?'])
    # store DataFrame in list
    Traj.append(file)

# Combine all the files
Traj_E8 = pd.concat(Traj)

#------------------------------------------------------------------------------
# TRANSPOSE THE MAX-DOAS DATAFRAMES

BrO_V1_17 = BrO_V1_17.T
AEC_V1_17 = AEC_V1_17.T

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

#---------
# BrO
#---------
BrO_V1_17.index = (pd.to_datetime(BrO_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# Aerosol extinction at 338 nm (BrO)
#---------
AEC_V1_17.index = (pd.to_datetime(AEC_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# AOD
#---------
AOD_V1_17.index = (pd.to_datetime(AOD_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# SZA
#---------
SZA_V1_17.index = (pd.to_datetime(SZA_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# MET
#---------
Met_V1_17.index = (pd.to_datetime(Met_V1_17.index, dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# O3
#---------
O3_V1_17.index  = (pd.to_datetime(O3_V1_17.index,  dayfirst=True) + timedelta(hours=7)) # Davis timezone is UT+7

#---------
# Hg0
#---------
Hg0_V1_17.index  = (pd.to_datetime(Hg0_V1_17.index, dayfirst=True))# + timedelta(hours=8)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 1)
#-------------
Traj_E1['year']     = Traj_E1['Traj Year']
Traj_E1['month']    = Traj_E1['Traj Mon']
Traj_E1['day']      = Traj_E1['Traj Day']
Traj_E1['hour']     = Traj_E1['Traj Hour']
Traj_E1['minute']   = Traj_E1['Traj Min']
Traj_E1['DateTime'] = pd.to_datetime(Traj_E1[['year', 'month', 'day', 'hour', 'minute']])
Traj_E1.index       = (pd.to_datetime(Traj_E1['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 2)
#-------------
Traj_E2['year']     = Traj_E2['Traj Year']
Traj_E2['month']    = Traj_E2['Traj Mon']
Traj_E2['day']      = Traj_E2['Traj Day']
Traj_E2['hour']     = Traj_E2['Traj Hour']
Traj_E2['minute']   = Traj_E2['Traj Min']
Traj_E2['DateTime'] = pd.to_datetime(Traj_E2[['year', 'month', 'day', 'hour', 'minute']])
Traj_E2.index       = (pd.to_datetime(Traj_E2['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 3)
#-------------
Traj_E3['year']     = Traj_E3['Traj Year']
Traj_E3['month']    = Traj_E3['Traj Mon']
Traj_E3['day']      = Traj_E3['Traj Day']
Traj_E3['hour']     = Traj_E3['Traj Hour']
Traj_E3['minute']   = Traj_E3['Traj Min']
Traj_E3['DateTime'] = pd.to_datetime(Traj_E3[['year', 'month', 'day', 'hour', 'minute']])
Traj_E3.index       = (pd.to_datetime(Traj_E3['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 4)
#-------------
Traj_E4['year']     = Traj_E4['Traj Year']
Traj_E4['month']    = Traj_E4['Traj Mon']
Traj_E4['day']      = Traj_E4['Traj Day']
Traj_E4['hour']     = Traj_E4['Traj Hour']
Traj_E4['minute']   = Traj_E4['Traj Min']
Traj_E4['DateTime'] = pd.to_datetime(Traj_E4[['year', 'month', 'day', 'hour', 'minute']])
Traj_E4.index       = (pd.to_datetime(Traj_E4['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 5)
#-------------
Traj_E5['year']     = Traj_E5['Traj Year']
Traj_E5['month']    = Traj_E5['Traj Mon']
Traj_E5['day']      = Traj_E5['Traj Day']
Traj_E5['hour']     = Traj_E5['Traj Hour']
Traj_E5['minute']   = Traj_E5['Traj Min']
Traj_E5['DateTime'] = pd.to_datetime(Traj_E5[['year', 'month', 'day', 'hour', 'minute']])
Traj_E5.index       = (pd.to_datetime(Traj_E5['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 6)
#-------------
Traj_E6['year']     = Traj_E6['Traj Year']
Traj_E6['month']    = Traj_E6['Traj Mon']
Traj_E6['day']      = Traj_E6['Traj Day']
Traj_E6['hour']     = Traj_E6['Traj Hour']
Traj_E6['minute']   = Traj_E6['Traj Min']
Traj_E6['DateTime'] = pd.to_datetime(Traj_E6[['year', 'month', 'day', 'hour', 'minute']])
Traj_E6.index       = (pd.to_datetime(Traj_E6['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 7)
#-------------
Traj_E7['year']     = Traj_E7['Traj Year']
Traj_E7['month']    = Traj_E7['Traj Mon']
Traj_E7['day']      = Traj_E7['Traj Day']
Traj_E7['hour']     = Traj_E7['Traj Hour']
Traj_E7['minute']   = Traj_E7['Traj Min']
Traj_E7['DateTime'] = pd.to_datetime(Traj_E7[['year', 'month', 'day', 'hour', 'minute']])
Traj_E7.index       = (pd.to_datetime(Traj_E7['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

#-------------
# Back Trajectories ( EVENT 8)
#-------------
Traj_E8['year']     = Traj_E8['Traj Year']
Traj_E8['month']    = Traj_E8['Traj Mon']
Traj_E8['day']      = Traj_E8['Traj Day']
Traj_E8['hour']     = Traj_E8['Traj Hour']
Traj_E8['minute']   = Traj_E8['Traj Min']
Traj_E8['DateTime'] = pd.to_datetime(Traj_E8[['year', 'month', 'day', 'hour', 'minute']])
Traj_E8.index       = (pd.to_datetime(Traj_E8['DateTime']) + timedelta(hours=7)) # Davis timezone is UT+7

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
SZA_V1_17 = hampel(SZA_V1_17['SZA'])

#------------------------------------------------------------------------------
# Filter for the day required

SIPEXIITT = BrO_V1_17

# Event 1 and 2 (14 Nov 2017)
start_date = '2017-11-14'
end_date   = '2017-11-15'
Event1_2   = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event1_2M  = SIPEXIITT[Event1_2]

# Event 3 and 4 (15 Nov 2017)
start_date = '2017-11-15'
end_date   = '2017-11-16'
Event3_4   = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event3_4M  = SIPEXIITT[Event3_4]

# Event 5 (16 Nov 2017)
start_date = '2017-11-16'
end_date   = '2017-11-17'
Event5     = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event5M    = SIPEXIITT[Event5]

# Event 6 and 7 (20 Nov 2017)
start_date = '2017-11-20'
end_date   = '2017-11-21'
Event6_7   = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event6_7M  = SIPEXIITT[Event6_7]

# Event 8 (21 Nov 2017)
start_date = '2017-11-21'
end_date   = '2017-11-22'
Event8     = (SIPEXIITT.index >= start_date) & (SIPEXIITT.index < end_date)
Event8M    = SIPEXIITT[Event8]

# Transpose the dataframes back again
Event1_2TT = Event1_2M.T
Event3_4TT = Event3_4M.T
Event5TT   = Event5M.T
Event6_7TT = Event6_7M.T
Event8TT   = Event8M.T

#------------------------------------------------------------------------------
# SET UP THE VALUES TO PLOT

#---------
# High BrO
#---------

high_fil = BrO_V1_17 > 5.9e-6
high_BrO = BrO_V1_17[high_fil]

#---------
# BrO
#---------
# Transpose BrO
BrO_V1_17 = BrO_V1_17.T
#high_BrO = high_BrO.T

# All
#y = V1_2018.index # set the values for the y-axis
#x = np.array(V1_2018.dtypes.index) # set the values for the x-axis
#z = V1_2018.copy() # identify the matrix containing the z-values (BrO in ppMv)

# Filtered
y  = BrO_V1_17.index # set the values for the y-axis
x  = np.array(BrO_V1_17.dtypes.index) # set the values for the x-axis
z  = BrO_V1_17.copy() # identify the matrix containing the z-values (BrO in ppMv)

# y  = high_BrO.index # set the values for the y-axis
# x  = np.array(high_BrO.dtypes.index) # set the values for the x-axis
# z  = high_BrO.copy() # identify the matrix containing the z-values (BrO in ppMv)

#---------------------------------
z[z==-9999]=np.nan # set the erroneous values as NaN 
z = z.loc[:]*1e6 # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz=np.ma.masked_where(np.isnan(z),z) 

#---------
# Aerosol extinction at 338 nm (BrO)
#---------
# Transpose AEC
AEC_V1_17 = AEC_V1_17.T

# All
y3 = AEC_V1_17.index # set the values for the y-axis
x3 = np.array(AEC_V1_17.dtypes.index) # set the values for the x-axis
z3 = AEC_V1_17.copy() # identify the matrix containing the z-values (BrO in ppMv)

z3[z3==-9999]=np.nan # set the erroneous values as NaN 
z3 = z3.loc[:] # change from ppMv to pptv

# when you plot colormaps it changes Nan values to 0.
# Need to mask the array so that Nan values are plotted as grey and not a concentration of 0.
mz3=np.ma.masked_where(np.isnan(z3),z3) 

#---------
# AOD
#---------
AOD_338 = np.array(AOD_V1_17['AOD'])

#---------
# SZA
#---------
SZA = SZA_V1_17

#---------
# MET
#---------
# Pressure
ATM_PRESS = np.array(Met_V1_17['atm_press_hpa'])

# Temperature
TEMP_P    = np.array(Met_V1_17['temp_air_port_degc'])
TEMP_S    = np.array(Met_V1_17['temp_air_strbrd_degc'])
TEMP      = (TEMP_P + TEMP_S) / 2

# Wind Speed
WSP_P     = np.array(Met_V1_17['wnd_spd_port_corr_knot'])   * 0.514444444 # Convert from knots to m/s
WSP_S     = np.array(Met_V1_17['wnd_spd_strbrd_corr_knot']) * 0.514444444 # Convert from knots to m/s
WSP       = (WSP_P + WSP_S) / 2

# Wind Direction
WDIR_P    = np.array(Met_V1_17['wnd_dir_port_corr_deg'])
WDIR_S    = np.array(Met_V1_17['wnd_dir_strbrd_corr_deg'])
WDIR      = (WDIR_P + WDIR_S) / 2

# Vector Mean Wind Direction
Met_V1_17['WD_vect'] = ((WDIR_S * WSP_S) / (WSP_S + WSP_P)) + ((WDIR_P * WSP_P) / (WSP_S + WSP_P))
WD_vect              = Met_V1_17['WD_vect']

# Relative Humidity
RH_P      = np.array(Met_V1_17['rel_humidity_port_percent'])
RH_S      = np.array(Met_V1_17['rel_humidity_strbrd_percent'])
RH        = (RH_P + RH_S) / 2

#---------
# O3
#---------

O3 = np.array(O3_V1_17['O3_(ppb)'])

#---------
# Hg0
#---------

Hg0 = np.array(Hg0_V1_17['ng/m3'])

#-------------
# Sea Ice
#-------------

#HAMBURG
seaice_data_E1_2a = cubes_E1_2a.variables['sea_ice_area_fraction'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
lats_E1_2a        = cubes_E1_2a.latitude
lons_E1_2a        = cubes_E1_2a.longitude

seaice_data_E3_4a = cubes_E3_4a.variables['sea_ice_area_fraction'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
lats_E3_4a        = cubes_E3_4a.latitude
lons_E3_4a        = cubes_E3_4a.longitude

seaice_data_E5a = cubes_E5a.variables['sea_ice_area_fraction'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
lats_E5a        = cubes_E5a.latitude
lons_E5a        = cubes_E5a.longitude

seaice_data_E6_7a = cubes_E6_7a.variables['sea_ice_area_fraction'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
lats_E6_7a        = cubes_E6_7a.latitude
lons_E6_7a        = cubes_E6_7a.longitude

seaice_data_E8a = cubes_E8a.variables['sea_ice_area_fraction'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
lats_E8a        = cubes_E8a.latitude
lons_E8a        = cubes_E8a.longitude

# NSIDC
# seaice_data_E1_2b = cubes2_E1_2b.variables['seaice_conc_cdr'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
# lats_E1_2b        = cubes2_E1_2b.latitude
# lons_E1_2b        = cubes2_E1_2b.longitude

# seaice_data_E3_4b = cubes2_E3_4b.variables['seaice_conc_cdr'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
# lats_E3_4b        = cubes2_E3_4b.latitude
# lons_E3_4b        = cubes2_E3_4b.longitude

# seaice_data_E5b = cubes2_E5b.variables['seaice_conc_cdr'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
# lats_E5b        = cubes2_E5b.latitude
# lons_E5b        = cubes2_E5b.longitude

# seaice_data_E6_7b = cubes2_E6_7b.variables['seaice_conc_cdr'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
# lats_E6_7b        = cubes2_E6_7b.latitude
# lons_E6_7b        = cubes2_E6_7b.longitude

# seaice_data_E8b = cubes2_E8b.variables['seaice_conc_cdr'][0,:,:] # Sea Ice concentration (time,y,x)(1,664,632)
# lats_E8b        = cubes2_E8b.latitude
# lons_E8b        = cubes2_E8b.longitude

# The data are defined in lat/lon coordinate system, so PlateCarree()
# is the appropriate coordinate system:
data_crs = ccrs.PlateCarree()

#------------------------------------------------------------------------------
# Filter the datasets for the ships exhaust
# (remove data when wind direction is 60-190 degrees and wind speed below 5 knots)

DF_O3Met = pd.merge(left=O3_V1_17,right=Met_V1_17, how='left', left_index=True, right_index=True)

# O3 (remove data when wind direction is 90-270 degrees)
O3_90 = DF_O3Met['WD_vect'] <=90 # <=90
D10 = DF_O3Met[O3_90]
O3_270 = DF_O3Met['WD_vect'] >=270 # >=270 
D11 = DF_O3Met[O3_270]
DFO3 = pd.concat([D10,D11],axis=0)

# Step 3 (Remove data when wind speed is below 5 knots (or 2.57222222 m/s))
O3_5knot = DFO3['WD_vect'] >=2.57222222
DFO3 = DFO3[O3_5knot]

#------------------------------------------------------------------------------
# Calculate the mean/StDev and median/MAD BrO VCD for each altitude 

# Event 1 and 2
Mean_Event1_2   = np.mean(Event1_2TT, axis=1) * 1e6
Median_Event1_2 = np.nanmedian(Event1_2TT, axis=1) * 1e6
StDev_Event1_2  = np.std(Event1_2TT, axis=1) * 1e6
MAD_Event1_2    = Event1_2TT.mad(axis=1, skipna='True') * 1e6
MAX_Event1_2    = np.max(Event1_2TT, axis=1) * 1e6
MIN_Event1_2    = np.min(Event1_2TT, axis=1) * 1e6

# Event 3 and 4
Mean_Event3_4   = np.mean(Event3_4TT, axis=1) * 1e6
Median_Event3_4 = np.nanmedian(Event3_4TT, axis=1) * 1e6
StDev_Event3_4  = np.std(Event3_4TT, axis=1) * 1e6
MAD_Event3_4    = Event3_4TT.mad(axis=1, skipna='True') * 1e6
MAX_Event3_4    = np.max(Event3_4TT, axis=1) * 1e6
MIN_Event3_4    = np.min(Event3_4TT, axis=1) * 1e6

# Event 5
Mean_Event5   = np.mean(Event5TT, axis=1) * 1e6
Median_Event5 = np.nanmedian(Event5TT, axis=1) * 1e6
StDev_Event5  = np.std(Event5TT, axis=1) * 1e6
MAD_Event5    = Event5TT.mad(axis=1, skipna='True') * 1e6
MAX_Event5    = np.max(Event5TT, axis=1) * 1e6
MIN_Event5    = np.min(Event5TT, axis=1) * 1e6

# Event 6 and 7
Mean_Event6_725   = np.mean(Event6_7TT, axis=1) * 1e6
Median_Event6_7 = np.nanmedian(Event6_7TT, axis=1) * 1e6
StDev_Event6_7  = np.std(Event6_7TT, axis=1) * 1e6
MAD_Event6_7    = Event6_7TT.mad(axis=1, skipna='True') * 1e6
MAX_Event6_7    = np.max(Event6_7TT, axis=1) * 1e6
MIN_Event6_7    = np.min(Event6_7TT, axis=1) * 1e6

# Event 8
Mean_Event8   = np.mean(Event8TT, axis=1) * 1e6
Median_Event8 = np.nanmedian(Event8TT, axis=1) * 1e6
StDev_Event8  = np.std(Event8TT, axis=1) * 1e6
MAD_Event8    = Event8TT.mad(axis=1, skipna='True') * 1e6
MAX_Event8    = np.max(Event8TT, axis=1) * 1e6
MIN_Event8    = np.min(Event8TT, axis=1) * 1e6

#------------------------------------------------------------------------------
# PLOT EVENT 1 (14 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('14 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax3.text(datetime(2017,11,14,6,10,0), 113,  "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,14,9,10,0), 113,  "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
#ax3.text(datetime(2017,11,14,15,50,0), 113, "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
#ax3.text(datetime(2017,11,14,21,30,0), 113, "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event1_2, MAX_Event1_2.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event1_2, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event1_2.index, MAX_Event1_2, MIN_Event1_2, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(9.3, 0.1, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 9.3 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-10,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
#ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,990) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(30,80) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E1_2a = np.ma.masked_where(seaice_data_E1_2a==0,seaice_data_E1_2a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E1_2a, lats_E1_2a, seaice_data_E1_2a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E1['Traj Lon'], Traj_E1['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E1['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E1['Traj Age'], Traj_E1['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E1['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E1['Traj Age'][0], Traj_E1['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#------------------------------------------------------------------------------
# PLOT EVENT 2 (14 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('14 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
#ax3.text(datetime(2017,11,14,6,10,0), 113,  "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
#ax3.text(datetime(2017,11,14,9,10,0), 113,  "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,14,15,50,0), 113, "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,14,21,30,0), 113, "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event1_2, MAX_Event1_2.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event1_2, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event1_2.index, MAX_Event1_2, MIN_Event1_2, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(9.3, 0.1, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 9.3 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-10,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,14,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,14,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,14,15,50,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,14,21,30,0), linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
#ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,14,0,0,0),datetime(2017,11,14,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,990) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(30,80) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E1_2a = np.ma.masked_where(seaice_data_E1_2a==0,seaice_data_E1_2a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E1_2a, lats_E1_2a, seaice_data_E1_2a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E2['Traj Lon'], Traj_E2['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E2['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E2['Traj Age'], Traj_E2['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E2['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E2['Traj Age'][0], Traj_E2['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#------------------------------------------------------------------------------
# PLOT EVENT 3 (15 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('15 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax3.text(datetime(2017,11,15,7,10,0), 113,  "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,15,9,10,0), 113,  "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,15,17,30,0), 113, "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,15,21,30,0), 113, "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event3_4, MAX_Event3_4.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event3_4, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event3_4.index, MAX_Event3_4, MIN_Event3_4, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(9.5, 0.3, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 9.5 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-15,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
#ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,990) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(30,90) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E3_4a = np.ma.masked_where(seaice_data_E3_4a==0,seaice_data_E3_4a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E3_4a, lats_E3_4a, seaice_data_E3_4a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E3['Traj Lon'], Traj_E3['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E3['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E3['Traj Age'], Traj_E3['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E3['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E3['Traj Age'][0], Traj_E3['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#------------------------------------------------------------------------------
# PLOT EVENT 4 (15 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('15 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
#ax3.text(datetime(2017,11,15,7,10,0), 113,  "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
#ax3.text(datetime(2017,11,15,9,10,0), 113,  "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,15,17,30,0), 113, "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,15,21,30,0), 113, "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event3_4, MAX_Event3_4.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event3_4, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event3_4.index, MAX_Event3_4, MIN_Event3_4, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(9.5, 0.3, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 9.5 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-15,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,15,7,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,15,9,10,0),  linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,15,17,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,15,21,30,0), linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
#ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,15,0,0,0),datetime(2017,11,15,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,990) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(30,90) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E3_4a = np.ma.masked_where(seaice_data_E3_4a==0,seaice_data_E3_4a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E3_4a, lats_E3_4a, seaice_data_E3_4a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E4['Traj Lon'], Traj_E4['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E4['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E4['Traj Age'], Traj_E4['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E4['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E4['Traj Age'][0], Traj_E4['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#------------------------------------------------------------------------------
# PLOT EVENT 5 (16 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('16 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,16,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,16,9,10,0),  linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax3.text(datetime(2017,11,16,4,50,0), 113,  "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,16,9,10,0), 113,  "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event5, MAX_Event5.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event5, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event5.index, MAX_Event5, MIN_Event5, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(8.4, 0.3, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 8.4 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,16,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,16,9,10,0),  linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,16,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,16,9,10,0),  linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-15,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,16,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,16,9,10,0),  linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
#ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,16,0,0,0),datetime(2017,11,16,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(30,90) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E5a = np.ma.masked_where(seaice_data_E5a==0,seaice_data_E5a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E5a, lats_E5a, seaice_data_E5a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E5['Traj Lon'], Traj_E5['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E5['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E5['Traj Age'], Traj_E5['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E5['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E5['Traj Age'][0], Traj_E5['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#------------------------------------------------------------------------------
# PLOT EVENT 6 (20 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('20 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax3.text(datetime(2017,11,20,6,10,0), 113,  "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,20,10,10,0), 113,  "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
#ax3.text(datetime(2017,11,20,16,30,0), 113, "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
#ax3.text(datetime(2017,11,20,22,30,0), 113, "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event6_7, MAX_Event6_7.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event6_7, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event6_7.index, MAX_Event6_7, MIN_Event6_7, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(8.8, 0.3, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 8.8 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-10,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
#start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
#ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1.4) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(40,90) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E6_7a = np.ma.masked_where(seaice_data_E6_7a==0,seaice_data_E6_7a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E6_7a, lats_E6_7a, seaice_data_E6_7a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E6['Traj Lon'], Traj_E6['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E6['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E6['Traj Age'], Traj_E6['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E6['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E6['Traj Age'][0], Traj_E6['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#------------------------------------------------------------------------------
# PLOT EVENT 7 (20 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('20 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
#ax3.text(datetime(2017,11,20,6,10,0), 113,  "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
#ax3.text(datetime(2017,11,20,10,10,0), 113,  "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,20,16,30,0), 113, "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,20,22,30,0), 113, "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event6_7, MAX_Event6_7.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event6_7, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event6_7.index, MAX_Event6_7, MIN_Event6_7, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(8.8, 0.3, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 8.8 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-10,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
#start  = ax.axvline(datetime(2017,11,20,6,10,0),  linewidth=1.0, color='r')
#finish = ax.axvline(datetime(2017,11,20,10,30,0), linewidth=1.0, color='r')
start  = ax.axvline(datetime(2017,11,20,16,30,0), linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,20,22,30,0), linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
#ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,20,0,0,0),datetime(2017,11,20,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1.4) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(40,90) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E6_7a = np.ma.masked_where(seaice_data_E6_7a==0,seaice_data_E6_7a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E6_7a, lats_E6_7a, seaice_data_E6_7a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E7['Traj Lon'], Traj_E7['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E7['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E7['Traj Age'], Traj_E7['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E7['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E7['Traj Age'][0], Traj_E7['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#------------------------------------------------------------------------------
# PLOT EVENT 8 (21 November 2017)
#------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,6))
fig.suptitle('21 November 2017', fontsize=20, y=0.95)
gs = fig.add_gridspec(4, 3)
plt.subplots_adjust(wspace=0.05)

#------------------------------
# Graph 1 (Colormap of BrO)
ax  = fig.add_subplot(gs[0,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Set up the colormap
cmap1 = plt.cm.jet
#cmap1 = cmocean.cm.thermal
norm1 = BoundaryNorm(np.arange(0,16,1), cmap1.N)

# Plot BrO
col1 = ax.pcolormesh(x, y-0.1, mz, vmin=0, vmax=15.5, norm=norm1, cmap=cmap1)

# Plot the AOD and SZA
ax2.scatter(AOD_V1_17.index, AOD_338, marker='x', color='black', label ='AOD (338 nm)')
ax3.plot(SZA_V1_17.index   , SZA,     marker='x', c='magenta',    markersize = 1.0, ls='None', label ='SZA')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,21,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,21,10,50,0), linewidth=1.0, color='r')

# Text box for Start/Finish
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax3.text(datetime(2017,11,21,4,50,0),  113, "Start",  color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)
ax3.text(datetime(2017,11,21,10,50,0), 113, "Finish", color='r', fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props)

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax2.set_ylabel('AOD  (338 nm)', fontsize=10)
ax3.set_ylabel('SZA ($^\circ$)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"BrO (pptv)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (BrO)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (AOD)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax2.set_ylim(0,0.5) # On Station
ax2.yaxis.label.set_color('Black')
ax2.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 3 (SZA)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax3.set_ylim(0,100) # On Station
ax3.yaxis.label.set_color('magenta')
ax3.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "a", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 2 (BrO VCD)

ax = fig.add_subplot(gs[0,-1]) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO MAX vertical profile
Line_Med = ax.errorbar(Median_Event8, MAX_Event8.index,   marker='o', c='blue',  markersize = 3.0, ls='-', xerr=MAD_Event8, capsize=2)
Line_Ran = ax.fill_betweenx(MAX_Event8.index, MAX_Event8, MIN_Event8, facecolor='blue', alpha=0.3, interpolate=False) # fill the distribution
Star_Max = ax.scatter(8.3, 0.3, c ='black', marker='*')

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('BrO (pptv)', fontsize=10)

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(0,10.0)
ax.xaxis.labelpad = 5

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0)
ax.yaxis.labelpad = 10

# adjust the axis labels and ticks
legend = ax.legend([Line_Med, Line_Ran, Star_Max], ['Median $\pm$ MAD', 'Range', 'Max BrO: 8.3 pptv'], loc='upper right', fontsize=10)
legend.get_frame().set_facecolor('grey')
legend.get_frame().set_alpha(0.9)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "e", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 3 (Colormap of Aerosol Extinction at 338nm (BrO))
ax  = fig.add_subplot(gs[1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Set up the colormap
cmap1 = plt.cm.jet
norm1 = BoundaryNorm(np.arange(0,0.55,0.05), cmap1.N)

# Plot AEC at 338nm (BrO)
col1 = ax.pcolormesh(x3, y3-0.1, mz3, vmin=0, vmax=0.5, norm=norm1, cmap=cmap1)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,21,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,21,10,50,0),  linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Altitude (km)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb1 = fig.colorbar(col1, extend='max', pad = 0.16)
clb1.set_label(r"AEC at 338 nm (km$^-$$^1$)", fontsize =10)
clb1.ax.tick_params(labelsize=10)
tick_locator = ticker.MaxNLocator(nbins=5)
clb1.locator = tick_locator
clb1.update_ticks()

# Format y-axis (AEC at 338nm)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_ylim(0,3.0) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "b", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 4 (Met)
ax  = fig.add_subplot(gs[-2,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.set_zorder(ax.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot the wind speed, wind direction and temperature
ax.scatter(Met_V1_17.index,  WSP,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, WD_vect, marker='o', s= 1.0, color='red')
ax3.scatter(Met_V1_17.index, TEMP, marker='o', s= 1.0, color='blue')

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,21,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,21,10,50,0), linewidth=1.0, color='r')

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Wind speed (m/s)', fontsize=10)
ax2.set_ylabel('Wind Direction ($^\circ$)', fontsize=10)
ax3.set_ylabel('Temperature ($^\circ$C)', fontsize=10)
#ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (Wind speed)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Wind direction)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(90))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(45))
ax2.set_ylim(0,360) # On Station
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', which='both', colors='red', labelsize=10)

# Format y-axis 3 (Temperature)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.set_ylim(-15,0) # On Station
ax3.yaxis.label.set_color('blue')
ax3.tick_params(axis='y', which='both', colors='blue', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('blue')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "c", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#------------------------------
# Graph 5 (O3, pressure and RH)
ax  = fig.add_subplot(gs[-1,:-1]) # options graph 2 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()
ax4 = ax.twinx()
ax4.set_zorder(ax.get_zorder()+1)
ax4.patch.set_visible(False)
ax3.set_zorder(ax4.get_zorder()+1)
ax3.patch.set_visible(False)
ax2.set_zorder(ax3.get_zorder()+1)
ax2.patch.set_visible(False)

# Plot Start/Finish time for high BrO event
start  = ax.axvline(datetime(2017,11,21,4,50,0),  linewidth=1.0, color='r')
finish = ax.axvline(datetime(2017,11,21,10,50,0),  linewidth=1.0, color='r')

# Plot the wind speed, wind direction and temperature
ax.scatter(O3_V1_17.index,   O3,  marker='o', s= 1.0, color='black')
ax2.scatter(Met_V1_17.index, ATM_PRESS, marker='o', s= 1.0, color='orange')
ax3.scatter(Hg0_V1_17.index, Hg0, marker='o', s= 1.0, color='green')
#ax3.plot(Hg0_V1_17.index, Hg0, marker='o', markersize= 1.0, ls='-', color='green')
ax4.scatter(Met_V1_17.index, RH,  marker='o', s= 1.0, color='magenta')

# Format x-axis
plt.xlim(datetime(2017,11,21,0,0,0),datetime(2017,11,21,23,59,59))
xmajor_formatter = mdates.DateFormatter('%H:%M') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

# Add axis labels
ax.set_ylabel('Surf. O$_3$ (ppbv)', fontsize=10)
ax2.set_ylabel('Pressure (hpa)', fontsize=10)
ax3.set_ylabel('Hg$^0$ (ng/m$^3$)', fontsize=10)
ax4.set_ylabel('Relative Humidity (%)', fontsize=10)
ax.set_xlabel('Time', fontsize=10)

# Format ColorBar
clb2 = fig.colorbar(col1, ax=ax, extend='max', pad = 0.16).ax.set_visible(False)

# Format y-axis (O3)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.set_ylim(0,40) # On Station
ax.tick_params(axis='y', which='both', colors='Black', labelsize=10)

# Format y-axis 2 (Atmospheric pressure)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax2.set_ylim(970,1000) # On Station
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange', labelsize=10)
ax3.spines["right"].set_color('orange')

# Format y-axis 3 (Hg0)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax3.set_ylim(0,1) # On Station
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', which='both', colors='green', labelsize=10)
ax3.spines["right"].set_position(("axes", 1.12))
ax3.spines["right"].set_color('green')

# Format y-axis 3 (Relative humidity)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax4.set_ylim(40,90) # On Station
ax4.yaxis.label.set_color('magenta')
ax4.tick_params(axis='y', which='both', colors='magenta', labelsize=10)
ax4.spines["right"].set_position(("axes", 1.22))
ax4.spines["right"].set_color('magenta')

# adjust the axis labels and ticks
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax3.text(0.025, 0.925, "d", transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)

#-------------------------------------
# Graph 6 (Sea Ice & HYSPLIT back trajectory)
#ax = fig.add_subplot(gs[1:-1,-1], projection=ccrs.PlateCarree()) # options graph 2 (vertical no, horizontal no, graph no)
ax = plt.subplot(gs[1:-1,-1], projection=ccrs.SouthPolarStereo())#PlateCarree()) # options graph 1 (vertical no, horizontal no, graph no)

# SET UP THE PLOT
ax.set_extent([-45, 135, -42.5, -90])#, crs=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND, zorder=1, edgecolor='k',color='grey')
ax.coastlines()

# PLOT THE DATA (SEA ICE CONCENTRATION) 
seaice_data_E8a = np.ma.masked_where(seaice_data_E8a==0,seaice_data_E8a)
#cmap=cm.get_cmap('viridis')
cmap=cmocean.cm.ice
cmap.set_bad(color='lightgrey')
cs = ax.pcolormesh(lons_E8a, lats_E8a, seaice_data_E8a, transform=data_crs, cmap=cmap) #, bins=np.arange(0,100, 10))
#cs = ax.pcolormesh(lons, lats, seaice_data, transform=data_crs, cmap=cmocean.cm.ice) #, bins=np.arange(0,100, 10))

cb = fig.colorbar(cs,ticks=[0,10,20,30,40,50,60,70,80,90,100], pad = 0.2, shrink=.775)#, orientation="horizontal")

# PLOT THE BACK TRAJECTORIES
cmap = plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#ax.scatter(Traj['Traj Lon'], Traj['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
ax.scatter(Traj_E8['Traj Lon'], Traj_E8['Traj Lat'], zorder=2, cmap=cmap, transform=data_crs, marker='o', s=1, norm=norm, c=Traj_E8['IceContact_100m'], label='Traj Height (m)')

# PLOT THE AAD STATIONS (Lon, Lat)
Davis_lon,   Davis_lat   = -68.5766, 77.9674
Mawson_lon,  Mawson_lat  = -67.6027, 62.8738
Casey_lon,   Casey_lat   = -66.2818, 110.5276
SIPEXII_lon, SIPEXII_lat = -61.5205, 121.1855

# Plot the station markers
ax.plot(Davis_lat,  Davis_lon,  transform=data_crs, color='k', marker='*')
ax.plot(Mawson_lat, Mawson_lon, transform=data_crs, color='k', marker='*')
ax.plot(Casey_lat,  Casey_lon,  transform=data_crs, color='k', marker='*')
#ax.plot(SIPEXII_lat, SIPEXII_lon, transform=data_crs, color='k', marker='o')

# Plot the marker labels
ax.text(Davis_lat + 3,  Davis_lon  - 2, 'Davis',  transform=data_crs, horizontalalignment='right')
ax.text(Mawson_lat + 3, Mawson_lon - 2, 'Mawson', transform=data_crs, horizontalalignment='right')
ax.text(Casey_lat + 3,  Casey_lon  - 2, 'Casey',  transform=data_crs, horizontalalignment='right')
#ax.text(SIPEXII_lat + 3, SIPEXII_lon - 2, 'SIPEXII',horizontalalignment='right')

# PLOT THE MAP GRIDLINES
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='black', alpha=0.5, linestyle='-')
#gl.xlocator   = ticker.FixedLocator([-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100,110,110,120,130,140,150,160,170,180])
#gl.ylocator   = ticker.FixedLocator([-35,-40,-45,-50,-55,-60,-65,-70,-75,-80,-85])
gl.xlocator   = ticker.FixedLocator([-180,-90,0,90,180])
gl.ylocator   = ticker.FixedLocator([-60,-90])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

# PLOT TITLE, AXIS LABEL & LEGEND TITLE
#plt.title("Sea Ice Cover (15/12/2018)", y=1.1, fontsize=20)
cb.set_label('Concentration (%)')#, rotation=90)

# ax.text(-0.12, 0.55, 'latitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='vertical', rotation_mode='anchor',
#          transform=ax.transAxes)

# ax.text(0.5, -0.4, 'longitude [$^\circ$]', fontsize=10, va='bottom', ha='center',
#          rotation='horizontal', rotation_mode='anchor',
#          transform=ax.transAxes)

# adjust the axis labels and ticks
ax.xaxis.labelpad = 30
ax.yaxis.labelpad = 30
ax.tick_params(labelsize=10)

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "f", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#-------------------------------------
# (Vertical profile - HYSPLIT back trajectory)
ax = fig.add_subplot(gs[-1:,-1]) # options graph 2 (vertical no, horizontal no, graph no)

# Plot axis lines for height
plt.axhline(500,  linewidth=0.5, color='k')
plt.axhline(1000, linewidth=0.5, color='k')
plt.axhline(1500, linewidth=0.5, color='k')
plt.axhline(2000, linewidth=0.5, color='k')
plt.axhline(2500, linewidth=0.5, color='k')
plt.axhline(3000, linewidth=0.5, color='k')

# Plot axis lines for age
plt.axvline(0,    linewidth=0.5, color='k')
plt.axvline(-20,  linewidth=0.5, color='k')
plt.axvline(-40,  linewidth=0.5, color='k')
plt.axvline(-60,  linewidth=0.5, color='k')
plt.axvline(-80,  linewidth=0.5, color='k')
plt.axvline(-100, linewidth=0.5, color='k')
plt.axvline(-120, linewidth=0.5, color='k')

# Back trajectory altitude
cmap=plt.cm.autumn_r
#norm = BoundaryNorm(np.arange(-120,0,10), cmap.N)
norm = BoundaryNorm(np.arange(0,90,10), cmap.N)

#cs1 = ax.scatter(Traj['Traj Age'], Traj['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj['Traj Age'], label='Traj Height (m)')
cs1 = ax.scatter(Traj_E8['Traj Age'], Traj_E8['Traj Height (m)'], marker='o', s=1, cmap=cmap, norm=norm, c=Traj_E8['IceContact_100m'], label='Traj Height (m)')
ax.plot(Traj_E8['Traj Age'][0], Traj_E8['Traj Height (m)'][0], color='k', marker='*')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
#ax.set_xlim(,0)

# Format y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.set_ylim(0,)
ax.set_xlim(5,-125)
# Plot axis labels & title
#plt.title("Back trajectory height", y=1.1, fontsize=20)
ax.set_xlabel('Age (hours)', fontsize=10)
ax.set_ylabel('Height (MSL)', fontsize=10)

# Format ColorBar
#clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,-20,-40,-60,-80,-100,-120])#, pad = 0.2, extend='max')
#clb1.set_label('Age (hours)')#, rotation=90)
clb1 = fig.colorbar(cs1, ax=ax, ticks=[0,10,20,30,40,50,60,70,80,90])#, pad = 0.2, extend='max')
clb1.set_label('Ice contact time below 100m (hours)')#, rotation=90)

# Set the background color for the plot
ax.set_facecolor('lightgrey')

# Text box in upper left
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
ax.text(0.025, 0.925, "g", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)


