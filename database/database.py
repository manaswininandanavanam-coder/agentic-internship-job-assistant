import sqlite3
import os


DATABASE_FOLDER = "database"
DATABASE_FILE = os.path.join(DATABASE_FOLDER, "career_assistant.db")


def get_connection():
    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            job_title TEXT NOT NULL,

            company TEXT,

            location TEXT,

            apply_url TEXT,

            match_score REAL,

            matched_skills TEXT,

            missing_skills TEXT,

            status TEXT DEFAULT 'Saved',

            applied_date TEXT,

            notes TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    connection.close()

    print("SQLite database initialized successfully.")


if __name__ == "__main__":
    initialize_database()