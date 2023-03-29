import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import time
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
st.subheader("🧑‍💻 Technical Question Set :")
with st.container():
    options = st.multiselect(
    'Select Companies :',
    ['Accenture', 'Wipro', 'TCS', 'Capgemini','Cognizant','Nagarro','Sumsung','Amazon','Goldman Sachs','Infosys'],
    ['Accenture', 'Capgemini'])
    df4=pd.read_csv('final_file/sumsung_add_file_tech.csv')
    df3=pd.read_csv('final_file/accenture_add_file.csv')
    df2=pd.read_csv('final_file/wipro_add_file.csv')
    df=pd.DataFrame()
    if 'Wipro' in options:
        df=pd.concat([df,df2])
        df = df.reset_index(drop=True)
    if 'Sumsung' in options:
        df=pd.concat([df,df4])
        df = df.reset_index(drop=True)
    if 'Accenture' in options:
        df=pd.concat([df,df3])
        df = df.reset_index(drop=True)
    df=df.reset_index(drop=True)
    st.write(df,index=False)
    



st.subheader("🧑‍🏫 HR Question Set  :")

with st.container():
    options = st.multiselect(
    'Select Companies :',
    ['accenture', 'wipro', 'tcs', 'capgemini','cognizant','nagarro','sumsung','amazon','goldman sachs','infosys'],
    ['accenture', 'capgemini'])
    df4=pd.read_csv('final_file/sumsung_add_file_hr.csv')
    df=pd.DataFrame()
    if 'sumsung' in options:
        df=pd.concat([df,df4])
        df = df.reset_index(drop=True)
    df=df.reset_index(drop=True)
    if df is not st.empty():
        st.write(df,index=False)
st.subheader("⭕ Recruitment Process & Interview Tips")
with st.container():
    option = st.multiselect(
    'Select Company:',
    ['accenture_process', 'wipro_process', 'tcs_process', 'capgemini_process','cognizant_process','nagarro_process','sumsung_process','amazon_process','goldmanSachs_process','infosys_process'])
    if 'sumsung_process' in option:
        c1,c2=st.columns(2)
        with c1:
            st.markdown("***Samsung conducts 3-4 rounds to select freshers as a Software Engineer in their organisation.***")
            st.markdown("\n 1. Coding Round \n 2. Technical Interview 1 \n 3. Technical Interview 2\n 4. HR Round")
            st.markdown("\n")
            st.markdown("***Academic Criteria:***")
            st.markdown("1. 70 percent or above in B.Tech, Class X, Class XII \n 2. No backlogs at the time of interview")
        with c2:
            st.image("http://lofrev.net/wp-content/photos/2016/06/samsung-logo-45.jpg")
        st.markdown("---")
    if 'accenture_process' in option:
        c1,c2=st.columns(2)
        with c1:
            st.markdown("***Accenture conducts 3-4 rounds to select freshers as SDE in their organisation.***")
            st.markdown("\n 1. Aptitude test \n 2. Technical Interview \n 3. HR Interview 2\n")
            st.markdown("\n")
            st.markdown("***Academic Criteria:***")
            st.markdown("1. 70 percent or above in B.Tech, Class X, Class XII \n 2. No backlogs at the time of interview")
        with c2:
            st.image("data:image/png;base64,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")
        st.markdown("---")




    
