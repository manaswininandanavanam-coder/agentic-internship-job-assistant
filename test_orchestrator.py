from agents.orchestrator import InternshipOrchestrator


print("ORCHESTRATOR TEST STARTED")

orchestrator = InternshipOrchestrator()

print("Orchestrator created")


resume_data = {
    "name": "John Doe",
    "skills": [
        "Python",
        "SQL",
        "Flask",
        "Machine Learning"
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


internship_query = "AI ML internship"


result = orchestrator.process(
    resume_data,
    internship_query
)


print("\n==============================")
print("FINAL AGENTIC AI RESULTS")
print("==============================")

print("Message:")
print(result["message"])

print("\nTotal Jobs:")
print(len(result["jobs"]))


for item in result["jobs"]:

    job = item["job"]
    match = item["match"]

    print("\n--------------------------------")
    print("Rank:", item["rank"])
    print("Title:", job["title"])
    print("Company:", job["company"])
    print("Location:", job["location"])

    print("Match Score:", match["score"])

    print("Matched Skills:")
    print(match["matched_skills"])

    print("Missing Skills:")
    print(match["missing_skills"])

    print("Apply URL:")
    print(job["apply_url"])

print("\n==============================")
print("ORCHESTRATOR TEST COMPLETED")
print("==============================")