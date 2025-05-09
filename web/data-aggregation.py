import pandas as pd


def get_index_starting(year):
    df = pd.read_csv("../data/kuluttajahintaindeksi-vuodet.csv")

    ratio = 100 / float(
        df.loc[df["vuosi"] == year]["pisteluku"].iloc[0].replace(",", ".")
    )

    df["pisteluku"] = df["pisteluku"].transform(
        lambda x: float(x.replace(",", ".")) * ratio / 100
    )

    return df.loc[df["vuosi"] > 2017]


uni_data = pd.read_csv("../data/uni_data_2018_2024.csv")
filtered_data = uni_data.loc[(uni_data["aikatyyppi"] == "Vuosi")]


sums = filtered_data.groupby(
    [filtered_data["vuosi"], filtered_data["etuus"]], as_index=False
).sum(numeric_only=True)

sums["average"] = sums["maksettu_laskenta_eur"] / sums["saaja_laskenta_lkm"]

sums["overall_change"] = sums.groupby("etuus")["average"].transform(
    lambda x: x - x.iloc[0]
)

sums["change"] = sums.groupby("etuus")["average"].pct_change() * 100


index_values = get_index_starting(2018)
index_values = index_values.reset_index(drop=True)


sums = sums.merge(index_values, on="vuosi", how="left")

sums["index_fixed_average"] = sums.groupby("etuus")["average"].transform(
    lambda x: x.iloc[0] * sums["pisteluku"]
)


print(sums.head(10))

# write
# sums.to_csv("../data/evaluated_data_2018_2024.csv")
