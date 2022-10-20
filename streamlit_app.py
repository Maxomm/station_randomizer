import random

import pandas as pd
import streamlit as st


def translate_tarif(opt):
    return "A|B|C" if opt == "ABC" else "A|B" if opt == "AB" else "A"


dfcsv = pd.read_csv("berlin_stations.csv")

if __name__ == "__main__":
    st.title("Berlin Stations")
    option = st.selectbox("Tarifbereich", ("ABC", "AB", "A"))
    random_button = st.button("Random Station")

    col1, col2 = st.columns(2)
    with col1: next_station_text = st.subheader(" ")
    with col2: trains = st.subheader(" ")

    filt = dfcsv[dfcsv["area"].str.contains(translate_tarif(option))]
    maps = st.map(filt[["latitude", "longitude"]])

    if random_button:
        rnd_st = random.randrange(0, len(filt))
        next_station_text.subheader(filt["name"].iloc[rnd_st])
        trains.subheader(filt["trains"].iloc[rnd_st])
        lat = filt["latitude"].iloc[rnd_st]
        lon = filt["longitude"].iloc[rnd_st]
        maps.map(pd.DataFrame({"latitude": [lat], "longitude": [lon]}))

    with st.expander("All Stations"):
        st.dataframe(dfcsv, 1000, 1000)
