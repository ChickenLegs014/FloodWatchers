'''
Authors     : Aaron Sapp & Warren Nixon
Date        : Oct. 5, 2026
Course      : CSCI-2996-A01-SPECIAL TOPICS: Problem Solving
Module      : map.py
Description : Creates a window with an interactive map
'''

import streamlit as st
import leafmap.foliumap as leafmap

# Configure web application
st.set_page_config(layout = "wide")
st.title("Interactive Flood Mapping Dashboard")
st.sidebar.title("Controls")

# Alamogordo coordinates
# latitude = 32.8995
# longitude = -105.9603

# Add coordinates inputs to the sidebar
latitude = st.sidebar.number_input("Latitude", value = 32.8995, format = "%.4f")
longitude = st.sidebar.number_input("Longitude", value = -105.9603, format = "%.4f")
zoom = st.sidebar.slider("Zoom Level", min_value = 1, max_value = 20, value = 10)

# Initialize and display map layer
st.write("### Regional Topography & Water Risk Map")
m = leafmap.Map(center = [latitude, longitude], zoom = zoom)

# Render interactive map block inside Streamlit
m.to_streamlit(height = 600)
