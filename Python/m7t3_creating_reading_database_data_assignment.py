"""
* Name         : m7t2_creating_reading_database_data_assignment.py
* Author       : Matt Staskal
* Created      : 02/20/25
* Module       : 7
* Topic        : 2
* Description  : Populate the database created in the previous assignment with data
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

import sqlite3
from sqlite3 import Error
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_connection(database):
    db_conn = None
    try:
        db_conn = sqlite3.connect(database)
        return db_conn
    except Error:
        print(Error)
    return db_conn

def execute_single(conn,statement):
    cur = conn.cursor()
    cur.execute(statement)
    conn.commit()

def execute_many(conn,statement,data):
    cur = conn.cursor()
    cur.executemany(statement,data)
    conn.commit()

weather_db = 'weather_tracking.db'
weatherdb_conn = create_connection(weather_db)
weatherdb_cur = weatherdb_conn.cursor()

#Code required to create tables if necessary, currently commented out
"""
location_table = """"""CREATE TABLE IF NOT EXISTS Location(
                        county text PRIMARY KEY,
                        state text);""""""
execute_single(weatherdb_conn,location_table)

precipitation_table = """"""CREATE TABLE IF NOT EXISTS Precipitation(
                            location text, 
                            date text,
                            precipitation real,
                            precip_type text,
                                FOREIGN KEY(location) REFERENCES Location(county)
                            );""""""
execute_single(weatherdb_conn,precipitation_table)
"""

#create data to enter into DB
ak_full = pd.read_csv("anchorage_ak_noaa_2024.csv")
ak_full_airport = ak_full[ak_full.STATION == 'USW00026451']
ak_snow = ak_full_airport[['NAME','DATE','SNOW']]
ak_snow_1 = ak_snow.rename(columns={'SNOW':'PRCP'})
ak_snow_1.insert(3,'TYPE','Snow')
ak_rain = ak_full_airport[['NAME','DATE','PRCP']]
ak_rain.insert(3,'TYPE','Rain')
ak_precip = pd.concat([ak_rain,ak_snow_1],ignore_index=True)
ak_precip.NAME = 'Anchorage'

ia_full = pd.read_csv("dsm_ia_noaa_2024.csv")
ia_full_airport = ia_full[ia_full.STATION == 'USW00014933']
ia_snow = ia_full_airport[['DATE','SNOW']]
ia_snow_1 = ia_snow.rename(columns={'SNOW':'PRCP'})
ia_snow_1.insert(2,'TYPE','Snow')
ia_snow_1.insert(0,'NAME','Polk')
ia_rain = ia_full_airport[['DATE','PRCP']]
ia_rain.insert(2,'TYPE','Rain')
ia_rain.insert(0,'NAME','Polk')
ia_precip = pd.concat([ia_rain,ia_snow_1],ignore_index=True)

ak_ia_precip = pd.concat([ak_precip,ia_precip],ignore_index=True)

#add data to DB
#the dataframe to enter into the DB doesn't have any unique column, so need to add primary key 'event_id' to Precipitation table
#SQLite doesn't allow adding a primary key to an existing table, so need to recreate table

drop_precip = "DROP TABLE IF EXISTS Precipitation"

create_precip = """CREATE TABLE IF NOT EXISTS Precipitation(
                            event_id PRIMARY KEY,
                            location text, 
                            date text,
                            precipitation real,
                            precip_type text,
                               FOREIGN KEY(location) REFERENCES Location(county)
                            );"""

execute_single(weatherdb_conn,drop_precip)
execute_single(weatherdb_conn,create_precip)

#add data to db
add_precip_data = "REPLACE INTO Precipitation (event_id, location, date, precipitation, precip_type) VALUES (?,?,?,?,?);"
to_precip_db = [(ak_ia_precip.index[i], ak_ia_precip.iloc[i,0], ak_ia_precip.iloc[i,1],ak_ia_precip.iloc[i,2],ak_ia_precip.iloc[i,3]) for i in range(len(ak_ia_precip))]
execute_many(weatherdb_conn,add_precip_data,to_precip_db)

add_location_data = "REPLACE INTO Location (county, state) VALUES (?,?);"
to_location_db = [('Anchorage','Alaska'),('Polk','Iowa')]
execute_many(weatherdb_conn,add_location_data,to_location_db)

#retrieve data and visualize
precipitation_df = pd.read_sql_query("SELECT * FROM Precipitation",weatherdb_conn)

ia_rain = precipitation_df[(precipitation_df.location == "Polk") & (precipitation_df.precip_type == "Rain")]
ia_rain_totals = ia_rain.precipitation.cumsum()
ia_rain_plot = list(ia_rain_totals)
ia_snow = precipitation_df[(precipitation_df.location == "Polk") & (precipitation_df.precip_type == "Snow")]
ia_snow_totals = ia_snow.precipitation.cumsum()
ia_snow_plot = list(ia_snow_totals)
ak_rain = precipitation_df[(precipitation_df.location == "Anchorage") & (precipitation_df.precip_type == "Rain")]
ak_rain_totals = ak_rain.precipitation.cumsum()
ak_rain_plot = list(ak_rain_totals)
ak_snow = precipitation_df[(precipitation_df.location == "Anchorage") & (precipitation_df.precip_type == "Snow")]
ak_snow_totals = ak_snow.precipitation.cumsum()
ak_snow_plot = list(ak_snow_totals)

dates = list(ia_rain.date)
date_labels = []
for i in range(0,len(dates),30):
    date_labels.append(dates[i])
fig,ax = plt.subplots(1,2)
ax[0].plot(dates,ia_rain_plot, color = 'black',label='Polk County, IA',ls='--',lw=.85)
ax[0].plot(dates,ak_rain_plot, color = 'blue',label='Anchorage County, AK',ls='--',lw=.85)
ax[0].set_xticks(date_labels)
ax[0].set_xticklabels(date_labels,rotation=45, fontsize=5)
ax[0].set_facecolor('whitesmoke')
ax[0].grid(axis='y',linestyle='--',lw=.5)
ax[0].set_title("Rain",fontsize=10)
ax[1].plot(dates,ia_snow_plot, color = 'black',label='Polk County, IA',lw=.85)
ax[1].plot(dates,ak_snow_plot, color = 'blue',label='Anchorage County, AK',lw=.85)
ax[1].set_xticks(date_labels)
ax[1].set_xticklabels(date_labels,rotation=45, fontsize=5)
ax[1].set_facecolor('whitesmoke')
ax[1].grid(axis='y',linestyle='--',lw=.5)
ax[1].set_title("Snow",fontsize=10)
fig.legend(fontsize='x-small')
fig.suptitle("2024 Cumulative Rain and Snow for Polk Co., IA and Anchorage Co., AK (in.)",fontsize=12)
plt.show()

weatherdb_conn.close()