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

def run() :
    conn = sqlite3.connect('../pelitaAirDB')
    c = conn.cursor()
    st.title('Login')
    #membuat form
    with st.form(key='form_login'):
        name = st.text_input('Name', value='')
        password = st.text_input('Password',type="password", value='')
        st.markdown('---')
        submitted = st.form_submit_button('Login')
        if submitted:
            if not conn.execute(''' SELECT * FROM Users WHERE username = "{}" AND password = "{}"'''.format(name, password)).fetchone():  # An empty result evaluates to False.
                st.warning("WRONG USERNAME OR PASSWORD")
            else:
                st.success("Logged In as {}!".format(name))
                role = conn.execute(''' SELECT role FROM Users WHERE username = "{}" AND password = "{}"'''.format(name, password)).fetchone()[0]
                st.session_state.user = name
                st.session_state.role  = role
                st.session_state.password  = password
    conn.close() 