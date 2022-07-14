# Oxaria sensor data processing repository
This repo hosts the exploratory data analysis code base of the OxAria (AQ) sensor project.

## Project info
Please see [oxaria.org.uk](https://www.oxaria.org.uk/) for further OxAria info.


# Table of contents

- [Oxaria sensor data processing repository](#oxaria-sensor-data-processing-repository)
  - [Project info](#project-info)
- [Table of contents](#table-of-contents)
  - [Workflow](#workflow)
    - [Exceptions for Random forest modelling tasks](#exceptions-for-random-forest-modelling-tasks)
  - [Repository architecture](#repository-architecture)
  - [Air qualty Sensor types](#air-qualty-sensor-types)
- [Scripting &  Jupyter Notebook codebase](#scripting---jupyter-notebook-codebase)
  - [TASK 1a - 4-gas sensor data acquisition](#task-1a---4-gas-sensor-data-acquisition)
    - [Batch 1 January 2020 to February 2021.](#batch-1-january-2020-to-february-2021)
    - [Batch 2 June 2021 to October 2021.](#batch-2-june-2021-to-october-2021)
    - [Batch 3 January 2021 to May 2021.](#batch-3-january-2021-to-may-2021)
  - [TASK 1b - 1-gas sensor data acquisition](#task-1b---1-gas-sensor-data-acquisition)
    - [Batch 1 January 2020 to February 2021.](#batch-1-january-2020-to-february-2021-1)
    - [Batch 2 January 2021 to May 2021.](#batch-2-january-2021-to-may-2021)
    - [Batch 3 June 2021 to October 2021.](#batch-3-june-2021-to-october-2021)
  - [TASK 1c - Loading CSVs to Pandas for data analysis](#task-1c---loading-csvs-to-pandas-for-data-analysis)
    - [Loading 4-gas sensor data](#loading-4-gas-sensor-data)
    - [Loading 1-gas sensor data](#loading-1-gas-sensor-data)
  - [TASK 2 - Visualising raw datasets](#task-2---visualising-raw-datasets)
  - [TASK 3 - Screening out unstable periods in sensor time series](#task-3---screening-out-unstable-periods-in-sensor-time-series)
  - [TASK 4 - Compiling reference obervations](#task-4---compiling-reference-obervations)
  - [TASK 5 - Aggregating data to 15-minutes averages](#task-5---aggregating-data-to-15-minutes-averages)
  - [TASK 6](#task-6)
  - [TASK 7 - Preparing training datasets](#task-7---preparing-training-datasets)
  - [TASK 8](#task-8)
  - [TASK 9 - Empirical filters & sensor baselining](#task-9---empirical-filters--sensor-baselining)
  - [ML model development & training for correction environmental interference](#ml-model-development--training-for-correction-environmental-interference)
  - [TASK 10 - Model deployment](#task-10---model-deployment)
  - [TASK 11 - Model correction visualisation](#task-11---model-correction-visualisation)
- [Random forest regression methods for environmental interference correction](#random-forest-regression-methods-for-environmental-interference-correction)
  - [Methods paper Random Forest Regression modelling](#methods-paper-random-forest-regression-modelling)
    - [NO2](#no2)
    - [PM10](#pm10)
    - [PM2.5](#pm25)
  - [Sensor lockdown paper Random Forest Regression modelling](#sensor-lockdown-paper-random-forest-regression-modelling)
    - [PM10](#pm10-1)
    - [PM2.5](#pm25-1)

## Workflow
The code base below is organised as a series of Python scripts (for tasks that don't require any user input / expert judgement ) & Jupyter Notebooks for components that require decision making or iterative working. The sequential workflow is indicated by the numeric prefix to file names.

e.g. `1_*`, `2_*` etc. (some possible exceptions may exist).

Where intermediate steps are found to be needed retrospectively, the workflow numeric prefix has been extended with an alpha character.

e.g. `1a_*`, `1b_*`, `2_*` etc.

### Exceptions for Random forest modelling tasks
An exception to this workflow structure is made for the random forest model training & developement tasks. These are presented seperately in the repo below $$$.

## Repository architecture
- `Py & ipynb` files are stored in the `./src` folder
- An external link to raw & processed data files on the University of Oxford Research Data Archive can be found in the `./data` folder
- Fle formats used for outputs include `csv, feather dorat diles (ftr), python pickle files (pkl) & pngs`

<pre>
oxaria/
├─ data/
├─ src/
│  ├─ rf_models/
|     ├─ methods_paper/
|     ├─ lockdown_paper/
│  ├─ batch_1_jan20_feb21/
│  ├─ batch_2_feb21_may21/
│  ├─ batch_3_jun21_oct21/
├─ outputs/
README.md
requirements.txt
.gitignore
</pre>

## Air qualty Sensor types
Two variants of the South Coast Science Praxis Urban sensor systems were dployed in the project.

- A 4-gas (no2, no, o3 & co) + PM (PM10, PM2.5 & PM1) sensor system purchased by the University of Birmingham, 8 sensors total
- A 1-gas (no2 only) + PM (PM10, PM2.5 & PM1) sensor system purchased by UoO, 8 sensors total
- 1 spare of each variant was kept in an operational state to cover instrument failure

The initial stages of the data processing workflow handle data from the 2 sensor systems separately - each vatriant has different pollutant 'channels' included in their data feed. The data handling components for each variant are denoted in folder & file name nomenclature e.g. `*oxaria1*` & `*oxaria2*` in the folder/filename, relating to 4-gas & 1-gas sensor processing activities respectively.

4-gas sensors are owned by the University of Birmingham & grouped under the `oxaria1` file label / folders - they were the 1st batch of sensors purchased for use by OxAria & via NERC funding.

# Scripting &  Jupyter Notebook codebase

The Praxis sensor systems push data via MQTT over a 4G network to the South Coast Science AWS cloud. Data were download from this resource perodically. For the period covered by this repo, (2020-2021), data were downloaded in 3 tranches;

**Batch 1.** January 2020 to February 2021.\
**Batch 2.** January 2021 to May 2021.\
**Batch 3.**  June 2021 to October 2021.

Downloads were handled separately for 1 and 4-gas sensors described in sections 1a & 1b below.

## TASK 1a - 4-gas sensor data acquisition
The `.py` scripts below download data from the 4-gas sensor variant from the AWS cloud to local Json files. The Json is then converted to a CSV format.

Mods to these scripts will be needed to update datasets for revisions to the data on the SCS cloud & to add more recent data. To add to the datasets with recent data copy &  modifying code in `./June 2021 to October 2021`. These are most up to date with SCS topic content.

`Note.` The SCS MQTT topic scope can change when SCS change / add new variables, parameters or attenuated pollutant variables to the feeds.

### Batch 1 January 2020 to February 2021.
| Code | Description |
|:-----|:------------|
|  [1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_status_json.py) | Downloads data for the status topic - GPS location, up-time info etc.|
[1_pull_pm_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_pm_json.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.|
[1_pull_gases_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_gases_json.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.|
[1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_status_json.py)| Downloads data for the status topic - GPS location, up-time info etc.|
[1_pull_climate_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_climate_json.py)| Downloads data for the climate topic - temperature, RH data etc.|
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.|

### Batch 2 June 2021 to October 2021.
| Code | Description |
|:-----|:------------|
[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_pm_json_2021.py)|bDownloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_gases_json_2021.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.

### Batch 3 January 2021 to May 2021.
| Code | Description |
|:-----|:------------|
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_gases_json_2021.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_pm_json_2021.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.

## TASK 1b - 1-gas sensor data acquisition
The `.py` scripts below download data from the 4-gas sensor variant from the AWS cloud to local Json files. The Json is then converted to a CSV format.

Mods to these scripts will be needed to update datasets for revisions to the data on the SCS cloud & to add more recent data. To add to the datasets with recent data copy &  modifying code in `./June 2021 to October 2021`. These are most up to date with SCS topic content.

`Note.` The SCS MQTT topic scope can change when SCS change / add new variables, parameters or attenuated pollutant variables to the feeds.

### Batch 1 January 2020 to February 2021.
| Code | Description |
|:-----|:------------|
[1_pull_status_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_status_json_2.py) | Downloads data for the status topic - GPS location, up-time info etc.|
[1_pull_pm_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_pm_json_2.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.|
[1_pull_gases_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_gases_json_2.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.|
[1_pull_climate_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_pull_climate_json_2.py)| Downloads data for the climate topic - temperature, RH data etc.|
[2_json_to_csv_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/2_json_to_csv_2.py)| Converts the json based files created by the above to CSV format.|

### Batch 2 January 2021 to May 2021.
| Code | Description |
|:-----|:------------|
[1_pull_climate_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_climate_json_2021_2.py)| Downloads data for the climate topic - temperature, RH data etc.
[1_pull_gases_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_gases_json_2021_2.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_pm_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_pm_json_2021_2.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_status_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_pull_status_json_2021_2.py)| Downloads data for the status topic - GPS location, up-time info etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.

### Batch 3 June 2021 to October 2021.
| Code | Description |
|:-----|:------------|
|[1_pull_status_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_status_json_2021_2.py)| Downloads data for the status topic - GPS location, up-time info etc.
[1_pull_pm_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_pm_json_2021_2.py)|bDownloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_gases_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_gases_json_2021_2.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_climate_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_pull_climate_json_2021_2.py)| Downloads data for the climate topic - temperature, RH data etc.
[2_json_to_csv_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_json_to_csv_2.py)| Converts the json based files created by the above to CSV format.

## TASK 1c - Loading CSVs to Pandas for data analysis
The notebooks below;

1. Load the raw CSV datasets from above (1a & b) to to a dataframe (Pandas)
2. Removing duplicate records by sensor & observation timestamp
3. Re-index
4. Add common sensor names (TODO review sensor naming, it currently gets redone in downstream data vis tasks, but of a pain)
5. Save to a binary format `Feather` for fast loading & saving

### Loading 4-gas sensor data
- Batch 1 January 2020 to February 2021

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_climate_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria1_climate_gf.py)| Loading climate topic data (T, RH etc.) , 4-gas|
| [1_load_oxaria1_gases_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria1_gases_gf.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_pm_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria1_pm_gf.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria1_status_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria1_status_gf.py)| Loading status topic data (location, signal strength etc.), 4-gas|

- Batch 2 Data January 2021 to May 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_gases_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_load_oxaria1_gases_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_load_oxaria1_pm_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_load_oxaria1_status_climate_v1.py)| Loading climate & status topic data (T, RH + location, signal strength etc.) , 4-gas|

-  Batch 3 Data June 2021 to October 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_gases_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_load_oxaria1_gases_v1.py)| Loading climate topic data (T, RH etc.) , 4-gas|
| [1_load_oxaria1_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_load_oxaria1_pm_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_load_oxaria1_pm_v1.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria1_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_load_oxaria1_status_climate_v1.py)| Loading status topic data (location, signal strength etc.), 4-gas|

### Loading 1-gas sensor data
- Batch 1 Data January 2020 to February 2021

| Code | Description |
|:-----|:------------|
| [1_load_oxaria2_climate_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria2_climate_gf.py)| Loading climate topic data (T, RH etc.) , 4-gas|
| [1_load_oxaria2_gases_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria2_gases_gf.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_pm_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria2_pm_gf.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria2_status_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_1_jan20_feb21/1_load_oxaria2_status_gf.py)| Loading status topic data (location, signal strength etc.), 4-gas|

- Batch 2 Data January 2021 to May 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria2_gases_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_load_oxaria2_gases_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_load_oxaria2_pm_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/1_load_oxaria2_status_climate_v1.py)| Loading climate & status topic data (T, RH + location, signal strength etc.) , 4-gas|

-  Batch 3 Data June 2021 to October 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_load_oxaria2_gases_gf.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_load_oxaria2_pm_gf.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria2_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/1_load_oxaria2_status_climate_v1.py)| Loading status topic data (location, signal strength etc.), 4-gas|

## TASK 2 - Visualising raw datasets
Notebooks to display & visualise raw sensor data in exploratory data analysis e.g. to indentify periods of instability / discontinuity for task 3.

Mods needed here if datasets updated & evidence of instability / discontinuity exists.

| Batch 1 January 2020 to February 2021 | Batch 2 January 2021 to May 2021 | Batch 3 June 2021 to October 2021 |
|:----------------------------|:------------------------|:-------------------------|
| No record of first look file for climate topic. | [2_first_look_oxaria1_raw_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_first_look_oxaria1_raw_climate_v1.ipynb) |  No record of first look file for climate topic. |
[2_first_look_oxaria1_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria1_raw_gases_v1.ipynb) | [2_first_look_oxaria1_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_first_look_oxaria1_raw_gases_v1.ipynb) | [2_first_look_oxaria1_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_first_look_oxaria1_raw_gases_v1.ipynb) |
[2_first_look_oxaria1_raw_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria1_raw_pm_v1.ipynb) | [2_first_look_oxaria1_raw_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_first_look_oxaria1_raw_pm_v1.ipynb) | [2_first_look_oxaria1_raw_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_first_look_oxaria1_raw_pm_v1.ipynb) |
[2_first_look_oxaria1_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria1_raw_status_v1.ipynb) | [2_first_look_oxaria1_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_first_look_oxaria1_raw_status_v1.ipynb) | [2_first_look_oxaria1_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_first_look_oxaria1_raw_status_v1.ipynb) |
[2_first_look_oxaria2_pm_data_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria2_pm_data_v1.ipynb) | [2_first_look_oxaria2_raw_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_first_look_oxaria2_raw_climate_v1.ipynb) | [2_first_look_oxaria2 raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_first_look_oxaria2_raw_gases_v1.ipynb) |
[2_first_look_oxaria2_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria2_raw_gases_v1.ipynb) | [2_first_look_oxaria2_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_first_look_oxaria2_raw_gases_v1.ipynb) | [2_first_look_oxaria2_pm_data_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_first_look_oxaria2_pm_data_v1.ipynb) |
[2_first_look_oxaria2_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria2_raw_status_v1.ipynb) | [2_first_look_oxaria2_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/2_first_look_oxaria2_raw_status_v1.ipynb) | [2_first_look_oxaria2_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/2_first_look_oxaria2_raw_status_v1.ipynb) |

## TASK 3 - Screening out unstable periods in sensor time series
Notebooks to display & visualise raw sensor data in exploratory data analysis e.g. to indentify periods of instability / discontinuity for task 3.

Mods needed here if datasets updated & evidence of instability / discontinuity exists.

| Batch 1 January 2020 to February 2021 | Batch 2 January 2021 to May 2021 | Batch 3 June 2021 to October 2021 |
|:-----------------------------|:------------------------|:-------------------------|
| [3_stable_oxaria1_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_climate_v1.ipynb) | [3_stable_oxaria1_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria1_climate_v1.ipynb) | [3_stable_oxaria1_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria1_climate_v1.ipynb) |
| [3_stable_oxaria1_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_gases_v1.ipynb) | [3_stable_oxaria1_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria1_gases_v1.ipynb) | [3_stable_oxaria1_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria1_gases_v1.ipynb) |
| [3_stable_oxaria1_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_pm_v1.ipynb) | [3_stable_oxaria1_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria1_pm_v1.ipynb) | [3_stable_oxaria1_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria1_pm_v1.ipynb) |
| [3_stable_oxaria1_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_status_v1.ipynb) | [3_stable_oxaria1_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria1_status_v1.ipynb) | [3_stable_oxaria1_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria1_status_v1.ipynb) |
| [3_stable_oxaria2_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_climate_v1.ipynb) | [3_stable_oxaria2_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria2_climate_v1.ipynb) | [3_stable_oxaria2_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria2_climate_v1.ipynb) |
| [3_stable_oxaria2_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_gases_v1.ipynb) | [3_stable_oxaria2_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria2_gases_v1.ipynb) | [3_stable_oxaria2_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria2_gases_v1.ipynb) |
| [3_stable_oxaria2_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_pm_v1.ipynb) | [3_stable_oxaria2_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria2_pm_v1.ipynb) | [3_stable_oxaria2_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria2_pm_v1.ipynb) |
| [3_stable_oxaria2_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_status_v1.ipynb) | [3_stable_oxaria2_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/3_stable_oxaria2_status_v1.ipynb) | [3_stable_oxaria2_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/3_stable_oxaria2_status_v1.ipynb) |

## TASK 4 - Compiling reference obervations
The notebooks below used compile reference measurements from 2 Oxford monitoring stations with reference methods & logging 15-minute averages. Not the 15-minute data are available by special arrangement with operators.

Mods / updates needed here if the sensor data need uodating, need to keep reference dataset up to date for the co-located sensor location - High St & St Ebbes.

| <!-- --> | <!-- --> |
|---|---|
| Batch 1 January 2020 to February 2021 | [4_converging_sebbes_highst_v1_ratified.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/4_converging_sebbes_highst_v1_ratified.ipynb) |
| Batch 2 January 2021 to May 2021. | [b4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb) |
| Batch 3 June 2021 to October 2021. | [4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb)

| <!-- --> | <!-- --> |
|---|---|
| Batch 1 January 2020 to February 2021 | [4_converging_sebbes_highst_v1_ratified.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/4_converging_sebbes_highst_v1_ratified.ipynb) |
| Batch 2 January 2021 to May 2021 | [4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb) |
| Batch 3 June 2021 to October 2021 | [4_converging_sebbes_highst_and_auto_merged_jan2022.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/4_converging_sebbes_highst_and_auto_merged_jan2022.ipynb) |

## TASK 5 - Aggregating data to 15-minutes averages
Notebooks to aggregate 10-second sensor observations to 15-minutes averages for comparing with the reference observations. Prior to aggregation some calcs to bring out lag / hysteresis in T & RH interferences.

| PM |  |
|:---|---|
|  Batch 1 January 2020 to February 2021  | [5_resample_stable_dfs_max_gradients_testing.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/5_resample_stable_dfs_max_gradients_testing.ipynb)  |
|  Batch 2 January 2021 to May 2021  | [5_resample_stable_dfs_v2_with_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/5_resample_stable_dfs_v2_with_transients.ipynb)  |
|  Batch 3 June 2021 to October 2021  | [5_resample_stable_dfs_v2_with_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/5_resample_stable_dfs_v2_with_transients.ipynb)  |
| **NO2** |  |
| All time periods / batches | [5_resample_stable_dfs_v2_with_transients_no2.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/5_resample_stable_dfs_v2_with_transients_no2.ipynb) |

## TASK 6
Missing, no longer implemented.

## TASK 7 - Preparing training datasets
Notebook preparing sensor datasets for RF regressor training.

- Combines January 2020 to February 2021 + January 2021 to May 2021 sensor datasets
- Subsets the sensor dataset to High St & St Ebbes which are co-located with reference observations
- Extracts essential & useful info from all 4 topics,
- Joins reference measurement data on to the sensor data

| <!-- --> | <!-- --> |
|---|---|
| PM | [7_extract_modelling_datasets_v2_sept21_update_with_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_2_feb21_may21/7_extract_modelling_datasets_v2_sept21_update_with_transients.ipynb) |
| NO2 | [7_extract_modelling_datasets_v2_oct21_update_with_transients_no2.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/7_extract_modelling_datasets_v2_oct21_update_with_transients_no2.ipynb) |

## TASK 8
Missing, no longer implemented.

## TASK 9 - Empirical filters & sensor baselining
Notebook(s) applying empirical filters to clean up anomalies in sensor data. AIRPLS technique used for baselining -  to correct for baseline offset & baseline drift for each sensor.

| <!-- --> | <!-- --> |
|---|---|
| PM10 | [9.0_baseline_analysis_pm_v2_536_sept_update_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/9.0_baseline_analysis_pm_v2_536_sept_update_transients.ipynb) |
| PM2.5 | [9.0_baseline_analysis_pm_v2_536_sept_update_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/9.0_baseline_analysis_pm_v2_536_sept_update_transients.ipynb) ||
| NO2 | [9.0_baseline_analysis_no2_v2_536_sept_update_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/9.0_baseline_analysis_no2_v2_536_sept_update_transients.ipynb) |

## ML model development & training for correction environmental interference
See below [Random forest regression methods for environmental interference correction](#random-forest-regression-methods-for-environmental-interference-correction)

Model training sits here in the workflow but was developed separately, so just stitching in as a ref. Mods needs here to retrain the models on new updated / extebded sensor data.

Run the referenced code to apply corrections prior to Task 10.

## TASK 10 - Model deployment
Deployment of the RF models, including corrections for non-unitary gradients & non-zero intercept terms vs. hold-out validation set.

Mods needed here on update of raw data

| Description | Notebook |
|---|---|
| Deploy PM10 correction model | [10a_pm10_model_deployment_2020_SH_xt.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/10a_pm10_model_deployment_2020_SH_xt.ipynb)|
| Deploy PM2.5 correction model | [10b_pm25_model_deployment_2020_H_xt.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/10b_pm25_model_deployment_2020_H_xt.ipynb)|
| Deploy NO2 correction model | [10c_no2_model_deployment_2020_SH_xt_normalised.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/10c_no2_model_deployment_2020_SH_xt_normalised.ipynb)|
| Compile & visualise corrected observations  | [10d_get_final_timeseries.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/10d_get_final_timeseries.ipynb)|

## TASK 11 - Model correction visualisation
Notebook for visualising model correction performance.

[11_corrected_15m_observations_fcor.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/batch_3_jun21_oct21/11_corrected_15m_observations_fcor.ipynb)


# Random forest regression methods for environmental interference correction
Machine learnng methods for handling & correction of environmental interferences acting upon NO2 & PM sensor readings are outlined below. These were developed & implemented for 2 periods;

1. **Jan - Dec 2020**, to support the "methods paper" which sets out a general approach for correction of sensor observations environmental interferences, including “baselining” and interference correction using random forest regression methods for low-cost sensing of NO2, PM10 (particulate matter) and PM2.5.

    see https://amt.copernicus.org/articles/15/3261/2022/amt-15-3261-2022-discussion.html.

2. **Jan 2020 - Oct 2021**, to support the preparaton of a 2nd paper evaluating changes in PM (PM10 and PM2.5) concentrations for successive phases of COVID-19 restrictions using a low-cost sensor network in Oxford, UK (paper in preparation).

## Methods paper Random Forest Regression modelling
This workflow item utilises the baselined datasets generated by TASK 9 to train RF models with sensor & co-located reference method obervations at 2 locations in Oxord (St Ebbes & High St).

### NO2
| Description | File  |
|:---|:---|
| RFR correction model training notebook - NO2  | [no2_sebbes_training_jun2nov_sebbes_methods_paper_final.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/no2_sebbes_training_jun2nov_sebbes_methods_paper_final.ipynb)  |
| Trained NO2 correction model as sklearn.ensemble.RandomForestRegressor object | [RFR_model_no2_mln3500_e100_sebbes_356_ratified_mar_final.sav](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/RFR_model_no2_mln3500_e100_sebbes_356_ratified_mar_final.sav) |
| Expanded uncertainty calculations NO2 RFR correction model | [1_values_for_cen_calc_RFR_model_no2_mln3500_val_no2_1_c2_sebbes_mar22_validation.xlsx](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/EquivalenceToolV3.1_values_for_cen_calc_RFR_model_no2_mln3500_val_no2_1_c2_sebbes_mar22_validation.xlsx)|

### PM10
| Description | File  |
|:---|:---|
| RFR correction model training notebook - PM10  | [pm10_sebbes_training_jun2nov_sebbes_methods_paper_final.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/pm10_sebbes_training_jun2nov_sebbes_methods_paper_final.ipynb)  |
| Trained PM10 correction model as sklearn.ensemble.RandomForestRegressor object | [RFR_model_pm10_mln3000_sebbes_val_pm10_1_c2_mar_final.sav](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/RFR_model_pm10_mln3000_sebbes_val_pm10_1_c2_mar_final.sav) |
| Expanded uncertainty calculations PM10 RFR correction model | [1_values_for_cen_calc_RFR_model_pm10_mln3000_val_pm10_1_c2_sebbes_mar22_validation.xlsx](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/EquivalenceToolV3.1_values_for_cen_calc_RFR_model_pm10_mln3000_val_pm10_1_c2_sebbes_mar22_validation.xlsx)|

### PM2.5
| Description | File  |
|:---|:---|
| RFR correction model training notebook - PM2.5  | [pm25_sebbes_training_jun2nov_sebbes_methods_paper_final.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/pm25_sebbes_training_jun2nov_sebbes_methods_paper_final.ipynb)  |
| Trained PM2.5 correction model as sklearn.ensemble.RandomForestRegressor object | [RFR_model_pm25_mln3000_val_pm2p5_1_c2_mar_final.sav](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/RFR_model_pm25_mln3000_val_pm2p5_1_c2_mar_final.sav) |
| Expanded uncertainty calculations PM10 RFR correction model | [1_values_for_cen_calc_RFR_model_pm25_mln3000_val_pm25_1_c2_sebbes_mar22_validation.xlsx](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/EquivalenceToolV3.1_values_for_cen_calc_RFR_model_pm25_mln3000_val_pm25_1_c2_sebbes_mar22_validation.xlsx)|

## Sensor lockdown paper Random Forest Regression modelling
A similar model training exercise, this time using sensor & co-located reference method obervations at 2 locations in Oxford (St Ebbes & High St) for a longer period than that described above (Jan 2020-Oct 2021) & focusing exclusively on PM10 & PM2.5.
### PM10
| Description | File  |
|:---|:---|
| RFR correction model training notebook - PM10  | [RFR_model_pm10_mln6000_jun_aug_val_pm10_1_c2_SH_xt.ipynb][(https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/methods_paper/pm10_sebbes_training_jun2nov_sebbes_methods_paper_final.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/lockdown_paper/RFR_model_pm10_mln6000_jun_aug_val_pm10_1_c2_SH_xt.sav))  |
| Trained PM10 correction model as sklearn.ensemble.RandomForestRegressor object | [RFR_model_pm10_mln6000_jun_aug_val_pm10_1_c2_SH_xt.sav](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/lockdown_paper/RFR_model_pm10_mln6000_jun_aug_val_pm10_1_c2_SH_xt.sav) |
| Expanded uncertainty calculations PM10 RFR correction model | [1_values_for_cen_calc_RFR_model_pm10_mln6000_jun_aug_val_pm10_1_c2_SH_xt.xlsx](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/lockdown_paper/Equivalence%20Tool%20V3.1_values_for_cen_calc_RFR_model_pm10_mln6000_jun_aug_val_pm10_1_c2_SH_xt.xlsx)|

### PM2.5
| Description | File  |
|:---|:---|
| RFR correction model training notebook - PM2.5  | [pm25_sebbes_training_jun_aug_sebbes_xt.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/lockdown_paper/pm25_sebbes_training_jun_aug_sebbes_xt.ipynb)  |
| Trained PM2.5 correction model as sklearn.ensemble.RandomForestRegressor object | [RFR_model_pm25_mln4000_jun_aug_val_pm2p5_1_c2_S_xt.sav](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/lockdown_paper/RFR_model_pm25_mln4000_jun_aug_val_pm2p5_1_c2_S_xt.sav) |
| Expanded uncertainty calculations PM10 RFR correction model | [1_values_for_cen_calc_RFR_model_pm25_mln4000_jun_aug_val_pm2p5_1_c2_S_xt.xlsx](https://github.com/tonybushido/oxaria_code/blob/main/src/rf_models/lockdown_paper/Equivalence%20Tool%20V3.1_values_for_cen_calc_RFR_model_pm25_mln4000_jun_aug_val_pm2p5_1_c2_S_xt.xlsx)|
