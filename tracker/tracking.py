import os
import threading
import schedule
import time
from datetime import datetime
from datetime import timedelta
from threading import Timer
from subprocess import call
import multiprocessing

#import other codes
import canvas
import googleClassroom

#---startConferenceCheckerOnOtherProcess---
def thread_second():
	print('StartingOTherThread')
	call(["python3", "conferenceChecker.py"])
	print('Ooga booga')
processThread = threading.Thread(target=thread_second)
processThread.start()

#---addAssignmentsToTODO---
def addAssignment():
	print('Doin YOur MOm');

#---checkForAssingments---
def check():
	print('Checking For Assignments')
	canvasCheck = []#checkCanvas()
	googleCheck = []#checkGoogle()

	if not googleCheck:
		print('No New Assignments From Classroom')
	else:
		for x in googleCheck:
			addAssignment(googleCheck[x])

	if not canvasCheck:
		print('No New Assignments From Canvas')
	else:
		for x in canvasCheck:
			addAssignment(canvasCheck[x])

schedule.every(1).minutes.do(check)

while True:
	schedule.run_pending()
	time.sleep(1)