Svg Skymaps
--------------

This is a astronomical API able to produce high quality svg maps of
the sky.

# Sources

The database used in this app makes an heavy (and fanly) use of
[astronexus databases](https://github.com/astronexus/HYG-Database). 

This sources (csv files) are used to feed the main app db

| **table**          | **fields** | **source**      | **rows** | **www**                                                  |
|--------------------|------------|-----------------|----------|----------------------------------------------------------|
| `stars`            | 36         | hygdata_v3.csv  |          | [astronexus](https://github.com/astronexus/HYG-Database) |
| `deep_sky_objects` | 20         | dso.csv         |          | idem                                                     |
| `world_cities`     | 11         | worldcities.csv |          | [simplemaps](https://simplemaps.com/data/world-cities))  |
|                    |            |                 |          |                                                          |

# Annexes
## Dependencies

Modules used in this app:

* `pendulum`
* `svgwrite`
* `sqlite3`

## Sources and db tables description
### HYG catalog
	
Right ascencion (`ra`) and declination (`dec`) are given for Epoch
2000.0 and Equinox 2000.0

|      **field** | **description**           | **unit**         | **type** | **null?** | **example**              |
|---------------:|---------------------------|------------------|----------|:---------:|--------------------------|
|           `id` | star id (*pk*)            |                  | int      |           | 32263                    |
|          `hip` | hipparcos id              |                  | int      |           | 32349                    |
|           `hd` | henry draper id           |                  | int      |           | 48915                    |
|           `hr` | harvard id                |                  | int      |           | 2491                     |
|           `gl` | gliese id                 |                  | string   |           | Gl 244A                  |
|           `bf` | bayer flamsteed name      |                  | string   | X         | `9 Alp CMa`              |
|       `proper` | proper name               |                  | string   | X         | `Sirius`                 |
|           `ra` | right ascencion           | degrees          | float    |           | 6.752481                 |
|          `dec` | declination               | degrees          | float    |           | -16.716116               |
|         `dist` | distance                  | parsecs          | float    |           | 2.6371                   |
|         `pmra` | ra proper motion          | milliarcsec/year | float    |           | -546.01                  |
|        `pmdec` | dec proper motion         | milliarcsec/year | float    |           | -1223.08                 |
|           `rv` | radial velocity           | km/sec           | float    | X         | -9.4                     |
|          `mag` | magnitude                 |                  | float    |           | -1.440                   |
|       `absmag` | absolute magnitude        |                  | float    |           | 1.454                    |
|        `spect` | spectral type             |                  | string   | X         | A0m...                   |
|           `ci` | color index               |                  | float    | X         | 0.009                    |
|            `x` | cartesian x pos           |                  | float    |           | -0.494323                |
|            `y` | cartesian y pos           |                  | float    |           | 2.476731                 |
|            `z` | cartesian z pos           |                  | float    |           | -0.758485                |
|           `vx` | cartesian x velocity      | parsec/year      | float    |           | 0.00000953               |
|           `vy` | cartesian y velocity      | parsec/year      | float    |           | -0.00001207              |
|           `vz` | cartesian z velocity      | parsec/year      | float    |           | -0.00001221              |
|        `rarad` | right ascencion           | radians          | float    |           | 1.7677953696021995       |
|       `decrad` | declination               | radians          | float    |           | -0.291751258517685       |
|      `pmrarad` | proper motion ra          | radians/year     | float    |           | -0.000002647131177201389 |
|     `pmdecrad` | proper motion dec         | radians/year     | float    |           | -0.000005929659164       |
|        `bayer` | bayer designation         |                  | string   |           | Alp                      |
|         `flam` | flamsteed number          |                  | int      |           | 9                        |
|          `con` | constellation             |                  | string   |           | CMa                      |
|         `comp` | companion star id         |                  | int      | X         | 1                        |
| `comp_primary` | system's primary star id  |                  | int      | X         | 32263                    |
|         `base` | system's gliese id        |                  | string   | X         | Gl 244                   |
|          `lum` | star luminosity           |                  | float    |           | 22.824433121735034       |
|          `var` | variable star designation |                  | ?        | X         |                          |
|      `var_min` | variable star min mag     |                  | float    | X         | -1.333                   |
|      `var_max` | variable star max mag     |                  | float    | X         | -1.523                   |


### DeepSkyObjects catalog

Right ascencion (`ra`) and declination (`dec`) are given for Epoch
2000.0 and Equinox 2000.0

**On objects orbits**:
if an object's semi-minor axe (`r2`) is undefined, its semi-major axe
(`r1`) is treated as orbit radius.
Object's `angle` is defined only if both `r1` and `r2` are defined.

|     **field** | **description**                       | **unit**   | **type** | **null?** |
|--------------:|---------------------------------------|------------|----------|:---------:|
|          `ra` | right ascencion                       | degrees    | float    |           |
|         `dec` | declination                           | degrees    | float    |           |
|       `const` | object's constellation if known       |            | float    | X         |
|         `mag` | visual magnitude                      |            | float    |           |
|        `name` | common name                           |            | string   |           |
|       `rarad` | right ascension                       | radians    | float    |           |
|      `decrad` | declination                           | radians    | float    |           |
|          `id` | unique id, primary key                |            | int      |           |
|          `r1` | semi-major axe                        | arcminutes | float    |           |
|          `r2` | semi-minor axe if known               | arcminutes | float    | X         |
|       `angle` | position angle of `r1`                | degrees    | float    | X         |
|  `dso_source` | DSO source for object data, see below |            | int      |           |
|         `id1` | most commonly used id                 |            | int      |           |
|        `cat1` | most commonly used name               |            | string   |           |
|         `id2` | alternative id                        |            | int      | X         |
|        `cat2` | alternative name                      |            | string   | X         |
|       `dupid` | duplicate id                          |            | int      |           |
|      `dupcat` | duplicate name                        |            | string   |           |
| `display_mag` | convenient magnitude (2)              |            | string   |           |

	(2) Display magnitude is an optionnal magnitude value for objects
	whose magnitude is either unknown or not representative of its
	actual visibility
	
### DSO Sources

Catalogs represented in the database:

| **code** | **catalog**                                      |
|----------|--------------------------------------------------|
| `M`      | Messier (bright objects of all types)            |
| `NGC`    | New General Catalogue (all types)                |
| `IC`     | Index Catalog (all types)                        |
| `C`      | Caldwell (bright objects of all types)           |
| `Col`    | Collinder (open clusters and associations)       |
| `PK`     | Perek + Kohoutek (planetary nebulas)             |
| `PGC`    | Principal Galaxy Catalog                         |
| `UGC`    | Uppsala Galaxy Catalog                           |
| `ESO`    | European Southern Observatory Catalog (galaxies) |
| `Ter`    | Terzian (globular clusters)                      |
| `Pal`    | Palomar (globular clusters)                      |

### World Cities

SvgSkymaps embbed a list of 13,000 cities around the world. Data are
taken from [simplemaps.com free
database](https://simplemaps.com/data/world-cities), thank to them!

|    **field** | **description**                               | **type** | **null?** |          **example** |
|-------------:|-----------------------------------------------|----------|:---------:|---------------------:|
|       `city` | unicode city name                             | str      |           |           `Bordeaux` |
| `city_ascii` | ascii city name                               | str      |           |           `Bordeaux` |
|        `lat` | latitude                                      | float    |           |            `44.8500` |
|        `lng` | longitude                                     | float    |           |            `-0.5950` |
|     `coutry` | country name                                  | str      |           |             `France` |
|       `iso2` | country's alpha-2 iso code                    | str      |           |                 `FR` |
|       `iso3` | country's alpha-3 iso code                    | str      |           |                `FRA` |
| `admin_name` | highest level of region's administration name | str      |           | `Nouvelle-Aquitaine` |
| `population` | estimated city's urban population             |          | X         |            `803,000` |
|         `id` | 10-digit unique id                            | int      |           |         `1250449238` |

# Footnotes

<a name="fnote1">Epoch J2000.0 see
[https://en.wikipedia.org/wiki/Epoch_(astronomy)](https://en.wikipedia.org/wiki/Epoch_(astronomy))</a>
