from flask import Flask , render_template
app = Flask(__name__)

@app.route('/<int:num>')
def index(num):

    return render_template('odd.html' , num=num)

app.run(debug=True)

