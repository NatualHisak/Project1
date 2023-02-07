import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image
import Login, Home, Input



st.set_page_config(page_title = 'Planning', layout='wide', initial_sidebar_state='expanded')

navigation = st.sidebar.selectbox('Pilih Halaman : ', ('Home', 'Login','Input'))
if navigation == 'Home':
    Home.run()
elif navigation == "Login" :
    Login.run()
elif navigation == "Input" :
    Input.run()