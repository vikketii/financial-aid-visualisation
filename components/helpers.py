import pandas as pd
import plotly.colors as palette


def get_index_starting(year):
    df = pd.read_csv("data/kuluttajahintaindeksi-vuodet.csv")

    ratio = 100 / float(
        df.loc[df["vuosi"] == year]["pisteluku"].iloc[0].replace(",", ".")
    )

    result = df["pisteluku"].transform(
        lambda x: float(x.replace(",", ".")) * ratio / 100
    )[year - 2005 :]

    return result


def hex_to_rgb(hex):
    h = hex.lstrip("#")
    l = [int(h[i : i + 2], 16) for i in (0, 2, 4)]
    return f"{l[0]},{l[1]},{l[2]},"


def get_colors(year):
    colors = []

    for i in range(10):
        color = []

        for j in range(10):
            if j == year - 2018:
                color.append(f"rgba({hex_to_rgb(palette.qualitative.Plotly[i])}1)")
            else:
                color.append(f"rgba({hex_to_rgb(palette.qualitative.Plotly[i])}0.6)")

        colors.append(color)

    result = {
        "Opintolainan valtiontakaus": colors[0],
        "Asumislisä": colors[1],
        "Opintoraha": colors[2],
    }

    return result


def get_inflation_adjusted(data):
    index = get_index_starting(2018)

    result = index * data.iloc[0]

    return result
