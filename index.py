import dash_core_components as dcc
import dash_html_components as html

from src.apps import index
from dash.dependencies import Input, Output
from src.apps.components.dataset_monitor import dm_index

from app import app, dataset_app

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == dataset_app:
        return dm_index.layout
    else:
        return index.layout


if __name__ == '__main__':
    app.run_server(debug=True)
