from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll TEXT,
            mobile TEXT,
            cgpa REAL,
            course TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/students", methods=["GET"])
def get_students():
    search = request.args.get("search")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    if search:
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%'+search+'%',))
    else:
        cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    conn.close()
    return jsonify(students)

@app.route("/students/count")
def count_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    conn.close()
    return jsonify({"count": count})

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, roll, mobile, cgpa, course)
        VALUES (?, ?, ?, ?, ?)
    """, (data["name"], data["roll"], data["mobile"], data["cgpa"], data["course"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Added"})

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name=?, roll=?, mobile=?, cgpa=?, course=?
        WHERE id=?
    """, (data["name"], data["roll"], data["mobile"], data["cgpa"], data["course"], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Updated"})

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)