#Валидация дня рожденья пользователя, если равен текущему месяцу то ок, иначе инвалид (Lesson_3)


from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators
import datetime as dt

#list of valid date
listdate = [str(dt.date(2018,8,i)).replace('-','.') for i in range(1,32)]


class ContactForm(FlaskForm):
    name = StringField(validators = [
        validators.Length(min = 4, max = 30)
    ])

    email = StringField(validators = [
        validators.Length(min=6, max=50),
        validators.Email()
    ])

    job = StringField(validators=[
        validators.Length(min=2, max=8),
        validators.Required(),
        validators.AnyOf('IT' 'HR' 'BANK')
    ])

    date = StringField(validators=[
        validators.Length(min=10, max=10),
        validators.AnyOf(listdate)
    ])


app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'SECRET KEY MUST BE SECRET',
    WTF_CSRF_ENABLED = False
)

@app.route('/', methods=['GET','POST'])
def req():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    elif request.method == 'GET':
        return 'It\'s GET request', 200


if __name__ == '__main__':
    app.run()