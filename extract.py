#!/usr/bin/python
# Extracts bike paths from OSM data in PostGIS, saves as GeoJSON.
# Written by Steve Bennett for OKFNau, released under WTFPL.
from psycopg2 import *
from subprocess import call

conn = connect(dbname='gis')
cur=conn.cursor()
networks = ['lcn','rcn','ncn']
for network in networks:
  cur.execute("SELECT distinct osm_id,route_name from planet_osm_line where route_name is not null and network='%s';" % network)

  for record in cur:
    print "%s" % record[1]
    call (["ogr2ogr", "-f", "GeoJSON", network + "/" + record[1] + ".json",  'PG:dbname=\'gis\'', "-sql", 'SELECT route_name,osm_id,tags::hstore->\'state\' as state,way from planet_osm_line where osm_id=%d' % record[0], "-t_srs", "EPSG:4326", "-s_srs", "EPSG:3857"])
