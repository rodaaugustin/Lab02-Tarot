# This creates the page for displaying data visualizations.

import plotly.express as px
import streamlit as st
import json
import pandas as pd

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈🔮")

# PART 1: GRAPHS FROM data.json

with open("data.json","r") as f:
    data = json.load(f)

df = pd.DataFrame(data["data_points"])

st.subheader("My Tarot Data")
st.write(df)

    
fig = px.pie(df, names="suit", title="Tarot Cards by Suit")
st.plotly_chart(fig)

st.subheader("Ratings by Suit")

st.radio("Pick a suit:", ["Major Arcana", "Cups", "Wands", "Swords", "Pentacles"], key="chosen_suit")

filtered = df[df["suit"] == st.session_state.chosen_suit]

st.bar_chart(filtered, x="label", y="value")

# PART 2: GRAPHS FROM data.csv

df2 = pd.read_csv("data.csv")

st.subheader("Survey Results")
st.write(df2)

fig2 = px.histogram(df2, x="Card", title="Which Tarot Card Are People?")
fig2.update_layout(xaxis_title="Tarot Card", yaxis_title="Number of People")
st.plotly_chart(fig2)


st.subheader("Explore by Reading Experience")

st.radio("Have they had a tarot reading?", ["Yes", "No", "No but I want to try"], key="chosen_reading")

filtered2 = df2[df2["Reading"] == st.session_state.chosen_reading]


fig3 = px.pie(filtered2, names="Card", title="Cards Picked by This Group")
st.plotly_chart(fig3)


#AVERAGE

current_avg = round(filtered2["Belief"].mean(), 1)

if "prev_avg" not in st.session_state:
    st.session_state.prev_avg = current_avg

change = current_avg - st.session_state.prev_avg

st.metric("Average Belief Rating", current_avg, delta=round(change, 1))

st.session_state.prev_avg = current_avg


#MEDIAN

current_median = round(filtered2["Belief"].median(), 1)

if "prev_median" not in st.session_state:
    st.session_state.prev_median = current_median

change = current_median - st.session_state.prev_median

st.metric("Median Belief Rating", current_median, delta=round(change, 1))

st.session_state.prev_median = current_median


