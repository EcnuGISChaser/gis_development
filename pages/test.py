# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:32:40 2023

@author: jpwu
"""

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd

#data = r'c:\data\china\china_cities.geojson'
#gdf = gpd.read_file(data)
map_1 = KeplerGl(height=400)
#map_1.add_data(gdf, 'china cities')
keplergl_static(map_1,center_map=True)
