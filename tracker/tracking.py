import os
import threading
import schedule
import time
from datetime import datetime
from datetime import timedelta
from threading import Timer
from subprocess import call

#---startConferenceChecker---
def thread_second():
	call(["python3", "conferenceChecker.py"])
processThread = threading.Thread(target=thread_second)
processThread.start()

#---checkForAssingments---
def check():
	print('Im Looking for Assingments')

schedule.every(10).minutes.do(check)

while True:
	time = datetime.now()
	parsedTime = (time.strftime("%H:%M:%S"))
	if 