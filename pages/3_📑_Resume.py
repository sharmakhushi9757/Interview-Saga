import streamlit as st
from PIL import Image
import base64
import pandas as pd
from io import StringIO
import numpy as np
import webbrowser

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


st.title("The Ultimate Resume Builder & Score Checker")



tab1, tab2 = st.tabs(["📝 Reume Builder", "🔍 Resume Score Checker"])

with tab1:
   st.header("We will help you to Build your Resume.")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
   
   resume_data="For most job-seekers, a good resume is what stands between a dream job and Choice D. Get your resume right, and you’ll be getting replies from every other company you apply to.If your resume game is weak, though, you’ll end up sitting around for weeks, maybe even months, before you even get a single response.So you’re probably wondering how you can write a resume that leads to HR managers inviting you to interviews daily.Well, you’ve come to the right place!In this guide, we’re going to teach you everything you need to know about how to make a resume, including:"
   st.markdown(resume_data)
   st.markdown(f'<h3 style="background-color:#F5F5F5;">{"✔️ How to Write a Resume in 9 Steps:"}</h3>', unsafe_allow_html=True)
   st.write('''<style>
   [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border: 2px black;
    }
    </style>''',unsafe_allow_html=True)
   
   with st.container():
       st.write("1. Pick the Right Resume Format & Layout")
       st.write("2. Mention Your Personal Details & Contact Information")
       st.write("3. Use a Resume Summary or Objective")
       st.write("4. List Your Work Experience & Achievements")
       st.write("5. Mention Your Top Soft & Hard Skills")
       st.write("6. Include Additional Resume Sections (Languages, Hobbies, etc.)")
       st.write("7. Tailor Your Information For the Job Ad")
       st.write("8. Craft a Convincing Cover Letter")
       st.write("9. Proofread Your Resume and Cover Letter")
   st.subheader("📄 How to Make a Resume (The Right Way!)")
   st.markdown("Before we go into detail about how you should make a resume, here’s a summary of the most important steps and tips to keep in mind: ")
   expander = st.expander("See Sample Resume")
   expander.image("Images/resumeexample.png")
   st.markdown("1. **Choose a resume format carefully.** In 99% of the cases, we recommend the chronological format. ")
   st.markdown("2. **Add the right contact details.** Leave your headshot out and make sure to include your job title, a professional email address, and relevant links (e.g. your LinkedIn profile, online portfolio, website, etc.). ")
   st.markdown("3. **Write an impactful resume summary.** Unless you’re an entry-level professional, always go for a resume summary (also known as a career summary). Done right, it’s your chance to get hiring managers to go through the rest of your resume in detail. ")
   st.markdown("4. **Pay attention to your work experience section.** Take your work experience section from OK-ish to exceptional by tailoring it to the job ad, making your achievements quantifiable, and using action verbs and power words. ")
   st.markdown("5. **Add the right skills for the job.** Keep this important section relevant by only including soft and hard skills that are required for the position. Deeper into the article, we’ll show you just how to do that!  ")
   st.markdown("6. **Keep your education short and to the point.** Your most recent and highest degree is more than enough for a strong education section. We recommend making a more detailed education section only if you’re a recent graduate with barely any work experience. ")
   st.markdown("7. **Take advantage of optional resume sections.** Optional sections like languages, hobbies, certifications, independent projects, and the sorts, can be what sets you apart from other candidates with similar skills and experience.")
   st.markdown("8. **Don’t forget about the cover letter.** Cover letters do matter in 2023 so you should definitely include one. To make the most out of your cover letter, check out this detailed guide on how to write a cover letter.")
   def get_st_button_a_tag(url_link, button_name):
        """
        generate html a tag
        :param url_link:
        :param button_name:
        :return:
        """
        return f'''
        <a href={url_link}><button style="
        fontWeight: 400;
        padding: 0.25rem 0.75rem;
        borderRadius: 0.25rem;
        margin: 0px;
        text-align: center;
        lineHeight: 1.6;
        width: auto;
        userSelect: none;
        backgroundColor: #FFFFFF;
        border: 1px solid rgba(49, 51, 63, 0.2);">{button_name}</button></a>
        '''

   st.markdown(get_st_button_a_tag('https://novoresume.com/resume-templates', 'Browse Templates'), unsafe_allow_html=True) 
  



with tab2:
   st.header("Check Your Resume Score")

   col1, col2 = st.columns(2)
   with col1:
       st.markdown("Are you not getting enough interview calls? 📞")
       st.markdown("Check your Resume's compatibility & get your Report in just 30 sec. ⌛")
       st.markdown("This is your chance to get 2X more interview calls. ")
   with col2:
       st.image("https://learning-static.storage.googleapis.com/rs/s/shine-resume/images/score-checker/parameters-image.png")
  

   st.subheader("How Resume Checker Works?")
   data="When you upload your resume, our AI-powered system analyzes it against key criteria required as per the Industry standards and commit an overall score to your resume. Our resume checker it gives you the fair idea of the resume quality and how it represents you in front of recruiters & hiring manager. We also provide you a detailed resume review and ways to increase the score further. You can also reach out to our professional resume experts to perfect your resume score. "
   st.markdown(data)
   st.image("Images/rr.png")
   
   def get_st_button_a_tag(url_link, button_name):
    """
    generate html a tag
    :param url_link:
    :param button_name:
    :return:
    """
    return f'''
    <a href={url_link}><button style="
    fontWeight: 400;
    padding: 0.25rem 0.75rem;
    borderRadius: 0.25rem;
    margin: 0px;
    text-align: center;
    lineHeight: 1.6;
    width: auto;
    userSelect: none;
    backgroundColor: #FFFFFF;
    border: 1px solid rgba(49, 51, 63, 0.2);">{button_name}</button></a>
    '''

   st.markdown(get_st_button_a_tag('https://resumeworded.com/upload-resume', 'Upload Resume'), unsafe_allow_html=True) 
  
        
    
        
    
  
  



