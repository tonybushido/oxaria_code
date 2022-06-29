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

The initial stages of the data processing workflow handles data from these different systems differently - because of the different 'channels' included in each topic. Processing tasks were grouped into `*oxaria1*` & `*oxaria2*` in the filename, relating to 4-gas & 1-gas sensor processing activities respectively.

# Scripting &  Jupyter Notebook codebase
## Data download & initial transformation tasks
OxAria datasets were dowmloaded periodically from the South Coast Science AWS cloud. For the period covered by NIHR & NERC funded research project & this repo, (2020-2021), data were downloaded in 3 tranches;

1. January 2020 to February 2021.
2. January 2021 to May 2021.
3. June 2021 to October 2021.

Downloads were handled separately for 1 and 4-gas sensors described in section (0). The files below were used to pull data from the AWS cloud d to local Json files & then to convert Json  to CSV format.

## 4-gas sensors download code
The files below used to download data from the 4-gas sensor variant. These sensors are owned by the University of Birmingham. File nomenclature:  4-gas sensors are grouped under the `oxaria1` file label / handle, they were the 1st batch of sensors purchased for use by OxAria & via NERC funding.

### Data January 2020 to February 2021.
| Code | Description |
|:-----|:------------|
|  [1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/1oxaria/jan20_feb21/1_pull_status_json.py) | Downloads data for the status topic - GPS location, up-time info etc.|
|[1_pull_pm_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/1oxaria/jan20_feb21/1_pull_pm_json.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.|
|[1_pull_gases_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/1oxaria/jan20_feb21/1_pull_gases_json.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.|
|[1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/1oxaria/jan20_feb21/1_pull_status_json.py)| Downloads data for the status topic - GPS location, up-time info etc.|
|[1_pull_climate_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/1oxaria/jan20_feb21/1_pull_climate_json.py)| Downloads data for the climate topic - temperature, RH data etc.|
|[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/1oxaria/jan20_feb21/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.|

### Data January 2021 to May 2021.
| Code | Description |
|:-----|:------------|
|[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/jun_to_sept_2021/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
|[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/jun_to_sept_2021/1_pull_pm_json_2021.py)|bDownloads data for the particles topic - PM concentrations data, counts, flow rates etc.
|[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/jun_to_sept_2021/1_pull_gases_json_2021.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/jun_to_sept_2021/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/jun_to_sept_2021/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.

### !Data June 2021 to October 2021.
| Code | Description |
|:-----|:------------|
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/q12021/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/q12021/1_pull_gases_json_2021.p)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/q12021/1_pull_pm_json_2021.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/q12021/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/1oxaria/q12021/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.


## 1-gas sensors download
The files below used to download data from the 1-gas sensor variant. These sensors are owned by the University of Oxford. For file nomenclature, 1-gas sensors are grouped under the `oxaria2` file label / handle, they were the 2nd batch of sensors purchase for use by OxAria & are non-NERC funded (Research England(?)).
### Data January 2020 to February 2021.
| Code | Description |
|:-----|:------------|
[1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/2oxaria/jan20_feb21/1_pull_status_json.py) | Downloads data for the status topic - GPS location, up-time info etc.|
|[1_pull_pm_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/2oxaria/jan20_feb21/1_pull_pm_json.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.|
|[1_pull_gases_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/2oxaria/jan20_feb21/1_pull_gases_json.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.|
|[1_pull_status_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/2oxaria/jan20_feb21/1_pull_status_json.py)| Downloads data for the status topic - GPS location, up-time info etc.|
|[1_pull_climate_json.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/2oxaria/jan20_feb21/1_pull_climate_json.py)| Downloads data for the climate topic - temperature, RH data etc.|
|[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/blob/main/inputs/21oxaria/jan20_feb21/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.|
### Data January 2021 to May 2021.
| Code | Description |
|:-----|:------------|
|[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/jun_to_sept_2021/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
|[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/jun_to_sept_2021/1_pull_pm_json_2021.py)|bDownloads data for the particles topic - PM concentrations data, counts, flow rates etc.
|[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/jun_to_sept_2021/1_pull_gases_json_2021.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/jun_to_sept_2021/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/jun_to_sept_2021/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.
### !Data June 2021 to October 2021.
| Code | Description |
|:-----|:------------|
[1_pull_climate_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/q12021/1_pull_climate_json_2021.py)| Downloads data for the climate topic - temperature, RH data etc.
[1_pull_gases_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/q12021/1_pull_gases_json_2021.py)| Downloads data for the gases topic - gas concentrations data, voltages, N3 based T & RH etc.
[1_pull_pm_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/q12021/1_pull_pm_json_2021.py)| Downloads data for the particles topic - PM concentrations data, counts, flow rates etc.
[1_pull_status_json_2021.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/q12021/1_pull_status_json_2021.py)| Downloads data for the status topic - GPS location, up-time info etc.
[2_json_to_csv.py](https://github.com/tonybushido/oxaria_code/tree/main/inputs/2oxaria/q12021/2_json_to_csv.py)| Converts the json based files created by the above to CSV format.