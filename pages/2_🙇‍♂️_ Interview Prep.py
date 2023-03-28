import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
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



st.title("Prep")

st.subheader("🧑‍💻 Tech Set :")

options = st.multiselect(
    'Select Companies :',
    ['Accenture', 'Wipro', 'TCS', 'Capgemini','Cognizant','Nagarro','Sumsung','Amazon','Goldman Sachs','Infosys'],
    ['Accenture', 'Capgemini'])
df4=pd.read_csv('final_file/sumsung_add_file_tech.csv')
df=pd.DataFrame()
if 'Sumsung' in options:
    df=pd.concat([df,df4])
    df = df.reset_index(drop=True)
df=df.reset_index(drop=True)
st.write(df,index=False)

st.subheader("🧑‍🏫 HR Set  :")

options_set = st.multiselect(
    'Select Companies :',
    ['Accenture ', 'Wipro ', 'TCS ', 'Capgemini ','Cognizant ','Nagarro ','Sumsung ','Amazon ','Goldman Sachs ','Infosys '],
    ['Accenture ', 'Capgemini '])
df_4=pd.read_csv('final_file/sumsung_add_file_hr.csv')
df_0=pd.DataFrame()
if 'Sumsung ' in options_set:
    df_0=pd.concat([df_0,df_4])
    df_0 = df_0.reset_index(drop=True)
df_0=df_0.reset_index(drop=True)
st.write(df_0,index=False)
