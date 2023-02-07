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
    st.title('Input Form Pekerjaan')
    #membuat form
    with st.form(key='form_input'):
        SKH = st.number_input('Nama Kendaraan', min_value = 20, max_value = 110,step=1)
        activity = st.selectbox('Jenis pekerjaan',('Bonding Wire, Lanyard & Flame Trap Check', 'interlock system',
       'tyre pressure and wheel', 'Emergency Shutdown Button Record',
       'Elevating Work Platform Inspection',
       'Refueler Tank Interior Inspection Report', 'Fire Extinguisher',
       'Deadman Valve Test', 'Millipore Calorimetric Test Record (1)',
       'Millipore Calorimetric Test Record (2)', 'ROTA B', 'ROTA A',
       'Fueling Step and Ladder', 'Pneumatic &Hidraulic Check', 'HEPC',
       'Collector Tank',
       'Overfill/ High Level Dry Test dan Wet Test (REFUELER)',
       'Meter Calibration (Internal)', 'METER CALIBRATION (EXTERNAL)',
       'Press Gauge Accuracy Test Record', 'PDG Test & EWS',
       'Flexible Join', 'Input Coupler Wear Check',
       'Internal Vessel Inspection & Accessories', 'Filter Change',
       'Tank Inspection/  Cleaning', 'Hose Check Input Coupler',
       'Hose Check Report Input Coupler', 'Hose Check Report Hose Reel',
       'Hose Check Hose Reel', 'Hose Check Platform',
       'Hose Check Report Platform'),index = 0)
        sch_date = st.date_input("Tanggal pada jadwal",datetime.date(2022, 7, 6))
        fin_date = st.date_input("Tanggal pengerjaan",datetime.date(2022, 7, 6))
        cause = st.text_input('Penyebab',value = '')
        follup = st.text_input('Tindak Lanjut',value='')
        sparepart = st.text_input('Penggunaan Sparepart',value='')
        status = st.selectbox('Status', ('Ok','Not Ok'),index = 0)
        st.markdown('---')
        
        submitted = st.form_submit_button('Sumbit')