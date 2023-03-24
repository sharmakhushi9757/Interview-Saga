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




st.header("Everything you need to crack your next interview")
st.subheader(":blue[Now!! All available at one place]")
st.sidebar.success("Select a page above.")
st.image("Images/backk.png")


cc1,cc2,cc3=st.columns(3)
with cc1:
    st.image("https://i.pinimg.com/564x/56/65/a1/5665a13e627cef12d66e88a2ed1cb019.jpg",caption="Practice Set")
with cc2:
    st.image("https://i.pinimg.com/564x/43/83/4c/43834c4236b7fd1d4e799f55ce32df9e.jpg",caption="Resume Building")
with cc3:
    st.image("https://i.pinimg.com/564x/c1/49/a0/c149a096cc84eb5972743be15b952f68.jpg",caption="Mock Interview")


st.write("**Our Users Have cracked interviews at :**")

cl1,cl2,cl3,cl4,cl5=st.columns(5)
with cl1:
    st.image("https://i.pinimg.com/474x/f4/46/99/f44699e42fa39104aee1063aa2eb09f5.jpg")
with cl2:
    st.image("https://i.pinimg.com/474x/53/b0/e6/53b0e6c332aa9cb17300f14c2c053a95.jpg")
with cl3:
    st.image("https://i.pinimg.com/474x/cf/5b/81/cf5b81678e89560e7757aefccc50f629.jpg")
with cl4:
    st.image("data:image/png;base64,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")
with cl5:
    st.image("data:image/jpeg;base64,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")
 
    
