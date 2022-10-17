import streamlit as st
import random

if __name__ == "__main__":
    with open("station_list.txt", "r", encoding="utf8") as file:
        stations = file.readlines()
    st.title("Stations Test")
    if st.button('Random Station'):
        random_station = random.randrange(0,len(stations))
        st.text(stations[random_station])