# Imports
#---------

import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from write_json2csv import write_json2csv
import os

os.chdir('/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling/jun_to_sept_2021/')
folder = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/2oxaria/json/gap_filling/jun_to_sept_2021/'

# Pull oxaria2 climate
#------------------
write_json2csv(folder=folder,topic_type='climate')

# Pull oxaria2 status
#------------------
write_json2csv(folder=folder,topic_type='status')

# Pull oxaria2 gases
#------------------
write_json2csv(folder=folder,topic_type='gases')

# Pull oxaria2 pm
#------------------
write_json2csv(folder=folder,topic_type='pm')


