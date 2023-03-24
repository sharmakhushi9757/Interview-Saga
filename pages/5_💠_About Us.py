import streamlit as st

from PIL import Image
import base64


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

st.title("About Us")
d="Our prime objective is to develop full fledged website application that helps people to get information about the interview preparation of different organisation.Creating a platform to get access about most frequent asked in technology jobs. We help you polish your skills and get ready for the job, whether you are a fresher college graduate or a working professional." 

st.markdown(d)
st.subheader("Our key features are :")
col1, col2, col3 = st.columns(3)
with col1:
   st.image("Images/prepp.jpeg",caption='Summarised Question Set')

with col2:
   st.image("Images/resm.jpeg",caption='Resume Building')

with col3:
   st.image("Images/mock.jpeg",caption='Mock Interviews')

