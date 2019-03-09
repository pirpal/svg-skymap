#!usr/bin/env python3
# coding: utf8

# SQL requests for tables creation

sqlite3_create_stars_table = """
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

sqlite3_create_deepskyobjects_table = """
    CREATE TABLE IF NOT EXISTS deep_sky_objects(
    id INTEGER PRIMARY KEY UNIQUE,
    ra REAL NOT NULL,
    dec REAL NOT NULL,
    const TEXT,
    mag REAL NOT NULL,
    name TEXT,
    rarad REAL NOT NULL,
    decrad REAL NOT NULL,
    r1 REAL,
    r2 REAL,
    angle REAL,
    dso_cource INTEGER,
    id1 INTEGER,
    cat1 TEXT,
    id2 INTEGER,
    cat2 TEXT,
    dupid INTEGER,
    dupcat TEXT,
    display_mag REAL
    );
    """

sqlite3_create_cities_table = """
    CREATE TABLE IF NOT EXISTS cities(
    id INTEGER PRIMARY KEY UNIQUE,
    city TEXT NOT NULL,
    city_ascii NOT NULL,
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    country TEXT NOT NULL,
    iso2 TEXT NOT NULL,
    iso3 TEXT NOT NULL,
    admin_name TEXT NOT NULL,
    population INTEGER
    );
    """
