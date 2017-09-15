from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kgisl@localhost/digital'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route("/")
def login():
	return render_template("logindrm.html")
	
@app.route("/register")
def register():
	return render_template("registrationdrm.html")
	
@app.route("/user")
def user():
	return render_template("userform.html")
	
class register(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	name=db.Column(db.String)
	email=db.Column(db.String)
	username=db.Column(db.String)
	password=db.Column(db.String)
	confirm=db.Column(db.String)
	
	def __init__(self,name,email,username,password,confirm):
		self.name=name
		self.email=email
		self.username=username
		self.password=password
		self.confirm=confirm
		
	@app.route("/register_db",methods=["GET","POST"])
	def register_db():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['username'] or not request.form['password'] or not request.form['confirm']:
				flash("Error")
			else:
				student=register(request.form['name'],request.form['email'],request.form['username'],request.form['password'],request.form['confirm'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('register'))
		return render_template("registrationdrm.html")




if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)
