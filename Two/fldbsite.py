import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, g

from FDataBase import FDataBase

# import sqlite3 - модуль, который работает с нашей базой данных

DATABASE = '/tmp/flsk.db'
# DATABASE = 'flsk.db'
DEBUG = True
SECRET_KEY = "3836088ecd621a849efb2ebf91eb00c13e459641"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():  # здесь происходит соединение с базой данных
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    # return render_template('index.html', menu=dbase.get_menu(),
    #                        posts=dbase.get_posts_annonce())
    # return render_template('index.html')
    return render_template('index.html', menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    # db = get_db()
    # dbase = FDataBase(db)
    # return render_template("page404.html", title="Страница не найдена",
    #                        menu=dbase.get_menu())
    return render_template("page404.html", title="Страница не найдена",
                           menu=[])


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()
