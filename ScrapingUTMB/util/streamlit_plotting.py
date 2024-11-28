import plotly.graph_objs as go

def plot_example(times, indexs, y_pred, threshold, out_plot_x, out_plot_y, time_p, index_input):
    race_plot = go.Figure()
    race_plot.add_trace(go.Scatter(x = times, y = indexs, mode='markers', marker=dict(size=10, color='blue'), name='runner predetti'))
    race_plot.add_trace(go.Scatter(x = out_plot_x, y = out_plot_y, mode='markers', marker=dict(size=10, color='red'), name = 'runner outliers'))
    race_plot.add_trace(go.Scatter(x = [time_p], y = [index_input] , mode='markers', marker=dict(size=25, color='green'), name='La tua predizione'))

    #race_plot.add_trace(go.Scatter(x = times, y = y_pred,marker=dict(size=10, color='green'), name = 'media predizione'))
    #race_plot.add_trace(go.Scatter(x = times, y = y_pred + threshold,marker=dict(size=10, color='red'), name = 'upperbound outliers'))
    #race_plot.add_trace(go.Scatter(x = times, y = y_pred - threshold, marker=dict(size=10, color='red'), name = 'lowerbound outliers'))
    race_plot.update_layout(
        height = 800
    )
    return race_plot

def plot_error(errori_race, runners_count):
    race_error = go.Figure()
    race_error.add_trace(
        go.Bar(
            x = ['outliers', 'runner predetti', 'totale runner'],
            y = [errori_race, runners_count - errori_race, runners_count] 
        )
    )
    return race_error