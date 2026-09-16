import os

from agents.resume_agent import ResumeAgent


# ==========================================
# INITIALIZE AGENT
# ==========================================

resume_agent = ResumeAgent()


# ==========================================
# FIND PDF INSIDE uploads FOLDER
# ==========================================

uploads_folder = "uploads"

pdf_files = [
    file
    for file in os.listdir(uploads_folder)
    if file.lower().endswith(".pdf")
]


if not pdf_files:

    print("\nERROR: No PDF found inside uploads folder.")

    print("\nPlease put your resume PDF here:")

    print(
        os.path.abspath(uploads_folder)
    )

    exit()


# Use the first PDF found

resume_path = os.path.join(
    uploads_folder,
    pdf_files[0]
)


print("\n================================")
print("RESUME FILE")
print("================================")

print(resume_path)


# ==========================================
# EXTRACT TEXT
# ==========================================

print("\n================================")
print("EXTRACTING RESUME TEXT")
print("================================")


resume_text = resume_agent.extract_text(
    resume_path
)


print("\nResume text extracted successfully.")


# ==========================================
# LOCAL ANALYSIS
# ==========================================

print("\n================================")
print("ANALYZING ACTUAL RESUME")
print("================================")


# IMPORTANT:
# We use LOCAL analysis for this test.
# This avoids Gemini quota / 503 problems.

result = resume_agent.analyze_resume_local(
    resume_text
)


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n================================")
print("RESUME ANALYSIS RESULT")
print("================================")


print("\nName:")
print(result.get("name", ""))


print("\nSkills:")

for skill in result.get("skills", []):

    print(" -", skill)


print("\nEducation:")

for item in result.get("education", []):

    print(" -", item)


print("\nExperience:")

for item in result.get("experience", []):

    print(" -", item)


print("\nProjects:")

for item in result.get("projects", []):

    print(" -", item)


print("\nCertifications:")

for item in result.get("certifications", []):

    print(" -", item)


print("\n================================")
print("TEST COMPLETED")
print("================================")