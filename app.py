import streamlit as st
from groq import Groq
from parser import extract_resume
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Resume Analyzer")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    resume_text = extract_resume(resume)

    prompt = f"""
    Compare resume with job description.

    Give:

    1. Skill Match Percentage
    2. Missing Skills
    3. Improvement Suggestions
    4. ATS Optimization Tips
    5. Better Resume Bullet Points

    Resume:
    {resume_text}

    Job Description:
    {jd}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content

    st.write(result)
