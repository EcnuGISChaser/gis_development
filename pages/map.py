# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:33:19 2023

@author: jpwu
"""

import streamlit as st
import pandas as pd

frame = pd.read_csv(r"https://jpwu19860184.github.io/china/china_city_noheader.csv",
                    names=["城市名","lon","lat","省名","是否省会"],
                    encoding="gbk")
st.map(frame)

