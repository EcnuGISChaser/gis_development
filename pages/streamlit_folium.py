# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:06:31 2023

@author: jpwu
"""


import folium
import streamlit as st
from streamlit_folium import st_folium

st.title("streamlit_folium示例")
tiles = 'http://webst01.is.autonavi.com/appmaptile?style=7&x={x}&y={y}&z={z}'
attr = '高德地图'

m = folium.Map(width = 600,height = 400,tiles=tiles,attr=attr,
               location=[30,115],zoom_start = 4)
cities=[
    ["北京",116.37,39.92,2170,"https://jpwu19860184.github.io/china/beijing.jpg"],
    ["上海",121.53,31.26,2418,"https://jpwu19860184.github.io/china/shanghai.jpg"],
    ["广州",113.25,23.13,1449,"https://jpwu19860184.github.io/china/guangzhou.jpg"] ]
for city in cities:
    city_name = city[0]
    x = city[1]
    y = city[2]
    pop = city[3]
    img_src = city[4]
    html = f"""<h4>{city_name}</h4>
               人口：{pop}万
               <img src={img_src}>
            """
    popup = folium.Popup(html,max_width=200)
    folium.Marker(location=[y,x],
                  popup=popup).add_to(m)

output = st_folium(m, width=700, height=500)

