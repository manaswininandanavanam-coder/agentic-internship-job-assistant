from agents.matching_agent import MatchingAgent


agent = MatchingAgent()


resume_skills = [
    "Python",
    "SQL",
    "Flask",
    "Machine Learning"
]


job_description = """
We are looking for a Software Developer Intern.

Requirements:

Python
SQL
Git
Docker
Flask
JavaScript
"""


result = agent.calculate_match(
    resume_skills,
    job_description
)


print("\n==============================")
print("MATCHING RESULT")
print("==============================")

print("Score:", result["score"])

print("Matched Skills:")
print(result["matched_skills"])

print("Missing Skills:")
print(result["missing_skills"])

print("Required Skills:")
print(result["required_skills"])