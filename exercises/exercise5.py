import urllib.request
import os
import pandas as pd
import sqlite3
from zipfile import ZipFile

# Step 1: Download the GTFS ZIP file from the specified URL
url = 'https://gtfs.rhoenenergie-bus.de/GTFS.zip'
file_path = 'data/GTFS.zip'
urllib.request.urlretrieve(url, file_path)

# Step 2: Extract and read the 'stops.txt' file from the downloaded ZIP archive
with ZipFile(file_path, 'r') as zip_ref:
    with zip_ref.open('stops.txt') as stops_file:
        # Step 3: Read the file into a pandas DataFrame
        stops_df = pd.read_csv(stops_file)

# Step 4: Filter data for zone 2001 and select required columns
selected_columns = ['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id']
data_frame = stops_df[stops_df['zone_id'] == 2001][selected_columns]

# Step 5: Validate latitude and longitude within valid ranges
data_frame = data_frame[(data_frame['stop_lat'].between(-90, 90)) & (data_frame['stop_lon'].between(-90, 90))]

# Step 6: Remove rows with missing or invalid data
data_frame.dropna(inplace=True)

# Step 7: Set the path for the SQLite database
db_path = 'gtfs.sqlite'

# Step 8: Create and connect to the SQLite database
conn = sqlite3.connect(db_path)

# Step 9: Write the data into the 'stops' table in the SQLite database
data_frame.to_sql('stops', conn, if_exists='replace', index=False, dtype={
    'stop_id': 'INTEGER',
    'stop_name': 'TEXT',
    'stop_lat': 'REAL',
    'stop_lon': 'REAL',
    'zone_id': 'INTEGER'
})

# Step 10: Close the database connection
conn.close()

# Step 11: Delete the downloaded ZIP file to clean up
os.remove(file_path)
