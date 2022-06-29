# Imports
#---------

import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from pull_topics import pull_topics
import os

os.chdir('/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/1oxaria/json/gap_filling/may2022_download/')
topic_path = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/topics/1oxaria/'

## Pull oxaria1 Oct
##------------------
pull_topics(topic_list=topic_path+'particulates.csv', \
topic_type='pm', \
start_date='2021-10-01T00:00:00Z', \
end_date='2021-11-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='oct21')

## Pull oxaria1 Nov
##------------------
pull_topics(topic_list=topic_path+'particulates.csv', \
topic_type='pm', \
start_date='2021-11-01T00:00:00Z', \
end_date='2021-12-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='nov21')

## Pull oxaria1 Dec
##------------------
pull_topics(topic_list=topic_path+'particulates.csv', \
topic_type='pm', \
start_date='2021-12-01T00:00:00Z', \
end_date='2022-01-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='dec21')

# Pull oxaria1 Jan 2022
##----------------------
pull_topics(topic_list=topic_path+'particulates.csv', \
topic_type='pm', \
start_date='2022-01-01T00:00:00Z', \
end_date='2022-02-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='jan22')

## Pull oxaria1 Feb
##------------------
pull_topics(topic_list=topic_path+'particulates.csv', \
topic_type='pm', \
start_date='2022-02-01T00:00:00Z', \
end_date='2022-03-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='feb22')

# Pull oxaria1 Mar
#------------------
pull_topics(topic_list=topic_path+'particulates.csv', \
topic_type='pm', \
start_date='2022-03-01T00:00:00Z', \
end_date='2022-04-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='mar22')

# Pull oxaria1 Apr
#------------------
pull_topics(topic_list=topic_path+'particulates.csv', \
topic_type='pm', \
start_date='2022-04-01T00:00:00Z', \
end_date='2022-05-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='apr22')
