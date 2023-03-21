import streamlit as st
from PIL import Image

def main():
    im = Image.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRkkCVpx0nGSVSN9A8xA-VBtnM617YKCWbvg&usqp=CAU")
    st.set_page_config(
    page_title="INTERVIEW SAGA",
    page_icon=im,
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
