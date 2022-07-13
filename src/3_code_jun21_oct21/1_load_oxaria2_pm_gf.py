#!/usr/bin/env python
# coding: utf-8

# Loading OxAria1 4-gas sensor data to feather files
#----------------------------------------------------
# UoB owner sensors only

# Inputs
#--------
# Sensor data in CSV format extracted from the SCS datastore using their
# aws_topic_history.py & csv_writer.py scripts.

# Outputs
#---------
# Top copies of the CSVs found at
# `/Home/OxAria Study (Suzanne Bartington)/praxis_data/raw/2oxaria/`
# Copies of these taken locally for processing.

# Imports
#---------
import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from load1gascsv_v2 import load1gascsv_v2
import pandas as pd
import feather
import numpy as np
import os

# File locations
#----------------
the_folder = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling/jun_to_sept_2021/'
#/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling/jun_to_sept_2021

# Loading pm data with load4gascsv function
#------------------------------------------------
print('Loading gzipped csvs...')
oxaria2_pm = load1gascsv_v2(folder=the_folder, topic='particulate').sort_index()
oxaria2_pm = oxaria2_pm.query('tag != "scs-bgx-500"')

# Get list of tags to help with adding location names
#-----------------------------------------------------
devices = oxaria2_pm.index.get_level_values(0).unique()

# Gen list of names for tags in same order as tag list
#------------------------------------------------------
location_names = ['Windmill School','Said Business School','County Hall','Divinity Road', \
                  'Jahlul Bayt Mosque','St Peters','St Giles','Warneford Hospital', \
                  'Spare','Speedwell St']

# Zip together with the tags as a dictionary * convert to df
#------------------------------------------------------------
device_names = dict(zip(devices, location_names))
df_device_names = pd.DataFrame.from_dict(device_names, orient='index', columns=['name'])
df_device_names.index.name = 'tag'

# Merge with pm_4gas
#-----------------------
print('Adding location names...')
oxaria2_pm = oxaria2_pm.merge(df_device_names, how='left', left_index=True, right_index=True)

# Saving to an ftr
#------------------
print('Writing to ftr...')
oxaria2_pm.reset_index().to_feather(the_folder+'oxaria2_pm_gf_oct.ftr')
print('\nAll done for pm.')
