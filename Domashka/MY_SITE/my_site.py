# from flask import Flask
#
# app = Flask(__name__)
#
# if __name__ == '__main__':
#     app.run(debug=True)
# Это минимальный функционал приложения на Flask

from flask import Flask, render_template, url_for, request, flash, session, redirect

# url_for - помогает объединять пути
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fhfhfjfj44552255ff558ffff58741112'

# @app.route("/")  # Это обработчик нашего пути по слэшу
# def index():
#     # return "index"  # Вернется на странице браузера такая строка - index
#     return render_template('index.html')  # , title="Главная"
#
#
# @app.route("/about")
# def about():
#     # return "<h1> О сайте </h1>"
#     return render_template('about.html')  # , title="О нас"


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/about")
def about():
    print(url_for("about"))
    return render_template('about.html', title="О нас", menu=menu)


@app.route("/profile/<username>")  # <username> - динамическая часть пути
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category='success')
            print(request.form)
        else:
            flash("Ошибка отправки", category='error')
        # print(request.form['username'])
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message'],
        # }
        # return render_template('contact.html', **context, title="Обратная связь", menu=menu)  # post
    return render_template('contact.html', title="Обратная связь", menu=menu)  # get


@app.errorhandler(404)
def page_not_fount(error):
    return render_template("page404.html", title='Страница не найдена', menu=menu)


# http://127.0.0.1:5000/contact/fgdhdjdjdkdkd - Страница не найдена

@app.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == "POST" and request.form['username'] == "admin" and request.form['psw']
            == "123456"):
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    if 'userLogged' in session:  # теперь не видим форму авторизации
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


# http://127.0.0.1:5000/login
# http://127.0.0.1:5000/profile/admin
# Пользователь: admin

if __name__ == '__main__':
    app.run(debug=True)
