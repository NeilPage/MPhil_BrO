#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:25:58 2019

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
# OBSERVATIONS
# Retrieve the observational data

#------------------
# CAMMPCAN
#------------------
#path =r'/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V3/all_BrO' # use your path
#path =r'/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V3/all_BrO' # use your path
path =r'/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII/all_BrO' # use your path
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V3_18/all_Aerosol' # use your path
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII/all_Aerosol' # use your path

#------------------
# SIPEXII
#path =r'/Users/ncp532/Documents/Data/SIPEXII_2012/BrO_Retrieval/all_BrO' # use your path
#------------------

#allFiles = glob.glob(path + "/all_BrO_vmr_prof_201*.dat")
#allFiles = glob.glob(path + "/all_NO2_vmr_prof_errs_201*.dat")
#allFiles = glob.glob(path + "/all_aer_ext_wl_360_201*.dat")
allFiles = glob.glob(path + "/BrO_retrieval_201*.dat")
#allFiles = glob.glob(path + "/aer_param_375_201*.dat")

list_ = []

for file_ in allFiles:
    
    #fdate=datetime.strptime(file_,'/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII/all_AOD/aer_param_375_%Y%m%d.dat')
    #fdate=datetime.strptime(file_,'/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII/all_NO2/NO2_retrieval_%Y%m%d.dat')
    #fdate=datetime.strptime(file_,'/Users/ncp532/Documents/Data/V1_17_APriori/V3_18/all_Aerosol/all_aer_ext_wl_360_%Y%m%d.dat')
    #fdate=datetime.strptime(file_,'/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII/all_Aerosol/all_aer_ext_wl_360_%Y%m%d.dat')
    
    df = pd.read_csv(file_, sep='\s+', index_col=None, header=None)
    #df = pd.read_csv(file_, sep='\s+', index_col=0, header=None, skiprows=1).T
    
#    df['altitude'] = s
#    cols = list(df.columns)
#    cols = [cols[-1]] + cols[:-1]
#    df = df[cols]
    #df['Date']=fdate
    #cols = list(df.columns)
    #cols = [cols[-1]] + cols[:-1]
    #df = df[cols]
    
    list_.append(df)

BrO_VMR = pd.concat(list_, axis = 0, ignore_index = True)

#------------------------------------------------------------------------------
# write the pandas dataframe to a .csv file
#BrO_VMR.to_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/BrO_VMR.csv')
#BrO_VMR.to_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_VMR_V3.csv')
#BrO_VMR.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V3_18/all_Aerosol/V3_18_AeroExt_wl_360.csv')
BrO_VMR.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_retrieval.csv')
