# from flask import Flask
#
# app = Flask(__name__)
#
# if __name__ == '__main__':
#     app.run(debug=True)
# Это минимальный синтаксис для FW Flask

from flask import Flask, render_template, url_for

app = Flask(__name__)

# @app.route("/")
# def index():
#     # return "index"
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


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)


