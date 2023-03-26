import streamlit as st
from PIL import Image
import pandas as pd
import base64
import datetime


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


st.title("Schedule your mock interview here!!")

import streamlit as st

with st.form("Book Your Interview Here!!",clear_on_submit=True):
   firstname = st.text_input("First Name :")
   lastname = st.text_input("Last Name :")
   mail=st.text_input("Enter Email :")
   sch=st.date_input("Enter Day :")
   tm=st.time_input("Enter Time :",datetime.time(8, 45))
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("Congrts!! you have booked your interview on :" ,sch,"at",tm,"You will receive further details via mail.")
       st.write("**Fill this form for conformtion :**")
       with st.form("details",clear_on_submit=True):
            Education = st.text_input("Enter Highest Qualification :")
            Experience = st.number_input("Enter Experience (in numbers) :")
            Role = st.selectbox('Select Role',('Software Developer', 'Data Science', 'Data Analytics','Python Developer','Java Developer'))
            book=st.form_submit_button("Book")
        

    
            

