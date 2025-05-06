import plotly.graph_objects as go


def get_colors(year):
    colors = [
        [
            "rgba(20,120,20,0.6)",
        ]
        * 10,
        [
            "rgba(20,20,120,0.6)",
        ]
        * 10,
    ]

    colors[0][year - 2018] = "rgba(20,120,20,1)"
    colors[1][year - 2018] = "rgba(20,20,120,1)"

    return colors


def evaluate_change(uni_data, year):
    filtered_data = uni_data.loc[
        (uni_data["aikatyyppi"] == "Vuosi")
        & (uni_data["etuus"] != "Opintoraha ja asumislisä yhteensä")
        & (uni_data["etuus"] != "Yhteensä")
        & (uni_data["etuus"] != "Asumislisä")
    ]

    sums = filtered_data.groupby(
        [filtered_data["vuosi"], filtered_data["etuus"]], as_index=False
    ).sum(numeric_only=True)

    sums["average"] = sums["maksettu_laskenta_eur"] / sums["saaja_laskenta_lkm"]

    sums["overall_change"] = sums.groupby("etuus")["average"].transform(
        lambda x: x - x.iloc[0]
    )

    sums["change"] = sums.groupby("etuus")["average"].pct_change() * 100

    return sums


def create_bargraph(uni_data, year):

    colors = get_colors(year)

    bargraph = go.Figure()

    evaluated_data = evaluate_change(uni_data, year)

    for id, (name, group) in enumerate(evaluated_data.groupby("etuus")):
        # fig.add_trace(go.Bar(x=group["Fruit"], y=group["Number Eaten"], name=name,
        # hovertemplate="Contestant=%s<br>Fruit=%%{x}<br>Number Eaten=%%{y}<extra></extra>"% contestant))
        bargraph.add_trace(
            go.Bar(
                x=group["vuosi"],
                y=group["average"],
                # y=group["maksettu_laskenta_eur"],
                name=name,
                marker_color=colors[id],
            )
        )

    bargraph.update_layout(
        legend_title_text="etuus",
        title_text="Change % on average financial aid",
        yaxis_title_text="Change %",
    )

    # bargraph = px.bar(
    #     sums,
    #     x="vuosi",
    #     y="maksettu_laskenta_eur",
    #     color="etuus",
    #     title="Financial aid received (total by year)",
    #     labels={"vuosi": "year", "maksettu_laskenta_eur": "total amount (billion)"},
    # )

    return bargraph
