from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Templates

from flask import Flask, render_template, request, redirect, url_for
import os

UPLOAD_FOLDER = os.getcwd() + '/src/server/static/downloads'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'insert-your-secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    engine = create_engine('sqlite:///db.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()
    templates = session.query(Templates).all()
    session.close()
    return render_template('index.html', templates=templates)


@app.route('/upload', methods=['POST'])
def upload():
    title = request.form['title']
    path = f'{title}.html'
    desc = request.form['desc']
    author = request.form['author']
    file = request.files['file']

    engine = create_engine('sqlite:///db.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()
    new_template = Templates(title, path, desc, author)
    session.add(new_template)
    session.commit()
    session.close()
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], path))

    return redirect(url_for('index'))