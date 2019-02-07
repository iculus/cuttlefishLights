#!/usr/bin/python

import os, signal, sys, inspect, thread, time, random, struct
from numpy import interp, zeros, chararray, reshape, append, array, roll, fliplr, where, add

sys.path.insert(0,'/home/admin/Desktop/cuttlefishLights/leapController/')
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess

from patterns import *
from sercoms import sendIt, setupSerial
from procCtl import setupProcess, set_procname

from sockets import *

if __name__ == "__main__":
	# setup area #
	ser = setupSerial()
	newSim = dot(1,1,35)
	simulator2 = chevronLine(False)
	simulator3 = diagonalLine()
	simulator4 = dot(5,9,4)
	simulator5 = heart(4)
	simulator6 = makeSaw(76)
	ranger=volts=button = 0

	count = 0
	maxCount = 22
	numFing = 0
	currentTime = lastTimeDelay = lastTimeMode = time.time()
	worked = True
	set_procname("crystalz-light")
	
	#mode setup
	delay = 0.0
	modeDelay = 1
	maxMode = 15
	oneMode = True
	thisMode = 0
	mode = thisMode
	fade = False

	#states
	state = 0
	switch = 1
	state2 = 0
	bright = 0
	sign = 1

	#for fingers and demo chosing 
	demo = True
	justSawFingers = False
	decayTimeStart = time.time()

	#setupProcess("leapd", "sudo leapd &")

	#pusubsetup
	port = "5556"
	socketA = setupListenSocket(port,"10001")
	'''
	port = "5556"
	context = zmq.Context()
	socket = context.socket(zmq.SUB)
	socket.connect ("tcp://localhost:%s" % port)
	topicfilter = "10001"
	socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
	'''
	# end of setup area #

	#setup Timers
	timeStart = time.time()

	#start threads
	lThreadA = startThreads(socketA, listenThread())

	#lThread = listenThread()
	#lThread.start()

	count = 0

	#body of program
	while True:

		print ranger, volts, button

		#update
		currentTime = time.time()

		
		#get fingers info			
		fingerUpdate = False
		fingerTopic = 0
		fingerPos = 0,0
		fingerNum = 0

		fingInfo = str(lThreadA).replace(" ", "")
		if fingInfo != "NONE": 
			fingerTopic, fingerPos, fingerNum = fingInfo.split(":")
			fingerPos = fingerPos.strip('[').strip(']').split('),(')

		if len(fingerPos) > 2:
			for index,fing in enumerate(fingerPos):
				x,y,z = fing.strip('(').strip(')').split(',')
				thisFing = (int(x), int(y), int(z))
				#print index,thisFing
				fingerPos[index] = thisFing
			fingerUpdate = True

		fingerNum = int(fingerNum)
		#have finger info
		

		if fingerNum == 0: demo = True
		if fingerNum > 0 and not fingerUpdate: demo = True			
		if fingerNum > 0 and fingerUpdate: demo = False
		
		if (currentTime - lastTimeMode) > modeDelay:
			if oneMode: mode = thisMode
			if not oneMode: mode += 1;
			if mode > maxMode: mode = 0
			lastTimeMode = currentTime
		#print mode
		
		if (currentTime - lastTimeDelay) > delay and demo:
			
			if justSawFingers == True:
				newSim = roll(newSim,-1,0)
				fade = True
				if currentTime-decayTimeStart > 10:
					justSawFingers = False

			if justSawFingers == False:
				
				if mode == 0: 
					newSim,count = patternZero(newSim,count)
					fade = True
					#delay = 1
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
			fade = False
			delay = 0
			justSawFingers = True
			decayTimeStart = time.time()
			#print fingerPos
			newSim = dot(0,0,0)
			#print fingerNum	  
			for index, info in enumerate(fingerPos):
				color = (index*10) + 6
				if info[1] >= 0 and info[0] >= 0:
					if info[0] < 11 and info[1] < 22:
						#print info[0],info[1],color
						thisMatrix = dot(info[1],info[0],color)
						newSim = where(newSim != 0, newSim, thisMatrix)
			#print newSim, '\n'
			fingerNum = 5
			#newSim, state, switch = patternNine(state,color, switch)
			lastTimeDelay = currentTime


		#show
		if fade:
			#fingerNum = 5
			step = 5
			if bright == 0: sign = 1; count = count+12; justSawFingers = False
			print bright
			ranger, volts, button = sendIt(newSim, fingerNum, ser, bright)
			bright = bright+(step*sign)
			if bright >= 255-step+1:
				sign = -1
		if not fade:
			print "here"
			ranger, volts, button = sendIt(newSim, fingerNum, ser, 255)

	#end threads
	lThreadA.join()
	
	
