# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🔮",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Welcome to My Tarot Dashboard! ✨")

# INTRODUCTORY TEXT
st.write("""
Tarot is a 78-card deck of illustrated cards used to reflect on life, explore choices, and gain personal guidance.
It is split into two sections: 22 Major Arcana cards and 56 Minor Arcana cards,
which are divided into 4 suits (Cups, Wands, Swords, and Pentacles).

My app shows my ratings of different cards, and collects survey answers!
I picked this because I love tarot cards, and I always enjoy learning and doing tarot!

### How to use this app:
- **Survey Page**: Take a quick quiz to find out which tarot card you are, and share your opinion on tarot!
- **Visuals Page**: See my tarot card ratings by suit, which cards survey takers picked, and how much each group believes in tarot.

This project is part of CS 1301's Lab 2.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
