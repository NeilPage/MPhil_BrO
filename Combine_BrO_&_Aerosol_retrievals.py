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

## AEROSOLS
# CAMMPCAN
#path =r'/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/Aerosol_Retrieval_V3/all_aero' # use your path
# SIPEXII
path =r'/Users/ncp532/Documents/Data/SIPEXII_2012/Aerosol_Retrieval/all_aero' # use your path
allFiles = glob.glob(path + "/retrieval_201*.dat")

list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_, sep='\s+', index_col=None, header=0)
    list_.append(df)

V1_Aero = pd.concat(list_, axis = 0, ignore_index = True)

# BrO
# Combine all the seperate .dat files into a single dataframe called V1_2018_19
# CAMMPCAN
#path =r'/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V3/all_BrO' # use your path
path =r'/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII/all_BrO' # a-priori test1
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_65_1_Test2/all_BrO' # a-priori test2
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_65_1_Test3/all_BrO' # a-priori test3
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_65_1_Test4/all_BrO' # a-priori test4
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_65_1_Test8/all_BrO' # a-priori test5
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_65_1_Test6/all_BrO' # a-priori test6
#path =r'/Users/ncp532/Documents/Data/V1_17_APriori/V1_65_1_Test7/all_BrO' # a-priori test7

# SIPEXII
#path =r'/Users/ncp532/Documents/Data/SIPEXII_2012/BrO_Retrieval/all_BrO' # use your path
allFiles = glob.glob(path + "/BrO_retrieval_201*.dat")

list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_, sep='\s+', index_col=None, header=0)
    list_.append(df)

V1_BrO = pd.concat(list_, axis = 0, ignore_index = True)

# NO2
## Combine all the seperate .dat files into a single dataframe called V1_2018_19
#path =r'/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V3/all_NO2' # use your path
#allFiles = glob.glob(path + "/NO2_retrieval_201*.dat")
#
#list_ = []
#
#for file_ in allFiles:
#    df = pd.read_csv(file_, sep='\s+', index_col=None, header=0)
#    list_.append(df)
#
#V1_NO2 = pd.concat(list_, axis = 0, ignore_index = True)

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

# AEROSOLS
dat1 = np.array(V1_Aero['Date'])
tim1 = np.array(V1_Aero['Time'])
dattim1 =dat1+' '+tim1

# CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    date1.append(datetime.strptime(dattim1[i],'%d/%m/%Y %H:%M:%S'))

# CONVERT TO A PANDAS DATAFRAME
Date1 = pd.DataFrame(date1)

#-----------------------------------

# BrO
dat2 = np.array(V1_BrO['Date'])
tim2 = np.array(V1_BrO['Time'])
dattim2 =dat2+' '+tim2

# CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S'))

# CONVERT TO A PANDAS DATAFRAME
Date2 = pd.DataFrame(date2)

#-----------------------------------

# NO2
#dat3 = np.array(V1_NO2['Date'])
#tim3 = np.array(V1_NO2['Time'])
#dattim3 =dat3+' '+tim3
#
## CONVERT TO DATETIME FROM STRING
#date3=[]
#for i in range(len(dattim3)):
#    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S'))
#
## CONVERT TO A PANDAS DATAFRAME
#Date3 = pd.DataFrame(date3)

#------------------------------------------------------------------------------
# ADD THE DATETIME COLUMN TO THE DATASETS

# AEROSOLS
X=V1_Aero.assign(DateTime = Date1)

# BrO
Y=V1_BrO.assign(DateTime = Date2)

# NO2
#Z=V1_NO2.assign(DateTime = Date3)

# Make new datasets (Data4 & Data5) with only the shared rows corresponding to DT
Data4 = pd.merge(left=Y,right=X, how='left', left_on='DateTime', right_on='DateTime') # BrO
#Data5 = pd.merge(left=Z,right=X, how='left', left_on='DateTime', right_on='DateTime') # NO2    

#------------------------------------------------------------------------------
# write the pandas dataframe to a .csv file
Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII.csv') # test1
#Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test2.csv') # Test 2
#Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test3.csv') # Test 3
#Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test4.csv') # Test 4
#Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test8.csv') # Test 5
#Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test6.csv') # Test 6
#Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test7.csv') # Test 7
#Data5.to_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_NO2.csv') # NO2
