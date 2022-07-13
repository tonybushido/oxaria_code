# Imports
#---------

import sys
sys.path.append('/home/tonyb/Gdrive/MinicondaProjects/oxaria/qoax')
from pull_topics import pull_topics
import os

os.chdir('/home/tonyb/Gdrive/MinicondaProjects/oxaria/data/raw/1oxaria/json/gap_filling/')
topic_path = '/home/tonyb/Gdrive/MinicondaProjects/oxaria/topics/1oxaria/'

# Pull oxaria1 Jan
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-01-01T00:00:00Z', \
end_date='2020-02-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='jan')

# Pull oxaria1 Feb
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-02-01T00:00:00Z', \
end_date='2020-03-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='feb')

# Pull oxaria1 Mar
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-03-01T00:00:00Z', \
end_date='2020-04-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='mar')

# Pull oxaria1 Apr
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-04-01T00:00:00Z', \
end_date='2020-05-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='apr')

# Pull oxaria1 May
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-05-01T00:00:00Z', \
end_date='2020-06-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='may')

# Pull oxaria1 Jun
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-06-01T00:00:00Z', \
end_date='2020-07-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='jun')

# Pull oxaria1 Jul
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-07-01T00:00:00Z', \
end_date='2020-08-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='jul')

# Pull oxaria1 Aug
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-08-01T00:00:00Z', \
end_date='2020-09-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='aug')

# Pull oxaria1 Sep
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-09-01T00:00:00Z', \
end_date='2020-10-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='sep')

# Pull oxaria1 Oct
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-10-01T00:00:00Z', \
end_date='2020-11-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='oct')

# Pull oxaria1 Nov
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-11-01T00:00:00Z', \
end_date='2020-12-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='nov')

# Pull oxaria1 Dec
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2020-12-01T00:00:00Z', \
end_date='2021-01-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='dec')

# Pull oxaria1 Jan
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2021-01-01T00:00:00Z', \
end_date='2021-02-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='jan21')

# Pull oxaria1 Feb
#------------------
pull_topics(topic_list=topic_path+'climate.csv', \
topic_type='climate', \
start_date='2021-02-01T00:00:00Z', \
end_date='2021-03-01T00:00:00Z', \
project_id='oxaria1', \
outfile_id='feb21')
