from flask import render_template

from main import app


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
