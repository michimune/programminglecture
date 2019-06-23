from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body>Hello World! <img src=static/cat.jpg></body></html>"

@app.route("/now")
def now():
    return render_template('now.html', now = datetime.now())

if __name__ == "__main__":
    app.run()
