from google.appengine.ext import db

class User(db.Model):
	timestamp = db.DateTimeProperty(auto_now_add=True)
	nickname = db.StringProperty()
	number = db.PhoneNumberProperty() #for identifying the owner

class Message(db.Model):
	timestamp = db.DateTimeProperty(auto_now_add=True)
	recipient = db.ReferenceProperty(User, collection_name='user_messages')
	read = db.BooleanProperty()
	content = db.StringProperty(multiline=False)