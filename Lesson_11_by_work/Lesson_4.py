from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    print(request)
    return 'hello, super world!', 200

with app.test_request_context('/'):
    print(request,type(request), request.method)

if __name__ == '__main__':
    app.run()