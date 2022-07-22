import datetime as dt
import pickle

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from lightgbm import LGBMRegressor
from scipy import stats
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import (GridSearchCV, cross_val_score,
                                     train_test_split)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer

    """
    Helper functions used in OxAria ML dev.

    A range of regular operations documented here which are used iteratvely
    in developing OxAria ML workflows.

    Poorly documented here, deployed with greater context in the codebase.

    Parameters
    ----------
    Various, to do.

    Returns
    -------
    Various, to do.

    """


# Sensor data for colocated device at St Ebbes
# ----------------------------------------------
def load_no24_training(folder, ftr_list, combo_cols):
    df_list = []
    tuple_list = zip(ftr_list, combo_cols)
    for f, c in tuple_list:
        # read the feather files
        dftmp = pd.read_feather(folder + f).set_index(["tag", "rec"]).sort_index()
        # Convert all float64 cols to float32
        cols = dftmp.select_dtypes(np.float64).columns
        dftmp[cols] = dftmp[cols].astype(np.float32)
        # Combine the reference method conc column into 1 column
        dftmp["no2_ppb_combo"] = dftmp[c]
        # If its below 3 ug.m-3, its probably not, so set to nan
        dftmp["no2_ppb_combo"] = np.where(
            dftmp["no2_ppb_combo"] < 3.0, np.nan, dftmp["no2_ppb_combo"]
        )
        df_list.append(dftmp)
    df_out = pd.concat(df_list)
    return df_out


# Function to generate time lagged feature
# -----------------------------------------
def no2_feature_gen(df):
    # calc % change in all df cols over last 15 mins
    tmpdf1 = (
        df.apply(lambda x: pd.to_numeric(x, errors="coerce"))
        .dropna(axis=1, how="all")
        .pct_change(periods=1)
    )
    tmpdf1.columns = ["pc15_" + name for name in list(tmpdf1.columns)]
    # and same over last 30 mins
    tmpdf2 = (
        df.apply(lambda x: pd.to_numeric(x, errors="coerce"))
        .dropna(axis=1, how="all")
        .pct_change(periods=2)
    )
    tmpdf2.columns = ["pc30_" + name for name in list(tmpdf2.columns)]
    # merge % change stats back on to original df
    df = (
        df.merge(tmpdf1, left_index=True, right_index=True, how="left")
        .merge(tmpdf2, left_index=True, right_index=True, how="left")
        .set_index(["tag", "rec"])
    )
    return df


# Function to generate rush hour & temporal flag features
# --------------------------------------------------------
def rushhour(df):
    # calc integer flags for hour of observation
    df["hour"] = df.index.get_level_values(1).hour
    # and day of week
    df["day"] = df.index.get_level_values(1).dayofweek
    # and integer flag(s) for off-peak, morning & evening rush hours
    df.loc[
        (df.index.get_level_values(1).time >= dt.time(7, 30, 0))
        & (df.index.get_level_values(1).time >= dt.time(9, 30, 0))
        & (df.index.get_level_values(1).weekday < 5),
        "rushhour",
    ] = 1
    df.loc[
        (df.index.get_level_values(1).time >= dt.time(16, 0, 0))
        & (df.index.get_level_values(1).time >= dt.time(18, 0, 0))
        & (df.index.get_level_values(1).weekday < 5),
        "rushhour",
    ] = 2
    df["rushhour"] = np.where(df["rushhour"] >= 1, df["rushhour"], 0).astype(np.int32)
    return df


# Function to constrain get training features for a soecific date envelope
# --------------------------------------------------------------------------
def get_training_no2(dfs, env_start, env_stop):
    start = pd.to_datetime(env_start, yearfirst=True, utc=True)
    end = pd.to_datetime(env_stop, yearfirst=True, utc=True)

    print(
        "Getting training features for sensors between: "
        + str(start)
        + " and "
        + str(end)
        + "\n"
    )
    df_list = []

    for df in dfs:
        dftmp = df.query("@start <= rec < @end").reset_index().set_index(["tag", "rec"])
        df_list.append(dftmp)

    df_out = pd.concat(df_list).sort_index()
    df_out = df_out[~df_out.index.duplicated()]
    df_out = df_out.loc[
        :,
        [
            "val.no2.wev",
            "val.no2.aev",
            "val.no2.wec",
            "val.hmd",
            "val.tmp",
            "no2_ppb_combo",
            "no2_ppb_s",
            "no2_ppb_h",
            "val.no2.cnc_1_c1",
            "pc15_val.no2.wev",
            "pc15_val.no2.aev",
            "pc15_val.no2.wec",
            "pc15_val.hmd",
            "pc15_val.tmp",
            "pc15_val.no2.cnc_1_c1",
            "pc30_val.no2.wev",
            "pc30_val.no2.cnc",
            "pc30_val.no2.aev",
            "pc30_val.no2.wec",
            "pc30_val.hmd",
            "pc30_val.tmp",
            "pc30_val.no2.cnc_1_c1",
            "hour",
            "day",
            "rushhour",
        ],
    ]
    df_out = df_out.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
    print(
        "Sensors in output :"
        + str(df_out.index.get_level_values(0).unique().tolist())
        + "\n"
    )
    return df_out


# Define a function to test model performance based on a range of max. no, of leaf node sizes
# ---------------------------------------------------------------------------------------------
# The following function estimates mean absolute error as a metric for model
# accuracy.The number of trees used is set to 100 (i.e. n_estimators). 500 trees have also been tested but
# without any imporvement in accuracy so 100 is used to reduce training times.
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    # Define the model
    model = RandomForestRegressor(
        max_leaf_nodes=max_leaf_nodes,
        random_state=7,
        n_jobs=-1,
        max_depth=max_depth,
        min_samples_leaf=1,
        min_samples_split=2,
        n_estimators=12000,
    )

    # Create a v simple pipeline that imputes missing input values before fitting the model to them
    # -----------------------------------------------------------------------------------------------
    my_pipeline = Pipeline(steps=[("preprocessor", SimpleImputer()), ("model", model)])

    # Calculate a metric variable using the cross_val_score function
    # ----------------------------------------------------------------
    # The block below performs a cross validation excersise. For a given model configuration, it splits the
    # training set in 5 subsets and carries out a training sequence with the mean absolute error as a metric
    # of performance.
    # An avergae of those 5 MAE is then returned (see Figure below 'Validation' label).
    # This procedure ensures a robust training sequence as it removes the chance of
    # selecting a validation set that is very similar to the testing subset.
    #
    # Fit 5 random subsets of train_x & train_y to the pipeline RFR model & calc mean absolute error
    # multiply by -1 since sklearn calculates *negative* MAE
    metric = -1 * cross_val_score(
        my_pipeline, train_X, train_y, cv=5, scoring="neg_mean_absolute_error"
    )

    # Train the model
    my_pipeline.fit(train_X, train_y)

    # Predict dependent variable using validation & training subsets of independent variables
    preds_val = my_pipeline.predict(val_X)
    preds_tr = my_pipeline.predict(train_X)

    # MAE calculation for training and validation data
    mae_ver = mean_absolute_error(val_y, preds_val)
    mae_tr = mean_absolute_error(train_y, preds_tr)

    # Bring it all together in outputs
    return (mae_ver, mae_tr, metric.mean())


# Function to plot a storyboard of model validation
# --------------------------------------------------
def plot_training_story_board(df, title, save_it, xylim, *args):
    sns.set_style("white", {"axes.grid": False})
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.3))
    fig.suptitle(
        title, y=1.1, fontsize=14,
    )
    plt.rcParams["ytick.labelsize"] = "12"
    plt.rcParams["xtick.labelsize"] = "12"
    plt.rcParams["figure.titlesize"] = "12"

    # xlim = xylim[0], xylim[1])
    axes[0].set_xlim(xylim[0], xylim[1])

    # Get regression stats - sensor vs reference method
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        train_df["val.no2.cnc_1_c1"], train_df["no2_ppb_combo"]
    )
    # Plot it
    sns.regplot(
        x=train_df["no2_ppb_combo"],
        y=train_df["val.no2.cnc_1_c1"],
        color="tab:blue",
        line_kws={
            "label": "y = {0:.3f}x+{1:.2f},  R-sqd = {3:.2f}".format(
                slope, intercept, r_value, r_value ** 2
            )
        },
        ax=axes[0],
        truncate=False,
    )
    axes[0].set(
        xlabel="AURN NO2 (ppb)",
        ylabel="Sensor NO2 (ppb)",
        title="Uncorrected sensor vs Reference method\n (all observations)",
        xlim=(-10, 180),
        ylim=(-10, 180),
        xticks=(np.arange(0, 185, 25)),
        yticks=(np.arange(0, 185, 25)),
    )

    one = [0, 180]
    sns.regplot(
        x=one,
        y=one,
        color="k",
        line_kws={"label": "1:1", "ls": ":", "lw": 1},
        scatter_kws={"s": 0},
        ax=axes[0],
        ci=None,
    )

    axes[1].set_xlim(xlim)

    # Recalc regression stats - uncorrected validation subset sensor vs reference method
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        val_y, val_X["val.no2.cnc_1_c1"]
    )
    # Plot it
    sns.regplot(
        x=val_y,
        y=val_X["val.no2.cnc_1_c1"],
        color="tab:orange",
        line_kws={
            "label": "y = {0:.2f}x+{1:.2f},  R-sqd = {3:.2f}".format(
                slope, intercept, r_value, r_value ** 2
            )
        },
        ax=axes[1],
        truncate=False,
    )
    axes[1].set(
        xlabel="Reference method NO2 (ppb)",
        ylabel="Sensor NO2 (ppb)",
        title="Uncorrected sensor vs Reference method\n (validation subset)",
        xlim=(-10, 180),
        ylim=(-10, 180),
        xticks=(np.arange(0, 185, 25)),
        yticks=(np.arange(0, 185, 25)),
    )

    one = [0, 180]
    sns.regplot(
        x=one,
        y=one,
        color="k",
        line_kws={"label": "1:1", "ls": ":", "lw": 1},
        scatter_kws={"s": 0},
        ax=axes[1],
        ci=None,
    )

    axes[2].set_xlim(xlim)

    # # Recalc regression stats - corrected validation subset sensor vs reference method
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        val_y, model_prediction
    )
    sns.regplot(
        x=val_y,
        y=model_prediction,
        color="tab:green",
        line_kws={
            "label": "y = {0:.2f}x+{1:.2f},  R-sqd = {3:.2f}".format(
                slope, intercept, r_value, r_value ** 2
            )
        },
        ax=axes[2],
        truncate=False,
    )
    axes[2].set(
        xlabel="Reference method NO2 (ppb)",
        ylabel="Corrected Sensor NO2 (ppb)",
        title="Corrected sensor vs Reference method\n (validation subset)",
        xlim=(-2, 50),
        ylim=(-2, 50),
        xticks=(np.arange(0, 55, 10)),
        yticks=(np.arange(0, 55, 10)),
    )

    one = [0, 50]
    sns.regplot(
        x=one,
        y=one,
        color="k",
        line_kws={"label": "1:1", "ls": ":", "lw": 1},
        scatter_kws={"s": 0},
        ax=axes[2],
        ci=None,
    )

    axes[0].legend(loc="upper center", fontsize=11)
    axes[1].legend(loc="upper center", fontsize=11)
    axes[2].legend(loc="upper center", fontsize=11)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    plt.subplots_adjust(wspace=0.3)

    if save_it == True:
        plt.savefig(
            f"training_storyboard_no2_mln{str(model.max_leaf_nodes)}_e{str(model.n_estimators)}_{png_descriptor}.png",
            dpi=300,
        )
    plt.show()
    return


# Function for plotting the verification results - split
# -------------------------------------------------------
def timeseries_plot_split(
    val_X, val_y, title, save_it, lower_pane_lims, upper_pane_lims, **kwargs
):
    # Model prediction
    # Set training & target variables
    #     val_X = df.drop(
    #         columns=['no2_ppb_s', 'pm25_ugg_s', 'no2_ppb_h', 'no2_ppb_combo']
    #     )
    #     val_y = df['no2_ppb_combo']

    model_prediction = model.predict(val_X)
    sns.set_style("white", {"axes.grid": False})
    myFmt = mdates.DateFormatter("%b")
    f, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 6))
    sns.lineplot(
        x=val_y.index.get_level_values(1),
        y=val_y.values,
        label="Reference method target",
        color="k",
        lw=4,
        zorder=2,
        ax=ax,
    )
    sns.lineplot(
        x=val_X.index.get_level_values(1),
        y=model_prediction,
        label="Corrected sensor",
        color="tab:green",
        zorder=3,
        ax=ax,
    )
    sns.lineplot(
        x=val_X.index.get_level_values(1),
        y=val_X["val.no2.cnc_1_c1"].values,
        label="Uncorrected sensor",
        color="tab:red",
        zorder=1,
        ax=ax,
    )
    sns.lineplot(
        x=val_y.index.get_level_values(1),
        y=val_y.values,
        color="k",
        lw=4,
        zorder=2,
        ax=ax2,
    )
    sns.lineplot(
        x=val_X.index.get_level_values(1),
        y=model_prediction,
        color="tab:green",
        zorder=3,
        ax=ax2,
    )
    sns.lineplot(
        x=val_X.index.get_level_values(1),
        y=val_X["val.no2.cnc_1_c1"].values,
        color="tab:red",
        zorder=1,
        ax=ax2,
    )
    # zoom-in / limit the view to different portions of the data
    ax.set_ylim(upper_pane_lims[0], upper_pane_lims[1])  # (100, 300)  # outliers only
    ax2.set_ylim(lower_pane_lims[0], lower_pane_lims[1])  # (-5, 30)  # most of the data

    # hide the spines between ax and ax2
    ax.spines["bottom"].set_visible(False)
    ax2.spines["top"].set_visible(False)
    ax.xaxis.set_ticks_position("none")
    ax2.yaxis.set_label_coords(-0.05, 1.1)
    ax.yaxis.label.set_visible(False)

    d = 0.007  # how big to make the diagonal lines in axes coordinates
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax.transAxes, color="k", clip_on=False, lw=0.75)
    ax.plot((-d, +d), (-d, +d), **kwargs)  # top-left diagonal
    ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal
    ax2.xaxis.set_major_formatter(myFmt)
    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
    ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

    # What's cool about this is that now if we vary the distance between
    # ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
    # the diagonal lines will move accordingly, and stay right at the tips
    # of the spines they are 'breaking'

    f.subplots_adjust(hspace=0.05)

    plt.ylabel("NO2 (ppb)", fontsize=11)
    ax.legend(loc="upper left", fontsize=11)
    ax.set_title(
        str(title), fontsize=14,
    )
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    if save_it is True:
        plt.savefig(
            f"split_validation_ts_no2_mln{model.max_leaf_nodes}_e{model.n_estimators}_str({png_descriptor}).png",
            dpi=300,
        )
    plt.show()


# Function for plotting the verification results - split
# -------------------------------------------------------
def timeseries_plot(val_X, val_y, title, save_it, **kwargs):
    # Model prediction
    # Set training & target variables
    #     val_X = df.drop(
    #         columns=['no2_ppb_s', 'pm25_ugg_s', 'no2_ppb_h', 'no2_ppb_combo']
    #     )
    #     val_y = df['no2_ppb_combo']

    model_prediction = model.predict(val_X)
    sns.set_style("white", {"axes.grid": False})
    myFmt = mdates.DateFormatter("%b")
    f, ax = plt.subplots(1, 1, sharex=True, figsize=(12, 6))
    sns.lineplot(
        x=val_y.index.get_level_values(1),
        y=val_y.values,
        label="Reference method target",
        color="k",
        lw=4,
        zorder=2,
        ax=ax,
    )
    sns.lineplot(
        x=val_X.index.get_level_values(1),
        y=model_prediction,
        label="Corrected sensor",
        color="tab:green",
        zorder=3,
        ax=ax,
    )
    sns.lineplot(
        x=val_X.index.get_level_values(1),
        y=val_X["val.no2.cnc_1_c1"].values,
        label="Uncorrected sensor",
        color="tab:red",
        zorder=1,
        ax=ax,
    )

    f.subplots_adjust(hspace=0.05)

    plt.ylabel("NO2 (ppb)", fontsize=11)
    ax.legend(loc="upper left", fontsize=11)
    ax.set_title(
        str(title), fontsize=14,
    )
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    if save_it is True:
        plt.savefig(
            f"validation_ts_no2_mln{model.max_leaf_nodes}_e{model.n_estimators}_str({png_descriptor}).png",
            dpi=300,
        )
    plt.show()
