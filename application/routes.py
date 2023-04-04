from flask import render_template
from application import app


@app.route('/index')
def index():
    return render_template('index.html', title='ChipIn Home Page')


@app.route('/articles')
def articles():
    return render_template('articles.html', title='Articles')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/form')
def form_page():
    return render_template('form_page.html', title='Form Page')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')