from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Karachi <br> Lahore <br> Islamabad <br></h1>'

app.run(debug = True)