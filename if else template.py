from flask import Flask , render_template
app = Flask(__name__)

@app.route('/<action>')
def index(action):
    args={}
    args['para'] = "ramsha"
    args['action'] = action
    return render_template('greet_case.html' , args = args)

app.run(debug=True)

