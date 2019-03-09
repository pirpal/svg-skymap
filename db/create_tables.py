#!usr/bin/venv python3
# coding: utf8

"""
Create Sqlite3 tables
Meant to be used once or to recreate db in case of corrupted db
"""

import sqlite3
from requests import *

def create_connection(db_file: str):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print("> Error")
        
def create_table(conn, sql_request: str):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_request)
        conn.commit()
    except Error as e:
        print(e)

def main():
    conn = create_connection("skymaps.db")
    # print(f"> debug: conn = {conn}") 
    if conn is not None:
        
        create_table(conn, sqlite3_create_stars_table)
        print("stars table created.")
        create_table(conn, sqlite3_create_deepskyobjects_table)
        print("deep_sky_objects table created.")
        create_table(conn, sqlite3_create_cities_table)
        print("cities table created.")
        conn.close()
    else:
        print("Error: cannot connect to database")

# --------------------------------------------------------------------
if __name__ == "__main__":
    main()
