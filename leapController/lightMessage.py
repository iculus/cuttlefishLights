#!/usr/bin/python

import os, signal, sys, inspect, thread, time, random, struct
from numpy import interp, zeros, chararray, reshape, append, array, roll, fliplr, where

sys.path.insert(0,'/home/admin/Desktop/cuttlefishLights/leapController/')
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess

from patterns import heart, dot, diagonalLine, chevronLine
from sercoms import sendIt, setupSerial
from procCtl import setupProcess

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
		return str(self.topic) + ',' + str(self.messagedata)


if __name__ == "__main__":
	# setup area #
	ser = setupSerial()
	simulator2 = chevronLine()
	simulator3 = diagonalLine()
	simulator4 = dot(5,9,4)
	simulator5 = heart(4)
	count = 0
	maxCount = 22
	numFing = 0
	currentTime = lastTime = time.time()
	delay = 0
	worked = True

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

	#body of program
	while time.time()-timeStart < 20:
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
				#flips and copies
				simulator1=fliplr(simulator2)
				#sets color
				simulator2=where(simulator2 == 0, simulator2,finger+1)
				simulator1=where(simulator1 == 0, simulator2,5)
				#merges
				newSim=where(simulator2 != 0, simulator2,simulator1)
				#moves
				simulator2=roll(simulator2, 1,1)
				simulator1=roll(simulator1, 1,1)
				
				lastTime = currentTime
				count = count + 1
				if count >= maxCount:count = 0			

			#show
			sendIt(newSim, numFing, ser)

	#end threads
	lThread.join()
	
	
