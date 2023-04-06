# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:53:50 2023

@author: jpwu
"""
import requests
import json
import streamlit as st
st.title("POI点查询")
add = st.text_input("地点","华东师范大学闵行校区")
distance = st.text_input("距离（m）","1000")
POI_type = st.selectbox("POI类型",("酒店","银行","学校"))
st.button("查询")
st.text("查询结果")

service ="http://api.map.baidu.com/geocoding/v3/?"
output = "json"
AK= "0IMHPtsuUFbNnYU7aCngXCq6Feh8TM1m"
address = add
parameters = f"address={address}&output={output}&ak={AK}"
url = service + parameters
response = requests.get(url)
text=response.text
dic=json.loads(text)
status = dic["status"]
if status==0:
    lng = dic["result"]["location"]["lng"]
    lat = dic["result"]["location"]["lat"]
else:
    st.text(f"{address}:地理编码不成功")

service ="http://api.map.baidu.com/place/v2/search?"
query = POI_type
radius = float(distance)
page_size = 20
parameters = f"query={query}&location={lat},{lng}&radius={radius}\
&page_size={page_size}&output={output}&ak={AK}"
url = service + parameters
response = requests.get(url)
text=response.text
dic=json.loads(text)
if dic["status"]==0:
    st.text(f"共检索到{dic['total']}个POI：")
    for result in dic["results"]:
        st.text(result["name"])
else:
    st.text("POI检索不成功")


   

  