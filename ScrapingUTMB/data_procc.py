import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import plotly.graph_objs as go
import os

# Specify the folder path

def plot_error(race_error, errori_race, runners_count):

    race_error.add_trace(
        go.Bar(
            x = ['outliers', 'runner predetti', 'totale runner'],
            y = [errori_race, runners_count - errori_race, runners_count] 
        )
    )

def UTMB_precision(race):

    folder_path = './data_races'

    # Get list of filenames in the folder
    file_json = os.listdir(folder_path)

    err = []
    err_race = []

    # Print the list of file names
    for json_data in file_json:

        times, indexs, y_pred, threshold, out_plot_x, out_plot_y, outlier_count = get_data_race(json_data)

        print(outlier_count, len(indexs), outlier_count/len(indexs))

        err.append(outlier_count/len(indexs) * 100)
        if json_data == race:

            err_race.append([outlier_count, len(times)])

    return err, err_race[0][0], err_race[0][1]

def plot_example(race_plot, times, indexs, y_pred, threshold, out_plot_x, out_plot_y):

    race_plot.add_trace(go.Scatter(x = times, y = indexs, mode='markers', marker=dict(size=10, color='blue'), name='runner predetti'))
    race_plot.add_trace(go.Scatter(x = out_plot_x, y = out_plot_y, mode='markers', marker=dict(size=10, color='red'), name = 'runner outliers'))
    race_plot.add_trace(go.Scatter(x = times, y = y_pred,marker=dict(size=10, color='green'), name = 'media predizione'))
    race_plot.add_trace(go.Scatter(x = times, y = y_pred + threshold,marker=dict(size=10, color='red'), name = 'upperbound outliers'))
    race_plot.add_trace(go.Scatter(x = times, y = y_pred - threshold, marker=dict(size=10, color='red'), name = 'lowerbound outliers'))
    race_plot.update_layout(
        height = 800
    )
    
def get_data_race(race):
    
    print(race)
    with open('./data_races/'+race, "r") as file:
        data = json.load(file)

    times = []
    indexs = []

    for runner in data:
        time, index = data[runner]
        if time != None and index != None and index != '-':
            hours, minutes, seconds = map(int, time.split(':'))
            # Convert everything to seconds
            total_seconds = hours * 3600 + minutes * 60 + seconds
            times.append(total_seconds)
            indexs.append(int(index))

    coefficients = np.polyfit(times, indexs, 1)  # Linear fit (degree 1)
    line = np.poly1d(coefficients)  # Line equation


    # Predicted y-values (on the fitted line)
    y_pred = line(times)
    residuals = np.abs(indexs - y_pred)
    threshold = 2 * np.std(residuals)

    # Identify outliers
    outliers = residuals > threshold
    outlier_count = np.sum(outliers)

    out_plot_x = np.array(times)[outliers]
    out_plot_y = np.array(indexs)[outliers]

    return times, indexs, y_pred, threshold, out_plot_x, out_plot_y, outlier_count