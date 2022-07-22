# Load 4-gases.csvs

import datetime as dt
import os
import tarfile
from io import BytesIO

import numpy as np
import pandas as pd


def loadgascsv_tgz(tgz_file, topic):

    """
    Function to load SCS Praxis Urban CSV data to a Pandas Dataframe.

    Coverts a collection (folder) of.csv files to a dataframe. Assumes the
    Praxis unit is a 4 gas sensor. If you are trying to load data from
    a 4 gas unit use its 'load4ga.csv' sibling function.

    Parameters
    ----------
    tgz_file : str
        Filename & (optionally) path of the files to be loaded.
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
    # -----------

    # Define a list of common vocab to identify files
    pm_flag = ["part", "pm"]
    gas_flag = ["no2", "gas"]
    clim_flag = ["clim"]
    stat_flag = ["status"]
    # Empty list to receive df for each file
    df_list = []

    # Open tar file
    # ---------------
    with tarfile.open(tgz_file, mode="r:gz") as tar_file:

        # Loop over topic categories, extract & load
        # -------------------------------------------
        # Do gases
        if "gases" in topic:
            for member in tar_file.getmembers():
                if "gases" in member.name and member.name.endswith("csv"):
                    print("Loading...  "+member.name)
                    content = tar_file.extractfile(member).read()
                    df = pd.read_csv(BytesIO(content), encoding="utf8")
                    df.columns = map(str.lower, df.columns)
                    df["rec"] = pd.to_datetime(
                        df["rec"],
                        errors="coerce",
                        utc=True,
                        unit="ns",
                        origin="unix",
                        yearfirst=True,
                    )  # infer_datetime_format=True,
                    df["rec"].dt.round(
                        "10S"
                    )  # sorts the wooblyness in the praxis early doors
                    df = df.astype(
                        {col: "int32" for col in df.select_dtypes("int64").columns}
                    )
                    df = df.astype(
                        {col: np.float32 for col in df.select_dtypes("float64").columns}
                    )
                    df.set_index(["tag", "rec"], inplace=True, drop=True)
                    df.sort_index(axis=0, inplace=True)
                    df_list.append(df)
            df = pd.concat(df_list)
            df["insert_date"] = dt.datetime.now(dt.timezone.utc).strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            df = df.loc[~df.index.duplicated(keep="last")]

        # Do particles
        if "particulate" in topic:
            for member in tar_file.getmembers():
                if "pm" in member.name and member.name.endswith(".csv"):
                    print("Loading...  "+member.name)
                    content = tar_file.extractfile(member).read()
                    df = pd.read_csv(BytesIO(content), encoding="utf8")
                    df.columns = map(str.lower, df.columns)
                    df["rec"] = pd.to_datetime(
                        df["rec"],
                        errors="coerce",
                        utc=True,
                        unit="ns",
                        origin="unix",
                        yearfirst=True,
                    )
                    df["rec"].dt.round(
                        "10S"
                    )  # sorts the wooblyness in the praxis early doors
                    df = df.astype(
                        {col: "int32" for col in df.select_dtypes("int64").columns}
                    )
                    df = df.astype(
                        {col: np.float32 for col in df.select_dtypes("float64").columns}
                    )
                    df.set_index(["tag", "rec"], inplace=True, drop=True)
                    df.sort_index(axis=0, inplace=True)
                    df_list.append(df)
            df = pd.concat(df_list)
            df["insert_date"] = dt.datetime.now(dt.timezone.utc).strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            df = df.loc[~df.index.duplicated(keep="last")]

        # Do status
        if "status" in topic:
            for member in tar_file.getmembers():
                if "status" in member.name and member.name.endswith(".csv"):
                    print("Loading...  "+member.name)
                    content = tar_file.extractfile(member).read()
                    df = pd.read_csv(BytesIO(content), encoding="utf8")
                    df.columns = map(str.lower, df.columns)
                    df["rec"] = pd.to_datetime(
                        df["rec"],
                        errors="coerce",
                        utc=True,
                        unit="ns",
                        origin="unix",
                        yearfirst=True,
                    )
                    df["rec"].dt.round(
                        "10S"
                    )  # sorts the wooblyness in the praxis early doors
                    df = df.astype(
                        {col: "int32" for col in df.select_dtypes("int64").columns}
                    )
                    df = df.astype(
                        {col: np.float32 for col in df.select_dtypes("float64").columns}
                    )
                    df.set_index(["tag", "rec"], inplace=True, drop=True)
                    df.sort_index(axis=0, inplace=True)
                    df_list.append(df)
            df = pd.concat(df_list)
            df["insert_date"] = dt.datetime.now(dt.timezone.utc).strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            df = df.loc[~df.index.duplicated(keep="last")]

        # Do climate
        if "climate" in topic:
            for member in tar_file.getmembers():
                if "climate" in member.name and member.name.endswith(".csv"):
                    print("Loading...  "+member.name)
                    content = tar_file.extractfile(member).read()
                    df = pd.read_csv(BytesIO(content), encoding="utf8")
                    df.columns = map(str.lower, df.columns)
                    df["rec"] = pd.to_datetime(
                        df["rec"],
                        errors="coerce",
                        utc=True,
                        unit="ns",
                        origin="unix",
                        yearfirst=True,
                    )
                    df["rec"].dt.round(
                        "10S"
                    )  # sorts the wooblyness in the praxis early doors
                    df = df.astype(
                        {col: "int32" for col in df.select_dtypes("int64").columns}
                    )
                    df = df.astype(
                        {col: np.float32 for col in df.select_dtypes("float64").columns}
                    )
                    df.set_index(["tag", "rec"], inplace=True, drop=True)
                    df.sort_index(axis=0, inplace=True)
                    df_list.append(df)
            df = pd.concat(df_list)
            df["insert_date"] = dt.datetime.now(dt.timezone.utc).strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            df = df.loc[~df.index.duplicated(keep="last")]
    return df


if __name__ == "__main__":
    main()
