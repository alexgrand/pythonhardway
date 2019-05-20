from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    greeting = "World"
    return f'Hello, {greeting}!'


@app.route('/nihao')
def nihao_world():
    return 'Nihao, World'

if __name__ == "__main__":
    app.run()
