from __future__ import absolute_import

from celery import shared_task
from celery.decorators import periodic_task
from celery.schedules import crontab

from datetime import datetime
from time import gmtime, strftime
import smtplib
import traceback

from api.models import Data

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def reminder():
	date = datetime.now().strftime ("%d/%m/%Y") # considering date in dd/mm/yyyy
	time = 	strftime("%I:%M %p", gmtime())	# strftime("%Y-%m-%d %H:%M:%S", gmtime()) for time in seconds also considering time in minutes only
	#print(date + " " + time)
	obj = Data.objects.filter(date=date,time=time)
	for i in obj:
		sendEmail(i.message)
    
# i have just hard coded the toaddress field otherwise will
# have to pass it from the model object, it's easy but didn't considered it because it may require more time.  
def sendEmail(message):
	fromaddr = 'infratab.rishabh@gmail.com'
	toaddrs  = 'freaky.geek8567@gmail.com'
	msg = "\r\n".join([
		"From: infratab.rishabh@gmail.com",
		"To: freaky.geek8567@gmail.com",
		"Subject: Just a message",
		"",
		"Hello, This is Infratab, just giving you a reminder ", message
		 ]) 
	username = 'infratab.rishabh@gmail.com'
	password = 'infratab1234'         # need to encode password first using encode and decode 
	try:
		# this will be probably the email server of infratab but i am just taking gmail server for testing purpose.
		server = smtplib.SMTP(host='smtp.gmail.com', port=587)  #74.125.200.109 
		server.set_debuglevel(1)
		server.ehlo()
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()
	except:
		traceback.print_exc()
		#print ("rishabh is bad boy failed to send mail")