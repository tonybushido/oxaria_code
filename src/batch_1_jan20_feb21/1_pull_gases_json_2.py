# Imports
#---------

import sys
sys.path.append('./oxaria/qoax')
from pull_topics import pull_topics
import os

os.chdir('./oxaria/data/raw/2oxaria/json/gap_filling/')
topic_path = './oxaria/topics/2oxaria/'

# Pull oxaria2 Jan
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-01-01T00:00:00Z', \
end_date='2020-02-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='jan')

# Pull oxaria2 Feb
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-02-01T00:00:00Z', \
end_date='2020-03-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='feb')

# Pull oxaria2 Mar
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-03-01T00:00:00Z', \
end_date='2020-04-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='mar')

# Pull oxaria2 Apr
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-04-01T00:00:00Z', \
end_date='2020-05-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='apr')

# Pull oxaria2 May
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-05-01T00:00:00Z', \
end_date='2020-06-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='may')

# Pull oxaria2 Jun
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-06-01T00:00:00Z', \
end_date='2020-07-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='jun')

# Pull oxaria2 Jul
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-07-01T00:00:00Z', \
end_date='2020-08-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='jul')

# Pull oxaria2 Aug
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-08-01T00:00:00Z', \
end_date='2020-09-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='aug')

# Pull oxaria2 Sep
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-09-01T00:00:00Z', \
end_date='2020-10-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='sep')

# Pull oxaria2 Oct
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-10-01T00:00:00Z', \
end_date='2020-11-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='oct')

# Pull oxaria2 Nov
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-11-01T00:00:00Z', \
end_date='2020-12-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='nov')

# Pull oxaria2 Dec
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2020-12-01T00:00:00Z', \
end_date='2021-01-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='dec')

# Pull oxaria2 Jan
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2021-01-01T00:00:00Z', \
end_date='2021-02-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='jan')

# Pull oxaria2 Feb
#------------------
pull_topics(topic_list=topic_path+'gases.csv', \
topic_type='gases', \
start_date='2021-02-01T00:00:00Z', \
end_date='2021-03-01T00:00:00Z', \
project_id='oxaria2', \
outfile_id='feb')
