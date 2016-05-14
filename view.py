from flask import Flask, render_template, redirect, flash, url_for, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
import os
from update import Num, db1
import time

class C:
	def v(self,curr):
		per1=(curr.att1 * 100) / curr.sub1
		per2=(curr.att2 * 100) / curr.sub2
		per3=(curr.att3 * 100) / curr.sub3
		per4=(curr.att4 * 100) / curr.sub4
		per5=(curr.att5 * 100) / curr.sub5
		per6=(curr.att6 * 100) / curr.sub6
		tot=((curr.att1 + curr.att2 + curr.att3 + curr.att4 + curr.att5 + curr.att6) *100) / (curr.sub1 + curr.sub2 + curr.sub3 + curr.sub4 + curr.sub5 + curr.sub6)
		return [tot,per1,per2,per3,per4,per5,per6]

	def w(self, data):
		if data[0] > 75:
			d1 = data[0]
			d2 = data[0]-75
			d3 = 0
		elif data[0] < 75 and data[0] > 68:
			d1 = data[0]
			d2 = 75-data[0]
			d3 = 0
		elif data[0] < 68:
			d1 = 0
			d2 = 75 - data[0]
			d3 = data[0]
		return [d1,d2,d3]

		
		
		
