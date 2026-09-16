from agents.job_discovery_agent import JobDiscoveryAgent
from agents.matching_agent import MatchingAgent


# Create agents
job_agent = JobDiscoveryAgent()
matching_agent = MatchingAgent()


# Temporary resume skills
# Later these will come automatically from Resume Agent
resume_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "Flask"
]


# Search real internships
jobs = job_agent.search_jobs(
    "AI ML internship"
)


print("\n==============================")
print("AI INTERNSHIP MATCHING SYSTEM")
print("==============================")


if not jobs:

    print("No jobs found.")

else:

    for job in jobs:

        result = matching_agent.calculate_match(
            resume_skills,
            job["description"]
        )


        print("\n------------------------------")

        print("Job Title:")
        print(job["title"])

        print("Company:")
        print(job["company"])

        print("Location:")
        print(job["location"])

        print("Match Score:")
        print(result["score"], "%")

        print("Matched Skills:")
        print(result["matched_skills"])

        print("Missing Skills:")
        print(result["missing_skills"])

        print("Apply:")
        print(job["apply_url"])