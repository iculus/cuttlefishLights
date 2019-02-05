#!/usr/bin/python

import os, signal, sys, inspect, thread, time, random, struct
from numpy import interp, zeros, chararray, reshape, append, array, roll, fliplr, where, add

sys.path.insert(0,'/home/admin/Desktop/cuttlefishLights/leapController/')
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess

from patterns import *
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
			self.messagedata = string

	def join(self, timeout=None):
		""" Stop the thread. """
		self._stopevent.set(  )
		threading.Thread.join(self, timeout)

	def __str__(self):
		""" info to send back to main process """
		return str(self.messagedata)


if __name__ == "__main__":
	# setup area #
	ser = setupSerial()
	newSim = dot(1,1,35)
	simulator2 = chevronLine(False)
	simulator3 = diagonalLine()
	simulator4 = dot(5,9,4)
	simulator5 = heart(4)
	simulator6 = makeSaw(76)
	count = 0
	maxCount = 22
	numFing = 0
	currentTime = lastTimeDelay = lastTimeMode = time.time()
	delay = 0.0
	modeDelay = 8
	worked = True
	set_procname("crystalz-light")
	maxMode = 15
	oneMode = False
	thisMode = 1
	mode = thisMode
	state = 0
	switch = 1
	state2 = 0
	bright = 0
	sign = 1
	demo = True
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
			fade = False
			currentTime = time.time()


			try:print lThread.replace(" ", "")
			except: pass

			finger = 0
			numFing = 0

			if finger == 0: demo = True
			if finger > 0: demo = False
			
			if (currentTime - lastTimeMode) > modeDelay:
				if oneMode: mode = thisMode
				if not oneMode: mode += 1;
				if mode > maxMode: mode = 0
				lastTimeMode = currentTime
			
			if (currentTime - lastTimeDelay) > delay and demo:
				
				if mode == 0: 
					newSim,count = patternZero(newSim,count)
					fade = False
				if mode == 1: 
					newSim, simulator2 = patternOne(simulator2,35,65)
				if mode == 2: newSim, simulator2 = patternTwo(simulator2,32,65)
				if mode == 3: newSim, simulator2 = patternThree(simulator2,35,65)
				if mode == 4: newSim, simulator2 = patternFour(simulator2,32,65)
				if mode == 5: newSim, simulator2 = patternFive(simulator2)
				if mode == 6: newSim, simulator2 = patternSix(simulator2,32,65)
				if mode == 7: newSim, simulator2 = patternFour(simulator2,32,65)
				if mode == 8: newSim, simulator2 = patternEight(simulator2,33,64)
				if mode == 9: newSim, state, switch = patternNine(state,34, switch)
				if mode == 10:newSim, simulator6, state2 = patternTen(simulator6,state2,44)
				if mode == 11:
					newSim, simulator6, state2 = patternTen(simulator6,state2,44)
					newSim =  where(simulator5!=0,simulator5,newSim)
				if mode == 12:
					newSim, state, switch = patternNine(state,34, switch)
					newSim =  where(simulator5!=0,simulator5,newSim)
				if mode == 13:
					newSim, simulator6, state2 = patternTen(simulator6,state2,44)
					newSim =  where(simulator5==0,simulator5,newSim)
				if mode == 14:
					newSim, state, switch = patternNine(state,34, switch)
					newSim =  where(simulator5==0,simulator5,newSim)
				if mode == 15:
					fade = True
					newSim = simulator5

				lastTimeDelay = currentTime

			if (currentTime - lastTimeDelay) > delay and not demo:
				color = (finger*10) + 6
				#print color
				newSim, state, switch = patternNine(state,color, switch)
				lastTimeDelay = currentTime
	

			#show
			if fade:
				step = 1
				if bright == 0: sign = 1
				sendIt(newSim, numFing, ser, bright)
				bright = bright+(step*sign)
				if bright >= 255-step+1:
					sign = -1
			if not fade:
				sendIt(newSim, numFing, ser, 255)

	#end threads
	lThread.join()
	
	
