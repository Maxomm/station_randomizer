import streamlit as st
import random
import pandas as pd


def translate_tarif(input):
    return "A|B|C" if input == "ABC" else "A|B" if input == "AB" else "A"


if __name__ == "__main__":
    dfcsv = pd.read_csv("berlin_stations.csv")
    st.title("Berlin Stations")

    option = st.selectbox("Tarifbereich", ("ABC", "AB", "A"))
    random_button = st.button("Random Station")

    col1, col2 = st.columns(2)
    with col1:
        next_station_text = st.subheader(" ")
    with col2:
        anbindung = st.subheader(" ")

    if random_button:
        filt = dfcsv[dfcsv["Tarifbereich"].str.contains(translate_tarif(option))]
        random_station = random.randrange(0, len(filt))
        next_station_text.subheader(filt["Name"].iloc[random_station])
        anbindung.subheader(filt["Anbindung"].iloc[random_station])

    # st.text("All Stations")
    st.empty()
    with st.expander("All Stations"):
        st.dataframe(dfcsv, 1000, 1000)
