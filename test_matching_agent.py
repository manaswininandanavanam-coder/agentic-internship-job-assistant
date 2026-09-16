from agents.matching_agent import MatchingAgent


agent = MatchingAgent()


resume_skills = [
    "Python",
    "Machine Learning",
    "SQL"
]


job_description = """
We are looking for an AI/ML intern.

Required skills:
Python
Machine Learning
SQL
Generative AI
Deep Learning

Experience with AI projects is preferred.
"""


result = agent.calculate_match(
    resume_skills,
    job_description
)


print("\n==============================")
print("INTELLIGENT MATCHING AGENT")
print("==============================")


print(
    "Match Score:",
    result["score"],
    "%"
)


print(
    "Required Skills:",
    result["required_skills"]
)


print(
    "Matched Skills:",
    result["matched_skills"]
)


print(
    "Missing Skills:",
    result["missing_skills"]
)