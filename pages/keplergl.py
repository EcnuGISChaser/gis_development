# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:32:40 2023

@author: jpwu
"""

import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd
st.title("天目山实习区POI点")
data = r'https://EcnuGISChaser.github.io/gis_development/data/tms_POIs.geojson'
gdf = gpd.read_file(data)
config ={'version': 'v1',
         'config': {'mapStyle':{'styleType':'satellite'}}}
map_1 = KeplerGl(height=400,config=config)
map_1.add_data(gdf, '天目山实习区POI点')
keplergl_static(map_1,center_map=True)



