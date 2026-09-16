import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


class ApplicationAgent:

    def __init__(self):

        self.client = None

        api_key = os.getenv("GEMINI_API_KEY")

        if api_key:
            try:
                self.client = genai.Client(
                    api_key=api_key
                )
                print("Application Agent initialized")
            except Exception as e:
                print("Gemini initialization failed:", e)
        else:
            print("Application Agent initialized without Gemini")

    def prepare_application(
        self,
        resume_data,
        job,
        match_result
    ):

        print("\nApplication Agent started")

        # --------------------------------
        # LOCAL FALLBACK
        # --------------------------------

        fallback_result = {

            "why_you_are_a_good_fit":
                self.create_fit_message(
                    resume_data,
                    match_result
                ),

            "skills_to_highlight":
                match_result.get(
                    "matched_skills",
                    []
                ),

            "resume_improvements":
                self.create_resume_improvements(
                    match_result
                ),

            "cover_letter":
                self.create_cover_letter(
                    resume_data,
                    job,
                    match_result
                ),

            "application_checklist": [

                "Review the internship requirements.",

                "Check that your resume matches the job.",

                "Highlight the matched skills.",

                "Attach the latest resume.",

                "Review the cover letter.",

                "Submit the application.",

                "Save the application link and date."
            ]
        }

        # --------------------------------
        # GEMINI
        # --------------------------------

        if not self.client:

            print(
                "Gemini unavailable. "
                "Using local application assistant."
            )

            return fallback_result

        prompt = f"""
You are an Internship Application Assistant.

STUDENT RESUME:
{json.dumps(resume_data, indent=2)}

JOB:
{json.dumps(job, indent=2)}

MATCH RESULT:
{json.dumps(match_result, indent=2)}

Create personalized application guidance.

Return ONLY valid JSON:

{{
    "why_you_are_a_good_fit": "",
    "skills_to_highlight": [],
    "resume_improvements": [],
    "cover_letter": "",
    "application_checklist": []
}}

Rules:

1. Use only information provided in the resume.
2. Never invent skills or experience.
3. Keep the cover letter professional and suitable
   for a college student.
4. Mention the actual internship and company.
5. Keep the answer concise.
"""

        try:

            print("Calling Gemini for application preparation...")

            response = self.client.models.generate_content(

                model="gemini-3.6-flash",

                contents=prompt,

                config=types.GenerateContentConfig(

                    response_mime_type="application/json",

                    response_schema={

                        "type": "object",

                        "properties": {

                            "why_you_are_a_good_fit":
                                {"type": "string"},

                            "skills_to_highlight":
                                {
                                    "type": "array",
                                    "items":
                                        {"type": "string"}
                                },

                            "resume_improvements":
                                {
                                    "type": "array",
                                    "items":
                                        {"type": "string"}
                                },

                            "cover_letter":
                                {"type": "string"},

                            "application_checklist":
                                {
                                    "type": "array",
                                    "items":
                                        {"type": "string"}
                                }
                        },

                        "required": [
                            "why_you_are_a_good_fit",
                            "skills_to_highlight",
                            "resume_improvements",
                            "cover_letter",
                            "application_checklist"
                        ]
                    }
                )
            )

            result = json.loads(response.text)

            print(
                "Application Agent completed successfully."
            )

            return result

        except Exception as e:

            print(
                "Gemini application generation failed:"
            )

            print(e)

            print(
                "Using local application assistant."
            )

            return fallback_result

    # --------------------------------
    # LOCAL FUNCTIONS
    # --------------------------------

    def create_fit_message(
        self,
        resume_data,
        match_result
    ):

        matched = match_result.get(
            "matched_skills",
            []
        )

        if matched:

            skills = ", ".join(matched)

            return (
                "Your resume matches this internship "
                f"through skills such as {skills}."
            )

        return (
            "Your resume has been evaluated against "
            "the internship requirements."
        )

    def create_resume_improvements(
        self,
        match_result
    ):

        missing = match_result.get(
            "missing_skills",
            []
        )

        suggestions = []

        if missing:

            for skill in missing[:5]:

                suggestions.append(
                    f"Consider learning or demonstrating "
                    f"{skill} if it is relevant to your career goals."
                )

        suggestions.append(
            "Keep your resume focused on skills relevant "
            "to the internship."
        )

        suggestions.append(
            "Add measurable results to projects or experience "
            "where applicable."
        )

        return suggestions

    def create_cover_letter(
        self,
        resume_data,
        job,
        match_result
    ):

        job_title = job.get(
            "title",
            "this internship"
        )

        company = job.get(
            "company",
            "your organization"
        )

        matched = match_result.get(
            "matched_skills",
            []
        )

        skills_text = ", ".join(
            matched[:5]
        )

        return f"""Dear Hiring Manager,

I am writing to express my interest in the {job_title}
position at {company}.

My background includes experience and skills relevant
to this opportunity. Some of the skills matching the
role include {skills_text if skills_text else "relevant technical and professional skills"}.

I am eager to learn, contribute to your team, and gain
practical industry experience through this internship.

Thank you for considering my application.

Sincerely,
Candidate
"""