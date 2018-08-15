#валидатор для Job
#1.Работы должны быть только такие: IT, Bank, HR
#2.Поле должно быть обязательным
#Валидация дня рожденья пользователя, если равен текущему месяцу то ок, иначе инвалид



from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators
import datetime as dt

#valid_date = ['2018.08.10','2018.08.11']

listdate = [str(dt.date(2018,8,i)).replace('-','.') for i in range(1,32)]
#listdate.replace

class ContactForm(FlaskForm):
    name = StringField(validators = [
        validators.Length(min=4, max=25)
    ])
    email = StringField(validators =
    [
        validators.Length(min=6, max = 35),
        validators.Email()
    ])
    job = StringField(validators = [
        validators.Length(min=2, max = 10),
        validators.Required(),
        validators.AnyOf("IT" "Bank" "HR" , 'Укажите корректное место работы' )
    ])

    date = StringField(validators=[
        validators.Length(min=2, max=10),
        validators.Required(),
        validators.AnyOf(listdate)
    ])

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret',
    WTF_CSRF_ENABLED=False,
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200

if __name__ == '__main__':
    app.run()