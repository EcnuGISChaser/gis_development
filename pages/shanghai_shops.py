# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:32:40 2023

@author: jpwu
"""

import folium
from folium.features import GeoJson,GeoJsonPopup
from folium import Marker,CircleMarker
import geopandas as gpd
import streamlit as st
from streamlit_folium import st_folium

import os
from pathlib import Path
path = Path(os.path.dirname(__file__))
filename = r"https://EcnuGISChaser.github.io/gis_development.github.io/data/上海商业网点.shp"
#st.write(filename)
gdf = gpd.read_file(filename)
minx = gdf.bounds["minx"].min()
miny = gdf.bounds["miny"].min()
maxx = gdf.bounds["maxx"].max()
maxy = gdf.bounds["maxy"].max()


m = folium.Map(tiles=None,zoom_start=10)
m.fit_bounds([(miny,minx),(maxy,maxx)])

map_tiles = 'http://webst01.is.autonavi.com/appmaptile?style=7&x={x}&y={y}&z={z}'
folium.TileLayer(tiles=map_tiles,
                 name="高德地图",
                 attr="高德地图",
                 control=True,
                 overlay=False,
                ).add_to(m)

image_tiles = "http://webst01.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}"
folium.TileLayer(tiles=image_tiles,
                 name="高德遥感影像",
                 attr="高德遥感影像",
                 control=True,
                 overlay=False,
                ).add_to(m)

circleMarker = CircleMarker()

def style_function(feature):
    style = {"radius":8,
             "color":"black",
             "weight":2,
             "fill":True,
             "fillColor":"red",
             "fillOpacity":1}
    return style


st.title("上海市商业网点")
#st.dataframe(gpd)
option = st.selectbox(
    '选择行业',
    ['食品', '房产', '衣着', '物质生活',"文化生活","资本流动","旅行","综合"])


exp = gdf["行业"]==option
gdf = gdf[exp]
count = len(gdf)
text = f"共有{count}个{option}商业网点"
st.text(text)
gjson = GeoJson(data=gdf,
                name="商业网点",
                marker=circleMarker,
                style_function=style_function).add_to(m)
GeoJsonPopup(fields=["行业","业态","业种","店名","地址","面积","商品"],
             labels=True).add_to(gjson)
folium.LayerControl().add_to(m)

output = st_folium(m, width=700, height=500)
