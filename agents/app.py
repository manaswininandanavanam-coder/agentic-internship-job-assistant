import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from pypdf import PdfReader

from agents.resume_agent import ResumeAgent
from agents.orchestrator import InternshipOrchestrator


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)

CORS(app)


# ============================================================
# CONFIGURATION
# ============================================================

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {
    "pdf"
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ============================================================
# INITIALIZE AGENTS
# ============================================================

print("\n================================")
print("INITIALIZING AI SYSTEM")
print("================================")

resume_agent = ResumeAgent()

orchestrator = InternshipOrchestrator()

print("\nAI system initialized successfully.")


# ============================================================
# HELPER FUNCTION
# ============================================================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(
            ".",
            1
        )[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ============================================================
# HOME PAGE
# ============================================================

@app.route(
    "/",
    methods=["GET"]
)
def home():

    return jsonify({

        "status": "success",

        "message":
            "Agentic AI Internship Job Discovery API is running.",

        "endpoints": {

            "find_internships":
                "/api/find-internships",

            "analyze_internship":
                "/api/analyze-internship",

            "prepare_application":
                "/api/prepare-application"

        }

    })


# ============================================================
# FIND INTERNSHIPS
# ============================================================

@app.route(
    "/api/find-internships",
    methods=["POST"]
)
def find_internships():

    try:

        print("\n================================")
        print("FIND INTERNSHIPS REQUEST")
        print("================================")

        # ----------------------------------------------------
        # GET FORM DATA
        # ----------------------------------------------------

        internship_query = request.form.get(
            "query",
            ""
        ).strip()

        year = request.form.get(
            "year",
            ""
        ).strip()

        branch = request.form.get(
            "branch",
            ""
        ).strip()

        skills = request.form.get(
            "skills",
            ""
        ).strip()


        print("\nQuery:")
        print(internship_query)

        print("Year:")
        print(year)

        print("Branch:")
        print(branch)

        print("Additional skills:")
        print(skills)


        # ----------------------------------------------------
        # VALIDATE QUERY
        # ----------------------------------------------------

        if not internship_query:

            return jsonify({

                "status":
                    "error",

                "message":
                    "Internship search query is required."

            }), 400


        # ----------------------------------------------------
        # RESUME FILE
        # ----------------------------------------------------

        resume_file = request.files.get(
            "resume"
        )


        if not resume_file:

            return jsonify({

                "status":
                    "error",

                "message":
                    "Resume PDF is required."

            }), 400


        if resume_file.filename == "":

            return jsonify({

                "status":
                    "error",

                "message":
                    "Please select a resume file."

            }), 400


        if not allowed_file(
            resume_file.filename
        ):

            return jsonify({

                "status":
                    "error",

                "message":
                    "Only PDF resume files are supported."

            }), 400


        # ----------------------------------------------------
        # SAVE RESUME
        # ----------------------------------------------------

        filename = secure_filename(
            resume_file.filename
        )

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        resume_file.save(
            filepath
        )

        print("\nResume saved:")
        print(filepath)


        # ----------------------------------------------------
        # EXTRACT PDF TEXT
        # ----------------------------------------------------

        print("\nExtracting resume text...")

        reader = PdfReader(
            filepath
        )

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:

                resume_text += (
                    text + "\n"
                )


        print(
            "Resume text extracted."
        )

        print(
            "Characters:",
            len(resume_text)
        )


        # ----------------------------------------------------
        # RESUME AGENT
        # ----------------------------------------------------

        print("\n================================")
        print("RESUME AGENT")
        print("================================")

        try:

            resume_data = (
                resume_agent.analyze_resume(
                    resume_text
                )
            )

        except Exception as e:

            print(
                "Resume Agent error:"
            )

            print(e)

            # Local fallback
            resume_data = {

                "name": "",

                "skills": [],

                "education": [],

                "experience": [],

                "projects": [],

                "certifications": []

            }


        # ----------------------------------------------------
        # ADD USER ENTERED SKILLS
        # ----------------------------------------------------

        resume_skills = resume_data.get(
            "skills",
            []
        )


        if isinstance(
            resume_skills,
            str
        ):

            resume_skills = [
                skill.strip()
                for skill in resume_skills.split(",")
                if skill.strip()
            ]


        # Add manually entered skills

        if skills:

            manual_skills = [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ]

            for skill in manual_skills:

                if skill.lower() not in [
                    s.lower()
                    for s in resume_skills
                ]:

                    resume_skills.append(
                        skill
                    )


        resume_data["skills"] = (
            resume_skills
        )


        # ----------------------------------------------------
        # ADD STUDENT INFORMATION
        # ----------------------------------------------------

        resume_data["year"] = year

        resume_data["branch"] = branch


        print("\nResume Analysis:")

        print(
            resume_data
        )


        # ----------------------------------------------------
        # AGENTIC ORCHESTRATOR
        # ----------------------------------------------------

        print("\n================================")
        print("AGENTIC ORCHESTRATOR")
        print("================================")


        results = (
            orchestrator.process(
                resume_data,
                internship_query
            )
        )


        # ----------------------------------------------------
        # RETURN RESPONSE
        # ----------------------------------------------------

        return jsonify({

            "status":
                "success",

            "message":
                results.get(
                    "message",
                    "Internships discovered successfully."
                ),

            "resume_data":
                resume_data,

            "resume_text":
                resume_text,

            "jobs":
                results.get(
                    "jobs",
                    []
                )

        })


    except Exception as e:

        print("\n================================")
        print("FIND INTERNSHIPS ERROR")
        print("================================")

        print(e)

        return jsonify({

            "status":
                "error",

            "message":
                str(e)

        }), 500


# ============================================================
# ANALYZE SELECTED INTERNSHIP
# ============================================================

@app.route(
    "/api/analyze-internship",
    methods=["POST"]
)
def analyze_internship():

    try:

        print("\n================================")
        print("INTERNSHIP ANALYSIS REQUEST")
        print("================================")


        data = request.get_json()


        if not data:

            return jsonify({

                "status":
                    "error",

                "message":
                    "No internship data received."

            }), 400


        # ----------------------------------------------------
        # GET DATA
        # ----------------------------------------------------

        resume_data = data.get(
            "resume_data",
            {}
        )

        job = data.get(
            "job",
            {}
        )

        match_result = data.get(
            "match_result",
            {}
        )


        if not job:

            return jsonify({

                "status":
                    "error",

                "message":
                    "Job information is required."

            }), 400


        # ----------------------------------------------------
        # SKILL GAP AGENT
        # ----------------------------------------------------

        print("\nStarting Skill Gap Agent...")


        skill_gap_result = (
            orchestrator
            .skill_gap_agent
            .analyze_skill_gaps(
                resume_data,
                job,
                match_result
            )
        )


        print(
            "\nSkill Gap Result:"
        )

        print(
            skill_gap_result
        )


        # ----------------------------------------------------
        # RETURN RESULT
        # ----------------------------------------------------

        return jsonify({

            "status":
                "success",

            "message":
                "Internship analysis completed.",

            "job":
                job,

            "match":
                match_result,

            "skill_gap":
                skill_gap_result

        })


    except Exception as e:

        print("\n================================")
        print("INTERNSHIP ANALYSIS ERROR")
        print("================================")

        print(e)


        return jsonify({

            "status":
                "error",

            "message":
                str(e)

        }), 500


# ============================================================
# PREPARE INTERNSHIP APPLICATION
# ============================================================

@app.route(
    "/api/prepare-application",
    methods=["POST"]
)
def prepare_application():

    try:

        print("\n================================")
        print("APPLICATION AGENT STARTED")
        print("================================")


        # ----------------------------------------------------
        # GET JSON DATA
        # ----------------------------------------------------

        data = request.get_json()


        if not data:

            return jsonify({

                "status":
                    "error",

                "message":
                    "No application data received."

            }), 400


        # ----------------------------------------------------
        # EXTRACT DATA
        # ----------------------------------------------------

        resume_data = data.get(
            "resume_data",
            {}
        )

        job = data.get(
            "job",
            {}
        )

        match_result = data.get(
            "match_result",
            {}
        )


        # ----------------------------------------------------
        # VALIDATE DATA
        # ----------------------------------------------------

        if not job:

            return jsonify({

                "status":
                    "error",

                "message":
                    "Job information is required."

            }), 400


        if not resume_data:

            return jsonify({

                "status":
                    "error",

                "message":
                    "Resume information is required."

            }), 400


        # ----------------------------------------------------
        # PRINT SELECTED JOB
        # ----------------------------------------------------

        print("\nSelected Job:")

        print(
            job.get(
                "title",
                "Unknown"
            )
        )


        print("\nCompany:")

        print(
            job.get(
                "company",
                "Unknown"
            )
        )


        print("\nMatch Score:")

        print(
            match_result.get(
                "score",
                0
            )
        )


        # ----------------------------------------------------
        # APPLICATION AGENT
        # ----------------------------------------------------

        print(
            "\nCalling Application Agent..."
        )


        application_result = (
            orchestrator
            .application_agent
            .prepare_application(
                resume_data,
                job,
                match_result
            )
        )


        # ----------------------------------------------------
        # PRINT RESULT
        # ----------------------------------------------------

        print(
            "\nApplication Agent Result:"
        )

        print(
            application_result
        )


        # ----------------------------------------------------
        # RETURN RESPONSE
        # ----------------------------------------------------

        return jsonify({

            "status":
                "success",

            "message":
                "Application preparation completed.",

            "job":
                job,

            "match":
                match_result,

            "application":
                application_result

        })


    except Exception as e:

        print("\n================================")
        print("APPLICATION AGENT ERROR")
        print("================================")

        print(e)


        return jsonify({

            "status":
                "error",

            "message":
                str(e)

        }), 500


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route(
    "/api/health",
    methods=["GET"]
)
def health_check():

    return jsonify({

        "status":
            "success",

        "message":
            "Backend is running.",

        "agents": {

            "resume_agent":
                "online",

            "job_discovery_agent":
                "online",

            "matching_agent":
                "online",

            "skill_gap_agent":
                "online",

            "application_agent":
                "online"

        }

    })


# ============================================================
# RUN FLASK
# ============================================================

if __name__ == "__main__":

    print("\n================================")
    print("AGENTIC AI CAREER ASSISTANT")
    print("================================")

    print(
        "\nBackend running at:"
    )

    print(
        "http://127.0.0.1:5000"
    )

    print("\nAvailable APIs:")

    print(
        "POST /api/find-internships"
    )

    print(
        "POST /api/analyze-internship"
    )

    print(
        "POST /api/prepare-application"
    )

    print(
        "GET /api/health"
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )