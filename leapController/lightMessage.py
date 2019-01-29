#!/usr/bin/python

import os, signal, sys, inspect, thread, time, random, struct
from numpy import interp, zeros, chararray, reshape, append, array, roll, fliplr, where

sys.path.insert(0,'/home/admin/Desktop/cuttlefishLights/leapController/')
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess

from patterns import heart, dot, diagonalLine, chevronLine, patternOne
from sercoms import sendIt, setupSerial
from procCtl import setupProcess, set_procname

import zmq
import threading

class listenThread(threading.Thread):

	def __init__(self, name='listenThread'):
		""" constructor, setting initial variables """
		self._stopevent = threading.Event(  )
		self._sleepperiod = 1.0
		self.topic = 0
		self.messagedata = 0
		threading.Thread.__init__(self, name=name)

	def run(self):
		""" main control loop """
		while not self._stopevent.isSet(  ):
			string = socket.recv()
			self.topic, self.messagedata = string.split()

	def join(self, timeout=None):
		""" Stop the thread. """
		self._stopevent.set(  )
		threading.Thread.join(self, timeout)

	def __str__(self):
		""" info to send back to main process """
		return str(self.topic) + ',' + str(self.messagedata)


if __name__ == "__main__":
	# setup area #
	ser = setupSerial()
	newSim = dot(1,1,35)
	simulator2 = chevronLine(False)
	simulator3 = diagonalLine()
	simulator4 = dot(5,9,4)
	simulator5 = heart(4)
	count = 0
	maxCount = 22
	numFing = 0
	currentTime = lastTime = time.time()
	delay = 0.5
	worked = True
	set_procname("crystalz-light")
	#setupProcess("leapd", "sudo leapd &")

	#pusubsetup
	port = "5556"
	context = zmq.Context()
	socket = context.socket(zmq.SUB)
	socket.connect ("tcp://localhost:%s" % port)
	topicfilter = "10001"
	socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
	# end of setup area #

	#setup Timers
	timeStart = time.time()

	#start threads
	lThread = listenThread()
	lThread.start()

	count = 0

	#body of program
	while True:
	#while time.time()-timeStart < 10:
		if not worked:
			#update
			count = count + 1
			if count >= maxCount:count = 0			

			#reshape
			currentTime = time.time()
			if (currentTime - lastTime) > delay:
				simulator3=roll(simulator3, count,0)
				lastTime = currentTime
			#print simulator3

			#show
			sendIt(simulator3, numFing, ser)

		if worked:
			#update
			currentTime = time.time()
			
			if (currentTime - lastTime) > delay:
				finger = str(lThread).split(',')[1]
				finger = int(finger)
				
				newSim, simulator2 = patternOne(simulator2,52,62)
				
				lastTime = currentTime
				#count = count + 1
				#if count >= maxCount:count = 0	
			'''

			count = count + 1;
			newSim = array([[0,0,0,12,13,14,15,16,0,0,0],
					[0,0,0,22,23,24,25,26,0,0,0],
					[0,0,0,32,33,34,35,36,0,0,0],
					[0,0,0,42,43,44,45,46,0,0,0],
					[0,0,0,52,53,54,55,56,0,0,0],
					[0,0,0,62,63,64,65,66,0,0,0],
					[0,0,0,72,73,74,75,76,0,0,0],
					[0,0,0,82,83,84,85,86,0,0,0],
					[0,0,0,92,93,94,95,96,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0]])
			'''


			
			#newSim = roll(newSim,count,1)
			
		

			#show
			sendIt(newSim, numFing, ser, 255)

	#end threads
	lThread.join()
	
	
