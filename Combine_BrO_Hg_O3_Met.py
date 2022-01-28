#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:06:24 2019

@author: ncp532
"""

import pandas as pd

#------------------------------------------------------------------------------
# Read in data from the .csv file

## CAMMPCAN 2017-18
## V1_17
#Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V01/CAMMPCAN_V1_underway_60.csv') # Met data
#O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V1_O3_1min.csv') # 1 min O3 data 
#BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_17_F.csv')
#Hg  = pd.read_csv('/Users/ncp532/Documents/Data/QC_Tekran/CAMMPCAN_V1_QAQC_17-18.csv')
#SeaIce = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V1_17_M_SeaIce.csv')

## V2_17
#Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V02/CAMMPCAN_V2_underway_60.csv') # Met data
#O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V2_O3_1min.csv') # 1 min O3 data 
#BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V2_17_F.csv')
#Hg  = pd.read_csv('/Users/ncp532/Documents/Data/QC_Tekran/CAMMPCAN_V2_QAQC_17-18.csv') 
#SeaIce = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V2_17_M_SeaIce.csv')

## V3_17
#Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V03/CAMMPCAN_V3_underway_60.csv') # Met data
#O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/ARM/V3_O3_1min.csv') # 1 min O3 data 
#BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V3_17_F.csv')
#Hg  = pd.read_csv('/Users/ncp532/Documents/Data/QC_Tekran/CAMMPCAN_V3_QAQC_17-18.csv') 
#SeaIce = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2017_18/V3_17_M_SeaIce.csv')

#--------------------------------
# CAMMPCAN 2018-19
## V1_18
#Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V01/CAMMPCAN_V1_underway_60.csv') # Met data
#O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V1_O3_1min.csv') # 1 min O3 data 
#BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V1_18_F.csv')
#Hg  = pd.read_csv('/Users/ncp532/Documents/Data/QC_Tekran/CAMMPCAN_V1_QAQC_18-19.csv')
#SeaIce = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V1_18_M_SeaIce.csv')

## V2_18
#Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V02/CAMMPCAN_V2_underway_60.csv') # Met data
#O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V2_O3_1min.csv') # 1 min O3 data 
#BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V2_18_F.csv')
#Hg  = pd.read_csv('/Users/ncp532/Documents/Data/QC_Tekran/CAMMPCAN_V2_QAQC_18-19.csv') 
#SeaIce = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V2_18_M_SeaIce.csv')

## V3_18
#Met = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V03/CAMMPCAN_V3_underway_60.csv') # Met data
#O3  = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/O3/V3_O3_1min.csv') # 1 min O3 data 
#BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/V3_18_F.csv')
#Hg  = pd.read_csv('/Users/ncp532/Documents/Data/QC_Tekran/CAMMPCAN_V3_QAQC_18-19.csv') 
#SeaIce = pd.read_csv('/Users/ncp532/Documents/Data/CAMMPCAN_2018_19/V3_18_M_SeaIce.csv')

#--------------------------------
# SIPEXII 2012
Met = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_underway_60.csv') # Met data
O3  = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv') # 1 min O3 data 
BrO = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII_F.csv')
Hg  = pd.read_csv('/Users/ncp532/Documents/Data/QC_Tekran/SIPEXII_QAQC.csv')
SeaIce = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv')

#------------------------------------------------------------------------------
# Set the date

Met['DateTime'] = pd.to_datetime(Met['DateTime'])
O3['DateTime'] = pd.to_datetime(O3['DateTime'])
BrO['DateTime'] = pd.to_datetime(BrO['DateTime'])
Hg['DateTime'] = pd.to_datetime(Hg['DateTime'])
SeaIce['DateTime'] = pd.to_datetime(SeaIce['DateTime'])

Met.index = Met['DateTime']
O3.index = O3['DateTime']
BrO.index = BrO['DateTime']
Hg.index = Hg['DateTime']
SeaIce.index = SeaIce['DateTime']

# Make a new dataset (Data3) with only the shared rows corresponding to DT
Data1 = pd.merge(left=BrO,right=Met, how='left', left_index=True, right_index=True)
Data2 = pd.merge(left=Data1,right=O3, how='left', left_index=True, right_index=True)
Data3 = pd.merge(left=Data2,right=Hg, how='left', left_index=True, right_index=True)
Data4 = pd.merge(left=Data3,right=SeaIce, how='left', left_index=True, right_index=True)

# write the pandas dataframe to a .csv file
Data4.to_csv('/Users/ncp532/Documents/Data/V1_17_APriori/SIPEXII_Data_SI.csv')