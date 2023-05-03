# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:32:40 2023

@author: jpwu
"""

import geopandas as gpd
url = "https://EcnuGISChaser.github.io/gis_development.github.io/data/shanghai_shops.json"
gdf = gpd.read_file(url, driver='GeoJSON')
gdf
