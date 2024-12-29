import streamlit as st
from streamlit_page import sidebar , main_content

if "groq_api_key" not in st.session_state:
    st.session_state["groq_api_key"] = None

if "resume_content" not in st.session_state:
    st.session_state["resume_content"] = None

if "job_description" not in st.session_state:
    st.session_state["job_description"] = None

st.title("Resume Matcher")

groq_api_key = st.sidebar.text_input("Enter Groq API key")

st.session_state["groq_api_key"] = groq_api_key

sidebar()

main_content()