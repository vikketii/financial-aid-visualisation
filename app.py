import json

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, Input, Output, dcc, html

from components.bargraph import create_bargraph
from components.big_numbers import create_big_numbers
from components.difference_graph import create_difference_graph
from components.helpers import get_translation
from components.map import create_map
from components.timeline import create_timeline

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

uni_data = pd.read_csv("data/evaluated_data_2018_2024.csv")
uni_data_full = pd.read_csv("data/uni_data_2018_2024_years.csv")


uni_data = uni_data.loc[
    (uni_data["etuus"] == "Opintoraha")
    | (uni_data["etuus"] == "Opintolainan valtiontakaus")
    | (uni_data["etuus"] == "Asumislisä")
]

benefits = {}
for i in uni_data["etuus"].unique():
    benefits[i] = get_translation(i)

timeline = create_timeline()

app.layout = dbc.Container(
    [
        html.H1("Financial aid for Finnish university students 2018-2024"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Timeline"),
                        html.Div(
                            "Timeline of changes for Finnish financial aid for students"
                        ),
                        html.Div(timeline),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dcc.Graph(id="bargraph"),
                        dcc.Graph(id="difference_graph"),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            benefits,
                            ["Opintoraha"],
                            id="dropdown_selector",
                            multi=True,
                        ),
                        html.P(),
                        html.Div("Difference between average and index fixed value"),
                        html.Div(id="big_numbers"),
                    ]
                ),
                # dbc.Col(dcc.Graph(id="choropleth_map"), width=4),
            ],
            align="start",
        ),
    ],
    fluid=True,
)

server = app.server


@app.callback(Output("timeline", "children"), Input("bargraph", "clickData"))
def select_year_from_graph(clickData):
    if not clickData:
        return create_timeline()

    return create_timeline(clickData["points"][0]["x"])


@app.callback(
    Output("bargraph", "figure"),
    [Input("timeline", "active_item")],
    [Input("dropdown_selector", "value")],
)
def update_bargraph(year, benefit):
    if not isinstance(year, int):
        return
    return create_bargraph(uni_data, year=year, benefit=benefit)


@app.callback(
    Output("difference_graph", "figure"),
    [Input("timeline", "active_item")],
    [Input("dropdown_selector", "value")],
)
def update_differencegraph(year, benefit):
    if not isinstance(year, int):
        return
    return create_difference_graph(uni_data, year=year, benefit=benefit)


# @app.callback(
#     Output("choropleth_map", "figure"),
#     [Input("timeline", "active_item")],
#     [Input("dropdown_selector", "value")],
# )
# def update_map(year, benefit):
#     return create_map(uni_data_full, year=year, benefit=benefit)


@app.callback(
    Output("big_numbers", "children"),
    [Input("timeline", "active_item")],
    [Input("dropdown_selector", "value")],
)
def update_big_numbers(year, benefit):
    if not isinstance(year, int):
        return
    return create_big_numbers(uni_data, year=year, benefit=benefit)


if __name__ == "__main__":
    app.run(debug=True, port=4321)
