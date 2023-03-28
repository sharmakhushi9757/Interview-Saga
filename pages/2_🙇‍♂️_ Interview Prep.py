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
st.snow()
st.subheader("🧑‍💻 Tech Set :")
with st.container():
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
            st.markdown("1.Coding Round \n 2. Technical Interview 1 \n 3. Technical Interview 2\n 4. HR Round")
            st.markdown("\n")
            st.markdown("***Academic Criteria:***")
            st.markdown("1. 70 percent or above in B.Tech, Class X, Class XII \n 2. No backlogs at the time of interview")
        with c2:
            st.image("data:image/jpeg;base64,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")
st.markdown("---")



    
