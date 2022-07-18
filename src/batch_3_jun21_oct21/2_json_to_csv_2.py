# Imports
#---------

import sys
sys.path.append('./oxaria/qoax')
from write_json2csv import write_json2csv
import os

os.chdir('./oxaria/raw/2oxaria/json/gap_filling/batch_3_jun21_oct21/')
folder = './oxaria/raw/2oxaria/json/gap_filling/batch_3_jun21_oct21/'

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


