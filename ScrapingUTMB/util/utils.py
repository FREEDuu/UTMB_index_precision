import numpy as np
from typing import Dict


def convert_time_to_sec(time : str) -> int:
    # Convert everything to seconds

    hours, minutes, seconds = map(int, time.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds   

    return total_seconds

def get_plot_data(json_data : Dict):

    times = []
    indexs = []
    for runner in json_data:
        time, index = json_data[runner]
        if time != None and index != None and index != '-':
            total_seconds = convert_time_to_sec(time)
            times.append(total_seconds)
            indexs.append(int(index))

    coefficients = np.polyfit(times, indexs, 2)  # Linear fit (degree 1)
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