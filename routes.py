from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>welcome</h1>'

@app.route("/pakistan")
def count():
   return '<h1> <u> i love Pakistan </u> </h1>'

@app.route("/pakistan/<city>")
def country(city):
    if city=="karachi":
     return '<h2> %s is the hub of Pakistan </h2>' %city
    if city=="islamabad":
     return '<h2> %s is the capital of pakistan </h2' %city

app.run(debug = True)
