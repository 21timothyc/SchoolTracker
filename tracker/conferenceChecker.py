import os
from datetime import datetime
from datetime import timedelta
from threading import Timer
from subprocess import call

print("Starting Program");

#---declaring global variables---
startDate = datetime.now()
startTime = (startDate.strftime("%H:%M:%S"))
classTime = ['9:00', '9:35', '10:10', '10:45']

print("It is currently", startTime)


#---Finding NextClass---
def nextClass():
	found = 'false'
	runningTime = datetime.now()
	runningTimeStr = (startDate.strftime("%H:%M"))

	while found == 'false':
		runningTimeStr = (runningTime.strftime("%H:%M"))
		for x in classTime:
			#print(type(x), "?", type(runningTimeStr))
			if x == runningTimeStr:
				print("Your next class is at :", x)
				found = 'true'
				return(x)
		runningTime += timedelta(seconds=60)

nextClass = nextClass()

#---Check For Conferences---
def checkForConferences():
	print("Checking For Conferences")


#---Setting Timer For Next Class---
d1 = (startDate.strftime("%H:%M:%S"))
timeDifference = datetime.strptime(nextClass, '%H:%M') - datetime.strptime(d1, '%H:%M:%S')
print('Checking for Conferences in', timeDifference.seconds, 'Seconds')
t = Timer(timeDifference.seconds, checkForConferences)
t.start()

















