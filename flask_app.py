from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)