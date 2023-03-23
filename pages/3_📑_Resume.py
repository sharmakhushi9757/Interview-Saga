import streamlit as st
from PIL import Image
import base64
import numpy as np


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



@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="10% 10%",
    margin_top="10%",
    image_width="30%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo("Images/logo1.png")
st.title("We will help you to build your resume")


tab1, tab2 = st.tabs(["📝 Reume Builder", "🔍 Resume Score Checker"])

with tab1:
   st.header("We will help you to Build your Resume.")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)



with tab2:
   st.header("We will Score your Resume.")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   st.wite()
   st.wite()
   st.wite()
   col1, col2 = st.columns([2, 2])
   data = np.random.randn(10, 1)

   col1.subheader("A wide column with a chart")
   col1.line_chart(data)

   col2.subheader("A narrow column with the data")
   col2.write(data)





