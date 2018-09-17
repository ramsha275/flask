from flask import Flask , make_response, request
app = Flask(__name__)
@app.route('/')
def index():
    response = make_response('<h1>Making a Response</h1>')
    response.set_cookie('color', 'blue')
    response.set_cookie('font' , '24')
    return response

@app.route('/c1')
def index1():
   color = request.cookies['color']
   size = request.cookies['font']
   response = make_response('<font color='+color+' size = '+size+'>  this is on my cookied value </font>')
   return response


app.run(debug=True)