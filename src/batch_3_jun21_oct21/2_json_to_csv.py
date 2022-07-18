# Imports
#---------

import sys
sys.path.append('./oxaria/qoax')
from write_json2csv import write_json2csv
import os

os.chdir('./oxaria/raw/1oxaria/json/gap_filling/batch_3_jun21_oct21/')
folder = './oxaria/raw/1oxaria/json/gap_filling/batch_3_jun21_oct21/'

# Pull oxaria1 climate
#------------------
#write_json2csv(folder=folder,topic_type='climate')

# Pull oxaria1 status
#------------------
#write_json2csv(folder=folder,topic_type='status')

# Pull oxaria1 gases
#------------------
write_json2csv(folder=folder,topic_type='gases')

# Pull oxaria1 pm
#------------------
#write_json2csv(folder=folder,topic_type='pm')


