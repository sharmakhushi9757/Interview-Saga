import streamlit as st
from PIL import Image
import base64
import pandas as pd
from io import StringIO
import numpy as np
import webbrowser

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


st.title("The Ultimate Resume Builder & Score Checker")



tab1, tab2 = st.tabs(["📝 Reume Builder", "🔍 Resume Score Checker"])

with tab1:
   st.header("We will help you to Build your Resume.")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)



with tab2:
   st.header("Check Your Resume Score")

   col1, col2 = st.columns(2)
   with col1:
       st.markdown("Are you not getting enough interview calls? 📞")
       st.markdown("Check your Resume's compatibility & get your Report in just 30 sec. ⌛")
       st.markdown("This is your chance to get 2X more interview calls. ")
   with col2:
       st.image("https://learning-static.storage.googleapis.com/rs/s/shine-resume/images/score-checker/parameters-image.png")
  

   st.subheader("How Resume Checker Works?")
   data="When you upload your resume, our AI-powered system analyzes it against key criteria required as per the Industry standards and commit an overall score to your resume. Our resume checker it gives you the fair idea of the resume quality and how it represents you in front of recruiters & hiring manager. We also provide you a detailed resume review and ways to increase the score further. You can also reach out to our professional resume experts to perfect your resume score. "
   st.markdown(data)
   st.image("Images/rr.png")
   
   def get_st_button_a_tag(url_link, button_name):
    """
    generate html a tag
    :param url_link:
    :param button_name:
    :return:
    """
    return f'''
    <a href={url_link}><button style="
    fontWeight: 400;
    padding: 0.25rem 0.75rem;
    borderRadius: 0.25rem;
    margin: 0px;
    text-align: center;
    lineHeight: 1.6;
    width: auto;
    userSelect: none;
    backgroundColor: #FFFFFF;
    border: 1px solid rgba(49, 51, 63, 0.2);">{button_name}</button></a>
    '''

   st.markdown(get_st_button_a_tag('https://resumeworded.com/upload-resume', 'Upload Resume'), unsafe_allow_html=True) 
  
        
    
        
    
  
  



