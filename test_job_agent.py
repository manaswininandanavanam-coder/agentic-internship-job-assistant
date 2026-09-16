from agents.job_discovery_agent import JobDiscoveryAgent


agent = JobDiscoveryAgent()


jobs = agent.search_jobs(
    "AI ML internship"
)


print("\n==============================")
print("REAL JOB DISCOVERY RESULTS")
print("==============================")


if not jobs:

    print("No jobs found.")


else:

    for job in jobs:

        print("\nJob Title:", job["title"])

        print(
            "Company:",
            job["company"]
        )

        print(
            "Location:",
            job["location"]
        )

        print(
            "Description:",
            job["description"][:200],
            "..."
        )

        print(
            "Apply:",
            job["apply_url"]
        )