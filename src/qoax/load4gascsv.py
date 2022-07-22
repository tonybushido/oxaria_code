# Load 1-gases csvs

import pandas as pd
import numpy as np
import datetime as dt
import os

def load4gascsv(folder, topic):

    """
    Function to load SCS Praxis Urban CSV data to a Pandas Dataframe.

    Coverts a collection (folder) of csv files to a dataframe. Assumes the
    Praxis unit is a 4 gas sensor. If you are trying to load data from
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

    df_list = []
    if 'gases' in topic:
        for file in os.listdir(folder):
            if 'gases' in file and file.endswith('.csv.gz'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                header=None, \
                                low_memory=False, \
                                usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                                         16,17,18,19
                                ], \
                                names=['val.NO2.weV','val.NO2.cnc','val.NO2.aeV','val.NO2.weC', \
                                       'val.Ox.weV','val.Ox.cnc','val.Ox.aeV','val.Ox.weC', \
                                       'val.NO.weV','val.NO.cnc','val.NO.aeV','val.NO.weC', \
                                       'val.CO.weV','val.CO.cnc','val.CO.aeV','val.CO.weC', \
                                       'val.sht.hmd','val.sht.tmp','rec','tag'], \
                                parse_dates=['rec']
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
    if 'particulate' in topic:
        for file in os.listdir(folder):
            if 'pm' in file and file.endswith('.csv.gz'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                header=None, \
                                low_memory=False, \
                                usecols=[0,1,2,3,4,5,6,7,8,9,
                                         10,11,12,13,14,15,16,17,18,19,
                                         20,21,22,23,24,25,26,27,28,29,
                                         30,31,32,33,34,35,36,37], \
                                names=['val.mtf1','val.pm1','val.mtf5','val.pm2p5','val.bin:0','val.bin:1', \
                                       'val.bin:2','val.bin:3','val.bin:4','val.bin:5','val.bin:6','val.bin:7', \
                                       'val.bin:8','val.bin:9','avl.bin:10','val.bin:11','val.bin:12', \
                                       'val.bin:13','val.bin:14','val.bin:15','val.bin:16','val.bin:17', \
                                       'val.bin:18','val.bin:19','val.bin:20','val.bin:21','val.bin:22', \
                                       'val.bin:23','val.mtf3','val.pm10','val.mtf7','val.per','val.sfr', \
                                       'val.sht.hmd','val.sht.tmp','rec','tag','src'
                                      ], \
                                parse_dates=['rec']
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
    if 'status' in topic:
        for file in os.listdir(folder):
            if 'status' in file and file.endswith('.csv.gz'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                header=None, \
                                low_memory=False, \
                                usecols=[0,1,2,3,4,5,6,7,8,9,
                                         10,11,12,13,14,15,16,17,18,19,
                                         20,21,22,23,24,25,26,27,28,29,30
                                        ], \
                                names=['val.sch.scs-particulates.tally','val.sch.scs-particulates.interval', \
                                       'val.sch.scs-status.tally','val.sch.scs-status.interval', \
                                       'val.sch.scs-climate.tally','val.sch.scs-climate.interval', \
                                       'val.sch.scs-gases.tally','val.sch.scs-gases.interval', \
                                       'val.gps.pos:0','val.gps.pos:1','val.gps.elv','val.gps.qual', \
                                       'val.up.load.av15','val.up.load.av1','val.up.load.av5','val.up.period', \
                                       'val.up.users','val.psu.prot-batt','val.psu.rst','val.psu.chg', \
                                       'val.psu.standby','val.psu.pwr-in','val.psu.host-3v3', \
                                       'val.psu.batt-flt','val.tz.name','val.tz.utc-offset','val.tmp.brd', \
                                       'rec','tag','x','y'], \
                                #parse_dates=['rec']
                                )
                df.columns = map(str.lower, df.columns)
                #df['rec'] = pd.to_datetime(df['rec'],errors='raise',utc=True, \
                #               unit='ns',origin='unix',infer_datetime_format=True, yearfirst=True)
                #df['rec'].dt.round('10S') # sorts the wooblyness in the praxis early doors
                #df = df.astype({col: 'int32' for col in df.select_dtypes('int64').columns})
                #df = df.astype({col: np.float32 for col in df.select_dtypes('float64').columns})
                #df.set_index(['tag','rec'], inplace=True, drop=True)
                #df.sort_index(axis=0,inplace=True)
                df_list.append(df)
        df = pd.concat(df_list)
        #df = df.loc[~df.index.duplicated(keep='last')]
    if 'climate' in topic:
        for file in os.listdir(folder):
            if 'climate' in file and file.endswith('.csv.gz'):
                print(folder+file)
                df = pd.read_csv(folder+file, \
                                header=None, \
                                low_memory=False, \
                                usecols=[0,1,2,3,4,], \
                                names=['val.hmd','val.tmp','val.bar','rec','tag'], \
                                #parse_dates=['rec']
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
    return df

if __name__ == '__main__':
    main()
