import dash_bootstrap_components as dbc
from dash import html

from components.helpers import get_translation


def create_big_numbers(uni_data, year, benefit):
    filtered_data = uni_data.loc[
        (uni_data["vuosi"] == year) & (uni_data["etuus"].isin(benefit))
    ]

    filtered_data.assign(difference=lambda x: x["average"] - x["index_fixed_average"])
    x = (filtered_data["average"] - filtered_data["index_fixed_average"]).values
    # y = filtered_data["average"] - filtered_data["index_fixed_average"]

    # print(filtered_data.head())

    difference = []
    for i, _ in enumerate(benefit):
        difference.append(f"{get_translation(benefit[i])}: {x[i]:.2f}€")

    return dbc.Row(
        [
            html.Div(f"Baseline 2018, chosen year {year}.", style={"height": "2em"}),
            html.Div(
                [html.Div(diff) for diff in difference], style={"fontSize": "1.2em"}
            ),
        ]
    )
