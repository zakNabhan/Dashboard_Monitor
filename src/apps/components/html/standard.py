import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def create_standard_loading_indicator(id, type, className):
    indicator = html.Div(children=[
        dcc.Loading(
            className=className,
            type=type,
            children=html.Div(id=id))
    ]),

    return indicator
