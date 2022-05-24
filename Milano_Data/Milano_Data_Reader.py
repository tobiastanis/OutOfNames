"""
This file imports the data of LUMIO and the Moon over an epoch of Modified Julian Time 59091.50000 to 61325.00000,
meaning from date 2020-08-30 12:00:00.000 to 2026-10-12 00:00:00.000.

Two important times at which the initial state of LUMIO are considered are at 21-03-2024 and 18-04-2024, since no
stationkeeping is performed from then to a certain amount of days

See below for function description (from line 46)
"""
import numpy as np
from pathlib import Path
import pandas as pd
import csv
print("Reading Milano data")
# Opening csv datasets
LUMIO_datacsv = open(Path.joinpath(Path(__file__).parent, 'LUMIO_states.csv'))
Moon_datacsv = open(Path.joinpath(Path(__file__).parent, 'Moon_states.csv'))

# Reading
csvreader_LUMIO = csv.reader(LUMIO_datacsv)
csvreader_Moon = csv.reader(Moon_datacsv)

# Extruding
header_LUMIO = next(csvreader_LUMIO)
header_Moon = next(csvreader_Moon)
rows_LUMIO = []
rows_Moon = []
for row in csvreader_LUMIO:
    rows_LUMIO.append(row)
for row in csvreader_Moon:
    rows_Moon.append(row)
data_LUMIO = np.array(rows_LUMIO).astype(float)
data_Moon = np.array(rows_Moon).astype(float)

t0_data_mjd = data_Moon[0, 0]
tend_data_mjd = data_Moon[(len(data_Moon) - 1), 0]

LUMIO_dataframe = pd.DataFrame(
    {'MJD': data_LUMIO[:, 0], 'ET': data_LUMIO[:, 1], 'x': data_LUMIO[:, 2], 'y': data_LUMIO[:, 3],
     'z': data_LUMIO[:, 4], 'vx': data_LUMIO[:, 5], 'vy': data_LUMIO[:, 6], 'vz': data_LUMIO[:, 7]})
Moon_dataframe = pd.DataFrame(
    {'MJD': data_Moon[:, 0], 'ET': data_Moon[:, 1], 'x': data_Moon[:, 2], 'y': data_Moon[:, 3],
     'z': data_Moon[:, 4], 'vx': data_Moon[:, 5], 'vy': data_Moon[:, 6], 'vz': data_Moon[:, 7]})
"""
Output are two dataframes, which are used obtain initial states and states over an epoch, which are determined by Milano
. The states provided by Milano contain SKM
"""
# Closing csv files
LUMIO_datacsv.close()
Moon_datacsv.close()
print('Finished reading data')