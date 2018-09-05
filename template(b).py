from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route("/user")
def user():
    return "<h3> Proceed </h3>"

@app.route("/user/<name>")
def dummy(name):
    return render_template('greet.html' ,name=name)

app.run(debug=True)

