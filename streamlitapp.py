import streamlit as st

def main():
    
    st.set_page_config(
    page_title="INTERVIEW SAGA",
    page_icon="👀",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/sharmakhushi9757',
        'Report a bug': "https://github.com/sharmakhushi9757",
        'About': "sharmakhushi9757"
    }
)
    
    st.write("Welcome to my app!")

if __name__ == "__main__":
    main()
