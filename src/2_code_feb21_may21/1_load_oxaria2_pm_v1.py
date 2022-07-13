#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
#---------
import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from load1gascsv_v2 import load1gascsv_v2
import pandas as pd
import feather
import os

# File locations
#----------------
the_folder = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling/q12021/'


# In[2]:


# Loading gases data with load4gascsv function
#------------------------------------------------
oxaria2_pm = load1gascsv_v2(folder=the_folder,
                            topic='particulate').sort_index()


# In[3]:


# Drop the rare occasions of dodgy indices & duplicated records
#---------------------------------------------------------------
oxaria2_pm = oxaria2_pm[~oxaria2_pm.index.duplicated(keep='last')]
oxaria2_pm.reset_index(inplace=True)
oxaria2_pm = oxaria2_pm.dropna(axis=0,
                               subset=['tag', 'rec']).set_index(['tag', 'rec'])


# In[4]:


# Let list of tags
#------------------
devices = oxaria2_pm.index.get_level_values(0).unique()
devices

# Gen list of names for tags in same order as tag list
#------------------------------------------------------
location_names = ['Windhmill School','Said Business School','County Hall','Divinity Road',                   'Jahlul Bayt Mosque','Windhmill School2','St Giles','Warneford Hospital',                   'Spare','Speedwell St']

# Zip together with the tags as a dictionary * convert to df
#------------------------------------------------------------
device_names = dict(zip(devices, location_names))
df_device_names = pd.DataFrame.from_dict(device_names,
                                         orient='index',
                                         columns=['name'])
df_device_names.index.name = 'tag'

# Merge with gases_4gas
#-----------------------
oxaria2_pm = oxaria2_pm.merge(df_device_names,
                              how='left',
                              left_index=True,
                              right_index=True)
oxaria2_pm.head()


# In[5]:


# Saving to an ftr
#------------------
oxaria2_pm.reset_index().to_feather(the_folder + 'oxaria2_pm_q12021_gf.ftr')

