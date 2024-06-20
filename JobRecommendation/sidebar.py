import streamlit as st

# Set sidebar config
def sidebar():
    st.sidebar.title("About us")
    st.sidebar.subheader("Through seamless integration of technology and human connections, Buddy empowers individuals to thrive in a digitally interconnected world.")
    text_string_variable1=("Made By Shubhi")
    url_string_variable1=("https://www.linkedin.com/in/shubhi-shrotriya-190573162/")
    link = f'[{text_string_variable1}]({url_string_variable1})'
    st.sidebar.markdown(link, unsafe_allow_html=True)

