import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc


st.title('🌧️ Predict Rainfall')

st.info(' This app uses a machine learning model to predict rainfall')

with st.expander('Data'):
  st.write('**Raw Cleaned Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/daudisraf/weatherAUS/refs/heads/main/cleaned2_weatherAUS.csv')
  df

  st.write('**X = Features**')
  X = df.drop('RainTomorrow', axis=1)
  X

  st.write('**y = Target**')
  y = df.RainTomorrow
  y

with st.expander('Data Viz'):
  st.scatter_chart(data=df, x='Rainfall', y='Humidity3pm', color='Rainfall')

# Data Prep
with st.sidebar:
  st.header('Input Features')
  MinTemp = st.slider('Min Temperature (Celsius)', -10, 50, 30)
  MaxTemp = st.slider('Max Temperature (Celsius)', -10, 50, 30)
  Temp9a = st.slider('Temperature at 9am (Celsius)', -10, 50, 30)
  Temp3p = st.slider('Temperature at 3pm (Celsius)', -10, 50, 30)
  

  
  
  
