### CREATING SQL DATABASE CONNECTION ####

###Importing library that allows POSTGRESQL####
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd 
import sqlite3
import os
import psycopg2

df = pd.read_csv('CDOT_Ski_Data_V3.csv')

###Engine = 'type of sql://username:password@host_name/database_name####
engine = create_engine('postgresql://steve:steve@localhost/ski_analysis')

### WRITING PANDAS DATAFRAME TO SQL####

## CONNECTING TO POSTGRESQL & DATABASE ##
con = engine.connect()

##DATAFRAME.TO_SQL('TABLE NAME OR VARIABLE CONTAINING TABLENAME', CONNECTION)
table_name = 'traffic_data'
df.to_sql(table_name,con, if_exists = 'replace')
#print(engine.table_names())
con.close()