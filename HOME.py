# Core Pkgs
import streamlit as st 
from JobRecommendation.side_logo import add_logo
from JobRecommendation.sidebar import sidebar
import altair as alt
import plotly.express as px 
from streamlit_extras.switch_page_button import switch_page
from JobRecommendation.lottie_animation import load_lottieurl
# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime
from streamlit_lottie import st_lottie


st.set_page_config(layout="centered", page_icon='logo/logo2.png', page_title="HOMEPAGE")



url = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_m075yjya.json")

add_logo()
sidebar()


st.markdown("<h1 style='text-align: center; font-family: Verdana, sans-serif; padding: 20px; border: 2px solid #758283; border-radius: 5px;'>Welcome to BUDDY !</h1>", unsafe_allow_html=True)

st.markdown("<div style='background-color: rgba(255, 0, 0, 0); padding: 10px;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-family: Verdana, sans-serif; padding: 20px;'>WHAT WE OFFER : </h2>", unsafe_allow_html=True)

s1,s2, s3 = st.columns(3)
with s1:

    candidate = st.button("BootCamps")
    if candidate:
        switch_page("Bootcamp")
    st.balloons()

with s2:
        analyzer = st.button("Resume Analyzer")
        if analyzer:
            switch_page("resume analyzer")
        st.balloons()

with s3:
        recruiter = st.button("Mentors")
        if recruiter:
            switch_page("🧑🏻\u200d🏫🧑🏻\u200d🏫mentors")
        st.balloons()



# st.image('logo/TALENTHIVE.png', use_column_width="auto")
st.markdown("</div>", unsafe_allow_html=True)
st_lottie(url)

# Project Description Section
st.markdown("<h2 style='text-align: center; font-family: Verdana, sans-serif; padding: 20px;'>Why BUDDY ?</h2>", unsafe_allow_html=True)
st.write("<p style='font-size:20px;'>Buddy simplifies career growth. We bring candidates, and mentors together in one platform. Access personalized mentorship. Buddy empowers you to take control of your career journey and unlock your full potential.</p>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-family: Verdana, sans-serif; padding: 20px;'>AIM</h2>", unsafe_allow_html=True)
st.write("<p style='font-size:20px;'>At Buddy, our vision is clear: to transform the landscape of career development. We are committed to providing an all-encompassing platform that connects candidates with the personalized mentorship and guidance for their career aspirations.By seamlessly bridging the gap between candidates, and mentors, we aspire to cultivate a supportive ecosystem where individuals can flourish and achieve their professional aspirations. Our mission is to empower individuals to make informed career decisions, discover meaningful opportunities, and ultimately realize their full potential", unsafe_allow_html=True)
st.write("<p style='font-size:20px;'>What sets us apart is our extensive use of cutting-edge AI technology, which enables us to deliver AI-based suggestions for the perfect resume, and our advanced algorithms, which ensure that every interaction is tailored to meet the unique needs of our users.With Buddy, the future of career development shines bright. Join us on this exciting journey as we pave the way for a new era in professional growth and success!", unsafe_allow_html=True)

# Set footer config

# # Set footer config
# footer = "<div style='background-color: #758283; padding: 10px; color: white; text-align: center; position: absolute; bottom: 0; width: 100%;'>© 2023 TalentHive</div>"
# st.markdown(footer, unsafe_allow_html=True)


# Create a container for the footer
footer_container = st.container()

# Add content to the footer container
with footer_container:

    st.write(" ", unsafe_allow_html=True)