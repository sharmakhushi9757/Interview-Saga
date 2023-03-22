import streamlit as st
from PIL import Image



def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

'''
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
    
    st.title("INTERVIEW SAGA")
    st.sidebar.markdown("# HOME PAGE ")
    def HOME_PAGE():
        st.markdown("# HOME APGE 🎈")
        st.sidebar.markdown("# HOME PAGE 🎈")
    def page2():
        st.markdown("# Page 2 ❄️")
        st.sidebar.markdown("# Page 2 ❄️")
    def page3():
        st.markdown("# Page 3 🎉")
        st.sidebar.markdown("# Page 3 🎉")
    page_names_to_funcs = {
    "HOME PAGE": HOME_PAGE,
    "Page 2": page2,
    "Page 3": page3,
}
    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()'''
