#1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']

#Мой вариант решения
# from flask import Flask
# from flask.json import jsonify
#
# def open_file(filename):
#     f = open(filename)
#     info = f.read()
#     f.close
#     return info
#
#
# app = Flask(__name__)
# app.config.update(
#     DEBUG = True
# )
#
# @app.route('/locales')
# def masjson():
#     return open_file('somefile.json')
#
#
# if __name__ == '__main__':
#     app.run()


#Вариант решения от участников (используется метод jsonify (прочитать про него)
from flask import Flask,jsonify


app = Flask(__name__)
app.config.update(
    DEBUG = True
)


@app.route('/locales', methods =['GET', 'POST'])
def my_dict():
    my_locale = {'ru': 'russian', 'en': 'english', 'it': 'italian'}
    return jsonify(my_locale)


if __name__ == '__main__':
    app.run()

