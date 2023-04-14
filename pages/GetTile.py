# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:25:48 2023

@author: jpwu
"""

import streamlit as st
from math import log,tan,pi
import requests

st.title("返回地图切片")
z = st.number_input('输入比例尺级别0~18',min_value=0,max_value=18,value=0,format="%d")
lng = st.number_input('输入经度-180~180',min_value=-180.,max_value=180.,value=0.,format="%f")
lat = st.number_input('输入纬度-90~90',min_value=-90.,max_value=90.,value=0.,format="%f")
st.button('确定')
r = 20037508.34
x = lng*r/180 
y = log(tan(pi/4+lat*pi/360))*(r/pi)  
d = 40075014/(2**int(z))
row = int((20037507-y)/d)
col = int((x-(-20037507))/d)
url = f"https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{row}/{col}.png"
response = requests.get(url)
image = response.content   
st.image(image, width = 400,caption=f'z={z},lng={lng},lat={lat}')

st.download_button('下载切片图像', 
                   image,
                   file_name="tile.png",
                   mime="image/png")