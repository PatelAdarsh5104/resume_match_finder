import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq



# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY"),
# )


def match_resume(resume, job_description,groq_api_key):
    prompt = f"""
    You are an advanced AI resume and job description matching tool. Your task is to analyze both a resume and a job description to determine how well the resume aligns with the job description.

    Given the following inputs:

    Resume: {resume}
    Job Description: {job_description}

    ### Task 1: Overall Match Percentage
    - Analyze the resume and job description to provide a **match percentage** reflecting how well the resume aligns with the job description. Consider skills, qualifications, experience, education, and overall relevance.

    ### Task 2: In-Depth Match Breakdown
    - Provide a **breakdown** of the match between the resume and the job description in the following areas:
        - **Skills Match**: How well do the skills in the resume align with those in the job description?
        - **Experience Match**: Does the resume reflect the required job experience for the position?
        - **Education/Certifications Match**: Does the candidate's education and certifications align with the job requirements?
        - **Key Responsibilities Match**: Does the resume reflect the key responsibilities required for the role?
        - **Additional Factors Match**: Does the resume demonstrate other relevant qualities (e.g., leadership, cultural fit)?

    For each category, provide a **percentage** match.

    ### Personalization
    - Ensure the analysis is **personalized** to the job description, considering industry-specific terminology and requirements.

    Please format your results as follows:

    1. **Overall Match Percentage:** X%
    2. **Skills Match:** X%
    3. **Experience Match:** X%
    4. **Education Match:** X%
    5. **Key Responsibilities Match:** X%
    6. **Additional Factors Match:** X%
    """

    client = Groq(api_key=groq_api_key)

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
    )
    output = chat_completion.choices[0].message.content

    return output



def suggestion_resume(resume, job_description,groq_api_key):
    prompt = f"""
    You are an experienced recruiter specializing in helping candidates optimize their resumes for Applicant Tracking Systems (ATS). Your task is to analyze a resume and job description, then provide keyword and content suggestions to help the resume pass through ATS filters and increase the chances of being noticed by recruiters.

    Given the following inputs:

    Resume: {resume}
    Job Description: {job_description}

    ### Task 1: Keyword Suggestions
    - Analyze the job description and identify key **keywords** and **phrases** commonly searched for by ATS, including **skills**, **certifications**, **tools**, **technologies**, and **role-specific terms**.
    - Suggest **keywords** to be added or emphasized in the resume to improve ATS compatibility.
    - Provide tips on how to effectively incorporate these keywords.

    ### Task 2: Content and Customization Suggestions
    - Suggest **content** that could be added to make the resume more ATS-friendly:
        - If certain skills or qualifications are underrepresented, suggest adding them based on the job description.
        - Advise on tailoring the **summary**, **work experience**, and **education** sections to better align with the job description.

    ### Personalization
    - Ensure all suggestions are **tailored** to the specific job description, industry, and role.

    Please format your results as follows:

    1. **Keyword Suggestions**:
        - Keyword: [Explanation of why it’s relevant]

    2. **Content and Customization Suggestions**:
        - Suggestion: [Description]
    """

    client = Groq(api_key=groq_api_key)
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
    )
    output = chat_completion.choices[0].message.content
    return output