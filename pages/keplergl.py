# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:32:40 2023

@author: jpwu
"""

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd

url = "https://EcnuGISChaser.github.io/gis_development.github.io/data/shanghai_shops.json"
gdf = gpd.read_file(url)
map_1 = KeplerGl(height=400)
map_1.add_data(gdf, 'shanghai shops')
keplergl_static(map_1,center_map=True)



