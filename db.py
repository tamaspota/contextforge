import csv
import sqlite3


DB_PATH = "contextforge.db"


def connect():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        project TEXT PRIMARY KEY,
        area TEXT,
        status TEXT,
        priority TEXT,
        mode TEXT,
        next_step TEXT,
        blocker TEXT,
        review_cycle TEXT,
        note TEXT,
        current_state TEXT
    )
    """)

    conn.commit()
    conn.close()


def import_tsv(path):
    conn = connect()
    cur = conn.cursor()

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for row in reader:
            cur.execute("""
            INSERT OR REPLACE INTO projects (
                project, area, status, priority, mode,
                next_step, blocker, review_cycle, note, current_state
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row.get("project", ""),
                row.get("area", ""),
                row.get("status", ""),
                row.get("priority", ""),
                row.get("mode", ""),
                row.get("next_step", ""),
                row.get("blocker", ""),
                row.get("review_cycle", ""),
                row.get("note", ""),
                row.get("current_state", ""),
            ))

    conn.commit()
    conn.close()


def get_projects():
    conn = connect()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM projects")
    rows = [dict(row) for row in cur.fetchall()]

    conn.close()
    return rows


def upsert_project(project):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO projects (
        project, area, status, priority, mode,
        next_step, blocker, review_cycle, note, current_state
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        project.get("project", ""),
        project.get("area", ""),
        project.get("status", ""),
        project.get("priority", ""),
        project.get("mode", ""),
        project.get("next_step", ""),
        project.get("blocker", ""),
        project.get("review_cycle", ""),
        project.get("note", ""),
        project.get("current_state", ""),
    ))

    conn.commit()
    conn.close()
