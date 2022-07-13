#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Imports
#---------
import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from load4gascsv_v2 import load4gascsv_v2
import feather
import numpy as np
import os
import pandas as pd

# File locations
#----------------
the_folder = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/1oxaria/json/gap_filling/q12021/'


# In[10]:


# Loading climate data with laod4gascsv function
#------------------------------------------------
oxaria1_climate = load4gascsv_v2(folder=the_folder, topic='climate').sort_index()


# In[11]:


# Drop the rare occasions of dodgy indices & duplicated records
#---------------------------------------------------------------
oxaria1_climate = oxaria1_climate[~oxaria1_climate.index.duplicated(keep='last')]
oxaria1_climate.reset_index(inplace=True)
oxaria1_climate = oxaria1_climate.dropna(axis=0,subset=['tag','rec']).set_index(['tag','rec'])


# In[12]:


# Adding location names
# Let list of tags
# -----------------------
devices = oxaria1_climate.index.get_level_values(0).unique().sort_values()


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
oxaria1_climate = oxaria1_climate.merge(
    df_device_names, how='left', left_index=True, right_index=True)
oxaria1_climate.head()


# In[13]:


oxaria1_climate.info()


# In[14]:


# Saving to an ftr 
#------------------
oxaria1_climate.reset_index().to_feather(the_folder+'oxaria1_climate_q12021_gf.ftr')


# In[15]:


# Loading status data with laod4gascsv function
#------------------------------------------------
oxaria1_status = load4gascsv_v2(folder=the_folder, topic='status').sort_index()


# In[16]:


# Drop the rare occasions of dodgy indices & duplicated records
#---------------------------------------------------------------
oxaria1_status = oxaria1_status[~oxaria1_status.index.duplicated(keep='last')]
oxaria1_status.reset_index(inplace=True)
oxaria1_status = oxaria1_status.dropna(axis=0,subset=['tag','rec']).set_index(['tag','rec'])


# In[17]:


# Adding location names
# Let list of tags
# -----------------------
devices = oxaria1_status.index.get_level_values(0).unique().sort_values()


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
oxaria1_status = oxaria1_status.merge(
    df_device_names, how='left', left_index=True, right_index=True)
oxaria1_status.head()


# In[18]:


# Saving to an ftr
# ------------------
oxaria1_status['val.psu.rst'] = oxaria1_status['val.psu.rst'].astype(np.str)
oxaria1_status.reset_index().to_feather(
    the_folder+'oxaria1_status_q12021_gf.ftr')

