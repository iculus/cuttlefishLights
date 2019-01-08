#!/usr/bin/python

import os, sys, inspect, thread, time, random, struct
		
LIB_DIR = "/home/mike/Desktop/LeapDeveloperKit_2.3.1+31549_linux/LeapSDK/lib"

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '/x64' if sys.maxsize > 2**32 else '/x86'

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, LIB_DIR + arch_dir)))

sys.path.insert(0, LIB_DIR)

import Leap 
from numpy import interp, zeros, chararray, reshape

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
			
			if f.hand.is_left:
				fingerListLeft[f.type] = (thisRow,thisCol,thisZ)
			if f.hand.is_right:
				fingerListRight[f.type] = (thisRow,thisCol,thisZ)
				
			#print "{:0.3f} \t {:d} \t {:d} \t {:d} \t {:d} \t {:d}".format(f.touch_distance, f.type, thisRow, thisCol, thisZ, numFing)
				
			
			
			#build struct and send message
			start = chr(255)
			end = chr(254)

			x = thisRow #rows
			y = thisCol #columns
			fing = f.type #controls color
			depth = random.randrange(10) #controls brightness

			message = start + struct.pack("<BBBBB", x,y,fing,depth,numFing) + end
			
			ser.write(message)
			'''
			fingerListLeft = [(0, 1, 2), 
								(3, 4, 5), 
								(6, 7, 8), 
								(9, 10, 11), 
								(12, 13, 14)]
			fingerListRight = [(15, 16, 17), 
								(18, 19, 20), 
								(21, 22, 23), 
								(24, 25, 26), 
								(27, 28, 29)]
			#print fingerListRight
			''' 
			
			
			
			#L4 and R0 are thumbs
			'''
			message = start + struct.pack("<BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
				fingerListLeft[0][0],
				fingerListLeft[0][1],
				fingerListLeft[0][2],
				fingerListLeft[1][0],
				fingerListLeft[1][1],
				fingerListLeft[1][2],
				fingerListLeft[2][0],
				fingerListLeft[2][1],
				fingerListLeft[2][2],
				fingerListLeft[3][0],
				fingerListLeft[3][1],
				fingerListLeft[3][2],
				fingerListLeft[4][0],
				fingerListLeft[4][1],
				fingerListLeft[4][2],
				fingerListRight[0][0],
				fingerListRight[0][1],
				fingerListRight[0][2],
				fingerListRight[1][0],
				fingerListRight[1][1],
				fingerListRight[1][2],
				fingerListRight[2][0],
				fingerListRight[2][1],
				fingerListRight[2][2],
				fingerListRight[3][0],
				fingerListRight[3][1],
				fingerListRight[3][2],
				fingerListRight[4][0],
				fingerListRight[4][1],
				fingerListRight[4][2],) + end
			ser.write(message)	
			
			print ser.read()
			'''
				
		
		if len(extended_fingers) != 0:
			simulator = resetSim()
			if len(fingerListLeft) > 0:
				for indexL, thisFingL in enumerate(fingerListLeft):
					if thisFingL[1] < 22 and thisFingL[0] < 11:
						simulator[thisFingL[1]][thisFingL[0]] = 1 #indexL
			if len(fingerListRight) > 0:
				for indexR, thisFingR in enumerate(fingerListRight):
					if thisFingR[1] < 22 and thisFingR[0] < 11:
						simulator[thisFingR[1]][thisFingR[0]] = 1 #indexR+5
					
			
			#print '\n\n\n\n', simulator
			
			simulator = resetSim()
		
			
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
