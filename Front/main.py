import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image
import sqlite3
import Home, Input, Login

if 'role' not in st.session_state:
    st.session_state.role = "user"
    
st.set_page_config(page_title = 'Planning', layout='wide', initial_sidebar_state='expanded')

if st.session_state.role == "admin":
    navigation = st.sidebar.selectbox('Pilih Halaman : ', ('Login','Home','Input','Add User','Ganti Tahun'))
else:
    navigation = st.sidebar.selectbox('Pilih Halaman : ', ('Login','Home','Input'))

if navigation == 'Home':
    Home.run()
elif navigation == "Login" :
    Login.run()
elif navigation == "Input" :
    Input.run()