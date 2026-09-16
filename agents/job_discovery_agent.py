import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()


class JobDiscoveryAgent:

    def __init__(self):

        self.app_id = os.getenv("ADZUNA_APP_ID")
        self.app_key = os.getenv("ADZUNA_APP_KEY")

        print("Job Discovery Agent initialized")

    # -------------------------------------------------
    # CLEAN TEXT
    # -------------------------------------------------

    def clean_text(self, text):

        if not text:
            return ""

        text = re.sub(
            r"<[^>]+>",
            " ",
            str(text)
        )

        text = (
            text
            .replace("&amp;", "&")
            .replace("&nbsp;", " ")
            .replace("&quot;", '"')
            .replace("&#39;", "'")
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    # -------------------------------------------------
    # CHECK INTERNSHIP TITLE
    # -------------------------------------------------

    def is_internship(self, job):

        title = self.clean_text(
            job.get("title", "")
        ).lower()

        description = self.clean_text(
            job.get("description", "")
        ).lower()

        # Strong internship indicators
        internship_keywords = [
            "intern",
            "internship",
            "trainee",
            "apprentice",
            "co-op",
            "placement",
            "graduate trainee",
            "student trainee"
        ]

        # Clearly senior roles
        senior_keywords = [
            "senior",
            "sr.",
            "lead",
            "manager",
            "director",
            "principal",
            "staff engineer",
            "head of"
        ]

        # Title is the strongest signal
        if any(
            keyword in title
            for keyword in internship_keywords
        ):
            return True

        # Reject obvious senior jobs
        if any(
            keyword in title
            for keyword in senior_keywords
        ):
            return False

        # Some companies mention internship
        # multiple times in the description.
        count = sum(
            description.count(keyword)
            for keyword in internship_keywords
        )

        return count >= 2

    # -------------------------------------------------
    # CALCULATE QUERY RELEVANCE
    # -------------------------------------------------

    def calculate_relevance(
        self,
        query,
        job
    ):

        query_words = set(
            re.findall(
                r"[a-zA-Z0-9]+",
                query.lower()
            )
        )

        title = self.clean_text(
            job.get("title", "")
        ).lower()

        description = self.clean_text(
            job.get("description", "")
        ).lower()

        score = 0

        # Title matches are more important
        for word in query_words:

            if len(word) < 3:
                continue

            if word in title:
                score += 3

            elif word in description:
                score += 1

        # Internship title bonus
        internship_words = [
            "intern",
            "internship",
            "trainee",
            "apprentice"
        ]

        if any(
            word in title
            for word in internship_words
        ):
            score += 5

        return score

    # -------------------------------------------------
    # SEARCH ADZUNA
    # -------------------------------------------------

    def search_adzuna(
        self,
        search_query,
        page=1
    ):

        url = (
            f"https://api.adzuna.com/v1/api/"
            f"jobs/in/search/{page}"
        )

        params = {

            "app_id":
                self.app_id,

            "app_key":
                self.app_key,

            "what":
                search_query,

            "where":
                "Hyderabad",

            "results_per_page":
                50,

            "content-type":
                "application/json"
        }

        try:

            response = requests.get(
                url,
                params=params,
                timeout=20
            )

            print(
                f"Adzuna page {page} status:",
                response.status_code
            )

            if response.status_code != 200:

                print(
                    response.text
                )

                return []

            return response.json().get(
                "results",
                []
            )

        except Exception as e:

            print(
                "Adzuna request failed:",
                e
            )

            return []

    # -------------------------------------------------
    # MAIN SEARCH FUNCTION
    # -------------------------------------------------

    def search_jobs(self, query):

        print(
            f"\nSearching internships for: {query}"
        )

        if not self.app_id or not self.app_key:

            print(
                "ERROR: Adzuna API credentials missing."
            )

            return []

        query = query.strip()

        if not query:

            return []

        # ---------------------------------------------
        # MULTI-QUERY SEARCH
        # ---------------------------------------------

        search_queries = []

        # Original query
        search_queries.append(
            query
        )

        # Internship-enhanced query
        if "intern" not in query.lower():

            search_queries.append(
                query + " internship"
            )

        # ---------------------------------------------
        # COLLECT RESULTS
        # ---------------------------------------------

        all_results = []

        for search_query in search_queries:

            print(
                f"\nSearching Adzuna for:"
                f" {search_query}"
            )

            # Search first two pages
            for page in [1, 2]:

                results = self.search_adzuna(
                    search_query,
                    page
                )

                all_results.extend(
                    results
                )

        print(
            f"\nTotal raw results:"
            f" {len(all_results)}"
        )

        # ---------------------------------------------
        # CONVERT RESULTS
        # ---------------------------------------------

        jobs = []

        for item in all_results:

            job = {

                "title":
                    self.clean_text(
                        item.get(
                            "title",
                            ""
                        )
                    ),

                "company":
                    item.get(
                        "company",
                        {}
                    ).get(
                        "display_name",
                        ""
                    ),

                "location":
                    item.get(
                        "location",
                        {}
                    ).get(
                        "display_name",
                        ""
                    ),

                "description":
                    self.clean_text(
                        item.get(
                            "description",
                            ""
                        )
                    ),

                "apply_url":
                    item.get(
                        "redirect_url",
                        ""
                    )
            }

            # Only keep actual internships
            if self.is_internship(job):

                job["relevance"] = (
                    self.calculate_relevance(
                        query,
                        job
                    )
                )

                jobs.append(
                    job
                )

        print(
            f"Internships after filtering:"
            f" {len(jobs)}"
        )

        # ---------------------------------------------
        # REMOVE DUPLICATES
        # ---------------------------------------------

        unique_jobs = []

        seen = set()

        for job in jobs:

            key = (
                job["title"].lower()
                + "|"
                + job["company"].lower()
            )

            if key in seen:
                continue

            seen.add(key)

            unique_jobs.append(
                job
            )

        # ---------------------------------------------
        # SORT BY RELEVANCE
        # ---------------------------------------------

        unique_jobs.sort(
            key=lambda x: x.get(
                "relevance",
                0
            ),
            reverse=True
        )

        # Remove internal field before returning
        for job in unique_jobs:

            job.pop(
                "relevance",
                None
            )

        print(
            f"Final unique internships:"
            f" {len(unique_jobs)}"
        )

        return unique_jobs