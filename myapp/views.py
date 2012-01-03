import os
import logging
import string
import datetime
import re 
import twilio
from models import *
from helpers import *
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
  def get(self):
    self.post() #NEW mapping gets to post
  def post(self):
    if self.request.get('name'):
      new_user = User(number = self.request.get('number'),nickname = self.request.get('name'))
      id = new_user.put()
    users = User.all().fetch(15)
    template_values = {'users': users}
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'main.html')
    self.response.out.write(template.render(path, template_values))
	

class AdminPanel(webapp.RequestHandler):
  def get(self):
    self.post() #NEW mapping gets to post
	
  def post(self):
	  users = User.all().fetch(15)
	  template_values = {'users': users}
	  path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'main.html')
	  self.response.out.write(template.render(path, template_values))
	  
class UserDetails(webapp.RequestHandler):
  def get(self,id):
    self.post(id) #NEW mapping gets to post
  def post(self, id):
    user = User.get_by_id(int(id))
    if self.request.get('content'):
      new_message = Message(content = self.request.get('content'), recipient = user, read = False )
      id = new_message.put()
      updated_user = new_message.recipient
    else:
      updated_user = user
    template_values = {'user': updated_user}
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'user.html')
    self.response.out.write(template.render(path, template_values))
	
	

class MessageWorker(webapp.RequestHandler):
	def get(self):
		self.post() #NEW mapping gets to post
		
	def post(self):
		message = Message.get_by_id(int(self.request.get('id')))
		
		for user in User.get(message.mob.members):
			if user.number != message.sender.number and user.unsubscribed is not True: #if the member is not the one who texted in and is subscribed
				SMS_Send(user.number, '+14157993415', "%s: %s" % (message.sender.nickname, message.content)) 
				

class TwilioHandler(webapp.RequestHandler):
	def get(self):
		self.post() #NEW mapping gets to post
	
	def post(self):
		#TODO: event log stuff
		BODY = self.request.get('Body')
		INCOMING = self.request.get('From')
		ACCOUNT =  self.request.get('To') # May need to add "+1"  "+1%s" %
		body_content = BODY.split()
		
		#Is this a user?
		user_query = User.gql("WHERE number= :1", INCOMING) #get the user
		user = user_query.get()
		if user:
		  message_query = user.user_messages.filter('read =', False).order('timestamp').fetch(1)
		  if message_query:
		    message_to_send = message_query[0]
		    SMS_Send(user.number, ACCOUNT, message_to_send.content)
		    message_to_send.read = True
		    message_to_send.put()
		  else:
		    SMS_Send(user.number, ACCOUNT, "You are looking for MORE?!? Our master list doesn't show any, but others may be generous and give you more :)")
		else:
		  SMS_Send(INCOMING, ACCOUNT, "Whoa! You up already? We are still digging through all this wrapping paper looking for the master list. Hold your horses.")
			
	


class AboutPage(webapp.RequestHandler):
	def get(self):
		self.post()
	
	def post(self):
		template_values = {		}
		path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'about.html')
		self.response.out.write(template.render(path, template_values))
	

class PrivacyPage(webapp.RequestHandler):
	def get(self):
		self.post()
	def post(self):
		template_values = {		}
		path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'privacy.html')
		self.response.out.write(template.render(path, template_values))
