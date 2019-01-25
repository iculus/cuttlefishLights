#!/usr/bin/python

import os, signal, sys, inspect, thread, time, random, struct
from numpy import interp, zeros, chararray, reshape, append, array, roll

sys.path.insert(0,'/home/admin/Desktop/cuttlefishLights/leapController/')
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess

from patterns import heart, dot, diagonalLine
from sercoms import sendIt, setupSerial
from procCtl import setupProcess

if __name__ == "__main__":
	# setup area #
	ser = setupSerial()
	simulator3 = diagonalLine()
	simulator4 = dot(5,9,4)
	simulator5 = heart(4)
	count = 0
	maxCount = 22
	numFing = 0
	currentTime = lastTime = time.time()
	delay = 0
	worked = True
	# end of setup area #

	setupProcess("leapd", "sudo leapd &")

	while True:
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
			count = count + 1
			if count >= maxCount:count = 0			

			#show
			sendIt(simulator5, numFing, ser)
	
