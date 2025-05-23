import plotly.graph_objects as go

from components.helpers import get_colors, get_translation


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
                name=get_translation(name),
                marker_color=colors[name],
                legendgroup="group",
                legendgrouptitle_text="Benefit",
            )
        )

        # line_colors = ["orange", "yellow"]

        bargraph.add_trace(
            go.Scatter(
                x=group["vuosi"],
                y=group["index_fixed_average"],
                name=get_translation(name),
                # marker_color=colors[name],
                line_color=colors[name][0],
                # colors=colors[name],
                legendgroup="group2",
                legendgrouptitle_text="Inflation adjusted",
            )
        )

    bargraph.update_layout(
        # legend_title_text="Benefit",
        title_text="Financial aid received (yearly average)",
        yaxis_title_text="Average €",
        # legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
    )

    return bargraph
