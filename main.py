#import views
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from myapp.views import *

application = webapp.WSGIApplication([
				('/', MainPage),
				('/about', AboutPage),
				('/privacy', PrivacyPage),
				('/messageworker', MessageWorker),
				('/admin', AdminPanel),
				('/user/(.*)', UserDetails),
				('/twilio', TwilioHandler),
				], debug=True)
					
					
def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
