import streamlit as st
from PIL import Image
import base64
import pandas as pd
from io import StringIO
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
st.title("We will help you with your resume.")


tab1, tab2 = st.tabs(["📝 Reume Builder", "🔍 Resume Score Checker"])

with tab1:
   st.header("We will help you to Build your Resume.")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)



with tab2:
   st.header("Check Your Resume Score")
   st.image("https://learning-static.storage.googleapis.com/rs/s/shine-resume/images/score-checker/parameters-image.png")
   st.markdown("Are you not getting enough interview calls? 📞")
   st.markdown("Check your Resume's compatibility & get your Report in just 30 sec. ⌛")
   st.markdown("This is your chance to get 2X more interview calls. ")

   st.subheader("How Resume Checker Works?")
   data="When you upload your resume, our AI-powered system analyzes it against key criteria required as per the Industry standards and commit an overall score to your resume. Our resume checker it gives you the fair idea of the resume quality and how it represents you in front of recruiters & hiring manager. We also provide you a detailed resume review and ways to increase the score further. You can also reach out to our professional resume experts to perfect your resume score. "
   st.markdown(data)
   st.image("Images/rr.png")


   uploaded_file = st.file_uploader("Upload Resume")
   if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
      

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        

        # To read file as string:
        string_data = stringio.read()
       

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        
    
  
  



