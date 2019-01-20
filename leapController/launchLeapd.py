#!/usr/bin/env python
from subprocess import Popen, PIPE
import os, signal

def do_it():

	killProcess()

	sudo_password = 'admin'
	command = 'leapd'.split()

	p = Popen(['gnome-terminal', '-x', 'sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,universal_newlines=True, shell=False, preexec_fn=os.setpgrp)
	sudo_prompt = p.communicate(sudo_password + '\n')[1]

	status = p.wait()

	try:
		thisPID.append( get_pid('leapd') )	
	except:
		pass


from subprocess import check_output
def get_pid(name):
	try:
		return map(int,check_output(["pidof",name]).split())	
	except:
		return 'fail'

def killProcess():
	runningIDS = get_pid('leapd')
	if len(runningIDS) > 0 and 'fail' not in runningIDS:
		print 'kill them'
		for i in runningIDS:
			print i
			os.kill(i,signal.SIGTERM)
	if 'fail' in runningIDS:
		print 'all good'


if __name__ == "__main__":
	do_it()
