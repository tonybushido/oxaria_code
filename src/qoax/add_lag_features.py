# A feature engineering function to generate time lagged feature for the
# RF model.

import pandas as pd

def add_lag_features(df):

    """
    Function to add new 'lagged' features to a candidate RF training df.
    Lagged features contain the % change of the previous 1-2 observations, 
    prefixed with pc15_* & pc30_*

    Parameters
    ----------
    df : dataframe
        The dataframe containing 15-miute average sensor observations to
        to be lagged b 15 & 30-minutes. 

    Returns
    -------
    Dataframe
        A df with lagged features added for all numeric columns. 

    """
    
    # calc % change in all df cols over last 15 mins
    tmpdf1 = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna(
        axis=1, how='all').pct_change(periods=1)
    tmpdf1.columns = ['pc15_' + name for name in list(tmpdf1.columns)]
    # and same over last 30 mins
    tmpdf2 = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna(
        axis=1, how='all').pct_change(periods=2)
    tmpdf2.columns = ['pc30_' + name for name in list(tmpdf2.columns)]
    # merge % change stats back on to original df
    df = df.merge(tmpdf1, left_index=True, right_index=True,
                  how='left').merge(tmpdf2,
                                    left_index=True,
                                    right_index=True,
                                    how='left').set_index(['tag', 'rec'])
    return df

if __name__ == '__main__':
    main()
    
