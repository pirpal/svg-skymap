#!usr/bin/venv python3
# coding: utf8

"""
Create Sqlite3 tables
Meant to be used once or to recreate db in case of corrupted db
"""

import sqlite3

def create_connection(db_file: str):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
def create_table(conn, sql_request: str):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_request)
    except Error as e:
        print(e)

def main():
    db = "~/Python/svg-skymap/db/SKYMAPS_TEST_DB_01"
    sql_create_stars_table = """
    CREATE TABLE IF NOT EXISTS stars(
    id INTEGER PRIMARY KEY UNIQUE,
    hip INTEGER NOT NULL,
    hd INTEGER NOT NULL,
    hr INTEGER NOT NULL,
    gl INTEGER NOT NULL,
    bf TEXT,
    proper TEXT,
    ra REAL NOT NULL,
    dec REAL NOT NULL,
    dist REAL NOT NULL,
    pmra REAL NOT NULL,
    pmdec REAL NOT NULL,
    rv REAL,
    mag REAL NOT NULL,
    absmag REAL NOT NULL,
    spect TEXT,
    ci REAL,
    x REAL NOT NULL,
    y REAL NOT NULL,
    z REAL NOT NULL,
    vx REAL NOT NULL,
    vy REAL NOT NULL,
    vz REAL NOT NULL,
    rarad REAL NOT NULL,
    radec REAL NOT NULL,
    pmrarad REAL NOT NULL,
    pmdecrad REAL NOT NULL,
    bayer TEXT,
    flam INTEGER,
    con TEXT,
    comp INTEGER,
    comp_primary INTEGER,
    base TEXT,
    lum REAL NOT NULL,
    var TEXT,
    var_min REAL,
    var_max REAL
    );
    """
    conn = create_connection(db)
    if conn is not None:
        create_table(conn, sql_create_stars_table)
    else:
        print(f"Error: cannot connect to db: {db}")


if __name__ == "__main__":
    main()
