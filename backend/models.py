import sqlite3
from flask_bcrypt import Bcrypt
from flask import g

bcrypt = Bcrypt()

DATABASE = 'medcare.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Close the database connection when the request ends
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Initialize the database with necessary tables
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        role TEXT NOT NULL,
                        emergency_contact TEXT)''')

        c.execute('''CREATE TABLE IF NOT EXISTS hospitals (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        specialization TEXT NOT NULL,
                        location TEXT NOT NULL)''')

        c.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER,
                        doctor_id INTEGER,
                        hospital_id INTEGER,
                        appointment_time TEXT NOT NULL,
                        blockchain_tx TEXT,
                        FOREIGN KEY(patient_id) REFERENCES users(id),
                        FOREIGN KEY(doctor_id) REFERENCES users(id),
                        FOREIGN KEY(hospital_id) REFERENCES hospitals(id))''')

        c.execute('''CREATE TABLE IF NOT EXISTS prescriptions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER,
                        doctor_id INTEGER,
                        prescription_data TEXT NOT NULL,
                        blockchain_tx TEXT,
                        FOREIGN KEY(patient_id) REFERENCES users(id),
                        FOREIGN KEY(doctor_id) REFERENCES users(id))''')
        
        conn.commit()
