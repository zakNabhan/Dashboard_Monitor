import pandas as pd


from app import app
from dash.dependencies import Input, Output
from src.apps.components.dataset_monitor.layout import dataset_monitor_view
from src.apps.components.reports.pandas_profiling import Report
import plotly.express as px


layout = dataset_monitor_view

df = pd.read_csv('./data/datafake.csv')


@app.callback(

    Output("loading-output", "children"),
    Output("report_file", "options"),
    Input("generate_report", "n_clicks"),

)
def generate_a_report(n_clicks):
    report = Report()
    if n_clicks:
        report.create_pandas_profiling_report(df)
    files = report.display_list_of_reports()
    return "", [{'label': filename, 'value': filename} for filename in files]


@app.callback(

    Output('indicator-graphic', 'figure'),
    Input("xaxis-column", "value"),
    Input("yaxis-column", "value"),


)
def update_graph(xaxis_column_name, yaxis_column_name):
    df = pd.read_csv(
        "https://plotly.github.io/datasets/country_indicators.csv")
    fig = px.scatter(df, x=xaxis_column_name, y=yaxis_column_name)

    return fig
