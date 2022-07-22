# Function to load a 15-min average sensor file from feather file

def load_s15_df_from_ftr(folder, ftr):

"""
    Function to load a sensor file to df from a feather file &
    convert all 64 bit floats to 32 bits for space saving.

    
    Parameters
    ----------
    folder : str
        The foldercontaining the ftr file. 
        
    ftr: str
        The name of the ftr file to load. 

    Returns
    -------
    Dataframe
        A df of the ftr with 'tag' & 'rec' columns as index. 

    """
    
    df = pd.read_feather(folder+ftr)
    cols = df.select_dtypes(np.float64).columns 
    df[cols] = df[cols].astype(np.float32)
    df = df.set_index(['tag','rec']).sort_index()
    return df
    
if __name__ == '__main__':
    main()