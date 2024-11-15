import streamlit as st
import os
from data_procc import get_data_race, plot_example, UTMB_precision, plot_error
import plotly.graph_objs as go
import numpy as np

st.set_page_config(layout="wide")

st.title('UTMB INDEX PRECISION ( data-driven study )')

race = st.selectbox(
    '! Select one vehicle !',
    os.listdir('data_races'))

times, indexs, y_pred, threshold, out_plot_x, out_plot_y, outlier_count = get_data_race(race)
errori_totali, errori_race, runners_count = UTMB_precision(race)

col1, col2 = st.columns([3,2])
with col1:
    st.subheader('Runner time/UTMB index plot')
    race_plot = go.Figure()
    plot_example(race_plot, times, indexs, y_pred, threshold, out_plot_x, out_plot_y)
    st.plotly_chart(race_plot)
with col2:
    st.subheader('UTMB precision calculation')
    st.write('number of outliers / total runner of the race')
    race_error = go.Figure()
    plot_error(race_error, errori_race, runners_count)
    st.plotly_chart(race_error)
    print(errori_totali)
    st.subheader('MEDIA ERRORE UTMB INDEX')
    st.write(np.mean(errori_totali))   
    st.subheader('MEDIA ERRORE QUESTA GARA') 
    st.write((errori_race) / runners_count * 100)