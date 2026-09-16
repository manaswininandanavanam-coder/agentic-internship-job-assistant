from agents.application_agent import ApplicationAgent


# Create Application Agent
agent = ApplicationAgent()


# --------------------------------
# SAMPLE RESUME DATA
# --------------------------------

resume_data = {

    "name": "John Doe",

    "skills": [
        "Python",
        "Machine Learning",
        "SQL",
        "Flask"
    ],

    "education": [
        "B.Tech in Computer Science"
    ],

    "experience": [
        "Python Intern"
    ],

    "projects": [
        "AI Resume Analyzer"
    ],

    "certifications": [
        "Machine Learning Certification"
    ]
}


# --------------------------------
# SAMPLE JOB
# --------------------------------

job = {

    "title": "AI/ML Intern",

    "company": "Example Technologies",

    "location": "Hyderabad",

    "description": """
    We are looking for an AI/ML intern.

    Required skills:
    Python
    Machine Learning
    SQL
    Flask
    Generative AI
    """,

    "apply_url": "https://example.com/apply"
}


# --------------------------------
# MATCHING RESULT
# --------------------------------

match_result = {

    "score": 80,

    "matched_skills": [
        "python",
        "machine learning",
        "sql",
        "flask"
    ],

    "missing_skills": [
        "generative ai"
    ],

    "required_skills": [
        "Python",
        "Machine Learning",
        "SQL",
        "Flask",
        "Generative AI"
    ]
}


# --------------------------------
# APPLICATION AGENT
# --------------------------------

result = agent.prepare_application(

    resume_data,

    job,

    match_result

)


# --------------------------------
# DISPLAY RESULT
# --------------------------------

print("\n======================================")
print("APPLICATION AGENT RESULT")
print("======================================")


print("\nWhy You Are a Good Fit:")
print("--------------------------------------")

print(
    result["why_you_are_a_good_fit"]
)


print("\nSkills to Highlight:")
print("--------------------------------------")

for skill in result["skills_to_highlight"]:

    print("-", skill)


print("\nResume Improvements:")
print("--------------------------------------")

for improvement in result["resume_improvements"]:

    print("-", improvement)


print("\nCover Letter:")
print("--------------------------------------")

print(
    result["cover_letter"]
)


print("\nApplication Checklist:")
print("--------------------------------------")

for item in result["application_checklist"]:

    print("-", item)


print("\n======================================")
print("APPLICATION AGENT TEST COMPLETED")
print("======================================")