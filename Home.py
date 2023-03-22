import streamlit as st
from PIL import Image

image = Image.open('Images/page icon1.png')
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

title_container = st.beta_container()
        col1, col2 = st.beta_columns([1, 20])
        im = Image.open('home.png')
        with title_container:
            with col1:
                st.image(im, width=64)
            with col2:
                st.title("Main Page")
 

st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
