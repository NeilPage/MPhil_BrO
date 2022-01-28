#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:26:31 2019

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

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# CAMMPCAN 2017-18
#V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V1/V1_BrO_QAQC.csv') # all data
V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_Hourly_Mean/V1_BrO_5am_9pm.csv') # midday data
V1_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv') 
SI_V1_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv')

#V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V2/V2_BrO_QAQC.csv') # all data
V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_Hourly_Mean/V2_BrO_5am_9pm.csv') # midday data
V2_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv') 
SI_V2_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv')

#V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/TG_Retrieval_V3/V3_BrO_QAQC.csv') # all data
V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/BrO_Hourly_Mean/V3_BrO_5am_9pm.csv') # midday data
V3_17_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv') 
SI_V3_17 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv')

# CAMMPCAN 2018-19
#V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V1/V1_BrO_QAQC.csv') # all data
V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_Hourly_Mean/V1_BrO_5am_9pm.csv') # midday data
V1_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv') 
SI_V1_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv')

#V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V2/V2_BrO_QAQC.csv') # all data
V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_Hourly_Mean/V2_BrO_5am_9pm.csv') # midday data
V2_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv') 
SI_V2_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv')

#V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/TG_Retrieval_V3/V3_BrO_QAQC.csv') # all data
V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/BrO_Hourly_Mean/V3_BrO_5am_9pm.csv') # midday data
V3_18_Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv') 
SI_V3_18 = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv')

# SIPEXII 2012
SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_BrO_QAQC.csv')
SIPEXII_Met = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/201213001.csv') #SIPEXII_underway_60.csv') 
SI_SIPEXII = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv')

#------------------------------------------------------------------------------
# Define the variables

# CAMMPCAN (2017-18)
BrO_V1_17 = np.array(V1_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V1_17 = np.array(V1_17_Met['LATITUDE'])
SeaIce_V1_17 = np.array(SI_V1_17['Sea_Ice_Conc'])

BrO_V2_17 = np.array(V2_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V2_17 = np.array(V2_17_Met['LATITUDE'])
SeaIce_V2_17 = np.array(SI_V2_17['Sea_Ice_Conc'])

BrO_V3_17 = np.array(V3_17['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V3_17 = np.array(V3_17_Met['LATITUDE'])
SeaIce_V3_17 = np.array(SI_V3_17['Sea_Ice_Conc'])

# CAMMPCAN (2018-19)
BrO_V1_18 = np.array(V1_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V1_18 = np.array(V1_18_Met['LATITUDE'])
SeaIce_V1_18 = np.array(SI_V1_18['Sea_Ice_Conc'])

BrO_V2_18 = np.array(V2_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V2_18 = np.array(V2_18_Met['LATITUDE'])
SeaIce_V2_18 = np.array(SI_V2_18['Sea_Ice_Conc'])

BrO_V3_18 = np.array(V3_18['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_V3_18 = np.array(V3_18_Met['LATITUDE'])
SeaIce_V3_18 = np.array(SI_V3_18['Sea_Ice_Conc'])

# SIPEXII (2012)
BrO_SIPEXII = np.array(SIPEXII['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
Lat_SIPEXII = np.array(SIPEXII_Met['LATITUDE'])
SeaIce_SIPEXII = np.array(SI_SIPEXII['Sea_Ice_Conc'])

#------------------------------------------------------------------------------
# SET THE DATE AND TIME
#------------------------------------
# V1_17
dattim1 = np.array(V1_17['DateTime'])
#tim1 = np.array(V1_BrO['Time'])
#dattim1 = dat1+' '+tim1

#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    #date1.append(datetime.strptime(dattim1[i],'%Y/%m/%d %H:%M:%S')) # all data
    date1.append(datetime.strptime(dattim1[i],'%d/%m/%Y %H:%M:%S')) # midday data    

# V1_17_Met
datM1 = np.array(V1_17_Met['Date'])
timM1 = np.array(V1_17_Met['Time'])
dattimM1 = datM1+' '+timM1

#CONVERT TO DATETIME FROM STRING
dateM1=[]
for i in range(len(dattimM1)):
    dateM1.append(datetime.strptime(dattimM1[i],'%d/%m/%Y %H:%M:%S'))

# V1_17_SI
datSI1 = np.array(SI_V1_17['Date'])
timSI1 = np.array(SI_V1_17['Time'])
dattimSI1 = datSI1+' '+timSI1

#CONVERT TO DATETIME FROM STRING
dateSI1=[]
for i in range(len(dattimSI1)):
    dateSI1.append(datetime.strptime(dattimSI1[i],'%d/%m/%Y %H:%M:%S'))

#------------------------------------    
# V2_17
dattim2 = np.array(V2_17['DateTime'])
#tim2 = np.array(V2_BrO['Time'])
#dattim2 = dat+2' '+tim2

#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    #date2.append(datetime.strptime(dattim2[i],'%Y/%m/%d %H:%M:%S')) # all data
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V2_17_Met
datM2 = np.array(V2_17_Met['Date'])
timM2 = np.array(V2_17_Met['Time'])
dattimM2 = datM2+' '+timM2

#CONVERT TO DATETIME FROM STRING
dateM2=[]
for i in range(len(dattimM2)):
    dateM2.append(datetime.strptime(dattimM2[i],'%d/%m/%Y %H:%M:%S'))

# V2_17_SI
datSI2 = np.array(SI_V2_17['Date'])
timSI2 = np.array(SI_V2_17['Time'])
dattimSI2 = datSI2+' '+timSI2

#CONVERT TO DATETIME FROM STRING
dateSI2=[]
for i in range(len(dattimSI2)):
    dateSI2.append(datetime.strptime(dattimSI2[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------
# V3_17
dattim3 = np.array(V3_17['DateTime'])
#tim3 = np.array(V3_BrO['Time'])
#dattim3 = dat3+' '+tim3

#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    #date3.append(datetime.strptime(dattim3[i],'%Y/%m/%d %H:%M:%S')) # all data
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V3_17_Met
datM3 = np.array(V3_17_Met['Date'])
timM3 = np.array(V3_17_Met['Time'])
dattimM3 = datM3+' '+timM3

#CONVERT TO DATETIME FROM STRING
dateM3=[]
for i in range(len(dattimM3)):
    dateM3.append(datetime.strptime(dattimM3[i],'%d/%m/%Y %H:%M:%S'))

# V3_17_SI
datSI3 = np.array(SI_V3_17['Date'])
timSI3 = np.array(SI_V3_17['Time'])
dattimSI3 = datSI3+' '+timSI3

#CONVERT TO DATETIME FROM STRING
dateSI3=[]
for i in range(len(dattimSI3)):
    dateSI3.append(datetime.strptime(dattimSI3[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------
# V1_18
dattim4 = np.array(V1_18['DateTime'])
#tim4 = np.array(V1_BrO['Time'])
#dattim4 = dat4+' '+tim4

#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    #date4.append(datetime.strptime(dattim4[i],'%Y/%m/%d %H:%M:%S')) # all data
    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V1_18_Met
datM4 = np.array(V1_18_Met['Date'])
timM4 = np.array(V1_18_Met['Time'])
dattimM4 = datM4+' '+timM4

#CONVERT TO DATETIME FROM STRING
dateM4=[]
for i in range(len(dattimM4)):
    dateM4.append(datetime.strptime(dattimM4[i],'%d/%m/%Y %H:%M:%S'))

# V1_18_SI
datSI4 = np.array(SI_V1_18['Date'])
timSI4 = np.array(SI_V1_18['Time'])
dattimSI4 = datSI4+' '+timSI4

#CONVERT TO DATETIME FROM STRING
dateSI4=[]
for i in range(len(dattimSI4)):
    dateSI4.append(datetime.strptime(dattimSI4[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------
# V2_18
dattim5 = np.array(V2_18['DateTime'])
#tim5 = np.array(V2_BrO['Time'])
#dattim5 = dat5+' '+tim5

#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    #date5.append(datetime.strptime(dattim5[i],'%Y/%m/%d %H:%M:%S')) # all data
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V2_18_Met
datM5 = np.array(V2_18_Met['Date'])
timM5 = np.array(V2_18_Met['Time'])
dattimM5 = datM5+' '+timM5

#CONVERT TO DATETIME FROM STRING
dateM5=[]
for i in range(len(dattimM5)):
    dateM5.append(datetime.strptime(dattimM5[i],'%d/%m/%Y %H:%M:%S'))

# V2_18_SI
datSI5 = np.array(SI_V2_18['Date'])
timSI5 = np.array(SI_V2_18['Time'])
dattimSI5 = datSI5+' '+timSI5

#CONVERT TO DATETIME FROM STRING
dateSI5=[]
for i in range(len(dattimSI5)):
    dateSI5.append(datetime.strptime(dattimSI5[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------
# V3_18
dattim6 = np.array(V3_18['DateTime'])
#tim6 = np.array(V3_BrO['Time'])
#dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    #date6.append(datetime.strptime(dattim6[i],'%Y/%m/%d %H:%M:%S')) # all data
    date6.append(datetime.strptime(dattim6[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# V3_18_Met
datM6 = np.array(V3_18_Met['Date'])
timM6 = np.array(V3_18_Met['Time'])
dattimM6 = datM6+' '+timM6

#CONVERT TO DATETIME FROM STRING
dateM6=[]
for i in range(len(dattimM6)):
    dateM6.append(datetime.strptime(dattimM6[i],'%d/%m/%Y %H:%M:%S'))

# V3_18_SI
datSI6 = np.array(SI_V3_18['Date'])
timSI6 = np.array(SI_V3_18['Time'])
dattimSI6 = datSI6+' '+timSI6

#CONVERT TO DATETIME FROM STRING
dateSI6=[]
for i in range(len(dattimSI6)):
    dateSI6.append(datetime.strptime(dattimSI6[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------
# SIPEXII
dattim7 = np.array(SIPEXII['DateTime'])
#tim6 = np.array(V3_BrO['Time'])
#dattim6 = dat6+' '+tim6

#CONVERT TO DATETIME FROM STRING
date7=[]
for i in range(len(dattim7)):
    #date6.append(datetime.strptime(dattim6[i],'%Y/%m/%d %H:%M:%S')) # all data
    date7.append(datetime.strptime(dattim7[i],'%d/%m/%Y %H:%M:%S')) # midday data 

# SIPEXII_Met
datM7 = np.array(SIPEXII_Met['Date'])
timM7 = np.array(SIPEXII_Met['Time'])
dattimM7 = datM7+' '+timM7

#CONVERT TO DATETIME FROM STRING
dateM7=[]
for i in range(len(dattimM7)):
    dateM7.append(datetime.strptime(dattimM7[i],'%d/%m/%Y %H:%M:%S'))

# SIPEXII_SI
datSI7 = np.array(SI_SIPEXII['Date'])
timSI7 = np.array(SI_SIPEXII['Time'])
dattimSI7 = datSI7+' '+timSI7

#CONVERT TO DATETIME FROM STRING
dateSI7=[]
for i in range(len(dattimSI7)):
    dateSI7.append(datetime.strptime(dattimSI7[i],'%d/%m/%Y %H:%M:%S'))
    
#------------------------------------------------------------------------------
# CALCULATE THE BRO DAILY AVERAGE (MEAN)

# Function to calculate the daily mean
def dailyM(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('D').mean()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Daily Means
BrO_V1_17_DM, date1_DM=dailyM(BrO_V1_17[:],date1) # V1_17
BrO_V2_17_DM, date2_DM=dailyM(BrO_V2_17[:],date2) # V2_17
BrO_V3_17_DM, date3_DM=dailyM(BrO_V3_17[:],date3) # V3_17
BrO_V1_18_DM, date4_DM=dailyM(BrO_V1_18[:],date4) # V1_18
BrO_V2_18_DM, date5_DM=dailyM(BrO_V2_18[:],date5) # V2_18
BrO_V3_18_DM, date6_DM=dailyM(BrO_V3_18[:],date6) # V3_18
BrO_SIPEXII_DM, date7_DM=dailyM(BrO_SIPEXII[:],date7) # SIPEXII

# Latitude Daily Means
Lat_V1_17_DM, dateM1_DM=dailyM(Lat_V1_17[:],dateM1) # V1_17
Lat_V2_17_DM, dateM2_DM=dailyM(Lat_V2_17[:],dateM2) # V2_17
Lat_V3_17_DM, dateM3_DM=dailyM(Lat_V3_17[:],dateM3) # V3_17
Lat_V1_18_DM, dateM4_DM=dailyM(Lat_V1_18[:],dateM4) # V1_18
Lat_V2_18_DM, dateM5_DM=dailyM(Lat_V2_18[:],dateM5) # V2_18
Lat_V3_18_DM, dateM6_DM=dailyM(Lat_V3_18[:],dateM6) # V3_18
Lat_SIPEXII_DM, dateM7_DM=dailyM(Lat_SIPEXII[:],dateM7) # SIPEXII

# SeaIce Daily Means
SI_V1_17_DM, dateSI1_DM=dailyM(SeaIce_V1_17[:],dateSI1) # V1_17
SI_V2_17_DM, dateSI2_DM=dailyM(SeaIce_V2_17[:],dateSI2) # V2_17
SI_V3_17_DM, dateSI3_DM=dailyM(SeaIce_V3_17[:],dateSI3) # V3_17
SI_V1_18_DM, dateSI4_DM=dailyM(SeaIce_V1_18[:],dateSI4) # V1_18
SI_V2_18_DM, dateSI5_DM=dailyM(SeaIce_V2_18[:],dateSI5) # V2_18
SI_V3_18_DM, dateSI6_DM=dailyM(SeaIce_V3_18[:],dateSI6) # V3_18
SI_SIPEXII_DM, dateSI7_DM=dailyM(SeaIce_SIPEXII[:],dateSI7) # SIPEXII

#------------------------------------------------------------------------------
# CALCULATE THE STANDARD DEVIATION FOR THE BRO DAILY AVERAGE (MEAN)

# Function to calculate the standard deviation
def dailySTD(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('D').std()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Standard Deviations
BrO_V1_17_STD, date1_STD=dailySTD(BrO_V1_17[:],date1) # V1_17
BrO_V2_17_STD, date2_STD=dailySTD(BrO_V2_17[:],date2) # V2_17
BrO_V3_17_STD, date3_STD=dailySTD(BrO_V3_17[:],date3) # V3_17
BrO_V1_18_STD, date4_STDM=dailySTD(BrO_V1_18[:],date4) # V1_18
BrO_V2_18_STD, date5_STD=dailySTD(BrO_V2_18[:],date5) # V2_18
BrO_V3_18_STD, date6_STD=dailySTD(BrO_V3_18[:],date6) # V3_18
BrO_SIPEXII_STD, date7_STD=dailySTD(BrO_SIPEXII[:],date7) # SIPEXII

#------------------------------------------------------------------------------
# Set the date

V1_17['DateTime'] = pd.to_datetime(V1_17['DateTime'])
V2_17['DateTime'] = pd.to_datetime(V2_17['DateTime'])
V3_17['DateTime'] = pd.to_datetime(V3_17['DateTime'])
V1_18['DateTime'] = pd.to_datetime(V1_18['DateTime'])
V2_18['DateTime'] = pd.to_datetime(V2_18['DateTime'])
V3_18['DateTime'] = pd.to_datetime(V3_18['DateTime'])
SIPEXII['DateTime'] = pd.to_datetime(SIPEXII['DateTime'])

# Current time in UTC

#------------------------------------------------------------------------------
# Filter the datasets based on the date

#-----------------------------
# CAMMPCAN 2017-18
#-----------------------------
# V1_17 Davis (14-22 Nov 2017)
start_date = '2017-11-14'
end_date = '2017-11-23'
Davis = (V1_17['DateTime'] >= start_date) & (V1_17['DateTime'] < end_date)
V1_17_Davis = V1_17[Davis]

# V2_17 Casey (21-22 Dec 2017 and 26 Dec 2017 - 5 Jan 2018)
start_date1 = '2017-12-21'
end_date1 = '2017-12-23'
start_date2 = '2017-12-26'
end_date2 = '2018-01-6'
Casey1 = (V2_17['DateTime'] >= start_date1) & (V2_17['DateTime'] < end_date1)
Casey2 = (V2_17['DateTime'] >= start_date2) & (V2_17['DateTime'] < end_date2)
V2_17_Casey1 = V2_17[Casey1]
V2_17_Casey2 = V2_17[Casey2]
V2_17_Casey = pd.concat([V2_17_Casey1,V2_17_Casey2], axis =0)

# V3_17 Mawson (1-17 Feb 2018)
start_date = '2018-02-01'
end_date = '2018-02-18'
Mawson = (V3_17['DateTime'] >= start_date) & (V3_17['DateTime'] < end_date)
V3_17_Mawson = V3_17[Mawson]

#-----------------------------
# CAMMPCAN 2018-19
#-----------------------------
# V1_18 Davis (7-15 Nov 2018)
start_date = '2018-11-07'
end_date = '2018-11-16'
Davis = (V1_18['DateTime'] >= start_date) & (V1_18['DateTime'] < end_date)
V1_18_Davis = V1_18[Davis]

# V2_18 Casey (15-30 Dec 2018)
start_date = '2018-12-15'
end_date = '2018-12-31'
Casey = (V2_18['DateTime'] >= start_date) & (V2_18['DateTime'] < end_date)
V2_18_Casey = V2_18[Casey]

# V3_18 Mawson (30 Jan - 9 Feb 2019)
start_date = '2019-01-30'
end_date = '2019-02-10'
Mawson = (V3_18['DateTime'] >= start_date) & (V3_18['DateTime'] < end_date)
V3_18_Mawson = V3_18[Mawson]

#-----------------------------
# SIPEXII 2012
#-----------------------------
# SIPEXII (23 Sep to 11 Nov 2012)
start_date = '2012-09-23'
end_date = '2012-11-11'
SeaIce = (SIPEXII['DateTime'] >= start_date) & (SIPEXII['DateTime'] < end_date)
SIPEXII_Ice = SIPEXII[SeaIce]

#------------------------------------------------------------------------------
# BrO while on station

# CAMMPCAN (2017-18)
BrO_17_D = np.array(V1_17_Davis['surf_vmr(ppmv)'])* 1e6
BrO_17_C = np.array(V2_17_Casey['surf_vmr(ppmv)'])* 1e6
BrO_17_M = np.array(V3_17_Mawson['surf_vmr(ppmv)'])* 1e6

# CAMMPCAN (2018-19)
BrO_18_D = np.array(V1_18_Davis['surf_vmr(ppmv)'])* 1e6
BrO_18_C = np.array(V2_18_Casey['surf_vmr(ppmv)'])* 1e6
BrO_18_M = np.array(V3_18_Mawson['surf_vmr(ppmv)'])* 1e6

# SIPEXII (2012)
BrO_SIPEXII_I = np.array(SIPEXII_Ice['surf_vmr(ppmv)'])* 1e6

#-----------------------------
# Calculate the standard deviation
# 2017-18
std1 = np.std(BrO_17_D)
std2 = np.std(BrO_17_C)
std3 = np.std(BrO_17_M)
# 2018-19
std4 = np.std(BrO_18_D)
std5 = np.std(BrO_18_C)
std6 = np.std(BrO_18_M)
# 2012
std7 = np.std(BrO_SIPEXII_I)

# Standard deviation for season
std2017 = (std1+std2+std3)/3
std2018 = (std4+std5+std6)/3

#-----------------------------
# Calculate the mean
# 2017-18
mean1 = np.mean(BrO_17_D)
mean2 = np.mean(BrO_17_C)
mean3 = np.mean(BrO_17_M)
# 2018-19
mean4 = np.mean(BrO_18_D)
mean5 = np.mean(BrO_18_C)
mean6 = np.mean(BrO_18_M)
# 2012
mean7 = np.mean(BrO_SIPEXII_I)

# Mean for season
mean2017 = (mean1+mean2+mean3)/3
mean2018 = (mean3+mean5+mean6)/3

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(331) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()
ax3 = ax.twinx()

# Plot the variables
ax.plot(date1_DM, BrO_V1_17_DM, marker='o', c='red', markersize = 3.0, ls='-', label ='V1 (2017-18)')
ax2.plot(dateM1_DM, Lat_V1_17_DM, ls='--', c='black', label ='Latitude')

UL1 = BrO_V1_17_DM + BrO_V1_17_STD # find the upper limit
LL1 = BrO_V1_17_DM - BrO_V1_17_STD # find the lower limit
ax.plot(date1_DM, UL1, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date1_DM, LL1, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date1_DM, UL1, LL1, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
legend = ax.legend(loc='upper left')

#------------------------------
# Graph 2
ax=plt.subplot(332) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date2_DM, BrO_V2_17_DM, marker='o', c='red', markersize = 3.0, ls='-', label ='V2 (2017-18)')
ax2.plot(dateM2_DM, Lat_V2_17_DM, ls='--', c='black', label ='Latitude')

UL2 = BrO_V2_17_DM + BrO_V2_17_STD # find the upper limit
LL2 = BrO_V2_17_DM - BrO_V2_17_STD # find the lower limit
ax.plot(date2_DM, UL2, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date2_DM, LL2, 'r-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date2_DM, UL2, LL2, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
plt.title('BrO Daily Averages for CAMMPCAN 2017-19 and SIPEXII 2012 Voyages', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 3
ax=plt.subplot(333) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date3_DM, BrO_V3_17_DM, marker='o', c='red', markersize = 3.0, ls='-', label ='V3 (2017-18)')
ax2.plot(dateM3_DM, Lat_V3_17_DM, ls='--', c='black', label ='Latitude')

UL3 = BrO_V3_17_DM + BrO_V3_17_STD # find the upper limit
LL3 = BrO_V3_17_DM - BrO_V3_17_STD # find the lower limit
ax.plot(date3_DM, UL3, c='red', ls='--', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date3_DM, LL3, c='red', ls='--', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date3_DM, UL3, LL3, facecolor='red', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2017-18)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 4
ax=plt.subplot(334) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date4_DM, BrO_V1_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V1 (2018-19)')
ax2.plot(dateM4_DM, Lat_V1_18_DM, ls='--', c='black', label ='Latitude')

UL4 = BrO_V1_18_DM + BrO_V1_18_STD # find the upper limit
LL4 = BrO_V1_18_DM - BrO_V1_18_STD # find the lower limit
ax.plot(date4_DM, UL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date4_DM, LL4, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date4_DM, UL4, LL4, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V1 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 5
ax=plt.subplot(335) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date5_DM, BrO_V2_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V2 (2018-19)')
ax2.plot(dateM5_DM, Lat_V2_18_DM, ls='--', c='black', label ='Latitude')

UL5 = BrO_V2_18_DM + BrO_V2_18_STD # find the upper limit
LL5 = BrO_V2_18_DM - BrO_V2_18_STD # find the lower limit
ax.plot(date5_DM, UL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date5_DM, LL5, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date5_DM, UL5, LL5, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)

#Plot the legend and title
#plt.title('BrO Daily Average (V2 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 6
ax=plt.subplot(336) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date6_DM, BrO_V3_18_DM, marker='o', c='blue', markersize = 3.0, ls='-', label ='V3 (2018-19)')
ax2.plot(dateM6_DM, Lat_V3_18_DM, ls='--', c='black', label ='Latitude')

UL6 = BrO_V3_18_DM + BrO_V3_18_STD # find the upper limit
LL6 = BrO_V3_18_DM - BrO_V3_18_STD # find the lower limit
ax.plot(date6_DM, UL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date6_DM, LL6, 'b-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date6_DM, UL6, LL6, facecolor='blue', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')

#------------------------------
# Graph 6
ax=plt.subplot(338) # options graph 1 (vertical no, horizontal no, graph no)
ax2 = ax.twinx()

# Plot the variables
ax.plot(date7_DM, BrO_SIPEXII_DM, marker='o', c='green', markersize = 3.0, ls='-', label ='SIPEXII (2012)')
ax2.plot(dateM7_DM, Lat_SIPEXII_DM, ls='--', c='black', label ='Latitude')

UL7 = BrO_SIPEXII_DM + BrO_SIPEXII_STD # find the upper limit
LL7 = BrO_SIPEXII_DM - BrO_SIPEXII_STD # find the lower limit
ax.plot(date7_DM, UL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the upper limit
ax.plot(date7_DM, LL7, 'g-', linewidth=2, alpha=0.3, label='_nolegend_')   # plot the lower limit
ax.fill_between(date7_DM, UL7, LL7, facecolor='green', alpha=0.3) # fill the distribution

# Format x-axis
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=10)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
#ax2.axes.get_xaxis().set_visible(False)

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0,55)

# Format y-axis 2
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.set_ylim(-69,-42)

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax2.set_ylabel('Latitude ($^\circ$S)', fontsize=10)
ax.set_xlabel('Date', fontsize=15)
#ax.set_xlabel('Date', fontsize=15)
#Plot the legend and title
#plt.title('BrO Daily Average (V3 CAMMPCAN 2018-19)', fontsize=25, y=1.2)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax.legend(loc='upper left')
