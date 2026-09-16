from agents.job_discovery_agent import JobDiscoveryAgent
from agents.matching_agent import MatchingAgent
from agents.skill_gap_agent import SkillGapAgent
from agents.application_agent import ApplicationAgent


class InternshipOrchestrator:

    def __init__(self):

        print("\nInternship Orchestrator initialized")

        self.job_agent = JobDiscoveryAgent()
        self.matching_agent = MatchingAgent()

        self.skill_gap_agent = SkillGapAgent()
        self.application_agent = ApplicationAgent()

    # =====================================================
    # MAIN AGENTIC WORKFLOW
    # =====================================================

    def process(self, resume_data, internship_query):

        print("\n================================")
        print("STARTING AGENTIC WORKFLOW")
        print("================================")

        # -------------------------------------------------
        # STEP 1: RESUME SKILLS
        # -------------------------------------------------

        resume_skills = resume_data.get(
            "skills",
            []
        )

        print("\n[1] Resume skills detected:")

        for skill in resume_skills:
            print("   -", skill)

        # -------------------------------------------------
        # STEP 2: JOB DISCOVERY
        # -------------------------------------------------

        print("\n[2] Job Discovery Agent")

        jobs = self.job_agent.search_jobs(
            internship_query
        )

        if not jobs:

            print(
                "\nNo internships found."
            )

            return {
                "jobs": [],
                "message":
                    "No internships found for this search."
            }

        print(
            f"\nDiscovered internships: {len(jobs)}"
        )

        # -------------------------------------------------
        # STEP 3: LIMIT JOBS
        # -------------------------------------------------

        # We process the first 10 opportunities
        # to keep the workflow fast.

        jobs = jobs[:10]

        print(
            f"Processing top {len(jobs)} internships..."
        )

        # -------------------------------------------------
        # STEP 4: MATCHING AGENT
        # -------------------------------------------------

        print(
            "\n[3] Matching Agent"
        )

        results = []

        for job in jobs:

            print(
                "\nAnalyzing:",
                job.get("title")
            )

            match_result = (
                self.matching_agent.calculate_match(
                    resume_skills,
                    job.get(
                        "description",
                        ""
                    ),
                    job.get(
                        "title",
                        ""
                    )
                )
            )

            results.append({

                "job": job,

                "match": match_result
            })

            print(
                "Match Score:",
                match_result.get(
                    "score",
                    0
                )
            )

        # -------------------------------------------------
        # STEP 5: RANKING AGENT
        # -------------------------------------------------

        print(
            "\n[4] Ranking internships"
        )

        results.sort(
            key=lambda item:
                item["match"].get(
                    "score",
                    0
                ),
            reverse=True
        )

        # -------------------------------------------------
        # ADD RANK
        # -------------------------------------------------

        for index, result in enumerate(
            results,
            start=1
        ):

            result["rank"] = index

        # -------------------------------------------------
        # PRINT FINAL RANKING
        # -------------------------------------------------

        print(
            "\n================================"
        )

        print(
            "FINAL INTERNSHIP RANKING"
        )

        print(
            "================================"
        )

        for result in results:

            job = result["job"]
            match = result["match"]

            print(
                f"\n#{result['rank']} "
                f"{job.get('title')}"
            )

            print(
                "Company:",
                job.get(
                    "company"
                )
            )

            print(
                "Match Score:",
                match.get(
                    "score",
                    0
                ),
                "%"
            )

            print(
                "Matched:",
                match.get(
                    "matched_skills",
                    []
                )
            )

            print(
                "Missing:",
                match.get(
                    "missing_skills",
                    []
                )
            )

        print(
            "\n================================"
        )

        print(
            "AGENTIC WORKFLOW COMPLETED"
        )

        print(
            "================================"
        )

        return {

            "jobs":
                results,

            "message":
                "Internships discovered, matched and ranked successfully."
        }