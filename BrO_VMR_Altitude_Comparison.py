#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:23:17 2018

@author: ncp532
"""

# File system packages
from netCDF4 import Dataset				# function used to open single netcdf file
from netCDF4 import MFDataset				# function used to open multiple netcdf files

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd
from scipy import signal, stats
import glob

# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# Define the datasets

# SIMULATIONS
# Retrieve the model simulation data

#dataset1a = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_Dynamic_Ocean/GEOSChem.SpeciesConc.2013*.nc4') # Dynamic Ocean Hg Data
#dataset1b = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_Dynamic_Ocean/GEOSChem.StateMet.2013*.nc4') # Dynamic Ocean Met Data
#dataset2a = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_Offline_Ocean/GEOSChem.SpeciesConc.2013*.nc4') # Offline Ocean Hg Data
#dataset2b = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_Offline_Ocean/GEOSChem.StateMet.2013*.nc4') # Offline Ocean Met Data
#dataset3  = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_Default_Files/trac_avg.2013.nc')  # Default
#dataset4  = MFDataset('/Users/ncp532/Documents/Some_scripts_/nc_InvOcean_Files/trac_avg.2013.nc') # InvOcean

# OBSERVATIONS
# Retrieve the observational data

# FOR FILE 'all_BrO_vmr_prof_2012*.dat'
# Combine all the seperate .dat files into a single dataframe called SIPEXII
path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_17/all_NO2/' # use your path
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_17/all_Aerosol/' # use your path

allFiles = glob.glob(path + "/all_NO2_vmr_prof_201*.dat") # BrO and NO2
#allFiles = glob.glob(path + "/aer_param_375_201*.dat") # AOD 338 and 375
#allFiles = glob.glob(path + "/meas_201*.dat") # SZA
#allFiles = glob.glob(path + "/all_aer_ext_338_201*.dat") # Aerosol Ext at 338 (BrO) and 375 (NO2)

list_ = []

# Not that theres no date in this files, so need to add date.
# also the script below appends on the y-axis, for this i need to append on the x-axis.
for file_ in allFiles:
    #print file_
    
    fdate=datetime.strptime(file_,'/Users/ncp532/Documents/Data/V1_17_APriori/V1_17/all_NO2/all_NO2_vmr_prof_%Y%m%d.dat')
    #fdate=datetime.strptime(file_,'/Users/ncp532/Documents/Data/V1_17_APriori/V1_17/all_Aerosol/all_aer_ext_338_%Y%m%d.dat')
    
    df = pd.read_csv(file_, sep='\s+', index_col=0, header=None).T # BrO and NO2
    #df = pd.read_csv(file_, sep='\s+') # SZA
    #df['Date']=fdate
    ftime=datetime.strptime(df['altitude'], '%H:%M:%S')
    df['altitude'] = df['altitude'] + fdate
    list_.append(df)

SIPEX_II = pd.concat(list_, axis = 0, ignore_index = False)

SIPEX_II.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17/all_AOD/V1_17_AeroExt_338.csv')

#SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEX_II_BrO/all_BrO_vmr_2012.csv', index_col=0)
##------------------------------------------------------------------------------
## SET THE DATE AND TIME
#dattim = np.array(SIPEXII.index)
#
##CONVERT TO DATETIME FROM STRING
#date=[]
#for i in range(len(dattim)):
#    date.append(datetime.strptime(dattim[i],'%d/%m/%Y %H:%M:%S'))
#
##------------------------------------------------------------------------------
## SET UP THE VALUES TO PLOT
#
## BrO volume mixing ratio (VMR)
#z = SIPEXII.copy() # identify the matrix containing the z-values (BrO in ppMv)
#z[z==-9999]=np.nan # set the erroneous values as NaN 
#z = z.loc[:]*1e6 # change from ppMv to ppTv
#
#surface = z['0.1']
#one = z['1.1']
#one_5 = z['1.5']
#two = z['2.1']
#
##------------------------------------------------------------------------------
## Plot the axis for each graph
#fig = plt.figure()
#plt.subplots_adjust(hspace=0.5)
#
## Graph 1
#ax=plt.subplot(111) # options graph 1 (vertical no, horizontal no, graph no)
#
## OBSERVATIONS
## Plot the observations for the location
##plt.plot(datea,y1, 'k', linewidth=2, label="Observations")
#
## SIMULATIONS
## Plot the modelling simulations for each location
#plt.plot(date, surface, marker='o', markerfacecolor='none', color='red', linestyle='none', label= 'Surface') # VMR at surface
##plt.plot(date, one, marker='o', markerfacecolor='none', color='magenta', linestyle='none', label = '1km') # VMR at 1km
##plt.plot(date, one_5, marker='o', markerfacecolor='none', color='green', linestyle='none', label = '1.5km') # VMR at 1.5km
#plt.plot(date, two, marker='o', markerfacecolor='none', color='blue', linestyle='none', label ='2km') # VMR at 2km
#    
##plt.xlim(datetime(2013,1,1),datetime(2013,12,31)) # set the date limits
##plt.xticks(rotation=35)
#xmajor_formatter = mdates.DateFormatter('%b %Y') # format how the date is displayed
#ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
#ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # set the interval between dispalyed dates
#ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax.tick_params(pad=20, labelsize=15)
#plt.tick_params(which='minor', labelsize=13)
#
## Plot the axis labels, legend and title
#plt.ylabel('BrO VMR (pptv)', fontsize=20)
#plt.xlabel('Date', fontsize=20)
#plt.title("BrO VMR (SIPEXII)", fontsize=25)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, fontsize=20, borderaxespad=0.)
