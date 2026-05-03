# AI Resume Analyzer

## Project Overview

This project is an AI-powered Resume Analyzer built using Python and Streamlit.  
The application analyzes resumes against job descriptions and provides ATS-based improvement suggestions using Large Language Models (LLMs).

The system helps users understand:

- Resume match percentage
- Missing skills
- ATS optimization tips
- Resume improvements
- Better resume bullet points
- Interview preparation suggestions

The application uses a ChatGPT-style conversational interface for interactive resume analysis.

---

# Features

- Resume upload (PDF)
- Job description comparison
- ATS score analysis
- Missing skill identification
- AI-powered resume suggestions
- ChatGPT-style interface
- Conversation history support
- Resume improvement guidance
- Interview preparation assistance

---

# Problem Statement

Many job seekers face problems such as:

- Resume rejection by ATS systems
- Missing important keywords
- Weak project descriptions
- Poor resume formatting
- Skill mismatch with job roles

This project solves these problems by analyzing resumes intelligently and providing AI-based optimization suggestions.

---

# Use Cases

- Resume optimization
- ATS score improvement
- Skill gap analysis
- Career guidance
- Interview preparation
- Recruitment assistance

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| Groq API / OpenAI API | AI-powered resume analysis |
| PyPDF2 | Resume PDF text extraction |
| python-dotenv | Secure API key management |
| Session State | Maintain conversation history |

---

# Project Structure

```plaintext
resume_analyzer/
│
├── app.py
├── parser.py
├── requirements.txt
├── .env
└── README.md
````
#steps to run the app

# Steps to Run the Project

1. Clone the repository using `git clone <your_repo_link>` and move into the project folder using `cd resume_analyzer`.

2. Create a virtual environment using `python -m venv venv`.

3. Activate the virtual environment using `venv\Scripts\activate` for Windows or `source venv/bin/activate` for Mac/Linux.

4. Install all required libraries using `pip install -r requirements.txt`.

5. Create a `.env` file inside the project folder and add your API key as `GROQ_API_KEY=your_api_key`.

6. Run the application using `streamlit run app.py`.

7. Open the browser and visit `http://localhost:8501` to use the application.
