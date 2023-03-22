import streamlit as st
from PIL import Image

def main():
    st.set_page_config(
    page_title="INTERVIEW SAGA",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/sharmakhushi9757',
        'Report a bug': "https://github.com/sharmakhushi9757",
        'About': "sharmakhushi9757"
    }
)
    col1,mid,col2=st.beta_columns([1,1,20])
    with col1:
      st.image('logo main.png', width=60)
    with col2:
      st.title("INTERVIEW SAGA")
    
    st.write("Welcome to my app!")

if __name__ == "__main__":
    main()
