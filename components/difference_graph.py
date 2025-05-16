import plotly.graph_objects as go

from components.helpers import get_colors, get_translation


def create_difference_graph(uni_data, year=2018, benefit=["opintoraha"]):
    uni_data = uni_data.loc[uni_data["etuus"].isin(benefit)]

    colors = get_colors(year)

    bargraph = go.Figure()

    for id, (name, group) in enumerate(uni_data.groupby("etuus")):
        bargraph.add_trace(
            go.Bar(
                x=group["vuosi"],
                y=group["change"],
                name=get_translation(name),
                marker_color=colors[name],
                showlegend=True,
            )
        )

    bargraph.update_layout(
        legend_title_text="Benefit",
        title_text="Change in average financial aid compared to previous year",
        yaxis_title_text="Change %",
    )

    return bargraph
