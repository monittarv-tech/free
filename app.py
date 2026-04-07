from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create DB + table
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            budget TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        budget = request.form['budget']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO projects (title, description, budget) VALUES (?, ?, ?)",
                       (title, description, budget))

        conn.commit()
        conn.close()

        return redirect('/projects')

    return render_template('post_project.html')

@app.route('/projects')
def view_projects():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    data = cursor.fetchall()

    conn.close()

    return render_template('projects.html', projects=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)