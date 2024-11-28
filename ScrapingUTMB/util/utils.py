import numpy as np
from typing import Dict


def convert_time_to_sec(time : str) -> int:
    # Convert everything to seconds

    hours, minutes, seconds = map(int, time.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds   

    return total_seconds

def seconds_to_hms(seconds):
    # Calculate hours, minutes, and seconds

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

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

import numpy as np

def find_exact_x(x_values, y_values, target_y):
    """
    Approximate the x value corresponding to a given y using linear interpolation.
    Automatically sorts the data by y-values.
    
    Parameters:
        x_values (list or np.array): The x-axis values.
        y_values (list or np.array): The y-axis values.
        target_y (float): The target y value.
    
    Returns:
        float: Approximated x value.
    """
    # Convert to numpy arrays for easier manipulation

    print(y_values)
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    # Sort by y-values
    sorted_indices = np.argsort(y_values)
    y_values = y_values[sorted_indices]
    x_values = x_values[sorted_indices]

    # Check if target_y is within range
    if target_y < y_values.min() or target_y > y_values.max():
        raise ValueError(f"Non abbiamo dati per questo indice, aumenta l'indice fornito\n minimo {y_values.min()} e max {y_values.max()}")

    # Find the interval for interpolation
    for i in range(len(y_values) - 1):
        y1, y2 = y_values[i], y_values[i + 1]
        x1, x2 = x_values[i], x_values[i + 1]

        if y1 <= target_y <= y2 or y2 <= target_y <= y1:
            # Perform linear interpolation
            x_approx = x1 + (target_y - y1) * (x2 - x1) / (y2 - y1)
            return x_approx

    raise ValueError("Interpolation failed: check your data or target value.")
