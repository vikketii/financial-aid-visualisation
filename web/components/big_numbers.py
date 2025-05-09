import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from dash import html


def create_big_numbers(uni_data, year, benefit):
    filtered_data = uni_data.loc[
        (uni_data["vuosi"] == year) & (uni_data["etuus"].isin(benefit))
    ]

    x = (filtered_data["average"] - filtered_data["index_fixed_average"]).values

    difference = []
    for i, _ in enumerate(benefit):
        difference.append(f"{benefit[i]}: {x[i]:.2f}€")

    return dbc.Row(
        [
            html.Div(
                f"Difference between average and index fixed value (baseline is 2018, chosen year is {year})"
            ),
            html.Div([html.Div(diff) for diff in difference]),
        ]
    )
