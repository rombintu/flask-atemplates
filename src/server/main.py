from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user

from .model import Templates, Users
from .config import DATABASE, UPLOAD_FOLDER
from .checksign import check
import os

main = Blueprint('main', __name__)

@login_required
@main.route('/')
def index():
    engine = create_engine(DATABASE)
    Session = sessionmaker(bind=engine)
    session = Session()
    templates = session.query(Templates).all()
    session.close()
    return render_template('index.html', templates=templates)


@main.route('/upload', methods=['POST'])
def upload():
    title = request.form['title']
    path = f'{title}.html'
    desc = request.form['desc']

    mainfile = request.files['mainfile']
    keyfile = request.files['keyfile']
    signfile = request.files['signfile']

    if title == "" or not mainfile or not keyfile or not signfile:
        flash('Нужно заполнить все поля')
        return redirect(url_for('main.index'))

    # Проверка ЭЦП
    if check(mainfile.stream.read(), keyfile.stream.read(), signfile.stream.read()):
        flash('Подпись проверена')

        engine = create_engine(DATABASE)
        Session = sessionmaker(bind=engine)
        session = Session()
        new_template = Templates(title, path, desc, current_user.email)
        session.add(new_template)
        session.commit()
        session.close()
        
        mainfile.save(os.path.join(UPLOAD_FOLDER, path))
        return redirect(url_for('main.index'))
    else:
        flash('Подпись не верна')
        return redirect(url_for('main.index'))

