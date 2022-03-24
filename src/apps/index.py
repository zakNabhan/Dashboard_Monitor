
import os

import dash_html_components as html
import dash_bootstrap_components as dbc

from app import *
from dash.dependencies import Input, Output

cards = dbc.CardDeck([
    dbc.Card([
        dbc.CardBody(
            [


                html.H4("Dataset Monitor", className="card-title"),
                html.Br(),

                dbc.CardLink("Dataset Monitor", href=dataset_app),
            ]
        ),

    ]),
    dbc.Card([
        dbc.CardBody(

        ),

    ],),


    dbc.Card([
        dbc.CardBody(

        ),

    ],),

], className="cards")


layout = html.Div([

    header,
    html.Br(),
    cards,

], style={"margin-top": "150px"})
