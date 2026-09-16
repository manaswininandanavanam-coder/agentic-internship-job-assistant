import sqlite3
import json
from datetime import datetime


DATABASE_FILE = "database/career_assistant.db"


class ApplicationTrackingAgent:

    def __init__(self):

        print("Application Tracking Agent initialized")

    def add_application(self, job, match_result):

        connection = sqlite3.connect(DATABASE_FILE)

        cursor = connection.cursor()

        matched_skills = json.dumps(
            match_result.get("matched_skills", [])
        )

        missing_skills = json.dumps(
            match_result.get("missing_skills", [])
        )

        cursor.execute("""
            INSERT INTO applications (
                job_title,
                company,
                location,
                apply_url,
                match_score,
                matched_skills,
                missing_skills,
                status,
                applied_date,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            job.get("title", ""),

            job.get("company", ""),

            job.get("location", ""),

            job.get("url", "")
            or job.get("apply_url", ""),

            match_result.get("score", 0),

            matched_skills,

            missing_skills,

            "Saved",

            None,

            ""

        ))

        application_id = cursor.lastrowid

        connection.commit()

        connection.close()

        print(
            f"Application saved successfully. ID: {application_id}"
        )

        return {
            "success": True,
            "application_id": application_id,
            "status": "Saved"
        }

    def get_applications(self):

        connection = sqlite3.connect(DATABASE_FILE)

        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM applications
            ORDER BY created_at DESC
        """)

        rows = cursor.fetchall()

        connection.close()

        applications = []

        for row in rows:

            application = dict(row)

            try:
                application["matched_skills"] = json.loads(
                    application["matched_skills"] or "[]"
                )
            except Exception:
                application["matched_skills"] = []

            try:
                application["missing_skills"] = json.loads(
                    application["missing_skills"] or "[]"
                )
            except Exception:
                application["missing_skills"] = []

            applications.append(application)

        return applications

    def update_status(self, application_id, status):

        connection = sqlite3.connect(DATABASE_FILE)

        cursor = connection.cursor()

        applied_date = None

        if status == "Applied":

            applied_date = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        cursor.execute("""
            UPDATE applications

            SET status = ?,
                applied_date = COALESCE(?, applied_date)

            WHERE id = ?
        """, (

            status,

            applied_date,

            application_id

        ))

        connection.commit()

        updated = cursor.rowcount

        connection.close()

        if updated == 0:

            return {
                "success": False,
                "message": "Application not found."
            }

        return {
            "success": True,
            "message": "Application status updated.",
            "status": status
        }

    def delete_application(self, application_id):

        connection = sqlite3.connect(DATABASE_FILE)

        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM applications
            WHERE id = ?
        """, (application_id,))

        connection.commit()

        deleted = cursor.rowcount

        connection.close()

        if deleted == 0:

            return {
                "success": False,
                "message": "Application not found."
            }

        return {
            "success": True,
            "message": "Application deleted."
        }