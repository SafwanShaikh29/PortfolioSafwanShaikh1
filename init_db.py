import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Drop tables if they exist (allows you to re-run this script safely)
cursor.execute("DROP TABLE IF EXISTS profile")
cursor.execute("DROP TABLE IF EXISTS tech_stack")
cursor.execute("DROP TABLE IF EXISTS projects")
cursor.execute("DROP TABLE IF EXISTS experience")

# Create and populate Profile table
cursor.execute('''
    CREATE TABLE profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        title TEXT NOT NULL,
        bio TEXT NOT NULL,
        resume_file_path TEXT
    )
''')
cursor.execute('''
    INSERT INTO profile (full_name, title, bio, resume_file_path) 
    VALUES (
        'Safwan Feroz Shaikh', 
        'AI & Data Science', 
        'I transform complex data into actionable insights and robust software. Specializing in Machine Learning, real-time web applications, and scalable backend tools.', 
        'Safwan_Shaikh_Resume.pdf' 
    )
''')

# Create and populate Tech Stack table
cursor.execute('''
    CREATE TABLE tech_stack (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skill_name TEXT NOT NULL
    )
''')
skills = [('Python',), ('Java',), ('TensorFlow',), ('SQL',), ('JavaScript',)]
cursor.executemany('INSERT INTO tech_stack (skill_name) VALUES (?)', skills)

# Create and populate Projects table
cursor.execute('''
    CREATE TABLE projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date_completed TEXT,
        description TEXT NOT NULL
    )
''')
projects = [
    ('Real-Time Public Transport', 'AUG 2025', 'Live tracking system using Flask and Server-Sent Events (SSE). Integrated OpenStreetMap for continuous GPS visualization and route overlays.'),
    ('Face Mask Detection AI', 'DEC 2024', 'Computer vision system built with OpenCV and pre-trained CNN architectures, achieving 95%+ classification accuracy in real-time environments.'),
    ('Movie Recommendation Engine', 'MAY 2024', 'Data-driven hybrid model utilizing both Content-Based and Collaborative Filtering algorithms for personalized user suggestions.'),
    ('Art Gallery DB Management', '2024', 'Highly normalized MySQL architecture optimized with complex SQL subqueries, ensuring data integrity across artists, orders, and transactions.')
]
cursor.executemany('INSERT INTO projects (title, date_completed, description) VALUES (?, ?, ?)', projects)

# Create and populate Experience table
cursor.execute('''
    CREATE TABLE experience (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        organization TEXT NOT NULL,
        duration TEXT NOT NULL,
        description TEXT
    )
''')
experiences = [
    ('Machine Learning Intern', 'YBI Foundation', "DEC '25 - MAR '26", 'Applied multiple programming languages and ML technologies to design features and analyze substantial datasets within a professional pipeline.'),
    ('Fundamentals of Deep Learning', 'NVIDIA Skill Program', 'JUN 2025', 'Mastered neural network optimization techniques and loss functions, directly applying concepts to improve model training and evaluation.'),
    ('Employability & Soft Skills', 'Zensar Technologies', 'MAR - APR 2025', 'Strengthened corporate readiness, cross-team communication, and full-stack development foundations in a structured environment.')
]
cursor.executemany('INSERT INTO experience (role, organization, duration, description) VALUES (?, ?, ?, ?)', experiences)

connection.commit()
connection.close()
print("Database 'database.db' generated successfully!")