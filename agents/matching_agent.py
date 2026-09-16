import re
import html


class MatchingAgent:

    def __init__(self):
        print("Matching Agent initialized")

        # Skill dictionary for multiple internship domains
        self.skill_aliases = {

            # =========================
            # PROGRAMMING
            # =========================
            "python": [
                "python",
                "python programming",
                "python3"
            ],

            "java": [
                "java",
                "java programming",
                "java se",
                "java ee"
            ],

            "javascript": [
                "javascript",
                "java script",
                "js"
            ],

            "typescript": [
                "typescript",
                "type script",
                "ts"
            ],

            "c": [
                "c programming",
                "c language"
            ],

            "c++": [
                "c++",
                "cpp"
            ],

            "c#": [
                "c#",
                "c sharp"
            ],

            # =========================
            # WEB DEVELOPMENT
            # =========================
            "html": [
                "html",
                "html5"
            ],

            "css": [
                "css",
                "css3"
            ],

            "react": [
                "react",
                "react.js",
                "reactjs",
                "react js"
            ],

            "angular": [
                "angular",
                "angular.js",
                "angularjs"
            ],

            "vue": [
                "vue",
                "vue.js",
                "vuejs"
            ],

            "node": [
                "node",
                "node.js",
                "nodejs"
            ],

            "express": [
                "express",
                "express.js",
                "expressjs"
            ],

            "flask": [
                "flask"
            ],

            "django": [
                "django"
            ],

            # =========================
            # DATABASE
            # =========================
            "sql": [
                "sql",
                "structured query language"
            ],

            "mysql": [
                "mysql"
            ],

            "postgresql": [
                "postgresql",
                "postgres"
            ],

            "mongodb": [
                "mongodb",
                "mongo db"
            ],

            "oracle": [
                "oracle",
                "oracle database",
                "oracle db"
            ],

            "sqlite": [
                "sqlite"
            ],

            "pl/sql": [
                "pl/sql",
                "plsql"
            ],

            # =========================
            # DATA / AI
            # =========================
            "machine learning": [
                "machine learning",
                "machine-learning",
                "ml"
            ],

            "deep learning": [
                "deep learning",
                "deep-learning",
                "dl"
            ],

            "artificial intelligence": [
                "artificial intelligence",
                "artificial-intelligence",
                "ai"
            ],

            "generative ai": [
                "generative ai",
                "genai",
                "generative artificial intelligence"
            ],

            "nlp": [
                "nlp",
                "natural language processing"
            ],

            "computer vision": [
                "computer vision",
                "computer-vision"
            ],

            "tensorflow": [
                "tensorflow"
            ],

            "pytorch": [
                "pytorch",
                "torch"
            ],

            "scikit-learn": [
                "scikit-learn",
                "scikit learn",
                "sklearn"
            ],

            "pandas": [
                "pandas"
            ],

            "numpy": [
                "numpy"
            ],

            "matplotlib": [
                "matplotlib"
            ],

            "data science": [
                "data science",
                "data-science"
            ],

            "data analysis": [
                "data analysis",
                "data-analysis",
                "data analyst"
            ],

            # =========================
            # DATA VISUALIZATION
            # =========================
            "excel": [
                "excel",
                "microsoft excel",
                "ms excel"
            ],

            "power bi": [
                "power bi",
                "powerbi"
            ],

            "tableau": [
                "tableau"
            ],

            # =========================
            # FINANCE / ACCOUNTING
            # =========================
            "accounts receivable": [
                "accounts receivable",
                "account receivable",
                "ar"
            ],

            "accounts payable": [
                "accounts payable",
                "account payable",
                "ap"
            ],

            "accounting": [
                "accounting",
                "financial accounting"
            ],

            "invoicing": [
                "invoicing",
                "invoice processing",
                "invoice management"
            ],

            "collections": [
                "collections",
                "collection management",
                "debt collection"
            ],

            "payment tracking": [
                "payment tracking",
                "payment processing",
                "payment monitoring"
            ],

            "account reconciliation": [
                "account reconciliation",
                "account reconciliations",
                "reconciliation"
            ],

            "financial reporting": [
                "financial reporting",
                "financial reports",
                "financial analysis"
            ],

            "cash flow forecasting": [
                "cash flow forecasting",
                "cash flow forecast",
                "cash flow analysis"
            ],

            "aging reports": [
                "aging reports",
                "accounts aging",
                "aging analysis"
            ],

            "billing": [
                "billing",
                "billing management",
                "billing operations"
            ],

            "audit": [
                "audit",
                "auditing",
                "audit support"
            ],

            "erp": [
                "erp",
                "enterprise resource planning"
            ],

            "accounts management": [
                "accounts management",
                "account management"
            ],

            "financial analysis": [
                "financial analysis",
                "finance analysis"
            ],

            "risk management": [
                "risk management",
                "financial risk"
            ],

            # =========================
            # BUSINESS
            # =========================
            "sales": [
                "sales",
                "sales operations",
                "sales management"
            ],

            "marketing": [
                "marketing",
                "digital marketing",
                "marketing strategy"
            ],

            "business development": [
                "business development",
                "business development associate"
            ],

            "client management": [
                "client management",
                "client relationship management",
                "customer management"
            ],

            "customer service": [
                "customer service",
                "customer support"
            ],

            "negotiation": [
                "negotiation",
                "negotiating"
            ],

            "reporting": [
                "reporting",
                "report generation"
            ],

            "process improvement": [
                "process improvement",
                "process optimization",
                "business process improvement"
            ],

            "automation": [
                "automation",
                "process automation",
                "workflow automation"
            ],

            # =========================
            # SOFT SKILLS
            # =========================
            "communication": [
                "communication",
                "communication skills",
                "verbal communication",
                "written communication"
            ],

            "team collaboration": [
                "team collaboration",
                "teamwork",
                "collaboration"
            ],

            "leadership": [
                "leadership",
                "leadership skills"
            ],

            "problem solving": [
                "problem solving",
                "problem-solving"
            ],

            "time management": [
                "time management"
            ],

            "analytical thinking": [
                "analytical thinking",
                "analytical skills"
            ],

            # =========================
            # CLOUD / DEVOPS
            # =========================
            "aws": [
                "aws",
                "amazon web services"
            ],

            "azure": [
                "azure",
                "microsoft azure"
            ],

            "gcp": [
                "gcp",
                "google cloud",
                "google cloud platform"
            ],

            "docker": [
                "docker"
            ],

            "kubernetes": [
                "kubernetes",
                "k8s"
            ],

            "linux": [
                "linux"
            ],

            "git": [
                "git"
            ],

            "github": [
                "github",
                "git hub"
            ],

            "devops": [
                "devops",
                "dev ops"
            ],

            # =========================
            # CYBERSECURITY
            # =========================
            "cybersecurity": [
                "cybersecurity",
                "cyber security"
            ],

            "network security": [
                "network security"
            ],

            "ethical hacking": [
                "ethical hacking"
            ],

            # =========================
            # DESIGN
            # =========================
            "figma": [
                "figma"
            ],

            "ui/ux": [
                "ui/ux",
                "ui ux",
                "user interface",
                "user experience"
            ],

            "graphic design": [
                "graphic design",
                "graphic designing"
            ],

            # =========================
            # ENGINEERING
            # =========================
            "matlab": [
                "matlab"
            ],

            "autocad": [
                "autocad",
                "auto cad"
            ],

            "solidworks": [
                "solidworks",
                "solid works"
            ],

            "arduino": [
                "arduino"
            ],

            "raspberry pi": [
                "raspberry pi",
                "raspberrypi"
            ],

            "embedded systems": [
                "embedded systems",
                "embedded system"
            ]
        }

    # =====================================================
    # CLEAN TEXT
    # =====================================================

    def clean_text(self, text):

        if not text:
            return ""

        text = html.unescape(str(text))

        # Remove HTML tags
        text = re.sub(
            r"<[^>]+>",
            " ",
            text
        )

        # Normalize common technology names
        replacements = {

            "javascriptreact": "javascript react",

            "javascript/react":
                "javascript react",

            "react.js":
                "react",

            "reactjs":
                "react",

            "node.js":
                "node",

            "nodejs":
                "node",

            "next.js":
                "next",

            "nextjs":
                "next",

            "powerbi":
                "power bi",

            "machine-learning":
                "machine learning",

            "deep-learning":
                "deep learning"
        }

        lower = text.lower()

        for old, new in replacements.items():
            lower = lower.replace(
                old,
                new
            )

        # Replace special separators
        lower = lower.replace(
            "/",
            " "
        )

        lower = lower.replace(
            "&",
            " and "
        )

        # Remove excessive whitespace
        lower = re.sub(
            r"[\r\n\t]+",
            " ",
            lower
        )

        lower = re.sub(
            r"\s+",
            " ",
            lower
        )

        return lower.strip()

    # =====================================================
    # CHECK WHETHER SKILL EXISTS
    # =====================================================

    def skill_exists(
        self,
        text,
        alias
    ):

        alias = alias.lower().strip()

        if not alias:
            return False

        pattern = (
            r"(?<![a-z0-9])"
            + re.escape(alias)
            + r"(?![a-z0-9])"
        )

        return bool(
            re.search(
                pattern,
                text,
                re.IGNORECASE
            )
        )

    # =====================================================
    # EXTRACT SKILLS FROM JOB
    # =====================================================

    def extract_skills_from_text(
        self,
        text
    ):

        text = self.clean_text(text)

        found_skills = []

        for canonical_skill, aliases in self.skill_aliases.items():

            for alias in aliases:

                if self.skill_exists(
                    text,
                    alias
                ):

                    if canonical_skill not in found_skills:

                        found_skills.append(
                            canonical_skill
                        )

                    break

        return found_skills

    # =====================================================
    # NORMALIZE RESUME SKILLS
    # =====================================================

    def normalize_resume_skills(
        self,
        resume_skills
    ):

        normalized = set()

        for skill in resume_skills:

            skill_text = self.clean_text(
                skill
            )

            matched = False

            for canonical_skill, aliases in self.skill_aliases.items():

                for alias in aliases:

                    if self.skill_exists(
                        skill_text,
                        alias
                    ):

                        normalized.add(
                            canonical_skill
                        )

                        matched = True

                        break

                if matched:
                    break

            # Keep unknown resume skills too
            if not matched and skill_text:

                normalized.add(
                    skill_text
                )

        return normalized

    # =====================================================
    # CALCULATE MATCH
    # =====================================================

    def calculate_match(
        self,
        resume_skills,
        job_description,
        job_title=""
    ):

        print(
            "Matching resume with job..."
        )

        complete_job_text = (
            str(job_title)
            + " "
            + str(job_description)
        )

        # Extract skills from job
        required_skills = (
            self.extract_skills_from_text(
                complete_job_text
            )
        )

        # Normalize resume skills
        resume_skills_normalized = (
            self.normalize_resume_skills(
                resume_skills
            )
        )

        matched_skills = []
        missing_skills = []

        # Compare
        for skill in required_skills:

            if skill in resume_skills_normalized:

                matched_skills.append(
                    skill
                )

            else:

                missing_skills.append(
                    skill
                )

        # Calculate score
        if required_skills:

            score = (
                len(matched_skills)
                /
                len(required_skills)
            ) * 100

        else:

            score = 0

        return {

            "score": round(
                score,
                2
            ),

            "matched_skills":
                matched_skills,

            "missing_skills":
                missing_skills,

            "required_skills":
                required_skills
        }