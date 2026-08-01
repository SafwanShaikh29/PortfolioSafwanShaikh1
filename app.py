import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    
    # Fetch data from SQLite
    profile = conn.execute('SELECT * FROM profile LIMIT 1').fetchone()
    skills = conn.execute('SELECT * FROM tech_stack').fetchall()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    experience = conn.execute('SELECT * FROM experience').fetchall()
    
    conn.close()
    
    # Pass data into Jinja2 template
    return render_template('index.html', 
                           profile=profile, 
                           skills=skills, 
                           projects=projects, 
                           experience=experience)

if __name__ == '__main__':
    app.run(debug=True)