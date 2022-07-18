## Imports
##---------

import sys
sys.path.append('./oxaria/qoax')
from pull_topics import pull_topics
import os

os.chdir('./oxaria/data/raw/1oxaria/json/gap_filling/batch_2_feb21_may21/')
topic_path = './oxaria/topics/1oxaria/'

## Pull oxaria1 Jan
##------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2021-01-01T00:00:00Z', \
end_date='2021-02-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='jan21')

## Pull oxaria1 Feb
##------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2021-02-01T00:00:00Z', \
end_date='2021-03-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='feb21')

## Pull oxaria1 Mar
##------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2021-03-01T00:00:00Z', \
end_date='2021-04-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='mar21')

# Pull oxaria1 Apr
##------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2021-04-01T00:00:00Z', \
end_date='2021-05-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='apr21')

## Pull oxaria1 May
##------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2021-05-01T00:00:00Z', \
end_date='2021-06-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='may21')

## Pull oxaria1 Jun
##------------------
#pull_topics(topic_list=topic_path+'gases.csv', \
#topic_type='gases', \
#start_date='2021-06-01T00:00:00Z', \
#end_date='2021-07-01T00:00:00Z', \
#project_id='oxaria1', \
#outfile_id='jun21')
#
## Pull oxaria1 Jul
##------------------
#pull_topics(topic_list=topic_path+'gases.csv', \
#topic_type='gases', \
#start_date='2021-07-01T00:00:00Z', \
#end_date='2021-08-01T00:00:00Z', \
#project_id='oxaria1', \
#outfile_id='jul21')
#
## Pull oxaria1 Aug
##------------------
#pull_topics(topic_list=topic_path+'gases.csv', \
#topic_type='gases', \
#start_date='2021-08-01T00:00:00Z', \
#end_date='2021-09-01T00:00:00Z', \
#project_id='oxaria1', \
#outfile_id='aug21')
#
## Pull oxaria1 Sep
##------------------
#pull_topics(topic_list=topic_path+'gases.csv', \
#topic_type='gases', \
#start_date='2021-09-01T00:00:00Z', \
#end_date='2021-10-01T00:00:00Z', \
#project_id='oxaria1', \
#outfile_id='sep21')
#
## Pull oxaria1 Oct
##------------------
#pull_topics(topic_list=topic_path+'gases.csv', \
#topic_type='gases', \
#start_date='2021-10-01T00:00:00Z', \
#end_date='2021-11-01T00:00:00Z', \
#project_id='oxaria1', \
#outfile_id='oct21')
#
## Pull oxaria1 Nov
##------------------
#pull_topics(topic_list=topic_path+'gases.csv', \
#topic_type='gases', \
#start_date='2021-11-01T00:00:00Z', \
#end_date='2021-12-01T00:00:00Z', \
#project_id='oxaria1', \
#outfile_id='nov21')
#
## Pull oxaria1 Dec
##------------------
#pull_topics(topic_list=topic_path+'gases.csv', \
#topic_type='gases', \
#start_date='2021-12-01T00:00:00Z', \
#end_date='2021-01-01T00:00:00Z', \
#project_id='oxaria1', \
#outfile_id='dec21')
#
