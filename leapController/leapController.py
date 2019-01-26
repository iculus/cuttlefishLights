#!/usr/bin/python

import os, signal, sys, inspect, thread, time, random, struct
		
LIB_DIR = "/home/admin/Desktop/LeapDeveloperKit_2.3.1+31549_linux/LeapSDK/lib"
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '/x64'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, LIB_DIR + arch_dir)))
sys.path.insert(0, LIB_DIR)
sys.path.insert(0,'/home/admin/Desktop/cuttlefishLights/leapController/')
sys.path.insert(0,'/usr/lib/python2.7')

import Leap 

from patterns import heart, dot, diagonalLine, chevronLine
from sercoms import sendIt, setupSerial
from procCtl import setupProcess, killProcess
from calibrate import returnCalibratedPosition

from numpy import interp, zeros, chararray, reshape, append, array, roll

import zmq

# setup area #
#physical object dimensions
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

pixelRow = pixelCol = 0
count = 0
maxCount = 22

fingerListLeft = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
fingerListRight = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

#for publishing
port = "5556"
# end of setup area #

#start = chr(255)
#end = chr(254)

#pidList = []

'''
def set_procname(newname):
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(len(newname)+1) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.
'''

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

	def on_device_change(self, controller):
		print "Device change"
	
	def on_device_failure(self, controller):
		print "Failure"

	def on_diagnostic_event(self, controller):
		print "Diagnositc Event"

	def on_disconnect(self, controller):
		# Note: not dispatched when running in a debugger.
		print "Disconnected"		
	
	def on_exit(self, controller):
		killProcess('leapd')
		print "Exited"

	def on_focus_gained(self, controller):
		print "Focused"

	def on_focus_lost(self, controller):
		print "Unfocused"

	def on_init(self, controller):
		print "Initialized"
		print "starting Leap Service"
		setupProcess("leapd", "sudo leapd &") 

	def on_service_change(self, controller):
		print "change", 

	def on_service_disconnect(self, controller):
		print "Lost Connection"
		print "starting Leap Service"
		setupProcess("leapd", "sudo leapd &")
	
	def on_service_connect(self, controller):
		print "Connection Gained"
		
	
	def on_frame(self, controller):
		'''
		simulator = resetSim()
		simulator2 = resetSim2()
		simulator3 = diagonalLine()
		simulator4 = chevronLine()
		'''
		frame = controller.frame() 
		extended_fingers = frame.fingers.extended()
		hands = frame.hands
		
		numFing = len(extended_fingers)
		
		allFings = resetFings()
		
		for f in extended_fingers:
		
			thisRow = returnCalibratedPosition(
				f.stabilized_tip_position[0],LeapRowMin,LeapRowMax,M0RowMin,M0RowMax)
			thisCol = returnCalibratedPosition(
				f.stabilized_tip_position[1],LeapColMin,LeapColMax,M0ColMin,M0ColMax)
			thisZ = returnCalibratedPosition(
				f.stabilized_tip_position[2],LeapZMin,LeapZMax,M0ZMin,M0ZMax)
		
			
			if f.hand.is_left:
				allFings[f.type] = (thisRow,thisCol,thisZ)
			if f.hand.is_right:
				allFings[f.type+5] = (thisRow,thisCol,thisZ)	

		topic = 10001
		messagedata = int(numFing)
		print "%d %d" % (topic, messagedata)
		socket.send("%d %d" % (topic, messagedata))		
		
		'''
		if numFing == 0:
			
			global count
			option = random.randrange(3)
			option = 2
			
			if option == 0:
				#update
				count = count + 1
				if count >= maxCount:count = 0			
		
				#reshape
				simulator3=roll(simulator3, count,0)
				#print simulator3

				#show
				sendIt(simulator3, numFing, ser)

			if option == 1:
				#update
				count = count + 1
				if count >= maxCount:count = 0			
		
				#reshape
				simulator4=roll(simulator4, count,1)
				#print simulator4

				#show
				sendIt(simulator4, numFing, ser)

			if option == 2:
				#update
				count = count + 1
				if count >= maxCount:count = 0			
		
				#reshape
				simulator4=roll(simulator4, count,0)
				#print simulator4

				#show
				sendIt(simulator4, numFing, ser)


		if numFing !=0:
			for fingDex, thisFing in enumerate(allFings):
				
				if thisFing[1]<22 and thisFing[1]>=0 and thisFing[0]<11 and thisFing[0]>=0:
					simulator[thisFing[1]][thisFing[0]] = fingDex+1
				elif thisFing[1]>= 22: print "condition 22"
				elif thisFing[0]>= 11: print "condition 11"
			
				simulator[pixelRow][pixelCol] = fingDex+1
				simulator2[pixelRow][pixelCol] = fingDex+1


			#print '\n\n\n\n', simulator
					
			sendIt(simulator, numFing, ser)
		'''

def main():
	#init messaging
	global socket
	context = zmq.Context()
	socket = context.socket(zmq.PUB)
	socket.bind("tcp://*:%s" % port)
	#count = 0

	#init serial
	global ser
	ser = setupSerial()
	#set_procname("crystalz")

	#init leap
	listener = SampleListener()
	controller = Leap.Controller()
	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	while True: 
		pass

if __name__ == "__main__":
	killProcess("leapd")
	main()
