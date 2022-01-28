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
from scipy import stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# CAMMPCAN 2017-18
Test1 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test1_F.csv') # Test 1
Test2 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test2_F.csv') # Test 2
Test3 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test3_F.csv') # Test 3
Test4 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test4_F.csv') # Test 4
Test5 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test5_F.csv') # Test 5
Test6 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test6_F.csv') # Test 6
Test7 = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test7_F.csv') # Test 7

#------------------------------------------------------------------------------
# Set the date
# Davis timezone is UT+7

Test1['DateTime'] = pd.to_datetime(Test1['DateTime'])# + pd.DateOffset(hours=7)
Test2['DateTime'] = pd.to_datetime(Test2['DateTime'])# + pd.DateOffset(hours=7)
Test3['DateTime'] = pd.to_datetime(Test3['DateTime'])# + pd.DateOffset(hours=7)
Test4['DateTime'] = pd.to_datetime(Test4['DateTime'])# + pd.DateOffset(hours=7)
Test5['DateTime'] = pd.to_datetime(Test5['DateTime'])# + pd.DateOffset(hours=7)
Test6['DateTime'] = pd.to_datetime(Test6['DateTime'])# + pd.DateOffset(hours=7)
Test7['DateTime'] = pd.to_datetime(Test7['DateTime'])# + pd.DateOffset(hours=7)

#Test1.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test1.csv') # Test 1
#Test2.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test2.csv') # Test 2
#Test3.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test3.csv') # Test 3
#Test4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test4.csv') # Test 4
#Test5.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test5.csv') # Test 5
#Test6.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test6.csv') # Test 6
#Test7.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_Test7.csv') # Test 7

Test1.set_index('DateTime')
Test2.set_index('DateTime')
Test3.set_index('DateTime')
Test4.set_index('DateTime')
Test5.set_index('DateTime')
Test6.set_index('DateTime')
Test7.set_index('DateTime')

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

# Test 1 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday1 = (Test1['Time'] >= start_time) & (Test1['Time'] < end_time)
Test1_MM = Test1[Midday1]

# Test 2 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday2 = (Test2['Time'] >= start_time) & (Test2['Time'] < end_time)
Test2_MM = Test2[Midday2]

# Test 3 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday3 = (Test3['Time'] >= start_time) & (Test3['Time'] < end_time)
Test3_MM = Test3[Midday3]

# Test 4 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday4 = (Test4['Time'] >= start_time) & (Test4['Time'] < end_time)
Test4_MM = Test4[Midday4]

# Test 5 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday5 = (Test5['Time'] >= start_time) & (Test5['Time'] < end_time)
Test5_MM = Test5[Midday5]

# Test 6 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday6 = (Test6['Time'] >= start_time) & (Test6['Time'] < end_time)
Test6_MM = Test6[Midday6]

# Test 7 (07:00 to 18:00)
start_time = '07:00:00'
end_time = '18:00:00'
Midday7 = (Test7['Time'] >= start_time) & (Test7['Time'] < end_time)
Test7_MM = Test7[Midday7]

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

Test1F = (Test1_MM['Filter'] < 0.6)
Test1T = Test1_MM[Test1F]

Test2F = (Test2_MM['Filter'] < 0.6)
Test2T = Test2_MM[Test2F]

Test3F = (Test3_MM['Filter'] < 0.6)
Test3T = Test3_MM[Test3F]

Test4F = (Test4_MM['Filter'] < 0.6)
Test4T = Test4_MM[Test4F]

Test5F = (Test5_MM['Filter'] < 0.6)
Test5T = Test5_MM[Test5F]

Test6F = (Test6_MM['Filter'] < 0.6)
Test6T = Test6_MM[Test6F]

Test7F = (Test7_MM['Filter'] < 0.6)
Test7T = Test7_MM[Test7F]

#------------------------------------------------------------------------------
# Define the variables

#BrO_Test1 = np.array(Test1_MM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
#BrO_Test2 = np.array(Test2_MM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
#BrO_Test3 = np.array(Test3_MM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
#BrO_Test4 = np.array(Test4_MM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
#BrO_Test5 = np.array(Test5_MM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
#BrO_Test6 = np.array(Test6_MM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
#BrO_Test7 = np.array(Test7_MM['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

BrO_Test1 = np.array(Test1T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Test2 = np.array(Test2T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Test3 = np.array(Test3T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Test4 = np.array(Test4T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Test5 = np.array(Test5T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Test6 = np.array(Test6T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv
BrO_Test7 = np.array(Test7T['surf_vmr(ppmv)']) * 1e6 # convert from ppmv to pptv

#------------------------------------------------------------------------------
# SET THE DATE AND TIME

# Test1
#dat1 = np.array(Test1_MM['Date'])
#tim1 = np.array(Test1_MM['Time'])

dat1 = np.array(Test1T['Date'])
tim1 = np.array(Test1T['Time'])
dattim1 = dat1+' '+tim1
#CONVERT TO DATETIME FROM STRING
date1=[]
for i in range(len(dattim1)):
    date1.append(datetime.strptime(dattim1[i],'%d/%m/%Y %H:%M:%S')) # midday data    

#------------------------------------
# Test2
#dat2 = np.array(Test2_MM['Date'])
#tim2 = np.array(Test2_MM['Time'])

dat2 = np.array(Test2T['Date'])
tim2 = np.array(Test2T['Time'])
dattim2 = dat2+' '+tim2
#CONVERT TO DATETIME FROM STRING
date2=[]
for i in range(len(dattim2)):
    date2.append(datetime.strptime(dattim2[i],'%d/%m/%Y %H:%M:%S')) # midday data 

#------------------------------------
# Test3
#dat3 = np.array(Test3_MM['Date'])
#tim3 = np.array(Test3_MM['Time'])

dat3 = np.array(Test3T['Date'])
tim3 = np.array(Test3T['Time'])
dattim3 = dat3+' '+tim3
#CONVERT TO DATETIME FROM STRING
date3=[]
for i in range(len(dattim3)):
    date3.append(datetime.strptime(dattim3[i],'%d/%m/%Y %H:%M:%S')) # midday data 

#------------------------------------
# Test4
#dat4 = np.array(Test4_MM['Date'])
#tim4 = np.array(Test4_MM['Time'])

dat4 = np.array(Test4T['Date'])
tim4 = np.array(Test4T['Time'])
dattim4 = dat4+' '+tim4
#CONVERT TO DATETIME FROM STRING
date4=[]
for i in range(len(dattim4)):
    date4.append(datetime.strptime(dattim4[i],'%d/%m/%Y %H:%M:%S')) # midday data 

#------------------------------------
# Test5
#dat5 = np.array(Test5_MM['Date'])
#tim5 = np.array(Test5_MM['Time'])

dat5 = np.array(Test5T['Date'])
tim5 = np.array(Test5T['Time'])
dattim5 = dat5+' '+tim5
#CONVERT TO DATETIME FROM STRING
date5=[]
for i in range(len(dattim5)):
    date5.append(datetime.strptime(dattim5[i],'%d/%m/%Y %H:%M:%S')) # midday data 

#------------------------------------
# Test6
#dat6 = np.array(Test6_MM['Date'])
#tim6 = np.array(Test6_MM['Time'])

dat6 = np.array(Test6T['Date'])
tim6 = np.array(Test6T['Time'])
dattim6 = dat6+' '+tim6
#CONVERT TO DATETIME FROM STRING
date6=[]
for i in range(len(dattim6)):
    date6.append(datetime.strptime(dattim6[i],'%d/%m/%Y %H:%M:%S')) # midday data 

#------------------------------------
# Test7
#dat7 = np.array(Test7_MM['Date'])
#tim7 = np.array(Test7_MM['Time'])

dat7 = np.array(Test7T['Date'])
tim7 = np.array(Test7T['Time'])
dattim7 = dat7+' '+tim7
#CONVERT TO DATETIME FROM STRING
date7=[]
for i in range(len(dattim7)):
    date7.append(datetime.strptime(dattim7[i],'%d/%m/%Y %H:%M:%S')) # midday data 

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
Test1_DM, date1_DM=dailyM(BrO_Test1[:],date1) # Test1
Test2_DM, date2_DM=dailyM(BrO_Test2[:],date2) # Test2
Test3_DM, date3_DM=dailyM(BrO_Test3[:],date3) # Test3
Test4_DM, date4_DM=dailyM(BrO_Test4[:],date4) # Test4
Test5_DM, date5_DM=dailyM(BrO_Test5[:],date5) # Test5
Test6_DM, date6_DM=dailyM(BrO_Test6[:],date6) # Test6
Test7_DM, date7_DM=dailyM(BrO_Test7[:],date7) # Test7

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
Test1_STD, date1_STD=dailySTD(BrO_Test1[:],date1) # Test1
Test2_STD, date2_STD=dailySTD(BrO_Test2[:],date2) # Test2
Test3_STD, date3_STD=dailySTD(BrO_Test3[:],date3) # Test3
Test4_STD, date4_STDM=dailySTD(BrO_Test4[:],date4) # Test4
Test5_STD, date5_STDM=dailySTD(BrO_Test5[:],date5) # Test5
Test6_STD, date6_STDM=dailySTD(BrO_Test6[:],date6) # Test6
Test7_STD, date7_STDM=dailySTD(BrO_Test7[:],date7) # Test7

#------------------------------------------------------------------------------
# CALCULATE THE BRO DAILY MEDIAN

# Function to calculate the daily mean
def dailyMed(x, date):
    df = pd.DataFrame({'X':x}, index=date) 
    df = df.resample('D').median()
    #Reset the index
    df =df.reset_index()
    #extract the values
    x=df['X']
    date=df['index']  
    #convert the pandas series date to list
    date = date.tolist()
    return x,date 

# BrO Daily Median
Test1_DMed, date1_DMed=dailyMed(BrO_Test1[:],date1) # Test1
Test2_DMed, date2_DMed=dailyMed(BrO_Test2[:],date2) # Test2
Test3_DMed, date3_DMed=dailyMed(BrO_Test3[:],date3) # Test3
Test4_DMed, date4_DMed=dailyMed(BrO_Test4[:],date4) # Test4
Test5_DMed, date5_DMed=dailyMed(BrO_Test5[:],date5) # Test5
Test6_DMed, date6_DMed=dailyMed(BrO_Test6[:],date6) # Test6
Test7_DMed, date7_DMed=dailyMed(BrO_Test7[:],date7) # Test7

#------------------------------------------------------------------------------
# Set the date

Test1_MM['DateTime'] = pd.to_datetime(Test1_MM['DateTime'])
Test2_MM['DateTime'] = pd.to_datetime(Test2_MM['DateTime'])
Test3_MM['DateTime'] = pd.to_datetime(Test3_MM['DateTime'])
Test4_MM['DateTime'] = pd.to_datetime(Test4_MM['DateTime'])
Test5_MM['DateTime'] = pd.to_datetime(Test5_MM['DateTime'])
Test6_MM['DateTime'] = pd.to_datetime(Test6_MM['DateTime'])
Test7_MM['DateTime'] = pd.to_datetime(Test7_MM['DateTime'])

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# At Davis (14-22 Nov 2017)
start_date = '2017-11-14'
end_date = '2017-11-23'

# Test1
Test1F = (Test1_MM['DateTime'] >= start_date) & (Test1_MM['DateTime'] < end_date)
Test1_Davis = Test1_MM[Test1F]

# Test2
Test2F = (Test2_MM['DateTime'] >= start_date) & (Test2_MM['DateTime'] < end_date)
Test2_Davis = Test2_MM[Test1F]

# Test3
Test3F = (Test3_MM['DateTime'] >= start_date) & (Test3_MM['DateTime'] < end_date)
Test3_Davis = Test3_MM[Test3F]

#Test4
Test4F = (Test4_MM['DateTime'] >= start_date) & (Test4_MM['DateTime'] < end_date)
Test4_Davis = Test4_MM[Test4F]

## Test5
Test5F = (Test5_MM['DateTime'] >= start_date) & (Test5_MM['DateTime'] < end_date)
Test5_Davis = Test5_MM[Test5F]

# Test6
Test6F = (Test6_MM['DateTime'] >= start_date) & (Test6_MM['DateTime'] < end_date)
Test6_Davis = Test6_MM[Test6F]

# Test7
Test7F = (Test7_MM['DateTime'] >= start_date) & (Test7_MM['DateTime'] < end_date)
Test7_Davis = Test7_MM[Test7F]

#------------------------------------------------------------------------------
# BrO while on station

BrO_Test1F = np.array(Test1_Davis['surf_vmr(ppmv)'])* 1e6
BrO_Test2F = np.array(Test2_Davis['surf_vmr(ppmv)'])* 1e6
BrO_Test3F = np.array(Test3_Davis['surf_vmr(ppmv)'])* 1e6
BrO_Test4F = np.array(Test4_Davis['surf_vmr(ppmv)'])* 1e6
BrO_Test5F = np.array(Test5_Davis['surf_vmr(ppmv)'])* 1e6
BrO_Test6F = np.array(Test6_Davis['surf_vmr(ppmv)'])* 1e6
BrO_Test7F = np.array(Test7_Davis['surf_vmr(ppmv)'])* 1e6

#-----------------------------
# Calculate the standard deviation

std1 = np.std(BrO_Test1)
std2 = np.std(BrO_Test2)
std3 = np.std(BrO_Test3)
std4 = np.std(BrO_Test4)
std5 = np.std(BrO_Test5)
std6 = np.std(BrO_Test6)
std7 = np.std(BrO_Test7)

#-----------------------------
# Calculate the mean

mean1 = np.mean(BrO_Test1)
mean2 = np.mean(BrO_Test2)
mean3 = np.mean(BrO_Test3)
mean4 = np.mean(BrO_Test4)
mean5 = np.mean(BrO_Test5)
mean6 = np.mean(BrO_Test6)
mean7 = np.mean(BrO_Test7)

#-----------------------------
# Calculate the median

median1 = np.median(BrO_Test1)
median2 = np.median(BrO_Test2)
median3 = np.median(BrO_Test3)
median4 = np.median(BrO_Test4)
median5 = np.median(BrO_Test5)
median6 = np.median(BrO_Test6)
median7 = np.median(BrO_Test7)

#-----------------------------
# Calculate the median absolute deviation

mad1 = stats.median_absolute_deviation(BrO_Test1)
mad2 = stats.median_absolute_deviation(BrO_Test2)
mad3 = stats.median_absolute_deviation(BrO_Test3)
mad4 = stats.median_absolute_deviation(BrO_Test4)
mad5 = stats.median_absolute_deviation(BrO_Test5)
mad6 = stats.median_absolute_deviation(BrO_Test6)
mad7 = stats.median_absolute_deviation(BrO_Test7)

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 1
ax=plt.subplot(211) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
# Test1
ax.plot(date2_DM, Test2_DM, marker='o', c='red', markersize = 3.0, ls='dotted', label ='Test 1 (a priori = 1 pptv, albedo = 0.06)\n mean:'+str("%6.2f"%(mean2))+" $\pm$ "+str("%7.2f"%(std2))+" pptv")
ax.errorbar(date2_DM, Test2_DM, c='red', yerr=std2, ls='dotted',capsize=3)
# Test2
ax.plot(date4_DM, Test4_DM, marker='^', c='red', markersize = 3.0, ls='-', label ='Test 2 (a priori = 1 pptv, albedo = 0.6)\n mean:'+str("%6.2f"%(mean4))+" $\pm$ "+str("%7.2f"%(std4))+" pptv")
ax.errorbar(date4_DM, Test4_DM, marker='^', c='red', yerr=std4, ls='-', capsize=3)
# Test3
ax.plot(date6_DM, Test6_DM, marker='s', c='red', markersize = 3.0, ls='--', label ='Test 3 (a priori = 1 pptv, albedo = 0.8)\n mean:'+str("%6.2f"%(mean6))+" $\pm$ "+str("%7.2f"%(std6))+" pptv")
ax.errorbar(date6_DM, Test6_DM, marker='s', c='red', yerr=std6, ls='--', capsize=3)
# Test4
ax.plot(date3_DM, Test3_DM, marker='o', c='blue', markersize = 3.0, ls='dotted', label ='Test 4 (a priori = 3 pptv, albedo = 0.06)\n mean:'+str("%6.2f"%(mean3))+" $\pm$ "+str("%7.2f"%(std3))+" pptv")
ax.errorbar(date3_DM, Test3_DM, marker='o', c='blue', ls='dotted', yerr=std3, capsize=3)
# Test5
ax.plot(date5_DM, Test5_DM, marker='^', c='blue', markersize = 3.0, ls='-', label ='Test 5 (a priori = 3 pptv, albedo = 0.6)\n mean:'+str("%6.2f"%(mean5))+" $\pm$ "+str("%7.2f"%(std5))+" pptv")
ax.errorbar(date5_DM, Test5_DM, marker='^', c='blue', ls='-', yerr=std5, capsize=3)
# Test6
ax.plot(date7_DM, Test7_DM, marker='s', c='blue', markersize = 3.0, ls='--', label ='Test 6 (a priori = 3 pptv, albedo = 0.8)\n mean:'+str("%6.2f"%(mean7))+" $\pm$ "+str("%7.2f"%(std7))+" pptv")
ax.errorbar(date7_DM, Test7_DM,marker='s',  c='blue', ls='--', yerr=std7, capsize=3)
# Test7
ax.plot(date1_DM, Test1_DM, marker='o', c='orange', markersize = 3.0, ls='dotted', label ='Test 7 (a priori = 10 pptv, albedo = 0.06)\n mean:'+str("%6.2f"%(mean1))+" $\pm$ "+str("%7.2f"%(std1))+" pptv")
ax.errorbar(date1_DM, Test1_DM, marker='o', c='orange', yerr=std1, ls='dotted', capsize=3)

# Format x-axis
plt.xlim(datetime(2017,11,13,12,0,0),datetime(2017,11,24,12,0,0)) # on station
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('black')
ax.tick_params(axis='y', which='both', colors='black')
ax.set_ylim(0,13) # all dates
#ax.set_ylim(0,15) # on station

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax.set_xlabel('Date', fontsize=10)
plt.title('Daily mean BrO concentration at Davis V1 (2017-18)', fontsize=25, y=1.05)
legend = ax.legend(bbox_to_anchor=(1.01, 1.025), loc=2)
#legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------
# Graph 2
ax=plt.subplot(212) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
# Test1
ax.plot(date2_DMed, Test2_DMed, marker='o', c='red', markersize = 3.0, ls='dotted', label ='Test 1 (a priori = 1 pptv, albedo = 0.06)\n median:'+str("%6.2f"%(median2))+" $\pm$ "+str("%7.2f"%(mad2))+" pptv")
ax.errorbar(date2_DMed, Test2_DMed, c='red', yerr=mad2, ls='dotted', capsize=3)
# Test2
ax.plot(date4_DMed, Test4_DMed, marker='^', c='red', markersize = 3.0, ls='-', label ='Test 2 (a priori = 1 pptv, albedo = 0.6)\n median:'+str("%6.2f"%(median4))+" $\pm$ "+str("%7.2f"%(mad4))+" pptv")
ax.errorbar(date4_DMed, Test4_DMed, marker='^', c='red', yerr=mad4, ls='-', capsize=3)
# Test3
ax.plot(date6_DMed, Test6_DMed, marker='s', c='red', markersize = 3.0, ls='--', label ='Test 3 (a priori = 1 pptv, albedo = 0.8)\n median:'+str("%6.2f"%(median6))+" $\pm$ "+str("%7.2f"%(mad6))+" pptv")
ax.errorbar(date6_DMed, Test6_DMed, marker='s', c='red', yerr=mad6, ls='--', capsize=3)
# Test4
ax.plot(date3_DMed, Test3_DMed, marker='o', c='blue', markersize = 3.0, ls='dotted', label ='Test 4 (a priori = 3 pptv, albedo = 0.06)\n median:'+str("%6.2f"%(median3))+" $\pm$ "+str("%7.2f"%(mad3))+" pptv")
ax.errorbar(date3_DMed, Test3_DMed, marker='o', c='blue', ls='dotted', yerr=mad3, capsize=3)
# Test5
ax.plot(date5_DMed, Test5_DMed, marker='^', c='blue', markersize = 3.0, ls='-', label ='Test 5 (a priori = 3 pptv, albedo = 0.6)\n median:'+str("%6.2f"%(median5))+" $\pm$ "+str("%7.2f"%(mad5))+" pptv")
ax.errorbar(date5_DMed, Test5_DMed, marker='^', c='blue', ls='-', yerr=mad5, capsize=3)
# Test6
ax.plot(date7_DMed, Test7_DMed, marker='s', c='blue', markersize = 3.0, ls='--', label ='Test 6 (a priori = 3 pptv, albedo = 0.8)\n median:'+str("%6.2f"%(median7))+" $\pm$ "+str("%7.2f"%(mad7))+" pptv")
ax.errorbar(date7_DMed, Test7_DMed, marker='s', c='blue', ls='--', yerr=mad7, capsize=3)
# Test7
ax.plot(date1_DMed, Test1_DMed, marker='o', c='orange', markersize = 3.0, ls='dotted', label ='Test 7 (a priori = 10 pptv, albedo = 0.06)\n median:'+str("%6.2f"%(median1))+" $\pm$ "+str("%7.2f"%(mad1))+" pptv")
ax.errorbar(date1_DMed, Test1_DMed, marker='o', c='orange', ls='dotted', yerr=mad1, capsize=3)

# Format x-axis
plt.xlim(datetime(2017,11,13,12,0,0),datetime(2017,11,24,12,0,0)) # on station
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('black')
ax.tick_params(axis='y', which='both', colors='black')
ax.set_ylim(0,10) # all dates
#ax.set_ylim(0,15) # on station

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax.set_xlabel('Date', fontsize=10)
plt.title('Daily median BrO concentration at Davis V1 (2017-18)', fontsize=25, y=1.05)
legend = ax.legend(bbox_to_anchor=(1.01, 1.025), loc=2)
#legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

#------------------------------------------------------------------------------
# PLOT THE GRAPH
fig = plt.figure()
plt.subplots_adjust(hspace=0.5)

#------------------------------
# Graph 3
ax=plt.subplot(111) # options graph 1 (vertical no, horizontal no, graph no)

# Plot the variables
# Test1
ax.plot(date2, BrO_Test2, marker='+', c='red', markersize = 3.0, ls='None', label ='Test 1\n(a-priori = 1 pptv, albedo = 0.06)')
# Test2
ax.plot(date4, BrO_Test4, marker='+', c='green', markersize = 3.0, ls='None', label ='Test 2\n(a-priori = 1 pptv, albedo = 0.6)')
# Test3
ax.plot(date6, BrO_Test6, marker='+', c='cyan', markersize = 3.0, ls='None', label ='Test 3\n(a-priori = 1 pptv, albedo = 0.8)')
# Test4
ax.plot(date3, BrO_Test3, marker='+', c='black', markersize = 3.0, ls='None', label ='Test 4\n(a-priori = 3 pptv, albedo = 0.06)')
# Test5
ax.plot(date5, BrO_Test5, marker='+', c='orange', markersize = 3.0, ls='None', label ='Test 5\n(a-priori = 3 pptv, albedo = 0.6)')
# Test6
ax.plot(date7, BrO_Test7, marker='+', c='saddlebrown', markersize = 3.0, ls='None', label ='Test 6\n(a-priori = 3 pptv, albedo = 0.8)')
# Test7
ax.plot(date1, BrO_Test1, marker='+', c='blue', markersize = 3.0, ls='None', label ='Test 7\n(a-priori = 10 pptv, albedo = 0.06)')

# Format x-axis
plt.xlim(datetime(2017,11,14),datetime(2017,11,23)) # on station
plt.xticks(rotation=45)
xmajor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
ax.xaxis.set_major_formatter(xmajor_formatter)
#xminor_formatter = mdates.DateFormatter('%d %b') # format how the date is displayed
#ax.xaxis.set_minor_formatter(xminor_formatter)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # set the interval between dispalyed dates
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.label.set_color('black')
ax.tick_params(axis='y', which='both', colors='black')
ax.set_ylim(0,15) # all dates
#ax.set_ylim(0,15) # on station

# Plot the axis labels, legend and title
ax.set_ylabel('BrO VMR (pptv)', fontsize=10)
ax.set_xlabel('Date', fontsize=10)
plt.title('BrO concentrations at Davis V1 (2017-18)', fontsize=25, y=1.05)
legend = ax.legend(bbox_to_anchor=(1.01, 1.0), loc=2)
#legend.get_frame().set_facecolor('#00FFCC')
legend.get_frame().set_alpha(0.9)

