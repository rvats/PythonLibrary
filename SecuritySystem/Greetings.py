import datetime as dt
from datetime import time

def GetGreetingMessage():
	greeting = "Hello! How are you?"
	today = dt.datetime.now()
	now = today.time()
	# print(today)
	# print(now)
	
	# Set The Engine Greetings
	if time(4,0) <= now <= time(11,00):
		greeting = 'Good morning. ' + greeting
	elif time(11,1) <= now <= time(16,00):
		greeting = 'Good after noon. ' + greeting
	else:
		greeting = 'Good night. '
	
	return greeting