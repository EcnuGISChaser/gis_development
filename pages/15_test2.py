# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:25:48 2023

@author: jpwu
"""


import folium
from folium.plugins import LocateControl
import streamlit as st
from streamlit_folium import st_folium
tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png'
attr = 'ArcGIS online全球影像'
m = folium.Map(location=[31, 121.5],
               tiles=tiles,
               attr=attr,
               width=600,
               height=400)
LocateControl(strings={"title":"定位当前位置","popup":"你的位置"}
             ).add_to(m)

output = st_folium(m,width=700, height=400)
if output["center"] != None:
    lat = output["center"]["lat"]
    lng = output["center"]["lng"]
    txt = f"lat:{lat},lng:{lng}"
    st.text(txt)
#csv = df.to_csv().encode('GBK')
st.download_button('下载',txt,file_name="test.txt")