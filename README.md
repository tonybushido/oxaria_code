# Oxaria sensor data processing repo
This repo hosts the exploratory data analysis code base of the OxAria (AQ) sensor project.

## Further project info
Please see [oxaria.org.uk](https://www.oxaria.org.uk/) for further OxAria info.

## Workflow
The code base is organised in a series of Python scripts for tasks that don't require any user input & Jupyter Notebooks for stuff that requires some decision making & iterative working. The workflow sequence is indicated by the numeric prefix to file names.

e.g. `1_*`, `2_*` etc. (some possible exceptions may exist).

Where intermediate are found to be needed retrospectively, the workflow numeric prefix has been extended with an alpha character.

e.g. `1a_*`, `1b_*`, `2_*` etc.

## Repo architecture
- `Py & ipynb` files are stored in the src folder
- Raw data files are stored in the inputs folder as `tar.gz` files
- Outputs datasets & intermediate files are stored in the outputs folder variably as `csv, ftr & png` serialisations

<pre>
oxaria/
├─ src/
├─ inputs/
│  ├─ csv/
│  ├─ json/
├─ outputs/
README.md
requirements.txt
.gitignore
</pre>

## Sensor types
Two variants of the South Coast Science Praxis Urban sensor systems were dployed in the project.

- A 4-gas (no2, no, o3 & co) + PM (PM10, PM2.5 & PM1) sensor system purchased by UoB, 8 sensors total
- A 1-gas (no2 only) + PM (PM10, PM2.5 & PM1) sensor system purchased by UoO, 8 sensors total

The initial stages of the data processing workflow handles data from these different systems differently - because of the different 'channels' included in each MQTT topic. Processing tasks were grouped into `*oxaria1*` & `*oxaria2*` in the filename, relating to 4-gas & 1-gas sensor processing activities respectively.

4-gas sensors are owned by the University of Birmingham & grouped under the `oxaria1` file label / folders - they were the 1st batch of sensors purchased for use by OxAria & via NERC funding.

# Scripting &  Jupyter Notebook codebase

OxAria datasets were dowmloaded periodically from the South Coast Science AWS cloud. For the period covered by NIHR & NERC funded research project & this repo, (2020-2021), data were downloaded in 3 tranches;

1. January 2020 to February 2021.
2. January 2021 to May 2021.
3. June 2021 to October 2021.

Downloads were handled separately for 1 and 4-gas sensors described in sections 1a & 1b below. 

# TASK 1a - 4-gas sensor data acquisition
The `.py` scripts below used to download data from the 4-gas sensor variant from the AWS cloud to local Json files & then to convert Json to CSV format.

## January 2020 to February 2021.
| Code | Description |
|:-----|:------------|
|  [1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_status_json.py) | Downloads data for the status topic - GPS location, up-time info etc.|
[1_pull_pm_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_pm_json.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.|
[1_pull_gases_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_gases_json.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.|
[1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_status_json.py)| Downloads data for the status topic - GPS location, up-time info etc.|
[1_pull_climate_json.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_climate_json.py)| Downloads data for the climate topic - temperature, RH data etc.|
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.|

## June 2021 to October 2021.
| Code | Description |
|:-----|:------------|
[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_pm_json_2021.py)|bDownloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_gases_json_2021.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.

## January 2021 to May 2021.
| Code | Description |
|:-----|:------------|
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_gases_json_2021.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_pm_json_2021.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.

# TASK 1b - 1-gas sensor data acquisition
The `py` files below used to download data from the 1-gas sensor variant. These sensors are owned by the University of Oxford & grouped under the `oxaria2` file label / folder - they were the 2nd batch of sensors purchased for use by OxAria & are non-NERC funded (Research England(?)).

## January 2020 to February 2021.
| Code | Description |
|:-----|:------------|
[1_pull_status_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_status_json_2.py) | Downloads data for the status topic - GPS location, up-time info etc.|
[1_pull_pm_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_pm_json_2.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.|
[1_pull_gases_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_gases_json_2.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.|
[1_pull_climate_json_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_pull_climate_json_2.py)| Downloads data for the climate topic - temperature, RH data etc.|
[2_json_to_csv_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/2_json_to_csv_2.py)| Converts the json based files created by the above to CSV format.|

## January 2021 to May 2021.
| Code | Description |
|:-----|:------------|
[1_pull_climate_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_climate_json_2021_2.py)| Downloads data for the climate topic - temperature, RH data etc.
[1_pull_gases_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_gases_json_2021_2.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_pm_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_pm_json_2021_2.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_status_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_pull_status_json_2021_2.py)| Downloads data for the status topic - GPS location, up-time info etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.

## June 2021 to October 2021.
| Code | Description |
|:-----|:------------|
|[1_pull_status_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_status_json_2021_2.py)| Downloads data for the status topic - GPS location, up-time info etc.
[1_pull_pm_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_pm_json_2021_2.py)|bDownloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_gases_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_gases_json_2021_2.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_climate_json_2021_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_pull_climate_json_2021_2.py)| Downloads data for the climate topic - temperature, RH data etc.
[2_json_to_csv_2.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_json_to_csv_2.py)| Converts the json based files created by the above to CSV format.

# TASK 1c - Loading CSVs to Pandas for data analysis
The notebooks below present the workflow for;

1. Loading the raw CSV datasets from above (1) to the Python based Pandas tabular data analysis framework https://pandas.pydata.org/docs/
2. Removing duplicate records by sesnor & observation timestamp
3. Re-indexing
4. Adding common sensor names
5. Saving the raw data to a binary *Feather* format, https://github.com/wesm/feather, which  provides a binary columnar serialization for Pandas data frames. It is designed to make reading and writing data frames efficient, and to make sharing data across data analysis languages easy.

## Loading 4-gas sensor data
- Data January 2020 to February 2021

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_climate_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria1_climate_gf.py)| Loading climate topic data (T, RH etc.) , 4-gas|
| [1_load_oxaria1_gases_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria1_gases_gf.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_pm_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria1_pm_gf.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria1_status_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria1_status_gf.py)| Loading status topic data (location, signal strength etc.), 4-gas|

- Data January 2021 to May 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_gases_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_load_oxaria1_gases_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_load_oxaria1_pm_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_load_oxaria1_status_climate_v1.py)| Loading climate & status topic data (T, RH + location, signal strength etc.) , 4-gas|

-  Data June 2021 to October 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_gases_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_load_oxaria1_gases_v1.py)| Loading climate topic data (T, RH etc.) , 4-gas|
| [1_load_oxaria1_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_load_oxaria1_pm_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria1_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_load_oxaria1_pm_v1.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria1_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_load_oxaria1_status_climate_v1.py)| Loading status topic data (location, signal strength etc.), 4-gas|

## Loading 1-gas sensor data
- Data January 2020 to February 2021

| Code | Description |
|:-----|:------------|
| [1_load_oxaria2_climate_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria2_climate_gf.py)| Loading climate topic data (T, RH etc.) , 4-gas|
| [1_load_oxaria2_gases_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria2_gases_gf.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_pm_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria2_pm_gf.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria2_status_gf.py](https://github.com/tonybushido/oxaria_code/blob/main/src/1_jan20_feb21/1_load_oxaria2_status_gf.py)| Loading status topic data (location, signal strength etc.), 4-gas|

- Data January 2021 to May 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria2_gases_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_load_oxaria2_gases_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_load_oxaria2_pm_v1.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/1_load_oxaria2_status_climate_v1.py)| Loading climate & status topic data (T, RH + location, signal strength etc.) , 4-gas|

-  Data June 2021 to October 2021.

| Code | Description |
|:-----|:------------|
| [1_load_oxaria1_pm_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_load_oxaria2_gases_gf.py)| Loading gases topic data (NO2, NO, O3, CO), 4-gas|
| [1_load_oxaria2_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_load_oxaria2_pm_gf.py)| Loading particles topic data (Nos, PM10,PM2.5, PM1), 4-gas|
| [1_load_oxaria2_status_climate_v1.py](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/1_load_oxaria2_status_climate_v1.py)| Loading status topic data (location, signal strength etc.), 4-gas|

# TASK 2 - Visualising raw datasets

The notebooks below used to display & visualise raw sensor data for exploratory data analysis.

| January 2020 to February 2021 | January 2021 to May 2021 | June 2021 to October 2021 |
|:-----------------------------:|:------------------------:|:-------------------------:|
| No record of first look file for climate topic. | [2_first_look_oxaria1_raw_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_first_look_oxaria1_raw_climate_v1.ipynb) |  No record of first look file for climate topic. |
[2_first_look_oxaria1_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria1_raw_gases_v1.ipynb) | [2_first_look_oxaria1_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_first_look_oxaria1_raw_gases_v1.ipynb) | [2_first_look_oxaria1_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_first_look_oxaria1_raw_gases_v1.ipynb) |
[2_first_look_oxaria1_raw_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria1_raw_pm_v1.ipynb) | [2_first_look_oxaria1_raw_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_first_look_oxaria1_raw_pm_v1.ipynb) | [2_first_look_oxaria1_raw_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_first_look_oxaria1_raw_pm_v1.ipynb) |
[2_first_look_oxaria1_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria1_raw_status_v1.ipynb) | [2_first_look_oxaria1_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_first_look_oxaria1_raw_status_v1.ipynb) | [2_first_look_oxaria1_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_first_look_oxaria1_raw_status_v1.ipynb) |
[2_first_look_oxaria2_pm_data_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria2_pm_data_v1.ipynb) | [2_first_look_oxaria2_raw_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_first_look_oxaria2_raw_climate_v1.ipynb) | [2_first_look_oxaria2 raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_first_look_oxaria2_raw_gases_v1.ipynb) |
[2_first_look_oxaria2_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria2_raw_gases_v1.ipynb) | [2_first_look_oxaria2_raw_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_first_look_oxaria2_raw_gases_v1.ipynb) | [2_first_look_oxaria2_pm_data_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_first_look_oxaria2_pm_data_v1.ipynb) |
[2_first_look_oxaria2_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/2_first_look_oxaria2_raw_status_v1.ipynb) | [2_first_look_oxaria2_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/2_first_look_oxaria2_raw_status_v1.ipynb) | [2_first_look_oxaria2_raw_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/2_first_look_oxaria2_raw_status_v1.ipynb) |

# TASK 3 - Screening out unstable periods in sensor time series
The notebooks below used to screen out parts of respective time series where there is clear evidnce of instability / discontinuity.

| January 2020 to February 2021. | January 2021 to May 2021 | June 2021 to October 2021 |
|---|---|---|
| [3_stable_oxaria1_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_climate_v1.ipynb) | [3_stable_oxaria1_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria1_climate_v1.ipynb) | [3_stable_oxaria1_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria1_climate_v1.ipynb) |
| [3_stable_oxaria1_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_gases_v1.ipynb) | [3_stable_oxaria1_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria1_gases_v1.ipynb) | [3_stable_oxaria1_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria1_gases_v1.ipynb) |
| [3_stable_oxaria1_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_pm_v1.ipynb) | [3_stable_oxaria1_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria1_pm_v1.ipynb) | [3_stable_oxaria1_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria1_pm_v1.ipynb) |
| [3_stable_oxaria1_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria1_status_v1.ipynb) | [3_stable_oxaria1_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria1_status_v1.ipynb) | [3_stable_oxaria1_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria1_status_v1.ipynb) |
| [3_stable_oxaria2_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_climate_v1.ipynb) | [3_stable_oxaria2_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria2_climate_v1.ipynb) | [3_stable_oxaria2_climate_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria2_climate_v1.ipynb) |
| [3_stable_oxaria2_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_gases_v1.ipynb) | [3_stable_oxaria2_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria2_gases_v1.ipynb) | [3_stable_oxaria2_gases_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria2_gases_v1.ipynb) |
| [3_stable_oxaria2_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_pm_v1.ipynb) | [3_stable_oxaria2_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria2_pm_v1.ipynb) | [3_stable_oxaria2_pm_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria2_pm_v1.ipynb) |
| [3_stable_oxaria2_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/3_stable_oxaria2_status_v1.ipynb) | [3_stable_oxaria2_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/3_stable_oxaria2_status_v1.ipynb) | [3_stable_oxaria2_status_v1.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/3_stable_oxaria2_status_v1.ipynb) |

# TASK 4 - Compiling reference obervations
The notebooks below used compile reference measurements from reference methods installed in Oxford 15-minute averages. Not the 15-minute data are available by special arrangement with operators.

| <!-- --> | <!-- --> |
|---|---|
| January 2020 to February 2021 | [4_converging_sebbes_highst_v1_ratified.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/4_converging_sebbes_highst_v1_ratified.ipynb) |
| January 2021 to May 2021. | [b4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb) |
| June 2021 to October 2021. | [4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb)

| <!-- --> | <!-- --> |
|---|---|
| January 2020 to February 2021 | [4_converging_sebbes_highst_v1_ratified.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/4_converging_sebbes_highst_v1_ratified.ipynb) |
| January 2021 to May 2021 | [4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/4_converging_sebbes_highst_and_auto_merged_sept2021.ipynb) |
| June 2021 to October 2021 | [4_converging_sebbes_highst_and_auto_merged_jan2022.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/4_converging_sebbes_highst_and_auto_merged_jan2022.ipynb) |

# TASK 5 - Aggregating data to 15-minutes averages
These notebooks aggregate 10-second sensor observations to 15-minutes averages for comparing with the reference observations above.

| <!-- --> | <!-- --> |
|---|---|
| January 2020 to February 2021 | [5_resample_stable_dfs_max_gradients_testing.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/1_2020/5_resample_stable_dfs_max_gradients_testing.ipynb) |
| January 2021 to May 2021 | [5_resample_stable_dfs_v2_with_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/5_resample_stable_dfs_v2_with_transients.ipynb) |
| June 2021 to October 2021 | [5_resample_stable_dfs_v2_with_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/3_oct2021/5_resample_stable_dfs_v2_with_transients.ipynb) |

# TASK 6
Missing, no longer implemented.

# TASK 7 - Preparing training datasets
This notebook prepares sensor datasets for RF regressor training. 

- Combines January 2020 to February 2021 + January 2021 to May 2021 sensor datasets
- Subsets the sensor dataset to High St & St Ebbes which are co-located with reference observations
- Extracts essential & useful info from all 4 topics, 
- Joins reference measurement data on to the sensor data 

[7_extract_modelling_datasets_v2_sept21_update_with_transients.ipynb](https://github.com/tonybushido/oxaria_code/blob/main/src/2_q12021/7_extract_modelling_datasets_v2_sept21_update_with_transients.ipynb)

# TASK 8
Missing, no longer implemented.

# TASK 9 - Empirical filters & sensor baselining 

Notebook applying empirical filters to clean up gross anomalies in sensor data, then applies AIRPLS to correct for baseline offset & drift.


