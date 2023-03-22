import streamlit as st
from PIL import Image

image = Image.open('Images/page icon1.png')
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
st.title("Main Page")
st.sidebar.success("Select a page above.")

im1=Image.open('Images/home.png')
st.set_page_config(page_title="Home",
layout="wide",
initial_sidebar_state="auto",
multi_app_icon=im1,
ordering=1
)

im=Image.open('Images/prep.png')
st.set_page_config(page_title="Interview Prep",
layout="wide",
initial_sidebar_state="auto",
multi_app_icon=im,
ordering=2
)

im2=Image.open('Images/resume.png')
st.set_page_config(page_title="Resume",
layout="wide",
initial_sidebar_state="auto",
multi_app_icon=im2,
ordering=3
)

im3=Image.open('Images/mockiw.png')
st.set_page_config(page_title="Mock Interview",
layout="wide",
initial_sidebar_state="auto",
multi_app_icon=im3,
ordering=4
)

im4=Image.open('Images/about.png')
st.set_page_config(page_title="About",
layout="wide",
initial_sidebar_state="auto",
multi_app_icon=im4,
ordering=5
)

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
