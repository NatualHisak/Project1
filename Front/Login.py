import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image

def run() :
    st.title('Login')
    #membuat form
    with st.form(key='form_login'):
        name = st.text_input('Name', value='')
        password = st.text_input('Password',type="password", value='')
        st.markdown('---')
        
        submitted = st.form_submit_button('Login')
