# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:25:48 2023

@author: jpwu
"""
import streamlit as st
import streamlit.components.v1 as components

content = """
<body>
    <button onclick="getLocation()">定位</button><br>
    当前坐标：<input type="text" value="" id="position"></><br>

    <script>
      function getLocation()
      {
          if (navigator.geolocation)
          {
              navigator.geolocation.getCurrentPosition(showPosition);
          }
          else
          {
              alert("你的浏览器不支持地理定位");
          }
      }
      function showPosition(position)
      {
          
          x = position.coords.longitude.toFixed(4); 
          y = position.coords.latitude.toFixed(4);
          coords = x+","+y;
          document.getElementById("position").value=coords;
      }
    </script>
</body>
"""
components.html(f"<div>{content}</div>")

import folium
from folium.plugins import LocateControl
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

st_folium(m,width=700, height=400)