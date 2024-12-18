import streamlit as st
import os
import numpy as np
from util.streamlit_plotting import plot_example, plot_error
from util.utils import seconds_to_hms
from api.scraperUTMBapi import Scraper_UTMB_Api

st.set_page_config(layout="wide")

st.title('UTMB INDEX PRECISION ( data-driven study )')

race = st.selectbox(
    '! Select one vehicle !',
    os.listdir('data_races'))

number = st.text_input(
    "Insert a number", value='500', placeholder="Type a number..."
)

assert number.isdigit() == True , 'Please enter a valid number'
assert 0 < int(number) < 1000, 'Index incorrect ( 0 < index < 1000)'

if st.button('make calculation'):
    times, indexs, y_pred, threshold, out_plot_x, out_plot_y, outlier_count = Scraper_UTMB_Api.get_plots_data_race_fromJson(race)
    errori_totali, errori_race, runners_count = Scraper_UTMB_Api.UTMB_precision(race)
    time_pred = (Scraper_UTMB_Api.estimate_time_race(int(number), race))
    st.subheader(f'Tempo in gara stimato tra {seconds_to_hms(time_pred + time_pred//10)} Ed {seconds_to_hms(time_pred - time_pred//10)}')
    col1, col2 = st.columns([3,2])
    with col1:
        st.subheader('Runner time/UTMB index plot')
        race_plot = plot_example(times, indexs, y_pred, threshold, out_plot_x, out_plot_y, time_pred, number)
        st.plotly_chart(race_plot)
    with col2:
        st.subheader('UTMB precision calculation')
        st.write('number of outliers / total runner of the race')
        race_error = plot_error(errori_race, runners_count)
        st.plotly_chart(race_error)
        st.subheader('MEDIA ERRORE UTMB INDEX')
        st.write(np.mean(errori_totali))   
        st.subheader('MEDIA ERRORE QUESTA GARA') 
        st.write((errori_race) / runners_count * 100)

