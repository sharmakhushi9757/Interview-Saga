import streamlit as st
im=Image.open('Images/prep.png')
st.set_page_config(page_title=“Interview Prep”,
layout=“wide”,
initial_sidebar_state=“auto”,
multi_app_icon=im,
ordering=1
)

st.title("Projects")

st.write("You have entered", st.session_state["my_input"])
