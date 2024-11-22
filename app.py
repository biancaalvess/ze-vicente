from flask import Flask, request, jsonify
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def init_db():
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS resumes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT,
                  phone TEXT,
                  position TEXT,
                  resume_path TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/submit', methods=['POST'])
def submit_resume():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    position = request.form['position']
    resume = request.files['resume']

    if resume:
        filename = secure_filename(resume.filename)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(resume_path)

        conn = sqlite3.connect('resumes.db')
        c = conn.cursor()
        c.execute("INSERT INTO resumes (name, email, phone, position, resume_path) VALUES (?, ?, ?, ?, ?)",
                  (name, email, phone, position, resume_path))
        conn.commit()
        conn.close()

        return jsonify({"message": "Resume submitted successfully"}), 200
    else:
        return jsonify({"error": "No resume file provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)

    