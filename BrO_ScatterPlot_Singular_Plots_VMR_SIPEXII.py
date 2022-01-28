#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:39:27 2019

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
from scipy import signal, stats

# Drawing packages
import matplotlib.pyplot as plt             # import package as shorter nickname
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# OBSERVATIONAL DATA

# SIPEXII 2012
SIPEXII_BrO   = pd.read_csv('/Users/ncp532/Documents/Data/V1_17_Apriori/SIPEXII_Data.csv',header=0,encoding = 'unicode_escape')
SIPEXII_VMR   = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/all_BrO/SIPEXII_BrO_VMR.csv', index_col=0) # BrO data for SIPEXII (2012)
SIPEXII_Error = pd.read_csv('/Users/ncp532/Documents/data/V1_17_APriori/SIPEXII/BrO_error/SIPEXII_BrO_error.csv', index_col=0) # BrO error data for SIPEXII (2012)
SIPEXII_Met   = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_underway_60.csv') #SIPEXII_underway_60.csv') 
SIPEXII_SI    = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_M_SeaIce.csv')
SIPEXII_Hg    = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_Hg_Air/SIPEXII_Hg0_QAQC_2012.csv')
SIPEXII_O3    = pd.read_csv('/Users/ncp532/Documents/Data/SIPEXII_2012/SIPEXII_O3/SIPEXII_O3_QAQC.csv')

#------------------------------------------------------------------------------
# Calculate the Relative Error (>=0.6)

# Define the filter
Filter_SIPEXII = SIPEXII_Error / SIPEXII_VMR

# Apply the filter
SIPEXIIF    = Filter_SIPEXII < 0.6
SIPEXII_VMR = SIPEXII_VMR[SIPEXIIF]

#------------------------------------------------------------------------------
# Set the date

# SIPEXII (2012)
SIPEXII_BrO['DateTime'] = pd.to_datetime(SIPEXII_BrO['DateTime'], dayfirst=True)
SIPEXII_VMR.columns     = (pd.to_datetime(SIPEXII_VMR.columns, dayfirst=True) + timedelta(hours=8)) # SIPEXII timezone is UT+8
SIPEXII_Met['DateTime'] = pd.to_datetime(SIPEXII_Met['DateTime'], dayfirst=True)
SIPEXII_SI['DateTime']  = pd.to_datetime(SIPEXII_SI['DateTime'],  dayfirst=True)
SIPEXII_Hg['DateTime']  = pd.to_datetime(SIPEXII_Hg['DateTime'],  dayfirst=True)
SIPEXII_O3['DateTime']  = pd.to_datetime(SIPEXII_O3['DateTime'],  dayfirst=True)

#------------------------------------------------------------------------------
# Transpose the VMR dataframes

SIPEXIITT = SIPEXII_VMR.T

#------------------------------------------------------------------------------
# Add columns for DateTime, Date and Time

# DateTime
SIPEXIITT['DateTime'] = SIPEXIITT.index

# Date
SIPEXIITT['Date'] = SIPEXIITT['DateTime'].dt.date

# Time
SIPEXIITT['Time'] = SIPEXIITT['DateTime'].dt.time

#------------------------------------------------------------------------------
# set datetime as the index

# SIPEXII (2012)
SIPEXII_BrO = SIPEXII_BrO.set_index('DateTime')
SIPEXII_Met = SIPEXII_Met.set_index('DateTime')
SIPEXII_SI  = SIPEXII_SI.set_index('DateTime')
SIPEXII_Hg  = SIPEXII_Hg.set_index('DateTime')
SIPEXII_O3  = SIPEXII_O3.set_index('DateTime')

#------------------------------------------------------------------------------
# Resample all data to 20 min averages

# SIPEXII (2012)
SIPEXII_Met = SIPEXII_Met.resample('20T').mean()
SIPEXII_SI  = SIPEXII_SI.resample('20T').mean()
SIPEXII_Hg  = SIPEXII_Hg.resample('20T').mean()
SIPEXII_O3  = SIPEXII_O3.resample('20T').mean()

#------------------------------------------------------------------------------
# Change datetime to be 10 mins earlier

# SIPEXII (2012)
SIPEXII_Met.index = SIPEXII_Met.index - pd.Timedelta(minutes=10)
SIPEXII_SI.index  = SIPEXII_SI.index  - pd.Timedelta(minutes=10)
SIPEXII_Hg.index  = SIPEXII_Hg.index  - pd.Timedelta(minutes=10)
SIPEXII_O3.index  = SIPEXII_O3.index  - pd.Timedelta(minutes=10)

#------------------------------------------------------------------------------
# Filter the datasets for midday hours only

#-----------------------
# SIPEXII (07:00 to 18:00)
#-----------------------
start_time = '07:00:00'
end_time   = '18:00:00'
# BrO
Midday     = (SIPEXII_BrO['Time'] >= start_time) & (SIPEXII_BrO['Time'] < end_time)
SIPEXII_MM = SIPEXII_BrO[Midday]
# VMR
start_time = pd.to_datetime('07:00:00').time()
end_time   = pd.to_datetime('18:00:00').time()
Midday_VMR = (SIPEXIITT['Time'] >= start_time) & (SIPEXIITT['Time'] < end_time)
SIPEXIIM   = SIPEXIITT[Midday_VMR]

#------------------------------------------------------------------------------
# Filter dataframe for when filter is less than 60%

# SIPEXII (2012)
SIPEXIIF = (SIPEXII_MM['Filter'] < 0.6)
SIPEXIIT = SIPEXII_MM[SIPEXIIF]

#------------------------------------------------------------------------------
# Filter the datasets based on the date

# SIPEXII (23 Sep to 11 Nov 2012)
start_date   = '2012-09-23'
end_date     = '2012-11-11'
# BrO
SIPEX_BrO    = (SIPEXIIT.index >= start_date) & (SIPEXIIT.index < end_date)
SIPEXIIT     = SIPEXIIT[SIPEX_BrO]
# VMR
SIPEX_VMR    = (SIPEXIIM.index >= start_date) & (SIPEXIIM.index < end_date)
SIPEXIIM     = SIPEXIIM[SIPEX_VMR]

#------------------------------------------------------------------------------
#  Sample the dataframe for only times corresponding to the BrO values

# SIPEXII (2012)
D1_SIPEXII = pd.merge(left=SIPEXIIM,   right=SIPEXII_Met, how='left', left_index=True, right_index=True)
D2_SIPEXII = pd.merge(left=D1_SIPEXII, right=SIPEXII_SI,  how='left', left_index=True, right_index=True)
D3_SIPEXII = pd.merge(left=D2_SIPEXII, right=SIPEXII_Hg,  how='left', left_index=True, right_index=True)
D4_SIPEXII = pd.merge(left=D3_SIPEXII, right=SIPEXII_O3,  how='left', left_index=True, right_index=True)

#------------------------------------------------------------------------------
# Calculate the Wind Speed average

WS_s_SIPEXII         = np.array(D4_SIPEXII['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXII         = np.array(D4_SIPEXII['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
D4_SIPEXII['WS_Avg'] = (WS_s_SIPEXII + WS_p_SIPEXII)/2 # Average the wind speed for port and starboard

#------------------------------------------------------------------------------
# Seperate the data into low (<=7 m/s) and high (>7 m/s) wind speeds

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

SIPEXII_LWS = (D4_SIPEXII['WS_Avg'] <= 7)
D4_SIPEXIIL = D4_SIPEXII[SIPEXII_LWS]

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

SIPEXII_HWS = (D4_SIPEXII['WS_Avg'] > 7)
D4_SIPEXIIH = D4_SIPEXII[SIPEXII_HWS]

#------------------------------------------------------------------------------
# Define the variables
#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# Surface Layer
BrO_SIPEXIILS = np.array(D4_SIPEXIIL[0.1]) * 1e6 # convert from ppmv to ppbv

# Boundary Layer
BrO_SIPEXIILB = np.array(D4_SIPEXIIL[0.3]) * 1e6 # convert from ppmv to ppbv

#--------------------------------
# O3 (ppb)

O3_SIPEXIIL = np.array(D4_SIPEXIIL['O3_(ppb)']) # O3 (ppb)

#--------------------------------
# Solar Radiation (W/m2)

Sol_s_SIPEXIIL         = np.array(D4_SIPEXIIL['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_SIPEXIIL         = np.array(D4_SIPEXIIL['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_SIPEXIIL['MeanSol'] = D4_SIPEXIIL[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_SIPEXIIL           = np.array(D4_SIPEXIIL['MeanSol'])

#--------------------------------
# Temperature (C)

Temp_s_SIPEXIIL         = np.array(D4_SIPEXIIL['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_SIPEXIIL         = np.array(D4_SIPEXIIL['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_SIPEXIIL['MeanTemp'] = D4_SIPEXIIL[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_SIPEXIIL           = np.array(D4_SIPEXIIL['MeanTemp'])

#--------------------------------
# Wind Direction

WD_s_SIPEXIIL = np.array(D4_SIPEXIIL['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_SIPEXIIL = np.array(D4_SIPEXIIL['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

#--------------------------------
# Wind Speed

WS_s_SIPEXIIL = np.array(D4_SIPEXIIL['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXIIL = np.array(D4_SIPEXIIL['WND_SPD_PORT_CORR_KNOT'])  * 0.514444444 # Convert from knots to m/s
WS_SIPEXIIL   = (WS_s_SIPEXIIL + WS_p_SIPEXIIL)/2 # Average the wind speed for port and starboard

#--------------------------------
# Vector Mean Wind Direction

WD_vect_SIPEXIIL = ((WD_s_SIPEXIIL * WS_s_SIPEXIIL) / (WS_s_SIPEXIIL + WS_p_SIPEXIIL)) + ((WD_p_SIPEXIIL * WS_p_SIPEXIIL) / (WS_s_SIPEXIIL + WS_p_SIPEXIIL)) # Calculate the vector mean wind direction

#--------------------------------
# Hg0

Hg0_SIPEXIIL = np.array(D4_SIPEXIIL['ng/m3']) # Hg0

#--------------------------------
# Sea Ice Concentration

SI_SIPEXIIL = np.array(D4_SIPEXIIL['Sea_Ice_Conc'])*100

#--------------------------------
# Relative Humidity

RH_s_SIPEXIIL = np.array(D4_SIPEXIIL['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_SIPEXIIL = np.array(D4_SIPEXIIL['REL_HUMIDITY_PORT_PERCENT'])
RH_SIPEXIIL   = (RH_s_SIPEXIIL + RH_p_SIPEXIIL)/2

#------------------------------------------------------------------------------
# Define the variables
#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# Surface Layer 
BrO_SIPEXIIHS = np.array(D4_SIPEXIIH[0.1]) * 1e6 # convert from ppmv to ppbv

# Boundary Layer 
BrO_SIPEXIIHB = np.array(D4_SIPEXIIH[0.3]) * 1e6 # convert from ppmv to ppbv

#--------------------------------
# O3 (ppb)

O3_SIPEXIIH = np.array(D4_SIPEXIIH['O3_(ppb)']) # O3 (ppb)

#--------------------------------
# Solar Radiation (W/m2)

Sol_s_SIPEXIIH         = np.array(D4_SIPEXIIH['RAD_SLR_STRBRD_WPERM2']) # starboard side solar radiation
Sol_p_SIPEXIIH         = np.array(D4_SIPEXIIH['RAD_SLR_PORT_WPERM2']) # port side solar radiation
D4_SIPEXIIH['MeanSol'] = D4_SIPEXIIH[['RAD_SLR_STRBRD_WPERM2','RAD_SLR_PORT_WPERM2']].mean(axis=1) # Average the solar radiation for port and starboard
Sol_SIPEXIIH           = np.array(D4_SIPEXIIH['MeanSol'])

#--------------------------------
# Temperature (C)

Temp_s_SIPEXIIH         = np.array(D4_SIPEXIIH['TEMP_AIR_STRBRD_DEGC']) # starboard side temperature
Temp_p_SIPEXIIH         = np.array(D4_SIPEXIIH['TEMP_AIR_PORT_DEGC']) # port side temperature
D4_SIPEXIIH['MeanTemp'] = D4_SIPEXIIH[['TEMP_AIR_STRBRD_DEGC','TEMP_AIR_PORT_DEGC']].mean(axis=1) # Average the temperature for port and starboard
Temp_SIPEXIIH           = np.array(D4_SIPEXIIH['MeanTemp'])

#--------------------------------
# Wind Direction

WD_s_SIPEXIIH = np.array(D4_SIPEXIIH['WND_DIR_STRBD_CORR_DEG']) # starboard side wind direction (correlated)
WD_p_SIPEXIIH = np.array(D4_SIPEXIIH['WND_DIR_PORT_CORR_DEG']) # port side wind direction (correlated)

#--------------------------------
# Wind Speed

WS_s_SIPEXIIH = np.array(D4_SIPEXIIH['WND_SPD_STRBD_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_p_SIPEXIIH = np.array(D4_SIPEXIIH['WND_SPD_PORT_CORR_KNOT']) * 0.514444444 # Convert from knots to m/s
WS_SIPEXIIH   = (WS_s_SIPEXIIH + WS_p_SIPEXIIH)/2 # Average the wind speed for port and starboard

#--------------------------------
# Vector Mean Wind Direction

WD_vect_SIPEXIIH = ((WD_s_SIPEXIIH * WS_s_SIPEXIIH) / (WS_s_SIPEXIIH + WS_p_SIPEXIIH)) + ((WD_p_SIPEXIIH * WS_p_SIPEXIIH) / (WS_s_SIPEXIIH + WS_p_SIPEXIIH)) # Calculate the vector mean wind direction

#--------------------------------
# Hg0

Hg0_SIPEXIIH = np.array(D4_SIPEXIIH['ng/m3']) # Hg0

#--------------------------------
# Sea Ice Concentration

SI_SIPEXIIH = np.array(D4_SIPEXIIH['Sea_Ice_Conc']) * 100

#--------------------------------
# Relative Humidity

RH_s_SIPEXIIH = np.array(D4_SIPEXIIH['REL_HUMIDITY_STRBRD_PERCENT'])
RH_p_SIPEXIIH = np.array(D4_SIPEXIIH['REL_HUMIDITY_PORT_PERCENT'])
RH_SIPEXIIH   = (RH_s_SIPEXIIH + RH_p_SIPEXIIH)/2

#------------------------------------------------------------------------------
# Concate the variables from each voyage

#-----------------------------
# Low Wind Speed (<=7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOLS    = BrO_SIPEXIILS

# BrO boundary volume mixing ratio (VMR)
BrOLB    = BrO_SIPEXIILB

# O3 (ppb)
O3L      = O3_SIPEXIIL

# Solar Radiation (W/m2)
SolL     = Sol_SIPEXIIL

# Temperature (C)
TempL    = Temp_SIPEXIIL

# Wind Speed
WSL      = WS_SIPEXIIL

# Vector Mean Wind Direction
WD_vectL = WD_vect_SIPEXIIL

# Hg0
Hg0L     = Hg0_SIPEXIIL

# Sea Ice Concentration
SIL      = SI_SIPEXIIL

# Relative Humidity
RHL      = RH_SIPEXIIL

#-----------------------------
# High Wind Speed (>7 m/s)
#-----------------------------

# BrO surface volume mixing ratio (VMR)
BrOHS    = BrO_SIPEXIIHS

# BrO boundary volume mixing ratio (VMR)
BrOHB    = BrO_SIPEXIIHB

# O3 (ppb)
O3H      = O3_SIPEXIIH

# Solar Radiation (W/m2)
SolH     = Sol_SIPEXIIH

# Temperature (C)
TempH    = Temp_SIPEXIIH

# Wind Speed
WSH      = WS_SIPEXIIH

# Vector Mean Wind Direction
WD_vectH = WD_vect_SIPEXIIH

# Hg0
Hg0H     = Hg0_SIPEXIIH

# Sea Ice Concentration
SIH      = SI_SIPEXIIH

# Relative Humidity
RHH      = RH_SIPEXIIH

#------------------------------------------------------------------------------
# Scan for NaN values
#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (BrO) 
SIPEXII_Y1maskLS   = np.isfinite(BrO_SIPEXIILS) # Scan for NaN values
BrO_SIPEXIILS      = BrO_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from BrO
O3_SIPEXIILS       = O3_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from Sol
Sol_SIPEXIILS      = Sol_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from Sol
Temp_SIPEXIILS     = Temp_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from Sol
WD_vect_SIPEXIILS  = WD_vect_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from Sol
WS_SIPEXIILS       = WS_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from Sol
Hg0_SIPEXIILS      = Hg0_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from Sol
SI_SIPEXIILS       = SI_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from Sol
RH_SIPEXIILS       = RH_SIPEXIIL[SIPEXII_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
SIPEXII_Y1maskLS   = np.isfinite(Sol_SIPEXIILS) # Scan for NaN values
BrO_SIPEXIILS      = BrO_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from BrO
O3_SIPEXIILS       = O3_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from Sol
Sol_SIPEXIILS      = Sol_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from Sol
Temp_SIPEXIILS     = Temp_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from Sol
WD_vect_SIPEXIILS  = WD_vect_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from Sol
WS_SIPEXIILS       = WS_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from Sol
Hg0_SIPEXIILS      = Hg0_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from Sol
SI_SIPEXIILS       = SI_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from Sol
RH_SIPEXIILS       = RH_SIPEXIILS[SIPEXII_Y1maskLS] # Remove NaN values from RH

# Pass 2 (Temp) 
SIPEXII_Y2maskLS   = np.isfinite(Temp_SIPEXIILS) # Scan for NaN values
BrO_Temp_SIPEXIILS = BrO_SIPEXIILS[SIPEXII_Y2maskLS] # Remove NaN values from BrO
Temp_SIPEXIILS     = Temp_SIPEXIILS[SIPEXII_Y2maskLS] # Remove NaN values from Temp
Sol_Temp_SIPEXIILS = Sol_SIPEXIILS[SIPEXII_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (WD_vect) 
SIPEXII_Y3maskLS   = np.isfinite(WD_vect_SIPEXIILS) # Scan for NaN values
BrO_WD_SIPEXIILS   = BrO_SIPEXIILS[SIPEXII_Y3maskLS] # Remove NaN values from BrO
WD_vect_SIPEXIILS  = WD_vect_SIPEXIILS[SIPEXII_Y3maskLS] # Remove NaN values from WD_vect
Sol_WD_SIPEXIILS   = Sol_SIPEXIILS[SIPEXII_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WS) 
SIPEXII_Y4maskLS   = np.isfinite(WS_SIPEXIILS) # Scan for NaN values
BrO_WS_SIPEXIILS   = BrO_SIPEXIILS[SIPEXII_Y4maskLS] # Remove NaN values from BrO
WS_SIPEXIILS       = WS_SIPEXIILS[SIPEXII_Y4maskLS] # Remove NaN values from WS
Sol_WS_SIPEXIILS   = Sol_SIPEXIILS[SIPEXII_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (Hg0) 
SIPEXII_Y5maskLS   = np.isfinite(Hg0_SIPEXIILS) # Scan for NaN values
BrO_Hg0_SIPEXIILS  = BrO_SIPEXIILS[SIPEXII_Y5maskLS] # Remove NaN values from BrO
Hg0_SIPEXIILS      = Hg0_SIPEXIILS[SIPEXII_Y5maskLS] # Remove NaN values from SI
Sol_Hg0_SIPEXIILS  = Sol_SIPEXIILS[SIPEXII_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (SI Field) 
SIPEXII_Y6maskLS   = np.isfinite(SI_SIPEXIILS) # Scan for NaN values
BrO_SI_SIPEXIILS   = BrO_SIPEXIILS[SIPEXII_Y6maskLS] # Remove NaN values from BrO
SI_SI_SIPEXIILS    = SI_SIPEXIILS[SIPEXII_Y6maskLS] # Remove NaN values from SI
Sol_SI_SIPEXIILS   = Sol_SIPEXIILS[SIPEXII_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (RH) 
SIPEXII_Y7maskLS   = np.isfinite(RH_SIPEXIILS) # Scan for NaN values
BrO_RH_SIPEXIILS   = BrO_SIPEXIILS[SIPEXII_Y7maskLS] # Remove NaN values from BrO
RH_SIPEXIILS       = RH_SIPEXIILS[SIPEXII_Y7maskLS] # Remove NaN values from WS
Sol_RH_SIPEXIILS   = Sol_SIPEXIILS[SIPEXII_Y7maskLS] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskLS  = np.isfinite(BrOLS) # Scan for NaN values
BrOLS         = BrOLS[ALL_Y1maskLS] # Remove NaN values from BrO
O3LS          = O3L[ALL_Y1maskLS] # Remove NaN values from Sol
SolLS         = SolL[ALL_Y1maskLS] # Remove NaN values from Sol
TempLS        = TempL[ALL_Y1maskLS] # Remove NaN values from Sol
WD_vectLS     = WD_vectL[ALL_Y1maskLS] # Remove NaN values from Sol
WSLS          = WSL[ALL_Y1maskLS] # Remove NaN values from Sol
Hg0LS         = Hg0L[ALL_Y1maskLS] # Remove NaN values from Sol
SILS          = SIL[ALL_Y1maskLS] # Remove NaN values from Sol
RHLS          = RHL[ALL_Y1maskLS] # Remove NaN values from RH

# Pass 1 (Sol) 
ALL_Y1maskLS  = np.isfinite(SolLS) # Scan for NaN values
BrOLS         = BrOLS[ALL_Y1maskLS] # Remove NaN values from BrO
O3LS          = O3LS[ALL_Y1maskLS] # Remove NaN values from Sol
SolLS         = SolLS[ALL_Y1maskLS] # Remove NaN values from Sol
TempLS        = TempLS[ALL_Y1maskLS] # Remove NaN values from Sol
WD_vectLS     = WD_vectLS[ALL_Y1maskLS] # Remove NaN values from Sol
WSLS          = WSLS[ALL_Y1maskLS] # Remove NaN values from Sol
Hg0LS         = Hg0LS[ALL_Y1maskLS] # Remove NaN values from Sol
SILS          = SILS[ALL_Y1maskLS] # Remove NaN values from Sol
RHLS          = RHLS[ALL_Y1maskLS] # Remove NaN values from RH

# Pass 2 (O3) 
ALL_Y2maskLS  = np.isfinite(O3LS) # Scan for NaN values
BrO_O3LS      = BrOLS[ALL_Y2maskLS] # Remove NaN values from BrO
O3LS          = O3LS[ALL_Y2maskLS] # Remove NaN values from Temp
Sol_O3LS      = SolLS[ALL_Y2maskLS] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskLS  = np.isfinite(TempLS) # Scan for NaN values
BrO_TempLS    = BrOLS[ALL_Y3maskLS] # Remove NaN values from BrO
TempLS        = TempLS[ALL_Y3maskLS] # Remove NaN values from Temp
Sol_TempLS    = SolLS[ALL_Y3maskLS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskLS  = np.isfinite(WD_vectLS) # Scan for NaN values
BrO_WDLS      = BrOLS[ALL_Y4maskLS] # Remove NaN values from BrO
WD_vectLS     = WD_vectLS[ALL_Y4maskLS] # Remove NaN values from WD_vect
Sol_WDLS      = SolLS[ALL_Y4maskLS] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskLS  = np.isfinite(WSLS) # Scan for NaN values
BrO_WSLS      = BrOLS[ALL_Y5maskLS] # Remove NaN values from BrO
WSLS          = WSLS[ALL_Y5maskLS] # Remove NaN values from WS
Sol_WSLS      = SolLS[ALL_Y5maskLS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskLS  = np.isfinite(Hg0LS) # Scan for NaN values
BrO_Hg0LS     = BrOLS[ALL_Y6maskLS] # Remove NaN values from BrO
Hg0LS         = Hg0LS[ALL_Y6maskLS] # Remove NaN values from SI
Sol_Hg0LS     = SolLS[ALL_Y6maskLS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskLS  = np.isfinite(SILS) # Scan for NaN values
BrO_SILS      = BrOLS[ALL_Y7maskLS] # Remove NaN values from BrO
SI_SILS       = SILS[ALL_Y7maskLS] # Remove NaN values from SI
Sol_SILS      = SolLS[ALL_Y7maskLS] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskLS  = np.isfinite(RHLS) # Scan for NaN values
BrO_RHLS      = BrOLS[ALL_Y8maskLS] # Remove NaN values from BrO
RHLS          = RHLS[ALL_Y8maskLS] # Remove NaN values from RH
Sol_RHLS      = SolLS[ALL_Y8maskLS] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#------------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (BrO) 
SIPEXII_Y1maskHS   = np.isfinite(BrO_SIPEXIIHS) # Scan for NaN values
BrO_SIPEXIIHS      = BrO_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from BrO
O3_SIPEXIIHS       = O3_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from Sol
Sol_SIPEXIIHS      = Sol_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from Sol
Temp_SIPEXIIHS     = Temp_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from Sol
WD_vect_SIPEXIIHS  = WD_vect_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from Sol
WS_SIPEXIIHS       = WS_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from Sol
Hg0_SIPEXIIHS      = Hg0_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from Sol
SI_SIPEXIIHS       = SI_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from Sol
RH_SIPEXIIHS       = RH_SIPEXIIH[SIPEXII_Y1maskHS] # Remove NaN values from RH

# Pass 1 (Sol) 
SIPEXII_Y1maskHS   = np.isfinite(Sol_SIPEXIIHS) # Scan for NaN values
BrO_SIPEXIIHS      = BrO_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from BrO
O3_SIPEXIIHS       = O3_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from Sol
Sol_SIPEXIIHS      = Sol_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from Sol
Temp_SIPEXIIHS     = Temp_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from Sol
WD_vect_SIPEXIIHS  = WD_vect_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from Sol
WS_SIPEXIIHS       = WS_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from Sol
Hg0_SIPEXIIHS      = Hg0_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from Sol
SI_SIPEXIIHS       = SI_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from Sol
RH_SIPEXIIHS       = RH_SIPEXIIHS[SIPEXII_Y1maskHS] # Remove NaN values from RH

# Pass 2 (Temp) 
SIPEXII_Y2maskHS   = np.isfinite(Temp_SIPEXIIHS) # Scan for NaN values
BrO_Temp_SIPEXIIHS = BrO_SIPEXIIHS[SIPEXII_Y2maskHS] # Remove NaN values from BrO
Temp_SIPEXIIHS     = Temp_SIPEXIIHS[SIPEXII_Y2maskHS] # Remove NaN values from Temp
Sol_Temp_SIPEXIIHS = Sol_SIPEXIIHS[SIPEXII_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (WD_vect) 
SIPEXII_Y3maskHS   = np.isfinite(WD_vect_SIPEXIIHS) # Scan for NaN values
BrO_WD_SIPEXIIHS   = BrO_SIPEXIIHS[SIPEXII_Y3maskHS] # Remove NaN values from BrO
WD_vect_SIPEXIIHS  = WD_vect_SIPEXIIHS[SIPEXII_Y3maskHS] # Remove NaN values from WD_vect
Sol_WD_SIPEXIIHS   = Sol_SIPEXIIHS[SIPEXII_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WS) 
SIPEXII_Y4maskHS   = np.isfinite(WS_SIPEXIIHS) # Scan for NaN values
BrO_WS_SIPEXIIHS   = BrO_SIPEXIIHS[SIPEXII_Y4maskHS] # Remove NaN values from BrO
WS_SIPEXIIHS       = WS_SIPEXIIHS[SIPEXII_Y4maskHS] # Remove NaN values from WS
Sol_WS_SIPEXIIHS   = Sol_SIPEXIIHS[SIPEXII_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (Hg0) 
SIPEXII_Y5maskHS   = np.isfinite(Hg0_SIPEXIIHS) # Scan for NaN values
BrO_Hg0_SIPEXIIHS  = BrO_SIPEXIIHS[SIPEXII_Y5maskHS] # Remove NaN values from BrO
Hg0_SIPEXIIHS      = Hg0_SIPEXIIHS[SIPEXII_Y5maskHS] # Remove NaN values from SI
Sol_Hg0_SIPEXIIHS  = Sol_SIPEXIIHS[SIPEXII_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (SI Field) 
SIPEXII_Y6maskHS   = np.isfinite(SI_SIPEXIIHS) # Scan for NaN values
BrO_SI_SIPEXIIHS   = BrO_SIPEXIIHS[SIPEXII_Y6maskHS] # Remove NaN values from BrO
SI_SI_SIPEXIIHS    = SI_SIPEXIIHS[SIPEXII_Y6maskHS] # Remove NaN values from SI
Sol_SI_SIPEXIIHS   = Sol_SIPEXIIHS[SIPEXII_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (RH) 
SIPEXII_Y7maskHS   = np.isfinite(RH_SIPEXIIHS) # Scan for NaN values
BrO_RH_SIPEXIIHS   = BrO_SIPEXIIHS[SIPEXII_Y7maskHS] # Remove NaN values from BrO
RH_SIPEXIIHS       = RH_SIPEXIIHS[SIPEXII_Y7maskHS] # Remove NaN values from WS
Sol_RH_SIPEXIIHS   = Sol_SIPEXIIHS[SIPEXII_Y7maskHS] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskHS   = np.isfinite(BrOHS) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHS] # Remove NaN values from BrO
O3HS           = O3H[ALL_Y1maskHS] # Remove NaN values from Sol
SolHS          = SolH[ALL_Y1maskHS] # Remove NaN values from Sol
TempHS         = TempH[ALL_Y1maskHS] # Remove NaN values from Sol
WD_vectHS      = WD_vectH[ALL_Y1maskHS] # Remove NaN values from Sol
WSHS           = WSH[ALL_Y1maskHS] # Remove NaN values from Sol
Hg0HS          = Hg0H[ALL_Y1maskHS] # Remove NaN values from Sol
SIHS           = SIH[ALL_Y1maskHS] # Remove NaN values from Sol
RHHS          = RHH[ALL_Y1maskHS] # Remove NaN values from WS

# Pass 1 (Sol) 
ALL_Y1maskHS   = np.isfinite(SolHS) # Scan for NaN values
BrOHS          = BrOHS[ALL_Y1maskHS] # Remove NaN values from BrO
O3HS           = O3HS[ALL_Y1maskHS] # Remove NaN values from Sol
SolHS          = SolHS[ALL_Y1maskHS] # Remove NaN values from Sol
TempHS         = TempHS[ALL_Y1maskHS] # Remove NaN values from Sol
WD_vectHS      = WD_vectHS[ALL_Y1maskHS] # Remove NaN values from Sol
WSHS           = WSHS[ALL_Y1maskHS] # Remove NaN values from Sol
Hg0HS          = Hg0HS[ALL_Y1maskHS] # Remove NaN values from Sol
SIHS           = SIHS[ALL_Y1maskHS] # Remove NaN values from Sol
RHHS          = RHHS[ALL_Y1maskHS] # Remove NaN values from WS

# Pass 2 (O3) 
ALL_Y2maskHS   = np.isfinite(O3HS) # Scan for NaN values
BrO_O3HS       = BrOHS[ALL_Y2maskHS] # Remove NaN values from BrO
O3HS           = O3HS[ALL_Y2maskHS] # Remove NaN values from Temp
Sol_O3HS       = SolHS[ALL_Y2maskHS] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskHS   = np.isfinite(TempHS) # Scan for NaN values
BrO_TempHS     = BrOHS[ALL_Y3maskHS] # Remove NaN values from BrO
TempHS         = TempHS[ALL_Y3maskHS] # Remove NaN values from Temp
Sol_TempS      = SolHS[ALL_Y3maskHS] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskHS   = np.isfinite(WD_vectHS) # Scan for NaN values
BrO_WDHS       = BrOHS[ALL_Y4maskHS] # Remove NaN values from BrO
WD_vectHS      = WD_vectHS[ALL_Y4maskHS] # Remove NaN values from WD_vect
Sol_WDHS       = SolHS[ALL_Y4maskHS] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskHS   = np.isfinite(WSHS) # Scan for NaN values
BrO_WSHS       = BrOHS[ALL_Y5maskHS] # Remove NaN values from BrO
WSHS           = WSHS[ALL_Y5maskHS] # Remove NaN values from WS
Sol_WSHS       = SolHS[ALL_Y5maskHS] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskHS   = np.isfinite(Hg0HS) # Scan for NaN values
BrO_Hg0HS      = BrOHS[ALL_Y6maskHS] # Remove NaN values from BrO
Hg0HS          = Hg0HS[ALL_Y6maskHS] # Remove NaN values from SI
Sol_Hg0HS      = SolHS[ALL_Y6maskHS] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskHS   = np.isfinite(SIHS) # Scan for NaN values
BrO_SIHS       = BrOHS[ALL_Y7maskHS] # Remove NaN values from BrO
SI_SIHS        = SIHS[ALL_Y7maskHS] # Remove NaN values from SI
Sol_SIHS       = SolHS[ALL_Y7maskHS] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskHS  = np.isfinite(RHHS) # Scan for NaN values
BrO_RHHS      = BrOHS[ALL_Y8maskHS] # Remove NaN values from BrO
RHHS          = RHHS[ALL_Y8maskHS] # Remove NaN values from WS
Sol_RHHS      = SolHS[ALL_Y8maskHS] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (BrO) 
SIPEXII_Y1maskLB   = np.isfinite(BrO_SIPEXIILB) # Scan for NaN values
BrO_SIPEXIILB      = BrO_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from BrO
O3_SIPEXIILB       = O3_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from Sol
Sol_SIPEXIILB      = Sol_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from Sol
Temp_SIPEXIILB     = Temp_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from Sol
WD_vect_SIPEXIILB  = WD_vect_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from Sol
WS_SIPEXIILB       = WS_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from Sol
Hg0_SIPEXIILB      = Hg0_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from Sol
SI_SIPEXIILB       = SI_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from Sol
RH_SIPEXIILB       = RH_SIPEXIIL[SIPEXII_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
SIPEXII_Y1maskLB   = np.isfinite(Sol_SIPEXIILB) # Scan for NaN values
BrO_SIPEXIILB      = BrO_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from BrO
O3_SIPEXIILB       = O3_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from Sol
Sol_SIPEXIILB      = Sol_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from Sol
Temp_SIPEXIILB     = Temp_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from Sol
WD_vect_SIPEXIILB  = WD_vect_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from Sol
WS_SIPEXIILB       = WS_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from Sol
Hg0_SIPEXIILB      = Hg0_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from Sol
SI_SIPEXIILB       = SI_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from Sol
RH_SIPEXIILB       = RH_SIPEXIILB[SIPEXII_Y1maskLB] # Remove NaN values from RH

# Pass 2 (Temp) 
SIPEXII_Y2maskLB   = np.isfinite(Temp_SIPEXIILB) # Scan for NaN values
BrO_Temp_SIPEXIILB = BrO_SIPEXIILB[SIPEXII_Y2maskLB] # Remove NaN values from BrO
Temp_SIPEXIILB     = Temp_SIPEXIILB[SIPEXII_Y2maskLB] # Remove NaN values from Temp
Sol_Temp_SIPEXIILB = Sol_SIPEXIILB[SIPEXII_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (WD_vect) 
SIPEXII_Y3maskLB   = np.isfinite(WD_vect_SIPEXIILB) # Scan for NaN values
BrO_WD_SIPEXIILB   = BrO_SIPEXIILB[SIPEXII_Y3maskLB] # Remove NaN values from BrO
WD_vect_SIPEXIILB  = WD_vect_SIPEXIILB[SIPEXII_Y3maskLB] # Remove NaN values from WD_vect
Sol_WD_SIPEXIILB   = Sol_SIPEXIILB[SIPEXII_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WS) 
SIPEXII_Y4maskLB   = np.isfinite(WS_SIPEXIILB) # Scan for NaN values
BrO_WS_SIPEXIILB   = BrO_SIPEXIILB[SIPEXII_Y4maskLB] # Remove NaN values from BrO
WS_SIPEXIILB       = WS_SIPEXIILB[SIPEXII_Y4maskLB] # Remove NaN values from WS
Sol_WS_SIPEXIILB   = Sol_SIPEXIILB[SIPEXII_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (Hg0) 
SIPEXII_Y5maskLB   = np.isfinite(Hg0_SIPEXIILB) # Scan for NaN values
BrO_Hg0_SIPEXIILB  = BrO_SIPEXIILB[SIPEXII_Y5maskLB] # Remove NaN values from BrO
Hg0_SIPEXIILB      = Hg0_SIPEXIILB[SIPEXII_Y5maskLB] # Remove NaN values from SI
Sol_Hg0_SIPEXIILB  = Sol_SIPEXIILB[SIPEXII_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (SI Field) 
SIPEXII_Y6maskLB   = np.isfinite(SI_SIPEXIILB) # Scan for NaN values
BrO_SI_SIPEXIILB   = BrO_SIPEXIILB[SIPEXII_Y6maskLB] # Remove NaN values from BrO
SI_SI_SIPEXIILB    = SI_SIPEXIILB[SIPEXII_Y6maskLB] # Remove NaN values from SI
Sol_SI_SIPEXIILB   = Sol_SIPEXIILB[SIPEXII_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (RH) 
SIPEXII_Y7maskLB   = np.isfinite(RH_SIPEXIILB) # Scan for NaN values
BrO_RH_SIPEXIILB   = BrO_SIPEXIILB[SIPEXII_Y7maskLB] # Remove NaN values from BrO
RH_SIPEXIILB       = RH_SIPEXIILB[SIPEXII_Y7maskLB] # Remove NaN values from WS
Sol_RH_SIPEXIILB   = Sol_SIPEXIILB[SIPEXII_Y7maskLB] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskLB  = np.isfinite(BrOLB) # Scan for NaN values
BrOLB         = BrOLB[ALL_Y1maskLB] # Remove NaN values from BrO
O3LB          = O3L[ALL_Y1maskLB] # Remove NaN values from Sol
SolLB         = SolL[ALL_Y1maskLB] # Remove NaN values from Sol
TempLB        = TempL[ALL_Y1maskLB] # Remove NaN values from Sol
WD_vectLB     = WD_vectL[ALL_Y1maskLB] # Remove NaN values from Sol
WSLB          = WSL[ALL_Y1maskLB] # Remove NaN values from Sol
Hg0LB         = Hg0L[ALL_Y1maskLB] # Remove NaN values from Sol
SILB          = SIL[ALL_Y1maskLB] # Remove NaN values from Sol
RHLB          = RHL[ALL_Y1maskLB] # Remove NaN values from RH

# Pass 1 (Sol) 
ALL_Y1maskLB  = np.isfinite(SolLB) # Scan for NaN values
BrOLB         = BrOLB[ALL_Y1maskLB] # Remove NaN values from BrO
O3LB          = O3LB[ALL_Y1maskLB] # Remove NaN values from Sol
SolLB         = SolLB[ALL_Y1maskLB] # Remove NaN values from Sol
TempLB        = TempLB[ALL_Y1maskLB] # Remove NaN values from Sol
WD_vectLB     = WD_vectLB[ALL_Y1maskLB] # Remove NaN values from Sol
WSLB          = WSLB[ALL_Y1maskLB] # Remove NaN values from Sol
Hg0LB         = Hg0LB[ALL_Y1maskLB] # Remove NaN values from Sol
SILB          = SILB[ALL_Y1maskLB] # Remove NaN values from Sol
RHLB          = RHLB[ALL_Y1maskLB] # Remove NaN values from RH

# Pass 2 (O3) 
ALL_Y2maskLB  = np.isfinite(O3LB) # Scan for NaN values
BrO_O3LB      = BrOLB[ALL_Y2maskLB] # Remove NaN values from BrO
O3LB          = O3LB[ALL_Y2maskLB] # Remove NaN values from Temp
Sol_O3LB      = SolLB[ALL_Y2maskLB] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskLB  = np.isfinite(TempLB) # Scan for NaN values
BrO_TempLB    = BrOLB[ALL_Y3maskLB] # Remove NaN values from BrO
TempLB        = TempLB[ALL_Y3maskLB] # Remove NaN values from Temp
Sol_TempLB    = SolLB[ALL_Y3maskLB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskLB  = np.isfinite(WD_vectLB) # Scan for NaN values
BrO_WDLB      = BrOLB[ALL_Y4maskLB] # Remove NaN values from BrO
WD_vectLB     = WD_vectLB[ALL_Y4maskLB] # Remove NaN values from WD_vect
Sol_WDLB      = SolLB[ALL_Y4maskLB] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskLB  = np.isfinite(WSLB) # Scan for NaN values
BrO_WSLB      = BrOLB[ALL_Y5maskLB] # Remove NaN values from BrO
WSLB          = WSLB[ALL_Y5maskLB] # Remove NaN values from WS
Sol_WSLB      = SolLB[ALL_Y5maskLB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskLB  = np.isfinite(Hg0LB) # Scan for NaN values
BrO_Hg0LB     = BrOLB[ALL_Y6maskLB] # Remove NaN values from BrO
Hg0LB         = Hg0LB[ALL_Y6maskLB] # Remove NaN values from SI
Sol_Hg0LB     = SolLB[ALL_Y6maskLB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskLB  = np.isfinite(SILB) # Scan for NaN values
BrO_SILB      = BrOLB[ALL_Y7maskLB] # Remove NaN values from BrO
SI_SILB       = SILB[ALL_Y7maskLB] # Remove NaN values from SI
Sol_SILB      = SolLB[ALL_Y7maskLB] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskLB  = np.isfinite(RHLB) # Scan for NaN values
BrO_RHLB      = BrOLB[ALL_Y8maskLB] # Remove NaN values from BrO
RHLB          = RHLB[ALL_Y8maskLB] # Remove NaN values from RH
Sol_RHLB      = SolLB[ALL_Y8maskLB] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Scan for NaN values
#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# Pass 1 (BrO) 
SIPEXII_Y1maskHB   = np.isfinite(BrO_SIPEXIIHB) # Scan for NaN values
BrO_SIPEXIIHB      = BrO_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from BrO
O3_SIPEXIIHB       = O3_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from Sol
Sol_SIPEXIIHB      = Sol_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from Sol
Temp_SIPEXIIHB     = Temp_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from Sol
WD_vect_SIPEXIIHB  = WD_vect_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from Sol
WS_SIPEXIIHB       = WS_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from Sol
Hg0_SIPEXIIHB      = Hg0_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from Sol
SI_SIPEXIIHB       = SI_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from Sol
RH_SIPEXIIHB       = RH_SIPEXIIH[SIPEXII_Y1maskHB] # Remove NaN values from RH

# Pass 1 (Sol) 
SIPEXII_Y1maskHB   = np.isfinite(Sol_SIPEXIIHB) # Scan for NaN values
BrO_SIPEXIIHB      = BrO_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from BrO
O3_SIPEXIIHB       = O3_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from Sol
Sol_SIPEXIIHB      = Sol_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from Sol
Temp_SIPEXIIHB     = Temp_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from Sol
WD_vect_SIPEXIIHB  = WD_vect_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from Sol
WS_SIPEXIIHB       = WS_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from Sol
Hg0_SIPEXIIHB      = Hg0_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from Sol
SI_SIPEXIIHB       = SI_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from Sol
RH_SIPEXIIHB       = RH_SIPEXIIHB[SIPEXII_Y1maskHB] # Remove NaN values from RH

# Pass 2 (Temp) 
SIPEXII_Y2maskHB   = np.isfinite(Temp_SIPEXIIHB) # Scan for NaN values
BrO_Temp_SIPEXIIHB = BrO_SIPEXIIHB[SIPEXII_Y2maskHB] # Remove NaN values from BrO
Temp_SIPEXIIHB     = Temp_SIPEXIIHB[SIPEXII_Y2maskHB] # Remove NaN values from Temp
Sol_Temp_SIPEXIIHB = Sol_SIPEXIIHB[SIPEXII_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (WD_vect) 
SIPEXII_Y3maskHB   = np.isfinite(WD_vect_SIPEXIIHB) # Scan for NaN values
BrO_WD_SIPEXIIHB   = BrO_SIPEXIIHB[SIPEXII_Y3maskHB] # Remove NaN values from BrO
WD_vect_SIPEXIIHB  = WD_vect_SIPEXIIHB[SIPEXII_Y3maskHB] # Remove NaN values from WD_vect
Sol_WD_SIPEXIIHB   = Sol_SIPEXIIHB[SIPEXII_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WS) 
SIPEXII_Y4maskHB   = np.isfinite(WS_SIPEXIIHB) # Scan for NaN values
BrO_WS_SIPEXIIHB   = BrO_SIPEXIIHB[SIPEXII_Y4maskHB] # Remove NaN values from BrO
WS_SIPEXIIHB       = WS_SIPEXIIHB[SIPEXII_Y4maskHB] # Remove NaN values from WS
Sol_WS_SIPEXIIHB   = Sol_SIPEXIIHB[SIPEXII_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (Hg0) 
SIPEXII_Y5maskHB   = np.isfinite(Hg0_SIPEXIIHB) # Scan for NaN values
BrO_Hg0_SIPEXIIHB  = BrO_SIPEXIIHB[SIPEXII_Y5maskHB] # Remove NaN values from BrO
Hg0_SIPEXIIHB      = Hg0_SIPEXIIHB[SIPEXII_Y5maskHB] # Remove NaN values from SI
Sol_Hg0_SIPEXIIHB  = Sol_SIPEXIIHB[SIPEXII_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (SI Field) 
SIPEXII_Y6maskHB   = np.isfinite(SI_SIPEXIIHB) # Scan for NaN values
BrO_SI_SIPEXIIHB   = BrO_SIPEXIIHB[SIPEXII_Y6maskHB] # Remove NaN values from BrO
SI_SI_SIPEXIIHB    = SI_SIPEXIIHB[SIPEXII_Y6maskHB] # Remove NaN values from SI
Sol_SI_SIPEXIIHB   = Sol_SIPEXIIHB[SIPEXII_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (RH) 
SIPEXII_Y7maskHB   = np.isfinite(RH_SIPEXIIHB) # Scan for NaN values
BrO_RH_SIPEXIIHB   = BrO_SIPEXIIHB[SIPEXII_Y7maskHB] # Remove NaN values from BrO
RH_SIPEXIIHB       = RH_SIPEXIIHB[SIPEXII_Y7maskHB] # Remove NaN values from WS
Sol_RH_SIPEXIIHB   = Sol_SIPEXIIHB[SIPEXII_Y7maskHB] # Remove NaN values from Sol

#--------------------------------
# COMBINED
#--------------------------------
# Pass 1 (BrO) 
ALL_Y1maskHB   = np.isfinite(BrOHB) # Scan for NaN values
BrOHB          = BrOHB[ALL_Y1maskHB] # Remove NaN values from BrO
O3HB           = O3H[ALL_Y1maskHB] # Remove NaN values from Sol
SolHB          = SolH[ALL_Y1maskHB] # Remove NaN values from Sol
TempHB         = TempH[ALL_Y1maskHB] # Remove NaN values from Sol
WD_vectHB      = WD_vectH[ALL_Y1maskHB] # Remove NaN values from Sol
WSHB           = WSH[ALL_Y1maskHB] # Remove NaN values from Sol
Hg0HB          = Hg0H[ALL_Y1maskHB] # Remove NaN values from Sol
SIHB           = SIH[ALL_Y1maskHB] # Remove NaN values from Sol
RHHB          = RHH[ALL_Y1maskHB] # Remove NaN values from WS

# Pass 1 (Sol) 
ALL_Y1maskHB   = np.isfinite(SolHB) # Scan for NaN values
BrOHB          = BrOHB[ALL_Y1maskHB] # Remove NaN values from BrO
O3HB           = O3HB[ALL_Y1maskHB] # Remove NaN values from Sol
SolHB          = SolHB[ALL_Y1maskHB] # Remove NaN values from Sol
TempHB         = TempHB[ALL_Y1maskHB] # Remove NaN values from Sol
WD_vectHB      = WD_vectHB[ALL_Y1maskHB] # Remove NaN values from Sol
WSHB           = WSHB[ALL_Y1maskHB] # Remove NaN values from Sol
Hg0HB          = Hg0HB[ALL_Y1maskHB] # Remove NaN values from Sol
SIHB           = SIHB[ALL_Y1maskHB] # Remove NaN values from Sol
RHHB          = RHHB[ALL_Y1maskHB] # Remove NaN values from WS

# Pass 2 (O3) 
ALL_Y2maskHB   = np.isfinite(O3HB) # Scan for NaN values
BrO_O3HB       = BrOHB[ALL_Y2maskHB] # Remove NaN values from BrO
O3HB           = O3HB[ALL_Y2maskHB] # Remove NaN values from Temp
Sol_O3HB       = SolHB[ALL_Y2maskHB] # Remove NaN values from Sol

# Pass 3 (Temp) 
ALL_Y3maskHB   = np.isfinite(TempHB) # Scan for NaN values
BrO_TempHB     = BrOHB[ALL_Y3maskHB] # Remove NaN values from BrO
TempHB         = TempHB[ALL_Y3maskHB] # Remove NaN values from Temp
Sol_TempHB      = SolHB[ALL_Y3maskHB] # Remove NaN values from Sol

# Pass 4 (WD_vect) 
ALL_Y4maskHB   = np.isfinite(WD_vectHB) # Scan for NaN values
BrO_WDHB       = BrOHB[ALL_Y4maskHB] # Remove NaN values from BrO
WD_vectHB      = WD_vectHB[ALL_Y4maskHB] # Remove NaN values from WD_vect
Sol_WDHB       = SolHB[ALL_Y4maskHB] # Remove NaN values from Sol

# Pass 5 (WS) 
ALL_Y5maskHB   = np.isfinite(WSHB) # Scan for NaN values
BrO_WSHB       = BrOHB[ALL_Y5maskHB] # Remove NaN values from BrO
WSHB           = WSHB[ALL_Y5maskHB] # Remove NaN values from WS
Sol_WSHB       = SolHB[ALL_Y5maskHB] # Remove NaN values from Sol

# Pass 6 (Hg0) 
ALL_Y6maskHB   = np.isfinite(Hg0HB) # Scan for NaN values
BrO_Hg0HB      = BrOHB[ALL_Y6maskHB] # Remove NaN values from BrO
Hg0HB          = Hg0HB[ALL_Y6maskHB] # Remove NaN values from SI
Sol_Hg0HB      = SolHB[ALL_Y6maskHB] # Remove NaN values from Sol

# Pass 7 (SI Field) 
ALL_Y7maskHB   = np.isfinite(SIHB) # Scan for NaN values
BrO_SIHB       = BrOHB[ALL_Y7maskHB] # Remove NaN values from BrO
SI_SIHB        = SIHB[ALL_Y7maskHB] # Remove NaN values from SI
Sol_SIHB       = SolHB[ALL_Y7maskHB] # Remove NaN values from Sol

# Pass 8 (RH) 
ALL_Y8maskHB  = np.isfinite(RHHB) # Scan for NaN values
BrO_RHHB      = BrOHB[ALL_Y8maskHB] # Remove NaN values from BrO
RHHB          = RHHB[ALL_Y8maskHB] # Remove NaN values from WS
Sol_RHHB      = SolHB[ALL_Y8maskHB] # Remove NaN values from Sol

#------------------------------------------------------------------------------
# Calculate the Coefficient of Correlation (r)
#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_SIPEXIILS, p_valueD1_SIPEXIILS = stats.pearsonr(O3_SIPEXIILS,BrO_SIPEXIILS)
slopeD1_SIPEXIILS, interceptD1_SIPEXIILS, rD1_SIPEXIILS, pD1_SIPEXIILS, std_errD1_SIPEXIILS = stats.linregress(O3_SIPEXIILS,BrO_SIPEXIILS)

# 2) Between Temp and BrO
r_rowD2_SIPEXIILS, p_valueD2_SIPEXIILS = stats.pearsonr(Temp_SIPEXIILS,BrO_SIPEXIILS)
slopeD2_SIPEXIILS, interceptD2_SIPEXIILS, rD2_SIPEXIILS, pD2_SIPEXIILS, std_errD2_SIPEXIILS = stats.linregress(Temp_SIPEXIILS,BrO_SIPEXIILS)

# 3) Between Wind Direction and BrO
r_rowD3_SIPEXIILS, p_valueD3_SIPEXIILS = stats.pearsonr(WD_vect_SIPEXIILS,BrO_WD_SIPEXIILS)
slopeD3_SIPEXIILS, interceptD3_SIPEXIILS, rD3_SIPEXIILS, pD3_SIPEXIILS, std_errD3_SIPEXIILS = stats.linregress(WD_vect_SIPEXIILS,BrO_WD_SIPEXIILS)

# 4) Between Wind Speed and BrO
r_rowD4_SIPEXIILS, p_valueD4_SIPEXIILS = stats.pearsonr(WS_SIPEXIILS,BrO_WS_SIPEXIILS)
slopeD4_SIPEXIILS, interceptD4_SIPEXIILS, rD4_SIPEXIILS, pD4_SIPEXIILS, std_errD4_SIPEXIILS = stats.linregress(WS_SIPEXIILS,BrO_WS_SIPEXIILS)

# 5) Between Solar Radiation and BrO
r_rowD5_SIPEXIILS, p_valueD5_SIPEXIILS = stats.pearsonr(Sol_SIPEXIILS,BrO_SIPEXIILS)
slopeD5_SIPEXIILS, interceptD5_SIPEXIILS, rD5_SIPEXIILS, pD5_SIPEXIILS, std_errD5_SIPEXIILS = stats.linregress(Sol_SIPEXIILS,BrO_SIPEXIILS)

# 6) Between Hg0 and BrO
r_rowD6_SIPEXIILS, p_valueD6_SIPEXIILS = stats.pearsonr(Hg0_SIPEXIILS,BrO_Hg0_SIPEXIILS)
slopeD6_SIPEXIILS, interceptD6_SIPEXIILS, rD6_SIPEXIILS, pD6_SIPEXIILS, std_errD6_SIPEXIILS = stats.linregress(Hg0_SIPEXIILS,BrO_Hg0_SIPEXIILS)

# 7) Between SI and BrO
r_rowD7_SIPEXIILS, p_valueD7_SIPEXIILS = stats.pearsonr(SI_SI_SIPEXIILS,BrO_SI_SIPEXIILS)
slopeD7_SIPEXIILS, interceptD7_SIPEXIILS, rD7_SIPEXIILS, pD7_SIPEXIILS, std_errD7_SIPEXIILS = stats.linregress(SI_SI_SIPEXIILS,BrO_SI_SIPEXIILS)

# 8) Between RH and BrO
r_rowD8_SIPEXIILS, p_valueD8_SIPEXIILS = stats.pearsonr(RH_SIPEXIILS,BrO_RH_SIPEXIILS)
slopeD8_SIPEXIILS, interceptD8_SIPEXIILS, rD8_SIPEXIILS, pD8_SIPEXIILS, std_errD8_SIPEXIILS = stats.linregress(RH_SIPEXIILS,BrO_RH_SIPEXIILS)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1LS, p_valueD1LS = stats.pearsonr(O3LS,BrO_O3LS)
slopeD1LS, interceptD1LS, rD1LS, pD1LS, std_errD1LS = stats.linregress(O3LS,BrO_O3LS)

# 2) Between Temp and BrO
r_rowD2LS, p_valueD2LS = stats.pearsonr(TempLS,BrOLS)
slopeD2LS, interceptD2LS, rD2LS, pD2LS, std_errD2LS = stats.linregress(TempLS,BrOLS)

# 3) Between Wind Direction and BrO
r_rowD3LS, p_valueD3LS = stats.pearsonr(WD_vectLS,BrO_WDLS)
slopeD3LS, interceptD3LS, rD3LS, pD3LS, std_errD3LS = stats.linregress(WD_vectLS,BrO_WDLS)

# 4) Between Wind Speed and BrO
r_rowD4LS, p_valueD4LS = stats.pearsonr(WSLS,BrO_WSLS)
slopeD4LS, interceptD4LS, rD4LS, pD4LS, std_errD4LS = stats.linregress(WSLS,BrO_WSLS)

# 5) Between Solar Radiation and BrO
r_rowD5LS, p_valueD5LS = stats.pearsonr(SolLS,BrOLS)
slopeD5LS, interceptD5LS, rD5LS, pD5LS, std_errD5LS = stats.linregress(SolLS,BrOLS)

# 6) Between Hg0 and BrO
r_rowD6LS, p_valueD6LS = stats.pearsonr(Hg0LS,BrO_Hg0LS)
slopeD6LS, interceptD6LS, rD6LS, pD6LS, std_errD6LS = stats.linregress(Hg0LS,BrO_Hg0LS)

# 7) Between SI and BrO
r_rowD7LS, p_valueD7LS = stats.pearsonr(SI_SILS,BrO_SILS)
slopeD7LS, interceptD7LS, rD7LS, pD7LS, std_errD7LS = stats.linregress(SI_SILS,BrO_SILS)

# 8) Between SI and BrO
r_rowD8LS, p_valueD8LS = stats.pearsonr(RHLS,BrO_RHLS)
slopeD8LS, interceptD8LS, rD8LS, pD8LS, std_errD8LS = stats.linregress(RHLS,BrO_RHLS)

#------------------------------------------------------------------------------
#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_SIPEXIIHS, p_valueD1_SIPEXIIHS = stats.pearsonr(O3_SIPEXIIHS,BrO_SIPEXIIHS)
slopeD1_SIPEXIIHS, interceptD1_SIPEXIIHS, rD1_SIPEXIIHS, pD1_SIPEXIIHS, std_errD1_SIPEXIIHS = stats.linregress(O3_SIPEXIIHS,BrO_SIPEXIIHS)

# 2) Between Temp and BrO
r_rowD2_SIPEXIIHS, p_valueD2_SIPEXIIHS = stats.pearsonr(Temp_SIPEXIIHS,BrO_SIPEXIIHS)
slopeD2_SIPEXIIHS, interceptD2_SIPEXIIHS, rD2_SIPEXIIHS, pD2_SIPEXIIHS, std_errD2_SIPEXIIHS = stats.linregress(Temp_SIPEXIIHS,BrO_SIPEXIIHS)

# 3) Between Wind Direction and BrO
r_rowD3_SIPEXIIHS, p_valueD3_SIPEXIIHS = stats.pearsonr(WD_vect_SIPEXIIHS,BrO_WD_SIPEXIIHS)
slopeD3_SIPEXIIHS, interceptD3_SIPEXIIHS, rD3_SIPEXIIHS, pD3_SIPEXIIHS, std_errD3_SIPEXIIHS = stats.linregress(WD_vect_SIPEXIIHS,BrO_WD_SIPEXIIHS)

# 4) Between Wind Speed and BrO
r_rowD4_SIPEXIIHS, p_valueD4_SIPEXIIHS = stats.pearsonr(WS_SIPEXIIHS,BrO_WS_SIPEXIIHS)
slopeD4_SIPEXIIHS, interceptD4_SIPEXIIHS, rD4_SIPEXIIHS, pD4_SIPEXIIHS, std_errD4_SIPEXIIHS = stats.linregress(WS_SIPEXIIHS,BrO_WS_SIPEXIIHS)

# 5) Between Solar Radiation and BrO
r_rowD5_SIPEXIIHS, p_valueD5_SIPEXIIHS = stats.pearsonr(Sol_SIPEXIIHS,BrO_SIPEXIIHS)
slopeD5_SIPEXIIHS, interceptD5_SIPEXIIHS, rD5_SIPEXIIHS, pD5_SIPEXIIHS, std_errD5_SIPEXIIHS = stats.linregress(Sol_SIPEXIIHS,BrO_SIPEXIIHS)

# 6) Between Hg0 and BrO
r_rowD6_SIPEXIIHS, p_valueD6_SIPEXIIHS = stats.pearsonr(Hg0_SIPEXIIHS,BrO_Hg0_SIPEXIIHS)
slopeD6_SIPEXIIHS, interceptD6_SIPEXIIHS, rD6_SIPEXIIHS, pD6_SIPEXIIHS, std_errD6_SIPEXIIHS = stats.linregress(Hg0_SIPEXIIHS,BrO_Hg0_SIPEXIIHS)

# 7) Between SI and BrO
r_rowD7_SIPEXIIHS, p_valueD7_SIPEXIIHS = stats.pearsonr(SI_SI_SIPEXIIHS,BrO_SI_SIPEXIIHS)
slopeD7_SIPEXIIHS, interceptD7_SIPEXIIHS, rD7_SIPEXIIHS, pD7_SIPEXIIHS, std_errD7_SIPEXIIHS = stats.linregress(SI_SI_SIPEXIIHS,BrO_SI_SIPEXIIHS)

# 8) Between RH and BrO
r_rowD8_SIPEXIIHS, p_valueD8_SIPEXIIHS = stats.pearsonr(RH_SIPEXIIHS,BrO_RH_SIPEXIIHS)
slopeD8_SIPEXIIHS, interceptD8_SIPEXIIHS, rD8_SIPEXIIHS, pD8_SIPEXIIHS, std_errD8_SIPEXIIHS = stats.linregress(RH_SIPEXIIHS,BrO_RH_SIPEXIIHS)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1HS, p_valueD1HS = stats.pearsonr(O3HS,BrO_O3HS)
slopeD1HS, interceptD1HS, rD1HS, pD1HS, std_errD1HS = stats.linregress(O3HS,BrO_O3HS)

# 2) Between Temp and BrO
r_rowD2HS, p_valueD2HS = stats.pearsonr(TempHS,BrOHS)
slopeD2HS, interceptD2HS, rD2HS, pD2HS, std_errD2HS = stats.linregress(TempHS,BrOHS)

# 3) Between Wind Direction and BrO
r_rowD3HS, p_valueD3HS = stats.pearsonr(WD_vectHS,BrO_WDHS)
slopeD3HS, interceptD3HS, rD3HS, pD3HS, std_errD3HS = stats.linregress(WD_vectHS,BrO_WDHS)

# 4) Between Wind Speed and BrO
r_rowD4HS, p_valueD4HS = stats.pearsonr(WSHS,BrO_WSHS)
slopeD4HS, interceptD4HS, rD4HS, pD4HS, std_errD4HS = stats.linregress(WSHS,BrO_WSHS)

# 5) Between Solar Radiation and BrO
r_rowD5HS, p_valueD5HS = stats.pearsonr(SolHS,BrOHS)
slopeD5HS, interceptD5HS, rD5HS, pD5HS, std_errD5HS = stats.linregress(SolHS,BrOHS)

# 6) Between Hg0 and BrO
r_rowD6HS, p_valueD6HS = stats.pearsonr(Hg0HS,BrO_Hg0HS)
slopeD6HS, interceptD6HS, rD6HS, pD6HS, std_errD6HS = stats.linregress(Hg0HS,BrO_Hg0HS)

# 7) Between SI and BrO
r_rowD7HS, p_valueD7HS = stats.pearsonr(SI_SIHS,BrO_SIHS)
slopeD7HS, interceptD7HS, rD7HS, pD7HS, std_errD7HS = stats.linregress(SI_SIHS,BrO_SIHS)

# 8) Between SI and BrO
r_rowD8HS, p_valueD8HS = stats.pearsonr(RHHS,BrO_RHHS)
slopeD8HS, interceptD8HS, rD8HS, pD8HS, std_errD8HS = stats.linregress(RHHS,BrO_RHHS)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#-----------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_SIPEXIILB, p_valueD1_SIPEXIILB = stats.pearsonr(O3_SIPEXIILB,BrO_SIPEXIILB)
slopeD1_SIPEXIILB, interceptD1_SIPEXIILB, rD1_SIPEXIILB, pD1_SIPEXIILB, std_errD1_SIPEXIILB = stats.linregress(O3_SIPEXIILB,BrO_SIPEXIILB)

# 2) Between Temp and BrO
r_rowD2_SIPEXIILB, p_valueD2_SIPEXIILB = stats.pearsonr(Temp_SIPEXIILB,BrO_SIPEXIILB)
slopeD2_SIPEXIILB, interceptD2_SIPEXIILB, rD2_SIPEXIILB, pD2_SIPEXIILB, std_errD2_SIPEXIILB = stats.linregress(Temp_SIPEXIILB,BrO_SIPEXIILB)

# 3) Between Wind Direction and BrO
r_rowD3_SIPEXIILB, p_valueD3_SIPEXIILB = stats.pearsonr(WD_vect_SIPEXIILB,BrO_WD_SIPEXIILB)
slopeD3_SIPEXIILB, interceptD3_SIPEXIILB, rD3_SIPEXIILB, pD3_SIPEXIILB, std_errD3_SIPEXIILB = stats.linregress(WD_vect_SIPEXIILB,BrO_WD_SIPEXIILB)

# 4) Between Wind Speed and BrO
r_rowD4_SIPEXIILB, p_valueD4_SIPEXIILB = stats.pearsonr(WS_SIPEXIILB,BrO_WS_SIPEXIILB)
slopeD4_SIPEXIILB, interceptD4_SIPEXIILB, rD4_SIPEXIILB, pD4_SIPEXIILB, std_errD4_SIPEXIILB = stats.linregress(WS_SIPEXIILB,BrO_WS_SIPEXIILB)

# 5) Between Solar Radiation and BrO
r_rowD5_SIPEXIILB, p_valueD5_SIPEXIILB = stats.pearsonr(Sol_SIPEXIILB,BrO_SIPEXIILB)
slopeD5_SIPEXIILB, interceptD5_SIPEXIILB, rD5_SIPEXIILB, pD5_SIPEXIILB, std_errD5_SIPEXIILB = stats.linregress(Sol_SIPEXIILB,BrO_SIPEXIILB)

# 6) Between Hg0 and BrO
r_rowD6_SIPEXIILB, p_valueD6_SIPEXIILB = stats.pearsonr(Hg0_SIPEXIILB,BrO_Hg0_SIPEXIILB)
slopeD6_SIPEXIILB, interceptD6_SIPEXIILB, rD6_SIPEXIILB, pD6_SIPEXIILB, std_errD6_SIPEXIILB = stats.linregress(Hg0_SIPEXIILB,BrO_Hg0_SIPEXIILB)

# 7) Between SI and BrO
r_rowD7_SIPEXIILB, p_valueD7_SIPEXIILB = stats.pearsonr(SI_SI_SIPEXIILB,BrO_SI_SIPEXIILB)
slopeD7_SIPEXIILB, interceptD7_SIPEXIILB, rD7_SIPEXIILB, pD7_SIPEXIILB, std_errD7_SIPEXIILB = stats.linregress(SI_SI_SIPEXIILB,BrO_SI_SIPEXIILB)

# 8) Between RH and BrO
r_rowD8_SIPEXIILB, p_valueD8_SIPEXIILB = stats.pearsonr(RH_SIPEXIILB,BrO_RH_SIPEXIILB)
slopeD8_SIPEXIILB, interceptD8_SIPEXIILB, rD8_SIPEXIILB, pD8_SIPEXIILB, std_errD8_SIPEXIILB = stats.linregress(RH_SIPEXIILB,BrO_RH_SIPEXIILB)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1LB, p_valueD1LB = stats.pearsonr(O3LB,BrO_O3LB)
slopeD1LB, interceptD1LB, rD1LB, pD1LB, std_errD1LB = stats.linregress(O3LB,BrO_O3LB)

# 2) Between Temp and BrO
r_rowD2LB, p_valueD2LB = stats.pearsonr(TempLB,BrOLB)
slopeD2LB, interceptD2LB, rD2LB, pD2LB, std_errD2LB = stats.linregress(TempLB,BrOLB)

# 3) Between Wind Direction and BrO
r_rowD3LB, p_valueD3LB = stats.pearsonr(WD_vectLB,BrO_WDLB)
slopeD3LB, interceptD3LB, rD3LB, pD3LB, std_errD3LB = stats.linregress(WD_vectLB,BrO_WDLB)

# 4) Between Wind Speed and BrO
r_rowD4LB, p_valueD4LB = stats.pearsonr(WSLB,BrO_WSLB)
slopeD4LB, interceptD4LB, rD4LB, pD4LB, std_errD4LB = stats.linregress(WSLB,BrO_WSLB)

# 5) Between Solar Radiation and BrO
r_rowD5LB, p_valueD5LB = stats.pearsonr(SolLB,BrOLB)
slopeD5LB, interceptD5LB, rD5LB, pD5LB, std_errD5LB = stats.linregress(SolLB,BrOLB)

# 6) Between Hg0 and BrO
r_rowD6LB, p_valueD6LB = stats.pearsonr(Hg0LB,BrO_Hg0LB)
slopeD6LB, interceptD6LB, rD6LB, pD6LB, std_errD6LB = stats.linregress(Hg0LB,BrO_Hg0LB)

# 7) Between SI and BrO
r_rowD7LB, p_valueD7LB = stats.pearsonr(SI_SILB,BrO_SILB)
slopeD7LB, interceptD7LB, rD7LB, pD7LB, std_errD7LB = stats.linregress(SI_SILB,BrO_SILB)

# 8) Between SI and BrO
r_rowD8LB, p_valueD8LB = stats.pearsonr(RHLB,BrO_RHLB)
slopeD8LB, interceptD8LB, rD8LB, pD8LB, std_errD8LB = stats.linregress(RHLB,BrO_RHLB)

#------------------------------------------------------------------------------
#-----------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#-----------------------------------

#--------------------------------
# SIPEXII (2012)
#--------------------------------
# 1) Between O3 and BrO
r_rowD1_SIPEXIIHB, p_valueD1_SIPEXIIHB = stats.pearsonr(O3_SIPEXIIHB,BrO_SIPEXIIHB)
slopeD1_SIPEXIIHB, interceptD1_SIPEXIIHB, rD1_SIPEXIIHB, pD1_SIPEXIIHB, std_errD1_SIPEXIIHB = stats.linregress(O3_SIPEXIIHB,BrO_SIPEXIIHB)

# 2) Between Temp and BrO
r_rowD2_SIPEXIIHB, p_valueD2_SIPEXIIHB = stats.pearsonr(Temp_SIPEXIIHB,BrO_SIPEXIIHB)
slopeD2_SIPEXIIHB, interceptD2_SIPEXIIHB, rD2_SIPEXIIHB, pD2_SIPEXIIHB, std_errD2_SIPEXIIHB = stats.linregress(Temp_SIPEXIIHB,BrO_SIPEXIIHB)

# 3) Between Wind Direction and BrO
r_rowD3_SIPEXIIHB, p_valueD3_SIPEXIIHB = stats.pearsonr(WD_vect_SIPEXIIHB,BrO_WD_SIPEXIIHB)
slopeD3_SIPEXIIHB, interceptD3_SIPEXIIHB, rD3_SIPEXIIHB, pD3_SIPEXIIHB, std_errD3_SIPEXIIHB = stats.linregress(WD_vect_SIPEXIIHB,BrO_WD_SIPEXIIHB)

# 4) Between Wind Speed and BrO
r_rowD4_SIPEXIIHB, p_valueD4_SIPEXIIHB = stats.pearsonr(WS_SIPEXIIHB,BrO_WS_SIPEXIIHB)
slopeD4_SIPEXIIHB, interceptD4_SIPEXIIHB, rD4_SIPEXIIHB, pD4_SIPEXIIHB, std_errD4_SIPEXIIHB = stats.linregress(WS_SIPEXIIHB,BrO_WS_SIPEXIIHB)

# 5) Between Solar Radiation and BrO
r_rowD5_SIPEXIIHB, p_valueD5_SIPEXIIHB = stats.pearsonr(Sol_SIPEXIIHB,BrO_SIPEXIIHB)
slopeD5_SIPEXIIHB, interceptD5_SIPEXIIHB, rD5_SIPEXIIHB, pD5_SIPEXIIHB, std_errD5_SIPEXIIHB = stats.linregress(Sol_SIPEXIIHB,BrO_SIPEXIIHB)

# 6) Between Hg0 and BrO
r_rowD6_SIPEXIIHB, p_valueD6_SIPEXIIHB = stats.pearsonr(Hg0_SIPEXIIHB,BrO_Hg0_SIPEXIIHB)
slopeD6_SIPEXIIHB, interceptD6_SIPEXIIHB, rD6_SIPEXIIHB, pD6_SIPEXIIHB, std_errD6_SIPEXIIHB = stats.linregress(Hg0_SIPEXIIHB,BrO_Hg0_SIPEXIIHB)

# 7) Between SI and BrO
r_rowD7_SIPEXIIHB, p_valueD7_SIPEXIIHB = stats.pearsonr(SI_SI_SIPEXIIHB,BrO_SI_SIPEXIIHB)
slopeD7_SIPEXIIHB, interceptD7_SIPEXIIHB, rD7_SIPEXIIHB, pD7_SIPEXIIHB, std_errD7_SIPEXIIHB = stats.linregress(SI_SI_SIPEXIIHB,BrO_SI_SIPEXIIHB)

# 8) Between RH and BrO
r_rowD8_SIPEXIIHB, p_valueD8_SIPEXIIHB = stats.pearsonr(RH_SIPEXIIHB,BrO_RH_SIPEXIIHB)
slopeD8_SIPEXIIHB, interceptD8_SIPEXIIHB, rD8_SIPEXIIHB, pD8_SIPEXIIHB, std_errD8_SIPEXIIHB = stats.linregress(RH_SIPEXIIHB,BrO_RH_SIPEXIIHB)

#--------------------------------
# COMBINED
#--------------------------------
# 1) Between O3 and BrO
r_rowD1HB, p_valueD1HB = stats.pearsonr(O3HB,BrO_O3HB)
slopeD1HB, interceptD1HB, rD1HB, pD1HB, std_errD1HB = stats.linregress(O3HB,BrO_O3HB)

# 2) Between Temp and BrO
r_rowD2HB, p_valueD2HB = stats.pearsonr(TempHB,BrOHB)
slopeD2HB, interceptD2HB, rD2HB, pD2HB, std_errD2HB = stats.linregress(TempHB,BrOHB)

# 3) Between Wind Direction and BrO
r_rowD3HB, p_valueD3HB = stats.pearsonr(WD_vectHB,BrO_WDHB)
slopeD3HB, interceptD3HB, rD3HB, pD3HB, std_errD3HB = stats.linregress(WD_vectHB,BrO_WDHB)

# 4) Between Wind Speed and BrO
r_rowD4HB, p_valueD4HB = stats.pearsonr(WSHB,BrO_WSHB)
slopeD4HB, interceptD4HB, rD4HB, pD4HB, std_errD4HB = stats.linregress(WSHB,BrO_WSHB)

# 5) Between Solar Radiation and BrO
r_rowD5HB, p_valueD5HB = stats.pearsonr(SolHB,BrOHB)
slopeD5HB, interceptD5HB, rD5HB, pD5HB, std_errD5HB = stats.linregress(SolHB,BrOHB)

# 6) Between Hg0 and BrO
r_rowD6HB, p_valueD6HB = stats.pearsonr(Hg0HB,BrO_Hg0HB)
slopeD6HB, interceptD6HB, rD6HB, pD6HB, std_errD6HB = stats.linregress(Hg0HB,BrO_Hg0HB)

# 7) Between SI and BrO
r_rowD7HB, p_valueD7HB = stats.pearsonr(SI_SIHB,BrO_SIHB)
slopeD7HB, interceptD7HB, rD7HB, pD7HB, std_errD7HB = stats.linregress(SI_SIHB,BrO_SIHB)

# 8) Between SI and BrO
r_rowD8HB, p_valueD8HB = stats.pearsonr(RHHB,BrO_RHHB)
slopeD8HB, interceptD8HB, rD8HB, pD8HB, std_errD8HB = stats.linregress(RHHB,BrO_RHHB)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs O3)

fig1 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 1
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_SIPEXIILS, BrO_SIPEXIILS,    edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(O3LS, interceptD1LS + slopeD1LS * O3LS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1LS))+" $\pm$"+str("%7.4f"%(std_errD1LS))+" pptv, r: "+str("%7.4f"%(rD1LS))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 1
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_SIPEXIILB, BrO_SIPEXIILB,    edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(O3LB, interceptD1LB + slopeD1LB * O3LB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1LB))+" $\pm$"+str("%7.4f"%(std_errD1LB))+" pptv, r: "+str("%7.4f"%(rD1LB))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 1
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_SIPEXIIHS, BrO_SIPEXIIHS,    edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(O3HS, interceptD1HS + slopeD1HS * O3HS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1HS))+" $\pm$"+str("%7.4f"%(std_errD1HS))+" pptv, r: "+str("%7.4f"%(rD1HS))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 1
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs O3
ax.scatter(O3_SIPEXIIHB, BrO_SIPEXIIHB,    edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(O3HB, interceptD1HB + slopeD1HB * O3HB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0.1, 34.5)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('O$_3$ (ppbv)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("O$_3$ and BrO:\n (slope: "+str("%7.4f"%(slopeD1HB))+" $\pm$"+str("%7.4f"%(std_errD1HB))+" pptv, r: "+str("%7.4f"%(rD1HB))+")", xy=(1.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Temperature)

fig2 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 2
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_SIPEXIILS, BrO_SIPEXIILS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(TempLS, interceptD2LS + slopeD2LS * TempLS, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2LS))+" $\pm$"+str("%7.4f"%(std_errD2LS))+" $^\circ$C, r: "+str("%7.4f"%(rD2LS))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 2
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_SIPEXIILB, BrO_SIPEXIILB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(TempLB, interceptD2LB + slopeD2LB * TempLB, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2LB))+" $\pm$"+str("%7.4f"%(std_errD2LB))+" $^\circ$C, r: "+str("%7.4f"%(rD2LB))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 2
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_SIPEXIIHS, BrO_SIPEXIIHS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(TempHS, interceptD2HS + slopeD2HS * TempHS, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2HS))+" $\pm$"+str("%7.4f"%(std_errD2HS))+" $^\circ$C, r: "+str("%7.4f"%(rD2HS))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 2
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Temperature
ax.scatter(Temp_SIPEXIIHB, BrO_SIPEXIIHB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(TempHB, interceptD2HB + slopeD2HB * TempHB, color='black') 

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-21.9, 5.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Temperature ($^\circ$C)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Temperature and BrO:\n (slope: "+str("%7.4f"%(slopeD2HB))+" $\pm$"+str("%7.4f"%(std_errD2HB))+" $^\circ$C, r: "+str("%7.4f"%(rD2HB))+")", xy=(-20.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Direction)

fig3 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 3
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_SIPEXIILS, BrO_SIPEXIILS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WD_vectLS, interceptD3LS + slopeD3LS * WD_vectLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3LS))+" $\pm$"+str("%7.4f"%(std_errD3LS))+" $^\circ$, r: "+str("%7.4f"%(rD3LS))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 3
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_SIPEXIILB, BrO_SIPEXIILB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WD_vectLB, interceptD3LB + slopeD3LB * WD_vectLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3LB))+" $\pm$"+str("%7.4f"%(std_errD3LB))+" $^\circ$, r: "+str("%7.4f"%(rD3LB))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 3
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_SIPEXIIHS, BrO_SIPEXIIHS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WD_vectHS, interceptD3HS + slopeD3HS * WD_vectHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3HS))+" $\pm$"+str("%7.4f"%(std_errD3HS))+" $^\circ$, r: "+str("%7.4f"%(rD3HS))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#-----------------------------------
# Graph 3
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Direction
ax.scatter(WD_vect_SIPEXIIHB, BrO_SIPEXIIHB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WD_vectHB, interceptD3HB + slopeD3HB * WD_vectHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_xlim(-1.0, 361)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind vector direction ($^\circ$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind vector direction and BrO:\n (slope: "+str("%7.4f"%(slopeD3HB))+" $\pm$"+str("%7.4f"%(std_errD3HB))+" $^\circ$, r: "+str("%7.4f"%(rD3HB))+")", xy=(10.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Wind Speed)

fig4 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 4
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_SIPEXIILS, BrO_SIPEXIILS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WSLS, interceptD4LS + slopeD4LS * WSLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4LS))+" $\pm$"+str("%7.4f"%(std_errD4LS))+" m/s, r: "+str("%7.4f"%(rD4LS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 4
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_SIPEXIILB, BrO_SIPEXIILB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WSLB, interceptD4LB + slopeD4LB * WSLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4LB))+" $\pm$"+str("%7.4f"%(std_errD4LB))+" m/s, r: "+str("%7.4f"%(rD4LB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 4
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_SIPEXIIHS, BrO_SIPEXIIHS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WSHS, interceptD4HS + slopeD4HS * WSHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4HS))+" $\pm$"+str("%7.4f"%(std_errD4HS))+" m/s, r: "+str("%7.4f"%(rD4HS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 4
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Wind Speed
ax.scatter(WS_SIPEXIIHB, BrO_SIPEXIIHB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(WSHB, interceptD4HB + slopeD4HB * WSHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(0, 21.9)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Wind Speed (m/s)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Wind speed and BrO:\n (slope: "+str("%7.4f"%(slopeD4HB))+" $\pm$"+str("%7.4f"%(std_errD4HB))+" m/s, r: "+str("%7.4f"%(rD4HB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Solar Radiation)

fig5 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 5
ax=plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_SIPEXIILS, BrO_SIPEXIILS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(SolLS, interceptD5LS + slopeD5LS * SolLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5LS))+" $\pm$"+str("%7.4f"%(std_errD5LS))+" W/m$^2$, r: "+str("%7.4f"%(rD5LS))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 5
ax=plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_SIPEXIILB, BrO_SIPEXIILB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(SolLB, interceptD5LB + slopeD5LB * SolLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5LB))+" $\pm$"+str("%7.4f"%(std_errD5LB))+" W/m$^2$, r: "+str("%7.4f"%(rD5LB))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 5
ax=plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_SIPEXIIHS, BrO_SIPEXIIHS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(SolHS, interceptD5HS + slopeD5HS * SolHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5HS))+" $\pm$"+str("%7.4f"%(std_errD5HS))+" W/m$^2$, r: "+str("%7.4f"%(rD5HS))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 5
ax=plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Solar Radiation
ax.scatter(Sol_SIPEXIIHB, BrO_SIPEXIIHB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(SolHB, interceptD5HB + slopeD5HB * SolHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.set_xlim(-1.0, 1401)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Solar radiation (W/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Solar radiation and BrO:\n (slope: "+str("%7.4f"%(slopeD5HB))+" $\pm$"+str("%7.4f"%(std_errD5HB))+" W/m$^2$, r: "+str("%7.4f"%(rD5HB))+")", xy=(15.0,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Hg0)

fig6 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 6
ax = plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_SIPEXIILS, BrO_Hg0_SIPEXIILS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(Hg0LS, interceptD6LS + slopeD6LS * Hg0LS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6LS))+" $\pm$ "+str("%7.4f"%(std_errD6LS))+" ng/m$^2$, r: "+str("%7.4f"%(rD6LS))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 6
ax = plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_SIPEXIILB, BrO_Hg0_SIPEXIILB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(Hg0LB, interceptD6LB + slopeD6LB * Hg0LB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6LB))+" $\pm$ "+str("%7.4f"%(std_errD6LB))+" ng/m$^2$, r: "+str("%7.4f"%(rD6LB))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 6
ax = plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_SIPEXIIHS, BrO_Hg0_SIPEXIIHS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(Hg0HS, interceptD6HS + slopeD6HS * Hg0HS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6HS))+" $\pm$ "+str("%7.4f"%(std_errD6HS))+" ng/m$^2$, r: "+str("%7.4f"%(rD6HS))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 6
ax = plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(Hg0_SIPEXIIHB, BrO_Hg0_SIPEXIIHB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line1, = plt.plot(Hg0HB, interceptD6HB + slopeD6HB * Hg0HB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.set_xlim(0, 1.45)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Hg$^0$ (ng/m$^2$)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Hg$^0$ and BrO:\n (slope: "+str("%7.4f"%(slopeD6HB))+" $\pm$ "+str("%7.4f"%(std_errD6HB))+" ng/m$^2$, r: "+str("%7.4f"%(rD6HB))+")", xy=(0.015,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Sea Ice)

fig7 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 7
ax = plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_SIPEXIILS, BrO_SIPEXIILS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SILS, interceptD7LS + slopeD7LS * SILS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7LS))+" $\pm$"+str("%7.4f"%(std_errD7LS))+" %, r: "+str("%7.4f"%(rD7LS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#------------------------------------
# Graph 7
ax = plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_SIPEXIILB, BrO_SIPEXIILB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SILB, interceptD7LB + slopeD7LB * SILB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7LB))+" $\pm$"+str("%7.4f"%(std_errD7LB))+" %, r: "+str("%7.4f"%(rD7LB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 7
ax = plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_SIPEXIIHS, BrO_SIPEXIIHS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SIHS, interceptD7HS + slopeD7HS * SIHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7HS))+" $\pm$"+str("%7.4f"%(std_errD7HS))+" %, r: "+str("%7.4f"%(rD7HS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 7
ax = plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs SeaIce
ax.scatter(SI_SIPEXIIHB, BrO_SIPEXIIHB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(SIHB, interceptD7HB + slopeD7HB * SIHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Sea Ice Concentration (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Sea Ice Concentration and BrO:\n (slope: "+str("%7.4f"%(slopeD7HB))+" $\pm$"+str("%7.4f"%(std_errD7HB))+" %, r: "+str("%7.4f"%(rD7HB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#------------------------------------------------------------------------------
# PLOT THE GRAPH (BrO vs Relative Humidity)

fig8 = plt.figure()
plt.subplots_adjust(hspace=0.5)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *SURFACE*
#-----------------------------------
# Graph 8
ax = plt.subplot(223) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_SIPEXIILS, BrO_RH_SIPEXIILS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(RHLS, interceptD8LS + slopeD8LS * RHLS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8LS))+" $\pm$"+str("%7.4f"%(std_errD8LS))+" %, r: "+str("%7.4f"%(rD8LS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# Low Wind Speed (<=7 m/s) *BOUNDARY*
#-----------------------------------
# Graph 8
ax = plt.subplot(221) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_SIPEXIILB, BrO_RH_SIPEXIILB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(RHLB, interceptD8LB + slopeD8LB * RHLB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] Low Wind Speed (<7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8LB))+" $\pm$"+str("%7.4f"%(std_errD8LB))+" %, r: "+str("%7.4f"%(rD8LB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)

#-----------------------------------
# High Wind Speed (>7 m/s) *SURFACE*
#-----------------------------------
# Graph 8
ax = plt.subplot(224) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_SIPEXIIHS, BrO_RH_SIPEXIIHS, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(RHHS, interceptD8HS + slopeD8HS * RHHS, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[0-100m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8HS))+" $\pm$"+str("%7.4f"%(std_errD8HS))+" %, r: "+str("%7.4f"%(rD8HS))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)


#------------------------------------
# High Wind Speed (>7 m/s) *BOUNDARY*
#------------------------------------
# Graph 8
ax = plt.subplot(222) # options graph 1 (vertical no, horizontal no, graph no)

# Plot BrO vs Relative Humidity
ax.scatter(RH_SIPEXIIHB, BrO_RH_SIPEXIIHB, edgecolors='none', marker='o', c='cyan',   label='SIPEXII (2012)')

# Plot the regression line
line6, = plt.plot(RHHB, interceptD8HB + slopeD8HB * RHHB, color='black')

# Format x-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_xlim(-1, 101.0)
ax.xaxis.labelpad = 10

# Format y-axis 1
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.set_ylim(0.1, 22.5)
ax.yaxis.labelpad = 10

# Plot the axis labels
ax.set_ylabel('BrO (pptv)', fontsize=20)
ax.set_xlabel('Relative Humidity (%)', fontsize=20)

# Plot the title
plt.title('[100-300m ASL] High Wind Speed (>7 m/s)', fontsize=25, pad=10)

## Plot the legend
#legend = ax.legend(bbox_to_anchor=(-0.42, 1), loc=2, borderaxespad=0., fontsize=13)
#legend.get_frame().set_facecolor('grey')
#legend.get_frame().set_alpha(0.9)

# Format axis labels
ax.tick_params(labelsize=15)

# Plot the label for the regression line
plt.annotate("Relative Humidity (%) and BrO:\n (slope: "+str("%7.4f"%(slopeD8HB))+" $\pm$"+str("%7.4f"%(std_errD8HB))+" %, r: "+str("%7.4f"%(rD8HB))+")", xy=(0.5,18.0), color='black', fontweight='bold', fontsize=15)
