# A feature engineering function to generate rushour related features for 
# the RF model.

import pandas as pd
import numpy as np
import datetime as dt

def add_rushhour_features(df):

    """
    Function to add new 'rushhour' features to a candidate RF training df.
    Each record coded up with rushhour features;
    
     hour = int flag for the hour of observation
     day = int flag for the day of observation
     rushhour = int lag(s) for off-peak, morning & evening rush hours
    
    Parameters
    ----------
    df : dataframe
        The dataframe containing 15-miute average sensor observations to
        to be coded. 

    Returns
    -------
    Dataframe
        A df with coded features added for all numeric columns. 

    """
    
    # calc integer flags for hour of observation
    df['hour'] = df.index.get_level_values(1).hour
    # and day of week
    df['day'] = df.index.get_level_values(1).dayofweek
    # and integer flag(s) for off-peak, morning & evening rush hours
    df.loc[(df.index.get_level_values(1).time >= dt.time(7, 30, 0)) &
           (df.index.get_level_values(1).time >= dt.time(9, 30, 0)) &
           (df.index.get_level_values(1).weekday < 5), 'rushhour'] = 1
    df.loc[(df.index.get_level_values(1).time >= dt.time(16, 0, 0)) &
           (df.index.get_level_values(1).time >= dt.time(18, 0, 0)) &
           (df.index.get_level_values(1).weekday < 5), 'rushhour'] = 2
    df['rushhour'] = np.where(df['rushhour'] >= 1, df['rushhour'],
                              0).astype(np.int32)
    return df
    
if __name__ == '__main__':
    main()