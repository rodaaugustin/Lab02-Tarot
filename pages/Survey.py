# This creates the page for users to input data.
# The collected data is added to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE
st.title("Which Tarot Card Are You? 🔮")
st.write("Answer 3 quick questions. No tarot knowledge needed!")

# SURVEY FORM
with st.form("survey_form"):
    card_input = st.radio(
        "Which tarot card are you?",
        [
            "The Fool - free and adventurous",
            "The Magician - creative and makes things happen",
            "The Empress - caring and nurturing",
            "The Hermit - thoughtful and loves alone time",
            "The Sun - cheerful and positive",
        ],
    )

    reading_input = st.radio(
        "Have you ever had a tarot reading?",
        ["Yes", "No", "No but I want to try"],
    )

    belief_input = st.slider("How much do you believe tarot can give good advice?", 1, 10)

    submitted = st.form_submit_button("Submit")

    
    if submitted:
        card_name = card_input.split(" - ")[0]

        with open("data.csv", "a") as f:
            f.write(f"{card_name},{reading_input},{belief_input}\n")

        st.success("Your answers have been saved!")


# SHOW CURRENT DATA
st.divider()
st.header("Current Data in CSV")

if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    current_data_df = pd.read_csv("data.csv")
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
