# Function to subset RF model training df by date & std RF training columns

import pandas as pd
import numpy as np
import datetime as dt

def subset_training_data(in_dfs, start_date=None, end_date=None):
    
    """
    Function to subset & process a list of 1 or more dataframes by date 
    for RF model training. Use it to remove extraneous crap not need for 
    model training & to constrain a preferred training timeframe.
    
    Expects as input stable 15-minute dfs ('*15*', '*stable15*' dfs 
    etc.) which have had training features added using 'add_lag_features' 
    and 'add_rushhour_features' functions.

    Parameters
    ----------
    in_dfs : list of dfs
        A list of dataframes to be processed. 
    start_date : str
        The start of the model training time period to keep in well known
        format (yyyy-mm-dd, dd/mm/yyyy etc.)
    end_date : str
        The end of the model training time period to keep in well known
        format (yyyy-mm-dd, dd/mm/yyyy etc.)

    Returns
    -------
    Dataframe
        A concatenated Pandas dataframe of all the dfs in 'in_dfs'.

    """
    
    tmplist = []
    for df in in_dfs:
        if start_date == None:
            start_date = '2020-01-01'
            start = pd.to_datetime(
                start_date, infer_datetime_format=True, utc=True)
        else:
            start = pd.to_datetime(
                start_date, infer_datetime_format=True, utc=True)
        if end_date == None:
            end_date = '2024-01-01'
            end = pd.to_datetime(
                end_date, infer_datetime_format=True, utc=True)
        else:
            end = pd.to_datetime(
                end_date, infer_datetime_format=True, utc=True)
        try:
            df = df.reset_index('tag')
        except:
            print('Expecting tag & rec in a 2-level index')
        df = df.reset_index().query('@start <= rec <= @end')
        df = df.loc[:, [
            'tag',
            'rec',
            'val.mtf1',
            'val.mtf5',
            'val.mtf3',
            'val.mtf7',
            'val.sfr',
            'val.sht.hmd_p',
            'val.sht.tmp_p',
            'pc15_val.mtf1',
            'pc15_val.mtf5',
            'pc15_val.mtf3',
            'pc15_val.mtf7',
            'pc15_val.sfr',
            'pc15_val.sht.hmd_p',
            'pc15_val.sht.tmp_p',
            'pc30_val.mtf1',
            'pc30_val.mtf5',
            'pc30_val.mtf3',
            'pc30_val.mtf7',
            'pc30_val.sfr',
            'pc30_val.sht.hmd_p',
            'pc30_val.sht.tmp_p',
            'hour',
            'day',
            'rushhour',
            'val.pm10_1_c1',
            'pc15_val.pm10_1_c1',
            'pc30_val.pm10_1_c1'
        ]]
        df = df.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
        tmplist.append(df)
    train_df = pd.concat(tmplist).set_index(['tag','rec'])
    return train_df

if __name__ == '__main__':
    main()