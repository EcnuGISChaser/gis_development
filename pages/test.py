# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:32:40 2023

@author: jpwu
"""

import streamlit as st
from PIL import Image

image1 = Image.open(r'data\p1.jpg')
st.image([image1], 
         width = 400,
         caption=['my photo1'])
