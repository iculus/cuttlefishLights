#!/usr/bin/python

import os, sys, inspect, thread, time
		
LIB_DIR = "/home/mike/Desktop/LeapDeveloperKit_2.3.1+31549_linux/LeapSDK/lib"

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '/x64' if sys.maxsize > 2**32 else '/x86'

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, LIB_DIR + arch_dir)))

sys.path.insert(0, LIB_DIR)

import Leap 
from numpy import interp

LeapRowMin = -140
LeapRowMax = 140
M0RowMin = 11
M0RowMax = 0
LeapColMin = 50
LeapColMax = 400
M0ColMin = 0
M0ColMax = 22

class SampleListener(Leap.Listener):

	def on_connect(self,controller):
		print "connected"

	def on_frame(self, controller):
		extended_fingers = controller.frame().fingers.extended()
		numFing = len(extended_fingers)
		for f in extended_fingers:
		
			thisRow = f.stabilized_tip_position[0]
			thisRow = clamp(thisRow,LeapRowMin,LeapRowMax)
			thisRow = int( interp(thisRow,[LeapRowMin,LeapRowMax],[M0RowMin,M0RowMax]) )
			
			thisCol = f.stabilized_tip_position[1]
			thisCol = clamp(thisCol,LeapColMin,LeapColMax)
			thisCol = int( interp(thisCol,[LeapColMin,LeapColMax],[M0ColMin,M0ColMax]) )
			print f.touch_distance, f.type, thisRow, thisCol, numFing
			#print readSerial()
			
			#build struct and send message
			start = chr(255)
			end = chr(254)

			x = thisRow #rows
			y = thisCol #columns
			fing = f.type #controls color
			depth = random.randrange(10) #controls brightness

			message = start + struct.pack("<BBBBB", x,y,fing,depth,numFing) + end

			ser.write(message)
			
			#print numFing

			#print 'writing', time.time()
			
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

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

import serial, random, struct

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
