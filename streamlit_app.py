import streamlit as st
import pandas as pd

st.title('🌧️ Predict Rainfall')

st.info(' This app uses a machine learning model to predict rainfall')

with st.expander('Data'):
  st.write("**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/daudisraf/weatherAUS/refs/heads/main/weatherAUS.csv')
  df
