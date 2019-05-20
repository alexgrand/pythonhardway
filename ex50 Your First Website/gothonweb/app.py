from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)


@app.route('/nihao')
def nihao_world():
    return 'Nihao, World'

if __name__ == "__main__":
    app.run()
