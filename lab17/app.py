"""
Gabriel Miravite
April 30, 2026
Lab 17: Image Uploader App
"""

import os
from flask import Flask, render_template, request, jsonify
import mysql.connector
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ---------------------------------------------------
# CONFIGURATION TO WORK WITH IMAGE
# ---------------------------------------------------
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# ---------------------------------------------------
# MYSQL CONNECTION
# ---------------------------------------------------
db_config = {
    'host' : 'localhost',
    'user' : 'flaskuser',
    'password' : 'password123',
    'database' : 'image_app'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------------------------------------------
# LOADING PAGE
# ---------------------------------------------------
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM images ORDER BY uploaded_at DESC")
    images = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html' , images = images)

# ---------------------------------------------------
# RUN APP
# ---------------------------------------------------
if __name__ == '__main__':
    app.run(debug = True)