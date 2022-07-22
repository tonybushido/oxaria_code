# Load 1-gases csvs

import pandas as pd
import numpy as np
import datetime as dt
import os

def load1gascsv_v2(folder, topic):

    """
    Function to load SCS Praxis Urban CSV data to a Pandas Dataframe.

    Coverts a collection (folder) of csv files to a dataframe. Assumes the
    Praxis unit is a 1 gas sensor (NO2). If you are trying to load data from
    a 4 gas unit use its 'load4gascsv' sibling function.

    Parameters
    ----------
    folder : str
        A path to the folder containing the files to be loaded.
    topic : str
        A flag for the topic category being loaded. The vocab of this parameter
        is constrained to the topics defined by SCS, e.g.
        - gases
        - particulates
        - status
        - climate

    Returns
    -------
    Dataframe
        A Pandas dataframe.

    """

    # Variables
    #-----------

    # Define a list of common vocab to identify files
    pm_flag = ['part','pm']
    gas_flag = ['no2','gas']
    clim_flag = ['clim']
    stat_flag = ['status']
    # Empty list to receive df for each file
    df_list = []

    # Loop over topic categories & load
    #-----------------------------------

    # Do gases
    if 'gases' in topic:
        for file in os.listdir(folder):
            if 'gases' in file and file.endswith('.csv'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                low_memory=False, \
                                compression='infer', \
                                )
                df.columns = map(str.lower, df.columns)
                df['rec'] = pd.to_datetime(df['rec'],errors='raise',utc=True, \
                               unit='ns',origin='unix',infer_datetime_format=True)
                df['rec'].dt.round('10S') # sorts the wooblyness in the praxis early doors
                df = df.astype({col: 'int32' for col in df.select_dtypes('int64').columns})
                df = df.astype({col: np.float32 for col in df.select_dtypes('float64').columns})
                df.set_index(['tag','rec'], inplace=True, drop=True)
                df.sort_index(axis=0,inplace=True)
                df_list.append(df)
        df = pd.concat(df_list)
        df = df.loc[~df.index.duplicated(keep='last')]

    #Do particles
    if 'particulate' in topic:
        for file in os.listdir(folder):
            if 'pm' in file and file.endswith('.csv'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                low_memory=False, \
                                compression='infer', \
                                )
                df.columns = map(str.lower, df.columns)
                df['rec'] = pd.to_datetime(df['rec'],errors='raise',utc=True, \
                               unit='ns',origin='unix',yearfirst=True)
                df['rec'].dt.round('10S') # sorts the wooblyness in the praxis early doors
                df = df.astype({col: 'int32' for col in df.select_dtypes('int64').columns})
                df = df.astype({col: np.float32 for col in df.select_dtypes('float64').columns})
                df.set_index(['tag','rec'], inplace=True, drop=True)
                df.sort_index(axis=0,inplace=True)
                df_list.append(df)
        df = pd.concat(df_list)
        df = df.loc[~df.index.duplicated(keep='last')]

    # Do status
    if 'status' in topic:
        for file in os.listdir(folder):
            if 'status' in file and file.endswith('.csv'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                low_memory=False, \
                                compression='infer', \
                                )
                df.columns = map(str.lower, df.columns)
                df['rec'] = pd.to_datetime(df['rec'],errors='raise',utc=True, \
                               unit='ns',origin='unix',yearfirst=True)
                df['rec'].dt.round('10S') # sorts the wooblyness in the praxis early doors
                df = df.astype({col: 'int32' for col in df.select_dtypes('int64').columns})
                df = df.astype({col: np.float32 for col in df.select_dtypes('float64').columns})
                df.set_index(['tag','rec'], inplace=True, drop=True)
                df.sort_index(axis=0,inplace=True)
                df_list.append(df)
        df = pd.concat(df_list)
        df = df.loc[~df.index.duplicated(keep='last')]

    # Do climate
    if 'climate' in topic:
        for file in os.listdir(folder):
            if 'climate' in file and file.endswith('.csv'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                low_memory=False, \
                                compression='infer', \
                                )
                df.columns = map(str.lower, df.columns)
                df['rec'] = pd.to_datetime(df['rec'],errors='raise',utc=True, \
                               unit='ns',origin='unix',yearfirst=True)
                df['rec'].dt.round('10S') # sorts the wooblyness in the praxis early doors
                df = df.astype({col: 'int32' for col in df.select_dtypes('int64').columns})
                df = df.astype({col: np.float32 for col in df.select_dtypes('float64').columns})
                df.set_index(['tag','rec'], inplace=True, drop=True)
                df.sort_index(axis=0,inplace=True)
                df_list.append(df)
        df = pd.concat(df_list)
        df = df.loc[~df.index.duplicated(keep='last')]
    return df

if __name__ == '__main__':
    main()
