import streamlit as st
import pandas as pd

st.title('🌧️ Predict Rainfall')

st.info(' This app uses a machine learning model to predict rainfall')

df = pd.read_csv('https://github.com/daudisraf/weatherAUS/blob/main/weatherAUS.csv')
