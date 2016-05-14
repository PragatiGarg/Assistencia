from flask import Flask, render_template, redirect, flash, url_for, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from flask_table import Table, Col
import os
import time

app1 = Flask(__name__)
app1.secret_key = 'super secret key'
basedir = os.path.abspath(os.path.dirname(__file__))
app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db1 = SQLAlchemy(app1)

class Num(db1.Model):
	prn = Column(Integer, primary_key=True)
	sub1 = Column(Integer, default = 0)
	att1 = Column(Integer, default = 0)
	sub2 = Column(Integer, default = 0)
	att2 = Column(Integer, default = 0)
	sub3 = Column(Integer, default = 0)
	att3 = Column(Integer, default = 0)
	sub4 = Column(Integer, default = 0)
	att4 = Column(Integer, default = 0)
	sub5 = Column(Integer, default = 0)
	att5 = Column(Integer, default = 0)
	sub6 = Column(Integer, default = 0)
	att6 = Column(Integer, default = 0)
		
class A:
	result = db1.session.query(Num.prn).all()
	rolls = [r[0] for r in result]
	t=time.strftime("%d/%m/%Y") 


class B:
	def adds(self, sub):
		res = db1.session.query(Num).all()
		if sub == "Data Structures":
			for re in res:
				re.sub1=self.inc(re.sub1)
				print(re.sub1)
		elif sub == "Operating System":
			for re in res:
				re.sub2=self.inc(re.sub2)
		elif sub == "Software Engineering":
			for re in res:
				re.sub3=self.inc(re.sub3)
		elif sub == "Engeering Mathemtics III":
			for re in res:
				re.sub4=self.inc(re.sub4)
		elif sub == "Java and Web Technologies":
			for re in res:
				re.sub5=self.inc(re.sub5)
		elif sub == "Microprocessor Techniques":
			for re in res:
				re.sub6=self.inc(re.sub6)
		db1.session.commit()
		
		

	def add1(self,sub, checks):
		rf=db1.session.query(Num).filter(Num.prn.in_(checks))
		if sub == "Data Structures":
			for re1 in rf:
				re1.att1=self.inc(re1.att1)
		elif sub == "Operating System":
			for re1 in rf:
				re1.att2=self.inc(re1.att2)
		elif sub == "Software Engineering":
			for re1 in rf:
				re1.att3=self.inc(re1.att3)
		elif sub == "Engeering Mathemtics III":
			for re1 in rf:
				re1.att4=self.inc(re1.att4)
		elif sub == "Java and Web Technologies":
			for re1 in rf:
				re1.att5=self.inc(re1.att5)
		elif sub == "Microprocessor Techniques":
			for re1 in rf:
				re1.att6=self.inc(re1.att6)
		db1.session.commit()

	def inc(self,x):
		x=x+1
		return x
		

			
