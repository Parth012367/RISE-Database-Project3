# 🎓 Student Result Management System

This is a beginner-friendly project that helps schools/colleges manage student records, including personal details, marks, and performance reports using a simple web interface built with Flask and SQLite.

---

## 📁 Folder Structure
```
Project 1/
│
├── venv/ # Virtual environment
├── app.py # Main Flask application
├── schema.sql # SQL to create tables
├── student.db # SQLite database file (created after setup)
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
│ ├── index.html
│ ├── add_student.html
│ ├── add_marks.html
│ └── view_result.html
└── static/
└── style.css # Custom styling
```

---

## ⚙️ Technologies Used

- Python
- Flask
- SQLite (can be later upgraded to MySQL/PostgreSQL)
- HTML (Jinja2 Templates)

---

## 🚀 Setup Instructions

### 1. Clone this repository / Navigate to the folder

```bash
cd "D:\Parth\Coding\Internship\RISE\Database\Project 1"
```
### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # macOS/Linux
```
### 3. Install dependencies
```bash
pip install flask
pip freeze > requirements.txt
```
### 4. Set up the SQLite database
```bash
sqlite3 student.db < schema.sql
```
``` sql
INSERT INTO Subjects (name) VALUES ('Math'), ('Science'), ('English');
.exit
```
### 5. Run the application
```bash
python app.py
```
