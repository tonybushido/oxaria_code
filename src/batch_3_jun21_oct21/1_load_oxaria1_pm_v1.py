#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
# ---------
import sys
sys.path.append('./oxaria/qoax')
import numpy as np
import pandas as pd
import os
import feather
from load4gascsv_v2 import load4gascsv_v2

# File locations
# ----------------
the_folder = './oxaria/raw/1oxaria/json/gap_filling/q12021/'


# In[2]:


# Loading PM data with laod4gascsv function
# ------------------------------------------------
oxaria1_pm = load4gascsv_v2(
    folder=the_folder, topic='particulate').sort_index()


# In[3]:


# Drop the rare occasions of dodgy indices & duplicated records
#---------------------------------------------------------------
oxaria1_pm = oxaria1_pm[~oxaria1_pm.index.duplicated(keep='last')]
oxaria1_pm.reset_index(inplace=True)
oxaria1_pm = oxaria1_pm.dropna(axis=0,subset=['tag','rec']).set_index(['tag','rec'])


# In[4]:


# Adding location names
# Let list of tags
# -----------------------
devices = oxaria1_pm.index.get_level_values(0).unique()


# Gen list of names for tags in same order as tag list
# ------------------------------------------------------
location_names = ['High St', 'South Parks Rd', 'St Ebbes', 'Jesus College',
                  'Marsten', 'The Plain', 'Worcester College', 'John Radcliffe']

# Zip together with the tags as a dictionary * convert to df
# ------------------------------------------------------------
device_names = dict(zip(devices, location_names))
df_device_names = pd.DataFrame.from_dict(
    device_names, orient='index', columns=['name'])
df_device_names.index.name = 'tag'

# Merge with gases_4gas
# -----------------------
oxaria1_pm = oxaria1_pm.merge(
    df_device_names, how='left', left_index=True, right_index=True)
oxaria1_pm.head()


# In[5]:


oxaria1_pm.info()


# In[6]:


# Saving to an ftr
# ------------------
oxaria1_pm.reset_index().to_feather(the_folder+'oxaria1_pm_q12021_gf.ftr')

