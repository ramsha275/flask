from flask import Flask , render_template

app = Flask(__name__ )
@app.route('/')
def index():
    return "Index"

@app.route("/flask")
def flask():
    return " <h3> <i> To see the introduction of the flask add 'intro' in URL </i> </h3>"

@app.route("/flask/intro")
def define():
    return render_template('flask_intro.html')

app.run(debug=True)
