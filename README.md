This is a collection of GeoJSON files extracted from OpenStreetMap Oceania, representing bike routes tagged with the 'LCN','RCN' or 'NCN' network tags. (These correspond to local, regional and national cycling network - concepts that do not apply very well in countries outside Europe.)

Why? Because it's much easier for people with limited knowledge of GIS to overlay a GeoJSON file on an existing map, rather than working with OSM extracts.

Licence: ODbL, just like OpenStreetMap. Attribution: OpenStreetMap contributors.

Limitations:

* There is an issue if two separate routes have the same name (usually because they're the same route, but haven't been merged in OSM). Only one file will be produced.
* There is no information about physical infrastructure (bike paths vs on-road), because of how OSM2PGSQL processes routes.
