import streamlit as st
from PIL import Image

def main():
    #im = Image.open("")
    st.set_page_config(
    page_title="INTERVIEW SAGA",
    page_icon="https://www.flaticon.com/free-icon/interview_3222637?term=interview&page=1&position=3&origin=search&related_id=3222637",
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
