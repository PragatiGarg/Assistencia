from flask import Flask, render_template, redirect, flash, url_for, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from flask_mail import Mail, Message
import os
import time


app2 = Flask(__name__)
app2.secret_key = 'super secret key'
basedir = os.path.abspath(os.path.dirname(__file__))
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db2 = SQLAlchemy(app2)


class Fl(db2.Model):
	email = Column(String)
	date = Column(Integer, default = 1)
	fid = Column(Integer)
	
	def __init__(self, email, date, fid):
		self.email = email
		self.date = date
		self.fid = fid
	
app2.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'qragatigarg@gmail.com',
	MAIL_PASSWORD = 'qragati11'
	)
mail=Mail(app2)

class D:
	def malert(self,email1):
		msg = Message('Attendance ALERT!!',sender='pragati.garg@sitpune.edu.in', recipients=[email1])
		msg.body = "Your attendace is below 68%."
		#msg.html = "<h3 class>{{ prn }}</h3><h1><b>{{ name }}<h1><table width='100%'><tr><td><h2><b>Total attendance<h2><td ><h3><b>{{ data[0] }}%</b><h3></tr><tr><td><h3>Operating System<h3><td ><h4>{{ data[2] }}%<h4></tr><tr><td><h3>Microprocessor Techniques<h3><td ><h4>{{ data[6] }}%<h4></tr><tr><td><h3>Engineering Mathematics III<h3><td ><h4>{{ data[4] }}%<h4></tr><tr><td><h3>Data Structure<h3><td ><h4>{{ data[1] }}%<h4></tr><tr><td><h3>Software Engineering<h3><td ><h4>{{ data[3] }}%<h4></tr><tr><td><h3>Java and Web Technologies<h3><td ><h4>{{ data[5] }}%<h4></tr></table>"
		mail.send(msg)
		print("Sent")	
