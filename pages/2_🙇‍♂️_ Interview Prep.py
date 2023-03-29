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
    if 'wipro_process' in option:
        c1,c2=st.columns(2)
        with c1:
            st.markdown("***Wipro conducts 3 rounds to recruit new employees.***")
            st.markdown("\n 1. Online test \n 2. Technical Interview \n 3. HR Interview 2\n")
            st.markdown("\n")
            st.markdown("***Academic Criteria:***")
            st.markdown("1. 60 percent or above in B.Tech, Class X, Class XII \n 2. One backlogs at the time of interview allowed")
        with c2:
            st.image("data:image/jpeg;base64,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8uMxuo+4iJDkREQEREBERAREQEREBERAREQEREBERAREQIjNMe2GYKtuL3IvN7CVvXRWItcXn1Ww6V/xKDbyJ5iKy4ZGYjZQTYe3iebDDPHyZZZZbnyfh0tlkknLNaR2CytMG7OCSWuN+AL3Npp5dn36VUCMmnVfSQb8C9jt4EnpWGfj82spzozxz8W8bxtX8wzSvQxK01S6HT2JLX5IPAt/ibme5qMpph9OoltIF7C9idz22EkrTFisNTxa6XUMp7EXEqY5TfPfX6b742zc4nf7aeVZn+saHqhSD8w03vuOwPeV3pjqDE5hiTTezKQxIC20W4+19rHfeXChQTDKFRQqjgAWELTC3IABPMrV45bPJhJlPXvr9KZnHQ36wxJqitpRzqddN27agpvbf34v3l1RbADxPqcwzHrzE+s3pCmtNSQAyliQDyTcc82HHvOnbphj5f6jWM+RP/EHOKuWU6aUmKGoWu45AW2wPYnVz7GV7orP8QMUlJ6j1EqEghmLkGxYMCdxxuOJcRRodXYRGqIQHFxY/MrC6tpNvII43HaeZF0ph8lcuhd3sQGcg6QedIUAD68zdzS8fJ48PFcMsf5crFPYiS8RERAREQEREBERAREQEREBERAREQEREBERAREQPJjq0xVUqwuCCCPaZZ5Ms2IvBZNSwbal1E9tRvb6TW6pxdTC010ErqaxYcjY7e1/PtJwTHUprVBVgCDyCLj+s5ZeGTC44cOuPlvvMs+dK70njauJ1q7FlUKQTuQTfa/fzMvU2eNlWlUUF2BN2uQBxwDuT/iTlCglAWRQo8AAD+kj84yWnmwGosrLwy2vvyNxYiTjhlh49S7rr/c8eXm9rjrH8MHTWctmytrUB1Iva9iDexseODK31rjqy19AZlUKpAUlb35Jtzvt9pb8nymnlSEJcljcsbXP5TJjsto5hb1UVrcX5H0I3nT1yuOreW4+Xx4ea5ScIbofG1cZQb1CW0tpVjuSLA2J728+8jMx+H64mqXSuaaMSSujURfchW1Cw+oNpdMPh0wyhUUKo4AFhM0vHcjn/fyxzuWHG2pl2CTLqS0kFlQWH+Sfcm5+824ia4W23dexEQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERA//9k=")
        st.markdown("---")
    if 'capgemini_process' in option:
        c1,c2=st.columns(2)
        with c1:
            st.markdown("***Wipro conducts 3 rounds to recruit new employees.***")
            st.markdown("\n 1. Aptitude and Essay Round \n 2. Technical Aptitude Round \n 3. Technical Interview \n 4. HR Interview 2\n")
            st.markdown("\n")
            st.markdown("***Academic Criteria:***")
            st.markdown("1. 65 percent or above in B.Tech, Class X, Class XII \n 2. No backlogs at the time of interview.")
        with c2:
            st.image("Images/Capgemini.png")
        st.markdown("---")




    
