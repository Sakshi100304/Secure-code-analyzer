import sqlite3
# 🔹 Connect Database
def connect_db():

    conn = sqlite3.connect("scanner.db")

    return conn

# 🔹 Create Table
def create_table():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS scans (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        total_issues INTEGER,

        high_issues INTEGER,

        medium_issues INTEGER,

        low_issues INTEGER,

        risk_score INTEGER,

        scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    conn.commit()

    conn.close()


# 🔹 Insert Scan Result
def insert_scan(filename, summary):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO scans (

        filename,
        total_issues,
        high_issues,
        medium_issues,
        low_issues,
        risk_score

    )

    VALUES (?, ?, ?, ?, ?, ?)

    """, (

        filename,
        summary["total"],
        summary["high"],
        summary["medium"],
        summary["low"],
        summary["risk_score"]

    ))

    conn.commit()

    conn.close()


# 🔹 Fetch All Records
def get_all_scans():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scans")

    rows = cursor.fetchall()

    conn.close()

    return rows