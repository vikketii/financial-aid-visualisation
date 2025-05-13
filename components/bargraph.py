import plotly.graph_objects as go

from components.helpers import get_colors


def create_bargraph(uni_data, year=2018, benefit=["opintoraha"]):

    uni_data = uni_data.loc[uni_data["etuus"].isin(benefit)]

    colors = get_colors(year)
    # print(colors)

    bargraph = go.Figure()

    for id, (name, group) in enumerate(uni_data.groupby("etuus")):
        # print(id)
        bargraph.add_trace(
            go.Bar(
                x=group["vuosi"],
                y=group["average"],
                name=name,
                marker_color=colors[name],
            )
        )

        line_colors = ["orange", "yellow"]

        bargraph.add_trace(
            go.Scatter(
                x=group["vuosi"],
                y=group["index_fixed_average"],
                name=f"Inflation adjusted {name}",
                # marker_color=colors[0],
                # line_color=line_colors[id],
                # colors=colors[0],
            )
        )

    bargraph.update_layout(
        legend_title_text="etuus",
        title_text="Financial aid received (monthly average by year)",
        yaxis_title_text="Average €",
    )

    return bargraph
