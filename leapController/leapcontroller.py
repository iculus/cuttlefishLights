#!/usr/bin/python

import os, sys, inspect, thread, time, random, struct
		
LIB_DIR = "/home/mike/Desktop/LeapDeveloperKit_2.3.1+31549_linux/LeapSDK/lib"

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '/x64' if sys.maxsize > 2**32 else '/x86'

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, LIB_DIR + arch_dir)))

sys.path.insert(0, LIB_DIR)

import Leap 
from numpy import interp, zeros, chararray, reshape, append

LeapRowMin = -140
LeapRowMax = 140
M0RowMin = 11
M0RowMax = 0
LeapColMin = 50
LeapColMax = 400
M0ColMin = 0
M0ColMax = 22
LeapZMin = -50
LeapZMax = 50
M0ZMin = 100
M0ZMax = 0



fingerListLeft = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
fingerListRight = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
def resetFings():
	allFings = [(-1,-1,-1),(-1,-1,-1),(-1,-1,-1),(-1,-1,-1),(-1,-1,-1),(-1,-1,-1),(-1,-1,-1),(-1,-1,-1),(-1,-1,-1),(-1,-1,-1)]
	return allFings
	
def resetSim():
	return zeros([M0ColMax,M0RowMin])
def resetSim2():
	c = chararray([M0ColMax,M0RowMin])
	c[:] = '.'
	return c
	
class SampleListener(Leap.Listener):

	def on_connect(self,controller):
		print "connected"
		
	def on_focus_gained(self, controller):
		print "Focused"

	def on_frame(self, controller):
		frame = controller.frame() 
		extended_fingers = frame.fingers.extended()
		hands = frame.hands
		
		numFing = len(extended_fingers)
		
		allFings = resetFings()
		
		for f in extended_fingers:
		
			def returnCalibratedPosition(uncalPos, sensorMin, sensorMax, lightMin, lightMax):
				calibrated = clamp(uncalPos,sensorMin,sensorMax)
				calibrated = int( interp(calibrated,[sensorMin,sensorMax],[lightMin,lightMax]) )
				return calibrated
		
			thisRow = returnCalibratedPosition(
				f.stabilized_tip_position[0],LeapRowMin,LeapRowMax,M0RowMin,M0RowMax)
			thisCol = returnCalibratedPosition(
				f.stabilized_tip_position[1],LeapColMin,LeapColMax,M0ColMin,M0ColMax)
			thisZ = returnCalibratedPosition(
				f.stabilized_tip_position[2],LeapZMin,LeapZMax,M0ZMin,M0ZMax)
			'''
			if f.hand.is_left:
				fingerListLeft[f.type] = (thisRow,thisCol,thisZ)
			if f.hand.is_right:
				fingerListRight[f.type] = (thisRow,thisCol,thisZ)
			'''
			
			if f.hand.is_left:
				allFings[f.type] = (thisRow,thisCol,thisZ)
			if f.hand.is_right:
				allFings[f.type+5] = (thisRow,thisCol,thisZ)			
		
		simulator = resetSim()
		if numFing !=0:
			for fingDex, thisFing in enumerate(allFings):
				if thisFing[1]<22 and thisFing[1]>=0 and thisFing[0]<11 and thisFing[0]>=0:
					simulator[thisFing[1]][thisFing[0]] = fingDex+1
			print '\n\n\n\n', simulator
			toSend = simulator.T
			toSend = toSend.reshape(242)
			
			#add the numfings to the end of the message
			toSend = append(toSend,numFing) 
			
			#build struct and send message
			start = chr(255)
			end = chr(254)
			message = start+struct.pack("<243B", *toSend)+end
			ser.write(message)		
			
def clamp(n, minn, maxn):
    return max(min(n, maxn), minn)

def readSerial():
	for line in ser.read():
		return line

def main():
	listener = SampleListener()
	controller = Leap.Controller()

	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)


import serial

try:
	ser = serial.Serial(port = '/dev/ttyACM1', baudrate = 9600,timeout = 0)
except:
	ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600,timeout = 0)

try:
	print 'its open'
    
	if(ser.isOpen() == False):
		ser.open()
		print 'its not open'
		
except IOError: # if port is already opened, close it and open it again and print message
	print 'error'
	ser.close()
	ser.open()

if __name__ == "__main__":
	main()
