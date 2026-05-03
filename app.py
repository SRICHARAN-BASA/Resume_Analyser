import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from parser import extract_resume
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit page config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.caption("ChatGPT-style Resume Analysis Assistant")

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

# Sidebar
with st.sidebar:

    st.header("Upload Resume")

    uploaded_resume = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_resume:
        st.session_state.resume_text = extract_resume(
            uploaded_resume
        )

        st.success("Resume Uploaded Successfully")

    st.header("Job Description")

    jd = st.text_area(
        "Paste Job Description"
    )

    if jd:
        st.session_state.job_description = jd

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
prompt = st.chat_input(
    "Ask about your resume..."
)

if prompt:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    # System Prompt
    system_prompt = f"""
    You are an expert AI Resume Analyzer and ATS optimization assistant.

    Analyze the resume and compare it with the job description.

    Resume:
    {st.session_state.resume_text}

    Job Description:
    {st.session_state.job_description}

    Help the user with:
    - ATS score analysis
    - Skill gap identification
    - Resume improvement suggestions
    - Better resume bullet points
    - Resume summary improvement
    - Interview preparation questions
    - Career suggestions
    """

    # AI Response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            }
        ] + st.session_state.messages,
        temperature=0.7,
        max_tokens=2048
    )

    reply = response.choices[0].message.content

    # Store Assistant Reply
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    # Display Assistant Reply
    with st.chat_message("assistant"):
        st.markdown(reply)