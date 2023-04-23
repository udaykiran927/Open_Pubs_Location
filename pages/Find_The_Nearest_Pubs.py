import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from PIL import Image
import os
st.set_page_config(layout="wide")

df = pd.read_csv('pubs.csv')

st.title(":red[Find the Nearest Pubs]")
image = Image.open('pub_image.jpeg')
st.image(image)
user_lat = st.text_input("Enter your Latitude:")
user_lon = st.text_input("Enter your Longitude:")

if st.button("Find nearest pubs"):
    if user_lat and user_lon:
        user_location = (float(user_lat), float(user_lon))
        df['distance'] = df.apply(lambda x: ((x['latitude'] - user_location[0])**2 + (x['longitude'] - user_location[1])**2)**0.5, axis=1)
        nearest_df = df.nsmallest(5, 'distance')
        pub_map = folium.Map(location=user_location, zoom_start=12)
        mc = MarkerCluster()
        for i in nearest_df.iterrows():
            mc.add_child(folium.Marker(location=[i[1]['latitude'], i[1]['longitude']], popup=i[1]['name']))
        pub_map.add_child(mc)
        folium_static(pub_map)