from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET','POST'])
def home():
    return 'hello, super world!', 200

if __name__ == '__main__':
    app.run()