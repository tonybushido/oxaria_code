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
the_folder = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling/'
#/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling

# Loading gases data with load1gascsv function
#------------------------------------------------
print('Loading gzipped csvs...')
oxaria2_gases = load1gascsv_v2(folder=the_folder, topic='gases')#.sort_index()
oxaria2_gases = oxaria2_gases.query('tag != "scs-bgx-500"')

# Get list of tags to help with adding location names
#-----------------------------------------------------
devices = oxaria2_gases.index.get_level_values(0).unique()

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

# Merge with gases_1gas
#-----------------------
print('Adding location names...')
oxaria2_gases = oxaria2_gases.merge(df_device_names, how='left', left_index=True, right_index=True)

# Saving to an ftr
#------------------
print('Writing to ftr...')
oxaria2_gases.reset_index().to_feather(the_folder+'oxaria2_gases_gf.ftr')
print('\nAll done for gases.')
