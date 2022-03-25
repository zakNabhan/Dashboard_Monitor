import dash

import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP], prevent_initial_callbacks=True)

server = app.server

app.config.suppress_callback_exceptions = True
dataset_app = "/data_set_view"

# the style arguments for the _sidebar.
sidebar_STYLE = {
    'background-color': '#f2f2f2'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '8%',
    'margin-right': '8%',
    'padding': '1px 1px'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

dropmenu = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active=True, href="/")),
    ]
)

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            html.Img(
                                src=app.get_asset_url("images/test.jpg"),
                                className="logo"
                            ),
                            href="/",
                        )
                    ),
                    dbc.Col(dbc.NavbarBrand("Dataset Dashboard"),
                            style={"font-weight": "700"}),
                ],

            ),
            dbc.Row(
                dbc.Col(
                    [
                        dbc.NavbarToggler(id="navbar-toggler"),
                        dbc.Collapse(
                            dbc.Nav(
                                [dbc.NavItem(dropmenu), ],
                                className="ml-auto",
                                navbar=True,
                            ),
                            id="navbar-collapse",
                            navbar=True,
                        ),
                    ]
                ),
                align="center",
            ),
        ],
        fluid=True,
    ),
    color="rgb(204, 0, 0)",
    dark=True,
    className="mb-5",
    fixed="top",
)
