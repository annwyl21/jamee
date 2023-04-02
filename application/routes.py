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
