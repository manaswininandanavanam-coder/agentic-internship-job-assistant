from agents.resume_agent import ResumeAgent


# ==========================================
# INITIALIZE RESUME AGENT
# ==========================================

resume_agent = ResumeAgent()


# ==========================================
# ACTUAL RESUME PDF
# ==========================================

resume_path = r"C:\Users\manas\OneDrive\Desktop\internship_job_agent\uploads\SowmyaChalla_Resume_General.pdf"


# ==========================================
# EXTRACT TEXT FROM PDF
# ==========================================

resume_text = resume_agent.extract_text(
    resume_path
)


print("\n==============================")
print("EXTRACTED RESUME TEXT")
print("==============================")

print(resume_text)


# ==========================================
# ANALYZE RESUME
# ==========================================

result = resume_agent.analyze_resume(
    resume_text
)


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n==============================")
print("AI RESUME ANALYSIS")
print("==============================")


print("\nName:")
print(result.get("name", ""))


print("\nSkills:")
for skill in result.get("skills", []):
    print(" -", skill)


print("\nEducation:")
for education in result.get("education", []):
    print(" -", education)


print("\nExperience:")
for experience in result.get("experience", []):
    print(" -", experience)


print("\nProjects:")
for project in result.get("projects", []):
    print(" -", project)


print("\nCertifications:")
for certification in result.get("certifications", []):
    print(" -", certification)