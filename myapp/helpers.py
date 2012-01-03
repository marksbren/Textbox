from models import *
from views import *
from google.appengine.api import taskqueue

#The SMS Send function
def SMS_Send(TO, CALLER_ID, BODY):	
	#Twilio REST API version
	API_VERSION = '2010-04-01'

	#Twilio AccountSid and AuthToken
	ACCOUNT_SID = 'TWILIO_SID'
	ACCOUNT_TOKEN = 'TWILIO_TOKEN'

	#Create a Twilio REST account object using your Twilio account ID and token
	account = twilio.Account(ACCOUNT_SID,ACCOUNT_TOKEN)
	
	#Initiate a new SMS
	d = {
		'To' : TO,
		'From' : CALLER_ID,
		'Body' : BODY #What should this be?
	}
	account.request('/%s/Accounts/%s/SMS/Messages' % (API_VERSION, ACCOUNT_SID), 'POST', d)#TEST


def add_user(FIRST, NUMBER):
	new_user = User(number = NUMBER,nickname = FIRST)
	new_user.number = NUMBER
	new_user.nickname = FIRST
	new_user.verified = False #TODO: implement verfication
	id = new_user.put()
	return id #for adding to mobs list
	logging.debug("User signed up")