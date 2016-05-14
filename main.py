from flask import Flask, render_template, redirect, flash, url_for, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
import os
from update import Num, db1, A, B
from view import C
from huffman import HFCode
#from alert import D, Fl, db2
import datetime
from collections import defaultdict 

numinstance = Num()
Ainstance = A()
Binstance = B()
Cinstance = C()
#Dinstance = D()
HF = HFCode()
now=datetime.datetime.now()

app = Flask(__name__)
app.secret_key = 'super secret key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
	email = Column(String, primary_key= True)
	name = Column(String)
	cid = Column(Integer)
	password = Column(String)
	stflag = Column(Integer, default= 0)


@app.route('/')
def homepage():	
	"""day=now.day
	if day % 7 == 0:
		flag = db.session.query(User).filter_by(date=day)
		if flag is None:
			q = db.session.query(Fl).all()
			for qeach in q:
				if qeach.date != day:
					Dinstance.malert(qeach.email)"""
	return render_template("homepage.html")
    
@app.route('/homepage.html')
def homepage1():
    return render_template("homepage.html")
		
    
@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/Register_student' , methods=['GET','POST'])
def registerforstudent():
	if request.method == 'GET':
		return render_template('registerforstudent.html')
	else:
		try:
			p=request.form['password']
			c=request.form['Cpassword']
			a=request.form['akey']
			stflag=0
			txt=request.form['email']
			symb2freq = defaultdict(int)
			for ch in txt:
				symb2freq[ch] += 1
			huff = HF.encode(symb2freq)
			huffcode= HF.encode1(txt,huff)
			print (huffcode)
			user1 = User(email=huffcode, name=request.form['name'],cid=request.form['prn'],password=request.form['password'], stflag=stflag)
			num1 = Num(prn=request.form['prn'])
			if p == c:
				if a == '3532':
					db.session.add(user1)
					db1.session.add(num1)
					db.session.commit()
					db1.session.commit()
					flash('User successfully registered')
		except Exception, e:
			flash(e)
			return redirect(url_for('registerforstudent'))
	return redirect(url_for('homepage'))
	

@app.route('/Register_teacher' , methods=['GET','POST'])
def registerforteacher():
	if request.method == 'GET':
		return render_template('registerforteacher.html')
	else:
		try:
			p=request.form['password']
			c=request.form['Cpassword']
			a=request.form['akey']
			stflag=1
			txt=request.form['email']
			symb2freq = defaultdict(int)
			for ch in txt:
				symb2freq[ch] += 1
			huff = HF.encode(symb2freq)
			huffcode= HF.encode1(txt,huff)
			print (huffcode)
			user1 = User(email=huffcode , name=request.form['name'],cid=request.form['prn'],password=request.form['password'], stflag=stflag)
			if p == c:
				if a == '3532':
					db.session.add(user1)
					db.session.commit()
					for instance in db.session.query(User).order_by(User.cid):
						print(instance.name)
					flash('User successfully registered')
		except Exception, e:
			flash(e)
			return redirect(url_for('registerforteacher'))
	return redirect(url_for('homepage'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		try:
			username1 = request.form['UserName']
			password1 = request.form['Password']
			txt=request.form['UserName']
			symb2freq = defaultdict(int)
			for ch in txt:
				symb2freq[ch] += 1
			huff = HF.encode(symb2freq)
			huffcode= HF.encode1(txt,huff)
			print (huffcode)
			global registered_user
			registered_user = db.session.query(User).filter_by(email=huffcode, password=password1).first()
			if registered_user is None:
				flash('Username or Password is invalid' , 'error')
				return redirect(url_for('login'))
			elif request.form['login'] == "Teacher" and registered_user.stflag==1:
				flash("Logged in successfully")
				return redirect(url_for('course'))
			elif request.form['login'] == "Student" and registered_user.stflag==0:
				flash("Logged in successfully")
				return redirect(url_for('semester'))
			else:
				return redirect(url_for('login'))
		except Exception, e:
			flash(e)
			return redirect(url_for('login'))
	else:
		flash("Problem!!")
	return render_template("login.html")
	

@app.route('/course', methods=['GET', 'POST'])
def course():
	if request.method == 'GET':
		return render_template("course.html")
	else:
		try:
			global sub
			sub=request.form['b1']
			print (sub)
		except Exception, e:
			flash(e)
			return redirect(url_for('course'))			
	return redirect(url_for('eregister'))

@app.route('/eregister', methods=['GET', 'POST'])
def eregister():
	if request.method == 'GET':
		return render_template("eregister.html", Ainst=Ainstance, sub=sub)
	else:
		try:
			Binstance.adds(sub)
			checks=request.form.getlist('attended')
			Binstance.add1(sub,checks)
		except Exception, e:
			flash(e)
			return redirect(url_for('eregister'))
	return redirect(url_for('course'))
			
    
@app.route('/logout.html')
def logout():
	db.session.close()
	db1.session.close()
	return render_template("logout.html")
    
@app.route('/attend.html')
def attend():
	try:
		print(registered_user.email)
		email = registered_user.email
		prn = registered_user.cid
		name = registered_user.name
		curr = db1.session.query(Num).filter_by(prn = registered_user.cid).first()
		data=Cinstance.v(curr)
		data2 = Cinstance.w(data)
		"""q = db2.session.query(Fl).filter_by(fid = prn)
		if q is None:
			db2.session.add(fid = curr.prn, email=email)
			db2.session.commit()"""
		return render_template("attend.html", name=name, prn=prn, data=data, data2=data2)
	except Exception, e:
		flash(e)
		return redirect(url_for('semester'))
    
@app.route('/semester.html')
def semester():
    return render_template("semester.html")


if __name__ == '__main__':
	app.run(debug=True)



