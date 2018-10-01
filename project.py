from flask import Flask , render_template ,  request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ramsha:9876@localhost/tododb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

class tasks(db.Model):
    id = db.Column('list_id' , db.Integer , primary_key=True)
    list = db.Column( db.String(50) )

    def __init__(self, list):
        self.list = list

    @app.route('/')
    def show_all():
            return render_template('show.html', tasks=tasks.query.all())

    @app.route('/insert', methods=['GET', 'POST'])
    def add( ):
        if request.method == 'POST':
            if not request.form['list'] :
                print ("Error")
            else:
                task = tasks(request.form['list'])

            db.session.add(task)
            db.session.commit()
            return redirect(url_for('show_all'))
        return render_template('add.html')

db.create_all()
app.run( debug=True)