import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


class LLMService:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )


    def analyze_resume(self, resume_text):

        prompt = f"""
You are an AI Resume Analysis Agent.

Analyze the following resume and extract the important information.

Return ONLY valid JSON in this exact structure:

{{
    "name": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Rules:
- Do not invent information.
- Only use information present in the resume.
- Keep skills as individual items.
- If a section is not available, return an empty list.

Resume:
{resume_text}
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text