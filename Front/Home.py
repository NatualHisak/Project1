import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image
df = pd.read_csv(r'C:\Users\Omen\Desktop\Database project\cleaned.csv')
def run() :
    st.title('Planning Pekerjaan Tahunan')
    image = Image.open('logo.png')
    st.image(image,caption = 'Logo')
    st.markdown('---')

    st.dataframe(df)