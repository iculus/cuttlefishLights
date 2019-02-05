import serial, struct, sys
from numpy import interp, zeros, chararray, reshape, append, array, roll
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess

start = chr(255)
end = chr(254)

def startProcess():
	p = subprocess.Popen(['./findDevicePath.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="/home/admin/Desktop/cuttlefishLights/utils")
	out, err = p.communicate()
	return out

def sendIt(sim, numFings, ser, bright):
	#print ser.read()
	toSend = sim.T
	toSend = toSend.reshape(242)

	#add the numfings to the end of the message
	toSend = append(toSend,numFings) 

	#add the brightness to the end of the message
	toSend = append(toSend,bright)

	#build struct and send messa
	message = start+struct.pack("<244B", *toSend)+end
	ser.write(message)

def setupSerial():

	result = startProcess()
	if "Leonardo" in result: 
		dev,name = result.split('-')

	ser = serial.Serial(port = str(dev.strip(' ')), baudrate = 115200,timeout = 0)

	try:
		if(ser.isOpen() != False):
			print 'Serial Port Open'
		if(ser.isOpen() == False):
			ser.open()
			print 'its not open'
	except IOError: # if port is already opened, close it and open it again and print message
		print 'error'
		ser.close()
		ser.open()
	return ser
