#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Imports
#---------
import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from load1gascsv_v2 import load1gascsv_v2
import feather
import numpy as np
import os
import pandas as pd

# File locations
#----------------
the_folder = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling/q12021/'


# In[11]:


# Loading climate data with laod4gascsv function
# ------------------------------------------------
oxaria2_climate = load1gascsv_v2(
    folder=the_folder, topic='climate').sort_index()


# In[12]:


# Drop the rare occasions of dodgy indices & duplicated records
#---------------------------------------------------------------
oxaria2_climate = oxaria2_climate[~oxaria2_climate.index.duplicated(keep='last')]
oxaria2_climate.reset_index(inplace=True)
oxaria2_climate = oxaria2_climate.dropna(axis=0,
                               subset=['tag', 'rec']).set_index(['tag', 'rec'])


# In[13]:


# Adding location names
# Let list of tags 
#-----------------------
devices = oxaria2_climate.index.get_level_values(0).unique().sort_values()


# Gen list of names for tags in same order as tag list
#------------------------------------------------------
location_names = ['Windhmill School','Said Business School','County Hall','Divinity Road',                   'Jahlul Bayt Mosque','Windhmill School2','St Giles','Warneford Hospital',                  'Spare','Speedwell St']

# Zip together with the tags as a dictionary * convert to df
#------------------------------------------------------------
device_names = dict(zip(devices, location_names))
df_device_names = pd.DataFrame.from_dict(device_names, orient='index', columns=['name'])
df_device_names.index.name = 'tag'

# Merge with gases_4gas
#-----------------------
oxaria2_climate = oxaria2_climate.merge(df_device_names, how='left', left_index=True, right_index=True)
oxaria2_climate.head()


# In[14]:


# Saving to an ftr 
#------------------
oxaria2_climate.reset_index().to_feather(the_folder+'oxaria2_climate_q12021_gf.ftr')


# ## Status data
# Loading teh device status data with laod4gascsv function & checking out the look of the dataframe. There seems to be several columns with mixed data types & ebcause of this we cannot set the datat types we would like. Loading as-is (as objects) to retain this data as a record. Re-using may require slicing & cleaning.

# In[15]:


# Loading status data with laod4gascsv function
# -----------------------------------------------
oxaria2_status = load1gascsv_v2(folder=the_folder, topic='status').sort_index()


# In[16]:


# Drop the rare occasions of dodgy indices & duplicated records
#---------------------------------------------------------------
oxaria2_status = oxaria2_status[~oxaria2_status.index.duplicated(keep='last')]
oxaria2_status.reset_index(inplace=True)
oxaria2_status = oxaria2_status.dropna(axis=0,
                               subset=['tag', 'rec']).set_index(['tag', 'rec'])


# In[17]:


# Adding location names
# Let list of tags
# -----------------------
devices = oxaria2_status.index.get_level_values(0).unique().sort_values()


# Gen list of names for tags in same order as tag list
# ------------------------------------------------------
location_names = ['Windhmill School', 'Said Business School', 'County Hall', 'Divinity Road',
                  'Jahlul Bayt Mosque', 'Windhmill School2', 'St Giles', 'Warneford Hospital',
                  'Spare', 'Speedwell St']

# Zip together with the tags as a dictionary * convert to df
# ------------------------------------------------------------
device_names = dict(zip(devices, location_names))
df_device_names = pd.DataFrame.from_dict(
    device_names, orient='index', columns=['name'])
df_device_names.index.name = 'tag'

# Merge with gases_4gas
# -----------------------
oxaria2_status = oxaria2_status.merge(
    df_device_names, how='left', left_index=True, right_index=True)
oxaria2_status.info()


# In[18]:


# Fix some weirdness
#--------------------
oxaria2_status['val.psu.rst'] = oxaria2_status['val.psu.rst'].astype(np.str)


# In[19]:


# Saving to an ftr
# ------------------
oxaria2_status.reset_index().to_feather(
    the_folder+'oxaria2_status_q12021_gf.ftr')

