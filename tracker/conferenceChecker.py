import os
import time
import datetime
from threading import Timer
from subprocess import call
from pytz import timezone
import requests
import json
import split

#---declaring global variables---
start = datetime.datetime.now(timezone('UTC'))
tz = timezone('America/Denver')
startDate = start.astimezone(timezone('America/Denver'))
startTime = (startDate.strftime("%H:%M:%S"))
#Enter This Value as HH:MM without SecondS!!! In chronilogical order
classTime = ['09:00', '09:35', '10:10', '10:45']
classTimeHour = [y.split(':', 1)[0] for y in classTime]
classTimeMin = [y.split(':', 1)[1] for y in classTime]
classTimeHour =  list(map(int, classTimeHour))
classTimeMin = list(map(int, classTimeMin))
classTimeMinS = classTimeMin
classTimeHourS = classTimeHour
classTimeHour = [y * 3600 for y in classTimeHour]
classTimeMin = [y * 60 for y in classTimeMin]
classSeconds = [y + z for y,z in zip(classTimeHour, classTimeMin)]

print('---------------------')
print("It is currently", startTime)


#---Finding NextClass---
def nextClass():
	found = False
	runningTime = startDate

	while found == False or runningTime.strftime('%H:%M') == '23:59':
		runningTimeStr = (runningTime.strftime('%H:%M'))

		for x in classTime:
			if x == runningTimeStr:
				print('Next Class is at', runningTimeStr)
				print('---------------------')
				return(x)

		runningTime += datetime.timedelta(seconds=60)

	return 'ERROR in Conference Checker, Something wrong with NextClass()'

def nextClassTwo():
	found = False
	runningTime = startDate

	while found == False or runningTime.strftime('%H:%M') == '23:59':
		runningTimeStr = (runningTime.strftime('%H:%M'))

		for x in classTime:
			if x == runningTimeStr:
				print('Next Class is at', runningTimeStr)
				print('---------------------')
				return(x)

		runningTime += datetime.timedelta(seconds=60)

	return 'ERROR in Conference Checker, Something wrong with NextClass()'

nextClass = nextClass()
#nextClass = '09:35'
print(nextClass)

#---WaitForNextClass---
def calculateWait():
	dateNow = datetime.datetime.now(timezone('America/Denver'))
	#dateNow = dateNow.replace(day=9, hour=9, minute=20)
	timeNowHour = int(dateNow.hour)
	ftr = [3600, 60, 1, 0]
	if nextClass == classTime[0] and classTimeHourS[0] < timeNowHour:
		nextClassDateTime = datetime.datetime.now(timezone('America/Denver'))
		nextClassDateTime = nextClassDateTime.replace(hour=classTimeHourS[0], minute=classTimeMinS[0], second=0)
		nextClassDateTime += datetime.timedelta(days=1)
		waitTime = nextClassDateTime - dateNow
		waitTime = waitTime.total_seconds()
		return(waitTime)
	else:
		classNumber = 0
		classNum = 1
		for x in classTime:
			if x == nextClass:
				break
			else:
				classNumber += 1

		nextClassDateTime = datetime.datetime.now(timezone('America/Denver'))
		nextClassDateTime = nextClassDateTime.replace(hour=classTimeHourS[classNum], minute=classTimeMinS[classNum], second=0)
		nextClassDateTime = nextClassDateTime.replace(year=2020, month=1, day=1)
		dateNow = dateNow.replace(year=2020, month=1, day=1)
		waitTime = nextClassDateTime - dateNow
		waitTime = waitTime.total_seconds()

	return(waitTime)



waitTime = calculateWait()
print(waitTime, 'Seconds')
time.sleep(int(waitTime))
print('waiting')

#---Check For Conferences---
def checkForConferences():
	print('He he')

checkForConferences()


while True:
	nextClass = nextClassTwo()
	waitTime = calculateWait()
	time.sleep(int(waitTime))
	checkForConferences()