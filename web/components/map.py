import json

import pandas as pd
import plotly.express as px


def create_map(uni_data, year, benefit):
    with open("../data/municipalities.json") as f:
        municipalities = json.load(f)

    filtered_aid24 = uni_data.loc[
        (uni_data["aikatyyppi"] == "Vuosi")
        & (uni_data["vuosi"] == year)
        & (uni_data["etuus"].isin(benefit))
    ]

    receivers_by_municipality = filtered_aid24.groupby("kunta_nro").sum(
        numeric_only=True
    )

    print(receivers_by_municipality.head(10))

    receivers_by_municipality = pd.DataFrame(
        {
            "kunta_nro": receivers_by_municipality.index,
            "average": receivers_by_municipality["maksettu_laskenta_eur"]
            / receivers_by_municipality["saaja_lkm"],
        }
    )

    choropleth_map = px.choropleth_map(
        receivers_by_municipality,
        geojson=municipalities,
        locations="kunta_nro",
        color="average",
        color_continuous_scale="Greens",
        zoom=3,
        center={"lat": 63.116000, "lon": 24.359000},
    )
    choropleth_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return choropleth_map
