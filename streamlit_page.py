import streamlit as st
from extract_content import extract_pdf_content, extract_docx_content
from groq_model import match_resume, suggestion_resume

def sidebar():
    st.sidebar.title("Resume Matcher")
    input_type = st.sidebar.selectbox("Input Type", ["PDF", "DOCX"])

    if input_type == "PDF":
        uploaded_file = st.sidebar.file_uploader("Choose an Resume file",type=["pdf"])
        if uploaded_file is not None:
            uploaded_file.read()
            st.session_state.resume_content = extract_pdf_content(uploaded_file)
    elif input_type == "DOCX":
        uploaded_file = st.sidebar.file_uploader("Choose an Resume file",type=["docx"])
        if uploaded_file is not None:
            st.session_state.resume_content = extract_docx_content(uploaded_file)
            st.sidebar.write(st.session_state.resume_content)
            st.toast("Content Extracted from Resume")


def main_content():

    job_description = st.text_input(label="Job Description",placeholder="Enter Job discription here")
    # print("job_description",job_description)

    st.session_state["job_description"] = job_description

    if not st.session_state.groq_api_key:
        st.warning("Please enter your Groq API key!", icon="⚠")
        st.stop() 

    left, right = st.columns(2)

    if st.session_state.get("resume_content") is not None and st.session_state.get("job_description"):
            
            if left.button("Find Matching", type="primary"):
                with st.spinner("Finding Matching..."):
                    result = match_resume(st.session_state.resume_content,st.session_state.job_description,st.session_state.groq_api_key)
                    st.write(result)

            if right.button("Suggestion", type="primary"):
                with st.spinner("Finding Suggestion..."):
                    ans = suggestion_resume(st.session_state.resume_content,job_description,st.session_state.groq_api_key)
                    st.write(ans)