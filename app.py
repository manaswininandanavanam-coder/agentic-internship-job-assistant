import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pypdf import PdfReader
from dotenv import load_dotenv

from agents.resume_agent import ResumeAgent
from agents.orchestrator import InternshipOrchestrator
from agents.application_tracking_agent import ApplicationTrackingAgent
from database.database import initialize_database

from rag.resume_indexer import ResumeIndexer
from rag.career_rag import CareerRAG


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# FLASK APPLICATION
# ============================================================

app = Flask(__name__)

CORS(app)
# Initialize SQLite database
initialize_database()


# ============================================================
# UPLOAD CONFIGURATION
# ============================================================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_text_from_pdf(filepath):

    text = ""

    reader = PdfReader(filepath)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text.strip()


# ============================================================
# INITIALIZE AI AGENTS
# ============================================================

print("\n")
print("================================")
print("INITIALIZING AI AGENTS")
print("================================")


resume_agent = ResumeAgent()

orchestrator = InternshipOrchestrator()

tracking_agent = ApplicationTrackingAgent()


# ============================================================
# INITIALIZE RAG
# ============================================================

print("\n")
print("Initializing Resume Indexer...")

resume_indexer = ResumeIndexer()


print("\n")
print("Initializing Career RAG...")

career_rag = CareerRAG()


print("\n")
print("All agents initialized.")

print("RAG Resume Indexer initialized.")

print("Career RAG initialized.")


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    try:

        return render_template("index.html")

    except Exception:

        return jsonify({
            "message": "Agentic AI Career Assistant Backend",
            "status": "running"
        })


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({

        "status": "healthy",

        "backend": "Flask",

        "frontend": "React",

        "ai": "Gemini",

        "jobs": "Adzuna",

        "rag": "ChromaDB + Sentence Transformers",

        "database": "SQLite"

    })


# ============================================================
# FIND INTERNSHIPS
# ============================================================

@app.route(
    "/api/find-internships",
    methods=["POST", "OPTIONS"]
)
def find_internships():

    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        })


    print("\n")
    print("================================")
    print("FIND INTERNSHIPS REQUEST")
    print("================================")


    try:

        # ----------------------------------------------------
        # GET SEARCH QUERY
        # ----------------------------------------------------

        internship_query = request.form.get(
            "query",
            ""
        ).strip()


        if not internship_query:

            internship_query = request.form.get(
                "internship_query",
                ""
            ).strip()


        print(
            "Internship query:",
            internship_query
        )


        if not internship_query:

            return jsonify({

                "success": False,

                "message":
                "Please enter an internship search query."

            }), 400


        # ----------------------------------------------------
        # GET RESUME
        # ----------------------------------------------------

        resume_file = request.files.get(
            "resume"
        )


        if not resume_file:

            return jsonify({

                "success": False,

                "message":
                "Please upload your resume PDF."

            }), 400


        if resume_file.filename == "":

            return jsonify({

                "success": False,

                "message":
                "Resume filename is empty."

            }), 400


        if not allowed_file(
            resume_file.filename
        ):

            return jsonify({

                "success": False,

                "message":
                "Only PDF resumes are supported."

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


        print(
            "Resume saved:",
            filepath
        )


        # ----------------------------------------------------
        # EXTRACT RESUME TEXT
        # ----------------------------------------------------

        print("\nExtracting resume text...")


        resume_text = extract_text_from_pdf(
            filepath
        )


        if not resume_text:

            return jsonify({

                "success": False,

                "message":
                "Could not extract text from the PDF."

            }), 400


        print(
            "Resume text length:",
            len(resume_text)
        )


        # ====================================================
        # RESUME AGENT
        # ====================================================

        print("\n")
        print("================================")
        print("RESUME AGENT")
        print("================================")


        try:

            resume_data = (
                resume_agent
                .analyze_resume(
                    resume_text
                )
            )


        except Exception as e:

            print(
                "Resume Agent error:"
            )

            print(e)


            resume_data = {

                "name": "",

                "skills": [],

                "education": [],

                "experience": [],

                "projects": [],

                "certifications": []

            }


        print(
            "\nResume analysis completed."
        )


        print(
            "Detected skills:",
            resume_data.get(
                "skills",
                []
            )
        )


        # ====================================================
        # RAG RESUME INDEXING
        # ====================================================

        print("\n")
        print("================================")
        print("RAG RESUME INDEXING")
        print("================================")


        try:

            resume_indexer.index_resume(
                resume_text
            )


            print(
                "Resume indexed successfully."
            )


        except Exception as e:

            print(
                "Resume indexing failed:"
            )

            print(e)


        # ====================================================
        # AGENTIC JOB WORKFLOW
        # ====================================================

        print("\n")
        print("================================")
        print("AGENTIC JOB WORKFLOW")
        print("================================")


        try:

            workflow_result = (
                orchestrator.process(
                    resume_data,
                    internship_query
                )
            )


        except Exception as e:

            print(
                "Orchestrator error:"
            )

            print(e)


            return jsonify({

                "success": False,

                "message":
                "Internship discovery failed.",

                "error":
                str(e)

            }), 500


        jobs = workflow_result.get(
            "jobs",
            []
        )


        # ====================================================
        # RESPONSE
        # ====================================================

        return jsonify({

            "success": True,

            "message":
            workflow_result.get(
                "message",
                "Internships discovered successfully."
            ),

            "resume":
            resume_data,

            "resume_text":
            resume_text,

            "resume_filename":
            filename,

            "jobs":
            jobs

        })


    except Exception as e:

        print("\n")

        print(
            "FIND INTERNSHIPS ERROR:"
        )

        print(e)


        return jsonify({

            "success": False,

            "message":
            "Something went wrong while finding internships.",

            "error":
            str(e)

        }), 500


# ============================================================
# ANALYZE SELECTED INTERNSHIP
# ============================================================

@app.route(
    "/api/analyze-internship",
    methods=["POST", "OPTIONS"]
)
def analyze_internship():

    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        })


    print("\n")
    print("================================")
    print("ANALYZE INTERNSHIP REQUEST")
    print("================================")


    try:

        data = request.get_json(
            silent=True
        ) or {}


        job = data.get(
            "job",
            {}
        )


        match_result = data.get(
            "match",
            {}
        )


        resume_data = data.get(
            "resume",
            {}
        )


        if not job:

            return jsonify({

                "success": False,

                "message":
                "Internship information is missing."

            }), 400


        job_title = job.get(
            "title",
            ""
        )


        company = job.get(
            "company",
            ""
        )


        description = job.get(
            "description",
            ""
        )


        print(
            "Job:",
            job_title
        )


        print(
            "Company:",
            company
        )


        missing_skills = match_result.get(
            "missing_skills",
            []
        )


        print(
            "Missing skills:",
            missing_skills
        )


        # ====================================================
        # RAG RETRIEVAL
        # ====================================================

        print("\n")
        print("================================")
        print("[RAG] RETRIEVING RESUME CONTEXT")
        print("================================")


        rag_query = f"""

Job Title:

{job_title}


Company:

{company}


Required Skills:

{description}


Missing Skills:

{missing_skills}

"""


        print(
            "RAG query created."
        )


        resume_context = ""


        try:

            resume_context = (
                career_rag
                .retrieve_resume_context(
                    rag_query
                )
            )


            print(
                "Resume context retrieved successfully."
            )


            print(
                "RAG context length:",
                len(resume_context)
            )


        except Exception as e:

            print(
                "RAG retrieval failed:"
            )

            print(e)


            resume_context = ""


        # ====================================================
        # SKILL GAP AGENT
        # ====================================================

        print("\n")
        print("================================")
        print("[3] SKILL GAP AGENT")
        print("================================")


        try:

            skill_gap_result = (

                orchestrator
                .skill_gap_agent
                .analyze_skill_gaps(

                    missing_skills,

                    resume_context

                )

            )


            print(
                "Skill Gap Analysis completed."
            )


        except Exception as e:

            print(
                "Skill Gap Agent error:"
            )

            print(e)


            skill_gap_result = {

                "skill_gaps": []

            }


        # ====================================================
        # RESPONSE
        # ====================================================

        return jsonify({

            "success": True,

            "job":
            job,

            "match":
            match_result,

            "resume":
            resume_data,

            "resume_context":
            resume_context,

            "skill_gap":
            skill_gap_result

        })


    except Exception as e:

        print("\n")

        print(
            "ANALYZE INTERNSHIP ERROR:"
        )

        print(e)


        return jsonify({

            "success": False,

            "message":
            "Internship analysis failed.",

            "error":
            str(e)

        }), 500


# ============================================================
# PREPARE APPLICATION
# ============================================================

@app.route(
    "/api/prepare-application",
    methods=["POST", "OPTIONS"]
)
def prepare_application():

    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        })


    print("\n")
    print("================================")
    print("PREPARE APPLICATION REQUEST")
    print("================================")


    try:

        data = request.get_json(
            silent=True
        ) or {}


        job = data.get(
            "job",
            {}
        )


        resume_data = data.get(
            "resume",
            {}
        )


        match_result = data.get(
            "match",
            {}
        )


        if not job:

            return jsonify({

                "success": False,

                "message":
                "Internship information is missing."

            }), 400


        application_agent = (
            orchestrator
            .application_agent
        )


        try:

            result = (
                application_agent
                .prepare_application(

                    resume_data,

                    job,

                    match_result

                )
            )


        except TypeError:

            try:

                result = (
                    application_agent
                    .prepare_application(

                        resume_data,

                        job

                    )
                )


            except Exception as e:

                print(
                    "Application Agent error:"
                )

                print(e)


                result = {

                    "success": False,

                    "message":
                    str(e)

                }


        except Exception as e:

            print(
                "Application Agent error:"
            )

            print(e)


            result = {

                "success": False,

                "message":
                str(e)

            }


        return jsonify({

            "success": True,

            "job":
            job,

            "application":
            result

        })


    except Exception as e:

        print("\n")

        print(
            "PREPARE APPLICATION ERROR:"
        )

        print(e)


        return jsonify({

            "success": False,

            "message":
            "Application preparation failed.",

            "error":
            str(e)

        }), 500


# ============================================================
# RAG SEARCH
# ============================================================

@app.route(
    "/api/rag-search",
    methods=["POST", "OPTIONS"]
)
def rag_search():

    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        })


    try:

        data = request.get_json(
            silent=True
        ) or {}


        query = data.get(
            "query",
            ""
        ).strip()


        if not query:

            return jsonify({

                "success": False,

                "message":
                "Please provide a search query."

            }), 400


        print("\n")
        print("================================")
        print("RAG SEARCH")
        print("================================")


        print(
            "Query:",
            query
        )


        try:

            context = (
                career_rag
                .retrieve_resume_context(
                    query
                )
            )


        except Exception as e:

            print(
                "RAG search failed:"
            )

            print(e)


            context = ""


        return jsonify({

            "success": True,

            "query":
            query,

            "context":
            context

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "message":
            "RAG search failed.",

            "error":
            str(e)

        }), 500


# ============================================================
# APPLICATION TRACKING
# ============================================================

@app.route(
    "/api/applications",
    methods=["GET", "POST", "OPTIONS"]
)
def applications():

    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        })


    try:

        # ====================================================
        # GET APPLICATIONS
        # ====================================================

        if request.method == "GET":

            applications_list = (
                tracking_agent
                .get_applications()
            )


            return jsonify({

                "success": True,

                "applications":
                applications_list

            })


        # ====================================================
        # SAVE APPLICATION
        # ====================================================

        data = request.get_json(
            silent=True
        ) or {}


        job = data.get(
            "job",
            {}
        )


        match_result = data.get(
            "match",
            {}
        )


        if not job:

            return jsonify({

                "success": False,

                "message":
                "Job information is missing."

            }), 400


        result = (
            tracking_agent
            .add_application(

                job,

                match_result

            )
        )


        return jsonify(
            result
        )


    except Exception as e:

        print(
            "Application Tracking API error:"
        )

        print(e)


        return jsonify({

            "success": False,

            "message":
            "Application tracking failed.",

            "error":
            str(e)

        }), 500


# ============================================================
# UPDATE APPLICATION STATUS
# ============================================================

@app.route(
    "/api/applications/<int:application_id>/status",
    methods=["PUT", "OPTIONS"]
)
def update_application_status(
    application_id
):

    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        })


    try:

        data = request.get_json(
            silent=True
        ) or {}


        status = data.get(
            "status",
            ""
        ).strip()


        allowed_statuses = [

            "Saved",

            "Applied",

            "Interview",

            "Selected",

            "Rejected"

        ]


        if status not in allowed_statuses:

            return jsonify({

                "success": False,

                "message":
                "Invalid application status."

            }), 400


        result = (
            tracking_agent
            .update_status(

                application_id,

                status

            )
        )


        return jsonify(
            result
        )


    except Exception as e:

        print(
            "Status update error:"
        )

        print(e)


        return jsonify({

            "success": False,

            "message":
            "Could not update application status.",

            "error":
            str(e)

        }), 500


# ============================================================
# DELETE APPLICATION
# ============================================================

@app.route(
    "/api/applications/<int:application_id>",
    methods=["DELETE", "OPTIONS"]
)
def delete_application(
    application_id
):

    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        })


    try:

        result = (
            tracking_agent
            .delete_application(

                application_id

            )
        )


        return jsonify(
            result
        )


    except Exception as e:

        print(
            "Delete application error:"
        )

        print(e)


        return jsonify({

            "success": False,

            "message":
            "Could not delete application.",

            "error":
            str(e)

        }), 500


# ============================================================
# 404 ERROR
# ============================================================

@app.errorhandler(404)
def not_found(error):

    return jsonify({

        "success": False,

        "message":
        "API endpoint not found."

    }), 404


# ============================================================
# 500 ERROR
# ============================================================

@app.errorhandler(500)
def internal_error(error):

    return jsonify({

        "success": False,

        "message":
        "Internal server error."

    }), 500


# ============================================================
# START FLASK SERVER
# ============================================================

if __name__ == "__main__":

    print("\n")
    print("========================================")
    print(" AGENTIC AI CAREER ASSISTANT")
    print("========================================")

    print(" Backend : Flask")

    print(" Frontend: React")

    print(" AI      : Gemini")

    print(" Jobs    : Adzuna")

    print(
        " RAG     : ChromaDB + Sentence Transformers"
    )

    print(" Database: SQLite")

    print("========================================")

    print(
        "Backend running at:"
    )

    print(
        "http://127.0.0.1:5000"
    )

    print("========================================")


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )