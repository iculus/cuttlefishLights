import sys
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess

def startProcess(process):
		return subprocess.call(process, shell=True)

def getPID(processName):
	try:
		return map(int,subprocess.check_output(["pidof",processName]).split())	
	except:
		return 'fail'

def killProcess(processName):
	runningIDS = getPID(processName)
	if len(runningIDS) > 0 and 'fail' not in runningIDS:
		print 'Kill Leapd Processes'
		for i in runningIDS:
			process = "sudo kill -9 " + str(i)
			print process
			print subprocess.call(process, shell=True)
	if 'fail' in runningIDS:
		print 'all good'

def setupProcess(processName, process):
	killProcess(processName)
	return_code = startProcess(process)
