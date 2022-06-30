# Imports
#---------

import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from write_json2csv import write_json2csv
import os

os.chdir('/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/1oxaria/json/gap_filling/')
folder = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/1oxaria/json/gap_filling/'

# Pull oxaria1 climate
#------------------
write_json2csv(folder=folder,topic_type='climate')

# Pull oxaria1 status
#------------------
write_json2csv(folder=folder,topic_type='status')

# Pull oxaria1 gases
#------------------
#write_json2csv(folder=folder,topic_type='gases')

# Pull oxaria1 pm
#------------------
write_json2csv(folder=folder,topic_type='pm')


