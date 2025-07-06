from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("student.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        clas = request.form['class']
        db = get_db()
        db.execute("INSERT INTO Students (name, roll_no, class) VALUES (?, ?, ?)", (name, roll, clas))
        db.commit()
        return redirect('/')
    return render_template('add_student.html')

@app.route('/add_marks', methods=['GET', 'POST'])
def add_marks():
    db = get_db()
    students = db.execute("SELECT * FROM Students").fetchall()
    subjects = db.execute("SELECT * FROM Subjects").fetchall()

    if request.method == 'POST':
        student_id = request.form['student']
        subject_id = request.form['subject']
        marks = request.form['marks']
        db.execute("INSERT INTO Marks (student_id, subject_id, marks) VALUES (?, ?, ?)",
                   (student_id, subject_id, marks))
        db.commit()
        return redirect('/')
    
    return render_template('add_marks.html', students=students, subjects=subjects)

@app.route('/view_result')
def view_result():
    db = get_db()
    results = db.execute("""
        SELECT Students.name, Students.roll_no, Subjects.name AS subject, Marks.marks
        FROM Marks
        JOIN Students ON Marks.student_id = Students.id
        JOIN Subjects ON Marks.subject_id = Subjects.id
    """).fetchall()
    return render_template('view_result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
