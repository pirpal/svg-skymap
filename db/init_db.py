#!usr/bin/venv python3
# coding: utf8

"""
Create Sqlite3 tables
Meant to be used once or to recreate db in case of corrupted db
"""

import sqlite3
import csv
from requests import *
from db_constants import *

DB_PATH = "skymaps.db"

def createConnection(db_file: str):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print("> Error")

def createTable(conn, sql_request: str):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_request)
        conn.commit()
    except Error as e:
        print(e)

def initStars(conn):
    cursor = conn.cursor()
    with open(STARS_CSV_PATH, "r") as f:
        reader = csv.DictReader(f)
        to_db = []
        for line in reader:
            _hip = int(line["hip"]) if line["hip"] != "" else -1
            _hd = int(line["hd"]) if line["hd"] != "" else -1
            _hr = int(line["hr"]) if line["hr"] != "" else -1
            _rv = float(line["rv"]) if line["rv"] != "" else 0.0
            _ci = float(line["ci"]) if line["ci"] != "" else 0.0
            _flam = int(line["flam"]) if line["flam"] != "" else -1
            _comp = int(line["comp"]) if line["comp"] != "" else -1
            _comp_p = int(line["comp_primary"]) if line["comp_primary"] != "" else -1
            _var_min = float(line["var_min"]) if line["var_min"] != "" else 0.0
            _var_max = float(line["var_max"]) if line["var_max"] != "" else 0.0
            line_data = (
                int(line["id"]),
                _hip,
                _hd,
                _hr,
                str(line["gl"]),
                str(line["bf"]),
                str(line["proper"]),
                float(line["ra"]),
                float(line["dec"]),
                float(line["dist"]),
                float(line["pmra"]),
                float(line["pmdec"]),
                _rv,
                float(line["mag"]),
                float(line["absmag"]),
                str(line["spect"]),
                _ci,
                float(line["x"]),
                float(line["y"]),
                float(line["z"]),
                float(line["vx"]),
                float(line["vy"]),
                float(line["vz"]),
                float(line["rarad"]),
                float(line["decrad"]),
                float(line["pmrarad"]),
                float(line["pmdecrad"]),
                str(line["bayer"]),
                _flam,
                str(line["con"]),
                _comp,
                _comp_p,
                str(line["base"]),
                float(line["lum"]),
                str(line["var"]),
                _var_min,
                _var_max)
            to_db.append(line_data)
    cursor.executemany(sqlite3_init_stars, to_db)
    conn.commit()
        
def initDeepSkyObjects(conn):
    cursor = conn.cursor()
    with open(DSO_CSV_PATH, "r") as f:
        reader = csv.DictReader(f)
        to_db = []
        for line in reader:
            _mag = float(line["mag"]) if line["mag"] != "" else 0.0
            _r1 = float(line["r1"]) if line["r1"] != "" else 0.0
            _r2 = float(line["r2"]) if line["r2"] != "" else 0.0
            _angle = float(line["angle"]) if line["angle"] != "" else 0.0
            _dso_source = int(line["dso_source"]) if line["dso_source"] != "" else -1
            _display_mag = float(line["display_mag"]) if line["display_mag"] != "" else 0.0
            line_data = (
                int(line["id"]),
                float(line["ra"]),
                float(line["dec"]),
                str(line["const"]),
                _mag,
                str(line["name"]),
                float(line["rarad"]),
                float(line["decrad"]),
                _r1,
                _r2,
                _angle,
                _dso_source,
                str(line["id1"]),
                str(line["cat1"]),
                str(line["id2"]),
                str(line["cat2"]),
                str(line["dupid"]),
                str(line["dupcat"]),
                _display_mag
            )
            to_db.append(line_data)
    cursor.executemany(sqlite3_init_deepskyobjects, to_db)
    conn.commit()

def initCities(conn):
    cursor = conn.cursor()
    with open(CITIES_CSV_PATH, "r") as f:
        reader = csv.DictReader(f)
        to_db = []
        for line in reader:
            _population = int(float(line["population"])) if line["population"] != "" else -1
            line_data = (
                int(line["id"]),
                str(line["city"]),
                str(line["city_ascii"]),
                float(line["lat"]),
                float(line["lng"]),
                str(line["country"]),
                str(line["iso2"]),
                str(line["iso3"]),
                str(line["admin_name"]),
                _population
            )
            to_db.append(line_data)
    cursor.executemany(sqlite3_init_cities, to_db)
    conn.commit()
    
def main():
    conn = createConnection(DB_PATH)
    # print(f"> debug: conn = {conn}") 
    if conn is not None:
        print("Creating stars table..............", end="")
        createTable(conn, sqlite3_create_stars_table)
        print("done")
        print("Creating deep_sky_objects table...", end="")
        createTable(conn, sqlite3_create_deepskyobjects_table)
        print("done")
        print("Creating cities table.............", end="")
        createTable(conn, sqlite3_create_cities_table)
        print("done")
        print("Initializing stars................", end="")
        initStars(conn)
        print("done")
        print("Initializing deep sky objects.....", end="")
        initDeepSkyObjects(conn)
        print("done")
        print("Initializing cities................", end="")
        initCities(conn)
        print("done")
        print("\nDB correctly initiated")
        conn.close()
    else:
        print("Error: cannot connect to database")

# --------------------------------------------------------------------
if __name__ == "__main__":
    main()
