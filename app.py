from flask import Flask, request, jsonify
import sqlite3
import os
from werkzeug.utils import secure_filename
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

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


EMAIL_ADDRESS = 'seuemail@gmail.com'  # Substitua pelo e-mail da sua empresa
EMAIL_PASSWORD = 'sua_senha'  # Substitua pela senha do seu e-mail

def send_email(subject, recipient, body):
    """Função para enviar e-mails."""
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server.send_message(msg)
            logging.info(f"E-mail enviado para {recipient}")
    except Exception as e:
        logging.error(f"Erro ao enviar e-mail: {str(e)}")


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


        subject = f"Novo Currículo: {name}"
        body = f"""
Novo Currículo Recebido!
Nome: {name}
Email: {email}
Telefone: {phone}
Cargo Desejado: {position}
"""
        send_email(subject, EMAIL_ADDRESS, body)

        return jsonify({"message": "Resume submitted and email sent successfully"}), 200
    else:
        return jsonify({"error": "No resume file provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
