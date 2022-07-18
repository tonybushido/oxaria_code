## Imports
##---------

import sys
sys.path.append('./oxaria/qoax')
from pull_topics import pull_topics
import os

os.chdir('./oxaria/data/raw/2oxaria/json/gap_filling/batch_2_feb21_may21/')
topic_path = './oxaria/topics/2oxaria/'

## Pull oxaria2 Jan
##------------------
pull_topics(topic_list=topic_path+'status.csv', \
topic_type='status', \
start_date='2021-01-01T00:00:00Z', \
end_date='2021-02-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='jan21')

## Pull oxaria2 Feb
##------------------
pull_topics(topic_list=topic_path+'status.csv', \
topic_type='status', \
start_date='2021-02-01T00:00:00Z', \
end_date='2021-03-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='feb21')

## Pull oxaria2 Mar
##------------------
pull_topics(topic_list=topic_path+'status.csv', \
topic_type='status', \
start_date='2021-03-01T00:00:00Z', \
end_date='2021-04-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='mar21')

# Pull oxaria2 Apr
##------------------
pull_topics(topic_list=topic_path+'status.csv', \
topic_type='status', \
start_date='2021-04-01T00:00:00Z', \
end_date='2021-05-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='apr21')

## Pull oxaria2 May
##------------------
pull_topics(topic_list=topic_path+'status.csv', \
topic_type='status', \
start_date='2021-05-01T00:00:00Z', \
end_date='2021-06-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='may21')

## Pull oxaria2 Jun
##------------------
#pull_topics(topic_list=topic_path+'status.csv', \
#topic_type='status', \
#start_date='2021-06-01T00:00:00Z', \
#end_date='2021-07-01T00:00:00Z', \
#project_id='oxaria2', \
#outfile_id='jun21')
#
## Pull oxaria2 Jul
##------------------
#pull_topics(topic_list=topic_path+'status.csv', \
#topic_type='status', \
#start_date='2021-07-01T00:00:00Z', \
#end_date='2021-08-01T00:00:00Z', \
#project_id='oxaria2', \
#outfile_id='jul21')
#
## Pull oxaria2 Aug
##------------------
#pull_topics(topic_list=topic_path+'status.csv', \
#topic_type='status', \
#start_date='2021-08-01T00:00:00Z', \
#end_date='2021-09-01T00:00:00Z', \
#project_id='oxaria2', \
#outfile_id='aug21')
#
## Pull oxaria2 Sep
##------------------
#pull_topics(topic_list=topic_path+'status.csv', \
#topic_type='status', \
#start_date='2021-09-01T00:00:00Z', \
#end_date='2021-10-01T00:00:00Z', \
#project_id='oxaria2', \
#outfile_id='sep21')
#
## Pull oxaria2 Oct
##------------------
#pull_topics(topic_list=topic_path+'status.csv', \
#topic_type='status', \
#start_date='2021-10-01T00:00:00Z', \
#end_date='2021-11-01T00:00:00Z', \
#project_id='oxaria2', \
#outfile_id='oct21')
#
## Pull oxaria2 Nov
##------------------
#pull_topics(topic_list=topic_path+'status.csv', \
#topic_type='status', \
#start_date='2021-11-01T00:00:00Z', \
#end_date='2021-12-01T00:00:00Z', \
#project_id='oxaria2', \
#outfile_id='nov21')
#
## Pull oxaria2 Dec
##------------------
#pull_topics(topic_list=topic_path+'status.csv', \
#topic_type='status', \
#start_date='2021-12-01T00:00:00Z', \
#end_date='2021-01-01T00:00:00Z', \
#project_id='oxaria2', \
#outfile_id='dec21')
#
