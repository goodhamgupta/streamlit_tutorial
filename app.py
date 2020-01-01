import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px


@st.cache
def get_data():
    return pd.read_csv(
        "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    )


df = get_data()
st.title("Streamlit Experiment")
st.markdown("Exploring new your city listing data")
st.dataframe(df.head(10))

st.header("Our regulation and news coverage")
st.subheader("On a map")
st.map(df)
df["index"] = np.random.randint(3)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.title("Number of regulations by country/location")
st.deck_gl_chart(
    viewport={"latitude": 37.76, "longitude": -122.4, "zoom": 11, "pitch": 50,},
    layers=[
        {
            "type": "HexagonLayer",
            "data": df,
            "radius": 200,
            "elevationScale": 4,
            "elevationRange": [0, 1000],
            "pickable": True,
            "extruded": True,
        },
        {"type": "ScatterplotLayer", "data": df,},
    ],
)
