import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

# Create the plot
def create_rainy_day_cartoon():
    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')  # Hide axes

    # Draw the ground
    ax.fill_between([0, 10], 0, 1, color='green', label="Ground")

    # Draw a cloud
    def draw_cloud(x, y, size=1):
        cloud_colors = ['#d3d3d3', '#f5f5f5']
        for dx, dy in [(0, 0), (-0.3, 0.2), (0.3, 0.2)]:
            circle = plt.Circle((x + dx, y + dy), size, color=np.random.choice(cloud_colors), ec='gray', lw=0.5)
            ax.add_patch(circle)

    # Clouds
    for cloud_x in [3, 7]:
        draw_cloud(cloud_x, 5, 0.8)

    # Draw raindrops
    def draw_raindrop(x, y):
        ax.plot([x, x], [y, y - 0.5], color='blue', lw=1)

    # Random raindrops below clouds
    np.random.seed(42)
    for _ in range(100):
        x = np.random.uniform(2.5, 3.5)
        y = np.random.uniform(3, 5)
        draw_raindrop(x, y)

    for _ in range(100):
        x = np.random.uniform(6.5, 7.5)
        y = np.random.uniform(3, 5)
        draw_raindrop(x, y)

    # Draw an umbrella
    def draw_umbrella():
        # Umbrella stick
        ax.plot([5, 5], [1, 3], color='brown', lw=2)
        # Umbrella top
        umbrella = plt.Polygon(
            [[4.5, 3], [5.5, 3], [5, 3.5]], color='red', ec='black'
        )
        ax.add_patch(umbrella)

    # Add the umbrella
    draw_umbrella()

    # Add a character (simple smiley face)
    face = plt.Circle((5, 2), 0.3, color='yellow', ec='black')
    ax.add_patch(face)
    # Eyes
    ax.plot([4.9, 5.1], [2.1, 2.1], 'o', color='black')
    # Smile
    smile = Arc((5, 1.9), 0.2, 0.1, angle=0, theta1=0, theta2=180, color='black')
    ax.add_patch(smile)

    plt.title("Rainy Day Cartoon", fontsize=16)
    return fig

# Streamlit interface
st.title("Rainy Day Cartoon in Streamlit")

# Generate and display the cartoon
fig = create_rainy_day_cartoon()
st.pyplot(fig)


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
