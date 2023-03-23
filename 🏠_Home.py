import streamlit as st
from PIL import Image


image = Image.open('Images/page icon.png')
st.set_page_config(
    page_title="INTERVIEW SAGA",
    page_icon=image,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/sharmakhushi9757',
        'Report a bug': "https://github.com/sharmakhushi9757",
        'About': "sharmakhushi9757"
    }
)

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open('Images/logo1.png')
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logo(logo_path='Images/logo1.png', width=50, height=60)
st.sidebar.image(my_logo)


st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
