#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:51:06 2020

@author: ncp532
"""
# File system packages
#from netCDF4 import Dataset				    # function used to open single netcdf file
#from netCDF4 import MFDataset				# function used to open multiple netcdf files
#import xarray as xr

# Drawing packages
import matplotlib.pyplot as plt             
import matplotlib.dates as mdates            
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# Data handing packages
import numpy as np                           
import pandas as pd
from scipy import signal, stats
from statsmodels.formula.api import ols      # For statistics. Requires statsmodels 5.0 or more
from statsmodels.stats.anova import anova_lm # Analysis of Variance (ANOVA) on linear models
from statsmodels.stats.diagnostic import lilliefors
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.cross_decomposition import PLSRegression, PLSSVD
from sklearn.decomposition import PCA
from statsmodels.multivariate.pca import PCA as PCA2
from sklearn.preprocessing import scale
from sklearn import model_selection
from sklearn.metrics import mean_squared_error

# Date and Time handling package
from datetime import datetime,timedelta		# functions to handle date and time

#------------------------------------------------------------------------------
# DEFINE THE DATASETS

dfPCA = pd.read_csv('/Users/ncp532/Documents/Data/MERRA2/PCA_Variables3.csv', index_col=0)
dfPCA = dfPCA.dropna()

#------------------------------------------------------------------------------
# SET THE DATE

dfPCA.index = pd.to_datetime(dfPCA.index)
dfPCA.sort_index()

#------------------------------------------------------------------------------
# PERFORM A LOG TRANSFORMATION ON AEC & SQUARE-ROOT TRANSFORMATION ON BrO

dfPCA['log_AEC']       = np.log(dfPCA['AEC'])
dfPCA['sqrt_SurfBrO']  = np.sqrt(dfPCA['SurfBrO'])
dfPCA['sqrt_LTBrO']    = np.sqrt(dfPCA['LTBrO'])
dfPCA['sqrt_SurfBrO2'] = np.sqrt(dfPCA['SurfBrO2'])
dfPCA['sqrt_SurfBrO3'] = np.sqrt(dfPCA['SurfBrO3'])

#------------------------------------------------------------------------------
# CALCULATE THE STATISTICS

# Mean
dfPCA_Mean = dfPCA.mean()

# Median
dfPCA_Median = dfPCA.median()

# Min
dfPCA_Min = dfPCA.min()

# Max
dfPCA_Max = dfPCA.max()

# Std
dfPCA_Std = dfPCA.std()

# Mean - Std
dfPCA_MeanMStd = dfPCA_Mean - dfPCA_Std

# Mean + Std
dfPCA_MeanPStd = dfPCA_Mean + dfPCA_Std

#----------------------
# Standardised (Manual Method)
dfPCA_Standard  = (dfPCA - dfPCA_Mean) / dfPCA_Std

#----------------------
# Standardised (preprocessing.scale() function)
# NOTE: THIS METHOD GENERATES A USERWARNING 
dfPCA_Standard2 = preprocessing.scale(dfPCA)
dfPCA_Standard2 = pd.DataFrame(dfPCA_Standard2, index = dfPCA.index, columns = dfPCA.columns)

#----------------------
# Standardised (StandardScaler() function)
scale2 = StandardScaler()
dfPCA_Standard3 = scale2.fit_transform(dfPCA)
dfPCA_Standard3 = pd.DataFrame(dfPCA_Standard3, index = dfPCA.index, columns = dfPCA.columns)

#------------------------------------------------------------------------------
# SELECT STANDARD VARIABLES FOR THE PCA

# Swanson Variables
SwansonVariables    = dfPCA_Standard3.drop(['SurfBrO','LTBrO','sqrt_SurfBrO','sqrt_LTBrO','AEC','WindDir','SolRad','IceContact','IceContact100m',
                                            'IceContactMLH','SeaIceConc','IceContactPerc','LandContact','LandContactMLH','OceanContact','Weighted_Ice',
                                            'Weighted_Land','Weighted_Ocean','Percentage_Ice','Percentage_Land','Percentage_Ocean','Chlorophyll',
                                            'Water_Temp','Water_Sal','RelHum','InfraRed','Fluro','nd100m','SurfBrO2','SurfBrO3','sqrt_SurfBrO2','sqrt_SurfBrO3'], 1)

# All Additional Variables
#AdditionalVariables = dfPCA_Standard3.drop(['SurfBrO','LTBrO','sqrt_SurfBrO','sqrt_LTBrO','AEC'], 1)
AdditionalVariables = dfPCA_Standard3.drop(['SurfBrO','LTBrO','sqrt_SurfBrO','sqrt_LTBrO','AEC','IceContact100m','IceContactMLH','IceContactPerc',
                                            'LandContact','LandContactMLH','OceanContact','Weighted_Ice','Weighted_Land','Weighted_Ocean',
                                            'Percentage_Ice','Percentage_Land','Percentage_Ocean','PTDif1000m','Water_Temp','Water_Sal','RelHum',
                                            'InfraRed','Fluro','nd100m','SurfBrO2','SurfBrO3','sqrt_SurfBrO2','sqrt_SurfBrO3'], 1)

# BrO_Surf Varaiables
BrOSurfVariables    = dfPCA_Standard3

# BrO_LTcol Varaiables
BrOLTcolVariables   = dfPCA_Standard3

#------------------------------------------------------------------------------
# INDIVIDUAL VARIABLE REGRESSION

#--------------
# BrO Surf
#--------------
dataS      = BrOSurfVariables
dataS['z'] = dfPCA['sqrt_SurfBrO']

# Swanson variables
slope_O3_S,             intercept_O3_S,             r_O3_S,             p_O3_S,             std_err_O3_S             = stats.linregress(dataS['z'], dataS['O3'])
slope_AEC_S,            intercept_AEC_S,            r_AEC_S,            p_AEC_S,            std_err_AEC_S            = stats.linregress(dataS['z'], dataS['log_AEC'])
slope_SurfTemp_S,       intercept_SurfTemp_S,       r_SurfTemp_S,       p_SurfTemp_S,       std_err_SurfTemp_S       = stats.linregress(dataS['z'], dataS['SurfTemp'])
slope_SLP_S,            intercept_SLP_S,            r_SLP_S,            p_SLP_S,            std_err_SLP_S            = stats.linregress(dataS['z'], dataS['SurfPres'])
slope_WS10m_S,          intercept_WS10m_S,          r_WS10m_S,          p_WS10m_S,          std_err_WS10m_S          = stats.linregress(dataS['z'], dataS['WS10m'])
slope_MLH_S,            intercept_MLH_S,            r_MLH_S,            p_MLH_S,            std_err_MLH_S            = stats.linregress(dataS['z'], dataS['MLH'])
slope_P1hr_S,           intercept_P1hr_S,           r_P1hr_S,           p_P1hr_S,           std_err_P1hr_S           = stats.linregress(dataS['z'], dataS['P1hr'])
slope_PTD1000m_S,       intercept_PTD1000m_S,       r_PTD1000m_S,       p_PTD1000m_S,       std_err_PTD1000m_S       = stats.linregress(dataS['z'], dataS['PTDif1000m'])
slope_PTD100m_S,        intercept_PTD100m_S,        r_PTD100m_S,        p_PTD100m_S,        std_err_PTD100m_S        = stats.linregress(dataS['z'], dataS['PTDif100m'])

# Additional variables
slope_WindDir_S,        intercept_WindDir_S,        r_WindDir_S,        p_WindDir_S,        std_err_WindDir_S        = stats.linregress(dataS['z'], dataS['WindDir'])
slope_SolRad_S,         intercept_SolRad_S,         r_SolRad_S,         p_SolRad_S,         std_err_SolRad_S         = stats.linregress(dataS['z'], dataS['SolRad'])
slope_IceContact_S,     intercept_IceContact_S,     r_IceContact_S,     p_IceContact_S,     std_err_IceContact_S     = stats.linregress(dataS['z'], dataS['IceContact'])
slope_IceContact100m_S, intercept_IceContact100m_S, r_IceContact100m_S, p_IceContact100m_S, std_err_IceContact100m_S = stats.linregress(dataS['z'], dataS['IceContact100m'])
slope_IceContactMLH_S,  intercept_IceContactMLH_S,  r_IceContactMLH_S,  p_IceContactMLH_S,  std_err_IceContactMLH_S  = stats.linregress(dataS['z'], dataS['IceContactMLH'])
slope_SeaIceConc_S,     intercept_SeaIceConc_S,     r_SeaIceConc_S,     p_SeaIceConc_S,     std_err_SeaIceConc_S     = stats.linregress(dataS['z'], dataS['SeaIceConc'])
slope_IceContactPerc_S, intercept_IceContactPerc_S, r_IceContactPerc_S, p_IceContactPerc_S, std_err_IceContactPerc_S = stats.linregress(dataS['z'], dataS['IceContactPerc'])
slope_LandContact_S,    intercept_LandContact_S,    r_LandContact_S,    p_LandContact_S,    std_err_LandContact_S    = stats.linregress(dataS['z'], dataS['LandContact'])
slope_LandContactMLH_S, intercept_LandContactMLH_S, r_LandContactMLH_S, p_LandContactMLH_S, std_err_LandContactMLH_S = stats.linregress(dataS['z'], dataS['LandContactMLH'])
slope_OceanContact_S,   intercept_OceanContact_S,   r_OceanContact_S,   p_OceanContact_S,   std_err_OceanContact_S   = stats.linregress(dataS['z'], dataS['OceanContact'])
slope_WeightedIce_S,    intercept_WeightedIce_S,    r_WeightedIce_S,    p_WeightedIce_S,    std_err_WeightedIce_S    = stats.linregress(dataS['z'], dataS['Weighted_Ice'])
slope_WeightedLand_S,   intercept_WeightedLand_S,   r_WeightedLand_S,   p_WeightedLand_S,   std_err_WeightedLand_S   = stats.linregress(dataS['z'], dataS['Weighted_Land'])
slope_WeightedOcean_S,  intercept_WeightedOcean_S,  r_WeightedOcean_S,  p_WeightedOcean_S,  std_err_WeightedOcean_S  = stats.linregress(dataS['z'], dataS['Weighted_Ocean'])
slope_PercentageIce_S,  intercept_PercentageIce_S,  r_PercentageIce_S,  p_PercentageIce_S,  std_err_PercentageIce_S  = stats.linregress(dataS['z'], dataS['Percentage_Ice'])
slope_PercentageLand_S, intercept_PercentageLand_S, r_PercentageLand_S, p_PercentageLand_S, std_err_PercentageLand_S = stats.linregress(dataS['z'], dataS['Percentage_Land'])
slope_PercentageOcean_S,intercept_PercentageOcean_S,r_PercentageOcean_S,p_PercentageOcean_S,std_err_PercentageOcean_S= stats.linregress(dataS['z'], dataS['Percentage_Ocean'])
slope_Chloro_S,         intercept_Chloro_S,         r_Chloro_S,         p_Chloro_S,         std_err_Chloro_S         = stats.linregress(dataS['z'], dataS['Chlorophyll'])
slope_WaterTemp_S,      intercept_WaterTemp_S,      r_WaterTemp_S,      p_WaterTemp_S,      std_err_WaterTemp_S      = stats.linregress(dataS['z'], dataS['Water_Temp'])
slope_WaterSal_S,       intercept_WaterSal_S,       r_WaterSal_S,       p_WaterSal_S,       std_err_WaterSal_S       = stats.linregress(dataS['z'], dataS['Water_Sal'])
slope_RelHum_S,         intercept_RelHum_S,         r_RelHum_S,         p_RelHum_S,         std_err_RelHum_S         = stats.linregress(dataS['z'], dataS['RelHum'])
slope_InfraRed_S,       intercept_InfraRed_S,       r_InfraRed_S,       p_InfraRed_S,       std_err_InfraRed_S       = stats.linregress(dataS['z'], dataS['InfraRed'])
slope_Fluro_S,          intercept_Fluro_S,          r_Fluro_S,          p_Fluro_S,          std_err_Fluro_S          = stats.linregress(dataS['z'], dataS['Fluro'])

# R-squared
r2_O3_S             = r_O3_S**2
r2_AEC_S            = r_AEC_S**2
r2_SurfTemp_S       = r_SurfTemp_S**2
r2_SLP_S            = r_SLP_S**2
r2_WS10m_S          = r_WS10m_S**2
r2_MLH_S            = r_MLH_S**2
r2_P1hr_S           = r_P1hr_S**2
r2_PTD1000m_S       = r_PTD1000m_S**2
r2_PTD100m_S        = r_PTD100m_S**2

# Additional variables
r2_WindDir_S        = r_WindDir_S**2
r2_SolRad_S         = r_SolRad_S**2
r2_IceContact_S     = r_IceContact_S**2
r2_IceContact100m_S = r_IceContact100m_S**2
r2_IceContactMLH_S  = r_IceContactMLH_S**2
r2_SeaIceConc_S     = r_SeaIceConc_S**2
r2_IceContactPerc_S = r_IceContactPerc_S**2
r2_LandContact_S    = r_LandContact_S**2
r2_LandContactMLH_S = r_LandContactMLH_S**2
r2_OceanContact_S   = r_OceanContact_S**2
r2_WeightedIce_S    = r_WeightedIce_S**2
r2_WeightedLand_S   = r_WeightedLand_S**2
r2_WeightedOcean_S  = r_WeightedOcean_S**2
r2_PercentageIce_S  = r_PercentageIce_S**2
r2_PercentageLand_S = r_PercentageLand_S**2
r2_PercentageOcean_S= r_PercentageOcean_S**2
r2_Chloro_S         = r_Chloro_S**2
r2_WaterTemp_S      = r_WaterTemp_S**2
r2_WaterSal_S       = r_WaterSal_S**2
r2_RelHum_S         = r_RelHum_S**2
r2_InfraRed_S       = r_InfraRed_S**2
r2_Fluro_S          = r_Fluro_S**2

#--------------
# BrO LTcol
#--------------
dataLT      = BrOLTcolVariables
dataLT['z'] = dfPCA['sqrt_LTBrO']

# Swanson variables
slope_O3_LT,             intercept_O3_LT,             r_O3_LT,             p_O3_LT,             std_err_O3_LT             = stats.linregress(dataLT['z'], dataLT['O3'])
slope_AEC_LT,            intercept_AEC_LT,            r_AEC_LT,            p_AEC_LT,            std_err_AEC_LT            = stats.linregress(dataLT['z'], dataLT['log_AEC'])
slope_SurfTemp_LT,       intercept_SurfTemp_LT,       r_SurfTemp_LT,       p_SurfTemp_LT,       std_err_SurfTemp_LT       = stats.linregress(dataLT['z'], dataLT['SurfTemp'])
slope_SLP_LT,            intercept_SLP_LT,            r_SLP_LT,            p_SLP_LT,            std_err_SLP_LT            = stats.linregress(dataLT['z'], dataLT['SurfPres'])
slope_WS10m_LT,          intercept_WS10m_LT,          r_WS10m_LT,          p_WS10m_LT,          std_err_WS10m_LT          = stats.linregress(dataLT['z'], dataLT['WS10m'])
slope_MLH_LT,            intercept_MLH_LT,            r_MLH_LT,            p_MLH_LT,            std_err_MLH_LT            = stats.linregress(dataLT['z'], dataLT['MLH'])
slope_P1hr_LT,           intercept_P1hr_LT,           r_P1hr_LT,           p_P1hr_LT,           std_err_P1hr_LT           = stats.linregress(dataLT['z'], dataLT['P1hr'])
slope_PTD1000m_LT,       intercept_PTD1000m_LT,       r_PTD1000m_LT,       p_PTD1000m_LT,       std_err_PTD1000m_LT       = stats.linregress(dataLT['z'], dataLT['PTDif1000m'])
slope_PTD100m_LT,        intercept_PTD100m_LT,        r_PTD100m_LT,        p_PTD100m_LT,        std_err_PTD100m_LT        = stats.linregress(dataLT['z'], dataLT['PTDif100m'])

# Additional variables
slope_WindDir_LT,        intercept_WindDir_LT,        r_WindDir_LT,        p_WindDir_LT,        std_err_WindDir_LT        = stats.linregress(dataLT['z'], dataLT['WindDir'])
slope_SolRad_LT,         intercept_SolRad_LT,         r_SolRad_LT,         p_SolRad_LT,         std_err_SolRad_LT         = stats.linregress(dataLT['z'], dataLT['SolRad'])
slope_IceContact_LT,     intercept_IceContact_LT,     r_IceContact_LT,     p_IceContact_LT,     std_err_IceContact_LT     = stats.linregress(dataLT['z'], dataLT['IceContact'])
slope_IceContact100m_LT, intercept_IceContact100m_LT, r_IceContact100m_LT, p_IceContact100m_LT, std_err_IceContact100m_LT = stats.linregress(dataLT['z'], dataLT['IceContact100m'])
slope_IceContactMLH_LT,  intercept_IceContactMLH_LT,  r_IceContactMLH_LT,  p_IceContactMLH_LT,  std_err_IceContactMLH_LT  = stats.linregress(dataLT['z'], dataLT['IceContactMLH'])
slope_SeaIceConc_LT,     intercept_SeaIceConc_LT,     r_SeaIceConc_LT,     p_SeaIceConc_LT,     std_err_SeaIceConc_LT     = stats.linregress(dataLT['z'], dataLT['SeaIceConc'])
slope_IceContactPerc_LT, intercept_IceContactPerc_LT, r_IceContactPerc_LT, p_IceContactPerc_LT, std_err_IceContactPerc_LT = stats.linregress(dataLT['z'], dataLT['IceContactPerc'])
slope_LandContact_LT,    intercept_LandContact_LT,    r_LandContact_LT,    p_LandContact_LT,    std_err_LandContact_LT    = stats.linregress(dataLT['z'], dataLT['LandContact'])
slope_LandContactMLH_LT, intercept_LandContactMLH_LT, r_LandContactMLH_LT, p_LandContactMLH_LT, std_err_LandContactMLH_LT = stats.linregress(dataLT['z'], dataLT['LandContactMLH'])
slope_OceanContact_LT,   intercept_OceanContact_LT,   r_OceanContact_LT,   p_OceanContact_LT,   std_err_OceanContact_LT   = stats.linregress(dataLT['z'], dataLT['OceanContact'])
slope_WeightedIce_LT,    intercept_WeightedIce_LT,    r_WeightedIce_LT,    p_WeightedIce_LT,    std_err_WeightedIce_LT    = stats.linregress(dataLT['z'], dataLT['Weighted_Ice'])
slope_WeightedLand_LT,   intercept_WeightedLand_LT,   r_WeightedLand_LT,   p_WeightedLand_LT,   std_err_WeightedLand_LT   = stats.linregress(dataLT['z'], dataLT['Weighted_Land'])
slope_WeightedOcean_LT,  intercept_WeightedOcean_LT,  r_WeightedOcean_LT,  p_WeightedOcean_LT,  std_err_WeightedOcean_LT  = stats.linregress(dataLT['z'], dataLT['Weighted_Ocean'])
slope_PercentageIce_LT,  intercept_PercentageIce_LT,  r_PercentageIce_LT,  p_PercentageIce_LT,  std_err_PercentageIce_LT  = stats.linregress(dataLT['z'], dataLT['Percentage_Ice'])
slope_PercentageLand_LT, intercept_PercentageLand_LT, r_PercentageLand_LT, p_PercentageLand_LT, std_err_PercentageLand_LT = stats.linregress(dataLT['z'], dataLT['Percentage_Land'])
slope_PercentageOcean_LT,intercept_PercentageOcean_LT,r_PercentageOcean_LT,p_PercentageOcean_LT,std_err_PercentageOcean_LT= stats.linregress(dataLT['z'], dataLT['Percentage_Ocean'])
slope_Chloro_LT,         intercept_Chloro_LT,         r_Chloro_LT,         p_Chloro_LT,         std_err_Chloro_LT         = stats.linregress(dataLT['z'], dataLT['Chlorophyll'])
slope_WaterTemp_LT,      intercept_WaterTemp_LT,      r_WaterTemp_LT,      p_WaterTemp_LT,      std_err_WaterTemp_LT      = stats.linregress(dataLT['z'], dataLT['Water_Temp'])
slope_WaterSal_LT,       intercept_WaterSal_LT,       r_WaterSal_LT,       p_WaterSal_LT,       std_err_WaterSal_LT       = stats.linregress(dataLT['z'], dataLT['Water_Sal'])
slope_RelHum_LT,         intercept_RelHum_LT,         r_RelHum_LT,         p_RelHum_LT,         std_err_RelHum_LT         = stats.linregress(dataLT['z'], dataLT['RelHum'])
slope_InfraRed_LT,       intercept_InfraRed_LT,       r_InfraRed_LT,       p_InfraRed_LT,       std_err_InfraRed_LT       = stats.linregress(dataLT['z'], dataLT['InfraRed'])
slope_Fluro_LT,          intercept_Fluro_LT,          r_Fluro_LT,          p_Fluro_LT,          std_err_Fluro_LT          = stats.linregress(dataLT['z'], dataLT['Fluro'])

# R-squared
r2_O3_LT             = r_O3_LT**2
r2_AEC_LT            = r_AEC_LT**2
r2_SurfTemp_LT       = r_SurfTemp_LT**2
r2_SLP_LT            = r_SLP_LT**2
r2_WS10m_LT          = r_WS10m_LT**2
r2_MLH_LT            = r_MLH_LT**2
r2_P1hr_LT           = r_P1hr_LT**2
r2_PTD1000m_LT       = r_PTD1000m_LT**2
r2_PTD100m_LT        = r_PTD100m_LT**2

# Additional variables
r2_WindDir_LT        = r_WindDir_LT**2
r2_SolRad_LT         = r_SolRad_LT**2
r2_IceContact_LT     = r_IceContact_LT**2
r2_IceContact100m_LT = r_IceContact100m_LT**2
r2_IceContactMLH_LT  = r_IceContactMLH_LT**2
r2_SeaIceConc_LT     = r_SeaIceConc_LT**2
r2_IceContactPerc_LT = r_IceContactPerc_LT**2
r2_LandContact_LT    = r_LandContact_LT**2
r2_LandContactMLH_LT = r_LandContactMLH_LT**2
r2_OceanContact_LT   = r_OceanContact_LT**2
r2_WeightedIce_LT    = r_WeightedIce_LT**2
r2_WeightedLand_LT   = r_WeightedLand_LT**2
r2_WeightedOcean_LT  = r_WeightedOcean_LT**2
r2_PercentageIce_LT  = r_PercentageIce_LT**2
r2_PercentageLand_LT = r_PercentageLand_LT**2
r2_PercentageOcean_LT= r_PercentageOcean_LT**2
r2_Chloro_LT         = r_Chloro_LT**2
r2_WaterTemp_LT      = r_WaterTemp_LT**2
r2_WaterSal_LT       = r_WaterSal_LT**2
r2_RelHum_LT         = r_RelHum_LT**2
r2_InfraRed_LT       = r_InfraRed_LT**2
r2_Fluro_LT          = r_Fluro_LT**2

#--------------
# Additional variables
#--------------
dfLinearRegression = pd.DataFrame({'R (BrO_Surf)':         [r_O3_S,   r_AEC_S,   r_SurfTemp_S,   r_SLP_S,   r_WS10m_S,   r_MLH_S,   r_P1hr_S,   r_PTD1000m_S,   r_PTD100m_S,   r_WindDir_S,   r_SolRad_S,   r_IceContact_S,   r_IceContact100m_S,   r_IceContactMLH_S,   r_SeaIceConc_S,   r_IceContactPerc_S,   r_LandContact_S,   r_LandContactMLH_S,   r_OceanContact_S,   r_WeightedIce_S,   r_WeightedLand_S,   r_WeightedOcean_S,   r_PercentageIce_S,   r_PercentageLand_S,   r_PercentageOcean_S,   r_Chloro_S,   r_WaterTemp_S,   r_WaterSal_S,   r_RelHum_S,   r_InfraRed_S,   r_Fluro_S],
                                    'R^2 (BrO_Surf)':      [r2_O3_S,  r2_AEC_S,  r2_SurfTemp_S,  r2_SLP_S,  r2_WS10m_S,  r2_MLH_S,  r2_P1hr_S,  r2_PTD1000m_S,  r2_PTD100m_S,  r2_WindDir_S,  r2_SolRad_S,  r2_IceContact_S,  r2_IceContact100m_S,  r2_IceContactMLH_S,  r2_SeaIceConc_S,  r2_IceContactPerc_S,  r2_LandContact_S,  r2_LandContactMLH_S,  r2_OceanContact_S,  r2_WeightedIce_S,  r2_WeightedLand_S,  r2_WeightedOcean_S,  r2_PercentageIce_S,  r2_PercentageLand_S,  r2_PercentageOcean_S,  r2_Chloro_S,  r2_WaterTemp_S,  r2_WaterSal_S,  r2_RelHum_S,  r2_InfraRed_S,  r2_Fluro_S],
                                    'p-value (BrO_Surf)':  [p_O3_S,   p_AEC_S,   p_SurfTemp_S,   p_SLP_S,   p_WS10m_S,   p_MLH_S,   p_P1hr_S,   p_PTD1000m_S,   p_PTD100m_S,   p_WindDir_S,   p_SolRad_S,   p_IceContact_S,   p_IceContact100m_S,   p_IceContactMLH_S,   p_SeaIceConc_S,   p_IceContactPerc_S,   p_LandContact_S,   p_LandContactMLH_S,   p_OceanContact_S,   p_WeightedIce_S,   p_WeightedLand_S,   p_WeightedOcean_S,   p_PercentageIce_S,   p_PercentageLand_S,   p_PercentageOcean_S,   p_Chloro_S,   p_WaterTemp_S,   p_WaterSal_S,   p_RelHum_S,   p_InfraRed_S,   p_Fluro_S],
                                    'R (BrO_LTcol)':       [r_O3_LT,  r_AEC_LT,  r_SurfTemp_LT,  r_SLP_LT,  r_WS10m_LT,  r_MLH_LT,  r_P1hr_LT,  r_PTD1000m_LT,  r_PTD100m_LT,  r_WindDir_LT,  r_SolRad_LT,  r_IceContact_LT,  r_IceContact100m_LT,  r_IceContactMLH_LT,  r_SeaIceConc_LT,  r_IceContactPerc_LT,  r_LandContact_LT,  r_LandContactMLH_LT,  r_OceanContact_LT,  r_WeightedIce_LT,  r_WeightedLand_LT,  r_WeightedOcean_LT,  r_PercentageIce_LT,  r_PercentageLand_LT,  r_PercentageOcean_LT,  r_Chloro_LT,  r_WaterTemp_LT,  r_WaterSal_LT,  r_RelHum_LT,  r_InfraRed_LT,  r_Fluro_LT],
                                    'R^2 (BrO_LTcol)':     [r2_O3_LT, r2_AEC_LT, r2_SurfTemp_LT, r2_SLP_LT, r2_WS10m_LT, r2_MLH_LT, r2_P1hr_LT, r2_PTD1000m_LT, r2_PTD100m_LT, r2_WindDir_LT, r2_SolRad_LT, r2_IceContact_LT, r2_IceContact100m_LT, r2_IceContactMLH_LT, r2_SeaIceConc_LT, r2_IceContactPerc_LT, r2_LandContact_LT, r2_LandContactMLH_LT, r2_OceanContact_LT, r2_WeightedIce_LT, r2_WeightedLand_LT, r2_WeightedOcean_LT, r2_PercentageIce_LT, r2_PercentageLand_LT, r2_PercentageOcean_LT, r2_Chloro_LT, r2_WaterTemp_LT, r2_WaterSal_LT, r2_RelHum_LT, r2_InfraRed_LT, r2_Fluro_LT],
                                    'p-value (BrO_LTcol)': [p_O3_LT,  p_AEC_LT,  p_SurfTemp_LT,  p_SLP_LT,  p_WS10m_LT,  p_MLH_LT,  p_P1hr_LT,  p_PTD1000m_LT,  p_PTD100m_LT,  p_WindDir_LT,  p_SolRad_LT,  p_IceContact_LT,  p_IceContact100m_LT,  p_IceContactMLH_LT,  p_SeaIceConc_LT,  p_IceContactPerc_LT,  p_LandContact_LT,  p_LandContactMLH_LT,  p_OceanContact_LT,  p_WeightedIce_LT,  p_WeightedLand_LT,  p_WeightedOcean_LT,  p_PercentageIce_LT,  p_PercentageLand_LT,  p_PercentageOcean_LT,  p_Chloro_LT,  p_WaterTemp_LT,  p_WaterSal_LT,  p_RelHum_LT,  p_InfraRed_LT,  p_Fluro_LT]})
dfLinearRegression.index = ['O3','AEC','SurfTemp','SLP','WS10m','MLH','P1hr','PTD1000m','PTD100m','WindDir','SolRad','IceContact','IceContact100m','IceContactMLH','SeaIceConc','IceContactPerc','LandContact','LandContactMLH','OceanContact','WeightedIce','WeightedLand','WeightedOcean','PercentageIce','PercentageLand','PercentageOcean','Chlorophyll','WaterTemp','WaterSal','RelHum','InfraRed','Fluro']
dfLinearRegression.to_csv('/Users/ncp532/Documents/Data/MERRA2/BrO_LinearRegression.csv')
