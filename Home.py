import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from PIL import Image
st.set_page_config(layout="wide")



df = pd.read_csv('pubs.csv')

st.title(":red[Pubs Application]")
image = Image.open('pub_image.jpeg')
st.image(image)

st.markdown("## :blue[About the Dataset]")

st.markdown("###### Top Five Rows of Dataset")
st.write(df.head())

st.markdown("###### Total Numbers of Rows and Columns")
st.write("Total number of Pubs:", df.shape[0])
st.write("Total number of columns:", df.shape[1])

st.markdown("Postal Codes :")
st.write(df['postcode'].value_counts().head().index)
st.markdown("###### Top 10 Locations Which have more pubs")
st.write(df['local_authority'].value_counts()[:10].index)
