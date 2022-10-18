import streamlit as st
import random
import pandas as pd


def translate_tarif(input):
    return "A|B|C" if input == "ABC" else "A|B" if input == "AB" else "A"


if __name__ == "__main__":
    dfcsv = pd.read_csv("stations_newest.csv")
    st.title("Stations")

    option = st.selectbox("Tarifbereich", ("ABC", "AB", "A"))

    if st.button("Random Station"):
        filt = dfcsv[dfcsv["Tarifbereich"].str.contains(translate_tarif(option))]
        random_station = random.randrange(0, len(filt))
        st.text(filt["Name"].iloc[random_station])

    st.subheader("All Stations")
    st.dataframe(dfcsv, 1000, 200)
