#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:55:26 2019

@author: ncp532
"""

# Date and Time handling package
from datetime import datetime,time,timedelta		# functions to handle date and time

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname

# Data handing packages
import numpy as np                          # import package as shorter nickname - Numpy is great at handling multidimensional data arrays.
import pandas as pd

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
V1_17   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_17_Data.csv',   header=0, encoding = 'unicode_escape') # BrO data for CAMPCANN V1 (2017/18)
V2_17   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_17_Data.csv',   header=0, encoding = 'unicode_escape') # BrO data for CAMPCANN V2 (2017/18)
V3_17   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_17_Data.csv',   header=0, encoding = 'unicode_escape') # BrO data for CAMPCANN V3 (2017/18)
V1_18   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V1_18_Data.csv',   header=0, encoding = 'unicode_escape') # BrO data for CAMPCANN V1 (2018/19)
V2_18   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V2_18_Data.csv',   header=0, encoding = 'unicode_escape') # BrO data for CAMPCANN V2 (2018/19)
V3_18   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/V3_18_Data.csv',   header=0, encoding = 'unicode_escape') # BrO data for CAMPCANN V3 (2018/19)
SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/SIPEXII_Data.csv', header=0, encoding = 'unicode_escape') # BrO data for SIPEXII (2012)

#---------
# SZA
#---------
DF1_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_17/all_SZA/V1_17_SZA.csv') # SZA data for CAMPCANN V1 (2017/18)
DF2_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_17/all_SZA/V2_17_SZA.csv') # SZA data for CAMPCANN V2 (2017/18)
DF3_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_17/all_SZA/V3_17_SZA.csv') # SZA data for CAMPCANN V3 (2017/18)
DF4_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V1_18/all_SZA/V1_18_SZA.csv') # SZA data for CAMPCANN V1 (2018/19)
DF5_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V2_18/all_SZA/V2_18_SZA.csv') # SZA data for CAMPCANN V2 (2018/19)
DF6_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/V3_18/all_SZA/V3_18_SZA.csv') # SZA data for CAMPCANN V3 (2018/19)
DF7_SZA = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_SZA/SIPEXII_SZA.csv') # SZA data for SIPEXII (2012)

#------------------------------------------------------------------------------
# Set the date

#---------
# BrO
#---------
V1_17['DateTime']   = pd.to_datetime(V1_17['DateTime']) # Davis timezone is UT+7
V2_17['DateTime']   = pd.to_datetime(V2_17['DateTime']) # Casey timezone is UT+8
V3_17['DateTime']   = pd.to_datetime(V3_17['DateTime']) # Mawson timezone is UT+5
V1_18['DateTime']   = pd.to_datetime(V1_18['DateTime']) # Davis timezone is UT+7
V2_18['DateTime']   = pd.to_datetime(V2_18['DateTime']) # Casey timezone is UT+8
V3_18['DateTime']   = pd.to_datetime(V3_18['DateTime']) # Mawson timezone is UT+5
SIPEXII['DateTime'] = pd.to_datetime(SIPEXII['DateTime']) # SIPEXII timezone is UT+5

#---------
# SZA
#---------
DF1_SZA['DateTime'] = pd.to_datetime(DF1_SZA['DateTime']) + timedelta(hours=7) # Davis timezone is UT+7
DF2_SZA['DateTime'] = pd.to_datetime(DF2_SZA['DateTime']) + timedelta(hours=8) # Casey timezone is UT+8
DF3_SZA['DateTime'] = pd.to_datetime(DF3_SZA['DateTime']) + timedelta(hours=5) # Mawson timezone is UT+5
DF4_SZA['DateTime'] = pd.to_datetime(DF4_SZA['DateTime']) + timedelta(hours=7) # Davis timezone is UT+7
DF5_SZA['DateTime'] = pd.to_datetime(DF5_SZA['DateTime']) + timedelta(hours=8) # Casey timezone is UT+8
DF6_SZA['DateTime'] = pd.to_datetime(DF6_SZA['DateTime']) + timedelta(hours=5) # Mawson timezone is UT+5
DF7_SZA['DateTime'] = pd.to_datetime(DF7_SZA['DateTime']) + timedelta(hours=8) # SIPEXII timezone is UT+8

DF1_SZA['Time'] = pd.to_datetime(DF1_SZA['Time']) + timedelta(hours=7) # Davis timezone is UT+7
DF2_SZA['Time'] = pd.to_datetime(DF2_SZA['Time']) + timedelta(hours=8) # Casey timezone is UT+8
DF3_SZA['Time'] = pd.to_datetime(DF3_SZA['Time']) + timedelta(hours=5) # Mawson timezone is UT+5
DF4_SZA['Time'] = pd.to_datetime(DF4_SZA['Time']) + timedelta(hours=7) # Davis timezone is UT+7
DF5_SZA['Time'] = pd.to_datetime(DF5_SZA['Time']) + timedelta(hours=8) # Casey timezone is UT+8
DF6_SZA['Time'] = pd.to_datetime(DF6_SZA['Time']) + timedelta(hours=5) # Mawson timezone is UT+5
DF7_SZA['Time'] = pd.to_datetime(DF7_SZA['Time']) + timedelta(hours=8) # SIPEXII timezone is UT+8

DF1_SZA['Time'] = DF1_SZA['Time'].apply(lambda dt: dt.replace(year=1900,month=1,day=1))
DF2_SZA['Time'] = DF2_SZA['Time'].apply(lambda dt: dt.replace(year=1900,month=1,day=1))
DF3_SZA['Time'] = DF3_SZA['Time'].apply(lambda dt: dt.replace(year=1900,month=1,day=1))
DF4_SZA['Time'] = DF4_SZA['Time'].apply(lambda dt: dt.replace(year=1900,month=1,day=1))
DF5_SZA['Time'] = DF5_SZA['Time'].apply(lambda dt: dt.replace(year=1900,month=1,day=1))
DF6_SZA['Time'] = DF6_SZA['Time'].apply(lambda dt: dt.replace(year=1900,month=1,day=1))
DF7_SZA['Time'] = DF7_SZA['Time'].apply(lambda dt: dt.replace(year=1900,month=1,day=1))

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

V1_17F   = (V1_17['Filter'] < 0.6)
V1_17T   = V1_17[V1_17F]

V2_17F   = (V2_17['Filter'] < 0.6)
V2_17T   = V2_17[V2_17F]

V3_17F   = (V3_17['Filter'] < 0.6)
V3_17T   = V3_17[V3_17F]

V1_18F   = (V1_18['Filter'] < 0.6)
V1_18T   = V1_18[V1_18F]

V2_18F   = (V2_18['Filter'] < 0.6)
V2_18T   = V2_18[V2_18F]

V3_18F   = (V3_18['Filter'] < 0.6)
V3_18T   = V3_18[V3_18F]

SIPEXIIF = (SIPEXII['Filter'] < 0.6)
SIPEXIIT = SIPEXII[SIPEXIIF]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

#---------
# BrO
#---------
# V1_17 Davis (14-22 Nov 2017)
start_date   = '2017-11-14'
end_date     = '2017-11-23'
Davis        = (V1_17T['DateTime'] >= start_date) & (V1_17T['DateTime'] < end_date)
V1_17_Davis  = V1_17T[Davis]

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1  = '2017-12-21'
end_date1    = '2017-12-23'
start_date2  = '2017-12-26'
end_date2    = '2018-01-6'
Casey1       = (V2_17T['DateTime'] >= start_date1) & (V2_17T['DateTime'] < end_date1)
Casey2       = (V2_17T['DateTime'] >= start_date2) & (V2_17T['DateTime'] < end_date2)
V2_17_Casey1 = V2_17T[Casey1]
V2_17_Casey2 = V2_17T[Casey2]
V2_17_Casey  = pd.concat([V2_17_Casey1,V2_17_Casey2], axis =0)

# V3_17 Mawson (1-17 Feb 2018)
start_date   = '2018-02-01'
end_date     = '2018-02-18'
Mawson       = (V3_17T['DateTime'] >= start_date) & (V3_17T['DateTime'] < end_date)
V3_17_Mawson = V3_17T[Mawson]

# V1_18 Davis (7-15 Nov 2018)
start_date   = '2018-11-07'
end_date     = '2018-11-16'
Davis        = (V1_18T['DateTime'] >= start_date) & (V1_18T['DateTime'] < end_date)
V1_18_Davis  = V1_18T[Davis]

# V2_18 Casey (15-30 Dec 2018)
start_date   = '2018-12-15'
end_date     = '2018-12-31'
Casey        = (V2_18T['DateTime'] >= start_date) & (V2_18T['DateTime'] < end_date)
V2_18_Casey  = V2_18T[Casey]

# V3_18 Mawson (30 Jan - 9 Feb 2019)
start_date   = '2019-01-30'
end_date     = '2019-02-10'
Mawson       = (V3_18T['DateTime'] >= start_date) & (V3_18T['DateTime'] < end_date)
V3_18_Mawson = V3_18T[Mawson]

# SIPEXII (23 Sep - 11 Nov)
start_date   = '2012-09-23'
end_date     = '2012-11-11'
SIPII        = (SIPEXIIT['DateTime'] >= start_date) & (SIPEXIIT['DateTime'] < end_date)
SIPEXII_Ice  = SIPEXIIT[SIPII]

#---------
# SZA
#---------
# V1_17 Davis (14-22 Nov 2017)
start_date   = '2017-11-14'
end_date     = '2017-11-23'
Davis        = (DF1_SZA['DateTime'] >= start_date) & (DF1_SZA['DateTime'] < end_date)
SZA_1        = DF1_SZA[Davis]

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1  = '2017-12-21'
end_date1    = '2017-12-23'
start_date2  = '2017-12-26'
end_date2    = '2018-01-6'
Casey1       = (DF2_SZA['DateTime'] >= start_date1) & (DF2_SZA['DateTime'] < end_date1)
Casey2       = (DF2_SZA['DateTime'] >= start_date2) & (DF2_SZA['DateTime'] < end_date2)
V2_17_Casey1 = DF2_SZA[Casey1]
V2_17_Casey2 = DF2_SZA[Casey2]
SZA_2        = pd.concat([V2_17_Casey1,V2_17_Casey2], axis =0)

# V3_17 Mawson (1-17 Feb 2018)
start_date   = '2018-02-01'
end_date     = '2018-02-18'
Mawson       = (DF3_SZA['DateTime'] >= start_date) & (DF3_SZA['DateTime'] < end_date)
SZA_3        = DF3_SZA[Mawson]

# V1_18 Davis (7-15 Nov 2018)
start_date   = '2018-11-07'
end_date     = '2018-11-16'
Davis        = (DF4_SZA['DateTime'] >= start_date) & (DF4_SZA['DateTime'] < end_date)
SZA_4        = DF4_SZA[Davis]

# V2_18 Casey (15-30 Dec 2018)
start_date   = '2018-12-15'
end_date     = '2018-12-31'
Casey        = (DF5_SZA['DateTime'] >= start_date) & (DF5_SZA['DateTime'] < end_date)
SZA_5        = DF5_SZA[Casey]

# V3_18 Mawson (30 Jan - 9 Feb 2019)
start_date   = '2019-01-30'
end_date     = '2019-02-10'
Mawson       = (DF6_SZA['DateTime'] >= start_date) & (DF6_SZA['DateTime'] < end_date)
SZA_6        = DF6_SZA[Mawson]

# SIPEXII (23 Sep - 11 Nov)
start_date   = '2012-09-23'
end_date     = '2012-11-11'
SIPII        = (DF7_SZA['DateTime'] >= start_date) & (DF7_SZA['DateTime'] < end_date)
SZA_7        = DF7_SZA[SIPII]

#------------------------------------------------------------------------------
# Define the variables

#---------
# BrO
#---------
BrO_V1_17   = np.array(V1_17_Davis['surf_vmr(ppmv)'])* 1e6
BrO_V2_17   = np.array(V2_17_Casey['surf_vmr(ppmv)'])* 1e6
BrO_V3_17   = np.array(V3_17_Mawson['surf_vmr(ppmv)'])* 1e6
BrO_V1_18   = np.array(V1_18_Davis['surf_vmr(ppmv)'])* 1e6
BrO_V2_18   = np.array(V2_18_Casey['surf_vmr(ppmv)'])* 1e6
BrO_V3_18   = np.array(V3_18_Mawson['surf_vmr(ppmv)'])* 1e6
BrO_SIPEXII = np.array(SIPEXII_Ice['surf_vmr(ppmv)'])* 1e6

#---------
# SZA
#---------
SZA_V1_17   = np.array(SZA_1['SZA'])
SZA_V2_17   = np.array(SZA_2['SZA'])
SZA_V3_17   = np.array(SZA_3['SZA'])
SZA_V1_18   = np.array(SZA_4['SZA'])
SZA_V2_18   = np.array(SZA_5['SZA'])
SZA_V3_18   = np.array(SZA_6['SZA'])
SZA_SIPEXII = np.array(SZA_7['SZA'])

#------------------------------------------------------------------------------
# SET THE DATE AND TIME
#------------------------------------

#---------
# BrO
#---------

# V1_17
tim1 = np.array(V1_17_Davis['Time']) # Davis timezone is UT+7
#CONVERT TO DATETIME FROM STRING
time1=[]
for i in range(len(tim1)):
    time1.append(datetime.strptime(tim1[i],'%H:%M:%S'))#+ timedelta(hours=7)).replace(day=1))

# V2_17
tim2 = np.array(V2_17_Casey['Time']) # Casey timezone is UT+8

#CONVERT TO DATETIME FROM STRING
time2=[]
for i in range(len(tim2)):
    time2.append(datetime.strptime(tim2[i],'%H:%M:%S'))#+ timedelta(hours=8)).replace(day=1))

# V3_17
tim3 = np.array(V3_17_Mawson['Time']) # Mawson timezone is UT+5

#CONVERT TO DATETIME FROM STRING
time3=[]
for i in range(len(tim3)):
    time3.append(datetime.strptime(tim3[i],'%H:%M:%S'))#+ timedelta(hours=5)).replace(day=1))

# V1_18
tim4 = np.array(V1_18_Davis['Time']) # Davis timezone is UT+7

#CONVERT TO DATETIME FROM STRING
time4=[]
for i in range(len(tim4)):
    time4.append(datetime.strptime(tim4[i],'%H:%M:%S'))#+ timedelta(hours=7)).replace(day=1))

# V2_18
tim5 = np.array(V2_18_Casey['Time']) # Casey timezone is UT+8

#CONVERT TO DATETIME FROM STRING
time5=[]
for i in range(len(tim5)):
    time5.append(datetime.strptime(tim5[i],'%H:%M:%S'))#+ timedelta(hours=8)).replace(day=1))

# V3_18
tim6 = np.array(V3_18_Mawson['Time']) # Mawson timezone is UT+5

#CONVERT TO DATETIME FROM STRING
time6=[]
for i in range(len(tim6)):
    time6.append(datetime.strptime(tim6[i],'%H:%M:%S'))#+ timedelta(hours=5)).replace(day=1))

# SIPEXII
tim7 = np.array(SIPEXII_Ice['Time']) # SIPEXII timezone is UT+8

#CONVERT TO DATETIME FROM STRING
time7=[]
for i in range(len(tim7)):
    time7.append(datetime.strptime(tim7[i],'%H:%M:%S'))#+ timedelta(hours=8)).replace(day=1))

#---------
# SZA
#---------

time1_SZA = np.array(SZA_1['Time']) # V1_17
time2_SZA = np.array(SZA_2['Time']) # V2_17
time3_SZA = np.array(SZA_3['Time']) # V3_17
time4_SZA = np.array(SZA_4['Time']) # V1_18
time5_SZA = np.array(SZA_5['Time']) # V2_18
time6_SZA = np.array(SZA_6['Time']) # V3_18
time7_SZA = np.array(SZA_7['Time']) # SIPEXII
    
#------------------------------------------------------------------------------
# CALCULATE A MEAN BRO CONCENTRATION FOR EACH HOUR OF THE DAY
    
# Function to calculate the hourly mean
def hourlyM(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').mean()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Daily Means
BrO_V1_17_HM,   time1_HM = hourlyM(BrO_V1_17[:],   time1) # V1_17
BrO_V2_17_HM,   time2_HM = hourlyM(BrO_V2_17[:],   time2) # V2_17
BrO_V3_17_HM,   time3_HM = hourlyM(BrO_V3_17[:],   time3) # V3_17
BrO_V1_18_HM,   time4_HM = hourlyM(BrO_V1_18[:],   time4) # V1_18
BrO_V2_18_HM,   time5_HM = hourlyM(BrO_V2_18[:],   time5) # V2_18
BrO_V3_18_HM,   time6_HM = hourlyM(BrO_V3_18[:],   time6) # V3_18
BrO_SIPEXII_HM, time7_HM = hourlyM(BrO_SIPEXII[:], time7) # SIPEXII

# SZA Daily Means
SZA_V1_17_HM,   time1_SZA_HM = hourlyM(SZA_V1_17[:],   time1_SZA) # V1_17
SZA_V2_17_HM,   time2_SZA_HM = hourlyM(SZA_V2_17[:],   time2_SZA) # V2_17
SZA_V3_17_HM,   time3_SZA_HM = hourlyM(SZA_V3_17[:],   time3_SZA) # V3_17
SZA_V1_18_HM,   time4_SZA_HM = hourlyM(SZA_V1_18[:],   time4_SZA) # V1_18
SZA_V2_18_HM,   time5_SZA_HM = hourlyM(SZA_V2_18[:],   time5_SZA) # V2_18
SZA_V3_18_HM,   time6_SZA_HM = hourlyM(SZA_V3_18[:],   time6_SZA) # V3_18
SZA_SIPEXII_HM, time7_SZA_HM = hourlyM(SZA_SIPEXII[:], time7_SZA) # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE A MEDIAN BRO CONCENTRATION FOR EACH HOUR OF THE DAY
    
# Function to calculate the hourly median
def hourlyMed(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').median()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Daily Medians
BrO_V1_17_HMed,   time1_HMed = hourlyMed(BrO_V1_17[:],   time1) # V1_17
BrO_V2_17_HMed,   time2_HMed = hourlyMed(BrO_V2_17[:],   time2) # V2_17
BrO_V3_17_HMed,   time3_HMed = hourlyMed(BrO_V3_17[:],   time3) # V3_17
BrO_V1_18_HMed,   time4_HMed = hourlyMed(BrO_V1_18[:],   time4) # V1_18
BrO_V2_18_HMed,   time5_HMed = hourlyMed(BrO_V2_18[:],   time5) # V2_18
BrO_V3_18_HMed,   time6_HMed = hourlyMed(BrO_V3_18[:],   time6) # V3_18
BrO_SIPEXII_HMed, time7_HMed = hourlyMed(BrO_SIPEXII[:], time7) # SIPEXII

# SZA Daily Medians
SZA_V1_17_HMed,   time1_SZA_HMed = hourlyMed(SZA_V1_17[:],   time1_SZA) # V1_17
SZA_V2_17_HMed,   time2_SZA_HMed = hourlyMed(SZA_V2_17[:],   time2_SZA) # V2_17
SZA_V3_17_HMed,   time3_SZA_HMed = hourlyMed(SZA_V3_17[:],   time3_SZA) # V3_17
SZA_V1_18_HMed,   time4_SZA_HMed = hourlyMed(SZA_V1_18[:],   time4_SZA) # V1_18
SZA_V2_18_HMed,   time5_SZA_HMed = hourlyMed(SZA_V2_18[:],   time5_SZA) # V2_18
SZA_V3_18_HMed,   time6_SZA_HMed = hourlyMed(SZA_V3_18[:],   time6_SZA) # V3_18
SZA_SIPEXII_HMed, time7_SZA_HMed = hourlyMed(SZA_SIPEXII[:], time7_SZA) # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE THE STANDARD DEVIATION FOR THE BRO DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def hourlySTD(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('H').std()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Standard Deviations
BrO_V1_17_STD,   date1_STD = hourlySTD(BrO_V1_17[:],   time1) # V1_17
BrO_V2_17_STD,   date2_STD = hourlySTD(BrO_V2_17[:],   time2) # V2_17
BrO_V3_17_STD,   date3_STD = hourlySTD(BrO_V3_17[:],   time3) # V3_17
BrO_V1_18_STD,   date4_STD = hourlySTD(BrO_V1_18[:],   time4) # V1_18
BrO_V2_18_STD,   date5_STD = hourlySTD(BrO_V2_18[:],   time5) # V2_18
BrO_V3_18_STD,   date6_STD = hourlySTD(BrO_V3_18[:],   time6) # V3_18
BrO_SIPEXII_STD, date7_STD = hourlySTD(BrO_SIPEXII[:], time7) # SIPEXII

# SZA Standard Deviations
SZA_V1_17_STD,   time1_SZA_STD = hourlySTD(SZA_V1_17[:],   time1_SZA) # V1_17
SZA_V2_17_STD,   time2_SZA_STD = hourlySTD(SZA_V2_17[:],   time2_SZA) # V2_17
SZA_V3_17_STD,   time3_SZA_STD = hourlySTD(SZA_V3_17[:],   time3_SZA) # V3_17
SZA_V1_18_STD,   time4_SZA_STD = hourlySTD(SZA_V1_18[:],   time4_SZA) # V1_18
SZA_V2_18_STD,   time5_SZA_STD = hourlySTD(SZA_V2_18[:],   time5_SZA) # V2_18
SZA_V3_18_STD,   time6_SZA_STD = hourlySTD(SZA_V3_18[:],   time6_SZA) # V3_18
SZA_SIPEXII_STD, time7_SZA_STD = hourlySTD(SZA_SIPEXII[:], time7_SZA) # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE THE MEDIAN ABSOLUTE DEVIATION FOR THE BRO DAILY MEDIAN
# MAD = median(| x - median(x)|)

#------------------------------------
# V1_17

# 1) Find the median
V1_17_Davis = V1_17_Davis.set_index('DateTime')
V1_17_Davis.index = V1_17_Davis.index.map(lambda t: t.replace(year=1900, month=1, day=1))
V1_17_Davis = V1_17_Davis.sort_index()
V1_17_MEDIAN = (V1_17_Davis['surf_vmr(ppmv)'].rolling('1h').median())*1e6
# 2) subtract the median from each value in X
V1_17_X = np.array(V1_17_Davis['surf_vmr(ppmv)'])
V1_17_X_M = V1_17_X - V1_17_MEDIAN
# 3) find the absolute value for the difference
V1_17_ABS = V1_17_X_M.abs()
# 4) find the median of the absolute difference
V1_17_MAD = V1_17_ABS.rolling('1h').median()
V1_17_MAD = V1_17_MAD.resample('1h').mean() # convert the MAD to a daily value
V1_17_MAD = np.array(V1_17_MAD[:]) # convert from pandas.df to np.array
V1_17_MAD = V1_17_MAD[~np.isnan(V1_17_MAD)] # drop the nan values

#------------------------------------
# V2_17

# 1) Find the median
V2_17_Casey = V2_17_Casey.set_index('DateTime')
V2_17_Casey.index = V2_17_Casey.index.map(lambda t: t.replace(year=1900, month=1, day=1))
V2_17_Casey = V2_17_Casey.sort_index()
V2_17_MEDIAN = (V2_17_Casey['surf_vmr(ppmv)'].rolling('1h').median())*1e6
# 2) subtract the median from each value in X
V2_17_X = np.array(V2_17_Casey['surf_vmr(ppmv)'])
V2_17_X_M = V2_17_X - V2_17_MEDIAN
# 3) find the absolute value for the difference
V2_17_ABS = V2_17_X_M.abs()
# 4) find the median of the absolute difference
V2_17_MAD = V2_17_ABS.rolling('1h').median()
V2_17_MAD = V2_17_MAD.resample('1h').mean() # convert the MAD to a daily value
V2_17_MAD = np.array(V2_17_MAD[:]) # convert from pandas.df to np.array
V2_17_MAD = V2_17_MAD[~np.isnan(V2_17_MAD)] # drop the nan values

#------------------------------------
# V3_17

# 1) Find the median
V3_17_Mawson = V3_17_Mawson.set_index('DateTime')
V3_17_Mawson.index = V3_17_Mawson.index.map(lambda t: t.replace(year=1900, month=1, day=1))
V3_17_Mawson = V3_17_Mawson.sort_index()
V3_17_MEDIAN = (V3_17_Mawson['surf_vmr(ppmv)'].rolling('1h').median())*1e6
# 2) subtract the median from each value in X
V3_17_X = np.array(V3_17_Mawson['surf_vmr(ppmv)'])
V3_17_X_M = V3_17_X - V3_17_MEDIAN
# 3) find the absolute value for the difference
V3_17_ABS = V3_17_X_M.abs()
# 4) find the median of the absolute difference
V3_17_MAD = V3_17_ABS.rolling('1h').median()
V3_17_MAD = V3_17_MAD.resample('1h').mean() # convert the MAD to a daily value
V3_17_MAD = np.array(V3_17_MAD[:]) # convert from pandas.df to np.array
V3_17_MAD = V3_17_MAD[~np.isnan(V3_17_MAD)] # drop the nan values

#------------------------------------
# V1_18

# 1) Find the median
V1_18_Davis = V1_18_Davis.set_index('DateTime')
V1_18_Davis.index = V1_18_Davis.index.map(lambda t: t.replace(year=1900, month=1, day=1))
V1_18_Davis = V1_18_Davis.sort_index()
V1_18_MEDIAN = (V1_18_Davis['surf_vmr(ppmv)'].rolling('1h').median())*1e6
# 2) subtract the median from each value in X
V1_18_X = np.array(V1_18_Davis['surf_vmr(ppmv)'])
V1_18_X_M = V1_18_X - V1_18_MEDIAN
# 3) find the absolute value for the difference
V1_18_ABS = V1_18_X_M.abs()
# 4) find the median of the absolute difference
V1_18_MAD = V1_18_ABS.rolling('1h').median()
V1_18_MAD = V1_18_MAD.resample('1h').mean() # convert the MAD to a daily value
V1_18_MAD = np.array(V1_18_MAD[:]) # convert from pandas.df to np.array
V1_18_MAD = V1_18_MAD[~np.isnan(V1_18_MAD)] # drop the nan values

#------------------------------------
# V2_18

# 1) Find the median
V2_18_Casey = V2_18_Casey.set_index('DateTime')
V2_18_Casey.index = V2_18_Casey.index.map(lambda t: t.replace(year=1900, month=1, day=1))
V2_18_Casey = V2_18_Casey.sort_index()
V2_18_MEDIAN = (V2_18_Casey['surf_vmr(ppmv)'].rolling('1h').median())*1e6
# 2) subtract the median from each value in X
V2_18_X = np.array(V2_18_Casey['surf_vmr(ppmv)'])
V2_18_X_M = V2_18_X - V2_18_MEDIAN
# 3) find the absolute value for the difference
V2_18_ABS = V2_18_X_M.abs()
# 4) find the median of the absolute difference
V2_18_MAD = V2_18_ABS.rolling('1h').median()
V2_18_MAD = V2_18_MAD.resample('1h').mean() # convert the MAD to a daily value
V2_18_MAD = np.array(V2_18_MAD[:]) # convert from pandas.df to np.array
V2_18_MAD = V2_18_MAD[~np.isnan(V2_18_MAD)] # drop the nan values

#------------------------------------
# V3_18

# 1) Find the median
V3_18_Mawson = V3_18_Mawson.set_index('DateTime')
V3_18_Mawson.index = V3_18_Mawson.index.map(lambda t: t.replace(year=1900, month=1, day=1))
V3_18_Mawson = V3_18_Mawson.sort_index()
V3_18_MEDIAN = (V3_18_Mawson['surf_vmr(ppmv)'].rolling('1h').median())*1e6
# 2) subtract the median from each value in X
V3_18_X = np.array(V3_18_Mawson['surf_vmr(ppmv)'])
V3_18_X_M = V3_18_X - V3_18_MEDIAN
# 3) find the absolute value for the difference
V3_18_ABS = V3_18_X_M.abs()
# 4) find the median of the absolute difference
V3_18_MAD = V3_18_ABS.rolling('1h').median()
V3_18_MAD = V3_18_MAD.resample('1h').mean() # convert the MAD to a daily value
V3_18_MAD = np.array(V3_18_MAD[:]) # convert from pandas.df to np.array
V3_18_MAD = V3_18_MAD[~np.isnan(V3_18_MAD)] # drop the nan values

#------------------------------------
# SIPEXII

# 1) Find the median
SIPEXII_Ice = SIPEXII_Ice.set_index('DateTime')
SIPEXII_Ice.index = SIPEXII_Ice.index.map(lambda t: t.replace(year=1900, month=1, day=1))
SIPEXII_Ice = SIPEXII_Ice.sort_index()
SIPEXII_MEDIAN = (SIPEXII_Ice['surf_vmr(ppmv)'].rolling('1h').median())*1e6
# 2) subtract the median from each value in X
SIPEXII_X = np.array(SIPEXII_Ice['surf_vmr(ppmv)'])
SIPEXII_X_M = SIPEXII_X - SIPEXII_MEDIAN
# 3) find the absolute value for the difference
SIPEXII_ABS = SIPEXII_X_M.abs()
# 4) find the median of the absolute difference
SIPEXII_MAD = SIPEXII_ABS.rolling('1h').median()
SIPEXII_MAD = SIPEXII_MAD.resample('1h').mean() # convert the MAD to a daily value
SIPEXII_MAD = np.array(SIPEXII_MAD[:]) # convert from pandas.df to np.array
SIPEXII_MAD = SIPEXII_MAD[~np.isnan(SIPEXII_MAD)] # drop the nan values

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)
ax.spines["left"].set_color('blue')
ax2 = ax.twinx()
#ax2.spines["right"].set_color('orange')

# Plot the variables
ax.plot(time1_HMed, BrO_V1_17_HMed, marker='o', c='blue', markersize = 3.0, ls='-', label ='Davis (V1)')
ax2.scatter(time1_SZA_HMed, SZA_V1_17_HMed, marker='x', color='Orange')

UL1 = BrO_V1_17_HMed + BrO_V1_17_STD # find the upper limit
LL1 = BrO_V1_17_HMed - BrO_V1_17_STD # find the lower limit
ax.plot(time1_HMed, UL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(time1_HMed, LL1, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(time1_HMed, UL1, LL1, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('blue')
ax.tick_params(axis='y', which='both', colors='blue')
ax.set_ylim(0,10)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange')
ax2.set_ylim(40,100)
ax2.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO (pptv)', fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#ax2.set_ylabel('SZA ($^\circ$)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
#ax2.spines["right"].set_color('orange')

# Plot the variables
ax.plot(time2_HMed, BrO_V2_17_HMed, marker='o', c='blue', markersize = 3.0, ls='-', label ='Casey (V2)')
ax2.scatter(time2_SZA_HMed, SZA_V2_17_HMed, marker='x', color='Orange')

UL2 = BrO_V2_17_HMed + BrO_V2_17_STD # find the upper limit
LL2 = BrO_V2_17_HMed - BrO_V2_17_STD # find the lower limit
ax.plot(time2_HMed, UL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(time2_HMed, LL2, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(time2_HMed, UL2, LL2, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange')
ax2.set_ylim(40,100)
ax2.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#ax2.set_ylabel('SZA ($^\circ$)', fontsize=15)
#Plot the legend and title
plt.title('CAMMPCAN (2017-18)', fontsize=20, y=1.05, color='blue')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax2.spines["right"].set_color('orange')

# Plot the variables
ax.plot(time3_HMed, BrO_V3_17_HMed, marker='o', c='blue', markersize = 3.0, ls='-', label ='Mawson (V3)')
ax2.scatter(time3_SZA_HMed, SZA_V3_17_HMed, marker='x', color='Orange')

UL3 = BrO_V3_17_HMed + BrO_V3_17_STD # find the upper limit
LL3 = BrO_V3_17_HMed - BrO_V3_17_STD # find the lower limit
ax.plot(time3_HMed, UL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(time3_HMed, LL3, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(time3_HMed, UL3, LL3, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange')
ax2.set_ylim(40,100)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
ax2.set_ylabel('SZA ($^\circ$)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)
ax.spines["left"].set_color('red')
ax2 = ax.twinx()
#ax2.spines["right"].set_color('orange')

# Plot the variables
ax.plot(time4_HMed, BrO_V1_18_HMed, marker='o', c='red', markersize = 3.0, ls='-', label ='Davis (V1)')
ax2.scatter(time4_SZA_HMed, SZA_V1_18_HMed, marker='x', color='Orange')

UL4 = BrO_V1_18_HMed + BrO_V1_18_STD # find the upper limit
LL4 = BrO_V1_18_HMed - BrO_V1_18_STD # find the lower limit
ax.plot(time4_HMed, UL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(time4_HMed, LL4, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(time4_HMed, UL4, LL4, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('red')
ax.tick_params(axis='y', which='both', colors='red')
ax.set_ylim(0,10)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange')
ax2.set_ylim(40,100)
ax2.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO (pptv)', fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#ax2.set_ylabel('SZA ($^\circ$)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
#ax2.spines["right"].set_color('orange')

# Plot the variables
ax.plot(time5_HMed, BrO_V2_18_HMed, marker='o', c='red', markersize = 3.0, ls='-', label ='Casey (V2)')
ax2.scatter(time5_SZA_HMed, SZA_V2_18_HMed, marker='x', color='Orange')

UL5 = BrO_V2_18_HMed + BrO_V2_18_STD # find the upper limit
LL5 = BrO_V2_18_HMed - BrO_V2_18_STD # find the lower limit
ax.plot(time5_HMed, UL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(time5_HMed, LL5, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(time5_HMed, UL5, LL5, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange')
ax2.set_ylim(40,100)
ax2.axes.get_yaxis().set_visible(False)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
#ax2.set_ylabel('SZA ($^\circ$)', fontsize=15)
#Plot the legend and title
plt.title('CAMMPCAN (2018-19)', fontsize=20, y=1.05, color='red')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax2.spines["right"].set_color('orange')

# Plot the variables
ax.plot(time6_HMed, BrO_V3_18_HMed, marker='o', c='red', markersize = 3.0, ls='-', label ='Mawson (V3)')
ax2.scatter(time6_SZA_HMed, SZA_V3_18_HMed, marker='x', color='Orange')

UL6 = BrO_V3_18_HMed + BrO_V3_18_STD # find the upper limit
LL6 = BrO_V3_18_HMed - BrO_V3_18_STD # find the lower limit
ax.plot(time6_HMed, UL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(time6_HMed, LL6, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(time6_HMed, UL6, LL6, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,10)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))
ax.axes.get_yaxis().set_visible(False)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange')
ax2.set_ylim(40,100)

# Plot the axis labels, legend and title
#ax.set_ylabel('BrO VMR (pptv)', fontsize=15)
#ax.set_xlabel('Time (hours)', fontsize=15)
ax2.set_ylabel('SZA ($^\circ$)', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 7
ax=plt.subplot(337) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax2.spines["right"].set_color('orange')
ax2.spines["left"].set_color('green')

# Plot the variables
ax.plot(time7_HMed, BrO_SIPEXII_HMed, marker='o', c='green', markersize = 3.0, ls='-', label ='SIPEXII')
ax2.scatter(time7_SZA_HMed, SZA_SIPEXII_HMed, marker='x', color='Orange')

UL7 = BrO_SIPEXII_HMed + BrO_SIPEXII_STD # find the upper limit
LL7 = BrO_SIPEXII_HMed - BrO_SIPEXII_STD # find the lower limit
ax.plot(time7_HMed, UL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(time7_HMed, LL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(time7_HMed, UL7, LL7, facecolor='green', alpha=0.3) # fill the distribution

# Format x-axis
#plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%H') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('green')
ax.tick_params(axis='y', which='both', colors='green')
ax.set_ylim(0,10)
plt.xlim(datetime(1900,1,1,0,1,0),datetime(1900,1,1,23,59,0))

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', which='both', colors='orange')
ax2.set_ylim(40,100)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO (pptv)', fontsize=15)
ax2.set_ylabel('SZA ($^\circ$)', fontsize=15)
ax.set_xlabel('Time (hours)', fontsize=15)
#Plot the legend and title
plt.title('SIPEXII (2012)', fontsize=20, y=1.05, color='green')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

# Custom Legend
custom_lines = [Line2D([0], [0], color='blue',   lw=4),
                Line2D([0], [0], color='red',  lw=4),
                Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='orange',   lw=4)]
fig.legend(custom_lines, ['BrO (CAMMPCAN 2017-18)', 'BrO (CAMMPCAN 2018-19)', 'BrO (SIPEXII)', 'SZA'], loc='upper left', bbox_to_anchor=(0.725, 0.25))
