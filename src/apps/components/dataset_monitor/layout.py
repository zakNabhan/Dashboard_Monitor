from src.apps.components.html.standard import create_standard_loading_indicator
from src.apps.components.reports.pandas_profiling import Report
import logging
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from app import header, sidebar_STYLE, CONTENT_STYLE


# df = pd.read_csv('./data/datafake.csv')
df = pd.read_csv("https://plotly.github.io/datasets/country_indicators.csv")

reports = Report()

table_col1 = dbc.Card([
    dbc.CardBody([
        dash_table.DataTable(
            id='dataset_table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="single",
            row_deletable=False,
            export_columns='all',
            export_format="csv",
            export_headers='display',
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            style_table={'overflowX': 'auto'},
            page_current=0,
            page_size=14,
            style_data={
                'color': '#363945',
                'backgroundColor': 'white'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(240, 240, 240)',
                }
            ],
            style_header={
                'paddingRight': '70px',
                'textAlign': 'left',
                'fontWeight': 'bold',
                'color': '#545454'

            },
            css=[{"selector": ".show-hide", "rule": "display: none"}]

        ),

    ]),
])


table_row = dbc.Row([
    dbc.Col(table_col1, width={'size': 12, 'order': 1, 'offset': 0})
])


common_statistics = html.Div([
    dbc.Container(
        [
            html.Br(),
            html.H3("Dataset Monitor", className="display-5"),
            html.Hr(className="my-2"),



        ],
        fluid=True,
        className="py-3",
    ),

], className="p-3 bg-light rounded-3", style={"margin-top": "0px"})


toast = html.Div([
    dbc.Toast(
        [html.Div(

            html.Div(
                 html.Div([
                     html.Div(
                          [
                              html.Br(),
                              dcc.Dropdown(
                                  id="report_file",
                                  options=[{'label': file, 'value': file}
                                           for file in reports.display_list_of_reports()],
                                  placeholder="Select a report to download..."
                              ),

                          ]),
                     html.Br(),
                     html.Br(),
                     dbc.Row([
                         dbc.Col(
                             dbc.Button(
                                 id='generate_report',
                                 children='Generate',
                                 outline=True,
                                 color="secondary",
                                 className="mr-1",
                                 block=True
                             ),),

                         dbc.Col([
                             dbc.Button(
                                 "Export",
                                 id="btn_report",
                                 outline=True,
                                 color="secondary",
                                 className="mr-1",
                                 block=True,
                             ),
                             dcc.Download(id="download-report"),
                         ]),
                     ])

                 ])
                 ), className="mb-0")],
        header="Export pandas profiling",),
    dbc.Toast(
        [html.Div(reports.generate_dataset_overview(df), className="mb-0")],
        header="Common Statistics",),

    dbc.Toast(
        [html.P("Common Statistics", className="mb-0")],
        header="Common Statistics",)

], style={
    "display": "flex",
    "justify-content": "space-between",
    "margin": "20px"
})


################################  graph area ################################

controls = controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("X variable"),
                dcc.Dropdown(
                    id="xaxis-column",
                    options=[
                        {"label": col, "value": col} for col in df.columns.unique()
                    ],


                ),
            ]
        ),

        html.Div(
            [
                dbc.Label("Y variable"),
                dcc.Dropdown(
                    id="yaxis-column",
                    options=[
                        {"label": col, "value": col} for col in df.columns.unique()
                    ],


                ),
            ]
        ),


    ], body=True,

)


graph_container = dbc.Container(
    [
        html.H1("Country common statistics "),
        html.Div(id="test"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id="indicator-graphic"), md=8),
                dbc.Col(html.Div([
                    dcc.Slider(min=df['Year'].min(), max=df['Year'].max(), step=None, value=df['Year'].max(
                    ), id='year-slider', marks={str(year): str(year) for year in df['Year'].unique()})
                ]))
            ],
            align="center",
        ),
    ],
    fluid=True,
    style={"background": "rgb(249,248,249)", "padding": "40px"}
)


content = html.Div(
    [
        html.Br(),
        common_statistics,
        html.Br(),
        table_row,
        html.Br(),
        graph_container,
        html.Br(),


    ],
    style=CONTENT_STYLE
)

loading_indicator = create_standard_loading_indicator(
    id="loading-output", type="circle", className='spinner-with-text')
sidebar = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(loading_indicator),

        toast,
        html.Br(),
        html.Br(),

    ],
    style=sidebar_STYLE,
)

dataset_monitor_view = [html.Div(children=[
    header,
    sidebar,
    content,


]
)]
