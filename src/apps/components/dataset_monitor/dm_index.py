import os
import dash
from dash import dcc
from dash.dependencies import Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import logging
import numpy as np
import pandas as pd

from app import app
from src.apps.components.dataset_monitor.layout import dataset_monitor_view
from src.apps.components.reports.pandas_profiling import Report


layout = dataset_monitor_view

df = pd.read_csv('./data/datafake.csv')

@app.callback(
    
    Output("loading-output", "children"),
    Output("report_file", "options"),
    Input("generate_report", "n_clicks"),

)
def create_a_report_from_dataset(n_clicks):
    report = Report()
    if n_clicks:
        report.create_pandas_profiling_report(df)
    files = report.display_list_of_reports()
    return  "", [{'label': filename ,'value': filename} for filename in files]