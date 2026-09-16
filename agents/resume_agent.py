import os
import json
import re

from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


class ResumeAgent:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")
        self.llm_service = None

        if self.api_key:
            try:
                self.llm_service = genai.Client(
                    api_key=self.api_key
                )

            except Exception as e:
                print("Gemini initialization failed:", e)

        print("Resume Agent initialized")

    # ==========================================================
    # PDF TEXT EXTRACTION
    # ==========================================================

    def extract_text(self, pdf_path):

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    # ==========================================================
    # CLEAN TEXT
    # ==========================================================

    def clean_text(self, text):

        if not text:
            return ""

        text = str(text)

        # Fix common PDF ligatures
        text = text.replace("\ufb01", "fi")
        text = text.replace("\ufb02", "fl")

        # Bullet characters
        text = text.replace("\u2022", " ")

        # Normalize whitespace
        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    # ==========================================================
    # SKILL DETECTION
    # ==========================================================

    def extract_skills(self, resume_text):

        # Normalize text
        text = self.clean_text(
            resume_text
        ).lower()

        # ------------------------------------------------------
        # Normalize common variations
        # ------------------------------------------------------

        replacements = {

            "git/github":
                "git github",

            "html/css":
                "html css",

            "html css":
                "html css",

            "linux/unix":
                "linux unix",

            "aws/cloud":
                "aws cloud",

            "rest api":
                "rest api",

            "ms sql server":
                "ms sql server",

            "pl/sql":
                "pl sql",

            "java/j2ee":
                "java j2ee",

            "c++":
                "cpp",

            "ui/ux":
                "ui ux",

            "power-bi":
                "power bi",

            "machine-learning":
                "machine learning",

            "deep-learning":
                "deep learning",

            "data-analysis":
                "data analysis",

            "data-analytics":
                "data analytics"
        }

        for old, new in replacements.items():

            text = text.replace(
                old,
                new
            )

        # ======================================================
        # SKILL LIBRARY
        # ======================================================

        skill_patterns = {

            # --------------------------------------------------
            # PROGRAMMING LANGUAGES
            # --------------------------------------------------

            "Java": [
                r"\bjava\b"
            ],

            "J2EE": [
                r"\bj2ee\b"
            ],

            "Python": [
                r"\bpython\b"
            ],

            "JavaScript": [
                r"\bjavascript\b"
            ],

            "TypeScript": [
                r"\btypescript\b"
            ],

            "C++": [
                r"\bcpp\b"
            ],

            "C": [
                r"(?<![a-z])c(?![a-z])"
            ],

            "SQL": [
                r"\bsql\b"
            ],

            "PL/SQL": [
                r"\bpl\s*/?\s*sql\b",
                r"\bpl sql\b"
            ],

            # --------------------------------------------------
            # WEB DEVELOPMENT
            # --------------------------------------------------

            "HTML": [
                r"\bhtml\b",
                r"\bhtml5\b"
            ],

            "CSS": [
                r"\bcss\b",
                r"\bcss3\b"
            ],

            "React": [
                r"\breact\b",
                r"\breactjs\b",
                r"\breact\.js\b"
            ],

            "Angular": [
                r"\bangular\b",
                r"\bangularjs\b",
                r"\bangular\.js\b"
            ],

            "Vue": [
                r"\bvue\b",
                r"\bvuejs\b",
                r"\bvue\.js\b"
            ],

            "Node.js": [
                r"\bnode\.?js\b",
                r"\bnodejs\b"
            ],

            "Express.js": [
                r"\bexpress\.?js\b",
                r"\bexpressjs\b"
            ],

            "Flask": [
                r"\bflask\b"
            ],

            "Django": [
                r"\bdjango\b"
            ],

            "REST API": [
                r"\brest api\b",
                r"\bapi integration\b",
                r"\brestful api\b"
            ],

            "MVC": [
                r"\bmvc\b"
            ],

            "JDBC": [
                r"\bjdbc\b"
            ],

            # --------------------------------------------------
            # DATABASES
            # --------------------------------------------------

            "MySQL": [
                r"\bmysql\b"
            ],

            "MS SQL Server": [
                r"\bms sql server\b"
            ],

            "Oracle DB": [
                r"\boracle db\b",
                r"\boracle database\b",
                r"\boracle\b"
            ],

            "PostgreSQL": [
                r"\bpostgresql\b",
                r"\bpostgres\b"
            ],

            "MongoDB": [
                r"\bmongodb\b",
                r"\bmongo db\b"
            ],

            "SQLite": [
                r"\bsqlite\b"
            ],

            # --------------------------------------------------
            # JAVA FRAMEWORKS
            # --------------------------------------------------

            "Hibernate": [
                r"\bhibernate\b"
            ],

            "Spring Boot": [
                r"\bspring boot\b"
            ],

            "JUnit": [
                r"\bjunit\b"
            ],

            "TDD": [
                r"\btdd\b",
                r"\btest driven development\b"
            ],

            # --------------------------------------------------
            # CLOUD
            # --------------------------------------------------

            "AWS": [
                r"\baws\b",
                r"\bamazon web services\b"
            ],

            "Cloud": [
                r"\bcloud\b",
                r"\bcloud-based\b",
                r"\bcloud based\b"
            ],

            "AWS Lambda": [
                r"\baws lambda\b"
            ],

            "AWS S3": [
                r"\baws s3\b",
                r"\bs3\b"
            ],

            "AWS SES": [
                r"\baws ses\b"
            ],

            "API Gateway": [
                r"\bapi gateway\b"
            ],

            "Azure": [
                r"\bazure\b",
                r"\bmicrosoft azure\b"
            ],

            "Google Cloud": [
                r"\bgoogle cloud\b",
                r"\bgcp\b",
                r"\bgoogle cloud platform\b"
            ],

            # --------------------------------------------------
            # DEVOPS
            # --------------------------------------------------

            "Docker": [
                r"\bdocker\b"
            ],

            "Kubernetes": [
                r"\bkubernetes\b",
                r"\bk8s\b"
            ],

            "DevOps": [
                r"\bdevops\b",
                r"\bdev ops\b"
            ],

            # --------------------------------------------------
            # AI / ML
            # --------------------------------------------------

            "Artificial Intelligence": [
                r"\bartificial intelligence\b"
            ],

            "Machine Learning": [
                r"\bmachine learning\b"
            ],

            "Deep Learning": [
                r"\bdeep learning\b"
            ],

            "NLP": [
                r"\bnlp\b",
                r"\bnatural language processing\b"
            ],

            "Computer Vision": [
                r"\bcomputer vision\b"
            ],

            "Data Science": [
                r"\bdata science\b"
            ],

            "Data Analysis": [
                r"\bdata analysis\b",
                r"\bdata analytics\b"
            ],

            "Pandas": [
                r"\bpandas\b"
            ],

            "NumPy": [
                r"\bnumpy\b"
            ],

            "Matplotlib": [
                r"\bmatplotlib\b"
            ],

            "TensorFlow": [
                r"\btensorflow\b"
            ],

            "PyTorch": [
                r"\bpytorch\b"
            ],

            "Scikit-learn": [
                r"\bscikit-learn\b",
                r"\bscikit learn\b",
                r"\bsklearn\b"
            ],

            "PySpark": [
                r"\bpyspark\b"
            ],

            "Bayesian Networks": [
                r"\bbayesian network\b",
                r"\bbayesian networks\b"
            ],

            "Granger Causality": [
                r"\bgranger causality\b"
            ],

            # --------------------------------------------------
            # VERSION CONTROL
            # --------------------------------------------------

            "Git": [
                r"\bgit\b"
            ],

            "GitHub": [
                r"\bgithub\b",
                r"\bgit hub\b"
            ],

            # --------------------------------------------------
            # OPERATING SYSTEMS
            # --------------------------------------------------

            "Linux": [
                r"\blinux\b"
            ],

            "Unix": [
                r"\bunix\b"
            ],

            "Unix Shell Scripting": [
                r"\bshell scripting\b",
                r"\bshell script\b",
                r"\bshell scripting\b"
            ],

            # --------------------------------------------------
            # OFFICE / ANALYTICS
            # --------------------------------------------------

            "Microsoft Excel": [
                r"\bmicrosoft excel\b",
                r"\bexcel\b"
            ],

            "VLOOKUP": [
                r"\bvlookup\b"
            ],

            "Pivot Tables": [
                r"\bpivot tables\b",
                r"\bpivot table\b"
            ],

            "Power BI": [
                r"\bpower bi\b",
                r"\bpowerbi\b"
            ],

            "Tableau": [
                r"\btableau\b"
            ],

            "Cognos": [
                r"\bcognos\b"
            ],

            # --------------------------------------------------
            # BUSINESS / FINANCE
            # --------------------------------------------------

            "Accounts Receivable": [
                r"\baccounts receivable\b"
            ],

            "Accounts Payable": [
                r"\baccounts payable\b"
            ],

            "Invoicing": [
                r"\binvoicing\b",
                r"\binvoice\b",
                r"\binvoices\b"
            ],

            "Collections": [
                r"\bcollections\b",
                r"\bcollection process\b"
            ],

            "Payment Tracking": [
                r"\bpayment tracking\b",
                r"\bpayment history\b",
                r"\bpayment histories\b"
            ],

            "Account Reconciliation": [
                r"\baccount reconciliation\b",
                r"\baccount reconciliations\b",
                r"\breconciliation process\b"
            ],

            "Financial Reporting": [
                r"\bfinancial reporting\b",
                r"\bfinancial reports\b"
            ],

            "Financial Analysis": [
                r"\bfinancial analysis\b"
            ],

            "Cash Flow Forecasting": [
                r"\bcash flow forecasting\b",
                r"\bcash flow\b"
            ],

            "Aging Reports": [
                r"\baging reports\b",
                r"\baging report\b"
            ],

            "Billing Dispute Resolution": [
                r"\bbilling disputes\b",
                r"\bbilling dispute\b",
                r"\bdispute resolution\b"
            ],

            "ERP": [
                r"\berp\b",
                r"\berp system\b"
            ],

            "Audit Support": [
                r"\baudit\b",
                r"\baudits\b"
            ],

            "Delinquency Management": [
                r"\bdelinquency\b",
                r"\bdelinquent\b"
            ],

            "Days Sales Outstanding": [
                r"\bdays sales outstanding\b",
                r"\bdso\b"
            ],

            "Process Improvement": [
                r"\bprocess improvement\b",
                r"\bprocess improvements\b"
            ],

            "Automation": [
                r"\bautomation\b",
                r"\bautomated\b"
            ],

            "Client Management": [
                r"\bclient management\b",
                r"\bclient communications\b"
            ],

            # --------------------------------------------------
            # BUSINESS / SOFT SKILLS
            # --------------------------------------------------

            "Communication": [
                r"\bcommunication\b",
                r"\bcommunications\b"
            ],

            "Team Collaboration": [
                r"\bcollaborat\w+\b",
                r"\bteam collaboration\b"
            ],

            "Negotiation": [
                r"\bnegotiat\w+\b"
            ],

            "Problem Solving": [
                r"\bproblem solving\b",
                r"\bproblem-solving\b"
            ],

            "Reporting": [
                r"\breporting\b",
                r"\breports\b"
            ],

            "Stakeholder Management": [
                r"\bstakeholder management\b"
            ],

            "Customer Service": [
                r"\bcustomer service\b"
            ],

            "Sales": [
                r"\bsales\b"
            ],

            "Marketing": [
                r"\bmarketing\b"
            ],

            "Digital Marketing": [
                r"\bdigital marketing\b"
            ],

            "SEO": [
                r"\bseo\b",
                r"\bsearch engine optimization\b"
            ],

            "Content Writing": [
                r"\bcontent writing\b",
                r"\bcontent writer\b"
            ],

            # --------------------------------------------------
            # DESIGN
            # --------------------------------------------------

            "UI/UX": [
                r"\bui\s*/?\s*ux\b",
                r"\bui ux\b",
                r"\buser interface\b",
                r"\buser experience\b"
            ],

            "Figma": [
                r"\bfigma\b"
            ],

            # --------------------------------------------------
            # ENTERPRISE TOOLS
            # --------------------------------------------------

            "Active Directory": [
                r"\bactive directory\b"
            ],

            "Ellucian Banner": [
                r"\bellucian banner\b"
            ],

            "Office 365": [
                r"\boffice 365\b"
            ],

            "Agile": [
                r"\bagile\b"
            ],

            "JIRA": [
                r"\bjira\b"
            ],

            "Google Apps Script": [
                r"\bgoogle apps script\b"
            ]
        }

        # ======================================================
        # DETECT SKILLS
        # ======================================================

        detected = []

        for skill, patterns in skill_patterns.items():

            for pattern in patterns:

                if re.search(
                    pattern,
                    text,
                    re.IGNORECASE
                ):

                    detected.append(skill)

                    break

        return detected

    # ==========================================================
    # SECTION EXTRACTION
    # ==========================================================

    def extract_sections(self, resume_text):

        lines = [
            line.strip()
            for line in resume_text.splitlines()
            if line.strip()
        ]

        sections = {

            "skills": [],

            "education": [],

            "experience": [],

            "projects": [],

            "certifications": []
        }

        current_section = None

        section_patterns = {

            "skills": [

                "skills",

                "technical skills",

                "key skills",

                "professional skills",

                "technical expertise"
            ],

            "education": [

                "education",

                "academic background",

                "educational background",

                "academic qualifications"
            ],

            "experience": [

                "experience",

                "work experience",

                "professional experience",

                "employment history",

                "work history"
            ],

            "projects": [

                "projects",

                "academic projects",

                "personal projects",

                "project experience"
            ],

            "certifications": [

                "certifications",

                "certification",

                "licenses and certifications",

                "licenses & certifications"
            ]
        }

        def detect_section(line):

            normalized = line.lower().strip()

            normalized = normalized.rstrip(":")

            normalized = normalized.strip()

            for section_name, names in section_patterns.items():

                for name in names:

                    if normalized == name:

                        return section_name

            return None

        for line in lines:

            detected_section = detect_section(line)

            # ----------------------------------------------
            # New section
            # ----------------------------------------------

            if detected_section:

                current_section = detected_section

                continue

            # ----------------------------------------------
            # Stop collecting when hobby/interests section
            # starts
            # ----------------------------------------------

            normalized_line = line.lower().strip()

            if normalized_line in [

                "hobbies",

                "interests",

                "hobbies and interests",

                "hobbies & interests"
            ]:

                current_section = None

                continue

            # ----------------------------------------------
            # Add content
            # ----------------------------------------------

            if current_section:

                sections[
                    current_section
                ].append(line)

        return sections

    # ==========================================================
    # CLEAN SECTION CONTENT
    # ==========================================================

    def clean_section_items(self, items):

        cleaned_items = []

        current = ""

        for item in items:

            item = item.strip()

            if not item:
                continue

            # Remove bullet characters
            item = re.sub(
                r"^[•●▪◦\-]+\s*",
                "",
                item
            )

            if not item:
                continue

            upper_item = item.upper()

            # Stop hobby/interests content
            if upper_item in [

                "HOBBIES",

                "HOBBIES AND INTERESTS",

                "HOBBIES & INTERESTS",

                "INTERESTS"
            ]:

                if current:

                    cleaned_items.append(
                        current.strip()
                    )

                    current = ""

                continue

            # ------------------------------------------
            # Combine PDF broken lines
            # ------------------------------------------

            if current:

                current += " " + item

            else:

                current = item

        # Add final item
        if current:

            cleaned_items.append(
                current.strip()
            )

        # Remove duplicates
        final_items = []

        for item in cleaned_items:

            if item not in final_items:

                final_items.append(item)

        return final_items

    # ==========================================================
    # NAME DETECTION
    # ==========================================================

    def extract_name(
        self,
        resume_text
    ):

        lines = [

            line.strip()

            for line in resume_text.splitlines()

            if line.strip()
        ]

        if not lines:

            return ""

        # Look at first few lines
        for line in lines[:5]:

            lower = line.lower()

            if "@" in line:
                continue

            if "linkedin" in lower:
                continue

            if "http" in lower:
                continue

            if re.search(
                r"\d{3,}",
                line
            ):
                continue

            if len(line.split()) <= 5:

                return line

        return ""

    # ==========================================================
    # LOCAL RESUME ANALYSIS
    # ==========================================================

    def analyze_resume_local(
        self,
        resume_text
    ):

        print(
            "Using local resume analysis..."
        )

        sections = self.extract_sections(
            resume_text
        )

        skills = self.extract_skills(
            resume_text
        )

        education = self.clean_section_items(
            sections["education"]
        )

        experience = self.clean_section_items(
            sections["experience"]
        )

        projects = self.clean_section_items(
            sections["projects"]
        )

        certifications = self.clean_section_items(
            sections["certifications"]
        )

        name = self.extract_name(
            resume_text
        )

        return {

            "name": name,

            "skills": skills,

            "education": education,

            "experience": experience,

            "projects": projects,

            "certifications": certifications
        }

    # ==========================================================
    # GEMINI ANALYSIS
    # ==========================================================

    def analyze_resume_with_gemini(
        self,
        resume_text
    ):

        prompt = f"""
You are an AI Resume Analysis Agent.

Analyze the following resume.

Extract ONLY information that actually exists
in the resume.

Return JSON with exactly this structure:

{{
    "name": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Rules:

1. Do not invent information.
2. Keep every skill as a separate item.
3. Preserve important technologies.
4. Preserve business, finance, analytical,
   design and technical skills.
5. If information is missing, return an empty list.
6. Return only information found in the resume.

RESUME:

{resume_text}
"""

        response = self.llm_service.models.generate_content(

            model="gemini-3.6-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                response_mime_type="application/json",

                response_schema={

                    "type": "object",

                    "properties": {

                        "name": {
                            "type": "string"
                        },

                        "skills": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },

                        "education": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },

                        "experience": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },

                        "projects": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },

                        "certifications": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },

                    "required": [

                        "name",

                        "skills",

                        "education",

                        "experience",

                        "projects",

                        "certifications"
                    ]
                }
            )
        )

        return json.loads(
            response.text
        )

    # ==========================================================
    # MAIN ANALYSIS FUNCTION
    # ==========================================================

    def analyze_resume(
        self,
        resume_text
    ):

        print(
            "\nAnalyzing resume..."
        )

        # ------------------------------------------------------
        # Try Gemini first
        # ------------------------------------------------------

        if self.llm_service:

            try:

                print(
                    "Trying Gemini resume analysis..."
                )

                result = (
                    self.analyze_resume_with_gemini(
                        resume_text
                    )
                )

                print(
                    "Gemini resume analysis successful."
                )

                return result

            except Exception as e:

                print(
                    "\nGemini failed:"
                )

                print(
                    str(e)
                )

                print(
                    "\nFalling back to local resume analysis..."
                )

        # ------------------------------------------------------
        # Local fallback
        # ------------------------------------------------------

        return self.analyze_resume_local(
            resume_text
        )