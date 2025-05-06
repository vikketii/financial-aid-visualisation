def change_index_baseline(df, year):
    ratio = 100 / float(
        df.loc[df["Vuosi"] == year]["Pisteluku"].iloc[0].replace(",", ".")
    )

    return df["Pisteluku"].transform(lambda x: float(x.replace(",", ".")) * ratio)
