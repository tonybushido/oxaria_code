#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
# ---------
import sys
sys.path.append('./oxaria/qoax/')
import os
import numpy as np
import feather
import pandas as pd
from load4gascsv_v2 import load4gascsv_v2

# File locations
# ----------------
the_folder = './oxaria/data/raw/1oxaria/json/gap_filling/batch_2_feb21_may21/'


# In[2]:


# Loading gases data with load4gascsv function
# ------------------------------------------------
oxaria1_gases = load4gascsv_v2(folder=the_folder, topic='gases').sort_index()


# In[3]:


# Drop the rare occasions of dodgy indices & duplicated records
#---------------------------------------------------------------
oxaria1_gases = oxaria1_gases[~oxaria1_gases.index.duplicated(keep='last')]
oxaria1_gases.reset_index(inplace=True)
oxaria1_gases = oxaria1_gases.dropna(axis=0,subset=['tag','rec']).set_index(['tag','rec'])


# In[4]:


# Let list of tags
# ------------------
devices = oxaria1_gases.index.get_level_values(0).unique()

# Gen list of names for tags in same order as tag list
# ------------------------------------------------------
location_names = ['High St', 'South Parks Rd', 'St Ebbes', 'Jesus College',
                  'New Marston', 'The Plain', 'Worcester College', 'John Radcliffe']

# Zip together with the tags as a dictionary * convert to df
# ------------------------------------------------------------
device_names = dict(zip(devices, location_names))
df_device_names = pd.DataFrame.from_dict(
    device_names, orient='index', columns=['name'])
df_device_names.index.name = 'tag'

# Merge with gases_4gas
# -----------------------
oxaria1_gases = oxaria1_gases.merge(
    df_device_names, how='left', left_index=True, right_index=True)
oxaria1_gases.head()


# In[5]:


oxaria1_gases.info()


# In[6]:


# Saving to an ftr
# ------------------
oxaria1_gases.reset_index().to_feather(the_folder+'oxaria1_gases_q12021_gf.ftr')

