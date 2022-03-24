import logging
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from app import header, sidebar_STYLE, CONTENT_STYLE
 

df = pd.read_csv('./data/datafake.csv')
 
table_col1 = dbc.Card([
    dbc.CardBody([      
        dash_table.DataTable(
            id='dataset_table',
            columns= [{"name": i, "id": i} for i in df.columns],
            data              =df.to_dict('records'), 
            editable          = False,
            filter_action     = "native",
            sort_action       = "native",
            sort_mode         = "multi",
            column_selectable = "single",
            row_selectable    = "single",
            row_deletable     = False,
            export_columns ='all',
            export_format="csv",
            export_headers='display',
            selected_columns  = [],
            selected_rows     = [],
            page_action       = "native",
            style_table       = {'overflowX': 'auto'},
            page_current      = 0,
            page_size         = 10,
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
                'color':'#545454'
              
            },
            css=[{"selector": ".show-hide", "rule": "display: none"}]
        
        ),  
           
    ]),
])


table_row  = dbc.Row([
                 dbc.Col(table_col1, width = {'size': 12, 'order': 1, 'offset': 0})
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
    
], className="p-3 bg-light rounded-3", style={"margin-top":"50px"})

                                  
content = html.Div(
    [ 
        html.Br(),
        common_statistics,
        html.Br(),
        table_row,
        html.Br(), 
        html.Br(),
        
        
    ],
    style=CONTENT_STYLE
)

 

sidebar = html.Div(
    [
        html.Br(),
        
        
    ],
    style=sidebar_STYLE,
)


dataset_monitor_view = [html.Div(children = 
    [
        header, 
        sidebar,
        content,
               
    ]
)]  