# Extracts bike paths from OSM data in PostGIS, saves as GeoJSON.
# Written by Steve Bennett for OKFNau, released under WTFPL.
from psycopg2 import *
from subprocess import call

conn = connect(dbname='gis')
cur=conn.cursor()

cur.execute("SELECT distinct osm_id,route_name from planet_osm_line where route_name like '%Rail Trail' and network='rcn';")

for record in cur:
  print "%s" % record[1]
  call (["ogr2ogr", "-f", "GeoJSON", record[1] + ".json",  'PG:dbname=\'gis\'', "-sql", 'SELECT route_name,osm_id,tags::hstore->\'state\' as state,way from planet_osm_line where osm_id=%d' % record[0], "-t_srs", "EPSG: 4326"])
