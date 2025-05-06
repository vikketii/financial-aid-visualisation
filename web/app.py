import dash_bootstrap_components as dbc
import pandas as pd
from components.bargraph import create_bargraph
from components.map import create_map
from components.timeline import create_timeline
from dash import Dash, Input, Output, dcc, html

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

uni_data = pd.read_csv("../data/uni_data_2018_2024.csv")


timeline = create_timeline()
# bargraph = create_bargraph(uni_data, 2020)
# choropleth_map = create_map(uni_data, 2020)


app.layout = dbc.Container(
    [
        html.H1("Financial aid for Finnish university students 2018-2024"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Description text box hey!"),
                        html.Div(timeline),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dcc.Graph(id="bargraph"),
                        html.H2("BIG numbers here"),
                    ],
                    width=5,
                ),
                dbc.Col(dcc.Graph(id="choropleth_map"), width=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

server = app.server


@app.callback(
    Output("bargraph", "figure"),
    [Input("timeline", "active_item")],
)
def make_graph(year):
    return create_bargraph(uni_data, year)


@app.callback(
    Output("choropleth_map", "figure"),
    [Input("timeline", "active_item")],
)
def make_map(year):
    return create_map(uni_data, year)


if __name__ == "__main__":
    app.run(debug=True, port=4321)
