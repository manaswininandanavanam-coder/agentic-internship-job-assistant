import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


class SkillGapAgent:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = None

        if self.api_key:
            try:
                self.client = genai.Client(
                    api_key=self.api_key
                )
            except Exception as e:
                print("Gemini initialization failed:")
                print(e)

        print("Skill Gap Agent initialized")

    # ==========================================================
    # LOCAL FALLBACK
    # ==========================================================

    def analyze_skill_gaps_local(self, missing_skills):

        print("\nUsing LOCAL Skill Gap Analysis...")

        skill_roadmaps = {

            "python": {
                "importance": "High",
                "reason": "Python is widely used in software development, automation, data analysis and AI internships.",
                "learning_steps": [
                    "Learn Python syntax, variables, conditions and loops.",
                    "Practice functions, lists, dictionaries and file handling.",
                    "Build small Python projects.",
                    "Practice Python interview problems."
                ]
            },

            "sql": {
                "importance": "High",
                "reason": "SQL is important for working with databases and analyzing structured data.",
                "learning_steps": [
                    "Learn SELECT, WHERE, ORDER BY and GROUP BY.",
                    "Practice JOIN operations.",
                    "Learn aggregate functions and subqueries.",
                    "Solve SQL interview problems."
                ]
            },

            "javascript": {
                "importance": "High",
                "reason": "JavaScript is commonly required for frontend and full-stack development.",
                "learning_steps": [
                    "Learn variables, functions and arrays.",
                    "Understand DOM manipulation.",
                    "Learn asynchronous JavaScript and APIs.",
                    "Build a small JavaScript web application."
                ]
            },

            "react": {
                "importance": "High",
                "reason": "React is widely used for modern frontend application development.",
                "learning_steps": [
                    "Learn components and JSX.",
                    "Understand props and state.",
                    "Learn useState and useEffect.",
                    "Build a small React project."
                ]
            },

            "java": {
                "importance": "High",
                "reason": "Java is widely used in backend and enterprise software development.",
                "learning_steps": [
                    "Learn Java syntax and OOP concepts.",
                    "Practice classes, objects and inheritance.",
                    "Learn collections and exception handling.",
                    "Build a small Java application."
                ]
            },

            "machine learning": {
                "importance": "High",
                "reason": "Machine learning is useful for AI, data science and predictive analytics internships.",
                "learning_steps": [
                    "Learn supervised and unsupervised learning.",
                    "Study regression and classification.",
                    "Practice using scikit-learn.",
                    "Build a small ML project."
                ]
            },

            "deep learning": {
                "importance": "High",
                "reason": "Deep learning is useful for computer vision, NLP and advanced AI applications.",
                "learning_steps": [
                    "Learn neural network fundamentals.",
                    "Understand forward and backward propagation.",
                    "Learn basic CNN and transformer concepts.",
                    "Build a small deep learning project."
                ]
            },

            "flask": {
                "importance": "Medium",
                "reason": "Flask is useful for building lightweight Python backend APIs.",
                "learning_steps": [
                    "Learn Flask routes.",
                    "Understand GET and POST requests.",
                    "Build REST APIs.",
                    "Connect Flask with a database."
                ]
            },

            "django": {
                "importance": "Medium",
                "reason": "Django is a popular Python framework for building web applications.",
                "learning_steps": [
                    "Learn Django project structure.",
                    "Understand models and views.",
                    "Learn URL routing and templates.",
                    "Build a small Django application."
                ]
            },

            "git": {
                "importance": "High",
                "reason": "Git is an essential skill for collaborative software development.",
                "learning_steps": [
                    "Learn git init, add and commit.",
                    "Learn branches and merging.",
                    "Learn GitHub repositories.",
                    "Practice pushing and pulling code."
                ]
            },

            "docker": {
                "importance": "Medium",
                "reason": "Docker is useful for packaging and deploying applications consistently.",
                "learning_steps": [
                    "Understand containers.",
                    "Learn Dockerfiles.",
                    "Build a Docker image.",
                    "Run your application inside a container."
                ]
            },

            "aws": {
                "importance": "Medium",
                "reason": "AWS knowledge is useful for cloud and backend engineering internships.",
                "learning_steps": [
                    "Learn basic cloud concepts.",
                    "Understand EC2 and S3.",
                    "Learn basic IAM concepts.",
                    "Deploy a small application."
                ]
            },

            "html": {
                "importance": "Medium",
                "reason": "HTML is the foundation of web page structure.",
                "learning_steps": [
                    "Learn semantic HTML.",
                    "Practice forms and tables.",
                    "Understand accessibility basics.",
                    "Build a simple webpage."
                ]
            },

            "css": {
                "importance": "Medium",
                "reason": "CSS is required to create responsive and professional web interfaces.",
                "learning_steps": [
                    "Learn selectors and box model.",
                    "Practice Flexbox.",
                    "Learn CSS Grid.",
                    "Build a responsive webpage."
                ]
            },

            "communication": {
                "importance": "High",
                "reason": "Communication skills are important during interviews and professional collaboration.",
                "learning_steps": [
                    "Practice introducing yourself.",
                    "Practice explaining your projects.",
                    "Improve technical communication.",
                    "Practice common interview questions."
                ]
            }
        }

        skill_gaps = []

        for skill in missing_skills:

            normalized_skill = skill.lower().strip()

            roadmap = skill_roadmaps.get(
                normalized_skill
            )

            if roadmap:

                skill_gaps.append({
                    "skill": skill,
                    "importance": roadmap["importance"],
                    "reason": roadmap["reason"],
                    "learning_steps": roadmap["learning_steps"]
                })

            else:

                skill_gaps.append({
                    "skill": skill,
                    "importance": "Medium",
                    "reason": (
                        f"{skill} appears to be relevant to this "
                        "internship and should be learned to improve "
                        "your profile."
                    ),
                    "learning_steps": [
                        f"Understand the basic concepts of {skill}.",
                        f"Practice {skill} using beginner-level exercises.",
                        f"Build a small project using {skill}.",
                        f"Practice common interview questions related to {skill}."
                    ]
                })

        return {
            "skill_gaps": skill_gaps
        }

    # ==========================================================
    # GEMINI + RAG
    # ==========================================================

    def analyze_skill_gaps_with_gemini(
        self,
        missing_skills,
        resume_context=""
    ):

        print("\nUsing Gemini + RAG Skill Gap Analysis...")

        prompt = f"""
You are an AI Career Skill Gap Agent.

You are helping a student prepare for an internship.

==================================================
RESUME CONTEXT RETRIEVED USING RAG
==================================================

{resume_context}

==================================================
MISSING SKILLS FOR THIS INTERNSHIP
==================================================

{missing_skills}

==================================================
TASK
==================================================

Analyze the student's skill gaps using BOTH:

1. The missing skills required by the internship.
2. The resume context retrieved using RAG.

Create a simple and personalized internship preparation roadmap.

IMPORTANT RULES:

- Focus only on the missing skills.
- Use the resume context to understand the student's existing background.
- Do not invent unrelated skills.
- Do not say that the student has a skill unless the resume context supports it.
- importance must be exactly High, Medium or Low.
- Give 2 to 4 practical learning steps for each missing skill.
- Keep explanations simple.
- Focus on internship preparation.
- The roadmap should be useful for a student.
- Return ONLY valid JSON.

Return exactly this structure:

{{
    "skill_gaps": [
        {{
            "skill": "",
            "importance": "",
            "reason": "",
            "learning_steps": []
        }}
    ]
}}
"""

        response = self.client.models.generate_content(

            model="gemini-3.6-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                response_mime_type="application/json",

                response_schema={
                    "type": "object",

                    "properties": {

                        "skill_gaps": {

                            "type": "array",

                            "items": {

                                "type": "object",

                                "properties": {

                                    "skill": {
                                        "type": "string"
                                    },

                                    "importance": {
                                        "type": "string"
                                    },

                                    "reason": {
                                        "type": "string"
                                    },

                                    "learning_steps": {

                                        "type": "array",

                                        "items": {
                                            "type": "string"
                                        }
                                    }
                                },

                                "required": [
                                    "skill",
                                    "importance",
                                    "reason",
                                    "learning_steps"
                                ]
                            }
                        }
                    },

                    "required": [
                        "skill_gaps"
                    ]
                }
            )
        )

        result = json.loads(
            response.text
        )

        return result

    # ==========================================================
    # MAIN METHOD
    # ==========================================================

    def analyze_skill_gaps(
        self,
        missing_skills,
        resume_context=""
    ):

        print("\n================================")
        print("SKILL GAP AGENT")
        print("================================")

        print(
            "Missing skills:",
            missing_skills
        )

        print(
            "RAG context length:",
            len(resume_context)
        )

        # No missing skills
        if not missing_skills:

            print(
                "\nNo skill gaps detected."
            )

            return {
                "skill_gaps": []
            }

        # ======================================================
        # TRY GEMINI
        # ======================================================

        if self.client:

            try:

                print(
                    "\nTrying Gemini Skill Gap Analysis..."
                )

                result = (
                    self.analyze_skill_gaps_with_gemini(
                        missing_skills,
                        resume_context
                    )
                )

                print(
                    "Gemini Skill Gap Analysis successful."
                )

                return result

            except Exception as e:

                print(
                    "\nGemini Skill Gap Analysis failed:"
                )

                print(e)

                print(
                    "\nSwitching to local fallback..."
                )

        # ======================================================
        # LOCAL FALLBACK
        # ======================================================

        return self.analyze_skill_gaps_local(
            missing_skills
        )