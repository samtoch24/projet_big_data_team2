from flask import Flask
app = Flask(__name__)

@app.route('/')
def page1():
    return "Je suis la 1ere page directement connecté sur le localhost"

@app.route('/hello')
def hello():
    return "Hello World directement connecté sr la page /hellowword"

if __name__ == 'main':
    app.run(host='127.0.0.1', port=8000)