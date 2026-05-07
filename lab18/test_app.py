""" 
Gabriel Miravite
May 7, 2026
Lab 19: Unit Testing to Verify Authentication in a Flask-SQLite App
""" 

import os
import sqlite3
import pytest
from app import app

# --------------------------
# TEST DATABASE SETUP
# --------------------------
TEST_DB = "test_flask_auth.db"

def init_test_db():
    # Simulate a database connection
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    # Create a template table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL
                   )
    """)
    conn.commit()
    conn.close()

# Create a mock database to run the app.py file
@pytest.fixture
def client(monkeypatch):
    # Override database to use test database instead
    def test_get_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn
    
    # Match the mock database
    from app import get_db
    monkeypatch.setattr("app.get_db", test_get_db)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'

    # Call function to run the mock database
    init_test_db()

    # Create an instance of the Flask test client
    with app.test_client() as client:
        # yield means returns the client AND the code resumes after all tests are finished
        yield client
    
    # Clean up test database after tests
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

# --------------------------
# TEST HOME REDIRECT
# --------------------------
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.location # response.location means properly redirect to the URL location

# --------------------------
# TEST LOGIN SUCCESS
# --------------------------
def test_login_success(client):
    # First, create a user to test the login later
    client.post('/signup', data = {
        "username" : "loginuser",
        "email" : "login@example.com",
        "password" : "123456"
    })

    # Test the login with the user info above
    response = client.post('/login', data = {
        "email" : "login@example.com",
        "password" : "123456"
    }, follow_redirects = True)

    # Assert testing
    assert response.status_code == 200
    # Convert the <h1>Welcome</h1> in dashboard.html into bytes object
    assert b"Welcome" in response.data

# --------------------------
# TEST LOGIN FAILURE
# --------------------------
def test_login_failure(client):
    response = client.post('login', data = {
        "email" : "login@example.com",
        "password" : "wrong123"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert b"Invalid email or password" in response.data

# --------------------------
# TEST SIGNUP SUCCESS
# --------------------------
def test_signup(client):
    response = client.post('/signup', data = {
        "username" : "testuser",
        "email" : "test@example.com",
        "password" : "123456"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert b"Account created successfully!" in response.data