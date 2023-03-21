import streamlit as st
from PIL import Image

def main():
    icon=Image.open("https://icons8.com/icon/mjPRxlOl6Wbb/candidate.png")
    st.set_page_config(
    page_title="INTERVIEW SAGA",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/sharmakhushi9757',
        'Report a bug': "https://github.com/sharmakhushi9757",
        'About': "sharmakhushi9757"
    }
)
    st.title("INTERVIEW SAGA")
    st.write("Welcome to my app!")

if __name__ == "__main__":
    main()
