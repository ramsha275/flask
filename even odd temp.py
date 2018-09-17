from flask import Flask , render_template
app = Flask(__name__)

@app.route('/<int:number>')
def index(number):

    return render_template('number.html' , number=number)

app.run(debug=True)

