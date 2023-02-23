import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image
df = pd.read_csv(r'C:\Projects\Project1\data\cleaned.csv')

def run() :
    if 'user' not in st.session_state and 'password' not in st.session_state:
        st.title('Planning Pekerjaan Tahunan')
        st.markdown('Please visit the login page')
    else:
        st.title('Planning Pekerjaan Tahunan')
        image = Image.open('logo.png')
        st.image(image,caption = 'Logo')
        st.markdown('---') 
        st.dataframe(df)