from google.appengine.ext import ndb

import datetime, time

class User(ndb.Model):
	# Properties
	name = ndb.StringProperty(required = True)
	pw_hash = ndb.StringProperty(required = True)
	created = ndb.DateTimeProperty(auto_now_add = True)
	
	expenses = ndb.KeyProperty(kind='Expense', repeated=True)

#-----------------------------------------------------------------------------------

class Expense(ndb.Model):
	# Properties
	amount 	 = ndb.IntegerProperty(required = True)
	category = ndb.StringProperty(required = True, default="General")
	description = ndb.StringProperty(default="")
	userKey = ndb.KeyProperty(kind='User')
	created = ndb.DateTimeProperty(auto_now_add = True)

	@staticmethod
	def getTotalForUser(user):
		return sum([expense.amount for expense in Expense.query(Expense.userKey==user.key).fetch()])

	@staticmethod
	def getAllForUser(user):
		return Expense.query(Expense.userKey==user.key).order(-Expense.created).fetch()